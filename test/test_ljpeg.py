import numpy as np

import ljpeg


def test_decode():
    input_file = np.fromfile('F-18.ljpg', np.uint8).astype(np.intc)
    ljpeg.decode(input_file)
    test = ljpeg.decode(input_file)
    standard = np.load('F-18.ppm.pickle.npy')
    assert np.array_equal(standard, test)


def test_encode():
    standard = np.load('F-18.ppm.pickle.npy')
    ljpeg.encode(standard, 8, 5)
    test = np.asarray(ljpeg.encode(standard, 8, 5)).astype(np.intc)
    test = ljpeg.decode(test)
    assert np.array_equal(standard, test)
