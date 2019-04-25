import numpy as np
import pytest

inputs_to_try = (('hello', TypeError),
                 (np.array([[1, 1], [1, 1]], dtype=np.intc), ValueError),
                 (np.array([1.5, 1.5], dtype=np.float), ValueError),
                 )


def id_user_inputs_func(fixture_value):
    """A function to generate fixture IDs"""
    return f'UserInputs({fixture_value[0]}, {fixture_value[1]})'


@pytest.fixture(params=inputs_to_try, ids=id_user_inputs_func)
def user_input_params(request):
    return request.param


@pytest.fixture()
def good_example_numpy_lossless_photo_w_decoded(data_folder_path):
    input_file = np.fromfile(str(data_folder_path / 'ljpg_F-18.ljpg'), np.uint8).astype(np.intc)
    expected = np.load(str(data_folder_path / 'F-18.ppm.pickle.np'))
    return input_file, expected


@pytest.fixture()
def example_numpy_lossy_photo(data_folder_path):
    return np.fromfile(str(data_folder_path / 'jpg_lossy.jpg'), np.uint8).astype(np.intc)


@pytest.fixture()
def example_numpy_lossless_photo_w_bad_huffman_value(data_folder_path):
    return np.fromfile(str(data_folder_path / 'ljpg_F-18_bad_huffman_value.ljpg'), np.uint8).astype(np.intc)


@pytest.fixture()
def example_numpy_lossless_photo_w_bad_hi_value(data_folder_path):
    return np.fromfile(str(data_folder_path / 'ljpg_F-18_bad_Hi.ljpg'), np.uint8).astype(np.intc)


@pytest.fixture()
def example_numpy_lossless_photo_w_bad_vi_value(data_folder_path):
    return np.fromfile(str(data_folder_path / 'ljpg_F-18_bad_Vi.ljpg'), np.uint8).astype(np.intc)


@pytest.fixture()
def example_numpy_lossless_photo_w_bad_tqi_value(data_folder_path):
    return np.fromfile(str(data_folder_path / 'ljpg_F-18_bad_Tqi.ljpg'), np.uint8).astype(np.intc)
