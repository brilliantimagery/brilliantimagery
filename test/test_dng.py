from collections import defaultdict

import numpy as np

from src.BrilliantImagery.dng import DNG


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


def test_get_capture_datetime():
    img = DNG('test_image_canon_6d.dng')
    assert img.get_capture_datetime() == '2017-09-07T16:01:38.03'


def test_get_image_cropped_raw():
    img = DNG('test_image_canon_6d.dng')
    test_image = img.get_image([1500/5030, 1450/3350, (1500+700)/5030, (1450+760)/3350])
    reference_image = np.load('test_image_canon_6d_cropped.npy')
    assert np.array_equal(test_image, reference_image)


def test_get_image_full_thumbnail():
    img = DNG('test_image_canon_6d.dng')
    test_image = img.get_image(sub_image_type='thumbnail')
    reference_image = np.load('test_image_canon_6d_thumb.npy')
    assert np.array_equal(test_image, reference_image)


def test_get_xmp():
    img = DNG('test_image_canon_6d.dng')
    assert img.get_xmp() == default_xmp


def test_set_xmp_attribute():
    img = DNG('test_image_canon_6d.dng')
    img.set_xmp_attribute(b'crs:Temperature', 700.0)
    img.set_xmp_attribute(b'crs:Sharpness', 30.0)
    assert img.get_xmp() == updated_xmp


def test_store_xmp_field():
    img = DNG('test_image_canon_6d.dng')
    img.set_xmp_attribute(b'crs:Temperature', 700.0)
    img.set_xmp_attribute(b'crs:Sharpness', 30.0)
    img.store_xmp_field()
    img._xmp = defaultdict(dict)
    assert img.get_xmp() == updated_xmp


def test_rendered_shape():
    img = DNG('test_image_canon_6d.dng')
    assert img.rendered_shape() == [5027, 3351]


def test_default_shape():
    img = DNG('test_image_canon_6d.dng')
    assert img.default_shape() == [5472, 3648]


def test_get_xmp_attribute():
    img = DNG('test_image_canon_6d.dng')
    assert img.get_xmp_attribute(b'crs:Exposure2012') == 0.2


def test_get_brightness():
    img = DNG('test_image_canon_6d.dng')
    assert img.get_brightness(rectangle=[0.3, 0.3, 0.4, 0.4]) == np.float32(0.067557134)

