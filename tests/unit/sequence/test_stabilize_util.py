import math


def test_find_misalignment_success(sequence):
    # GIVEN a Sequence, a rectangle, and offsets between images
    from brilliantimagery.sequence import _stabilize_util
    sequence, rectangle, offsets = sequence

    expected_misalignment = [-4.140580359578448, 0.5651787914802656]
    expected_brightness = 0.006079677492380142

    # WHEN the the first two MetaImages are found and have their misalignments found
    time0 = list(sequence._images)[0]
    time1 = list(sequence._images)[1]

    image0 = sequence._images[time0]
    image1 = sequence._images[time1]

    time, image = _stabilize_util.find_misalignment(image0, image1, rectangle, True, time1)

    # THEN the offset is correct, the time is passed back out, and the brightness is kept
    assert math.isclose(image.misalignment[0], expected_misalignment[0])
    assert math.isclose(image.misalignment[1], expected_misalignment[1])
    assert math.isclose(image.brightness, expected_brightness)
    assert time == time1
