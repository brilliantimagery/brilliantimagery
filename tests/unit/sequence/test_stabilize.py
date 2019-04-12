from BrilliantImagery.sequence._stabilize import Stabilizer


def test_find_misalignment_w_large_preexisting_crop_success(sequence):
    # GIVEN an image sequence to stabelize and the expected offsets/misalignments
    # note: they're all the same image; misalignment is achieved by editing the crops
    # so if the program ever stops assuming that all the crops are the same
    # then this test will fail
    sequence, rectangle, offsets = sequence
    _stabilizer = Stabilizer(sequence._images, rectangle)

    # WHEN the misalignments are found
    _stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(_stabilizer._images, offsets):
        actual_misalignment = _stabilizer._images[image_time].misalignment
        assert actual_misalignment == expected_offset


def test_find_misalignment_w_small_preexisting_crop_success(sequence_minimal_crop):
    # GIVEN an image sequence to stabelize and the expected offsets/misalignments
    # note: they're all the same image; misalignment is achieved by editing the crops
    # so if the program ever stops assuming that all the crops are the same
    # then this test will fail
    sequnce, rectangle, offsets = sequence_minimal_crop
    _stabilizer = Stabilizer(sequnce._images, rectangle)

    # WHEN the misalignments are found
    _stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(_stabilizer._images, offsets):
        actual_misalignment = _stabilizer._images[image_time].misalignment
        assert actual_misalignment == expected_offset


def test_update_crop_w_large_preexisting_crop_success(stabelized_sequence):
    # GIVEN a stabilized sequence where the needed offsets are found
    # and the resulting needed crops are given
    from BrilliantImagery.meta_image import META_TO_DNG
    sequence, rectangle, crops = stabelized_sequence
    _stabilizer = Stabilizer(sequence._images, rectangle)

    # WHEN the crop values are assigned to the metadata and retrieved
    _stabilizer.update_crop_xmp_attributes()

    # THEN the retrieved xmp crop values are as expected
    for image_time, expected_crops in zip(_stabilizer._images, crops):
        left = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom


def test_update_crop_w_small_preexisting_crop_success(stabelized_sequence_minimal_crop):
    # GIVEN a stabilized sequence where the needed offsets are found
    # and the resulting needed crops are given
    from BrilliantImagery.meta_image import META_TO_DNG
    sequence, rectangle, crops = stabelized_sequence_minimal_crop
    _stabilizer = Stabilizer(sequence._images, rectangle)

    # WHEN the crop values are assigned to the metadata and retrieved
    _stabilizer.update_crop_xmp_attributes()

    # THEN the retrieved xmp crop values are as expected
    for image_time, expected_crops in zip(_stabilizer._images, crops):
        left = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(_stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom
