import collections

import cv2
import numpy as np


_Point = collections.namedtuple('_Point', 'x y')


def find_misalignment(image0, image1, rectangle, keep_brightness, time_index):
    rgb_image0 = image0.get_image(rectangle)
    rgb_image1 = image1.get_image(rectangle)
    image1.misalignment = _find_offset(rgb_image0, rgb_image1)
    if keep_brightness:
        image1.get_median_green_value(image=rgb_image1)

    return time_index, image1


def _find_offset(im1, im2):
    image_1_gray = (im1[0, :, :] + im1[0, :, :] + im1[0, :, :]) / 3
    image_2_gray = (im2[0, :, :] + im2[0, :, :] + im2[0, :, :]) / 3

    image_1_median = np.median(image_1_gray)
    image_2_median = np.median(image_2_gray)

    image_1_gray /= image_1_median / image_2_median

    mapper = cv2.reg_MapperGradShift()
    mappPyr = cv2.reg_MapperPyramid(mapper)

    resMap = mappPyr.calculate(image_1_gray, image_2_gray)
    mapShift = cv2.reg_MapTypeCaster().toShift(resMap)

    shift = mapShift.getShift()
    return [shift[1][0], shift[0][0]]


def _get_brightness_deltas(rgb_image):
    avg_pix_brightness = np.add(rgb_image[0, :, :], np.add(rgb_image[1, :, :], rgb_image[2, :, :]))
    shifted_left = avg_pix_brightness[:-2, 1:-1]
    shifted_up = avg_pix_brightness[1:-1, :-2]
    middle = avg_pix_brightness[1:-1, 1:-1]
    middle = np.add(middle, middle)

    return np.subtract(middle, np.add(shifted_left, shifted_up))


def misalignment_bounding_box(images):
    min_x = 500
    max_x = -500
    min_y = 500
    max_y = -500

    for image in images:
        if image.misalignment[0] < min_x:
            min_x = image.misalignment[0]
        if image.misalignment[0] > max_x:
            max_x = image.misalignment[0]
        if image.misalignment[1] < min_y:
            min_y = image.misalignment[1]
        if image.misalignment[1] > max_y:
            max_y = image.misalignment[1]

    return min_x, min_y, max_x, max_y


def update_xmp_attributes(image, left, top, right, bottom):
    image.set_xmp_attribute('CropLeft', left)
    image.set_xmp_attribute('CropTop', top)
    image.set_xmp_attribute('CropRight', right)
    image.set_xmp_attribute('CropBottom', bottom)

    return image
