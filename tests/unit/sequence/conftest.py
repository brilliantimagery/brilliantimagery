from copy import deepcopy

import pytest

from BrilliantImagery.sequence import Sequence
from BrilliantImagery.sequence._stabilize import Stabilizer


rectangle = [0.1, 0.1, 0.3, 0.3]
offsets = [[0, 0], [1, -3], [2, 4], [-10, 11], [5, 17], [-8, 3], [2, -1], [0, -5], [8, 8], [-9, 1]]


@pytest.fixture()
def image_sequence(data_folder_path):
    sequence = Sequence(str(data_folder_path))
    time = next(iter(sequence._images))
    image = sequence._images[time]
    for i in range(1, 10):
        sequence._images[time + str(i).zfill(3)] = deepcopy(image)
    return sequence


@pytest.fixture()
def _stabilizer_sequence__init__(image_sequence):
    times = sorted(image_sequence._images.keys())
    image = image_sequence._images[times[0]].image
    image.get_xmp()
    image._get_fields_required_to_render('raw')
    image_width = image._used_fields['image_width']
    image_length = image._used_fields['image_length']

    pix_per_percent_width = 1 / image_width
    pix_per_percent_length = 1 / image_length

    left_crop = image._xmp[b'crs:CropLeft'].get('val', 0)
    top_crop = image._xmp[b'crs:CropTop'].get('val', 0)
    right_crop = image._xmp[b'crs:CropRight'].get('val', 1)
    bottom_crop = image._xmp[b'crs:CropBottom'].get('val', 1)

    return (image_sequence, times,
            pix_per_percent_width, pix_per_percent_length,
            left_crop, top_crop, right_crop, bottom_crop)


@pytest.fixture()
def stabilizer_sequence(_stabilizer_sequence__init__):
    (image_sequence, times,
     pix_per_prcnt_wdth, pix_per_prcnt_lngth,
     left_crop, top_crop, right_crop, bottom_crop) = _stabilizer_sequence__init__

    for offset, time in zip(offsets, times):
        image = image_sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft', left_crop - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropTop', top_crop - pix_per_prcnt_lngth * offset[1])
        image.set_xmp_attribute(b'crs:CropRight', right_crop - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom', bottom_crop - pix_per_prcnt_lngth * offset[1])
        image.store_xmp_field()

    return Stabilizer(image_sequence._images, rectangle), offsets


@pytest.fixture()
def stabilizer_sequence_minimal_crop(_stabilizer_sequence__init__):
    (image_sequence, times,
     pix_per_prcnt_wdth, pix_per_prcnt_lngth,
     left_crop, top_crop, right_crop, bottom_crop) = _stabilizer_sequence__init__

    for offset, time in zip(offsets, times):
        image = image_sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft', (3 * pix_per_prcnt_wdth) - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropTop', (3 * pix_per_prcnt_lngth) - pix_per_prcnt_lngth * offset[1])
        image.set_xmp_attribute(b'crs:CropRight', (1 - 3 * pix_per_prcnt_wdth) - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom', (1 - 3 * pix_per_prcnt_lngth) - pix_per_prcnt_lngth * offset[1])
        image.store_xmp_field()

    return Stabilizer(image_sequence._images, rectangle), offsets
