import numpy as np

from dng import DNG

from ._meta_constants import META_TO_DNG


class MetaImage:
    def __init__(self, path):
        self.image = DNG(path)
        self.median_green_value = 0

    def get_capture_datetime(self):
        return self.image.get_capture_datetime()

    def get_image(self, rectangle=[0.0, 0.0, 1.0, 1.0], sub_image='RAW'):
        return self.image.get_image(list.copy(rectangle), sub_image)

    def set_median_green_value(self, image):
        self.median_green_value = np.median(image[1, :, :])

    def rendered_shape(self):
        return self.image.rendered_shape()

    def default_shape(self):
        return self.image.default_shape()

    def get_crops(self):
        return self.image.get_crops()

    def update_xmp_attribute(self, xmp_property, value):
        self.image.update_xmp_attribute(META_TO_DNG[xmp_property], value)

    def store_xmp_field(self):
        self.image.store_xmp_field()

    def save(self):
        self.image.save()
