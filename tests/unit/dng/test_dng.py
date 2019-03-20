from collections import defaultdict
from io import BytesIO

import pytest
from unittest.mock import patch
import numpy as np

from BrilliantImagery.dng import DNG

# from tests._test_utils import data_folder

default_xmp = {b'crs:Temperature': 6500.0, b'crs:Tint': 10.0, b'crs:Saturation': 9.0, b'crs:Vibrance': 29.0,
               b'crs:Sharpness': 25.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:RedSaturation': 0.0,
               b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0,
               b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0,
               b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 0.0,
               b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0,
               b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0,
               b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0,
               b'crs:SaturationAdjustmentBlue': 0.0, b'crs:SaturationAdjustmentPurple': 0.0,
               b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0,
               b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0,
               b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0,
               b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0,
               b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0,
               b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0,
               b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0,
               b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0,
               b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0, b'crs:ColorNoiseReductionDetail': 50.0,
               b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0,
               b'crs:Contrast2012': 0.0, b'crs:Highlights2012': 24.0, b'crs:Shadows2012': -24.0,
               b'crs:Whites2012': 31.0, b'crs:Blacks2012': -10.0, b'crs:Clarity2012': 0.0,
               b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0,
               b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0,
               b'crs:Dehaze': 0.0, b'crs:CropLeft': 0.050467, b'crs:CropBottom': 0.969144, b'crs:CropRight': 0.969144,
               b'crs:CropTop': 0.050467, b'xmp:Rating': 2.0, b'crs:Exposure2012': 0.2}

updated_xmp = {b'crs:Temperature': 700.0, b'crs:Tint': 10.0, b'crs:Saturation': 9.0, b'crs:Vibrance': 29.0,
               b'crs:Sharpness': 30.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:RedSaturation': 0.0,
               b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0,
               b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0,
               b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 0.0,
               b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0,
               b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0,
               b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0,
               b'crs:SaturationAdjustmentBlue': 0.0, b'crs:SaturationAdjustmentPurple': 0.0,
               b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0,
               b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0,
               b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0,
               b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0,
               b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0,
               b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0,
               b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0,
               b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0,
               b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0, b'crs:ColorNoiseReductionDetail': 50.0,
               b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0,
               b'crs:Contrast2012': 0.0, b'crs:Highlights2012': 24.0, b'crs:Shadows2012': -24.0,
               b'crs:Whites2012': 31.0, b'crs:Blacks2012': -10.0, b'crs:Clarity2012': 0.0,
               b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0,
               b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0,
               b'crs:Dehaze': 0.0, b'crs:CropLeft': 0.050467, b'crs:CropBottom': 0.969144, b'crs:CropRight': 0.969144,
               b'crs:CropTop': 0.050467, b'xmp:Rating': 2.0, b'crs:Exposure2012': 0.2}

# with mock.patch('builtins.open', mocker.mock_open(read_data=b'II')) as f:
#     img.parse()
#     assert img._byte_order == b'II'

def test__byte_order_bII_success():
    # GIVEN an initialized DNG
    from BrilliantImagery.dng import DNG
    dng = DNG('fake.file')

    # WHEN the dng has small ended IO bytes passes in
    dng._get_byte_order(BytesIO(b'II'))

    # THEN the byte order is as expected
    assert dng._byte_order == '<'


def test__byte_order_bMM_success():
    # GIVEN an initialized DNG
    dng = DNG('fake.file')

    # WHEN the dng has big ended IO bytes passes in
    dng._get_byte_order(BytesIO(b'MM'))

    # THEN the byte order is as expected
    assert dng._byte_order == '>'


def test__byte_order_bad_raises():
    # GIVEN an initialized DNG
    dng = DNG('fake.file')
    expected = "Byte order should be b'II' or b'MM' but is"

    # WHEN the dng has small bad IO bytes passes in
    # THEN and excepton is raised
    with pytest.raises(ValueError) as e:
        dng._get_byte_order(BytesIO(b'bad'))
        err_msg = e.value.args[0]
        assert expected in err_msg


def test_get_capture_datetime(dng_canon_6d):
    # GIVEN an initialized DNG file and it's capture datetime
    expected = '2017-09-07T16:01:38.03'

    # WHEN parsed
    dng_canon_6d.parse()
    actual = dng_canon_6d.get_capture_datetime()

    # THEN the capture datetime is as expected
    assert expected == actual


def test_get_image_cropped_raw(dng_canon_6d, numpy_cropped_canon_6d):
    # GIVEN an initialized dng and a rendered image with its rendered area
    expected_image, rendered_area = numpy_cropped_canon_6d

    # WHEN it's parsed and then rendered
    dng_canon_6d.parse()
    actual_image = dng_canon_6d.get_image(rendered_area)

    # THEN the rendered image is as expected
    assert np.array_equal(actual_image, expected_image)


def test_get_image_full_thumbnail(dng_canon_6d, numpy_thumbnail_canon_6d):
    # GIVEN an initialized dng and a rendered image with its rendered area

    # WHEN it's parsed and then the thumbnail's rendered
    dng_canon_6d.parse()
    actual_image = dng_canon_6d.get_image(sub_image_type='thumbnail')

    # THEN the rendered image is as expected
    assert np.array_equal(actual_image, numpy_thumbnail_canon_6d)


@pytest.mark.skip()
def test_get_xmp(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    assert img.get_xmp() == default_xmp


@pytest.mark.skip()
def test_set_xmp_attribute(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    img.set_xmp_attribute(b'crs:Temperature', 700.0)
    img.set_xmp_attribute(b'crs:Sharpness', 30.0)
    assert img.get_xmp() == updated_xmp


@pytest.mark.skip()
def test_store_xmp_field(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    img.set_xmp_attribute(b'crs:Temperature', 700.0)
    img.set_xmp_attribute(b'crs:Sharpness', 30.0)
    img.store_xmp_field()
    img._xmp = defaultdict(dict)
    assert img.get_xmp() == updated_xmp


@pytest.mark.skip()
def test_rendered_shape(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    assert img.rendered_shape() == [5027, 3351]


@pytest.mark.skip()
def test_default_shape(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    assert img.default_shape() == [5472, 3648]


@pytest.mark.skip()
def test_get_xmp_attribute(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    assert img.get_xmp_attribute(b'crs:Exposure2012') == 0.2


@pytest.mark.skip()
def test_get_brightness(data_folder_path):
    img = DNG(str(data_folder_path / 'test_image_canon_6d.dng'))
    img.parse()
    assert img.get_brightness(rectangle=[0.3, 0.3, 0.4, 0.4]) == np.float32(0.067557134)
