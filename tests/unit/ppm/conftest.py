from collections import namedtuple
import pytest

import numpy as np


@pytest.fixture()
def setup_ppm_saving(data_folder_path):
    test_data = np.load(str(data_folder_path / 'F-18.ppm.pickle.np'))

    expected = np.fromfile(str(data_folder_path / 'ppm_F-18.ppm'), np.uint8).astype(np.intc)

    return test_data, expected
