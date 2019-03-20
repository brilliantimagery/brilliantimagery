from BrilliantImagery.dng import _dng_utils


def test_get_xmp_attribute_value_success(xmp_params):
    # GIVEN xmp data
    from BrilliantImagery.dng import _dng_utils
    expected = xmp_params.attr_value_pairs.value

    # WHEN it's searched for known attribute, value pairs
    actual = _dng_utils.get_xmp_attribute_value(xmp_params.xmp_data, xmp_params.attr_value_pairs.attr)

    # THEN the given and actual are equal
    assert actual == expected


def test_get_xmp_attribute_value_bad_value_none(xmp_params):
    # GIVEN xmp data
    from BrilliantImagery.dng import _dng_utils
    expected = None

    # WHEN it's searched for known attribute, value pairs
    actual = _dng_utils.get_xmp_attribute_value(xmp_params.xmp_data, b'bad')

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


def test_convert_rectangle_percent_to_pixels_default(used_ifd_fields):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.convert_rectangle_percent_to_pixels(used_ifd_fields,
                                                            [.25, .35, .65, .75],
                                                            0.05, 0.06, 0.92, 0.97)
    expected = ([1547, 1430, 3451, 2757], (1475, 1392))

    # THEN
    assert actual == expected


def test_convert_rectangle_percent_to_pixels_raw(used_ifd_fields):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.convert_rectangle_percent_to_pixels(used_ifd_fields,
                                                            [.25, .35, .65, .75],
                                                            0.05, 0.06, 0.92, 0.97, 'RAW')
    expected = ([1547, 1430, 3451, 2757], (1475, 1392))

    # THEN
    assert actual == expected


def test_convert_rectangle_percent_to_pixels_thumbnail(used_ifd_fields):
    # GIVEN the _used_field data
    from BrilliantImagery.dng import _dng_utils

    # WHEN
    actual = _dng_utils.convert_rectangle_percent_to_pixels(used_ifd_fields,
                                                            [.25, .35, .65, .75],
                                                            0.05, 0.06, 0.92, 0.97, 'thumbnail')
    expected = ([1392, 1297, 3619, 2781], (0, 0))

    # THEN
    assert actual == expected
