from BrilliantImagery.dng import _dng_utils


def test_get_xmp_attribute_value_success(xmp_buffer, xmp_params):
    # GIVEN xmp data
    from BrilliantImagery.dng import _dng_utils
    property, expected = xmp_params

    # WHEN it's searched for known attribute, value pairs
    actual = _dng_utils.get_xmp_attribute_value(xmp_buffer, property)

    # THEN the given and actual are equal
    assert actual == expected


def test_get_xmp_attribute_value_bad_value_none(xmp_buffer):
    # GIVEN xmp data
    from BrilliantImagery.dng import _dng_utils
    expected = None

    # WHEN it's searched for known attribute, value pairs
    actual = _dng_utils.get_xmp_attribute_value(xmp_buffer, b'bad')

    # THEN the given and actual are equal
    assert actual == expected


def test_renderd_area_bounding_box_success(bounding_box_params):
    # GIVEN bounding box data
    from BrilliantImagery.dng import _dng_utils
    bbx = bounding_box_params

    # WHEN the bounding box data is run through the conversion
    actual = _dng_utils.renderd_area_bounding_box(bbx.input, bbx.x0, bbx.y0, bbx.x1, bbx.y1)

    # THEN the output of the conversion is as expected
    assert actual == bbx.output


def test_convert_rectangle_percent_to_pixels_default(used_ifd_fields_raw):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.convert_rectangle_percent_to_pixels(used_ifd_fields_raw,
                                                            [.25, .35, .65, .75],
                                                            0.05, 0.06, 0.92, 0.97)
    expected = [1547, 1430, 3451, 2757]

    # THEN
    assert actual == expected


def test_get_active_area_offset_default(used_ifd_fields_raw):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.get_active_area_offset(used_ifd_fields_raw, [1547, 1430, 3451, 2757])
    expected = (1475, 1392)

    # THEN
    assert actual == expected


def test_convert_rectangle_percent_to_pixels_raw(used_ifd_fields_raw):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.convert_rectangle_percent_to_pixels(used_ifd_fields_raw,
                                                            [.25, .35, .65, .75],
                                                            0.05, 0.06, 0.92, 0.97, 'RAW')
    expected = [1547, 1430, 3451, 2757]

    # THEN
    assert actual == expected


def test_get_active_area_offset_raw(used_ifd_fields_raw):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.get_active_area_offset(used_ifd_fields_raw, [1547, 1430, 3451, 2757], 'RAW')
    expected = (1475, 1392)

    # THEN
    assert actual == expected


def test_convert_rectangle_percent_to_pixels_thumbnail(used_ifd_fields_thumbnail):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.convert_rectangle_percent_to_pixels(used_ifd_fields_thumbnail,
                                                            [.25, .35, .65, .75],
                                                            0.05, 0.06, 0.92, 0.97, 'thumbnail')
    expected = [64, 64, 166, 137]

    # THEN
    assert actual == expected


def test_get_active_area_offset_thumbnail(used_ifd_fields_thumbnail):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.get_active_area_offset(used_ifd_fields_thumbnail, [64, 64, 166, 137], 'thumbnail')
    expected = (0, 0)

    # THEN
    assert actual == expected
