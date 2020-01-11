


def test_get_xmp_attribute(meta_image_canon_6d, xmp_params):
    # GIVEN an initialized dng, and xmp attributes and values

    # WHEN the xmp value is gotten for each attribute and then converted to floats
    # (to avoid type mismatch issues
    # dng_canon_6d.parse()
    attr, expected_value = xmp_params
    actual_value = meta_image_canon_6d.get_xmp_attribute(attr)
    if expected_value:
        expected_value = float(expected_value)
    if actual_value:
        actual_value = float(actual_value)

    # THEN the attribute value is as expected
    assert actual_value == expected_value