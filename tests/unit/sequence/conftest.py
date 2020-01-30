from collections import namedtuple
from copy import deepcopy
from pathlib import Path

import pytest

from brilliantimagery.sequence import Sequence

rectangle = [0.67, 0.4, 0.79, 0.58]
offsets = [[0, 0], [-4.0, 1.0], [-0.0, -0.0], [-4, 1], [-0, 0], [-4, 1], [8, 8]]

Crops = namedtuple('Crops', ['left', 'top', 'right', 'bottom'])


@pytest.fixture()
def _base_sequence(data_folder_path):
    sequence = Sequence(str(data_folder_path / 'dng' / 'sequence'))
    sequence._images = {Path(name).name: image for name, image in sequence._images.items()}
    return sequence


# @pytest.fixture()
# def _sequence_info(_base_sequence):
#     times = sorted(_base_sequence._images.keys())
#     image = _base_sequence._images[times[0]].image
#     image.get_xmp()
#     image._get_fields_required_to_render('raw')
#     image_width = image._used_fields['image_width']
#     image_length = image._used_fields['image_length']
#
#     pix_per_percent_width = 1 / image_width
#     pix_per_percent_length = 1 / image_length
#
#     left_crop = image._xmp[b'crs:CropLeft'].get('val', 0)
#     top_crop = image._xmp[b'crs:CropTop'].get('val', 0)
#     right_crop = image._xmp[b'crs:CropRight'].get('val', 1)
#     bottom_crop = image._xmp[b'crs:CropBottom'].get('val', 1)
#
#     return (_base_sequence, times, pix_per_percent_width, pix_per_percent_length,
#             left_crop, top_crop, right_crop, bottom_crop)


# @pytest.fixture()
# def sequence(_sequence_info):
#     (_sequence, times, pix_per_prcnt_wdth, pix_per_prcnt_lngth,
#      left_crop, top_crop, right_crop, bottom_crop) = _sequence_info
#
#     for offset, time in zip(offsets, times):
#         image = _sequence._images[time].image
#         image.set_xmp_attribute(b'crs:CropLeft', left_crop - pix_per_prcnt_wdth * offset[0])
#         image.set_xmp_attribute(b'crs:CropTop', top_crop - pix_per_prcnt_lngth * offset[1])
#         image.set_xmp_attribute(b'crs:CropRight', right_crop - pix_per_prcnt_wdth * offset[0])
#         image.set_xmp_attribute(b'crs:CropBottom', bottom_crop - pix_per_prcnt_lngth * offset[1])
#         image.store_xmp_field()
#
#     return _sequence, deepcopy(rectangle), offsets@pytest.fixture()
@pytest.fixture()
def sequence(_base_sequence):
    return _base_sequence, deepcopy(rectangle), offsets


@pytest.fixture()
def stabelized_sequence(_base_sequence):
    # crops = [Crops(0.048838, 0.142125, 0.89261, 0.852893),
    #          Crops(0.048191, 0.141358, 0.891963, 0.852126),
    #          Crops(0.049269, 0.143658, 0.893041, 0.854426),
    #          Crops(0.046034, 0.146724, 0.889806, 0.857492),
    #          Crops(0.050132, 0.149024, 0.893904, 0.859792),
    #          Crops(0.04625, 0.144041, 0.890022, 0.854809),
    #          ]
    crops = [Crops(0.048838, 0.142125, 0.89261, 0.852893),
             Crops(0.047975, 0.142508, 0.891747, 0.853276),
             Crops(0.048838, 0.142125, 0.89261, 0.852893),
             Crops(0.047975, 0.142508, 0.891747, 0.853276),
             Crops(0.048838, 0.142125, 0.89261, 0.852893),
             Crops(0.047975, 0.142508, 0.891747, 0.853276),
             ]

    for time, offset in zip(_base_sequence._images, offsets):
        _base_sequence._images[time].misalignment = offset

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
                    'dng_canon_6d_0002.dng': 1.5366218653910104,
                    'dng_canon_6d_0003.dng': 1.9268323540914807,
                    'dng_canon_6d_0004.dng': 2.5,
                    'dng_canon_6d_0005.dng': 2.0880174422924322,
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

    # crops = [Crops(0.048838, 0.142125, 0.89261, 0.852893),
    #          Crops(0.047113, 0.142892, 0.890885, 0.85366),
    #          Crops(0.049269, 0.143658, 0.893041, 0.854426),
    #          Crops(0.045819, 0.146724, 0.889591, 0.857492),
    #          Crops(0.047328, 0.148258, 0.8911, 0.859026),
    #          Crops(0.045387, 0.145575, 0.889159, 0.856343),
    #          ]

    crops = [Crops(0.048838, 0.142125, 0.89261, 0.852893),
             Crops(0.047113, 0.142892, 0.890885, 0.85366),
             Crops(0.048838, 0.142125, 0.89261, 0.852893),
             Crops(0.047113, 0.142892, 0.890885, 0.85366),
             Crops(0.048838, 0.142125, 0.89261, 0.852893),
             Crops(0.047113, 0.142892, 0.890885, 0.85366),
             ]

    return _sequence, non_exp_xmp, expected_exp, rectangle, crops
