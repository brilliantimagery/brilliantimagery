from io import BytesIO

import pytest
import numpy as np

from BrilliantImagery.dng import DNG


def test_get_byte_order_bII_success(dng_canon_6d):
    # GIVEN an initialized DNG
    # from BrilliantImagery.dng import DNG
    # dng = DNG('fake.file')

    # WHEN the dng has small ended IO bytes passes in
    dng_canon_6d._get_byte_order(BytesIO(b'II'))

    # THEN the byte order is as expected
    assert dng_canon_6d._byte_order == '<'


def test_get_byte_order_bMM_success(dng_canon_6d):
    # GIVEN an initialized DNG
    # dng = DNG('fake.file')

    # WHEN the dng has big ended IO bytes passes in
    dng_canon_6d._get_byte_order(BytesIO(b'MM'))

    # THEN the byte order is as expected
    assert dng_canon_6d._byte_order == '>'


def test_get_byte_order_bad_raises(dng_canon_6d):
    # GIVEN an initialized DNG
    # dng = DNG('fake.file')
    expected = "Byte order should be b'II' or b'MM' but is"

    # WHEN the dng has small bad IO bytes passes in
    # THEN and excepton is raised
    with pytest.raises(ValueError) as e:
        dng_canon_6d._get_byte_order(BytesIO(b'bad'))
        err_msg = e.value.args[0]
        assert expected in err_msg


def test_get_capture_datetime(dng_canon_6d):
    # GIVEN an initialized DNG file and it's capture datetime
    expected = '2017-09-07T16:01:38.03'

    # WHEN parsed
    # dng_canon_6d.parse()
    actual = dng_canon_6d.get_capture_datetime()

    # THEN the capture datetime is as expected
    assert expected == actual


def test_get_capture_datetime_not_in_xmp(dng_pixel2):
    # GIVEN an initialized DNG file and it's capture datetime
    expected = '1556658902.9690008'

    # WHEN parsed
    # dng_pixel2.parse()
    actual = dng_pixel2.get_capture_datetime()

    # THEN the capture datetime is as expected
    assert expected == actual


def test_get_fields_required_to_render_raw(dng_canon_6d, used_ifd_fields_raw):
    # GIVEN an initialized DNG and the expected used IFD fields

    # WHEN it's parsed and the used ifd fields are retrieved
    # dng_canon_6d.parse()
    dng_canon_6d._get_fields_required_to_render('raw')
    actual_fields = dng_canon_6d._used_fields

    # THEN the retreived fields should match the expected fields
    assert actual_fields == used_ifd_fields_raw


def test_get_fields_required_to_render_thumbnail(dng_canon_6d, used_ifd_fields_thumbnail):
    # GIVEN an initialized DNG and the expected used IFD fields

    # WHEN it's parsed and the used ifd fields are retrieved
    # dng_canon_6d.parse()
    dng_canon_6d._get_fields_required_to_render('thumbnail')
    actual_fields = dng_canon_6d._used_fields

    # THEN the retrieved fields should match the expected fields
    assert actual_fields == used_ifd_fields_thumbnail


def test_get_fields_required_to_render_error(dng_canon_6d, used_ifd_fields_thumbnail):
    # GIVEN an initialized DNG and the expected error message
    expected = 'Retrieved image type must be "RAW" or "thumbnail" but "bad_value" was given.'

    # WHEN it's parsed and the used ifd fields are retrieved
    # THEN an exception should be raised with a particular message
    # dng_canon_6d.parse()
    with pytest.raises(ValueError) as e:
        dng_canon_6d._get_fields_required_to_render('bad_value')
        err_msg = e.value.args[0]
        assert expected in err_msg


def test_get_ifd_fields(dng_file_io_ifd, canon_6d_idfs):
    # GIVEN an initialized dng and the expected ifds as a string
    dng, f = dng_file_io_ifd

    # WHEN the IDF fiels are read
    dng._get_ifd_fields(f)
    actual_ifds = str(dng._ifds)

    # THEN the ifd is as expected
    assert actual_ifds == canon_6d_idfs


def test_get_image_cropped_raw(dng_canon_6d, numpy_cropped_canon_6d):
    # GIVEN an initialized dng and a rendered image with its rendered area
    expected_image, rendered_area = numpy_cropped_canon_6d

    # WHEN it's parsed and then rendered
    # dng_canon_6d.parse()
    actual_image = dng_canon_6d.get_image(rendered_area)

    # THEN the rendered image is as expected
    assert np.array_equal(actual_image, expected_image)


def test_get_image_full_thumbnail(dng_canon_6d, numpy_thumbnail_canon_6d):
    # GIVEN an initialized dng and a rendered image with its rendered area

    # WHEN it's parsed and then the thumbnail's rendered
    # dng_canon_6d.parse()
    actual_image = dng_canon_6d.get_image(sub_image='thumbnail')

    # THEN the rendered image is as expected
    assert np.array_equal(actual_image, numpy_thumbnail_canon_6d)


def test_get_xmp_success(dng_canon_6d, dng_xmp):
    # GIVEN an initialized dng and a dict of the included xmp data

    # WHEN it's parsed and then the xmp data's retrieved
    # dng_canon_6d.parse()
    xmp = dng_canon_6d.get_xmp()

    # THEN the xmp data read from the file matches what's expected
    assert xmp == dng_xmp


def test_parse_ifds_success(dng_canon_6d, canon_6d_idfs):
    # GIVEN an initialized dng and the expected ifds as a string
    dng_canon_6d._zeroth_ifd = 8

    # WHEN the IDF fiels are parsed
    dng_canon_6d._parse_ifds()
    actual_ifds = str(dng_canon_6d._ifds)

    # THEN the ifd is as expected
    assert actual_ifds == canon_6d_idfs


def test_get_tile_or_strip_bytes_compressed_tiles_success(dng_canon_6d, canon_6d_compressed_tiles):
    # GIVEN an initialized dng, and a rectangle to be rendered and the accompanying compressed raw data
    rectangle, tiles = canon_6d_compressed_tiles
    expected_key = list(tiles.keys())[0]

    # WHEN the dng's parsed and then the compressed tile data's retreaved
    # dng_canon_6d.parse()
    dng_canon_6d._get_fields_required_to_render('raw')
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)

    # THEN the resulting dicts have the same keys and the key's values are the same
    actual = dng_canon_6d._used_fields['section_bytes']
    assert tiles.keys() == actual.keys()
    assert np.array_equal(tiles[expected_key], actual[expected_key])


@pytest.mark.skip(reason="Don't have anything to test this against/might not be implemented")
def test_get_tile_or_strip_bytes_uncompressed_tile_success():
    pass


@pytest.mark.skip(reason="Don't have anything to test this against/might not be implemented")
def test_get_tile_or_strip_bytes_compressed_strip_success():
    pass


@pytest.mark.skip(reason="Don't have anything to test this against/might not be implemented")
def test_get_tile_or_strip_bytes_uncompressed_strip_success():
    pass


def test_get_ifd_offsets_success(dng_file_io_ifd):
    # GIVEN an initialized dng and an open file object
    dng_canon_6d, f = dng_file_io_ifd

    # WHEN the zeroth ifd offset's set and the ifds are parsed, and then the ifd offsets are gotten
    dng_canon_6d._zeroth_ifd = 8
    dng_canon_6d._parse_ifds()
    dng_canon_6d._get_ifd_offsets()

    # THEN the retreived offsets should be as expected
    assert dng_canon_6d._thumbnail_offset == 8
    assert dng_canon_6d._orig_img_offset == 202942
    assert dng_canon_6d._xmp_ifd_offset == 8


def test_set_xmp_attribute(dng_canon_6d, updated_dng_xmp):
    # GIVEN an initialized dng, xmp properties to change, and the resulting xmp data
    updated_xmp, new_xmp_values = updated_dng_xmp

    # WHEN the xmp values are updated
    # dng_canon_6d.parse()
    for prop_name, value in new_xmp_values.items():
        dng_canon_6d.set_xmp_attribute(prop_name, value)

    xmp = dng_canon_6d.get_xmp()

    assert xmp == updated_xmp


def test_store_xmp_field(dng_canon_6d, storable_dng_xmp):
    # GIVEN an initialized dng, updated but not stored xmp data, and the resulting xmp data
    xmp_to_be_stored, updated_xmp_data = storable_dng_xmp

    # WHEN the xmp data it set to the updated data and then stored
    # dng_canon_6d.parse()
    dng_canon_6d._xmp = xmp_to_be_stored
    dng_canon_6d.store_xmp_field()

    # THEN the xmp data is the updated data
    xmp = dng_canon_6d._ifds[dng_canon_6d._xmp_ifd_offset][700].values[0]
    assert xmp == updated_xmp_data
    assert dng_canon_6d._updated == True
    assert dng_canon_6d._xmp_length_changed == True


def test_rendered_shape(dng_canon_6d):
    # GIVEN an initialized dng and an expected shape
    expected_shape = [5027, 3351]

    # WHEN it's parsed and then has it's rendered shape is read
    # dng_canon_6d.parse()
    actual_shape = dng_canon_6d.rendered_shape()

    # THEN the expected and actual shapes are equal
    assert actual_shape == expected_shape


def test_default_shape(dng_canon_6d):
    # GIVEN an initialized dng and an expected shape
    expected_shape = [5472, 3648]

    # WHEN it's parsed and then has it's default shape is read
    # dng_canon_6d.parse()
    actual_shape = dng_canon_6d.default_shape()

    # THEN the expected and actual shapes are equal
    assert actual_shape == expected_shape


def test_get_xmp_attribute(dng_canon_6d, xmp_params):
    # GIVEN an initialized dng, and xmp attributes and values

    # WHEN the xmp value is gotten for each attribute and then converted to floats
    # (to avoid type mismatch issues
    # dng_canon_6d.parse()
    attr, expected_value = xmp_params
    actual_value = dng_canon_6d.get_xmp_attribute(attr)
    if expected_value:
        expected_value = float(expected_value)
    if actual_value:
        actual_value = float(actual_value)

    # THEN the attribute value is as expected
    assert actual_value == expected_value


def test_save_xmp_length_unchanged_success(copied_dng_canon_6d, dng_canon_6d):
    # GIVEN two copies of the same dng

    # WHEN one has the xmp data changed and then saved, and then reprocessed
    # and the other has equivalent operations other than the xmp change
    # copied_dng_canon_6d.parse()
    copied_dng_canon_6d._updated = True
    copied_dng_canon_6d._xmp_length_changed = False
    xmp_buffer = copied_dng_canon_6d._ifds[copied_dng_canon_6d._xmp_ifd_offset][700].values[0]
    xmp_buffer = xmp_buffer[:3] + b'q' + xmp_buffer[4:]
    copied_dng_canon_6d._ifds[copied_dng_canon_6d._xmp_ifd_offset][700].values[0] = xmp_buffer
    copied_dng_canon_6d.save()
    # copied_dng_canon_6d.parse()
    copied_dng_canon_6d._updated = True
    copied_dng_canon_6d._xmp_length_changed = False

    # dng_canon_6d.parse()
    dng_canon_6d._updated = False
    dng_canon_6d._xmp_length_changed = False
    dng_canon_6d.get_xmp()

    # THEN the xmp shows up as changed and the images have the same ifds
    assert xmp_buffer[3] == ord('q')
    assert copied_dng_canon_6d._ifds == dng_canon_6d._ifds


# def test_save_xmp_length_changed_success(copied_dng_canon_6d, saved_dng_canon_6d):
def test_save_xmp_length_changed_success(copied_dng_canon_6d, post_save_ifds):
    # GIVEN two copies of the same dng
    from BrilliantImagery.dng import DNG

    # WHEN one has the xmp data changed and then saved, and then reprocessed
    # and the other has equivalent operations other than the xmp change
    # copied_dng_canon_6d.parse()
    copied_dng_canon_6d._updated = True
    copied_dng_canon_6d._xmp_length_changed = True
    xmp_buffer = copied_dng_canon_6d._ifds[copied_dng_canon_6d._xmp_ifd_offset][700].values[0]
    xmp_buffer = xmp_buffer[:3] + b'qq' + xmp_buffer[4:]
    copied_dng_canon_6d._ifds[copied_dng_canon_6d._xmp_ifd_offset][700].values[0] = xmp_buffer
    copied_dng_canon_6d.save()

    path = copied_dng_canon_6d._path
    copied_dng_canon_6d = DNG(path)
    # copied_dng_canon_6d.parse()
    copied_dng_canon_6d._updated = False
    copied_dng_canon_6d._xmp_length_changed = False

    # THEN the xmp shows up as changed and the images have the same ifds
    actual = str(copied_dng_canon_6d._ifds)
    assert xmp_buffer[3] == ord('q')
    assert actual == post_save_ifds


def test_not_is_reference_frame_success(dng_canon_6d):
    # GIVEN a initialized dng that isn't a reference frame (it's 2 stars)

    # WHEN it's parsed
    # dng_canon_6d.parse()

    # THEN it's found to not be a ref frame
    assert not dng_canon_6d.is_reference_frame


def test_is_reference_frame_success(dng_canon_6d):
    # GIVEN a initialized dng that isn't a reference frame (it's 2 stars)
    from BrilliantImagery.dng import DNG

    # WHEN it's parsed and has it's rating set to that of the ref frame rating
    # dng_canon_6d.parse()
    dng_canon_6d.get_xmp()
    dng_canon_6d.set_xmp_attribute(b'xmp:Rating', DNG._REFERENCE_FRAME_STARS)
    dng_canon_6d.store_xmp_field()

    # THEN it's found to be a ref frame
    assert dng_canon_6d.is_reference_frame


def test_get_brightness(dng_canon_6d):
    # GIVEN an initialized dng and a rectangle and a brightness
    rectangle = [0.3, 0.3, 0.4, 0.4]
    expected_brightness = np.float32(0.067557134)

    # WHEN the the image is parsed and the brightness of the rectangle is calculated
    # dng_canon_6d.parse()
    actual_brightness = dng_canon_6d.get_brightness(rectangle=rectangle)

    # THEN the expected and actual brightnesses will match
    assert expected_brightness == actual_brightness
