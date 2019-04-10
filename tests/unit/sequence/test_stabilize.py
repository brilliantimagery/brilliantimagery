def test_find_misalignment_w_large_preexisting_crop_success(stabilizer):
    # GIVEN an image sequence to stabelize and the expected offsets/misalignments
    # note: they're all the same image; misalignment is achieved by editing the crops
    # so if the program ever stops assuming that all the crops are the same
    # then this test will fail
    stabilizer, offsets = stabilizer

    # WHEN the misalignments are found
    stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(stabilizer._images, offsets):
        actual_misalignment = stabilizer._images[image_time].misalignment
        assert actual_misalignment == expected_offset


def test_find_misalignment_w_small_preexisting_crop_success(stabilizer_minimal_crop):
    # GIVEN an image sequence to stabelize and the expected offsets/misalignments
    # note: they're all the same image; misalignment is achieved by editing the crops
    # so if the program ever stops assuming that all the crops are the same
    # then this test will fail
    stabilizer, offsets = stabilizer_minimal_crop

    # WHEN the misalignments are found
    stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(stabilizer._images, offsets):
        actual_misalignment = stabilizer._images[image_time].misalignment
        assert actual_misalignment == expected_offset


def test_update_crop_w_large_preexisting_crop_success(stabelized_stabilizer):
    # GIVEN a stabilized sequence where the needed offsets are found
    # and the resulting needed crops are given
    from BrilliantImagery.meta_image import META_TO_DNG
    stabilizer, crops = stabelized_stabilizer

    # WHEN the crop values are assigned to the metadata and retrieved
    stabilizer.update_crop_xmp_attributes()

    # THEN the retrieved xmp crop values are as expected
    for image_time, expected_crops in zip(stabilizer._images, crops):
        left = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom


def test_update_crop_w_small_preexisting_crop_success(stabelized_stabilizer_minimal_crop):
    # GIVEN a stabilized sequence where the needed offsets are found
    # and the resulting needed crops are given
    from BrilliantImagery.meta_image import META_TO_DNG
    stabilizer, crops = stabelized_stabilizer_minimal_crop

    # WHEN the crop values are assigned to the metadata and retrieved
    stabilizer.update_crop_xmp_attributes()

    # THEN the retrieved xmp crop values are as expected
    for image_time, expected_crops in zip(stabilizer._images, crops):
        left = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(stabilizer._images[image_time].get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom
