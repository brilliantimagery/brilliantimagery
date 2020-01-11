# distutils: language=c++
import numpy as np
import cython

cdef int SOF0 = 0xFFC0  # not implimented
cdef int SOF3 = 0xFFC3

cdef int SOI = 0xFFD8    # Start of image

cdef int SOS = 0xFFDA  # Start of scan
cdef int DQT = 0xFFDB  # Define quantization table(s)
cdef int DHT = 0xFFC4  # Define Huffman table(s)

cdef int EOI = 0xFFD9  # End of image


cdef int rd_index = 0      # current read index, byte index for decoding, bit index for encoding
cdef int[:, :, :] raw_image      # raw image in [x, y, component] format
cdef int[:] encoded_image       # encoded image including headers

# # Scan Header
cdef int Ns = 0    # Number of image components (color channels)
cdef int Ss = 0    # Start of spectral or predictor selection
cdef int Al = 0    # Successive approx bit position low or point transform

cdef int P = 0


def encode(int[:, :, :] image, int precision, int predictor) -> int[:]:
    """
    Encode a raw image into a Lossless Jpeg according to the 1992 standard 
    T.81, 10918.1.

    This is neither highly optimized nor heavily tested.
    
    :param image: A 3 dimensional Numpy array with index 0 being the color
        channel, index 1 being the X coordinate, and index 2 being the Y
        coordinate.
    :param precision: The number of bits of precision for each color value. 
        This can be different from the number of bits of precision used by the
        array holding the values.
    :param predictor: The predictor, Ss from the Jpeg standard, to be used.
    :return: A compressed Lossless Jpeg as a MemoryView to a 1D Numpy array.
    """
    global encoded_image, raw_image, Ns, rd_index, Ss, P, Al

    raw_image = image
    encoded_image = np.zeros(raw_image.size, dtype=np.intc)
    rd_index = 0

    Ss = predictor
    Ns = raw_image.shape[0]
    P = precision
    Al = 0

    _write_frame_info(P)
    huff_codes, actual_vs_predicted_diffs = _make_huffman_info()
    _write_SOS(huff_codes, actual_vs_predicted_diffs)

    while rd_index % 8 is not 0:
        rd_index += 1

    encoded_image = _int_into_array(encoded_image, EOI, 16)
    encoded_image = encoded_image[:rd_index // 8]

    return encoded_image.base


cdef _write_frame_info(int P):
    global encoded_image

    encoded_image = _int_into_array(encoded_image, SOI, 16)

    encoded_image = _int_into_array(encoded_image, SOF3, 16)
    encoded_image = _int_into_array(encoded_image, 8 + 3 * Ns, 16)
    encoded_image = _int_into_array(encoded_image, P, 8)
    encoded_image = _int_into_array(encoded_image, raw_image.shape[2], 16)
    encoded_image = _int_into_array(encoded_image, raw_image.shape[1], 16)
    encoded_image = _int_into_array(encoded_image, Ns, 8)

    cdef int i
    for i in range(Ns):
        encoded_image = _int_into_array(encoded_image, i, 8)
        encoded_image = _int_into_array(encoded_image, 1, 4)
        encoded_image = _int_into_array(encoded_image, 1, 4)
        encoded_image = _int_into_array(encoded_image, 0, 8)


cdef _make_huffman_info():
    global width, height, actual_predicted_pixel_diff

    cdef int write_index = 0  # write index of the decompressed image data

    cdef int x      # X location that's being processed
    cdef int y      # Y location that's being processed
    cdef int component
    cdef int px

    width = raw_image.shape[1]
    height = raw_image.shape[2]
    cdef int n_pix_in_image = width * height

    cdef int[:] context = np.zeros(6, dtype=np.intc)
    # cdef int[:] context = array(6, dtype=np.intc)
    cdef int[:, :, :] actual_vs_predicted_diffs = np.zeros((Ns, width, height), dtype=np.intc)
    cdef int[:, :] diff_precision_freques = np.zeros((17, 3), dtype=np.intc)

    while write_index < n_pix_in_image:
        for component in range(Ns):
            x = write_index % width
            y = write_index // width
            context = _get_context(component, x, y, context)
            px = _get_predicted_value(write_index, context)
            actual_predicted_pixel_diff = raw_image[component, x, y] - px
            diff_precision_freques[_get_ssss(actual_predicted_pixel_diff), component] += 1
            actual_vs_predicted_diffs[component, x, y] = actual_predicted_pixel_diff
        write_index += 1

    huff_codes = []
    for component in range(Ns):
        huff_codes.append(_build_codes(diff_precision_freques[:, component]))

    huff_tables = []
    for code in huff_codes:
        huff_tables.append(_build_tables(code))

    _write_huff_tables(huff_tables)
    return huff_codes, actual_vs_predicted_diffs


cdef int[:] _get_context(int component, int x, int y, int[:] context):

    cdef int a = 0
    cdef int b = 0
    cdef int c = 0
    cdef int ix = raw_image[component, x, y]

    if y is 0:
        if x is 0:
            a = 1 << (P - Al - 1)
        else:
            a = raw_image[component, x - 1, y]
    else:
        if x is not 0:
            a = raw_image[component, x - 1, y]
            c = raw_image[component, x - 1, y - 1]
        b = raw_image[component, x, y - 1]

    context[0] = x
    context[1] = a
    context[2] = b
    context[3] = c
    context[4] = ix

    return context


cdef int _get_predicted_value(int x, int[:] context):
    # see 10918-1 T.81 section H.1.2.1 Page 132

    cdef int predictor = 0
    if x < width:
        predictor = 1
    elif x % width == 0:
        predictor = 2
    else:
        predictor = Ss

    if predictor == 0:
        return 0
    elif predictor == 1:
        return context[1]
    elif predictor == 2:
        return context[2]
    elif predictor == 3:
        return context[3]
    elif predictor == 4:
        return context[1] + context[2] - context[3]
    elif predictor == 5:
        return context[1] + ((context[2] - context[3]) >> 1)
    elif predictor == 6:
        return context[2] + ((context[1] - context[3]) >> 1)
    elif predictor == 7:
        return (context[1] + context[2]) // 2


cdef int _get_ssss(int numb):
    """Table H.2, P. 134"""

    if numb == 0:
        return 0
    elif -1 <= numb <= 1:
        return 1
    elif -3 <= numb <= 3:
        return 2
    elif -7 <= numb <= 7:
        return 3
    elif -15 <= numb <= 15:
        return 4
    elif -31 <= numb <= 31:
        return 5
    elif -63 <= numb <= 63:
        return 6
    elif -127 <= numb <= 127:
        return 7
    elif -255 <= numb <= 255:
        return 8
    elif -511 <= numb <= 511:
        return 9
    elif -1023 <= numb <= 1023:
        return 10
    elif -2047 <= numb <= 2047:
        return 11
    elif -4095 <= numb <= 4095:
        return 12
    elif -8191 <= numb <= 8191:
        return 13
    elif -16383 <= numb <= 16383:
        return 14
    elif -32767 <= numb <= 32767:
        return 15
    elif numb == 32768:
        return 16


cdef _write_SOS(codes, actual_vs_predicted_diffs):
    global rd_index, encoded_image

    cdef int x
    cdef int y
    cdef int component # TODO: component
    cdef int actual_vs_predicted_pixel_diff
    cdef int ssss                           # The required precision to hold actual_vs_predicted_pixel_diff

    encoded_image = _int_into_array(encoded_image, SOS, 16)
    encoded_image = _int_into_array(encoded_image, 6 + Ns * 2, 16)
    encoded_image = _int_into_array(encoded_image, Ns, 8)
    for i in range(Ns):
        encoded_image = _int_into_array(encoded_image, i, 8)
        encoded_image = _int_into_array(encoded_image, i, 4)
        encoded_image = _int_into_array(encoded_image, 0, 4)
    encoded_image = _int_into_array(encoded_image, Ss, 8)
    encoded_image = _int_into_array(encoded_image, 0, 8)
    encoded_image = _int_into_array(encoded_image, 0, 4)
    encoded_image = _int_into_array(encoded_image, 0, 4)

    for y in range(height):
        for x in range(width):
            for component in range(Ns):
                actual_vs_predicted_pixel_diff = actual_vs_predicted_diffs[component, x, y]
                ssss = _get_ssss(actual_vs_predicted_pixel_diff)
                if actual_vs_predicted_pixel_diff < 0:
                    actual_vs_predicted_pixel_diff = actual_vs_predicted_pixel_diff + (1 << ssss) - 1
                encoded_image = _write_code_and_diff(encoded_image, codes[component][ssss],
                                                      actual_vs_predicted_pixel_diff, ssss)


cdef int[:] _write_code_and_diff(int[:] buffer, code, actual_vs_predicted_pixel_diff, n_bits):
    global rd_index

    cdef int byte_number
    cdef int bit_number

    for bit in code:
        byte_number = rd_index // 8
        bit_number = rd_index % 8
        if bit_number is 0 and buffer[byte_number - 1] is 0xFF:
            byte_number += 1
            rd_index += 8
        buffer[byte_number] = buffer[byte_number] | (bit << (7 - bit_number))
        rd_index += 1

    # TODO: consolidate with int_into_array

    cdef int bit_val
    for i in range(n_bits-1, -1, -1):
        byte_number = rd_index // 8
        bit_number = rd_index % 8
        bit_val = (actual_vs_predicted_pixel_diff >> i) & 1
        if bit_number is 0 and buffer[byte_number - 1] is 0xFF:
            byte_number += 1
            rd_index += 8
        buffer[byte_number] = buffer[byte_number] | (bit_val << (7 - bit_number))

        rd_index += 1

    return buffer


cdef int[:] _int_into_array(int[:] arr, int numb, int n_bits):
    global rd_index

    cdef int bit_val
    cdef int current_bit = n_bits - 1

    while current_bit > -1:
        bit_val = (numb & (1 << current_bit)) >> current_bit
        arr[rd_index // 8] = arr[rd_index // 8] | (bit_val << (7 - (rd_index % 8)))

        rd_index += 1
        current_bit -= 1

    return arr


cdef _build_codes(frequs):
    cdef list nodes = []
    cdef int n_bits

    for n_bits in range(frequs.shape[0]):
        if frequs[n_bits]:
            nodes.append({'n_bits': n_bits, 'freq': frequs[n_bits], 'left_branch': -1, 'right_branch': -1})

    cdef int node_count = len(nodes)

    cdef list treed_nodes = []
    cdef dict min1
    cdef dict min2

    while len(nodes) > 1:
        min1 = {}
        min2 = {}

        for node in nodes:
            if not min1 or min1['freq'] > node['freq']:
                min2 = min1
                min1 = node
            elif not min2 or min2['freq'] > node['freq']:
                min2 = node

        if min1['n_bits'] is not -1 and min2['n_bits'] is -1:
            holder = min1
            min1 = min2
            min2 = holder

        nodes.remove(min1)
        nodes.remove(min2)
        nodes.append({'n_bits': -1, 'freq': min1['freq'] + min2['freq'],
                      'left_branch': min2, 'right_branch': min1})

    cdef dict table = {}

    cdef list path = []
    path.append(nodes[0])
    cdef list code = []
    cdef int go_back = False
    cdef int go_right = False
    cdef int new_find = True
    cdef int found = 0

    cdef list new_code
    cdef int i

    last_key = 0

    while found < node_count:
        if path[-1]['n_bits'] is not -1 and new_find:
            new_code = []
            for i in code:
                new_code.append(i)
            if path[-1]['freq'] > 0:
                table[path[-1]['n_bits']] = new_code
                last_key = path[-1]['n_bits']
            go_back = True
            found += 1
            new_find = False
        else:
            if go_back:
                del path[-1]
                if code[-1] is 0:
                    go_right = True
                    go_back = False
                del code[-1]
            elif go_right:
                path.append(path[-1]['right_branch'])
                code.append(1)
                go_right = False
            else:
                path.append(path[-1]['left_branch'])
                code.append(0)
            new_find = True

    return table


cdef _build_tables(code):

    cdef dict output = {}

    for k, v in code.items():
        if len(v) in output:
            output[len(v)].append(k)
        else:
            output[len(v)] = [k]

    return output


cdef _write_huff_tables(tables):
    global encoded_image

    cdef int i = 0
    for table in tables:
        lq = 19
        for k, v in table.items():
            lq += len(v)
        encoded_image = _int_into_array(encoded_image, DHT, 16)
        encoded_image = _int_into_array(encoded_image, lq, 16)
        encoded_image = _int_into_array(encoded_image, 0, 4)
        encoded_image = _int_into_array(encoded_image, i, 4)
        for j in range(1, 17):
            if j in table:
                encoded_image = _int_into_array(encoded_image, len(table[j]), 8)
            else:
                encoded_image = _int_into_array(encoded_image, 0, 8)
        for k, v in table.items():
            for jj in v:
                encoded_image = _int_into_array(encoded_image, jj, 8)
        i += 1