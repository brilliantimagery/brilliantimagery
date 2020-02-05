from collections import defaultdict
from io import BytesIO
import math
import os
import platform
import struct
from typing import Dict, Union, Optional, NamedTuple
from typing import List

# from Cython.Compiler import MemoryView
import numpy as np
import numpy

from brilliantimagery.dng import _dng_constants as d_cnst
from brilliantimagery.dng import _dng_utils as d_utils
# from brilliantimagery.dng import _renderer


class DNG:
    """
    A representation of a DNG image file.

    Allows reading and editing the underlying file.

    It's based on the DNG 1.4 standard and works for most cameras by most
    manufacturers but the standard is not fully implemented and not
    all edge cases for older versions of the standard are fully supported.

    While the DNG 1.5 standard has come out since this was created,
    the standard's updates haven't been implemented since they have, at most,
    negligible impact on this project given this project's typical use cases.

    :param str path: The path to the represented DNG file.

    """

    class _Field:
        """A TIFF Field as defined by the TIFF6 standard."""

        def __init__(self, tag, type, count, value_offset, values=None):
            """
            Initializes the :class:`brilliantimagery.dng.DNG.Field` class.

            :param int tag: The tag number of the field
            :param int type: The type number of the field
            :param int count: The count of the field
            :param int value_offset: The value of the field or the offset
                to the value(s) if the combination of type and count
                require more than the 4 allotted bytes to store the
                Field's value(s).
            :param list[int or float] values: The list of the field's values.
                Values should be preconverted from the file's binary data
                to the intended value through the use of
                :meth:`brilliantimagery.dng._dng_utils.get_value_from_type`
                or
                :meth:`brilliantimagery.dng._dng_utils.get_values_from_type`
                or some other similar process. Fields with 1 value should
                have it in a list with a length of 1.

            """
            if not values:
                values = []
            self.tag = tag
            self.type = type
            self.count = count
            self.value_offset = value_offset
            self.values = values

        def __repr__(self):
            return f'{self.tag}, {self.type}, {self.count}, {self.value_offset}'

        def __eq__(self, other):
            return (self.tag == other.tag and self.type == other.type and
                    self.count == other.count and self.value_offset == other.value_offset)

    _BUFFER_SIZE = 50000000
    _REFERENCE_FRAME_STARS = 3

    def __init__(self, path: str):
        """
        Initializes an image file representation.

        :Example - Create a :class:`DNG` instance:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')

        :param str path: Path to the image file.

        """
        self.path = path
        self._ifds = dict()
        self._used_fields = dict()
        self._xmp = defaultdict(dict)
        self._updated = False
        self._xmp_length_changed = False

        self._byte_order = ''
        self._zeroth_ifd = 0

        self._parse()

    def _parse(self):
        """
        Parses the image's IFDs so that other functions have data to work with.

        Note: the image data is not read or stored with this call, only pointers
        and strip/tile sizes are.

        :return: None

        """
        with open(self.path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
            f = self._get_byte_order(f)
            assert (struct.unpack(f'{self._byte_order}H', f.read(2))[0] == 42)
            self._zeroth_ifd = struct.unpack(f'{self._byte_order}H', f.read(2))[0]

            self._parse_ifds()
            self._get_ifd_offsets()

    def _get_byte_order(self, f: BytesIO) -> BytesIO:
        """
        Reads the byte order used in the file.

        Rather than returning the byte order, it's stored in the :attr:`DNG._byte_order`
        variable as "<" if the file is small ended or ">" if it's big ended.

        :param BytesIO f: The :class:`I/O` stream to the file. Assumes the read index points
            to the first byte of the byte order denoting pair of bytes.

        :return: The :class:`I/O` stream to the file with the read index pointing
            to the byte that immediately follows the byte order denoting pair.
        :rtype: BytesIO

        :raises ValueError: If the order denoting bytes aren't either of the
            expected options.

        """
        self._byte_order = f.read(2)
        if self._byte_order == b'II':
            self._byte_order = '<'
        elif self._byte_order == b'MM':
            self._byte_order = '>'
        else:
            raise ValueError(f"Byte order should be b'II' or b'MM' but is {self._byte_order}")
        return f

    def get_capture_datetime(self) -> str:
        """
        Gets when the image was captured.

        The return value may be formatted as a datetime or unix
        time stamp depending on the available information. The format
        should be consistent between images captured on the same camera
        and processed with the same workflow.

        :Example - Get an images creation datetime:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> dng.get_capture_datetime()
        '2020-02-05 10:48:39.317369'

        :return: A creation time.
        :rtype: str

        """
        xmp = self._ifds.get(self._xmp_ifd_offset, {}). \
            get(700, DNG._Field(0, 0, 0, 0, [b''])).values[0]
        capture_datetime = d_utils.get_xmp_attribute_value(xmp, b'xmp:CreateDate')
        if capture_datetime:
            return capture_datetime
        else:
            if platform.system() == 'Windows':
                return str(os.path.getctime(self.path))
            else:
                stat = os.stat(self.path)
                try:
                    return str(stat.st_birthtime)
                except AttributeError:
                    return str(stat.st_mtime)

    def _get_fields_required_to_render(self, sub_image: str) -> None:
        """
        Consolidates the info required to render the DNG file.

        Rather than retuning them, they're stored in the
        :attr:`DNG._used_fields` variable.

        Consolidates the fields from throughout the file into a
        single IFD like structure holding all of the fields needed
        to render the desired image. This avoids having to search
        through multiple IFDs to get a value, or having to
        determine which instance of a value to use if it's stored
        multiple times for multiple images from within the file
        (such as how there are often 2 :attr:`width` fields, one
        for a thumbnail and one for the RAW image).

        :param str sub_image: 'thumbnail' or 'RAW' depending on which
            is to be rendered.

        :return: None

        :raises ValueError: If an invalid 'sub_image' is given.

        """
        if sub_image.lower() == 'thumbnail':
            offset = self._thumbnail_offset
        elif sub_image.lower() == 'raw':
            offset = self._orig_img_offset
        else:
            raise ValueError(f'Retrieved image type must be "RAW" or "thumbnail" but "{sub_image}" was given.')

        ifd = self._ifds[offset]
        plural_value_fields = {d_cnst.DNG_TAGS[tag].name: ifd[tag].values
                               for tag, field in d_cnst.DNG_TAGS.items()
                               if tag in ifd and field.is_multi_valued}
        single_value_fields = {d_cnst.DNG_TAGS[tag].name: ifd[tag].values[0]
                               for tag, field in d_cnst.DNG_TAGS.items()
                               if tag in ifd and not field.is_multi_valued}
        self._used_fields = {**plural_value_fields, **single_value_fields,
                             **{'orientation': self._ifds[self._thumbnail_offset][274].values[0]},
                             }

    def _get_ifd_fields(self, f: BytesIO) -> None:
        """
        Recursively parses the IFD fields and gets their values.

        Passing it an :class:`IO` with the file's first IFD's index
        will result in parsing the first IFD and all others that are
        pointed to. Passing a later IFD that doesn't point to any
        others results in just that one being parsed

        Rather than returning the IFD, it's stored to :attr:`DNG._ifds`
        which is a :class:`dict` where the key is the byte index of the
        start of the respective IFD and each value is another
        :class:`dict` where each key is a IFD field's tag with a value
        of the respective :class:`Field`.

        :param BytesIO f: the :class:`IO` holding the read index
            of the start of the IFD to be parsed from within the file.

        :return: None
        """
        ifd_offset = f.tell()
        n_ifd_fields = d_utils.get_value_from_type(f.read(2), 3, self._byte_order, False)
        ifd = dict()
        for _ in range(n_ifd_fields):
            field_values = []
            # field_offset = f.tell()
            tag = d_utils.get_value_from_type(f.read(2), 3, self._byte_order)
            field_type = d_utils.get_value_from_type(f.read(2), 3, self._byte_order)
            count = d_utils.get_value_from_type(f.read(4), 4, self._byte_order)
            value_offset_buffer = f.read(4)
            value_offset = d_utils.get_value_from_type(value_offset_buffer, 4, self._byte_order)

            length = d_utils.get_num_of_bytes_in_type(field_type)
            n_bytes = length * count
            if n_bytes > 4:
                position = f.tell()
                f.seek(value_offset)
                if length == 1:
                    if d_cnst.DNG_TAGS.get(tag, d_cnst.DEF_REND_TAG).is_string:
                        field_values.append(d_utils.get_value_from_type(f.read(count), field_type,
                                                                        self._byte_order, True))
                    else:
                        field_values.append(f.read(count))
                else:
                    buffer = f.read(n_bytes)
                    field_values = d_utils.get_values_from_type(buffer, field_type, self._byte_order,
                                                                d_cnst.DNG_TAGS.get(tag, d_cnst.DEF_REND_TAG).is_string)
                    if tag == 330 or tag == 34665:
                        for offset in field_values:
                            f.seek(offset)
                            self._get_ifd_fields(f)
                f.seek(position)
            else:
                field_values = d_utils.get_values_from_type(value_offset_buffer, field_type, self._byte_order)[:count]
                if tag == 330 or tag == 34665:
                    position = f.tell()
                    f.seek(value_offset)
                    self._get_ifd_fields(f)
                    f.seek(position)

            ifd[tag] = DNG._Field(tag, field_type, count, value_offset, field_values)
            if d_utils.get_num_of_bytes_in_type(field_type) in (1, 2) and n_bytes < 5:
                ifd[tag].value_offset_buffer = value_offset_buffer

        self._ifds[ifd_offset] = ifd

    def get_image(self, rectangle=[0.0, 0.0, 1.0, 1.0], sub_image_type='RAW') -> numpy.ndarray:
        """
        Gets the desired portion of the desired reference image.

        No transforms such as white balancing or exposure compensation
        are performed so the image may not look as expected (they're
        often too green).

        The rendering algorithm is relatively rudimentary so the
        results will be less refined than some other renderers.

        :Example - Gets the shape and then rendered pixel values for a portion of the RAW data in a hypothetical DNG file.:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> rectangle = [100, 100, 600, 400]
        >>> image = dng.get_image(rectangle, 'RAW')
        >>> image.shape
        (3, 500, 300)
        >>> image
        array([[[0.03698262, 0.03751407, ..., 0.04139052, 0.04229711],
                ...,
                [0.06149181, 0.06192947, ..., 0.05291047, 0.05264474]],
               [[0.08861135, 0.08715768, ..., 0.09322246, 0.09294111],
                ...,
                [0.13045517, 0.13178901, ..., 0.11453253, 0.11304239]],
               [[0.06405527, 0.06405527, ..., 0.06430537, 0.06463361],
                ...,
                [0.08818932, 0.08818932, ..., 0.07837314, 0.07571589]]], dtype=float32)


        :param rectangle: The bounding box of the portion of the image that's
            to be rendered. In the format X1, Y1, X2, Y2 where:

            * X1 is the x position of the top left corner,
            * Y1 is the y position of the top left corner,
            * X2 is the x position of the bottom right corner,
            * Y2 is the y position of the top right corner.

            The input values can either be in fractions of the way across the
            image from the origin, or pixels from the origin.
            The top left corner of the cropped area is assumed to be the
            origin. If no crop is applied by the user than the
            :attr:`DefaultCropOrigin` field data is used as the origin.
        :type rectangle: list[int or float]

        :param str sub_image_type: selects which sub-image to return from the file.

            :attr:`RAW` to get the original, raw, image.

            :attr:`thumbnail` to get the thumbnail if present.

        :return: A 3D float array holding the rendered image.

            * The first dimension represents the color channels: Red, Green, Blue at indices 0, 1, and 2 respectively.
            * The second represents the width.
            * The third represents the height.
        :rtype: Numpy.ndarray

        .. note:: Since the output is a float in the range of 0 to 1, for many
            applications it'll have to be scaled.

        .. note:: While this works for the vast majority of tested cameras,
            cameras that don't have pure GRB and/or 2x2 Bayer Masks can't presently
            be rendered. So while support will presumably eventually be added,
            at present, the images from a number of Fuji cameras can't be rendered.

        """

        from brilliantimagery.dng import _renderer

        self._get_fields_required_to_render(sub_image_type)
        if not self._xmp:
            self.get_xmp()
        rectangle = d_utils.convert_rectangle_percent_to_pixels(self._used_fields, rectangle,
                                                                self._xmp[b'crs:CropLeft'].get('val', 0),
                                                                self._xmp[b'crs:CropTop'].get('val', 0),
                                                                self._xmp[b'crs:CropRight'].get('val', 1),
                                                                self._xmp[b'crs:CropBottom'].get('val', 1),
                                                                sub_image_type)
        active_area_offset = d_utils.get_active_area_offset(self._used_fields, rectangle, sub_image_type)
        self._get_tile_or_strip_bytes(rectangle)
        image = _renderer.render(self._used_fields, rectangle, active_area_offset)
        self._clear_section_data()
        return image

    def get_xmp(self) -> Dict[bytes, float]:
        """
        Gets the stored XMP data from the represented dng file.

        The XMP data holds all of the edits that have been made in Lightroom.

        :Example - Get the XMP data stored in the underlying image:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> dng.get_xmp()
        {b'crs:Temperature': 7135.0, b'crs:Tint': 10.0, b'crs:Saturation': 35.0, b'crs:Vibrance': 76.0, b'crs:Sharpness': 25.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:RedSaturation': 0.0, b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0, b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0, b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 27.0, b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0, b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0, b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0, b'crs:SaturationAdjustmentBlue': -31.0, b'crs:SaturationAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0, b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0, b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0, b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0, b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0, b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0, b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0, b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0, b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0, b'crs:ColorNoiseReductionDetail': 50.0, b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0, b'crs:Contrast2012': 0.0, b'crs:Highlights2012': -100.0, b'crs:Shadows2012': 48.0, b'crs:Whites2012': 71.0, b'crs:Blacks2012': 2.0, b'crs:Clarity2012': 29.0, b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0, b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0, b'crs:Dehaze': 10.0, b'crs:CropLeft': 0.048838, b'crs:CropBottom': 0.852893, b'crs:CropRight': 0.89261, b'crs:CropTop': 0.142125, b'xmp:Rating': 3.0, b'crs:Exposure2012': -0.1}

        :return: The xmp data as a dict with the keys being the properties
            as found in the XMP data and values being the associated values
            as floats.
        :rtype: dict[bytes, float]

        """
        if not self._xmp:
            if self._xmp_ifd_offset in self._ifds:
                xmp_field = self._ifds[self._xmp_ifd_offset][700].values[0]
                for xmp_attribute in d_cnst.XMP_TAGS.keys():
                    value = d_utils.get_xmp_attribute_value(xmp_field, xmp_attribute)
                    if value:
                        self._xmp[xmp_attribute] = {'val': float(value), 'updated': False}
            else:
                return {}

        return {k: v['val'] for k, v in self._xmp.items() if v}

    def _parse_ifds(self) -> None:
        """
        Read the IFDs from the file and organize them into :attr:`DNG._ifds`

        :return: None
        """
        with open(self.path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
            f.seek(self._zeroth_ifd)
            self._get_ifd_fields(f)

    def _get_tile_or_strip_bytes(self, rectangle: List) -> None:
        """
        Retrieves the raw image data.

        Gets the image data from the file for the relevant image based on
        :attr:`DNG._used_fields` which is set by
        :func:`DNG._get_fields_required_to_render`,
        whether it be stored as strips or tiles.

        :param rectangle: The bounding box of the area to be rendered.
        :return: None
        """
        self._used_fields['section_bytes'] = {}
        self._used_fields['rendered_section_bounding_box'] = []
        self._used_fields['rendered_rectangle'] = rectangle

        if self._used_fields['bits_per_sample'][0] == 8 and self._used_fields['compression'] == 7:
            data_type = np.uint8
            bytes_per_sample = 1
        elif self._used_fields['bits_per_sample'][0] == 8 and self._used_fields['compression'] == 1:
            data_type = np.uint8
            bytes_per_sample = 1
        elif self._used_fields['bits_per_sample'][0] == 16 and self._used_fields['compression'] == 1:
            data_type = np.uint16
            bytes_per_sample = 2
        elif self._used_fields['bits_per_sample'][0] == 16 and self._used_fields['compression'] == 7:
            data_type = np.uint8
            bytes_per_sample = 1
        else:
            raise NotImplementedError(f'Compression not implemented in {__name__}.')

        with open(self.path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
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
                if 'rows_per_strip' in self._used_fields:
                    section_length = self._used_fields['rows_per_strip']
                else:
                    section_length = self._used_fields['image_length']
                image_width = self._used_fields['image_width']
                image_length = self._used_fields['image_length']
                n_tiles_wide = 1
                n_tiles_long = math.ceil(image_length / section_length)
            for index, (byte_count, offset) in enumerate(zip(section_byte_counts, section_offsets)):
                x1 = index % n_tiles_wide * section_width
                y1 = index // n_tiles_wide * section_length
                x2 = x1 + section_width
                y2 = y1 + section_length
                if x2 > rectangle[0] and x1 < rectangle[2] and y2 > rectangle[1] and y1 < rectangle[3]:
                    self._used_fields['rendered_section_bounding_box'] = d_utils \
                        .renderd_area_bounding_box(self._used_fields['rendered_section_bounding_box'], x1, y1, x2, y2)
                    if 'x_tile_offset' not in locals():
                        x_tile_offset = x1 // section_width
                        y_tile_offset = y1 // section_length
                    f.seek(offset)
                    self._used_fields['section_bytes'][(index % n_tiles_wide - x_tile_offset,
                                                        index // n_tiles_wide - y_tile_offset)] = \
                        np.fromfile(f, data_type, byte_count // bytes_per_sample).astype(np.intc)

    def _get_ifd_offsets(self) -> None:
        """
        Gets the byte indexes of the commonly used IFDs.

        Stores the offsets of the thumbnail, main uncompressed/raw
        image, and xmp containing IFDs.

        :return: None
        """
        self._thumbnail_offset = 0
        self._orig_img_offset = 0
        self._xmp_ifd_offset = 0

        offsets = sorted(self._ifds.keys())  # sorting since the thumbnail is the first IFD if present
        for offset in offsets:
            if self._thumbnail_offset == 0:
                self._thumbnail_offset = offset
            if 254 in self._ifds[offset]:
                if self._ifds[offset][254].values[0] == 0:
                    self._orig_img_offset = offset
            if 700 in self._ifds[offset]:
                self._xmp_ifd_offset = offset
            if self._orig_img_offset and self._xmp_ifd_offset:
                break

    def set_xmp_attribute(self, xmp_attribute: bytes, value: Union[int, float, str]) -> bool:
        """
        Updates the stored value of an XMP attribute.

        This isn't updating the file or the sored :class:`Field`, only
        a value in a :class:`dict` of xmp values.

        Cannot update attributes that aren't already present. If an
        attribute hasn't been set in photo editing software such as
        Adobe Lightroom then it won't be present and subsequently can't
        be updated.

        Only updates the representation in the :class:`DNG` object.
        :func:`DNG.store_xmp_field` and :func:`DNG.save` have to be called to
        permanently save the updated values. This is done to minimize
        redundant and time consuming read/write operations.

        :Example - Set and then get the color temperature for an image.:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> dng.set_xmp_attribute(b'crs:Temperature', 7000)
        True
        >>> dng.get_xmp()[b'crs:Temperature']
        7000

        :param xmp_attribute: The XMP attribute to be updated. Should be
            a key from the :attr:`_dng_constants.XMP_TAGS` dict
        :param value: The number to be assigned to the attribute.
        :type value: int, float, or str

        :return: True if it's successful, False if it isn't, presumably
            because the attribute isn't present or the specific value was
            already stored.
        :rtype: bool
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
        Consolidates the updated XMP attributes in the XMP data.

        This updates values of the associated :class:`Field` but
        doesn't change the underlying file.

        If this isn't called, the XMP data won't be updated in the
        file even if :func:`DNG.save` is called.

        :Example - Set and then store the color temperature for an image.:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> dng.set_xmp_attribute(b'crs:Temperature', 7000)
        True
        >>> dng.store_xmp_field()

        :return: None
        """

        xmp_data = self._ifds[self._xmp_ifd_offset][700].values[0]
        xmp_length = len(xmp_data)
        for field, value in self._xmp.items():
            if value.get('updated', False):
                self._updated = True
                xmp_attribute = d_cnst.XMP_TAGS[field]

                start_offset = xmp_data.find(field) + len(field)
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

    def get_rendered_shape(self) -> List[int]:
        """
        Gets the dimensions of the raw image, as cropped and rendered.

        Dimensions are in units of pixels.

        :Example - Get the shape of an image as rendered:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> dng.get_rendered_shape()
        [4637, 2609]

        :return: A list of ints where the first is the width and the
            second is the length (height) of the image.
        :rtype: list[int, int]
        """

        shape = self.get_default_shape()
        if not self._xmp:
            self.get_xmp()

        left = self._xmp[b'crs:CropLeft'].get('val', 0)
        top = self._xmp[b'crs:CropTop'].get('val', 0)
        right = self._xmp[b'crs:CropRight'].get('val', 1)
        bottom = self._xmp[b'crs:CropBottom'].get('val', 1)

        return [round(shape[0] * (right - left)), round(shape[1] * (bottom - top))]

    def get_default_shape(self) -> List[int]:
        """
        Gets the dimensions of the raw image, before it's edited or cropped.

        Dimensions are in units of pixels.

        :Example - Get the shape of an image.:

        >>> from brilliantimagery.dng import DNG
        >>> dng = DNG('path/to/image.dng')
        >>> dng.get_default_shape()()
        [4637, 2609]

        :return: A list of ints where the first is the width and the
            second is the length (height) of the image.
        :rtype: list[int, int]
        """

        if not self._used_fields:
            self._get_fields_required_to_render('RAW')
        return [int(a) for a in self._used_fields['default_crop_size']]

    def save(self) -> None:
        """
        Overwrites the dng's XMP data with the updated XMP data.

        something about time and when it overwrites vs replaces outright

        :return: None
        """

        if self._updated:
            if self._xmp_length_changed:
                last_item = 0
                for ifd in self._ifds.values():
                    for field in ifd.values():
                        length = d_utils.get_num_of_bytes_in_type(field.type) * field.count
                        if field.value_offset > last_item and length > 4:
                            last_item = field.value_offset

                if last_item == self._ifds[self._xmp_ifd_offset][700].value_offset:
                    with open(self.path, 'r+b', DNG._BUFFER_SIZE) as f:
                        f.seek(self._ifds[self._xmp_ifd_offset][700].value_offset)
                        f.write(self._ifds[self._xmp_ifd_offset][700].values[0])
                        if f.tell() % 1:
                            f.write(0x00)
                else:
                    self._write_dng()
            else:
                with open(self.path, 'r+b', DNG._BUFFER_SIZE) as f:
                    f.seek(self._ifds[self._xmp_ifd_offset][700].value_offset)
                    f.write(self._ifds[self._xmp_ifd_offset][700].values[0])

    def _write_dng(self):
        """
        Writes a whole new dng file as apposed to editing the xmp info.

        :return: None
        """

        first_ifd_location = 8
        # TODO: https://www.tutorialspoint.com/How-to-create-an-empty-file-using-Python
        with open(self.path + '.temp', 'w+b') as wf:
            # this is done to ensure that the file exists
            pass
        with open(self.path + '.temp', 'r+b', DNG._BUFFER_SIZE) as wf:
            with open(self.path, 'rb', DNG._BUFFER_SIZE) as rf:
                if self._byte_order == '>':
                    wf.write(bytes('MM', 'utf-8'))
                else:
                    wf.write(bytes('II', 'utf-8'))

                wf = self._write_value(wf, 42, data_type=3)
                wf = self._write_value(wf, first_ifd_location, data_type=4)
                wf.seek(self._write_ifd(wf, rf, self._ifds[self._thumbnail_offset], first_ifd_location))
            if wf.tell() % 2:
                self._write_value(wf, 0, data_type=1)
        os.remove(self.path)
        os.rename(self.path + '.temp', self.path)

    def _write_ifd(self, wf: BytesIO, rf: BytesIO, ifd: Dict, write_location: int):
        """
        Writes an IFD into a file.

        :param BytesIO wf: The io buffer for the file being written to.
        :param BytesIO rf: The io buffer for the file being referenced.
        :param dict ifd: The IFD to be written.
        :param int write_location: The index of the start of the IFD from
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
                    # TODO: theres a potential bug here if there were two shorts as the offsets
                else:
                    wf = self._write_value(wf, end_write_index)
                    section_write_offset = d_utils.get_num_of_bytes_in_type(field.type) * field.count + end_write_index

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
                n_bytes = d_utils.get_num_of_bytes_in_type(field.type) * field.count
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
                n_bytes = d_utils.get_num_of_bytes_in_type(field.type) * field.count
                if n_bytes > 4 or field.count > 1:
                    rf.seek(field.value_offset)
                    if n_bytes > 4:
                        # TODO: change to end_write_index += wf.write(... and tests
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

    def _write_value(self, f: BytesIO, value: int, data_type=4, values=None, n_bytes=None):
        """
        Writes a value/values to a write buffer.

        :param ByteIO f: The io buffer for the file being written to.
        :param value: The number to be written.
        :type value: int or float
        :param int data_type: The datatype , 1 - 12, of the value as
            defined by the TIFF standard.
        :param values: The values, as a list, to be written when there
            are multiple.
        :type values: list[int or float]
        :param int n_bytes: The number of bytes that should be used to
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
        Clears the tile/strip data from the :class:`DNG` object to save space.

        Used to keep large collections of :class:`DNG` objects from taking up
        too much space.

        :return: None
        """

        self._used_fields['section_bytes'] = None

    def has_n_stars(self, n=_REFERENCE_FRAME_STARS):
        """
        Says whether or not an image is rated :attr:`n` stars.

        Can be used to determine whether or not an image is a key frame
        in a timelapse sequence.

        :return: True the image's star rating is equal to ``n``, otherwise false.
        :rtype: bool

        """

        n = int(n)

        if not self._xmp:
            self.get_xmp()

        return int(self._xmp[b'xmp:Rating'].get('val', 0)) == n

    def get_brightness(self, rectangle=None, image=None):
        """
        Gets a reference brightness value for the image.

        The median green value for the image is used as the reference.

        :param rectangle: The bounding box of the portion of the image that's
            to be rendered. In the format X1, Y1, X2, Y2 where:

            * X1 is the x position of the top left corner,
            * Y1 is the y position of the top left corner,
            * X2 is the x position of the bottom right corner,
            * Y2 is the y position of the top right corner.

            The input values can either be in fractions of the way across the
            image from the origin, or pixels from the origin.
            The top left corner of the cropped area is assumed to be the
            origin. If no crop is applied by the user than the
            :attr:`DefaultCropOrigin` field data is used as the origin.
        :type rectangle: list[int or float]
        :param image: A 3D float array holding the rendered image.

            * The first dimension represents the color channels: Red, Green, Blue at indices 0, 1, and 2 respectively.
            * The second represents the width.
            * The third represents the height.

        :type image: Numpy.ndarray
        :return: The median green value from the image as a float in the range from 0 to 1.
        :rtype: float
        """

        if image is None:
            image = self.get_image(rectangle)
        return np.median(image[1, :, :])

    # def get_relevant_xmp_attributes() -> Dict[bytes, NamedTuple[int, str, bool, bool]]:
    @staticmethod
    def get_relevant_xmp_attributes():
        """
        Gets the list of XMP attributes that are relevant to image rendering.

        These are attributes that are edited with photo editing software
        such as exposure, rating, and saturation. Irrelevant attributes,
        from a photo editing perspective, such as when the photo was
        taken, are not returned.

        :return: A :class:`dict` of the below key value pairs:

            | - :attr:`key` is the property name.
            | - :attr:`value` is a :class:`namedtuple` with the follow properties.

                | - :attr:`n_decimal_places`: int - The number of decimal places
                    to use when storing the attribute value.
                | - :attr:`default_value`: str - The default value in Lightroom.
                | - :attr:`is_vector`: bool - True if it always has a
                    sign in a DNG file's XMP data, otherwise False.
                | - :attr:`is_ramped`: bool - True if it should be linearly ramped
                    (i.e. Temperature), otherwise False (i.e. Rating or Exposure)

        :rtype: dict(bytes: namedtuple(int, str, bool, bool))
        """
        return d_cnst.XMP_TAGS

    def __str__(self):
        return f'DNG {self.path}'
