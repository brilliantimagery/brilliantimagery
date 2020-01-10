import numpy as np
import pytest

from brilliantimagery import ljpeg


@pytest.mark.ljpeg
def test_encode_success(rgb_numpy_photo):
    # GIVEN a decoded photo in a 3D numpy array with a precision of 8

    # WHEN encode is run twice to ensure that everyting's reinitialized properly
    # and then decoded
    ljpeg.encode(rgb_numpy_photo, 8, 5)
    actual = np.asarray(ljpeg.encode(rgb_numpy_photo, 8, 5)).astype(np.intc)
    actual = ljpeg.decode(actual)

    # THEN the decoded image is the same as the input data
    assert np.array_equal(rgb_numpy_photo, actual)

