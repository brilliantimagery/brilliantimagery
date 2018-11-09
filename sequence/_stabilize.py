from . import _stabilize_util as sutil
from ._stabilize_util import _Point


class Stabilizer:
    def __init__(self, images, rectangle, max_pix_of_misalignment):
        self.images = images
        self._rectangle = rectangle
        self._max_pix_of_misalignment = max_pix_of_misalignment

    def find_misalignments(self, keep_brightness=False):
        images = self.images
        ordered_times = sorted(images.keys())
        image0 = images[ordered_times[0]].get_image(self._rectangle)

        if keep_brightness:
            images[ordered_times[0]].set_median_green_value(image0)

        images[ordered_times[0]].misalignment = _Point(0, 0)
        for time_index in range(1, len(ordered_times)):
            image1 = images[ordered_times[time_index]].get_image(self._rectangle)
            images[ordered_times[time_index]].misalignment = \
                sutil.find_offset(image0, image1, self._max_pix_of_misalignment)
            if keep_brightness:
                images[ordered_times[time_index]].set_median_green_value(image1)

    def update_xmp_attributes(self):
        example_image = next(iter(self.images.values()))
        min_x, min_y, max_x, max_y = sutil.misalignment_bounding_box(self.images.values())
        shape = example_image.rendered_shape()
        crops = example_image.get_crops()
        if (max_x < crops[0] * shape[0] and max_y < crops[1] * shape[1] and
                -min_x < (1 - crops[2]) * shape[0] and -min_y < (1 - crops[3]) * shape[1]):
            for image in self.images.values():
                left = crops[0] + image.misalignment.x / shape[0]
                top = crops[1] + image.misalignment.y / shape[1]
                right = crops[2] + image.misalignment.x / shape[0]
                bottom = crops[3] + image.misalignment.y / shape[1]
                image = sutil.update_xmp_attributes(image, left, top, right, bottom)
        else:
            for image in self.images.values():
                left = crops[0] + (max_x - min_x + image.misalignment.x) / shape[0]
                top = crops[1] + (max_y - min_y + image.misalignment.y) / shape[1]
                right = crops[2] + (-max_x + min_x + image.misalignment.x) / shape[0]
                bottom = crops[3] + (-max_y + min_y + image.misalignment.y) / shape[1]
                image = sutil.update_xmp_attributes(image, left, top, right, bottom)
