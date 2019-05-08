from typing import Union

from BrilliantImagery.dng import DNG

from ._meta_constants import META_TO_DNG


class MetaImage:
    """
    A representation of an image file.

    Only DNG image files are supported.

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
        self.image.parse()
        self.brightness = 0

    def get_capture_datetime(self):
        """
        Gets the datetime for when the image was captured.

        May return any of a variety of formats depending on the
        available information.

        :return:
        :rtype:
        :return: A creation time formatted as a string.
        """
        return self.image.get_capture_datetime()

    def get_image(self, rectangle=[0.0, 0.0, 1.0, 1.0], sub_image_type='RAW'):
        return self.image.get_image(list.copy(rectangle), sub_image_type)

    def get_brightness(self, rectangle=None, image=None):
        self.brightness = self.image.get_brightness(rectangle, image)
        return self.brightness

    def rendered_shape(self):
        return self.image.rendered_shape()

    def default_shape(self):
        return self.image.default_shape()

    def get_xmp_attribute(self, xmp_attribute: Union[bytes, str]):
        if isinstance(xmp_attribute, bytes):
            return self.image.get_xmp_attribute(xmp_attribute)
        else:
            return self.image.get_xmp_attribute(META_TO_DNG[xmp_attribute])

    def set_xmp_attribute(self, xmp_attribute: Union[bytes, str], value: Union[int, float, str]):
        if isinstance(xmp_attribute, bytes):
            self.image.set_xmp_attribute(xmp_attribute, value)
        else:
            self.image.set_xmp_attribute(META_TO_DNG[xmp_attribute], value)

    def store_xmp_field(self):
        self.image.store_xmp_field()

    def save(self):
        self.image.save()

    def is_reference_frame(self):
        return self.image.is_reference_frame()

    def get_xmp(self):
        return self.image.get_xmp()

    def get_possible_xmp_attributes(self):
        return self.image.get_possible_xmp_attributes()
