import array
import math
import os
import platform
import struct
import sys

import numpy as np

from . import _dng_constants as dcnst
from . import _dng_utils as dutils
from . import _renderer
# from ljpeg import decode
# import ljpeg

class DNG:
    """
    A representation of a DNG image file.

    Based on the DNG 1.4 standard and not fully backwards compatible.

    Arguments:
        path (string): The path to an existing DNG file.

    Attributes:
        path (string): The path to the original DNG file.

    """

    class Field:
        """
        A TIFF Field as defigned by the TIFF6 standard.

        Arguments:
            tag (int): The tag number of the field
            type (int): The type number of the field
            count (int): The count of the field
            value_offset (int): The value of the field.
            Could be the offset to the value(s) depending on the type
            and count.
            values (list): The list of the fields values as
            preformatted data, it should be correct, actual field
            values Fields with 1 value should have it in a list of
            len 1.

        Attributes:
            tag (int): The tag number of the field
            type (int): The type number of the field
            count (int): The count of the field
            value_offset (int): The value of the field.
            Could be the offset to the value(s) depending on the type
            and count.
            values (list): The list of the fields values as
            preformatted data, it should be correct, actual field
            values Fields with 1 value should have it in a list of
            len 1.
        """

        def __init__(self, tag, type, count, value_offset, values=[]):
            self.tag = tag
            self.type = type
            self.count = count
            self.value_offset = value_offset
            self.values = values

        def __repr__(self):
            return f'{self.tag}, {self.type}, {self.count}, {self.value_offset}'

    _buffer_size = 50000000

    def __init__(self, path):
        """
        Initialize a DNG file representation.

        Test to make sure the input file is a valid DNG and read the
        beginning of the file so that it can be parsed.
        :param path: File name of the DNG file
        """
        self.path = path
        self._ifds = dict()
        self._used_fields = dict()
        self._xmp = dict()
        self._updated = False
        self._xmp_length_changed = False
        with open(self.path, 'rb', buffering=DNG._buffer_size) as f:
            self._byte_order = f.read(2)
            if self._byte_order == b'II':
                self._byte_order = '<'
            elif self._byte_order == b'MM':
                self._byte_order = '>'
            else:
                pass
                # TODO throw an error
            assert (struct.unpack(f'{self._byte_order}H', f.read(2))[0] == 42)
            self._zeroth_ifd = struct.unpack(f'{self._byte_order}H', f.read(2))[0]

    def get_capture_datetime(self):
        self._parse_ifds()
        self._get_idf_offsets()
        xmp = self._ifds[self._xmp_ifd_offset][700].values[0]
        capture_datetime = dutils.get_xmp_property_value(xmp, b'xmp:CreateDate')
        if capture_datetime:
            return capture_datetime
        else:
            """
                Try to get the date that a file was created, falling back to when it was
                last modified if that isn't possible.
                See http://stackoverflow.com/a/39501288/1709587 for explanation.
                """
            if platform.system() == 'Windows':
                return os.path.getctime(self.path)
            else:
                stat = os.stat(self.path)
                try:
                    return stat.st_birthtime
                except AttributeError:
                    # We're probably on Linux. No easy way to get creation dates here,
                    # so we'll settle for when its content was last modified.
                    return stat.st_mtime

    def _get_fields_required_to_render(self, sub_image):
        """
        Consolidate the required to render a DNG file.

        Consolidate the fields from throughout the file into a
        single IFD like structure holding all of the fields needed
        to render the desired image.
        :param sub_image: 'Thumbnail' or 'RAW' depending on which
        is to be rendered.
        :return: None
        """
        if sub_image is 'Thumbnail':
            offset = self._thumbnail_offset
        if sub_image is 'RAW':
            offset = self._orig_img_offset

        ifd = self._ifds[offset]
        plural_value_fields = {dcnst.DNG_TAGS[tag].name: ifd[tag].values
                               for tag, field in dcnst.DNG_TAGS.items()
                               if tag in ifd and field.is_multi_valued}
        single_value_fields = {dcnst.DNG_TAGS[tag].name: ifd[tag].values[0]
                               for tag, field in dcnst.DNG_TAGS.items()
                               if tag in ifd and not field.is_multi_valued}
        self._used_fields = {**plural_value_fields, **single_value_fields,
                             **{'orientation': self._ifds[self._thumbnail_offset][274].values[0]},
                             }
        #
        # if compression == 7:
        #     # print('compression test', bits_per_sample, [8, 8, 8], bits_per_sample == [8, 8, 8])
        #     if ((photometric_interpretation == 6 and bits_per_sample == [8, 8, 8]) or
        #             (photometric_interpretation == 1 and bits_per_sample == 8)):
        #         compression = 'DCT JPEG'
        #     else:
        #         compression = 'lossless Huffman JPEG'

    def _get_ifd_fields(self, f):
        """
        Parses the IFD fields and gets their values

        :param f: the '_io.BufferedReader' holding the read index
        of the start of the IFD from within the file
        :return: None
        """
        ifd_offset = f.tell()
        n_ifd_fields = dutils.get_value_from_type(f.read(2), 3, self._byte_order, False)
        ifd = dict()
        for _ in range(n_ifd_fields):
            field_values = []
            field_offset = f.tell()
            tag = dutils.get_value_from_type(f.read(2), 3, self._byte_order)
            field_type = dutils.get_value_from_type(f.read(2), 3, self._byte_order)
            count = dutils.get_value_from_type(f.read(4), 4, self._byte_order)
            value_offset_buffer = f.read(4)
            value_offset = dutils.get_value_from_type(value_offset_buffer, 4, self._byte_order)

            # if tag in DNG._tags:
            length = dutils.get_num_of_bytes_in_type(field_type)
            n_bytes = length * count
            if n_bytes > 4:
                position = f.tell()
                f.seek(value_offset)
                if length == 1:
                    if dcnst.DNG_TAGS.get(tag, dcnst.DEF_REND_TAG).is_string:
                        field_values.append(dutils.get_value_from_type(f.read(count), field_type,
                                                                       self._byte_order, True))
                    else:
                        field_values.append(f.read(count))
                    # if tag in (336, 338):
                    #     assert False # they use BYTEs as datatype and may be broken
                    # # TODO: replace with better stuff
                    # if tag in dct.RENDERING_TAGS:
                    #     if dct.RENDERING_TAGS[tag]['Multiple Values']:
                    #         field_values.append(f.read(count))
                    #     else:
                    #         field_values.append(dutils._get_value_from_type(f.read(count), field_type, self._byte_order))
                    # # field_values = dutils._get_values_from_type(f.read(count), field_type, self._byte_order)
                else:
                    buffer = f.read(n_bytes)
                    field_values = dutils.get_values_from_type(buffer, field_type, self._byte_order,
                                                               dcnst.DNG_TAGS.get(tag, dcnst.DEF_REND_TAG).is_string)
                    if tag == 330 or tag == 34665:
                        for offset in field_values:
                            f.seek(offset)
                            self._get_ifd_fields(f)
                f.seek(position)
            else:
                field_values = dutils.get_values_from_type(value_offset_buffer, field_type, self._byte_order)[:count]
                if tag == 330 or tag == 34665:
                    position = f.tell()
                    f.seek(value_offset)
                    self._get_ifd_fields(f)
                    f.seek(position)

            ifd[tag] = DNG.Field(tag, field_type, count, value_offset, field_values)
            if dutils.get_num_of_bytes_in_type(field_type) in (1, 2) and n_bytes < 5:
                ifd[tag].value_offset_buffer = value_offset_buffer

        self._ifds[ifd_offset] = ifd

    def get_image(self, rectangle=[0.0, 0.0, 1.0, 1.0], sub_image='RAW'):
        """
        Get the desired image, thumbnail or raw.

        :param rectangle: The bounding box of the image to be rendered.
        In the format X1, Y1, X2, Y2 where:
        X1 is the x position of the top left corner,
        Y1 is the y position of the top left corner,
        X2 is the x position of the bottom right corner,
        Y2 is the y position of the top right corner.
        The input values are to but in percents of the way across the
        image from the origin.
        The top left corner of the cropped area is assumed to be the
        origin. If no crop is applied by the user than the
        DefaultCropOrigin tag data is used as the origin.
        :param sub_image: selects which sub-image to return from the file
        'RAW' to get the original raw image,
        'Thumbnail' to get the thumbnail if present.
        :return: A 3D numpy array holding the rendered image.
        The first dimension covers the color channels, Red, Green, Blue.
        The second covers the width.
        The third covers the height.
        """
        if not self._ifds:
            self._parse_ifds()
            self._get_idf_offsets()
        self._get_fields_required_to_render(sub_image)
        self.get_xmp()
        rectangle = dutils.convert_rectangle_percent_to_pixels(self._used_fields, rectangle,
                                                               self._xmp.get(b'crs:CropLeft', {'val': 0})['val'],
                                                               self._xmp.get(b'crs:CropTop', {'val': 0})['val'],
                                                               self._xmp.get(b'crs:CropRight', {'val': 1})['val'],
                                                               self._xmp.get(b'crs:CropBottom', {'val': 1})['val'])
        self._get_tile_or_strip_bytes(rectangle)
        image = _renderer.render(self._used_fields, rectangle)
        self._clear_section_data()
        return image

    def get_xmp(self):
        """
        Gets the xmp data from the dng.

        :return: The xmp data as a dict with the keys being properties
        as shown in the xmp data and values being a floats
        """
        xmp_field = self._ifds[self._xmp_ifd_offset][700].values[0]
        for xmp_property in dcnst.XMP_TAGS.keys():
            # name_offset = xmp_field.find(xmp_property)
            value = dutils.get_xmp_property_value(xmp_field, xmp_property)
            if value:
                self._xmp[xmp_property] = {'val': float(value), 'updated': False}
            # if name_offset > -1:
            # TODO: probably faster to just add the len of the property name + 2
            # value_start = xmp_field.find(b'="', name_offset) + 2
            # value_end = xmp_field.find(b'"', value_start)
            # self._xmp[property_name] = {'val': float(xmp_field[value_start:value_end]), 'updated': False}

        return {k: v['val'] for k, v in self._xmp.items()}

    def _parse_ifds(self):
        """
        Read the IFDs from the file and organize them into self._ifds

        :return: None
        """
        with open(self.path, 'rb', buffering=DNG._buffer_size) as f:
            f.seek(self._zeroth_ifd)
            self._get_ifd_fields(f)

    def _get_tile_or_strip_bytes(self, rectangle):
        """
        Retrieve the raw image data.

        Get the image data from the file for the relevant image,
        whether it be stored as strips or tiles, is is needed to
        render the portion of the image that's covered by the rectangle
        :param rectangle:
        :return: None
        """
        self._used_fields['section_bytes'] = {}
        self._used_fields['rendered_section_bounding_box'] = []
        self._used_fields['rendered_rectangle'] = rectangle
        with open(self.path, 'rb', buffering=DNG._buffer_size) as f:
            if 'tile_byte_counts' in self._used_fields:
                section_byte_counts = self._used_fields['tile_byte_counts']
                section_offsets = self._used_fields['tile_offsets']
                section_width = self._used_fields['tile_width']
                section_length = self._used_fields['tile_length']
                image_width = self._used_fields['image_width']
                image_length = self._used_fields['image_length']
                n_tiles_wide = math.ceil(image_width / section_width)
                n_tiles_long = math.ceil(image_length / section_length)
                # rendered_x_offset =
            elif 'strip_byte_counts' in self._used_fields:
                raise Exception('This feature needs work, strip_byte_counts')
                section_byte_counts = self._used_fields['tile_byte_counts']
                section_offsets = sub_image_fields['tile_offsets']
            for index, (byte_counts, offsets) in enumerate(zip(section_byte_counts, section_offsets)):
                x1 = index % n_tiles_wide * section_width
                y1 = index // n_tiles_wide * section_length
                x2 = x1 + section_width
                y2 = y1 + section_length
                if x2 > rectangle[0] and x1 < rectangle[2] and y2 > rectangle[1] and y1 < rectangle[3]:
                    self._used_fields['rendered_section_bounding_box'] = dutils \
                        .renderd_area_bounding_box(self._used_fields['rendered_section_bounding_box'], x1, y1, x2, y2)
                    if 'x_tile_offset' not in locals():
                        x_tile_offset = x1 // section_width
                        y_tile_offset = y1 // section_length
                    f.seek(offsets)
                    self._used_fields['section_bytes'][tuple([index % n_tiles_wide - x_tile_offset,
                                                              index // n_tiles_wide - y_tile_offset])] = \
                        np.fromfile(f, np.uint8, byte_counts).astype(np.intc)
        # return sub_image_fields

    def _get_idf_offsets(self):
        """
        Get the byte indexes of the thumbnail and main uncompressed/raw image in the file

        :return: None
        """
        self._thumbnail_offset = 0
        self._orig_img_offset = 0
        self._xmp_ifd_offset = 0

        offsets = sorted(self._ifds.keys())  # sorting since the thumbnail is the first IFD if present
        for offset in offsets:
            if self._thumbnail_offset is 0:
                self._thumbnail_offset = offset
            if 254 in self._ifds[offset]:
                if self._ifds[offset][254].values[0] is 0:
                    self._orig_img_offset = offset
                    # break
            if 700 in self._ifds[offset]:
                self._xmp_ifd_offset = offset
            if self._orig_img_offset and self._xmp_ifd_offset:
                break

    def update_xmp_property(self, xmp_property, value):
        # TODO: this could be better
        if xmp_property in self._xmp:
            if self._xmp.get(xmp_property).get('val') != value:
                self._xmp[xmp_property] = {'val': value, 'updated': True}
        else:
            raise Exception("Field to be updated wasn't present")

    def store_xmp_fields(self):
        xmp_data = self._ifds[self._xmp_ifd_offset][700].values[0]
        xmp_length = len(xmp_data)
        for field, value in self._xmp.items():
            if value['updated']:
                self._updated = True
                xmp_property = dcnst.XMP_TAGS[field]

                start_offset = xmp_data.find(field) + len(field) + 2
                end_offset = xmp_data.find(b'"', start_offset)
                # old_value = xmp_data[start_offset: end_offset]
                start = xmp_data[:start_offset]
                mid = str(round(float(value['val']), xmp_property.n_decimal_places))
                if not xmp_property.n_decimal_places:
                    mid = mid[:-2]
                if xmp_property.is_vector and mid[0] != '-':
                    mid = '+' + mid
                mid = bytes(mid, 'utf-8')
                end = xmp_data[end_offset:]
                xmp_data = start + mid + end
        self._xmp_length_changed = xmp_length != len(xmp_data)
        self._ifds[self._xmp_ifd_offset][700].values[0] = xmp_data
        self._ifds[self._xmp_ifd_offset][700].count = len(xmp_data)

    def rendered_shape(self):
        # TODO: who knows if it's 'initialized'
        shape = self.default_shape()
        crops = self.get_crops()

        return [round(shape[0] * (crops[2] - crops[0])), round(shape[1] * (crops[3] - crops[1]))]

    def default_shape(self):
        return self._used_fields['default_crop_size']

    def get_crops(self):
        return [self._xmp.get(b'crs:CropLeft').get('val', 0),
                self._xmp.get(b'crs:CropTop').get('val', 0),
                self._xmp.get(b'crs:CropRight').get('val', 1),
                self._xmp.get(b'crs:CropBottom').get('val', 1)]

    def save(self):
        if self._updated:
            if self._xmp_length_changed:
                last_item = 0
                for ifd in self._ifds.values():
                    for field in ifd.values():
                        length = dutils.get_num_of_bytes_in_type(field.type) * field.count
                        if field.value_offset > last_item and length > 4:
                            last_item = field.value_offset

                if last_item == self._ifds[self._xmp_ifd_offset][700].value_offset:
                    with open(self.path, 'r+b', DNG._buffer_size) as f:
                        f.seek(self._ifds[self._xmp_ifd_offset][700].value_offset)
                        f.write(self._ifds[self._xmp_ifd_offset][700].values[0])
                        if f.tell() % 1:
                            f.write(0x00)
                else:
                    self._write_dng()
            else:
                with open(self.path, 'wb', DNG._buffer_size) as f:
                    f.seek(self._ifds[self._xmp_ifd_offset][700].value_offset)
                    f.write(self._ifds[self._xmp_ifd_offset][700].values[0])

    def _write_dng(self):
        # file = array.array()
        first_ifd_location = 8
        with open(self.path + '.temp', 'w+b') as wf:
            pass
        with open(self.path + '.temp', 'r+b', DNG._buffer_size) as wf:
            with open(self.path, 'rb', DNG._buffer_size) as rf:
                if self._byte_order == '>':
                    wf.write(bytes('MM', 'utf-8'))
                else:
                    wf.write(bytes('II', 'utf-8'))

                wf = self._write_value(wf, 42, data_type=3)
                wf = self._write_value(wf, first_ifd_location, data_type=4)
                wf.seek(self._write_ifd(wf, rf, self._ifds[self._thumbnail_offset], first_ifd_location))
            if wf.tell() % 2:
                self._write_value(wf, 0, data_type=1)

    def _write_ifd(self, wf, rf, ifd, write_location):
        end_write_index = len(ifd) * 12 + 6 + write_location
        section_offsets = []
        section_byte_counts = []
        wf.seek(write_location)

        for field in ifd.values():
            if field.tag in (273, 324):
                section_offsets = field.values
            if field.tag in (279, 325):
                section_byte_counts = field.values
            if section_byte_counts and section_offsets:
                break

        wf = self._write_value(wf, len(ifd), data_type=3)

        for tag in sorted(ifd.keys()):
            field = ifd[tag]
            wf = self._write_value(wf, field.tag, data_type=3)
            wf = self._write_value(wf, field.type, data_type=3)
            wf = self._write_value(wf, field.count)
            if field.tag in (273, 324):
                resume_index = wf.tell() + 4
                if field.count == 1:
                    wf = self._write_value(wf, end_write_index)
                    # end_write_index += 4
                    wf.seek(end_write_index)
                    rf.seek(section_offsets[0])
                    end_write_index += wf.write(rf.read(section_byte_counts[0]))
                elif field.count == 2:
                    assert False
                    # Theres a potential bug here if there were two shorts as the offsets
                else:
                    wf = self._write_value(wf, end_write_index)
                    section_write_offset = dutils.get_num_of_bytes_in_type(field.type) * field.count + end_write_index

                    for sec_len, sec_off in zip(section_byte_counts, section_offsets):
                        wf.seek(end_write_index)
                        # end_write_index += wf.write(section_write_offset)
                        wf = self._write_value(wf, section_write_offset)
                        end_write_index += 4
                        wf.seek(section_write_offset)
                        rf.seek(sec_off)
                        section_write_offset += wf.write(rf.read(sec_len))
                    end_write_index = section_write_offset

                wf.seek(resume_index)
            elif field.tag in (330, 34665):
                n_bytes = dutils.get_num_of_bytes_in_type(field.type) * field.count
                wf = self._write_value(wf, end_write_index)
                resume_index = wf.tell()
                if n_bytes > 4:
                    ifd_index = end_write_index + n_bytes
                    for index in field.values:
                        wf.seek(end_write_index)
                        wf = self._write_value(wf, ifd_index)
                        end_write_index += 4
                        ifd_index = self._write_ifd(wf, rf, self._ifds[index], ifd_index)
                    end_write_index = ifd_index
                elif field.type == 3:
                    assert False
                    # This could be a bug if there are two shorts.
                else:
                    end_write_index = self._write_ifd(wf, rf, self._ifds[field.value_offset], end_write_index)
                wf.seek(resume_index)
            elif field.tag == 700:
                wf = self._write_value(wf, end_write_index)
                resume_index = wf.tell()
                wf.seek(end_write_index)
                end_write_index += wf.write(field.values[0])
                wf.seek(resume_index)
            else:
                n_bytes = dutils.get_num_of_bytes_in_type(field.type) * field.count
                if n_bytes > 4 or field.count > 1:
                    rf.seek(field.value_offset)
                    if n_bytes > 4:
                        # TODO: change to end_write_index += wf.write(... and test
                        wf = self._write_value(wf, end_write_index)
                        left_off_at = wf.tell()
                        wf.seek(end_write_index)
                        wf.write(rf.read(n_bytes))
                        end_write_index += n_bytes
                        wf.seek(left_off_at)
                    else:
                        # end_location = wf.tell() + 4
                        # wf.write(rf.read(n_bytes))
                        # wf.seek(end_location)
                        wf.write(field.value_offset_buffer)
                else:
                    wf = self._write_value(wf, field.value_offset, data_type=field.type,
                                           values=field.values, n_bytes=4)

        return end_write_index

    def _write_value(self, f, number, data_type=4, values=None, n_bytes=None):
        # TODO: make this a dict?
        bytes_to_skip = 0
        if data_type == 1:
            f.write(struct.pack(f'{self._byte_order}B', number))
            if n_bytes:
                bytes_to_skip = n_bytes - 1
        elif data_type == 2:
            a = 0
            if values:
                f.write(bytes(values, 'utf-8'))
            else:
                f.write(bytes(number, 'utf-8'))
            if n_bytes:
                bytes_to_skip = n_bytes - len(number)
        elif data_type == 3:
            f.write(struct.pack(f'{self._byte_order}H', number))
            if n_bytes:
                bytes_to_skip = n_bytes - 2
        elif data_type == 4:
            f.write(struct.pack(f'{self._byte_order}I', number))
            if n_bytes:
                bytes_to_skip = n_bytes - 4

        if n_bytes and bytes_to_skip:
            f.seek(f.tell() + bytes_to_skip)

        return f

    def _clear_section_data(self):
        self._used_fields['section_bytes'] = None
