import collections

import cv2
import numpy as np


_Point = collections.namedtuple('_Point', 'x y')


def find_misalignment(reference_rgb_image, probe_image, rectangle, max_misalignment_to_check,
                      keep_brightness, time_index):
    probe_rgb_image = probe_image.get_image(rectangle)
    # probe_image.misalignment = _find_offset(reference_rgb_image, probe_rgb_image, max_misalignment_to_check)
    probe_image.misalignment = opencv_stuff(reference_rgb_image, probe_rgb_image)
    if keep_brightness:
        probe_image.get_median_green_value(image=probe_rgb_image)

    return time_index, probe_image


def opencv_stuff(im1, im2):

    im1_gray = (im1[0, :, :] + im1[0, :, :] + im1[0, :, :]) / 3
    im2_gray = (im2[0, :, :] + im2[0, :, :] + im2[0, :, :]) / 3

    mapper = cv2.reg_MapperGradShift()
    mappPyr = cv2.reg_MapperPyramid(mapper)

    resMap = mappPyr.calculate(im1_gray, im2_gray)
    mapShift = cv2.reg_MapTypeCaster().toShift(resMap)

    a = mapShift.getShift()
    c = a[0][0], a[1][0]
    return _Point(round(a[0][0]), round(a[1][0]))


def _find_offset(reference_rgb_image, probe_rgb_image, max_misalignment_to_check):
    img0 = _get_brightness_deltas(reference_rgb_image)
    img1 = _get_brightness_deltas(probe_rgb_image)

    deltas = dict()

    for dx in range(-max_misalignment_to_check, max_misalignment_to_check):
        for dy in range(-max_misalignment_to_check, max_misalignment_to_check):
            d = np.subtract(img0[max_misalignment_to_check:-max_misalignment_to_check,
                            max_misalignment_to_check:-max_misalignment_to_check],
                            img1[max_misalignment_to_check + dx:-(max_misalignment_to_check - dx),
                            max_misalignment_to_check + dy:-(max_misalignment_to_check - dy)])
            deltas[_Point(dx, dy)] = np.sum(np.abs(d))

    min_delta = min(deltas.values())

    for k, v in deltas.items():
        if v == min_delta:
            return k


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
        if image.misalignment.x < min_x:
            min_x = image.misalignment.x
        if image.misalignment.x > max_x:
            max_x = image.misalignment.x
        if image.misalignment.y < min_y:
            min_y = image.misalignment.y
        if image.misalignment.y > max_y:
            max_y = image.misalignment.y

    return min_x, min_y, max_x, max_y


def update_xmp_attributes(image, left, top, right, bottom):
    image.set_xmp_attribute('CropLeft', left)
    image.set_xmp_attribute('CropTop', top)
    image.set_xmp_attribute('CropRight', right)
    image.set_xmp_attribute('CropBottom', bottom)

    return image
