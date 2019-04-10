from collections import namedtuple
from copy import deepcopy

import pytest

from BrilliantImagery.sequence import Sequence
from BrilliantImagery.sequence._stabilize import Stabilizer


rectangle = [0.1, 0.1, 0.3, 0.3]
offsets = [[0, 0], [1, -3], [2, 4], [-10, 11], [5, 17], [-8, 3], [2, -1], [0, -5], [8, 8], [-9, 1]]

Crops = namedtuple('Crops', ['left', 'top', 'right', 'bottom'])


@pytest.fixture()
def _sequence(data_folder_path):
    sequence = Sequence(str(data_folder_path))
    time = next(iter(sequence._images))
    image = sequence._images[time]
    for i in range(1, 10):
        sequence._images[time + str(i).zfill(3)] = deepcopy(image)
    return sequence


@pytest.fixture()
def _stabilizer(_sequence):
    times = sorted(_sequence._images.keys())
    image = _sequence._images[times[0]].image
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

    return (_sequence, times,
            pix_per_percent_width, pix_per_percent_length,
            left_crop, top_crop, right_crop, bottom_crop)


@pytest.fixture()
def stabilizer(_stabilizer):
    (image_sequence, times,
     pix_per_prcnt_wdth, pix_per_prcnt_lngth,
     left_crop, top_crop, right_crop, bottom_crop) = _stabilizer

    for offset, time in zip(offsets, times):
        image = image_sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft', left_crop - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropTop', top_crop - pix_per_prcnt_lngth * offset[1])
        image.set_xmp_attribute(b'crs:CropRight', right_crop - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom', bottom_crop - pix_per_prcnt_lngth * offset[1])
        image.store_xmp_field()

    return Stabilizer(image_sequence._images, rectangle), offsets


@pytest.fixture()
def stabelized_stabilizer(_sequence):
    crops = [Crops(0.050467, 0.050467, 0.969144, 0.969144),
             Crops(0.050666, 0.049572, 0.969343, 0.968249),
             Crops(0.050865, 0.051661, 0.969542, 0.970338),
             Crops(0.048478, 0.05375, 0.967155, 0.972427),
             Crops(0.051462, 0.05554, 0.970139, 0.974217),
             Crops(0.048876, 0.051362, 0.967553, 0.970039),
             Crops(0.050865, 0.050169, 0.969542, 0.968846),
             Crops(0.050467, 0.048975, 0.969144, 0.967652),
             Crops(0.052058, 0.052854, 0.970735, 0.971531),
             Crops(0.048677, 0.050765, 0.967354, 0.969442)]

    for time, offset in zip(_sequence._images, offsets):
        _sequence._images[time].misalignment = offset

    return Stabilizer(_sequence._images, rectangle), crops



@pytest.fixture()
def stabilizer_minimal_crop(_stabilizer):
    (image_sequence, times,
     pix_per_prcnt_wdth, pix_per_prcnt_lngth,
     left_crop, top_crop, right_crop, bottom_crop) = _stabilizer

    for offset, time in zip(offsets, times):
        image = image_sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft', (3 * pix_per_prcnt_wdth) - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropTop', (3 * pix_per_prcnt_lngth) - pix_per_prcnt_lngth * offset[1])
        image.set_xmp_attribute(b'crs:CropRight', (1 - 3 * pix_per_prcnt_wdth) - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom', (1 - 3 * pix_per_prcnt_lngth) - pix_per_prcnt_lngth * offset[1])
        image.store_xmp_field()

    return Stabilizer(image_sequence._images, rectangle), offsets


@pytest.fixture()
def stabelized_stabilizer_minimal_crop(_sequence):
    crops = [Crops(0.086274, 0.116119, 0.933337, 0.903492),
             Crops(0.088263, 0.107166, 0.935327, 0.894539),
             Crops(0.090252, 0.128056, 0.937316, 0.915429),
             Crops(0.066381, 0.148945, 0.913445, 0.936318),
             Crops(0.09622, 0.16685, 0.943284, 0.954223),
             Crops(0.07036, 0.125072, 0.917423, 0.912445),
             Crops(0.090252, 0.113135, 0.937316, 0.900508),
             Crops(0.086274, 0.101198, 0.933337, 0.888571),
             Crops(0.102188, 0.139993, 0.949251, 0.927365),
             Crops(0.06837, 0.119103, 0.915434, 0.906476)]

    for time, offset in zip(_sequence._images, offsets):
        _sequence._images[time].misalignment = [o*10 for o in offset]

    return Stabilizer(_sequence._images, rectangle), crops
