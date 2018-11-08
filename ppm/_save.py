"""
Helper module for working with PPM files.
"""

import numpy as np


def save(raw_img, file_name, white_value):
    """
    Save raw image data to a ppm file.

    Saves the input data as a ppm file in the current working
    directory. Only works for RGB images and only works for data stored
    as hex values, no decimal support; as defined by the file format,
    only P6 files are supported.

    :param raw_img: A 3D numpy array of type int where dimension 0 is
    the color channel, dimension 1 is the x coordinate, and dimension 2
    is the y coordinate. The top left corner is the origin.
    :param file_name: The relative file name that's to be save to.
    :param white_value: The max color value, the value of white
    :return: None
    """
    img = list()

    img.append(ord('P'))

    if len(raw_img.shape) is 3:
        if raw_img.shape[0] > 1:
            img.append(ord('6'))

            img.append(0x0A)

            [img.append(ord(c)) for c in str(raw_img.shape[1])]

            img.append(0x20)

            [img.append(ord(c)) for c in str(raw_img.shape[2])]

            img.append(0x0A)

            [img.append(ord(c)) for c in str(white_value)]

            img.append(0x0A)

            for y in range(raw_img.shape[2]):
                for x in range(raw_img.shape[1]):
                    for c in range(raw_img.shape[0]):
                        img.append(raw_img[c, x, y])
        else:
            img.append(ord('5'))
    else:
        exit(-1)

    img = np.array(img, dtype=np.uint8)

    img.tofile(file_name)
