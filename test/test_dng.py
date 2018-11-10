from dng import DNG

default_xmp = {b'crs:Temperature': 6400.0, b'crs:Tint': 16.0, b'crs:Saturation': 9.0,
               b'crs:Vibrance': 29.0, b'crs:Sharpness': 25.0, b'crs:VignetteAmount': 0.0,
               b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:CropLeft': 0.0,
               b'crs:CropBottom': 0.92051, b'crs:CropRight': 1.0, b'crs:CropTop': 0.17051,
               b'xmp:Rating': 2.0, b'crs:Exposure2012': 1.0}

updated_xmp = {b'crs:Temperature': 700.0, b'crs:Tint': 16.0, b'crs:Saturation': 9.0,
               b'crs:Vibrance': 29.0, b'crs:Sharpness': 30.0, b'crs:VignetteAmount': 0.0,
               b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:CropLeft': 0.0,
               b'crs:CropBottom': 0.92051, b'crs:CropRight': 1.0, b'crs:CropTop': 0.17051,
               b'xmp:Rating': 2.0, b'crs:Exposure2012': 1.0}


def test_get_capture_datetime():
    img = DNG('dng_test_input.dng')
    assert img.get_capture_datetime() == '2014-09-26T17:40:25.00'


def test_get_xmp():
    img = DNG('dng_test_input.dng')
    assert img.get_xmp() == default_xmp


def test_update_xmp_attribute_and_store_xmp_field():
    img = DNG('dng_test_input.dng')
    img.set_xmp_attribute(b'crs:Temperature', 700.0)
    img.set_xmp_attribute(b'crs:Sharpness', 30.0)
    img.store_xmp_field()
    assert img.get_xmp() == updated_xmp


def test_rendered_shape():
    img = DNG('dng_test_input.dng')
    assert img.rendered_shape() == [5472, 2736]


def test_default_shape():
    img = DNG('dng_test_input.dng')
    assert img.default_shape() == [5472, 3648]


def test_get_xmp_attribute():
    img = DNG('dng_test_input.dng')
    assert img.get_xmp_attribute(b'crs:Exposure2012') == 1


def test_is_reference_frame():
    img = DNG('dng_test_input.dng')
    assert not img.is_reference_frame()
    img.set_xmp_attribute(b'xmp:Rating', 3)
    assert img.is_reference_frame()

