def test_ramp_minus_exposure_success(sequence_wo_exposure_w_expected_values):
    # GIVEN a sequence to be ramped
    from brilliantimagery.sequence._ramp import Ramper
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_wo_exposure_w_expected_values
    ramper = Ramper(sequence._images)

    # WHEN the sequence is ramped
    ramper.ramp_minus_exposure()

    # THEN the values should be as expected
    for image_time in ramper._images.keys():
        for attr, expected in non_exp_xmp[image_time].items():
            actual = ramper._images[image_time].get_xmp_attribute(attr)
            assert expected == actual


def test_ramp_exposue_wo_preexisting_brightness_success(sequence_wo_exposure_w_expected_values):
    # GIVEN a sequence to be ramped
    from brilliantimagery.sequence._ramp import Ramper
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_wo_exposure_w_expected_values
    ramper = Ramper(sequence._images)

    # WHEN the sequence is ramped
    ramper.ramp_exposure(rectangle)

    # THEN the values should be as expected
    for image_time in ramper._images.keys():
        actual = ramper._images[image_time].get_xmp_attribute(b'crs:Exposure2012')
        expected = expected_exp[image_time]
        assert actual == expected


def test_ramp_exposue_w_preexisting_brightness_success(sequence_w_exposure_and_expected_values):
    # GIVEN a sequence to be ramped
    from brilliantimagery.sequence._ramp import Ramper
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_w_exposure_and_expected_values
    ramper = Ramper(sequence._images)

    # WHEN the sequence is ramped
    ramper.ramp_exposure(rectangle)

    # THEN the values should be as expected
    for image_time in ramper._images.keys():
        actual = ramper._images[image_time].get_xmp_attribute(b'crs:Exposure2012')
        expected = expected_exp[image_time]
        assert actual == expected


def test_is_multithreaded(sequence_wo_exposure_w_expected_values):
    # GIVEN a sequence to be ramped
    from brilliantimagery.sequence._ramp import Ramper
    sequence, non_exp_xmp, expected_exp, rectangle = sequence_wo_exposure_w_expected_values
    ramper = Ramper(sequence._images)

    # WHEN the sequence is ramped
    ramper.ramp_exposure(rectangle)

    # THEN 'is_single_threaded' shouldn't be a present property
    assert not hasattr(ramper, 'is_single_threaded')
