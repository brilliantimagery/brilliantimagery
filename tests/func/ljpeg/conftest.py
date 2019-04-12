import numpy as np
import pytest


@pytest.fixture()
def rgb_numpy_photo(data_folder_path):
    return np.load(str(data_folder_path / 'F-18.ppm.pickle.npy'))
