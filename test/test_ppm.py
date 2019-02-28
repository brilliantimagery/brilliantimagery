import os

import numpy as np

from src.BrilliantImagery import ppm


def test_save():
    test = np.load('F-18.ppm.pickle.npy')
    ppm.save(test, 'test_ppm_save_test.ppm', 255)
    test = np.fromfile('test_ppm_save_test.ppm', np.uint8).astype(np.intc)
    standard = np.fromfile('F-18.ppm', np.uint8).astype(np.intc)
    os.remove('test_ppm_save_test.ppm')

    assert np.array_equal(standard, test)
