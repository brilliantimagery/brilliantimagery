# distutils: language=c++
#cython: auto_pickle=True

from libcpp cimport bool
from libcpp.map cimport map as cpp_map
from libcpp.vector cimport vector as cpp_vector
from libcpp.string cimport string as cpp_string
# from libcpp.iterator cimport iterator as cpp_iterator
from cython.operator cimport dereference, postincrement

import numpy as np
import cython
import subprocess

cdef int SOF0 = 0xFFC0  # not implimented
cdef int SOF3 = 0xFFC3

cdef int SOI = 0xFFD8    # Start of image

cdef int SOS = 0xFFDA  # Start of scan
cdef int DQT = 0xFFDB  # Define quantization table(s)
cdef int DHT = 0xFFC4  # Define Huffman table(s)

cdef int EOI = 0xFFD9  # End of image

cdef int X
cdef int Y
cdef int n_components       # Nx
cdef int precision          # P

cdef cpp_map[int, cpp_map[cpp_string, int]] huffman_tables
cdef int[:] max_huffman_code_lengths = np.zeros(4, dtype=np.intc)
cdef int[:] min_huffman_code_lengths = np.zeros(4, dtype=np.intc)
cdef int rd_index
cdef int bit_rd_index
cdef int[:,:,:] raw_image

def decode(int[:] encoded_image):
    """
    Decode a Lossless Jpeg according to the 1992 standard T.81, 10918.1, 
    into its raw components.

    :param image: A 1D Numpy array holding the compressed image. 
    "image" can be created with something like 
    np.fromfile('F-18.ljpg', np.uint8).astype(np.intc), 
    note the "astype" at the end
    :return: A 3 dimensional Numpy array with index 1 being the color channel, 
    index 2 being the X coordinate, and index 3 being the Y coordinate.
    """
    global rd_index, bit_rd_index, raw_image

    cdef int marker
    rd_index = 0
    bit_rd_index = 0
    # cdef cpp_map[int, cpp_map[cpp_string, int]] huffman_tables_reset
    # huffman_tables = huffman_tables_reset

    cdef Py_ssize_t rd_index_length = encoded_image.shape[0]

    while rd_index < rd_index_length:
        marker = __bytes_to_int(encoded_image[rd_index:rd_index + 2])
        if marker > 0xFF00:
            rd_index += 2
            __parse_marker(encoded_image, marker)
        else:
            rd_index += 1

    return raw_image.base


cdef int __parse_marker(int[:] encoded_image, int marker):
    if marker == SOI:
        pass
    elif marker == SOF0:
        pass
        # throw new UnknownUnsupportedFieldOrMarkerException(
        # "Unsupport Jpeg compression in " + Jpeg.class.getName());
    elif marker == SOF3:
        __get_frame_header_info(encoded_image)
    elif marker == DHT:
        __get_huffman_table_info(encoded_image)
    elif marker == SOS:
        __get_scan_header_info(encoded_image)


cdef void __get_frame_header_info(int[:] encoded_image):
    # see 10918-1 T.81 section B.2.2 Page 35
    global raw_image, rd_index, precision, X, Y, n_components#, Hi, Vi, Tqi#, HiViTqi

    cdef int Lf = __bytes_to_int(encoded_image[rd_index:rd_index + 2])
    rd_index += 2
    precision = encoded_image[rd_index]
    rd_index += 1
    Y = __bytes_to_int(encoded_image[rd_index:rd_index + 2])
    rd_index += 2
    X = __bytes_to_int(encoded_image[rd_index:rd_index + 2])
    rd_index += 2
    n_components = encoded_image[rd_index]
    rd_index += 1

    for i in range(rd_index, rd_index + n_components * 3, 3):
        # _ci = encoded_image[i]
        if (encoded_image[i + 1] >> 4) is not 1:
            raise Exception('Pixels are the wrong shape, Hi')
        if (encoded_image[i + 1] & 0xF) is not 1:
            raise Exception('Pixels are the wrong shape, Vi')
        if (encoded_image[i + 2]) is not 0:
            raise Exception('Tqi should be 0')

    raw_image = np.zeros((n_components, X, Y), dtype=np.int32)

    rd_index += n_components * 3


cdef void __get_huffman_table_info(int[:] encoded_image):
    # see 10918-1 T.81 section B.2.4.2 Page 40
    global rd_index, huffman_tables, max_huffman_code_lengths, max_huffman_code_lengths

    cdef int Lh = __bytes_to_int(encoded_image[rd_index:rd_index + 2])
    rd_index += 2
    # cdef int Tc = encoded_image[rd_index] >> 4
    cdef int Th = encoded_image[rd_index] & 0xF
    rd_index += 1

    cdef int vij_index = rd_index + 16
    cdef int count_of_code_length_index
    cdef int _
    cdef int Li
    cdef int[:, :] code_lengths = np.full((16, 16), -1, dtype=np.intc)
    cdef int n_codes

    for count_of_code_length_index in range(rd_index, rd_index + 16):
        Li = encoded_image[count_of_code_length_index]
        if Li:
            n_codes = 0
            for _ in range(Li):
                code_lengths[count_of_code_length_index - rd_index, n_codes] = encoded_image[vij_index]
                n_codes += 1
                vij_index += 1

    cdef cpp_map[cpp_string, int] huff_table = __make_ssss_table(code_lengths)
    huffman_tables[Th] = huff_table
    min_huffman_code_lengths[Th] = 100
    max_huffman_code_lengths[Th] = 0
    cdef int code_length
    cdef cpp_map[cpp_string, int].iterator it = huff_table.begin()
    while it != huff_table.end():
        code_length = dereference(it).first.size()
        if code_length > max_huffman_code_lengths[Th]:
            max_huffman_code_lengths[Th] = code_length
        if code_length < min_huffman_code_lengths[Th]:
            min_huffman_code_lengths[Th] = code_length
        postincrement(it)

    rd_index = vij_index


cdef void __get_scan_header_info(int[:] encoded_image):
    # see 10918-1 T.81 section B.2.3 Page 37
    # global rd_index, n_components, Tdj, Taj, Ss, Se, Ah, Al
    global rd_index, n_components

    cdef int index
    cdef int Ls = __bytes_to_int(encoded_image[rd_index:rd_index + 2])
    rd_index += 2
    # n_components = encoded_image[rd_index]
    rd_index += 1
    cdef int _ci
    cdef int Tdj
    cdef int predictor          # Ss
    cdef int point_transform    # Al
    for index in range(rd_index, rd_index + n_components * 2, 2):
        _ci = encoded_image[index]
        Tdj = encoded_image[index + 1] >> 4
        if _ci is not Tdj:
            raise Exception('Tdj does not equal Ci')
        # Taj[_ci] = encoded_image[index + 1] & 0xF
    rd_index += n_components * 2
    predictor = encoded_image[rd_index]
    rd_index += 1
    # Se = encoded_image[rd_index]
    rd_index += 1
    # Ah = encoded_image[i + 1] >> 4
    # point_transform = encoded_image[index + 1] & 0xF
    point_transform = encoded_image[rd_index] & 0xF
    rd_index += 1

    __decode_scan(encoded_image, predictor, point_transform)


cdef void __decode_scan(int[:] encoded_image, int predictor, int point_transform):
    global raw_image

    cdef int width = X
    cdef int height = Y

    cdef int write_index = 0        # write index of the decompressed image data
    cdef int bit_read_index = 0     # bit read index in image data bits

    cdef int x
    cdef int y
    cdef int component

    cdef int px
    cdef int actual_vs_predicted_pixel_diff = 0
    cdef int P = precision

    cdef int[:] img_bits = __get_image_bits(encoded_image)
    cdef Py_ssize_t length = img_bits.shape[0]
    cdef int n_pix = width * height

    cdef int[:] context = np.zeros(6, dtype=np.intc)

    while write_index < n_pix:
        for component in range(n_components):
            x = write_index % width
            y = write_index // width
            context = __get_context(component, x, y, context, point_transform, P, raw_image)
            px = __get_predicted_value(write_index, context, predictor, width)
            actual_vs_predicted_pixel_diff = __get_huffmaned_value(component,
                                                                   actual_vs_predicted_pixel_diff,
                                                                   img_bits)
            raw_image[component, x, y] = (px + actual_vs_predicted_pixel_diff) & ((1 << P) - 1)
        write_index += 1


cdef inline int __get_huffmaned_value(int component, int actual_vs_predicted_pixel_diff, int[:] img_bits):
    # global actual_vs_predicted_pixel_diff
    global bit_rd_index

    cdef int jj = bit_rd_index

    # cdef int max_huffman_code_length = huff_table['max_length']
    cdef int start_j = jj
    cdef unsigned int ssss = -1
    cdef int first_bit
    cdef int _
    cdef cpp_map[cpp_string, int] huff_table = huffman_tables[component]

    cdef int end_j
    cdef cpp_string guess = ''

    # TODO: should if break or be error resistant? also goes for down below

    # TODO: don't know if it should be start_j + max_huffman_code_length + 1 or start_j + max_huffman_code_length
    for jj in range(jj, jj + min_huffman_code_lengths[component] - 1):
        guess.push_back(img_bits[jj])
    for jj in range(start_j + min_huffman_code_lengths[component] - 1,
                    start_j + max_huffman_code_lengths[component] + 1):
        guess.push_back(img_bits[jj])
        if huff_table.count(guess):
            ssss = huff_table[guess]
            break
    jj += 1

    # if no code is matched return a zero, this was said to be the safest somewhere
    if ssss == -1:
        # print('No matching Huffman code was found')
        # print('guess', guess, jj)
        # print(huff_table_table)
        # exit(10)
        pass
        # throw Error
    elif ssss == 16:
        # ssss 16 doesn't read extra bits, it just returns 32768
        actual_vs_predicted_pixel_diff = 32768
    else:
        actual_vs_predicted_pixel_diff = 0
        if ssss > 0:
            first_bit = img_bits[jj]
            # step thru the ssss number of bits to get the coded number
            for jj in range(jj, jj+ssss):
                actual_vs_predicted_pixel_diff = (actual_vs_predicted_pixel_diff << 1) | img_bits[jj]
            # if the first read bit is 0 the number is negative and has to be calculated
            if first_bit == 0:
                actual_vs_predicted_pixel_diff = -(1 << ssss) + actual_vs_predicted_pixel_diff + 1
            jj += 1
    bit_rd_index = jj
    return actual_vs_predicted_pixel_diff


cdef int[:] __get_context(int component, int x, int y, int[:] context, int point_transform, int P, int[:,:,:] img):

    cdef int a = 0
    cdef int b = 0
    cdef int c = 0
    cdef int ix = img[component, x, y]

    if y is 0:
        if x is 0:
            a = 1 << (P - point_transform - 1)
        else:
            a = img[component, x - 1, y]
    else:
        if x is not 0:
            a = img[component, x - 1, y]
            c = img[component, x - 1, y - 1]
        b = img[component, x, y - 1]

    context[0] = x
    context[1] = a
    context[2] = b
    context[3] = c
    context[4] = ix

    return context


cdef int __get_predicted_value(int x, int[:] context, int predictor, int width):
    # see 10918-1 T.81 section H.1.2.1 Page 132

    cdef int used_predictor = 0
    if x < width:
        used_predictor = 1
    elif x % width == 0:
        used_predictor = 2
    else:
        used_predictor = predictor

    if used_predictor == 0:
        return 0
    elif used_predictor == 1:
        return context[1]
    elif used_predictor == 2:
        return context[2]
    elif used_predictor == 3:
        return context[3]
    elif used_predictor == 4:
        return context[1] + context[2] - context[3]
    elif used_predictor == 5:
        return context[1] + ((context[2] - context[3]) >> 1)
    elif used_predictor == 6:
        return context[2] + ((context[1] - context[3]) >> 1)
    elif used_predictor == 7:
        return (context[1] + context[2]) // 2


cdef int[:] __get_image_bits(int[:] encoded_image):
    global rd_index

    # TODO: use instead of rd_index
    cdef int r_i = rd_index

    cdef int relitive_rd_index = 0
    cdef int[:] img = np.zeros_like(encoded_image)

    # TODO: shouldn't loop through everthing twice
    while True:
        if encoded_image[rd_index] < 0xff:
            img[relitive_rd_index] = encoded_image[rd_index]
            relitive_rd_index += 1
            rd_index += 1
        elif encoded_image[rd_index + 1] == 0:
            img[relitive_rd_index] = encoded_image[rd_index]
            relitive_rd_index += 1
            rd_index += 2
        else:
            # Hit the end of the section
            break

    cdef int[:] bits = np.zeros((relitive_rd_index * 8), np.intc)


    cdef int byte_index
    for byte_index in range(relitive_rd_index):
        bits[byte_index * 8] = (img[byte_index] >> 7) & 1
        bits[byte_index * 8 + 1] = (img[byte_index] >> 6) & 1
        bits[byte_index * 8 + 2] = (img[byte_index] >> 5) & 1
        bits[byte_index * 8 + 3] = (img[byte_index] >> 4) & 1
        bits[byte_index * 8 + 4] = (img[byte_index] >> 3) & 1
        bits[byte_index * 8 + 5] = (img[byte_index] >> 2) & 1
        bits[byte_index * 8 + 6] = (img[byte_index] >> 1) & 1
        bits[byte_index * 8 + 7] = img[byte_index] & 1

    return bits


cdef cpp_map[cpp_string, int] __make_ssss_table(int[:, :] code_lengths):

    cdef cpp_string code = ''
    cdef int valuesWNBits = 0

    # table = {}
    cdef cpp_map[cpp_string, int] table
    cdef bool has_all_ones_code = False
    cdef int index
    cdef int _
    cdef cpp_string removed

    for index in range(0, 16):
        if code_lengths[index, 0] > -1:
            values = [a for a in np.asarray(code_lengths[index]) if a > -1]
            valuesWNBits = 0
            while valuesWNBits <= len(values):
                while code.size() < index + 1:
                    code.push_back(0)

                if valuesWNBits:
                    while True:
                        removed = code.substr(code.size() - 1, code.size())
                        code = code.substr(0, code.size() - 1);
                        if not (removed == b'\x01' and code.size() > 0):
                            break
                    code.push_back(1)
                    for _ in range(code.size(), index + 1):
                        code.push_back(0)

                if values and len(values) > valuesWNBits:
                    table[code] = values[valuesWNBits]

                valuesWNBits += 1

    return table


cdef int __bytes_to_int(int[:] bytes):
    cdef int result = 0
    cdef int i

    for i in range(bytes.shape[0]):
        result = (result << 8) + bytes[i]

    return result

#cython: profile=True
#cython: linetrace=True