def test_render_even_offsed_even_width_success(dng_rendered_to_rgb_even_offsets):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = dng_rendered_to_rgb_even_offsets

    # WHEN the used_fields are rendered
    actual = _renderer.render(used_fields, rectangle, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_image)


def test_render_odd_offsed_even_width_success(dng_rendered_to_rgb_odd_offsets):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = dng_rendered_to_rgb_odd_offsets

    # WHEN the used_fields are rendered
    actual = _renderer.render(used_fields, rectangle, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_image)


def test_render_even_offsed_odd_width_success(dng_rendered_to_rgb_even_odd_offsets):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = dng_rendered_to_rgb_even_odd_offsets

    # WHEN the used_fields are rendered
    actual = _renderer.render(used_fields, rectangle, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_image)


def test_render_thumbnail_odd_offsed_even_width_success(dng_thumbnail_rendered_to_rgb_even_offsets):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = dng_thumbnail_rendered_to_rgb_even_offsets

    # WHEN the used_fields are rendered
    actual = _renderer.render(used_fields, rectangle, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_image)


def test_render_thumbnail_even_offsed_odd_width_success(dng_thumbnail_rendered_to_rgb_odd_offsets):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = dng_thumbnail_rendered_to_rgb_odd_offsets

    # WHEN the used_fields are rendered
    actual = _renderer.render(used_fields, rectangle, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_image)


def test_raw_to_rgb_0112_zero_offset(scaled_raw_data_w_ifd_0112_zero_offset):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = scaled_raw_data_w_ifd_0112_zero_offset

    # WHEN the used_fields are rendered
    actual = _renderer._raw_to_rgb(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_raw_to_rgb_0112_even_offset(scaled_raw_data_w_ifd_0112_even_offset):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = scaled_raw_data_w_ifd_0112_even_offset

    # WHEN the used_fields are rendered
    actual = _renderer._raw_to_rgb(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_raw_to_rgb_0112_odd_offset(scaled_raw_data_w_ifd_0112_odd_offset):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from  BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = scaled_raw_data_w_ifd_0112_odd_offset

    # WHEN the used_fields are rendered
    actual = _renderer._raw_to_rgb(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)

def test_raw_to_rgb_1021_even_offset(scaled_raw_data_w_ifd_1021_even_offset, data_folder_path):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = scaled_raw_data_w_ifd_1021_even_offset

    # WHEN the used_fields are rendered
    actual = _renderer._raw_to_rgb(ifd, image, active_area_offset)

    # with open(str(data_folder_path / 'raw_data_to_rgb_1021_even_offset.np'), 'wb') as f:
    #     expected_renderd_area = np.save(f, actual)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)
