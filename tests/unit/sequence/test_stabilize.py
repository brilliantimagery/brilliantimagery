from brilliantimagery.sequence._sequence import Stabilizer


def test_find_misalignment_w_large_preexisting_crop_success(sequence):
    # GIVEN an image sequence to stabilize and the expected offsets/misalignments
    sequence, rectangle, offsets = sequence
    _stabilizer = Stabilizer(sequence._images, rectangle)

    # WHEN the misalignments are found
    _stabilizer.find_misalignments(keep_brightness=False)

    # THEN each image's misalignment should be as expected
    for image_time, expected_offset in zip(_stabilizer._images, offsets):
        actual_misalignment = _stabilizer._images[image_time].misalignment

        assert actual_misalignment == expected_offset


def test_update_crop_w_large_preexisting_crop_success(stabilized_sequence):
    # GIVEN a stabilized sequence where the needed offsets are found
    # and the resulting needed crops are given
    from brilliantimagery.meta_image import META_TO_DNG
    sequence, rectangle, crops = stabilized_sequence
    _stabilizer = Stabilizer(sequence._images, rectangle)

    # WHEN the crop values are assigned to the metadata and retrieved
    _stabilizer.update_crop_xmp_attributes()

    # THEN the retrieved xmp crop values are as expected
    for image_time, expected_crops in zip(_stabilizer._images, crops):
        left = round(_stabilizer._images[image_time]
                     .get_xmp_attribute(META_TO_DNG['CropLeft']), 6)
        top = round(_stabilizer._images[image_time]
                    .get_xmp_attribute(META_TO_DNG['CropTop']), 6)
        right = round(_stabilizer._images[image_time]
                      .get_xmp_attribute(META_TO_DNG['CropRight']), 6)
        bottom = round(_stabilizer._images[image_time]
                       .get_xmp_attribute(META_TO_DNG['CropBottom']), 6)
        assert left == expected_crops.left
        assert top == expected_crops.top
        assert right == expected_crops.right
        assert bottom == expected_crops.bottom


def test_is_multithreaded(sequence):
    # GIVEN an image sequence to stabilize and the expected offsets/misalignments
    sequence, rectangle, offsets = sequence
    _stabilizer = Stabilizer(sequence._images, rectangle)

    # WHEN the misalignments are found
    _stabilizer.find_misalignments(keep_brightness=False)

    # THEN 'is_single_threaded' shouldn't be a present property
    assert not hasattr(_stabilizer, 'is_single_threaded')
