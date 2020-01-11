from typing import Union

from brilliantimagery.dng import DNG

from ._meta_constants import META_TO_DNG


class MetaImage:
    """
    A representation of an image file.

    Only DNG image files are presently supported.

    Arguments:
        path (string): The path to an existing image file file.

    Attributes:
        image (DNG): A representation of the underlying image file
        brightness (float): A value representing the brightness of the image.
    """
    def __init__(self, path: str):
        """
        Initializes an image file representation.

        :param str path: Path to the image file.
        """
        self.image = DNG(path)
        self.brightness = 0

    def get_capture_datetime(self):
        """
        Gets when the image was captured.

        The return value may be formatted as a datetime or unix
        time stamp depending on the available information. The format
        should be consistent between images captured on the same camera
        and processed with the same workflow.

        :return: A creation time.
        :rtype: str
        """
        return self.image.get_capture_datetime()

    def get_image(self, rectangle=[0.0, 0.0, 1.0, 1.0], sub_image_type='RAW'):
        """
        Get the desired portion of the desired reference image.

        No transforms such as white balancing or exposure compensation
        are performed so the image may not look as expected (they're
        often too green).

        The rendering algorithm is relatively rudimentary so the
        results will be less refined than some other renderers.

        Note that the output is a float in the range of 0 to 1 so for many
        applications it'll have to be scaled.

        While many (most?) cameras are, or could with relative ease
        be supported, some Fuji cameras (and presumably others)
        will require further development.

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

        :param str sub_image: selects which sub-image to return from the file.

            :attr:`RAW` to get the original, raw, image.

            :attr:`thumbnail` to get the thumbnail if present.

        :return: A 3D float array holding the rendered image.

            * The first dimension represents the color channels: Red, Green, Blue at indices 0, 1, and 2 respectively.
            * The second represents the width.
            * The third represents the height.

        :rtype: Numpy.ndarray

        """

        return self.image.get_image(list.copy(rectangle), sub_image_type)

    def get_brightness(self, rectangle=None, image=None):
        """
        Gets a reference brightness value for the image.

        Gets the median green value for the image.

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

        self.brightness = self.image.get_brightness(rectangle, image)
        return self.brightness

    def get_rendered_shape(self):
        """
        Gets the dimensions of the raw image, as cropped and rendered.

        Dimensions are in units of pixels.

        :return: A list of ints where the first is the width and the
            second is the length (height) of the image.
        :rtype: list[int, int]
        """

        return self.image.get_rendered_shape()

    def get_default_shape(self):
        """
        Gets the dimensions of the raw image, before it's edited or cropped.

        Dimensions are in units of pixels.

        :return: A list of ints where the first is the width and the
            second is the length (height) of the image.
        :rtype: list[int, int]
        """

        return self.image.get_default_shape()

    def get_xmp_attribute(self, xmp_attribute: Union[bytes, str]):
        """
        Gets the value of an XMP attribute.

        Only works for attributes with numeric values.

        :param bytes xmp_attribute: The attribute to be interrogated.
            Must include the full attribute name, the part before and after the :attr:`:``

        :return: The value of the attribute if it's present and numeric, otherwise :attr:`None`.
        :rtype: float or None
        """

        if isinstance(xmp_attribute, bytes):
            return self.image.get_xmp().get(xmp_attribute)
        else:
            return self.image.get_xmp().get(META_TO_DNG[xmp_attribute])

    def set_xmp_attribute(self, xmp_attribute: Union[bytes, str], value: Union[int, float, str]):
        """
        Updates the stored value of an XMP attribute.

        Cannot update attributes that aren't already present. If an
        attribute wasn't previously present it can't be
        updated.

        Only updates the representation in the :class:`DNG` object.
        :func:`DNG.store_xmp_field` and :func:`DNG.save` have to be called to
        permanently save the updated values.

        :param xmp_attribute: The XMP attribute to be updated. Should be
            a key from the :attr:`_dng_constants.XMP_TAGS` dict
        :param value: The number to be assigned to the attribute.
        :type value: int, float, or str

        :return: True if it's successful, False if it isn't, presumably
            because the attribute isn't present or the value was already
            stored.
        :rtype: bool
        """

        if isinstance(xmp_attribute, bytes):
            self.image.set_xmp_attribute(xmp_attribute, value)
        else:
            self.image.set_xmp_attribute(META_TO_DNG[xmp_attribute], value)

    def store_xmp_field(self):
        """
        Consolidate updated XMP attributes in the XMP data.

        If this isn't called, the XMP data won't be updated in the
        file even if :func:`DNG.save` is called.

        :return: None
        """

        self.image.store_xmp_field()

    def save(self):
        """
        Overwrites the dng's XMP data with the updated XMP data.

        :return: None
        """

        self.image.save()

    @property
    def is_key_frame(self):
        """
        Says whether or not an image is a reference frame.

        For timelapse sequences, specifies whether or not the given image is
        intended to be used as a reference frame. This is determined by the
        image star rating and whether or not it matches the number of stars
        that a DNG image must have to be considered a reference frame, 3 by
        default.

        :return: True if it's a reference frame, otherwise false.
        :rtype: bool

        """

        return self.image.is_key_frame

    def get_xmp(self):
        """
        Gets the stored XMP data from the represented dng file.

        The XMP data holds all of the edits that have been made in Lightroom.

        :return: The xmp data as a dict with the keys being the properties
            as found in the XMP data and values being the associated values
            as floats.
        :rtype: dict[bytes, float]
        """

        return self.image.get_xmp()

    def get_relevant_xmp_attributes(self):
        """
        Gets the inclusive set of relevant XMP attributes.

        These are attributes that are edited with photo editing software
        such as exposure, rating, and saturation. Irrelevant attributes,
        from a photo editing perspective, such as when the photo was
        taken, are not returned.

        :return: A :class:`dict` of the below key value pairs:

            | - :attr:`key` is the property name.
            | - :attr:`value` is a :class:`namedtuple` with the follow properties.

                | - :attr:`n_decimal_places`: int - The number of decimal places
                    to use when storing the property value.
                | - :attr:`default_value`: str - The default value in Lightroom.
                | - :attr:`is_vector`: bool - True if it always has a
                    sign in the XMP data, otherwise False.
                | - :attr:`is_ramped`: bool - True if it should be linearly ramped
                    (i.e. Temperature), otherwise False (i.e. Rating)

        :rtype: dict(bytes: namedtuple(int, str, bool, bool))
        """

        return self.image.get_relevant_xmp_attributes()
