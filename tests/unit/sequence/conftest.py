from collections import namedtuple
from copy import deepcopy
from pathlib import Path

import pytest

from brilliantimagery.sequence import Sequence

rectangle = [0.1, 0.1, 0.3, 0.3]
offsets = [[0, 0], [1, -3], [2, 4], [-10, 11], [5, 17], [-8, 3], [2, -1], [0, -5], [8, 8], [-9, 1]]

Crops = namedtuple('Crops', ['left', 'top', 'right', 'bottom'])


@pytest.fixture()
def _base_sequence(data_folder_path):
    sequence = Sequence(str(data_folder_path / 'dng' / 'sequence'))
    sequence._images = {Path(name).name: image for name, image in sequence._images.items()}
    return sequence


@pytest.fixture()
def _sequence_info(_base_sequence):
    times = sorted(_base_sequence._images.keys())
    image = _base_sequence._images[times[0]].image
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

    return (_base_sequence, times, pix_per_percent_width, pix_per_percent_length,
            left_crop, top_crop, right_crop, bottom_crop)


@pytest.fixture()
def sequence(_sequence_info):
    (_sequence, times, pix_per_prcnt_wdth, pix_per_prcnt_lngth,
     left_crop, top_crop, right_crop, bottom_crop) = _sequence_info

    for offset, time in zip(offsets, times):
        image = _sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft', left_crop - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropTop', top_crop - pix_per_prcnt_lngth * offset[1])
        image.set_xmp_attribute(b'crs:CropRight', right_crop - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom', bottom_crop - pix_per_prcnt_lngth * offset[1])
        image.store_xmp_field()

    return _sequence, deepcopy(rectangle), offsets


@pytest.fixture()
def stabelized_sequence(_base_sequence):
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

    for time, offset in zip(_base_sequence._images, offsets):
        _base_sequence._images[time].misalignment = offset

    return _base_sequence, deepcopy(rectangle), crops


@pytest.fixture()
def sequence_minimal_crop(_sequence_info):
    (_sequence, times, pix_per_prcnt_wdth, pix_per_prcnt_lngth,
     left_crop, top_crop, right_crop, bottom_crop) = _sequence_info

    for offset, time in zip(offsets, times):
        image = _sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft',
                                (3 * pix_per_prcnt_wdth) - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropTop',
                                (3 * pix_per_prcnt_lngth) - pix_per_prcnt_lngth * offset[1])
        image.set_xmp_attribute(b'crs:CropRight',
                                (1 - 3 * pix_per_prcnt_wdth) - pix_per_prcnt_wdth * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom',
                                (1 - 3 * pix_per_prcnt_lngth) - pix_per_prcnt_lngth * offset[1])
        image.store_xmp_field()

    return _sequence, deepcopy([0.1, 0.1, 0.4, 0.4]), offsets


@pytest.fixture()
def stabelized_sequence_minimal_crop(_base_sequence):
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

    for time, offset in zip(_base_sequence._images, offsets):
        _base_sequence._images[time].misalignment = [o * 10 for o in offset]

    return _base_sequence, deepcopy(rectangle), crops


@pytest.fixture()
def sequence_wo_exposure_w_expected_values(_base_sequence):
    xmp_update = [['dng_canon_6d_0001.dng', {b'xmp:Rating': 3,
                                             b'crs:Temperature': 6000,
                                             b'crs:Exposure2012': 1,
                                             b'crs:Contrast2012': 0}],
                  ['dng_canon_6d_0004.dng', {b'xmp:Rating': 3,
                                             b'crs:Temperature': 7500,
                                             b'crs:Exposure2012': 2.5,
                                             b'crs:Contrast2012': 30}],
                  ['dng_canon_6d_0006.dng', {b'xmp:Rating': 3,
                                             b'crs:Temperature': 7000,
                                             b'crs:Exposure2012': 1.5,
                                             b'crs:Contrast2012': 20}]
                  ]
    non_exp_xmp = {'dng_canon_6d_0001.dng': {b'crs:Temperature': 6000,
                                             b'crs:Contrast2012': 0.0},
                   'dng_canon_6d_0002.dng': {b'crs:Temperature': 6500,
                                             b'crs:Contrast2012': 10.0},
                   'dng_canon_6d_0003.dng': {b'crs:Temperature': 7000,
                                             b'crs:Contrast2012': 20.0},
                   'dng_canon_6d_0004.dng': {b'crs:Temperature': 7500,
                                             b'crs:Contrast2012': 30.0},
                   'dng_canon_6d_0005.dng': {b'crs:Temperature': 7250,
                                             b'crs:Contrast2012': 25.0},
                   'dng_canon_6d_0006.dng': {b'crs:Temperature': 7000,
                                             b'crs:Contrast2012': 20.0},
                   }
    expected_exp = {'dng_canon_6d_0001.dng': 1,
                    'dng_canon_6d_0002.dng': 1.5328466346945315,
                    'dng_canon_6d_0003.dng': 1.9187567079026229,
                    'dng_canon_6d_0004.dng': 2.5,
                    'dng_canon_6d_0005.dng': 2.0837716217061923,
                    'dng_canon_6d_0006.dng': 1.5,
                    }

    for image_time, xmp in xmp_update:
        for property, value in xmp.items():
            _base_sequence._images[image_time].set_xmp_attribute(property, value)

    [i.store_xmp_field() for i in _base_sequence._images.values()]

    return _base_sequence, non_exp_xmp, expected_exp, deepcopy(rectangle)


@pytest.fixture()
def sequence_w_exposure_and_expected_values(sequence_wo_exposure_w_expected_values):
    import numpy as np
    _sequence, non_exp_xmp, expected_exp, rectangle = sequence_wo_exposure_w_expected_values

    times = sorted(_sequence._images.keys())

    for time, brightness in zip(times[:3], np.arange(0.1, 0.15, 0.01)):
        _sequence._images[time].brightness = brightness

    for time, brightness in zip(times[3:], np.arange(0.11, 0.02, -0.02)):
        _sequence._images[time].brightness = brightness

    expected_exp = {'dng_canon_6d_0001.dng': 1,
                    'dng_canon_6d_0002.dng': 1.631215732498853,
                    'dng_canon_6d_0003.dng': 2.0045093171865456,
                    'dng_canon_6d_0004.dng': 2.5,
                    'dng_canon_6d_0005.dng': 2.1880559936852597,
                    'dng_canon_6d_0006.dng': 1.5,
                    }

    return _sequence, non_exp_xmp, expected_exp, rectangle


# TODO: refactor with above stuff
@pytest.fixture()
def rampable_and_stablizable_sequence(sequence_wo_exposure_w_expected_values):
    _sequence, non_exp_xmp, expected_exp, rectangle = sequence_wo_exposure_w_expected_values

    times = sorted(_sequence._images.keys())
    image = _sequence._images[times[0]].image
    [i.get_xmp() for i in _sequence._images.values()]
    # image.get_xmp()
    image._get_fields_required_to_render('raw')
    image_width = image._used_fields['image_width']
    image_length = image._used_fields['image_length']

    pix_per_percent_width = 1 / image_width
    pix_per_percent_length = 1 / image_length

    left_crop = image._xmp[b'crs:CropLeft'].get('val', 0)
    top_crop = image._xmp[b'crs:CropTop'].get('val', 0)
    right_crop = image._xmp[b'crs:CropRight'].get('val', 1)
    bottom_crop = image._xmp[b'crs:CropBottom'].get('val', 1)

    for offset, time in zip(offsets, times):
        image = _sequence._images[time].image
        image.set_xmp_attribute(b'crs:CropLeft', left_crop - pix_per_percent_width * offset[0])
        image.set_xmp_attribute(b'crs:CropTop', top_crop - pix_per_percent_length * offset[1])
        image.set_xmp_attribute(b'crs:CropRight', right_crop - pix_per_percent_width * offset[0])
        image.set_xmp_attribute(b'crs:CropBottom', bottom_crop - pix_per_percent_length * offset[1])
        image.store_xmp_field()

    crops = [Crops(0.050467, 0.050467, 0.969144, 0.969144),
             Crops(0.050486, 0.050381, 0.969163, 0.969058),
             Crops(0.050506, 0.050582, 0.969183, 0.969259),
             Crops(0.050274, 0.050783, 0.968951, 0.96946),
             Crops(0.050564, 0.050955, 0.969241, 0.969632),
             Crops(0.050312, 0.050553, 0.968989, 0.96923),
             Crops(0.050506, 0.050438, 0.969183, 0.969115),
             Crops(0.050467, 0.050323, 0.969144, 0.969),
             Crops(0.050622, 0.050697, 0.969299, 0.969374),
             Crops(0.050293, 0.050496, 0.96897, 0.969173)]

    return _sequence, non_exp_xmp, expected_exp, rectangle, crops
