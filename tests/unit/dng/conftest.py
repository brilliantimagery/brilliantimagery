from collections import namedtuple

import pytest
import numpy as np

# XMP = namedtuple('XMP', ['xmp_data', 'attr_value_pairs'])
# XMP_VALUE = namedtuple('XMP_VALUE', ['attr', 'value'])
# xmp_data = '<?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?>.<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c128 79.159124, 2016/03/18-14:01:55        ">. <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">.  <rdf:Description rdf:about="".    xmlns:xmp="http://ns.adobe.com/xap/1.0/".    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/".    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/".    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/".    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#".    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#".    xmlns:dc="http://purl.org/dc/elements/1.1/".    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/".    xmlns:lr="http://ns.adobe.com/lightroom/1.0/".   xmp:ModifyDate="2018-12-23T16:20:34-08:00".   xmp:CreateDate="2017-09-07T16:01:38.03".   xmp:MetadataDate="2018-12-25T16:04:27-08:00".   xmp:Rating="2".   xmp:CreatorTool="Adobe Photoshop Lightroom 6.12 (Windows)".   aux:SerialNumber="222020003981".   aux:LensInfo="24/1 105/1 0/0 0/0".   aux:Lens="EF24-105mm f/4L IS USM".   aux:LensID="237".   aux:LensSerialNumber="0000712524".   aux:ImageNumber="0".   aux:ApproximateFocusDistance="100/100".   aux:FlashCompensation="0/1".   aux:Firmware="1.1.6".   photoshop:DateCreated="2017-09-07T16:01:38.03".   xmpMM:DocumentID="xmp.did:c4db0699-4104-4f40-b561-27c7c7b028dd".   xmpMM:OriginalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8".   xmpMM:InstanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2".   dc:format="image/dng".   crs:Version="9.12".   crs:ProcessVersion="6.7".   crs:WhiteBalance="Cloudy".   crs:AutoWhiteVersion="134348800".   crs:Temperature="6500".   crs:Tint="+10".   crs:Saturation="+9".   crs:Sharpness="25".   crs:LuminanceSmoothing="0".   crs:ColorNoiseReduction="25".   crs:VignetteAmount="0".   crs:ShadowTint="0".   crs:RedHue="0".   crs:RedSaturation="0".   crs:GreenHue="0".   crs:GreenSaturation="0".   crs:BlueHue="0".   crs:BlueSaturation="0".   crs:Vibrance="+29".   crs:HueAdjustmentRed="0".   crs:HueAdjustmentOrange="0".   crs:HueAdjustmentYellow="0".   crs:HueAdjustmentGreen="0".   crs:HueAdjustmentAqua="0".   crs:HueAdjustmentBlue="0".   crs:HueAdjustmentPurple="0".   crs:HueAdjustmentMagenta="0".   crs:SaturationAdjustmentRed="0".   crs:SaturationAdjustmentOrange="0".   crs:SaturationAdjustmentYellow="0".   crs:SaturationAdjustmentGreen="0".   crs:SaturationAdjustmentAqua="0".   crs:SaturationAdjustmentBlue="0".   crs:SaturationAdjustmentPurple="0".   crs:SaturationAdjustmentMagenta="0".   crs:LuminanceAdjustmentRed="0".   crs:LuminanceAdjustmentOrange="0".   crs:LuminanceAdjustmentYellow="0".   crs:LuminanceAdjustmentGreen="0".   crs:LuminanceAdjustmentAqua="0".   crs:LuminanceAdjustmentBlue="0".   crs:LuminanceAdjustmentPurple="0".   crs:LuminanceAdjustmentMagenta="0".   crs:SplitToningShadowHue="0".   crs:SplitToningShadowSaturation="0".   crs:SplitToningHighlightHue="0".   crs:SplitToningHighlightSaturation="0".   crs:SplitToningBalance="0".   crs:ParametricShadows="0".   crs:ParametricDarks="0".   crs:ParametricLights="0".   crs:ParametricHighlights="0".   crs:ParametricShadowSplit="25".   crs:ParametricMidtoneSplit="50".   crs:ParametricHighlightSplit="75".   crs:SharpenRadius="+1.0".   crs:SharpenDetail="25".   crs:SharpenEdgeMasking="0".   crs:PostCropVignetteAmount="0".   crs:GrainAmount="0".   crs:ColorNoiseReductionDetail="50".   crs:ColorNoiseReductionSmoothness="50".   crs:LensProfileEnable="0".   crs:LensManualDistortionAmount="0".   crs:PerspectiveVertical="0".   crs:PerspectiveHorizontal="0".   crs:PerspectiveRotate="0.0".   crs:PerspectiveScale="100".   crs:PerspectiveAspect="0".   crs:PerspectiveUpright="0".   crs:PerspectiveX="0.00".   crs:PerspectiveY="0.00".   crs:AutoLateralCA="0".   crs:Exposure2012="+0.20".   crs:Contrast2012="0".   crs:Highlights2012="+24".   crs:Shadows2012="-24".   crs:Whites2012="+31".   crs:Blacks2012="-10".   crs:Clarity2012="0".   crs:DefringePurpleAmount="0".   crs:DefringePurpleHueLo="30".   crs:DefringePurpleHueHi="70".   crs:DefringeGreenAmount="0".   crs:DefringeGreenHueLo="40".   crs:DefringeGreenHueHi="60".   crs:Dehaze="0".   crs:ToneMapStrength="0".   crs:ConvertToGrayscale="False".   crs:ToneCurveName="Medium Contrast".   crs:ToneCurveName2012="Linear".   crs:CameraProfile="Adobe Standard".   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975".   crs:LensProfileSetup="LensDefaults".   crs:UprightVersion="151388160".   crs:UprightCenterMode="0".   crs:UprightCenterNormX="0.5".   crs:UprightCenterNormY="0.5".   crs:UprightFocalMode="0".   crs:UprightFocalLength35mm="35".   crs:UprightPreview="False".   crs:UprightTransformCount="6".   crs:UprightFourSegmentsCount="0".   crs:HasSettings="True".   crs:CropTop="0.050467".   crs:CropLeft="0.050467".   crs:CropBottom="0.969144".   crs:CropRight="0.969144".   crs:CropAngle="0".   crs:CropConstrainToWarp="0".   crs:HasCrop="True".   crs:AlreadyApplied="False".   crs:RawFileName="test_image_canon_6d.dng">.   <xmpMM:History>.    <rdf:Seq>.     <rdf:li.      stEvt:action="derived".      stEvt:parameters="converted from image/x-canon-cr2 to image/dng, saved to new location"/>.     <rdf:li.      stEvt:action="saved".      stEvt:instanceID="xmp.iid:c4db0699-4104-4f40-b561-27c7c7b028dd".      stEvt:when="2018-12-23T16:20:34-08:00".      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)".      stEvt:changed="/"/>.     <rdf:li.      stEvt:action="saved".      stEvt:instanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2".      stEvt:when="2018-12-25T16:04:27-08:00".      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)".      stEvt:changed="/metadata"/>.    </rdf:Seq>.   </xmpMM:History>.   <xmpMM:DerivedFrom.    stRef:documentID="6BF93FCB1F578C3204916BCCDEAD23D8".    stRef:originalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"/>.   <dc:subject>.    <rdf:Bag>.     <rdf:li>Jelleybean</rdf:li>.    </rdf:Bag>.   </dc:subject>.   <crs:ToneCurve>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>32, 22</rdf:li>.     <rdf:li>64, 56</rdf:li>.     <rdf:li>128, 128</rdf:li>.     <rdf:li>192, 196</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurve>.   <crs:ToneCurveRed>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveRed>.   <crs:ToneCurveGreen>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveGreen>.   <crs:ToneCurveBlue>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveBlue>.   <crs:ToneCurvePV2012>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012>.   <crs:ToneCurvePV2012Red>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Red>.   <crs:ToneCurvePV2012Green>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Green>.   <crs:ToneCurvePV2012Blue>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Blue>.   <lr:hierarchicalSubject>.    <rdf:Bag>.     <rdf:li>Jelleybean</rdf:li>.    </rdf:Bag>.   </lr:hierarchicalSubject>.  </rdf:Description>. </rdf:RDF>.</x:xmpmeta> <?xpacket end="w"?>'
# xmp_data = bytes(xmp_data, 'utf-8')

xmp_to_try = ((b'xmp:Rating', '2'),
              (b'crs:Saturation', '+9'),
              (b'crs:Exposure2012', '+0.20'),
              (b'crs:Shadows2012', '-24'),
              (b'crs:RedHue', '0'),
              (b'crs:CropTop', '0.050467'),
              # (b'crs:AlreadyApplied', 'False'),
              )

expected_xmp = {b'crs:Temperature': 6500.0, b'crs:Tint': 10.0, b'crs:Saturation': 9.0, b'crs:Vibrance': 29.0,
                b'crs:Sharpness': 25.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:RedSaturation': 0.0,
                b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0,
                b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0,
                b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 0.0,
                b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0,
                b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0,
                b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0,
                b'crs:SaturationAdjustmentBlue': 0.0, b'crs:SaturationAdjustmentPurple': 0.0,
                b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0,
                b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0,
                b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0,
                b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0,
                b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0,
                b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0,
                b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0,
                b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0,
                b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0,
                b'crs:ColorNoiseReductionDetail': 50.0,
                b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0,
                b'crs:Contrast2012': 0.0, b'crs:Highlights2012': 24.0, b'crs:Shadows2012': -24.0,
                b'crs:Whites2012': 31.0, b'crs:Blacks2012': -10.0, b'crs:Clarity2012': 0.0,
                b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0,
                b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0,
                b'crs:Dehaze': 0.0, b'crs:CropLeft': 0.050467, b'crs:CropBottom': 0.969144, b'crs:CropRight': 0.969144,
                b'crs:CropTop': 0.050467, b'xmp:Rating': 2.0, b'crs:Exposure2012': 0.2}

new_xmp_values = {b'xmp:Rating': '3',
                  b'crs:Saturation': '+11',
                  b'crs:Exposure2012': '+0.40',
                  b'crs:Shadows2012': '-28',
                  b'crs:RedHue': '4',
                  b'crs:CropTop': '0.06',
                  b'crs:AlreadyApplied': 'True',
                  }
updated_xmp = {b'crs:Temperature': 6500.0, b'crs:Tint': 10.0, b'crs:Saturation': '+11', b'crs:Vibrance': 29.0,
               b'crs:Sharpness': 25.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': '4', b'crs:RedSaturation': 0.0,
               b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0,
               b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0,
               b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 0.0,
               b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0,
               b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0,
               b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0,
               b'crs:SaturationAdjustmentBlue': 0.0, b'crs:SaturationAdjustmentPurple': 0.0,
               b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0,
               b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0,
               b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0,
               b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0,
               b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0,
               b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0,
               b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0,
               b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0,
               b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0, b'crs:ColorNoiseReductionDetail': 50.0,
               b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0,
               b'crs:Contrast2012': 0.0, b'crs:Highlights2012': 24.0, b'crs:Shadows2012': '-28',
               b'crs:Whites2012': 31.0, b'crs:Blacks2012': -10.0, b'crs:Clarity2012': 0.0,
               b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0,
               b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0,
               b'crs:Dehaze': 0.0, b'crs:CropLeft': 0.050467, b'crs:CropBottom': 0.969144, b'crs:CropRight': 0.969144,
               b'crs:CropTop': '0.06', b'xmp:Rating': '3', b'crs:Exposure2012': '+0.40'}

xmp_to_be_stored = {b'crs:Temperature': {'val': 6500.0, 'updated': False}, b'crs:Tint': {'val': 10.0, 'updated': False},
                    b'crs:Saturation': {'val': '+11', 'updated': True},
                    b'crs:Vibrance': {'val': 29.0, 'updated': False},
                    b'crs:Sharpness': {'val': 25.0, 'updated': False},
                    b'crs:ShadowTint': {'val': 0.0, 'updated': False},
                    b'crs:RedHue': {'val': '4', 'updated': True}, b'crs:RedSaturation': {'val': 0.0, 'updated': False},
                    b'crs:GreenHue': {'val': 0.0, 'updated': False},
                    b'crs:GreenSaturation': {'val': 0.0, 'updated': False},
                    b'crs:BlueHue': {'val': 0.0, 'updated': False},
                    b'crs:BlueSaturation': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentRed': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentOrange': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentYellow': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentGreen': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentAqua': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentBlue': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentPurple': {'val': 0.0, 'updated': False},
                    b'crs:HueAdjustmentMagenta': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentRed': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentOrange': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentYellow': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentGreen': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentAqua': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentBlue': {'val': 0.0, 'updated': False},
                    b'crs:SaturationAdjustmentPurple': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentRed': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentOrange': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentYellow': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentGreen': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentAqua': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentBlue': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentPurple': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceAdjustmentMagenta': {'val': 0.0, 'updated': False},
                    b'crs:ParametricShadows': {'val': 0.0, 'updated': False},
                    b'crs:ParametricDarks': {'val': 0.0, 'updated': False},
                    b'crs:ParametricLights': {'val': 0.0, 'updated': False},
                    b'crs:ParametricHighlights': {'val': 0.0, 'updated': False},
                    b'crs:ParametricShadowSplit': {'val': 25.0, 'updated': False},
                    b'crs:ParametricMidtoneSplit': {'val': 50.0, 'updated': False},
                    b'crs:ParametricHighlightSplit': {'val': 75.0, 'updated': False},
                    b'crs:SharpenRadius': {'val': 1.0, 'updated': False},
                    b'crs:SharpenDetail': {'val': 25.0, 'updated': False},
                    b'crs:SharpenEdgeMasking': {'val': 0.0, 'updated': False},
                    b'crs:GrainAmount': {'val': 0.0, 'updated': False},
                    b'crs:LuminanceSmoothing': {'val': 0.0, 'updated': False},
                    b'crs:ColorNoiseReduction': {'val': 25.0, 'updated': False},
                    b'crs:ColorNoiseReductionDetail': {'val': 50.0, 'updated': False},
                    b'crs:ColorNoiseReductionSmoothness': {'val': 50.0, 'updated': False},
                    b'crs:LensManualDistortionAmount': {'val': 0.0, 'updated': False},
                    b'crs:Contrast2012': {'val': 0.0, 'updated': False},
                    b'crs:Highlights2012': {'val': 24.0, 'updated': False},
                    b'crs:Shadows2012': {'val': '-28', 'updated': True},
                    b'crs:Whites2012': {'val': 31.0, 'updated': False},
                    b'crs:Blacks2012': {'val': -10.0, 'updated': False},
                    b'crs:Clarity2012': {'val': 0.0, 'updated': False},
                    b'crs:DefringePurpleAmount': {'val': 0.0, 'updated': False},
                    b'crs:DefringePurpleHueLo': {'val': 30.0, 'updated': False},
                    b'crs:DefringePurpleHueHi': {'val': 70.0, 'updated': False},
                    b'crs:DefringeGreenAmount': {'val': 0.0, 'updated': False},
                    b'crs:DefringeGreenHueLo': {'val': 40.0, 'updated': False},
                    b'crs:DefringeGreenHueHi': {'val': 60.0, 'updated': False},
                    b'crs:Dehaze': {'val': 0.0, 'updated': False}, b'crs:CropLeft': {'val': 0.050467, 'updated': False},
                    b'crs:CropBottom': {'val': 0.969144, 'updated': False},
                    b'crs:CropRight': {'val': 0.969144, 'updated': False},
                    b'crs:CropTop': {'val': '0.06', 'updated': True}, b'xmp:Rating': {'val': '3', 'updated': True},
                    b'crs:Exposure2012': {'val': '+0.40', 'updated': True}, b'crs:AlreadyApplied': {}}

stored_xmp = {b'crs:Temperature': {'val': 6500.0, 'updated': False}, b'crs:Tint': {'val': 10.0, 'updated': False},
              b'crs:Saturation': {'val': '+11', 'updated': True}, b'crs:Vibrance': {'val': 29.0, 'updated': False},
              b'crs:Sharpness': {'val': 25.0, 'updated': False}, b'crs:ShadowTint': {'val': 0.0, 'updated': False},
              b'crs:RedHue': {'val': '4', 'updated': True}, b'crs:RedSaturation': {'val': 0.0, 'updated': False},
              b'crs:GreenHue': {'val': 0.0, 'updated': False}, b'crs:GreenSaturation': {'val': 0.0, 'updated': False},
              b'crs:BlueHue': {'val': 0.0, 'updated': False}, b'crs:BlueSaturation': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentRed': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentOrange': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentYellow': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentGreen': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentAqua': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentBlue': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentPurple': {'val': 0.0, 'updated': False},
              b'crs:HueAdjustmentMagenta': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentRed': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentOrange': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentYellow': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentGreen': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentAqua': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentBlue': {'val': 0.0, 'updated': False},
              b'crs:SaturationAdjustmentPurple': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentRed': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentOrange': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentYellow': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentGreen': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentAqua': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentBlue': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentPurple': {'val': 0.0, 'updated': False},
              b'crs:LuminanceAdjustmentMagenta': {'val': 0.0, 'updated': False},
              b'crs:ParametricShadows': {'val': 0.0, 'updated': False},
              b'crs:ParametricDarks': {'val': 0.0, 'updated': False},
              b'crs:ParametricLights': {'val': 0.0, 'updated': False},
              b'crs:ParametricHighlights': {'val': 0.0, 'updated': False},
              b'crs:ParametricShadowSplit': {'val': 25.0, 'updated': False},
              b'crs:ParametricMidtoneSplit': {'val': 50.0, 'updated': False},
              b'crs:ParametricHighlightSplit': {'val': 75.0, 'updated': False},
              b'crs:SharpenRadius': {'val': 1.0, 'updated': False},
              b'crs:SharpenDetail': {'val': 25.0, 'updated': False},
              b'crs:SharpenEdgeMasking': {'val': 0.0, 'updated': False},
              b'crs:GrainAmount': {'val': 0.0, 'updated': False},
              b'crs:LuminanceSmoothing': {'val': 0.0, 'updated': False},
              b'crs:ColorNoiseReduction': {'val': 25.0, 'updated': False},
              b'crs:ColorNoiseReductionDetail': {'val': 50.0, 'updated': False},
              b'crs:ColorNoiseReductionSmoothness': {'val': 50.0, 'updated': False},
              b'crs:LensManualDistortionAmount': {'val': 0.0, 'updated': False},
              b'crs:Contrast2012': {'val': 0.0, 'updated': False},
              b'crs:Highlights2012': {'val': 24.0, 'updated': False},
              b'crs:Shadows2012': {'val': '-28', 'updated': True}, b'crs:Whites2012': {'val': 31.0, 'updated': False},
              b'crs:Blacks2012': {'val': -10.0, 'updated': False}, b'crs:Clarity2012': {'val': 0.0, 'updated': False},
              b'crs:DefringePurpleAmount': {'val': 0.0, 'updated': False},
              b'crs:DefringePurpleHueLo': {'val': 30.0, 'updated': False},
              b'crs:DefringePurpleHueHi': {'val': 70.0, 'updated': False},
              b'crs:DefringeGreenAmount': {'val': 0.0, 'updated': False},
              b'crs:DefringeGreenHueLo': {'val': 40.0, 'updated': False},
              b'crs:DefringeGreenHueHi': {'val': 60.0, 'updated': False},
              b'crs:Dehaze': {'val': 0.0, 'updated': False}, b'crs:CropLeft': {'val': 0.050467, 'updated': False},
              b'crs:CropBottom': {'val': 0.969144, 'updated': False},
              b'crs:CropRight': {'val': 0.969144, 'updated': False}, b'crs:CropTop': {'val': '0.06', 'updated': True},
              b'xmp:Rating': {'val': '3', 'updated': True}, b'crs:Exposure2012': {'val': '+0.40', 'updated': True},
              b'crs:AlreadyApplied': {}}

BoundingBox = namedtuple('BoundingBox', ['input', 'x0', 'y0', 'x1', 'y1', 'output'])
bounding_boxes = (BoundingBox([100, 100, 100, 100], 400, 400, 0, 200, [100, 100, 100, 200]),
                  BoundingBox([100, 100, 100, 200], 400, 400, 500, 0, [100, 100, 500, 200]),
                  BoundingBox([100, 100, 500, 200], 400, 50, 0, 0, [100, 50, 500, 200]),
                  BoundingBox([100, 50, 500, 200], 2, 400, 0, 0, [2, 50, 500, 200]),
                  )

# Crops = namedtuple('Crops', ['x0', 'y0', 'x1', 'y1'])
# used_fields = {'bits_per_sample': [16], 'tile_offsets': [831426, 886690, 947520, 1010088, 1068440, 1123368, 1181282, 1240416, 1292672, 1338188, 1382588, 1426656, 1470310, 1513722, 1557016, 1600274, 1643664, 1686910, 1730202, 1773250, 1815934, 1858712, 1897038, 1944524, 2001720, 2063388, 2118564, 2174494, 2233034, 2290956, 2344610, 2389622, 2433838, 2477966, 2521706, 2565448, 2610014, 2654102, 2698052, 2742364, 2785792, 2828790, 2871726, 2914500, 2952754, 2998304, 3043076, 3088012, 3134556, 3181924, 3227502, 3272492, 3317972, 3363820, 3413198, 3463930, 3514398, 3567306, 3625922, 3679108, 3728246, 3778414, 3825420, 3874058, 3918296, 3961500, 3999930, 4044652, 4089370, 4133120, 4176908, 4220814, 4265448, 4315554, 4374790, 4439040, 4505552, 4572596, 4634764, 4695880, 4760462, 4822788, 4879086, 4932444, 4984520, 5040900, 5091214, 5136632, 5175066, 5219722, 5264502, 5308730, 5352500, 5398244, 5451854, 5510964, 5576854, 5645096, 5713010, 5780346, 5847442, 5913758, 5979068, 6044914, 6108404, 6164920, 6226308, 6286406, 6338296, 6386680, 6428012, 6471486, 6516308, 6561298, 6607036, 6667940, 6729954, 6784612, 6842272, 6910186, 6980410, 7048674, 7116556, 7185348, 7250788, 7318078, 7385510, 7448526, 7513508, 7573790, 7624942, 7676682, 7724468, 7770346, 7819400, 7866972, 7913224, 7960370, 8011906, 8068692, 8121120, 8181364, 8249630, 8319528, 8388148, 8456908, 8523000, 8593036, 8661046, 8726868, 8794134, 8858760, 8916284, 8977398, 9028920, 9077046, 9124702, 9169976, 9213976, 9258222, 9301868, 9350828, 9404906, 9461218, 9524094, 9592180, 9658828, 9726460, 9795010, 9865556, 9933078, 9999200, 10064926, 10134396, 10199066, 10261388, 10310734, 10356592, 10401734, 10447688, 10495926, 10542646, 10585756, 10630682, 10683102, 10740516, 10800438, 10866356, 10931364, 10999822, 11068776, 11137052, 11203166, 11267154, 11330572, 11400972, 11470780, 11532562, 11580940, 11627578, 11674238, 11722122, 11771464, 11820476, 11868734, 11916454, 11965182, 12014776, 12068354, 12131394, 12195158, 12263230, 12331806, 12398076, 12462496, 12525320, 12589102, 12658792, 12732022, 12796160, 12847826, 12904478, 12961472, 13017038, 13070896, 13119622, 13168982, 13218066, 13267846, 13316826, 13379314, 13444340, 13505808, 13564652, 13631466, 13696734, 13759352, 13821112, 13886832, 13953880, 14019698, 14086336, 14142490, 14193510, 14250252, 14308224, 14366862, 14426172, 14482974, 14534712, 14583104, 14634310, 14695050, 14754162, 14804856, 14853258, 14909444, 14971812, 15035736, 15096136, 15159780, 15224512, 15286824, 15349048, 15403468, 15455740, 15509258, 15562402, 15617054, 15674078, 15733248, 15794702, 15856098, 15916862, 15973098, 16031294, 16084004, 16130728, 16176564, 16225698, 16283406, 16345166, 16403576, 16464730, 16520744, 16569212, 16611414, 16667942, 16726702, 16785048, 16842432, 16898444, 16953510, 17009430, 17065914, 17124742, 17184502, 17245566, 17307124, 17362666, 17411764, 17459612, 17507472, 17556068, 17604260, 17652142, 17698652, 17744904, 17786902, 17822308, 17859602, 17897430, 17934068, 17969528, 18003748, 18037730, 18074154, 18112866, 18147782, 18185406, 18222156, 18255590, 18286022, 18317440, 18348724, 18379750, 18410350, 18439752, 18469392, 18505582], 'tile_byte_counts': [55264, 60829, 62568, 58352, 54927, 57914, 59134, 52255, 45516, 44400, 44067, 43653, 43412, 43293, 43257, 43390, 43246, 43291, 43047, 42684, 42778, 38326, 47486, 57195, 61668, 55175, 55930, 58540, 57921, 53654, 45011, 44215, 44128, 43740, 43742, 44565, 44088, 43949, 44311, 43427, 42998, 42935, 42773, 38253, 45549, 44772, 44936, 46544, 47367, 45578, 44989, 45479, 45848, 49378, 50732, 50467, 52907, 58616, 53186, 49137, 50168, 47006, 48637, 44237, 43204, 38429, 44722, 44717, 43750, 43787, 43906, 44634, 50106, 59235, 64249, 66512, 67043, 62168, 61115, 64582, 62326, 56298, 53357, 52075, 56380, 50313, 45417, 38434, 44655, 44780, 44228, 43770, 45743, 53610, 59109, 65889, 68241, 67913, 67336, 67095, 66315, 65309, 65846, 63490, 56516, 61388, 60097, 51889, 48383, 41331, 43474, 44821, 44990, 45738, 60904, 62014, 54657, 57659, 67914, 70223, 68263, 67881, 68791, 65439, 67289, 67432, 63015, 64982, 60282, 51151, 51739, 47786, 45877, 49054, 47572, 46252, 47146, 51536, 56786, 52428, 60244, 68265, 69898, 68620, 68759, 66091, 70036, 68010, 65821, 67265, 64625, 57523, 61113, 51522, 48125, 47656, 45273, 44000, 44245, 43645, 48960, 54077, 56312, 62876, 68085, 66647, 67632, 68549, 70545, 67522, 66122, 65725, 69469, 64669, 62322, 49345, 45857, 45141, 45954, 48238, 46720, 43109, 44926, 52419, 57414, 59921, 65918, 65007, 68458, 68953, 68275, 66114, 63987, 63417, 70400, 69808, 61782, 48378, 46638, 46659, 47883, 49342, 49011, 48258, 47720, 48727, 49593, 53577, 63039, 63763, 68071, 68575, 66270, 64420, 62823, 63781, 69689, 73230, 64137, 51665, 56652, 56994, 55566, 53858, 48726, 49360, 49083, 49780, 48979, 62488, 65026, 61467, 58843, 66814, 65268, 62617, 61759, 65719, 67048, 65817, 66637, 56154, 51020, 56742, 57972, 58637, 59309, 56801, 51738, 48391, 51205, 60739, 59112, 50693, 48402, 56185, 62367, 63924, 60399, 63643, 64732, 62311, 62223, 54419, 52271, 53518, 53143, 54652, 57023, 59170, 61453, 61395, 60763, 56236, 58196, 52710, 46724, 45835, 49133, 57708, 61759, 58409, 61154, 56014, 48467, 42202, 56527, 58760, 58346, 57383, 56012, 55065, 55920, 56483, 58828, 59760, 61064, 61557, 55541, 49098, 47848, 47860, 48596, 48192, 47882, 46510, 46252, 41998, 35405, 37294, 37828, 36638, 35460, 34219, 33982, 36424, 38711, 34916, 37623, 36750, 33434, 30431, 31417, 31284, 31025, 30600, 29402, 29640, 36190, 30458], 'cfa_repeat_pattern_dim': [2, 2], 'cfa_pattern': [0, 1, 1, 2], 'black_level_repeat_dim': [2, 2], 'black_level': [2047.0, 2047.0, 2048.0, 2047.0], 'white_level': [15000], 'default_scale': [1.0, 1.0], 'default_crop_origin': [12.0, 12.0], 'default_crop_size': [5472.0, 3648.0], 'active_area': [38, 72, 3708, 5568], 'image_width': 5568, 'image_length': 3708, 'compression': 7, 'photometric_interpretation': 32803, 'samples_per_pix': 1, 'planar_configuration': 1, 'tile_width': 256, 'tile_length': 256, 'cfa_plane_color': 0, 'cfa_layout': 1, 'orientation': 1}

used_fields = {'bits_per_sample': [16],
               'tile_offsets': [831426, 886690, 947520, 1010088, 1068440, 1123368, 1181282, 1240416, 1292672,
                                1338188, 1382588, 1426656, 1470310, 1513722, 1557016, 1600274, 1643664, 1686910,
                                1730202, 1773250, 1815934, 1858712, 1897038, 1944524, 2001720, 2063388, 2118564,
                                2174494, 2233034, 2290956, 2344610, 2389622, 2433838, 2477966, 2521706, 2565448,
                                2610014, 2654102, 2698052, 2742364, 2785792, 2828790, 2871726, 2914500, 2952754,
                                2998304, 3043076, 3088012, 3134556, 3181924, 3227502, 3272492, 3317972, 3363820,
                                3413198, 3463930, 3514398, 3567306, 3625922, 3679108, 3728246, 3778414, 3825420,
                                3874058, 3918296, 3961500, 3999930, 4044652, 4089370, 4133120, 4176908, 4220814,
                                4265448, 4315554, 4374790, 4439040, 4505552, 4572596, 4634764, 4695880, 4760462,
                                4822788, 4879086, 4932444, 4984520, 5040900, 5091214, 5136632, 5175066, 5219722,
                                5264502, 5308730, 5352500, 5398244, 5451854, 5510964, 5576854, 5645096, 5713010,
                                5780346, 5847442, 5913758, 5979068, 6044914, 6108404, 6164920, 6226308, 6286406,
                                6338296, 6386680, 6428012, 6471486, 6516308, 6561298, 6607036, 6667940, 6729954,
                                6784612, 6842272, 6910186, 6980410, 7048674, 7116556, 7185348, 7250788, 7318078,
                                7385510, 7448526, 7513508, 7573790, 7624942, 7676682, 7724468, 7770346, 7819400,
                                7866972, 7913224, 7960370, 8011906, 8068692, 8121120, 8181364, 8249630, 8319528,
                                8388148, 8456908, 8523000, 8593036, 8661046, 8726868, 8794134, 8858760, 8916284,
                                8977398, 9028920, 9077046, 9124702, 9169976, 9213976, 9258222, 9301868, 9350828,
                                9404906, 9461218, 9524094, 9592180, 9658828, 9726460, 9795010, 9865556, 9933078,
                                9999200, 10064926, 10134396, 10199066, 10261388, 10310734, 10356592, 10401734,
                                10447688, 10495926, 10542646, 10585756, 10630682, 10683102, 10740516, 10800438,
                                10866356, 10931364, 10999822, 11068776, 11137052, 11203166, 11267154, 11330572,
                                11400972, 11470780, 11532562, 11580940, 11627578, 11674238, 11722122, 11771464,
                                11820476, 11868734, 11916454, 11965182, 12014776, 12068354, 12131394, 12195158,
                                12263230, 12331806, 12398076, 12462496, 12525320, 12589102, 12658792, 12732022,
                                12796160, 12847826, 12904478, 12961472, 13017038, 13070896, 13119622, 13168982,
                                13218066, 13267846, 13316826, 13379314, 13444340, 13505808, 13564652, 13631466,
                                13696734, 13759352, 13821112, 13886832, 13953880, 14019698, 14086336, 14142490,
                                14193510, 14250252, 14308224, 14366862, 14426172, 14482974, 14534712, 14583104,
                                14634310, 14695050, 14754162, 14804856, 14853258, 14909444, 14971812, 15035736,
                                15096136, 15159780, 15224512, 15286824, 15349048, 15403468, 15455740, 15509258,
                                15562402, 15617054, 15674078, 15733248, 15794702, 15856098, 15916862, 15973098,
                                16031294, 16084004, 16130728, 16176564, 16225698, 16283406, 16345166, 16403576,
                                16464730, 16520744, 16569212, 16611414, 16667942, 16726702, 16785048, 16842432,
                                16898444, 16953510, 17009430, 17065914, 17124742, 17184502, 17245566, 17307124,
                                17362666, 17411764, 17459612, 17507472, 17556068, 17604260, 17652142, 17698652,
                                17744904, 17786902, 17822308, 17859602, 17897430, 17934068, 17969528, 18003748,
                                18037730, 18074154, 18112866, 18147782, 18185406, 18222156, 18255590, 18286022,
                                18317440, 18348724, 18379750, 18410350, 18439752, 18469392, 18505582],
               'tile_byte_counts': [55264, 60829, 62568, 58352, 54927, 57914, 59134, 52255, 45516, 44400, 44067,
                                    43653, 43412, 43293, 43257, 43390, 43246, 43291, 43047, 42684, 42778, 38326,
                                    47486, 57195, 61668, 55175, 55930, 58540, 57921, 53654, 45011, 44215, 44128,
                                    43740, 43742, 44565, 44088, 43949, 44311, 43427, 42998, 42935, 42773, 38253,
                                    45549, 44772, 44936, 46544, 47367, 45578, 44989, 45479, 45848, 49378, 50732,
                                    50467, 52907, 58616, 53186, 49137, 50168, 47006, 48637, 44237, 43204, 38429,
                                    44722, 44717, 43750, 43787, 43906, 44634, 50106, 59235, 64249, 66512, 67043,
                                    62168, 61115, 64582, 62326, 56298, 53357, 52075, 56380, 50313, 45417, 38434,
                                    44655, 44780, 44228, 43770, 45743, 53610, 59109, 65889, 68241, 67913, 67336,
                                    67095, 66315, 65309, 65846, 63490, 56516, 61388, 60097, 51889, 48383, 41331,
                                    43474, 44821, 44990, 45738, 60904, 62014, 54657, 57659, 67914, 70223, 68263,
                                    67881, 68791, 65439, 67289, 67432, 63015, 64982, 60282, 51151, 51739, 47786,
                                    45877, 49054, 47572, 46252, 47146, 51536, 56786, 52428, 60244, 68265, 69898,
                                    68620, 68759, 66091, 70036, 68010, 65821, 67265, 64625, 57523, 61113, 51522,
                                    48125, 47656, 45273, 44000, 44245, 43645, 48960, 54077, 56312, 62876, 68085,
                                    66647, 67632, 68549, 70545, 67522, 66122, 65725, 69469, 64669, 62322, 49345,
                                    45857, 45141, 45954, 48238, 46720, 43109, 44926, 52419, 57414, 59921, 65918,
                                    65007, 68458, 68953, 68275, 66114, 63987, 63417, 70400, 69808, 61782, 48378,
                                    46638, 46659, 47883, 49342, 49011, 48258, 47720, 48727, 49593, 53577, 63039,
                                    63763, 68071, 68575, 66270, 64420, 62823, 63781, 69689, 73230, 64137, 51665,
                                    56652, 56994, 55566, 53858, 48726, 49360, 49083, 49780, 48979, 62488, 65026,
                                    61467, 58843, 66814, 65268, 62617, 61759, 65719, 67048, 65817, 66637, 56154,
                                    51020, 56742, 57972, 58637, 59309, 56801, 51738, 48391, 51205, 60739, 59112,
                                    50693, 48402, 56185, 62367, 63924, 60399, 63643, 64732, 62311, 62223, 54419,
                                    52271, 53518, 53143, 54652, 57023, 59170, 61453, 61395, 60763, 56236, 58196,
                                    52710, 46724, 45835, 49133, 57708, 61759, 58409, 61154, 56014, 48467, 42202,
                                    56527, 58760, 58346, 57383, 56012, 55065, 55920, 56483, 58828, 59760, 61064,
                                    61557, 55541, 49098, 47848, 47860, 48596, 48192, 47882, 46510, 46252, 41998,
                                    35405, 37294, 37828, 36638, 35460, 34219, 33982, 36424, 38711, 34916, 37623,
                                    36750, 33434, 30431, 31417, 31284, 31025, 30600, 29402, 29640, 36190, 30458],
               'cfa_repeat_pattern_dim': [2, 2], 'cfa_pattern': [0, 1, 1, 2], 'black_level_repeat_dim': [2, 2],
               'black_level': [2047.0, 2047.0, 2048.0, 2047.0], 'white_level': [15000], 'default_scale': [1.0, 1.0],
               'default_crop_origin': [12.0, 12.0], 'default_crop_size': [5472.0, 3648.0],
               'active_area': [38, 72, 3708, 5568], 'image_width': 5568, 'image_length': 3708, 'compression': 7,
               'photometric_interpretation': 32803, 'samples_per_pix': 1, 'planar_configuration': 1,
               'tile_width': 256, 'tile_length': 256, 'cfa_plane_color': 0, 'cfa_layout': 1, 'orientation': 1}


def id_xmp_data(fixture_value):
    """A function to generate fixture IDs"""
    return f'xmp({fixture_value[0]}, {fixture_value[1]})'


@pytest.fixture(params=xmp_to_try, ids=id_xmp_data)
def xmp_params(request):
    return request.param


@pytest.fixture(params=bounding_boxes)
def bounding_box_params(request):
    return request.param


@pytest.fixture()
def used_ifd_fields():
    return used_fields


@pytest.fixture()
def dng_canon_6d(data_folder_path):
    from BrilliantImagery.dng import DNG
    return DNG(str(data_folder_path / 'test_image_canon_6d.dng'))


@pytest.fixture()
def numpy_cropped_canon_6d(data_folder_path):
    image = np.load(str(data_folder_path / 'test_image_canon_6d_cropped.npy'))
    rendered_area = [1500 / 5030, 1450 / 3350, (1500 + 700) / 5030, (1450 + 760) / 3350]

    return image, rendered_area


@pytest.fixture()
def numpy_thumbnail_canon_6d(data_folder_path):
    return np.load(str(data_folder_path / 'test_image_canon_6d_thumb.npy'))


@pytest.fixture()
def dng_xmp():
    return expected_xmp


@pytest.fixture()
def updated_dng_xmp():
    return updated_xmp, new_xmp_values


@pytest.fixture()
def storable_dng_xmp():
    return xmp_to_be_stored, stored_xmp
