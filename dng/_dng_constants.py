import collections

__Xmp_Tag = collections.namedtuple('Xmp_Tag', 'n_decimal_places default_value is_vector is_ramped')

XMP_TAGS = {b'crs:Temperature': __Xmp_Tag(0, "6500", False, True),
            b'crs:Tint': __Xmp_Tag(0, "+7", True, True),
            b'crs:Saturation': __Xmp_Tag(0, "0", True, True),
            b'crs:Vibrance': __Xmp_Tag(0, "0", True, True),
            b'crs:Sharpness': __Xmp_Tag(0, "25", False, True),
            b'crs:VignetteAmount': __Xmp_Tag(0, "0", True, True),
            b'crs:VignetteMidpoint': __Xmp_Tag(0, "50", False, True),
            b'crs:ShadowTint': __Xmp_Tag(0, "0", True, True),
            b'crs:RedHue': __Xmp_Tag(0, "0", True, True),
    #     CRSREDSATURATION("crs:RedSaturation", 0, "0", true, false), CRSGREENHUE("crs:GreenHue", 0, "0",
    #                 true,
    #                 false), CRSGREENSATURATION("crs:GreenSaturation", 0, "0", true, false), CRSBLUEHUE("crs:BlueHue", 0,
    #                         "0", true, false), CRSBLUESATURATION("crs:BlueSaturation", 0, "0", true, false),
    #
    # CRSHUEADJUSTMENTRED("crs:HueAdjustmentRed", 0, "0", true, false), CRSHUEADJUSTMENTORANGE("crs:HueAdjustmentOrange",
    #         0, "0", true, false), CRSHUEADJUSTMENTYELLOW("crs:HueAdjustmentYellow", 0, "0", true,
    #                 false), CRSHUEADJUSTMTNEGREEN("crs:HueAdjustmentGreen", 0, "0", true, false), CRSHUEADJUSTMENTAQUA(
    #                         "crs:HueAdjustmentAqua", 0, "0", true, false), CRSHUEADJUSTMENTBLUE("crs:HueAdjustmentBlue",
    #                                 0, "0", true, false), CRSHUEADJUSMTMENTPURPLE("crs:HueAdjustmentPurple", 0, "0",
    #                                         true, false), CRSHUEADJUSTMENTMAGENTA("crs:HueAdjustmentMagenta", 0, "0",
    #                                                 true, false),
    #
    # CRSSATURATIONADJUSTMENTRED("crs:SaturationAdjustmentRed", 0, "0", true, false), CRSSATURATIONADJUSTMTENTORANGE(
    #         "crs:SaturationAdjustmentOrange", 0, "0", true,
    #         false), CRSSATURATIONADJUSTMTNETYELLOW("crs:SaturationAdjustmentYellow", 0, "0", true,
    #                 false), CRSSATURATIONADJUSTMTNETGREEN("crs:SaturationAdjustmentGreen", 0, "0", true,
    #                         false), CRSSATURATIONADJUSTMTENTAQUA("crs:SaturationAdjustmentAqua", 0, "0", true,
    #                                 false), CRSSATURATIONADJUSTMENTBLUE("crs:SaturationAdjustmentBlue", 0, "0", true,
    #                                         false), CRSSATURATIONADJUSTMENTPURPLE("crs:SaturationAdjustmentPurple", 0,
    #                                                 "0", true, false), CRSSATURATIONADJUSTMENTMAGENTA(
    #                                                         "crs:HueAdjustmentMagenta", 0, "0", true, false),
    #
    # CRSLUMINANCEADJUSTMENTRED("crs:LuminanceAdjustmentRed", 0, "0", true, false), CRSLUMINANCEADJUSTMENTORANGE(
    #         "crs:LuminanceAdjustmentOrange", 0, "0", true,
    #         false), CRSLUMINANCEADJUSTMENTYELLOW("crs:LuminanceAdjustmentYellow", 0, "0", true,
    #                 false), CRSLUMINANCEADJUSTMENTGREEN("crs:LuminanceAdjustmentGreen", 0, "0", true,
    #                         false), CRSLUMINANCEADJUSTMENTAQUA("crs:LuminanceAdjustmentAqua", 0, "0", true,
    #                                 false), CRSLUMINANCEADJUSYMENTBLUE("crs:LuminanceAdjustmentBlue", 0, "0", true,
    #                                         false), CRSLUMINANCEADJUSTMENTPURPLE("crs:LuminanceAdjustmentPurple", 0,
    #                                                 "0", true, false), CRSLUMINANCEADJUSTMENTMAGENTA(
    #                                                         "crs:LuminanceAdjustmentMagenta", 0, "0", true, false),
    #
    # CRSSPLITTONINGSHADOWHUE("crs:SplitToningShadowHue", 0, "0", false, false), CRSSPLITTONINGSHADOWSATURATION(
    #         "crs:SplitToningShadowSaturation", 0, "0", false,
    #         false), CRSSPLITTONINGHIGHLIGHTHUE("crs:SplitToningHighlightHue", 0, "0", false,
    #                 false), CRSSPLITTONINGHIGHLIGHTSATURATION("crs:SplitToningHighlightSaturation", 0, "0", false,
    #                         false), CRSSPLITTONINGBALANCE("crs:SplitToningBalance", 0, "0", true, false),
    #
    # CRSPARAMETRICSHADOWS("crs:ParametricShadows", 0, "0", true, false), CRSPARAMETRICDARK("crs:ParametricDarks", 0, "0",
    #         true, false), CRSPARAMETRICLIGHTS("crs:ParametricLights", 0, "0", true, false), CRSPARAMETRICHIGHLIGHTS(
    #                 "crs:ParametricHighlights", 0, "0", true, false), CRSPARAMETRICSHADOWSPLIT(
    #                         "crs:ParametricShadowSplit", 0, "25", false, false), CRSPARAMETRICMIDTONESPLIT(
    #                                 "crs:ParametricMidtoneSplit", 0, "50", false, false), CRSPARAMETRICHIGHTLIGHTSPLIT(
    #                                         "crs:ParametricHighlightSplit", 0, "75", false, false),
    #
    # CRSSHARPENRADIUS("crs:SharpenRadius", 1, "+1.0", true, false), CRSSHARPENDETAIL("crs:SharpenDetail", 0, "25", false,
    #         false), CRSSHARPENEDGEMARKING("crs:SharpenEdgeMasking", 0, "0", false, false),
    #
    # CRSPOSTCROPVIGNETTEAMOUNT("crs:PostCropVignetteAmount", 0, "0", true, false), CRSPOSTCROPVIGNETTEMIDPOINT(
    #         "crs:PostCropVignetteMidpoint", 0, "50", false, false), CRSPOSTCROPVIGNETTEROUNDESS(
    #                 "crs:PostCropVignetteRoundness", 0, "0", true, false), CRSPOSTCROPVIGNETTEFEATHER(
    #                         "crs:PostCropVignetteFeather", 0, "0", false, false), CRSPOSTCROPVIGNETTEHIGHLIGHTCONTRAST(
    #                                 "crs:PostCropVignetteHighlightContrast", 0, "0", false, false),
    #
    # CRSGRAINAMOUNT("crs:GrainAmount", 0, "0", false, false), CRSGRAINSIZE("crs:GrainSize", 0, "25", false,
    #         false), CRSGRAINFREQUENCY("crs:GrainFrequency", 0, "50", false, false),
    #
    # CRSLUMINANCESMOOTHING("crs:LuminanceSmoothing", 0, "0", false, false), CRSLUMINANCENOISEREDUCITONDETAIL(
    #         "crs:LuminanceNoiseReductionDetail", 0, "50", false,
    #         false), CRSLUMINANCENOISEREDUCITONCONTRAST("crs:LuminanceNoiseReductionContrast", 0, "0", false, false),
    #
    # CRSCOLORNOISEREDUCTION("crs:ColorNoiseReduction", 0, "25", false, false), CRSCOLORNOISEREDUCTIONDETAIL(
    #         "crs:ColorNoiseReductionDetail", 0, "50", false,
    #         false), CRSCOLORNOISEREDUCITONSMOOTHNESS("crs:ColorNoiseReductionSmoothness", 0, "50", false, false),
    #
    # // //CRSLENSPROFILEENABLE ("", 0, "0", false),
    # CRSLENSEMANUALDESTORTIONAMOUNT("crs:LensManualDistortionAmount", 0, "0", true, false),
    #
    # CRSPERSPECTIVEVERTICAL("crs:PerspectiveVertical", 0, "0", true, false), CRSPERSPECTIVEHORIZONTAL(
    #         "crs:PerspectiveHorizontal", 0, "0", true, false), CRSPERSPECTIVEROTATE("crs:PerspectiveRotate", 1, "0.0",
    #                 true, false), CRSPERSPECIVESCALE("crs:PerspectiveScale", 0, "100", false,
    #                         false), CRSPERSPECTIVEASPECT("crs:PerspectiveAspect", 0, "0", true, false),
    # // CRSPERSPECTIVEUPRIGHT ("crs:PerspectiveUpright", 0, "0", false),
    # CRSPURSPECTIVEX("crs:PerspectiveX", 1, "0.0", true, false), CRSPERSPECTIVEY("crs:PerspectiveY", 1, "0.0", true,
    #         false),
    #
    # // CRSAUSTOLATERALCA ("crs:AutoLateralCA", 0, "0", false),
    #
    # CRSCONTRAST2012("crs:Contrast2012", 0, "0", true, false), CRSHIGHTLIGHTS2012("crs:Highlights2012", 0, "0", true,
    #         false), CRSSHADOWS2012("crs:Shadows2012", 0, "0", true, false), CRSWHITES2012("crs:Whites2012", 0, "0",
    #                 true, false), CRSBLACKS2012("crs:Blacks2012", 0, "0", true,
    #                         false), CRSCLARITY2012("crs:Clarity2012", 0, "0", true, false),
    #
    # CRSDEFRINGEPURPLEAMOUNT("crs:DefringePurpleAmount", 0, "0", false, false), CRSDEFRINGEPURPLEHUELO(
    #         "crs:DefringePurpleHueLo", 0, "30", false,
    #         false), CRSDEFRINGEPURPLEHUEHI("crs:DefringePurpleHueHi", 0, "70", false, false), CRSDEFRINGEGREENAMOUNT(
    #                 "crs:DefringeGreenAmount", 0, "0", false, false), CRSDEFRINGEGREENHUELO("crs:DefringeGreenHueLo", 0,
    #                         "40", false, false), CRSDEFRINGEGREENHUEHI("crs:DefringeGreenHueHi", 0, "60", false, false),
    #
    # CRSDEHAZE("crs:Dehaze", 0, "0", true, false),
    # // CRSTONEMAPSTRENGTH ("crs:ToneMapStrength", 0, "0", false),
            b'crs:CropLeft': __Xmp_Tag(6, "0", False, False),
            b'crs:CropBottom': __Xmp_Tag(6, "1", False, False),
            b'crs:CropRight': __Xmp_Tag(6, "1", False, False),
            b'crs:CropTop': __Xmp_Tag(6, "0", False, False),
            b'xmp:Rating': __Xmp_Tag(0, "0", False, False),
            b'crs:Exposure2012': __Xmp_Tag(2, "0", True, False),
            }


__Rendering_Tag = collections.namedtuple('Rendering_Tag', ['is_multi_valued', 'is_string', 'name', 'used_to_render'])

DEF_REND_TAG = __Rendering_Tag(False, False, '', False)

DNG_TAGS = {256: __Rendering_Tag(False, False, 'image_width', True),  # IMAGE_WIDTH
            257: __Rendering_Tag(False, False, 'image_length', True),  # IMAGE_LENGTH
            258: __Rendering_Tag(True, False, 'bits_per_sample', True),  # BYTES_PER_SAMPLE
            259: __Rendering_Tag(False, False, 'compression', True),  # COMPRESSION
            262: __Rendering_Tag(False, False, 'photometric_interpretation', True),  # PhotometricInterpretation (color space)
            273: __Rendering_Tag(True, False, 'strip_offsets', True),
            274: __Rendering_Tag(False, False, 'orientation', True),
            277: __Rendering_Tag(False, False, 'samples_per_pix', True),
            278: __Rendering_Tag(False, False, 'rows_per_strip', True),
            279: __Rendering_Tag(True, False, 'strip_byte_counts', True),
            284: __Rendering_Tag(False, False, 'planar_configuration', True),
            322: __Rendering_Tag(False, False, 'tile_width', True),
            323: __Rendering_Tag(False, False, 'tile_length', True),
            324: __Rendering_Tag(True, False, 'tile_offsets', True),
            325: __Rendering_Tag(True, False, 'tile_byte_counts', True),
            330: __Rendering_Tag(True, False, 'sub_ifds', False),
            339: __Rendering_Tag(True, False, 'sample_format', False),
            700: __Rendering_Tag(False, True, 'xmp', True),
            33421: __Rendering_Tag(True, False, 'cfa_repeat_pattern_dim', True),
            33422: __Rendering_Tag(True, False, 'cfa_pattern', True),
            # 34665: {'Name': 'exif_ifd', 'Used To Render': False},
            50710: __Rendering_Tag(False, False, 'cfa_plane_color', True),
            50711: __Rendering_Tag(False, False, 'cfa_layout', True),
            50712: __Rendering_Tag(False, False, 'linearization_table', True),
            50713: __Rendering_Tag(True, False, 'black_level_repeat_dim', True),
            50714: __Rendering_Tag(True, False, 'black_level', True),
            50715: __Rendering_Tag(True, False, 'black_level_delta_H', True),
            50716: __Rendering_Tag(True, False, 'black_level_delta_V', True),
            50717: __Rendering_Tag(True, False, 'white_level', True),
            50718: __Rendering_Tag(True, False, 'default_scale', True),
            50719: __Rendering_Tag(True, False, 'default_crop_origin', True),
            50720: __Rendering_Tag(True, False, 'default_crop_size', True),
            50829: __Rendering_Tag(True, False, 'active_area', True),
            50975: __Rendering_Tag(False, False, 'row_interleave_factor', True),
            }
