import numpy as np
import pytest

# from tests._test_utils import data_folder
from BrilliantImagery import ljpeg


@pytest.mark.render
@pytest.mark.ljpeg
def test_decode_success(good_example_numpy_lossless_photo_w_decoded):
    # GIVEN a good lossless jpg that's been unpacked into a 1D numpy array of type intc
    # and what should result from decoding the jpg
    input_file, expected_array = good_example_numpy_lossless_photo_w_decoded

    # WHEN the supplied file is decoded
    test_file = ljpeg.decode(input_file)

    # THEN the test_file should math the expected_array
    assert np.array_equal(expected_array, test_file)


@pytest.mark.render
@pytest.mark.ljpeg
def test_decode_unsupported_marker_raises(example_numpy_lossy_photo):
    # GIVEN a lossy jpg (which isn't supported)
    input_file = example_numpy_lossy_photo

    # WHEN there's an attempt to decode it
    # THEN it raises an exception
    with pytest.raises(NotImplementedError):
        ljpeg.decode(input_file)


@pytest.mark.render
@pytest.mark.ljpeg
def test_decode_huffman_value_raises(example_numpy_lossless_photo_w_bad_huffman_value):
    # GIVEN a lossless jpg with bad huffman values
    input_file = example_numpy_lossless_photo_w_bad_huffman_value
    expected = 'No matching Huffman code was found for a lossless tile jpeg lkj'

    # WHEN attempt is made to decode it
    # THEN it raises a particular exception with particular text
    with pytest.raises(ValueError) as e:
        ljpeg.decode(input_file)
        err_msg = e.value.args[0]
        assert err_msg == expected


@pytest.mark.render
@pytest.mark.ljpeg
def test_decode_hi_value_raises(example_numpy_lossless_photo_w_bad_hi_value):
    # GIVEN a lossless jpg with a bad Hi value
    input_file = example_numpy_lossless_photo_w_bad_hi_value
    expected = 'Pixels are an unsupported shape, Hi'

    # WHEN attempt is made to decode it
    # THEN it raises a particular exception with particular text
    with pytest.raises(NotImplementedError) as e:
        ljpeg.decode(input_file)
        err_msg = e.value.args[0]
        assert err_msg == expected


@pytest.mark.render
@pytest.mark.ljpeg
def test_decode_vi_value_raises(example_numpy_lossless_photo_w_bad_vi_value):
    # GIVEN a lossless jpg with a bad Hi value
    input_file = example_numpy_lossless_photo_w_bad_vi_value
    expected = 'Pixels are an unsupported shape, Vi'

    # WHEN attempt is made to decode it
    # THEN it raises a particular exception with particular text
    with pytest.raises(NotImplementedError) as e:
        ljpeg.decode(input_file)
        err_msg = e.value.args[0]
        assert err_msg == expected


@pytest.mark.render
@pytest.mark.ljpeg
def test_decode_tqi_value_raises(example_numpy_lossless_photo_w_bad_tqi_value):
    # GIVEN a lossless jpg with a bad Hi value
    input_file = example_numpy_lossless_photo_w_bad_tqi_value
    expected = 'Tqi should be zero'

    # WHEN an attempt is made to decode it
    # THEN it raises a particular exception with particular text
    with pytest.raises(ValueError) as e:
        ljpeg.decode(input_file)
        err_msg = e.value.args[0]
        assert err_msg == expected


@pytest.mark.render
@pytest.mark.ljpeg
def test_user_inputs_raises(user_input_params):
    # GIVEN a set of inputs of the wrong data type or shape
    input_data, exception = user_input_params

    # WHEN an attempt is made to decode it
    # THEN it raises a particular exception
    with pytest.raises(exception):
        ljpeg.decode(input_data)
