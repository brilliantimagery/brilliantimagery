import collections

import numpy as np

_Point = collections.namedtuple('Point', 'x y')


def find_offset(image0, image1, max_misalignment):
    img0 = _get_brightness_deltas(image0)
    img1 = _get_brightness_deltas(image1)

    deltas = dict()

    for dx in range(-max_misalignment, max_misalignment):
        for dy in range(-max_misalignment, max_misalignment):
            # delta = 0
            # for ix in range(max_misalignment, img0.shape[0] - max_misalignment):
            #     for iy in range(max_misalignment, img0.shape[1] - max_misalignment):
            #         delta += abs(img0[ix, iy] - img1[ix + dx, iy + dy])
            d = np.subtract(img0[max_misalignment:-max_misalignment, max_misalignment:-max_misalignment],
                            img1[max_misalignment + dx:-(max_misalignment - dx),
                                 max_misalignment + dy:-(max_misalignment - dy)])
            # a = np.abs(d)
            # s = np.sum(np.abs(d))
            deltas[_Point(dx, dy)] = np.sum(np.abs(d))
            # deltas[_Point(dx, dy)] = np.sum(np.abs(np.subtract(image0[max_misalignment:
            #                                                           -max_misalignment],
            #                                                    image1[max_misalignment + dx:
            #                                                           -(max_misalignment + dx)])))
            # deltas[_Point(dx, dy)] = delta

    min_delta = min(deltas.values())

    for k, v in deltas.items():
        if v == min_delta:
            return k


def _get_brightness_deltas(image):
    avg_pix_brightness = np.add(image[0, :, :], np.add(image[1, :, :], image[2, :, :]))
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
    image.update_xmp_attribute('CropLeft', left)
    image.update_xmp_attribute('CropTop', top)
    image.update_xmp_attribute('CropRight', right)
    image.update_xmp_attribute('CropBottom', bottom)

    return image
