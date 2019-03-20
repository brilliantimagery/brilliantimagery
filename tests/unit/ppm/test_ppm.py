import os

import numpy as np

from BrilliantImagery import ppm


def test_save(setup_ppm_saving, tmpdir):
    # GIVEN a numpy array of image data, expected resulting data, and a temp folder
    test_data, expected_data = setup_ppm_saving
    filename = str(tmpdir.join('test_ppm_save_test.ppm'))

    # WHEN the given data is saved and then read
    ppm.save(test_data, filename, 255)
    actual_data = np.fromfile(filename, np.uint8).astype(np.intc)

    # THEN the read data should equal the given expected data
    assert np.array_equal(expected_data, actual_data)
