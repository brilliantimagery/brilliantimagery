from brilliantimagery.meta_image import META_TO_DNG


def test_ramp_minus_exmpsure(sequence_wo_exposure_w_expected_values):
    # GIVEN a sequence to be ramped
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_wo_exposure_w_expected_values

    # WHEN the sequence is ramped
    sequence.ramp_minus_exmpsure()

    # THEN the values should be as expected
    for image_time in sequence._images.keys():
        for attr, expected in non_exp_xmp[image_time].items():
            actual = sequence._images[image_time].get_xmp_attribute(attr)
            assert expected == actual


def test_ramp_exmpsure(sequence_w_exposure_and_expected_values):
    # GIVEN a sequence to be ramped
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_w_exposure_and_expected_values

    # WHEN the sequence is ramped
    sequence.ramp_exposure(rectangle)

    # THEN the values should be as expected
    for image_time, expected in zip(sequence._ordered_capture_times, expected_exp):
        actual = sequence._images[image_time].get_xmp_attribute(META_TO_DNG['Exposure'])
        assert expected == actual


def test_ramp(sequence_w_exposure_and_expected_values):
    # GIVEN a sequence to be ramped
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_w_exposure_and_expected_values

    # WHEN the sequence is ramped
    sequence.ramp(rectangle)

    # THEN the values should be as expected
    for image_time, expected in zip(sequence._ordered_capture_times, expected_exp):
        actual = sequence._images[image_time].get_xmp_attribute(META_TO_DNG['Exposure'])
        assert expected == actual

    for image_time in sequence._images.keys():
        for attr, expected in non_exp_xmp[image_time].items():
            actual = sequence._images[image_time].get_xmp_attribute(attr)
            assert expected == actual


def test_ramp_and_stabilize(rampable_and_stablizable_sequence):
    # GIVEN a sequence to be ramped
    sequence, non_exp_xmp, expected_exp, rectangle, crops = rampable_and_stablizable_sequence

    # WHEN the sequence is ramped
    sequence.ramp_and_stabilize(rectangle)

    # THEN the values should be as expected
    for image_time, expected in zip(sequence._ordered_capture_times, expected_exp):
        actual = sequence._images[image_time].get_xmp_attribute(META_TO_DNG['Exposure'])
        assert expected == actual

    for image_time in sequence._images.keys():
        for attr, expected in non_exp_xmp[image_time].items():
            actual = sequence._images[image_time].get_xmp_attribute(attr)
            assert expected == actual

    for image_time, expected_crops in zip(sequence._images, crops):
        left = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom


def test_stabilize(rampable_and_stablizable_sequence):
    # GIVEN a sequence to be ramped
    sequence, non_exp_xmp, expected_exp, rectangle, crops = rampable_and_stablizable_sequence

    # WHEN the sequence is ramped
    sequence.stabilize(rectangle)

    # THEN the values should be as expected
    for image_time, expected_crops in zip(sequence._images, crops):
        left = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(sequence._images[image_time].get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        # a = (left, top, right, bottom)
        # b = 0
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom


def test_is_multithreaded(rampable_and_stablizable_sequence):
    # GIVEN a sequence
    sequence, non_exp_xmp, expected_exp, rectangle, crops = rampable_and_stablizable_sequence

    # THEN 'is_single_threaded' shouldn't be a present property
    assert not hasattr(sequence, 'is_single_threaded')
