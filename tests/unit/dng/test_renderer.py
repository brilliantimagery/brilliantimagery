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


def test_raw_to_rgb_1021_even_offset(scaled_raw_data_w_ifd_1021_even_offset):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = scaled_raw_data_w_ifd_1021_even_offset

    # WHEN the used_fields are rendered
    actual = _renderer._raw_to_rgb(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_rescale_and_clip_positive():
    from BrilliantImagery.dng import _renderer

    color_value = 5000.0
    black_level = 500
    white_level = 13000

    expected = 0.36000001430511475

    actual = _renderer._rescale_and_clip(color_value, black_level, white_level)

    assert actual == expected


def test_rescale_and_clip_zero():
    from BrilliantImagery.dng import _renderer

    color_value = 300.0
    black_level = 500
    white_level = 13000

    expected = 0

    actual = _renderer._rescale_and_clip(color_value, black_level, white_level)

    assert actual == expected


def test_set_blacks_whites_scale_and_clip_w_2x2_mask_1_sample_per_pix(unscaled_raw_data_w_2x2_mask_1_sample_per_pix):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = unscaled_raw_data_w_2x2_mask_1_sample_per_pix

    # WHEN the used_fields are rendered
    actual = _renderer._set_blacks_whites_scale_and_clip(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_set_blacks_whites_scale_and_clip_w_2x2_mask_1_sample_per_pix_odd(
        unscaled_raw_data_w_2x2_mask_1_sample_per_pix_odd):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = unscaled_raw_data_w_2x2_mask_1_sample_per_pix_odd

    # WHEN the used_fields are rendered
    actual = _renderer._set_blacks_whites_scale_and_clip(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_set_blacks_whites_scale_and_clip_w_3_sample_per_pix(unscaled_raw_data_w_3_sample_per_pix):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = unscaled_raw_data_w_3_sample_per_pix

    # WHEN the used_fields are rendered
    actual = _renderer._set_blacks_whites_scale_and_clip(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_set_blacks_whites_scale_and_clip_w_linearization(unscaled_raw_data_w_linearization):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, active_area_offset, expected_renderd_area = unscaled_raw_data_w_linearization

    # WHEN the used_fields are rendered
    actual = _renderer._set_blacks_whites_scale_and_clip(ifd, image, active_area_offset)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected_renderd_area)


def test_clip_to_rendered_rectangle(rectangle_to_clip):
    # GIVEN a dng, a rendered area, a rectangle
    import numpy as np
    from BrilliantImagery.dng import _renderer
    ifd, image, expected = rectangle_to_clip

    # WHEN the used_fields are rendered
    actual = _renderer._clip_to_rendered_rectangle(ifd, image)

    # THEN the expected and actual arrays are equal
    assert np.array_equal(actual, expected)


def test_unpack_compressed_tile_data(unpackable_ifd_w_compressed_tiles):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = unpackable_ifd_w_compressed_tiles

    actual = np.asarray(_renderer._unpack_section_data(used_fields))

    assert np.array_equal(actual, expected_image)


def test_unpack_uncompressed_strip_data(unpackable_ifd_w_uncompressed_strips):
    # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
    import numpy as np
    from BrilliantImagery.dng import _renderer
    used_fields, expected_image, active_area_offset, rectangle = unpackable_ifd_w_uncompressed_strips

    actual = np.asarray(_renderer._unpack_section_data(used_fields))

    assert np.array_equal(actual, expected_image)


# def test_unpack_uncompressed_strip_data(unpackable_ifd_w_compressed_tiles, data_folder_path):
#     # GIVEN a dng, a rendered area, a rectangle, and the active_area_offset
#     import numpy as np
#     from BrilliantImagery.dng import _renderer
#     used_fields, expected_image, active_area_offset, rectangle = unpackable_ifd_w_compressed_tiles
#
#     actual = np.asarray(_renderer._unpack_tile_data(used_fields))
#
#     with open(str(data_folder_path / 'unpacked_compressed_tiles.np'), 'wb') as f:
#         expected_renderd_area = np.save(f, actual)
#
#     assert np.array_equal(actual, expected_image)
