def test_find_misalignment_w_crop_success(stabilizer_sequence):
    # GIVEN an image sequence to stabelize and the expected offsets/misalignments
    # note: they're all the same image; misalignment is achieved by editing the crops
    # so if the program ever stops assuming that all the crops are the same
    # then this test will fail
    stabilizer, offsets = stabilizer_sequence

    # WHEN the misalignments are found
    stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(stabilizer._images, offsets):
        actual_misalignment = stabilizer._images[image_time].misalignment
        assert actual_misalignment == expected_offset


def test_find_misalignment_w_minimal_crop_success(stabilizer_sequence_minimal_crop):
    # GIVEN an image sequence to stabelize and the expected offsets/misalignments
    # note: they're all the same image; misalignment is achieved by editing the crops
    # so if the program ever stops assuming that all the crops are the same
    # then this test will fail
    stabilizer, offsets = stabilizer_sequence_minimal_crop

    # WHEN the misalignments are found
    stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(stabilizer._images, offsets):
        actual_misalignment = stabilizer._images[image_time].misalignment
        assert actual_misalignment == expected_offset
