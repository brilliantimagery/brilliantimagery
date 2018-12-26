import math
import os
import platform
import struct
from collections import defaultdict
from typing import Dict
from typing import IO
from typing import List

from Cython.Compiler import MemoryView
import numpy as np

from . import _dng_constants as dcnst
from . import _dng_utils as dutils
from . import _renderer


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

    _BUFFER_SIZE = 50000000
    _REFERENCE_FRAME_STARS = 3

    def __init__(self, path):
        """
        Initialize a DNG file representation.

        Test to make sure the input file is a valid DNG and read the
        beginning of the file so that it can be parsed.
        :param path: File name of the DNG file
        """
        self._path = path
        self._ifds = dict()
        self._used_fields = dict()
        self._xmp = defaultdict(dict)
        self._updated = False
        self._xmp_length_changed = False
        with open(self._path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
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

            self._parse_ifds()
            self._get_idf_offsets()

    def get_capture_datetime(self) -> str:
        """
        Gets a datetime for when the image was captured.

        Gets the standardised capture datetime, first looking in the
        xmp data, and then falling back to the file creation time.

        :return: A creation time formatted as a string.
        """
        xmp = self._ifds[self._xmp_ifd_offset][700].values[0]
        capture_datetime = dutils.get_xmp_attribute_value(xmp, b'xmp:CreateDate')
        if capture_datetime:
            return capture_datetime
        else:
            """
                Try to get the date that a file was created, falling back to when it was
                last modified if that isn't possible.
                See http://stackoverflow.com/a/39501288/1709587 for explanation.
                """
            if platform.system() == 'Windows':
                return os.path.getctime(self._path)
            else:
                stat = os.stat(self._path)
                try:
                    return stat.st_birthtime
                except AttributeError:
                    # We're probably on Linux. No easy way to get creation dates here,
                    # so we'll settle for when its content was last modified.
                    return stat.st_mtime

    def _get_fields_required_to_render(self, sub_image: str):
        """
        Consolidate the info required to render a DNG file.

        Consolidate the fields from throughout the file into a
        single IFD like structure holding all of the fields needed
        to render the desired image.
        :param sub_image: 'thumbnail' or 'RAW' depending on which
        is to be rendered.
        :return: None
        """
        if sub_image is 'thumbnail':
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

    def _get_ifd_fields(self, f: IO):
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

    def get_image(self, rectangle=[0.0, 0.0, 1.0, 1.0], sub_image_type='RAW') -> MemoryView:
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
        :param sub_image_type: selects which sub-image to return from the file
        'RAW' to get the original raw image,
        'thumbnail' to get the thumbnail if present.
        :return: A 3D numpy array holding the rendered image.
        The first dimension covers the color channels, Red, Green, Blue.
        The second covers the width.
        The third covers the height.
        """
        self._get_fields_required_to_render(sub_image_type)
        if not self._xmp:
            self.get_xmp()
        if sub_image_type == 'RAW':
            rectangle, active_area_offset = dutils.convert_rectangle_percent_to_pixels(self._used_fields, rectangle,
                                                                   self._xmp[b'crs:CropLeft'].get('val', 0),
                                                                   self._xmp[b'crs:CropTop'].get('val', 0),
                                                                   self._xmp[b'crs:CropRight'].get('val', 1),
                                                                   self._xmp[b'crs:CropBottom'].get('val', 1))
        elif sub_image_type == 'thumbnail':
            rectangle, active_area_offset = dutils.convert_rectangle_percent_to_pixels(self._used_fields, rectangle,
                                                                   0, 0, 1, 1, sub_image_type)
        self._get_tile_or_strip_bytes(rectangle)
        image = _renderer.render(self._used_fields, rectangle, active_area_offset)
        self._clear_section_data()
        return image

    def get_xmp(self) -> Dict[bytes, int]:
        """
        Gets the xmp data from the dng.

        :return: The xmp data as a dict with the keys being properties
        as shown in the xmp data and values being a floats
        """
        if not self._xmp:
            xmp_field = self._ifds[self._xmp_ifd_offset][700].values[0]
            for xmp_attribute in dcnst.XMP_TAGS.keys():
                # name_offset = xmp_field.find(xmp_attribute)
                value = dutils.get_xmp_attribute_value(xmp_field, xmp_attribute)
                if value:
                    self._xmp[xmp_attribute] = {'val': float(value), 'updated': False}

        return {k: v['val'] for k, v in self._xmp.items() if v}

    def _parse_ifds(self):
        """
        Read the IFDs from the file and organize them into self._ifds

        :return: None
        """
        with open(self._path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
            f.seek(self._zeroth_ifd)
            self._get_ifd_fields(f)

    def _get_tile_or_strip_bytes(self, rectangle: List) -> None:
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
        with open(self._path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
            if 'tile_byte_counts' in self._used_fields:
                section_byte_counts = self._used_fields['tile_byte_counts']
                section_offsets = self._used_fields['tile_offsets']
                section_width = self._used_fields['tile_width']
                section_length = self._used_fields['tile_length']
                image_width = self._used_fields['image_width']
                image_length = self._used_fields['image_length']
                n_tiles_wide = math.ceil(image_width / section_width)
                n_tiles_long = math.ceil(image_length / section_length)
            elif 'strip_byte_counts' in self._used_fields:
                section_byte_counts = self._used_fields['strip_byte_counts']
                section_offsets = self._used_fields['strip_offsets']
                section_width = self._used_fields['image_width']
                if 'tile_length' in self._used_fields:
                    section_length = self._used_fields['tile_length']
                else:
                    section_length = self._used_fields['image_length']
                image_width = self._used_fields['image_width']
                image_length = self._used_fields['image_length']
                n_tiles_wide = 1
                n_tiles_long = math.ceil(image_length / section_length)
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

    def _get_idf_offsets(self) -> None:
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

    def set_xmp_attribute(self, xmp_attribute: bytes, value) -> bool:
        """
        Updates the stored value of the xmp attribute.

        Can not add attributes that aren't already present. If an
        attribute wasn't previously updated and present it can't be
        updated.

        Only updates the representation in the DNG object.
        DNG.store_xmp_fields() and DNG.save() have to be called to
        permanently save the updated values.

        :param xmp_attribute: The xmp attribute to be updated. Should be
        a key from the _dng_constants.XMP_TAGS Dict
        :param value: The number to be assigned to the attribute.
        :return: True if it's successful, False if it isn't, presumably
        because the attribute isn't present or the value was already
        stored.
        """

        if not self._xmp:
            self.get_xmp()
        if self._xmp[xmp_attribute].get('val') not in (value, None):
            self._xmp[xmp_attribute] = {'val': value, 'updated': True}
            return True
        else:
            return False

    def store_xmp_field(self) -> None:
        """
        Consolidate updated xmp attributes in the xmp data.

        If this isn't called, the xmp data won't be updated in the
        file even if DNG.save() is called.

        :return: None
        """
        xmp_data = self._ifds[self._xmp_ifd_offset][700].values[0]
        xmp_length = len(xmp_data)
        for field, value in self._xmp.items():
            if value.get('updated', False):
                self._updated = True
                xmp_attribute = dcnst.XMP_TAGS[field]

                # start_offset = xmp_data.find(field) + len(field) + 2
                # end_offset = xmp_data.find(b'"', start_offset)
                start_offset = xmp_data.find(field)
                uses_equals_sign = xmp_data[start_offset] == ord('=')

                if uses_equals_sign:
                    start_offset += 2
                    end_offset = xmp_data.find(b'"', start_offset)
                else:
                    start_offset += 1
                    end_offset = xmp_data.find(b'<', start_offset)

                start = xmp_data[:start_offset]
                mid = str(round(float(value['val']), xmp_attribute.n_decimal_places))
                if not xmp_attribute.n_decimal_places:
                    mid = mid[:-2]
                if xmp_attribute.is_vector and mid[0] != '-':
                    mid = '+' + mid
                mid = bytes(mid, 'utf-8')
                end = xmp_data[end_offset:]
                xmp_data = start + mid + end
        self._xmp_length_changed = xmp_length != len(xmp_data)
        self._ifds[self._xmp_ifd_offset][700].values[0] = xmp_data
        self._ifds[self._xmp_ifd_offset][700].count = len(xmp_data)

    def rendered_shape(self) -> List[int]:
        """
        The dimensions of the raw image, as cropped and rendered.

        Dimensions are in units of pixels.

        :return: A list of ints where the first is the width and the
        second is the height or length.
        """
        shape = self.default_shape()
        if not self._xmp:
            self.get_xmp()

        left = self._xmp[b'crs:CropLeft'].get('val', 0)
        top = self._xmp[b'crs:CropTop'].get('val', 0)
        right = self._xmp[b'crs:CropRight'].get('val', 1)
        bottom = self._xmp[b'crs:CropBottom'].get('val', 1)

        return [round(shape[0] * (right - left)), round(shape[1] * (bottom - top))]

    def default_shape(self) -> List[int]:
        """
        The dimensions of the raw image, before it's edited and cropped.

        Dimensions are in units of pixels.

        :return: A list of floats where the first is the width and the
        second is the height or length.
        """
        if not self._used_fields:
            self._get_fields_required_to_render('RAW')
        return [int(a) for a in self._used_fields['default_crop_size']]

    def get_xmp_attribute(self, xmp_attribute):
        if not self._xmp:
            self.get_xmp()

        return self._xmp[xmp_attribute].get('val')

    def save(self) -> None:
        """
        Overwrites the DNG file with the updated xmp info.

        :return: None
        """
        if self._updated:
            if self._xmp_length_changed:
                last_item = 0
                for ifd in self._ifds.values():
                    for field in ifd.values():
                        length = dutils.get_num_of_bytes_in_type(field.type) * field.count
                        if field.value_offset > last_item and length > 4:
                            last_item = field.value_offset

                if last_item == self._ifds[self._xmp_ifd_offset][700].value_offset:
                    with open(self._path, 'r+b', DNG._BUFFER_SIZE) as f:
                        f.seek(self._ifds[self._xmp_ifd_offset][700].value_offset)
                        f.write(self._ifds[self._xmp_ifd_offset][700].values[0])
                        if f.tell() % 1:
                            f.write(0x00)
                else:
                    self._write_dng()
            else:
                with open(self._path, 'r+b', DNG._BUFFER_SIZE) as f:
                    f.seek(self._ifds[self._xmp_ifd_offset][700].value_offset)
                    f.write(self._ifds[self._xmp_ifd_offset][700].values[0])

    def _write_dng(self):
        """
        Writes a whole new DNG file as apposed to editing the xmp info.

        :return: None
        """
        first_ifd_location = 8
        with open(self._path + '.temp', 'w+b') as wf:
            pass
        with open(self._path + '.temp', 'r+b', DNG._BUFFER_SIZE) as wf:
            with open(self._path, 'rb', DNG._BUFFER_SIZE) as rf:
                if self._byte_order == '>':
                    wf.write(bytes('MM', 'utf-8'))
                else:
                    wf.write(bytes('II', 'utf-8'))

                wf = self._write_value(wf, 42, data_type=3)
                wf = self._write_value(wf, first_ifd_location, data_type=4)
                wf.seek(self._write_ifd(wf, rf, self._ifds[self._thumbnail_offset], first_ifd_location))
            if wf.tell() % 2:
                self._write_value(wf, 0, data_type=1)
        os.remove(self._path)
        os.rename(self._path + '.temp', self._path)

    def _write_ifd(self, wf, rf, ifd, write_location):
        """
        Writes an IFD into a file.

        :param wf: The io buffer for the file being written to.
        :param rf: The io buffer for the file being referenced.
        :param ifd: The IFD to be written.
        :param write_location: The index of the start of the IFD from
        the beginning of the file in units of bytes.
        :return: None
        """
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
                        wf.write(field.value_offset_buffer)
                else:
                    wf = self._write_value(wf, field.value_offset, data_type=field.type,
                                           values=field.values, n_bytes=4)

        return end_write_index

    def _write_value(self, f, value, data_type=4, values=None, n_bytes=None):
        """
        Writes a value/values to a write buffer.

        :param f: The io buffer for the file being written to.
        :param value: The number to be written.
        :param data_type: The datatype , 1 - 12, of the value as
        defined by the TIFF standard.
        :param values: The values, as a list, to be written when there
        are multiple.
        :param n_bytes: The number of bytes that should be used to
        write the value or values
        :return: None
        """
        # TODO: make this a dict?
        bytes_to_skip = 0
        if data_type == 1:
            f.write(struct.pack(f'{self._byte_order}B', value))
            if n_bytes:
                bytes_to_skip = n_bytes - 1
        elif data_type == 2:
            if values:
                f.write(bytes(values, 'utf-8'))
            else:
                f.write(bytes(value, 'utf-8'))
            if n_bytes:
                bytes_to_skip = n_bytes - len(value)
        elif data_type == 3:
            f.write(struct.pack(f'{self._byte_order}H', value))
            if n_bytes:
                bytes_to_skip = n_bytes - 2
        elif data_type == 4:
            f.write(struct.pack(f'{self._byte_order}I', value))
            if n_bytes:
                bytes_to_skip = n_bytes - 4

        if n_bytes and bytes_to_skip:
            f.seek(f.tell() + bytes_to_skip)

        return f

    def _clear_section_data(self):
        """
        Clears the tile/strip data from the DNG object to save space.

        Used to keep large collections of DNG objects from taking up
        too much space.

        :return: None
        """
        self._used_fields['section_bytes'] = None

    def is_reference_frame(self):
        if not self._xmp:
            self.get_xmp()

        return int(self._xmp[b'xmp:Rating'].get('val', 0)) == DNG._REFERENCE_FRAME_STARS

    def get_median_green_value(self, rectangle=None, image=None):
        if image is None:
            image = self.get_image(rectangle)
        return np.median(image[1, :, :])

    @staticmethod
    def get_possible_xmp_attributes():
        return dcnst.XMP_TAGS
