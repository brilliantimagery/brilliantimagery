import struct
from typing import Any, List, Optional, Tuple, Union


def get_xmp_attribute_value(xmp_buffer: bytes, xmp_attribute: bytes) -> Optional[str]:
    """
    Get the value of an xmp attribute

    Searches the given xmp buffer for the given attribute.
    Assumes the buffer to be of format:
    b'crs:Tint="+10".   crs:Saturation="+9"' or
    b'crs:Tint<+10>.   crs:Saturation<+9>'

    Does not test to ensure inputs are of the correct datatype.
    :param xmp_buffer: The xmp data as bytes
    :param xmp_attribute: The attribute as bytes
    :return: the value, with sign if present, as a string or None if
    not found.
    """
    value_start = xmp_buffer.find(xmp_attribute)
    if value_start < 0:
        return None

    value_start += len(xmp_attribute)
    uses_equals_sign = xmp_buffer[value_start] == ord('=')

    if uses_equals_sign:
        value_start += 2
        value_end = xmp_buffer.find(b'"', value_start)
    else:
        value_start += 1
        value_end = xmp_buffer.find(b'<', value_start)

    return xmp_buffer[value_start:value_end].decode('utf-8')


def renderd_area_bounding_box(bounding_box: List, x0, y0, x1, y1) -> List:
    """
    Finds the smallest bounding box.

    Compares the input bounding box to the input values to see if they
    fall inside or outside the bounding box and make the box bigger
    as needed to encompass all the values
    :param bounding_box: A bounding box that's to be compared to the
    other values
    In the format X1, Y1, X2, Y2 where:
    x0 is the x position of the top left corner,
    y0 is the y position of the top left corner,
    x1 is the x position of the bottom right corner,
    y1 is the y position of the top right corner.
    :param x0: Left edge to be compares
    :param y0: Top edge to be compares
    :param x1: Right edge to be compares
    :param y1: Bottom edge to be compares
    :return: an updated bounding box to encompass the bounding box
    and all of the values.
    """
    if bounding_box:
        bounding_box[0] = min(bounding_box[0], x0)
        bounding_box[1] = min(bounding_box[1], y0)
        bounding_box[2] = max(bounding_box[2], x1)
        bounding_box[3] = max(bounding_box[3], y1)
    else:
        bounding_box = [x0, y0, x1, y1]

    return bounding_box


def convert_rectangle_percent_to_pixels(ifd, rectangle, left_crop, top_crop, right_crop, bottom_crop,
                                        sub_image_type='RAW') -> \
        Tuple[List[int], Tuple[Union[int, Any], Union[int, Any]]]:
    """
    Reformats the rectangle into absolute pixel terms.

    Converts the rectangle that's to be rendered from being in units of
    percent to units of pixels, changes the origin from being that of
    the top left corner of the crop to that of the ActiveArea, and
    ensures that that the perimeter of the rectangle falls along
    boundaries of the bayer mask, CFAPattern.
    :param ifd: The IFD formatted data containing the rendering info
    :param rectangle: The input rectangle as a list
    :param left_crop: Left crop percentage
    :param top_crop: Top crop percentage
    :param right_crop: Right crop percentage
    :param bottom_crop: Bottom crop percentage
    :param sub_image_type: Type of image: RAW or thumbnail
    :return: The reformatted rectangle as a list
    """
    if rectangle[0] < 1 or rectangle[1] < 1 or rectangle[1] < 1 or rectangle[1] < 1:
        if sub_image_type.lower() == 'raw':
            cropped_width = ifd['default_crop_size'][0] * (right_crop - left_crop)
            cropped_length = ifd['default_crop_size'][1] * (bottom_crop - top_crop)

            left_edge = int(ifd['active_area'][1] + ifd['default_crop_origin'][0]
                            + rectangle[0]*cropped_width + left_crop*ifd['default_crop_size'][0])
            right_edge = int(left_edge + (rectangle[2]-rectangle[0])*cropped_width)
            top_edge = int(ifd['active_area'][0] + ifd['default_crop_origin'][1]
                           + rectangle[1]*cropped_length + top_crop*ifd['default_crop_size'][1])
            bottom_edge = int(top_edge + (rectangle[3] - rectangle[1]) * cropped_length)
        elif sub_image_type.lower() == 'thumbnail':
            left_edge = int(ifd['image_width'] * rectangle[0])
            top_edge = int(ifd['image_length'] * rectangle[1])
            right_edge = int(ifd['image_width'] * rectangle[2])
            bottom_edge = int(ifd['image_length'] * rectangle[3])

        rectangle[0] = left_edge
        rectangle[1] = top_edge
        rectangle[2] = right_edge
        rectangle[3] = bottom_edge

    return rectangle


def get_active_area_offset(ifd, rectangle, sub_image_type='RAW'):
    if sub_image_type.lower() == 'raw':
        left_edge, top_edge, right_edge, bottom_edge = rectangle

        return left_edge - ifd['active_area'][1], top_edge - ifd['active_area'][0]
    elif sub_image_type.lower() == 'thumbnail':
        return 0, 0


def get_value_from_type(buffer, field_type, _byte_order, is_string=False):
    """
    Finds the value of the input buffer given the type of the field.

    Since data
    :param buffer:
    :param field_type:
    :param _byte_order:
    :param is_string:
    :return:
    """
    val = _get_value_from_type_format(struct.unpack, buffer, field_type, _byte_order, is_string)[0]
    return val


def get_values_from_type(buffer, field_type, _byte_order, is_string=False) -> List:
    val = _get_value_from_type_format(struct.iter_unpack, buffer, field_type, _byte_order, is_string)
    val = [v[0] for v in val]
    return val


def _get_value_from_type_format(unpacking_function, buffer, field_type, _byte_order, is_string):
    if field_type == 1:
        if is_string:
            return [buffer, ]
        return unpacking_function(f'{_byte_order}B', buffer)
    if field_type == 2:
        return buffer.decode('utf-8')
    if field_type == 3:
        return unpacking_function(f'{_byte_order}H', buffer)
    if field_type == 4:
        return unpacking_function(f'{_byte_order}I', buffer)
    if field_type == 5:
        numbs = list(struct.iter_unpack(f'{_byte_order}I', buffer))
        output = []
        for i in range(0, len(numbs), 2):
            try:
                output.append([numbs[i][0]/numbs[i+1][0],])
            except:
                pass
        return output
    if field_type == 6:
        return unpacking_function(f'{_byte_order}b', buffer)
    if field_type == 7:
        if is_string:
            return [buffer, ]
        return buffer.decode('ascii')
        # assert (False)
    if field_type == 8:
        return unpacking_function(f'{_byte_order}h', buffer)
    if field_type == 9:
        return unpacking_function(f'{_byte_order}i', buffer)
    if field_type == 10:
        numbs = list(struct.iter_unpack(f'{_byte_order}i', buffer))
        output = []
        for i in range(0, len(numbs), 2):
            try:
                output.append([numbs[i][0]/numbs[i+1][0],])
            except:
                pass
        return output
    if field_type == 11:
        return unpacking_function(f'{_byte_order}f', buffer)
    if field_type == 12:
        return unpacking_function(f'{_byte_order}d', buffer)


def get_num_of_bytes_in_type(field_type) -> int:
    if field_type == 1 or field_type == 2 or field_type == 6 or field_type == 7:
        return 1
    elif field_type == 3 or field_type == 8:
        return 2
    elif field_type == 4 or field_type == 9 or field_type == 11:
        return 4
    elif field_type == 5 or field_type == 10 or field_type == 12:
        return 8
    else:
        return 0
