from collections import namedtuple

import pytest
import numpy as np

xmp_data = '<?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?>.<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c128 79.159124, 2016/03/18-14:01:55        ">. <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">.  <rdf:Description rdf:about="".    xmlns:xmp="http://ns.adobe.com/xap/1.0/".    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/".    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/".    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/".    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#".    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#".    xmlns:dc="http://purl.org/dc/elements/1.1/".    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/".    xmlns:lr="http://ns.adobe.com/lightroom/1.0/".   xmp:ModifyDate="2018-12-23T16:20:34-08:00".   xmp:CreateDate="2017-09-07T16:01:38.03".   xmp:MetadataDate="2018-12-25T16:04:27-08:00".   xmp:Rating="2".   xmp:CreatorTool="Adobe Photoshop Lightroom 6.12 (Windows)".   aux:SerialNumber="222020003981".   aux:LensInfo="24/1 105/1 0/0 0/0".   aux:Lens="EF24-105mm f/4L IS USM".   aux:LensID="237".   aux:LensSerialNumber="0000712524".   aux:ImageNumber="0".   aux:ApproximateFocusDistance="100/100".   aux:FlashCompensation="0/1".   aux:Firmware="1.1.6".   photoshop:DateCreated="2017-09-07T16:01:38.03".   xmpMM:DocumentID="xmp.did:c4db0699-4104-4f40-b561-27c7c7b028dd".   xmpMM:OriginalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8".   xmpMM:InstanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2".   dc:format="image/dng".   crs:Version="9.12".   crs:ProcessVersion="6.7".   crs:WhiteBalance="Cloudy".   crs:AutoWhiteVersion="134348800".   crs:Temperature="6500".   crs:Tint="+10".   crs:Saturation="+9".   crs:Sharpness="25".   crs:LuminanceSmoothing="0".   crs:ColorNoiseReduction="25".   crs:VignetteAmount="0".   crs:ShadowTint="0".   crs:RedHue="0".   crs:RedSaturation="0".   crs:GreenHue="0".   crs:GreenSaturation="0".   crs:BlueHue="0".   crs:BlueSaturation="0".   crs:Vibrance="+29".   crs:HueAdjustmentRed="0".   crs:HueAdjustmentOrange="0".   crs:HueAdjustmentYellow="0".   crs:HueAdjustmentGreen="0".   crs:HueAdjustmentAqua="0".   crs:HueAdjustmentBlue="0".   crs:HueAdjustmentPurple="0".   crs:HueAdjustmentMagenta="0".   crs:SaturationAdjustmentRed="0".   crs:SaturationAdjustmentOrange="0".   crs:SaturationAdjustmentYellow="0".   crs:SaturationAdjustmentGreen="0".   crs:SaturationAdjustmentAqua="0".   crs:SaturationAdjustmentBlue="0".   crs:SaturationAdjustmentPurple="0".   crs:SaturationAdjustmentMagenta="0".   crs:LuminanceAdjustmentRed="0".   crs:LuminanceAdjustmentOrange="0".   crs:LuminanceAdjustmentYellow="0".   crs:LuminanceAdjustmentGreen="0".   crs:LuminanceAdjustmentAqua="0".   crs:LuminanceAdjustmentBlue="0".   crs:LuminanceAdjustmentPurple="0".   crs:LuminanceAdjustmentMagenta="0".   crs:SplitToningShadowHue="0".   crs:SplitToningShadowSaturation="0".   crs:SplitToningHighlightHue="0".   crs:SplitToningHighlightSaturation="0".   crs:SplitToningBalance="0".   crs:ParametricShadows="0".   crs:ParametricDarks="0".   crs:ParametricLights="0".   crs:ParametricHighlights="0".   crs:ParametricShadowSplit="25".   crs:ParametricMidtoneSplit="50".   crs:ParametricHighlightSplit="75".   crs:SharpenRadius="+1.0".   crs:SharpenDetail="25".   crs:SharpenEdgeMasking="0".   crs:PostCropVignetteAmount="0".   crs:GrainAmount="0".   crs:ColorNoiseReductionDetail="50".   crs:ColorNoiseReductionSmoothness="50".   crs:LensProfileEnable="0".   crs:LensManualDistortionAmount="0".   crs:PerspectiveVertical="0".   crs:PerspectiveHorizontal="0".   crs:PerspectiveRotate="0.0".   crs:PerspectiveScale="100".   crs:PerspectiveAspect="0".   crs:PerspectiveUpright="0".   crs:PerspectiveX="0.00".   crs:PerspectiveY="0.00".   crs:AutoLateralCA="0".   crs:Exposure2012="+0.20".   crs:Contrast2012="0".   crs:Highlights2012="+24".   crs:Shadows2012="-24".   crs:Whites2012="+31".   crs:Blacks2012="-10".   crs:Clarity2012="0".   crs:DefringePurpleAmount="0".   crs:DefringePurpleHueLo="30".   crs:DefringePurpleHueHi="70".   crs:DefringeGreenAmount="0".   crs:DefringeGreenHueLo="40".   crs:DefringeGreenHueHi="60".   crs:Dehaze="0".   crs:ToneMapStrength="0".   crs:ConvertToGrayscale="False".   crs:ToneCurveName="Medium Contrast".   crs:ToneCurveName2012="Linear".   crs:CameraProfile="Adobe Standard".   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975".   crs:LensProfileSetup="LensDefaults".   crs:UprightVersion="151388160".   crs:UprightCenterMode="0".   crs:UprightCenterNormX="0.5".   crs:UprightCenterNormY="0.5".   crs:UprightFocalMode="0".   crs:UprightFocalLength35mm="35".   crs:UprightPreview="False".   crs:UprightTransformCount="6".   crs:UprightFourSegmentsCount="0".   crs:HasSettings="True".   crs:CropTop="0.050467".   crs:CropLeft="0.050467".   crs:CropBottom="0.969144".   crs:CropRight="0.969144".   crs:CropAngle="0".   crs:CropConstrainToWarp="0".   crs:HasCrop="True".   crs:AlreadyApplied="False".   crs:RawFileName="dng_canon_6d.dng">.   <xmpMM:History>.    <rdf:Seq>.     <rdf:li.      stEvt:action="derived".      stEvt:parameters="converted from image/x-canon-cr2 to image/dng, saved to new location"/>.     <rdf:li.      stEvt:action="saved".      stEvt:instanceID="xmp.iid:c4db0699-4104-4f40-b561-27c7c7b028dd".      stEvt:when="2018-12-23T16:20:34-08:00".      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)".      stEvt:changed="/"/>.     <rdf:li.      stEvt:action="saved".      stEvt:instanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2".      stEvt:when="2018-12-25T16:04:27-08:00".      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)".      stEvt:changed="/metadata"/>.    </rdf:Seq>.   </xmpMM:History>.   <xmpMM:DerivedFrom.    stRef:documentID="6BF93FCB1F578C3204916BCCDEAD23D8".    stRef:originalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"/>.   <dc:subject>.    <rdf:Bag>.     <rdf:li>Jelleybean</rdf:li>.    </rdf:Bag>.   </dc:subject>.   <crs:ToneCurve>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>32, 22</rdf:li>.     <rdf:li>64, 56</rdf:li>.     <rdf:li>128, 128</rdf:li>.     <rdf:li>192, 196</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurve>.   <crs:ToneCurveRed>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveRed>.   <crs:ToneCurveGreen>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveGreen>.   <crs:ToneCurveBlue>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveBlue>.   <crs:ToneCurvePV2012>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012>.   <crs:ToneCurvePV2012Red>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Red>.   <crs:ToneCurvePV2012Green>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Green>.   <crs:ToneCurvePV2012Blue>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Blue>.   <lr:hierarchicalSubject>.    <rdf:Bag>.     <rdf:li>Jelleybean</rdf:li>.    </rdf:Bag>.   </lr:hierarchicalSubject>.  </rdf:Description>. </rdf:RDF>.</x:xmpmeta> <?xpacket end="w"?>'
xmp_data = bytes(xmp_data, 'utf-8')

updated_xmp_data = b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c128 79.159124, 2016/03/18-14:01:55        ">\n <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n  <rdf:Description rdf:about=""\n    xmlns:xmp="http://ns.adobe.com/xap/1.0/"\n    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/"\n    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"\n    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"\n    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"\n    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#"\n    xmlns:dc="http://purl.org/dc/elements/1.1/"\n    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"\n    xmlns:lr="http://ns.adobe.com/lightroom/1.0/"\n   xmp:ModifyDate="2018-12-23T16:20:34-08:00"\n   xmp:CreateDate="2017-09-07T16:01:38.03"\n   xmp:MetadataDate="2018-12-25T16:04:27-08:00"\n   xmp:Rating="3"\n   xmp:CreatorTool="Adobe Photoshop Lightroom 6.12 (Windows)"\n   aux:SerialNumber="222020003981"\n   aux:LensInfo="24/1 105/1 0/0 0/0"\n   aux:Lens="EF24-105mm f/4L IS USM"\n   aux:LensID="237"\n   aux:LensSerialNumber="0000712524"\n   aux:ImageNumber="0"\n   aux:ApproximateFocusDistance="100/100"\n   aux:FlashCompensation="0/1"\n   aux:Firmware="1.1.6"\n   photoshop:DateCreated="2017-09-07T16:01:38.03"\n   xmpMM:DocumentID="xmp.did:c4db0699-4104-4f40-b561-27c7c7b028dd"\n   xmpMM:OriginalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"\n   xmpMM:InstanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2"\n   dc:format="image/dng"\n   crs:Version="9.12"\n   crs:ProcessVersion="6.7"\n   crs:WhiteBalance="Cloudy"\n   crs:AutoWhiteVersion="134348800"\n   crs:Temperature="6500"\n   crs:Tint="+10"\n   crs:Saturation="+11"\n   crs:Sharpness="25"\n   crs:LuminanceSmoothing="0"\n   crs:ColorNoiseReduction="25"\n   crs:VignetteAmount="0"\n   crs:ShadowTint="0"\n   crs:RedHue="+4"\n   crs:RedSaturation="0"\n   crs:GreenHue="0"\n   crs:GreenSaturation="0"\n   crs:BlueHue="0"\n   crs:BlueSaturation="0"\n   crs:Vibrance="+29"\n   crs:HueAdjustmentRed="0"\n   crs:HueAdjustmentOrange="0"\n   crs:HueAdjustmentYellow="0"\n   crs:HueAdjustmentGreen="0"\n   crs:HueAdjustmentAqua="0"\n   crs:HueAdjustmentBlue="0"\n   crs:HueAdjustmentPurple="0"\n   crs:HueAdjustmentMagenta="0"\n   crs:SaturationAdjustmentRed="0"\n   crs:SaturationAdjustmentOrange="0"\n   crs:SaturationAdjustmentYellow="0"\n   crs:SaturationAdjustmentGreen="0"\n   crs:SaturationAdjustmentAqua="0"\n   crs:SaturationAdjustmentBlue="0"\n   crs:SaturationAdjustmentPurple="0"\n   crs:SaturationAdjustmentMagenta="0"\n   crs:LuminanceAdjustmentRed="0"\n   crs:LuminanceAdjustmentOrange="0"\n   crs:LuminanceAdjustmentYellow="0"\n   crs:LuminanceAdjustmentGreen="0"\n   crs:LuminanceAdjustmentAqua="0"\n   crs:LuminanceAdjustmentBlue="0"\n   crs:LuminanceAdjustmentPurple="0"\n   crs:LuminanceAdjustmentMagenta="0"\n   crs:SplitToningShadowHue="0"\n   crs:SplitToningShadowSaturation="0"\n   crs:SplitToningHighlightHue="0"\n   crs:SplitToningHighlightSaturation="0"\n   crs:SplitToningBalance="0"\n   crs:ParametricShadows="0"\n   crs:ParametricDarks="0"\n   crs:ParametricLights="0"\n   crs:ParametricHighlights="0"\n   crs:ParametricShadowSplit="25"\n   crs:ParametricMidtoneSplit="50"\n   crs:ParametricHighlightSplit="75"\n   crs:SharpenRadius="+1.0"\n   crs:SharpenDetail="25"\n   crs:SharpenEdgeMasking="0"\n   crs:PostCropVignetteAmount="0"\n   crs:GrainAmount="0"\n   crs:ColorNoiseReductionDetail="50"\n   crs:ColorNoiseReductionSmoothness="50"\n   crs:LensProfileEnable="0"\n   crs:LensManualDistortionAmount="0"\n   crs:PerspectiveVertical="0"\n   crs:PerspectiveHorizontal="0"\n   crs:PerspectiveRotate="0.0"\n   crs:PerspectiveScale="100"\n   crs:PerspectiveAspect="0"\n   crs:PerspectiveUpright="0"\n   crs:PerspectiveX="0.00"\n   crs:PerspectiveY="0.00"\n   crs:AutoLateralCA="0"\n   crs:Exposure2012="+0.4"\n   crs:Contrast2012="0"\n   crs:Highlights2012="+24"\n   crs:Shadows2012="-28"\n   crs:Whites2012="+31"\n   crs:Blacks2012="-10"\n   crs:Clarity2012="0"\n   crs:DefringePurpleAmount="0"\n   crs:DefringePurpleHueLo="30"\n   crs:DefringePurpleHueHi="70"\n   crs:DefringeGreenAmount="0"\n   crs:DefringeGreenHueLo="40"\n   crs:DefringeGreenHueHi="60"\n   crs:Dehaze="0"\n   crs:ToneMapStrength="0"\n   crs:ConvertToGrayscale="False"\n   crs:ToneCurveName="Medium Contrast"\n   crs:ToneCurveName2012="Linear"\n   crs:CameraProfile="Adobe Standard"\n   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975"\n   crs:LensProfileSetup="LensDefaults"\n   crs:UprightVersion="151388160"\n   crs:UprightCenterMode="0"\n   crs:UprightCenterNormX="0.5"\n   crs:UprightCenterNormY="0.5"\n   crs:UprightFocalMode="0"\n   crs:UprightFocalLength35mm="35"\n   crs:UprightPreview="False"\n   crs:UprightTransformCount="6"\n   crs:UprightFourSegmentsCount="0"\n   crs:HasSettings="True"\n   crs:CropTop="0.06"\n   crs:CropLeft="0.050467"\n   crs:CropBottom="0.969144"\n   crs:CropRight="0.969144"\n   crs:CropAngle="0"\n   crs:CropConstrainToWarp="0"\n   crs:HasCrop="True"\n   crs:AlreadyApplied="False"\n   crs:RawFileName="test_image_canon_6d.dng">\n   <xmpMM:History>\n    <rdf:Seq>\n     <rdf:li\n      stEvt:action="derived"\n      stEvt:parameters="converted from image/x-canon-cr2 to image/dng, saved to new location"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:c4db0699-4104-4f40-b561-27c7c7b028dd"\n      stEvt:when="2018-12-23T16:20:34-08:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)"\n      stEvt:changed="/"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2"\n      stEvt:when="2018-12-25T16:04:27-08:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)"\n      stEvt:changed="/metadata"/>\n    </rdf:Seq>\n   </xmpMM:History>\n   <xmpMM:DerivedFrom\n    stRef:documentID="6BF93FCB1F578C3204916BCCDEAD23D8"\n    stRef:originalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"/>\n   <dc:subject>\n    <rdf:Bag>\n     <rdf:li>Jelleybean</rdf:li>\n    </rdf:Bag>\n   </dc:subject>\n   <crs:ToneCurve>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>32, 22</rdf:li>\n     <rdf:li>64, 56</rdf:li>\n     <rdf:li>128, 128</rdf:li>\n     <rdf:li>192, 196</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurve>\n   <crs:ToneCurveRed>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveRed>\n   <crs:ToneCurveGreen>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveGreen>\n   <crs:ToneCurveBlue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveBlue>\n   <crs:ToneCurvePV2012>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012>\n   <crs:ToneCurvePV2012Red>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Red>\n   <crs:ToneCurvePV2012Green>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Green>\n   <crs:ToneCurvePV2012Blue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Blue>\n   <lr:hierarchicalSubject>\n    <rdf:Bag>\n     <rdf:li>Jelleybean</rdf:li>\n    </rdf:Bag>\n   </lr:hierarchicalSubject>\n  </rdf:Description>\n </rdf:RDF>\n</x:xmpmeta>\n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                             \n<?xpacket end="w"?>'

xmp_to_try = ((b'xmp:Rating', '2'),
              (b'crs:Saturation', '+9'),
              (b'crs:Exposure2012', '+0.20'),
              (b'crs:Shadows2012', '-24'),
              (b'crs:RedHue', '0'),
              (b'crs:CropTop', '0.050467'),
              (b'hello', None),
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

new_xmp_values = {b'xmp:Rating': 3,
                  b'crs:Saturation': '+11',
                  b'crs:Exposure2012': '+0.40',
                  b'crs:Shadows2012': '-28',
                  b'crs:RedHue': '4',
                  b'crs:CropTop': 0.06,
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
               b'crs:CropTop': 0.06, b'xmp:Rating': 3, b'crs:Exposure2012': '+0.40'}

xmp_to_be_stored = {b'crs:Temperature': {'val': 6500.0, 'updated': False}, b'crs:Tint': {'val': 10.0, 'updated': False},
                    b'crs:Saturation': {'val': '+11', 'updated': True},
                    b'crs:Vibrance': {'val': 29.0, 'updated': False}, b'crs:Sharpness': {'val': 25.0, 'updated': False},
                    b'crs:ShadowTint': {'val': 0.0, 'updated': False}, b'crs:RedHue': {'val': '4', 'updated': True},
                    b'crs:RedSaturation': {'val': 0.0, 'updated': False},
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
                    b'crs:CropTop': {'val': 0.06, 'updated': True}, b'xmp:Rating': {'val': 3, 'updated': True},
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

used_fields_raw = {'bits_per_sample': [16],
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

used_fields_thumbnail = {'bits_per_sample': [8, 8, 8], 'strip_offsets': [208602], 'strip_byte_counts': [140544],
                         'sub_ifds': [202942, 206072, 206470, 207058, 207550], 'image_width': 256, 'image_length': 183,
                         'compression': 1, 'photometric_interpretation': 2, 'orientation': 1, 'samples_per_pix': 3,
                         'rows_per_strip': 183, 'planar_configuration': 1,
                         'xmp': b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c128 79.159124, 2016/03/18-14:01:55        ">\n <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n  <rdf:Description rdf:about=""\n    xmlns:xmp="http://ns.adobe.com/xap/1.0/"\n    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/"\n    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"\n    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"\n    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"\n    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#"\n    xmlns:dc="http://purl.org/dc/elements/1.1/"\n    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"\n    xmlns:lr="http://ns.adobe.com/lightroom/1.0/"\n   xmp:ModifyDate="2018-12-23T16:20:34-08:00"\n   xmp:CreateDate="2017-09-07T16:01:38.03"\n   xmp:MetadataDate="2018-12-25T16:04:27-08:00"\n   xmp:Rating="2"\n   xmp:CreatorTool="Adobe Photoshop Lightroom 6.12 (Windows)"\n   aux:SerialNumber="222020003981"\n   aux:LensInfo="24/1 105/1 0/0 0/0"\n   aux:Lens="EF24-105mm f/4L IS USM"\n   aux:LensID="237"\n   aux:LensSerialNumber="0000712524"\n   aux:ImageNumber="0"\n   aux:ApproximateFocusDistance="100/100"\n   aux:FlashCompensation="0/1"\n   aux:Firmware="1.1.6"\n   photoshop:DateCreated="2017-09-07T16:01:38.03"\n   xmpMM:DocumentID="xmp.did:c4db0699-4104-4f40-b561-27c7c7b028dd"\n   xmpMM:OriginalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"\n   xmpMM:InstanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2"\n   dc:format="image/dng"\n   crs:Version="9.12"\n   crs:ProcessVersion="6.7"\n   crs:WhiteBalance="Cloudy"\n   crs:AutoWhiteVersion="134348800"\n   crs:Temperature="6500"\n   crs:Tint="+10"\n   crs:Saturation="+9"\n   crs:Sharpness="25"\n   crs:LuminanceSmoothing="0"\n   crs:ColorNoiseReduction="25"\n   crs:VignetteAmount="0"\n   crs:ShadowTint="0"\n   crs:RedHue="0"\n   crs:RedSaturation="0"\n   crs:GreenHue="0"\n   crs:GreenSaturation="0"\n   crs:BlueHue="0"\n   crs:BlueSaturation="0"\n   crs:Vibrance="+29"\n   crs:HueAdjustmentRed="0"\n   crs:HueAdjustmentOrange="0"\n   crs:HueAdjustmentYellow="0"\n   crs:HueAdjustmentGreen="0"\n   crs:HueAdjustmentAqua="0"\n   crs:HueAdjustmentBlue="0"\n   crs:HueAdjustmentPurple="0"\n   crs:HueAdjustmentMagenta="0"\n   crs:SaturationAdjustmentRed="0"\n   crs:SaturationAdjustmentOrange="0"\n   crs:SaturationAdjustmentYellow="0"\n   crs:SaturationAdjustmentGreen="0"\n   crs:SaturationAdjustmentAqua="0"\n   crs:SaturationAdjustmentBlue="0"\n   crs:SaturationAdjustmentPurple="0"\n   crs:SaturationAdjustmentMagenta="0"\n   crs:LuminanceAdjustmentRed="0"\n   crs:LuminanceAdjustmentOrange="0"\n   crs:LuminanceAdjustmentYellow="0"\n   crs:LuminanceAdjustmentGreen="0"\n   crs:LuminanceAdjustmentAqua="0"\n   crs:LuminanceAdjustmentBlue="0"\n   crs:LuminanceAdjustmentPurple="0"\n   crs:LuminanceAdjustmentMagenta="0"\n   crs:SplitToningShadowHue="0"\n   crs:SplitToningShadowSaturation="0"\n   crs:SplitToningHighlightHue="0"\n   crs:SplitToningHighlightSaturation="0"\n   crs:SplitToningBalance="0"\n   crs:ParametricShadows="0"\n   crs:ParametricDarks="0"\n   crs:ParametricLights="0"\n   crs:ParametricHighlights="0"\n   crs:ParametricShadowSplit="25"\n   crs:ParametricMidtoneSplit="50"\n   crs:ParametricHighlightSplit="75"\n   crs:SharpenRadius="+1.0"\n   crs:SharpenDetail="25"\n   crs:SharpenEdgeMasking="0"\n   crs:PostCropVignetteAmount="0"\n   crs:GrainAmount="0"\n   crs:ColorNoiseReductionDetail="50"\n   crs:ColorNoiseReductionSmoothness="50"\n   crs:LensProfileEnable="0"\n   crs:LensManualDistortionAmount="0"\n   crs:PerspectiveVertical="0"\n   crs:PerspectiveHorizontal="0"\n   crs:PerspectiveRotate="0.0"\n   crs:PerspectiveScale="100"\n   crs:PerspectiveAspect="0"\n   crs:PerspectiveUpright="0"\n   crs:PerspectiveX="0.00"\n   crs:PerspectiveY="0.00"\n   crs:AutoLateralCA="0"\n   crs:Exposure2012="+0.20"\n   crs:Contrast2012="0"\n   crs:Highlights2012="+24"\n   crs:Shadows2012="-24"\n   crs:Whites2012="+31"\n   crs:Blacks2012="-10"\n   crs:Clarity2012="0"\n   crs:DefringePurpleAmount="0"\n   crs:DefringePurpleHueLo="30"\n   crs:DefringePurpleHueHi="70"\n   crs:DefringeGreenAmount="0"\n   crs:DefringeGreenHueLo="40"\n   crs:DefringeGreenHueHi="60"\n   crs:Dehaze="0"\n   crs:ToneMapStrength="0"\n   crs:ConvertToGrayscale="False"\n   crs:ToneCurveName="Medium Contrast"\n   crs:ToneCurveName2012="Linear"\n   crs:CameraProfile="Adobe Standard"\n   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975"\n   crs:LensProfileSetup="LensDefaults"\n   crs:UprightVersion="151388160"\n   crs:UprightCenterMode="0"\n   crs:UprightCenterNormX="0.5"\n   crs:UprightCenterNormY="0.5"\n   crs:UprightFocalMode="0"\n   crs:UprightFocalLength35mm="35"\n   crs:UprightPreview="False"\n   crs:UprightTransformCount="6"\n   crs:UprightFourSegmentsCount="0"\n   crs:HasSettings="True"\n   crs:CropTop="0.050467"\n   crs:CropLeft="0.050467"\n   crs:CropBottom="0.969144"\n   crs:CropRight="0.969144"\n   crs:CropAngle="0"\n   crs:CropConstrainToWarp="0"\n   crs:HasCrop="True"\n   crs:AlreadyApplied="False"\n   crs:RawFileName="test_image_canon_6d.dng">\n   <xmpMM:History>\n    <rdf:Seq>\n     <rdf:li\n      stEvt:action="derived"\n      stEvt:parameters="converted from image/x-canon-cr2 to image/dng, saved to new location"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:c4db0699-4104-4f40-b561-27c7c7b028dd"\n      stEvt:when="2018-12-23T16:20:34-08:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)"\n      stEvt:changed="/"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2"\n      stEvt:when="2018-12-25T16:04:27-08:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)"\n      stEvt:changed="/metadata"/>\n    </rdf:Seq>\n   </xmpMM:History>\n   <xmpMM:DerivedFrom\n    stRef:documentID="6BF93FCB1F578C3204916BCCDEAD23D8"\n    stRef:originalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"/>\n   <dc:subject>\n    <rdf:Bag>\n     <rdf:li>Jelleybean</rdf:li>\n    </rdf:Bag>\n   </dc:subject>\n   <crs:ToneCurve>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>32, 22</rdf:li>\n     <rdf:li>64, 56</rdf:li>\n     <rdf:li>128, 128</rdf:li>\n     <rdf:li>192, 196</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurve>\n   <crs:ToneCurveRed>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveRed>\n   <crs:ToneCurveGreen>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveGreen>\n   <crs:ToneCurveBlue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveBlue>\n   <crs:ToneCurvePV2012>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012>\n   <crs:ToneCurvePV2012Red>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Red>\n   <crs:ToneCurvePV2012Green>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Green>\n   <crs:ToneCurvePV2012Blue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Blue>\n   <lr:hierarchicalSubject>\n    <rdf:Bag>\n     <rdf:li>Jelleybean</rdf:li>\n    </rdf:Bag>\n   </lr:hierarchicalSubject>\n  </rdf:Description>\n </rdf:RDF>\n</x:xmpmeta>\n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                             \n<?xpacket end="w"?>'}

ifds = '{202942: {254: 254, 4, 1, 0, 256: 256, 4, 1, 5568, 257: 257, 4, 1, 3708, 258: 258, 3, 1, 16, 259: 259, 3, 1, 7, 262: 262, 3, 1, 32803, 277: 277, 3, 1, 1, 284: 284, 3, 1, 1, 322: 322, 4, 1, 256, 323: 323, 4, 1, 256, 324: 324, 4, 330, 203272, 325: 325, 4, 330, 204592, 33421: 33421, 3, 2, 131074, 33422: 33422, 1, 4, 33620224, 50710: 50710, 1, 3, 131328, 50711: 50711, 3, 1, 1, 50713: 50713, 3, 2, 131074, 50714: 50714, 5, 4, 205912, 50717: 50717, 3, 1, 15000, 50718: 50718, 5, 2, 205944, 50719: 50719, 5, 2, 205960, 50720: 50720, 5, 2, 205976, 50733: 50733, 4, 1, 250, 50738: 50738, 5, 1, 205992, 50780: 50780, 5, 1, 206000, 50829: 50829, 4, 4, 206008, 51041: 51041, 12, 6, 206024}, 206072: {254: 254, 4, 1, 1, 256: 256, 4, 1, 1024, 257: 257, 4, 1, 731, 258: 258, 3, 3, 206318, 259: 259, 3, 1, 7, 262: 262, 3, 1, 6, 273: 273, 4, 1, 349146, 277: 277, 3, 1, 3, 278: 278, 4, 1, 731, 279: 279, 4, 1, 64473, 284: 284, 3, 1, 1, 529: 529, 5, 3, 206324, 530: 530, 3, 2, 131074, 531: 531, 3, 1, 2, 532: 532, 5, 6, 206348, 50966: 50966, 2, 26, 206396, 50967: 50967, 2, 5, 206422, 50969: 50969, 1, 16, 206428, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 206444}, 206470: {254: 254, 4, 1, 1, 256: 256, 4, 1, 2048, 257: 257, 4, 1, 1365, 258: 258, 3, 3, 206668, 259: 259, 3, 1, 34892, 262: 262, 3, 1, 34892, 277: 277, 3, 1, 3, 284: 284, 3, 1, 1, 322: 322, 4, 1, 512, 323: 323, 4, 1, 464, 324: 324, 4, 12, 206674, 325: 325, 4, 12, 206722, 50966: 50966, 2, 26, 206770, 50967: 50967, 2, 5, 206796, 51009: 51009, 7, 256, 206802, 51114: 51114, 4, 1, 256}, 207058: {254: 254, 4, 1, 1, 256: 256, 4, 1, 512, 257: 257, 4, 1, 341, 258: 258, 3, 3, 207256, 259: 259, 3, 1, 34892, 262: 262, 3, 1, 34892, 277: 277, 3, 1, 3, 284: 284, 3, 1, 1, 322: 322, 4, 1, 512, 323: 323, 4, 1, 352, 324: 324, 4, 1, 783778, 325: 325, 4, 1, 35886, 50966: 50966, 2, 26, 207262, 50967: 50967, 2, 5, 207288, 51009: 51009, 7, 256, 207294, 51114: 51114, 4, 1, 256}, 207550: {254: 254, 4, 1, 1, 256: 256, 4, 1, 256, 257: 257, 4, 1, 171, 258: 258, 3, 3, 207748, 259: 259, 3, 1, 34892, 262: 262, 3, 1, 34892, 277: 277, 3, 1, 3, 284: 284, 3, 1, 1, 322: 322, 4, 1, 256, 323: 323, 4, 1, 176, 324: 324, 4, 1, 819664, 325: 325, 4, 1, 11761, 50966: 50966, 2, 26, 207754, 50967: 50967, 2, 5, 207780, 51009: 51009, 7, 256, 207786, 51114: 51114, 4, 1, 256}, 208042: {33434: 33434, 5, 1, 208408, 33437: 33437, 5, 1, 208416, 34850: 34850, 3, 1, 3, 34855: 34855, 3, 1, 400, 34864: 34864, 3, 1, 2, 34866: 34866, 4, 1, 400, 36864: 36864, 7, 4, 808661552, 36867: 36867, 2, 20, 208424, 36868: 36868, 2, 20, 208444, 37377: 37377, 10, 1, 208464, 37378: 37378, 5, 1, 208472, 37380: 37380, 10, 1, 208480, 37381: 37381, 5, 1, 208488, 37383: 37383, 3, 1, 5, 37385: 37385, 3, 1, 16, 37386: 37386, 5, 1, 208496, 37521: 37521, 2, 3, 13104, 37522: 37522, 2, 3, 13104, 40961: 40961, 3, 1, 65535, 41486: 41486, 5, 1, 208504, 41487: 41487, 5, 1, 208512, 41488: 41488, 3, 1, 3, 41985: 41985, 3, 1, 0, 41986: 41986, 3, 1, 0, 41987: 41987, 3, 1, 1, 41990: 41990, 3, 1, 0, 42033: 42033, 2, 13, 208520, 42034: 42034, 5, 4, 208534, 42036: 42036, 2, 23, 208566, 42037: 42037, 2, 11, 208590}, 8: {254: 254, 4, 1, 1, 256: 256, 4, 1, 256, 257: 257, 4, 1, 183, 258: 258, 3, 3, 734, 259: 259, 3, 1, 1, 262: 262, 3, 1, 2, 271: 271, 2, 6, 740, 272: 272, 2, 13, 746, 273: 273, 4, 1, 208602, 274: 274, 3, 1, 1, 277: 277, 3, 1, 3, 278: 278, 4, 1, 183, 279: 279, 4, 1, 140544, 284: 284, 3, 1, 1, 305: 305, 2, 41, 760, 306: 306, 2, 20, 802, 330: 330, 4, 5, 822, 700: 700, 1, 12904, 842, 34665: 34665, 4, 1, 208042, 37393: 37393, 4, 1, 0, 50706: 50706, 1, 4, 1025, 50707: 50707, 1, 4, 257, 50708: 50708, 2, 13, 13746, 50721: 50721, 10, 9, 13760, 50722: 50722, 10, 9, 13832, 50723: 50723, 10, 9, 13904, 50724: 50724, 10, 9, 13976, 50727: 50727, 5, 3, 14048, 50728: 50728, 5, 3, 14072, 50730: 50730, 10, 1, 14096, 50731: 50731, 5, 1, 14104, 50732: 50732, 5, 1, 14112, 50734: 50734, 5, 1, 14120, 50735: 50735, 2, 13, 14128, 50736: 50736, 5, 4, 14142, 50739: 50739, 5, 1, 14174, 50740: 50740, 1, 68256, 14182, 50778: 50778, 3, 1, 17, 50779: 50779, 3, 1, 21, 50781: 50781, 1, 16, 82438, 50827: 50827, 2, 13, 82454, 50931: 50931, 2, 10, 82468, 50932: 50932, 2, 10, 82478, 50936: 50936, 2, 15, 82488, 50937: 50937, 4, 3, 82504, 50938: 50938, 11, 8100, 82516, 50939: 50939, 11, 8100, 114916, 50941: 50941, 4, 1, 0, 50942: 50942, 2, 35, 147316, 50964: 50964, 10, 9, 147352, 50965: 50965, 10, 9, 147424, 50966: 50966, 2, 26, 147496, 50967: 50967, 2, 5, 147522, 50969: 50969, 1, 16, 147528, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 147544, 50972: 50972, 1, 16, 147570, 50981: 50981, 4, 3, 147586, 50982: 50982, 11, 13824, 147598, 51041: 51041, 12, 6, 202894}}'

saved_ifds = '{141384: {254: 254, 4, 1, 0, 256: 256, 4, 1, 5568, 257: 257, 4, 1, 3708, 258: 258, 3, 1, 16, 259: 259, 3, 1, 7, 262: 262, 3, 1, 32803, 277: 277, 3, 1, 1, 284: 284, 3, 1, 1, 322: 322, 4, 1, 256, 323: 323, 4, 1, 256, 324: 324, 4, 330, 141714, 325: 325, 4, 330, 17847488, 33421: 33421, 3, 2, 131074, 33422: 33422, 1, 4, 33620224, 50710: 50710, 1, 3, 131328, 50711: 50711, 3, 1, 1, 50713: 50713, 3, 2, 131074, 50714: 50714, 5, 4, 17848808, 50717: 50717, 3, 1, 15000, 50718: 50718, 5, 2, 17848840, 50719: 50719, 5, 2, 17848856, 50720: 50720, 5, 2, 17848872, 50733: 50733, 4, 1, 250, 50738: 50738, 5, 1, 17848888, 50780: 50780, 5, 1, 17848896, 50829: 50829, 4, 4, 17848904, 51041: 51041, 12, 6, 17848920}, 17848968: {254: 254, 4, 1, 1, 256: 256, 4, 1, 1024, 257: 257, 4, 1, 731, 258: 258, 3, 3, 17849214, 259: 259, 3, 1, 7, 262: 262, 3, 1, 6, 273: 273, 4, 1, 17849220, 277: 277, 3, 1, 3, 278: 278, 4, 1, 731, 279: 279, 4, 1, 64473, 284: 284, 3, 1, 1, 529: 529, 5, 3, 17913693, 530: 530, 3, 2, 131074, 531: 531, 3, 1, 2, 532: 532, 5, 6, 17913717, 50966: 50966, 2, 26, 17913765, 50967: 50967, 2, 5, 17913791, 50969: 50969, 1, 16, 17913796, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 17913812}, 17913838: {254: 254, 4, 1, 1, 256: 256, 4, 1, 2048, 257: 257, 4, 1, 1365, 258: 258, 3, 3, 17914036, 259: 259, 3, 1, 34892, 262: 262, 3, 1, 34892, 277: 277, 3, 1, 3, 284: 284, 3, 1, 1, 322: 322, 4, 1, 512, 323: 323, 4, 1, 464, 324: 324, 4, 12, 17914042, 325: 325, 4, 12, 18284243, 50966: 50966, 2, 26, 18284291, 50967: 50967, 2, 5, 18284317, 51009: 51009, 7, 256, 18284322, 51114: 51114, 4, 1, 256}, 18284578: {254: 254, 4, 1, 1, 256: 256, 4, 1, 512, 257: 257, 4, 1, 341, 258: 258, 3, 3, 18284776, 259: 259, 3, 1, 34892, 262: 262, 3, 1, 34892, 277: 277, 3, 1, 3, 284: 284, 3, 1, 1, 322: 322, 4, 1, 512, 323: 323, 4, 1, 352, 324: 324, 4, 1, 18284782, 325: 325, 4, 1, 35886, 50966: 50966, 2, 26, 18320668, 50967: 50967, 2, 5, 18320694, 51009: 51009, 7, 256, 18320699, 51114: 51114, 4, 1, 256}, 18320955: {254: 254, 4, 1, 1, 256: 256, 4, 1, 256, 257: 257, 4, 1, 171, 258: 258, 3, 3, 18321153, 259: 259, 3, 1, 34892, 262: 262, 3, 1, 34892, 277: 277, 3, 1, 3, 284: 284, 3, 1, 1, 322: 322, 4, 1, 256, 323: 323, 4, 1, 176, 324: 324, 4, 1, 18321159, 325: 325, 4, 1, 11761, 50966: 50966, 2, 26, 18332920, 50967: 50967, 2, 5, 18332946, 51009: 51009, 7, 256, 18332951, 51114: 51114, 4, 1, 256}, 18346112: {33434: 33434, 5, 1, 18346478, 33437: 33437, 5, 1, 18346486, 34850: 34850, 3, 1, 3, 34855: 34855, 3, 1, 400, 34864: 34864, 3, 1, 2, 34866: 34866, 4, 1, 400, 36864: 36864, 7, 4, 808661552, 36867: 36867, 2, 20, 18346494, 36868: 36868, 2, 20, 18346514, 37377: 37377, 10, 1, 18346534, 37378: 37378, 5, 1, 18346542, 37380: 37380, 10, 1, 18346550, 37381: 37381, 5, 1, 18346558, 37383: 37383, 3, 1, 5, 37385: 37385, 3, 1, 16, 37386: 37386, 5, 1, 18346566, 37521: 37521, 2, 3, 13104, 37522: 37522, 2, 3, 13104, 40961: 40961, 3, 1, 65535, 41486: 41486, 5, 1, 18346574, 41487: 41487, 5, 1, 18346582, 41488: 41488, 3, 1, 3, 41985: 41985, 3, 1, 0, 41986: 41986, 3, 1, 0, 41987: 41987, 3, 1, 1, 41990: 41990, 3, 1, 0, 42033: 42033, 2, 13, 18346590, 42034: 42034, 5, 4, 18346603, 42036: 42036, 2, 23, 18346635, 42037: 42037, 2, 11, 18346658}, 8: {254: 254, 4, 1, 1, 256: 256, 4, 1, 256, 257: 257, 4, 1, 183, 258: 258, 3, 3, 734, 259: 259, 3, 1, 1, 262: 262, 3, 1, 2, 271: 271, 2, 6, 740, 272: 272, 2, 13, 746, 273: 273, 4, 1, 759, 274: 274, 3, 1, 1, 277: 277, 3, 1, 3, 278: 278, 4, 1, 183, 279: 279, 4, 1, 140544, 284: 284, 3, 1, 1, 305: 305, 2, 41, 141303, 306: 306, 2, 20, 141344, 330: 330, 4, 5, 141364, 700: 700, 1, 12904, 18333207, 34665: 34665, 4, 1, 18346112, 37393: 37393, 4, 1, 0, 50706: 50706, 1, 4, 1025, 50707: 50707, 1, 4, 257, 50708: 50708, 2, 13, 18346669, 50721: 50721, 10, 9, 18346682, 50722: 50722, 10, 9, 18346754, 50723: 50723, 10, 9, 18346826, 50724: 50724, 10, 9, 18346898, 50727: 50727, 5, 3, 18346970, 50728: 50728, 5, 3, 18346994, 50730: 50730, 10, 1, 18347018, 50731: 50731, 5, 1, 18347026, 50732: 50732, 5, 1, 18347034, 50734: 50734, 5, 1, 18347042, 50735: 50735, 2, 13, 18347050, 50736: 50736, 5, 4, 18347063, 50739: 50739, 5, 1, 18347095, 50740: 50740, 1, 68256, 18347103, 50778: 50778, 3, 1, 17, 50779: 50779, 3, 1, 21, 50781: 50781, 1, 16, 18415359, 50827: 50827, 2, 13, 18415375, 50931: 50931, 2, 10, 18415388, 50932: 50932, 2, 10, 18415398, 50936: 50936, 2, 15, 18415408, 50937: 50937, 4, 3, 18415423, 50938: 50938, 11, 8100, 18415435, 50939: 50939, 11, 8100, 18447835, 50941: 50941, 4, 1, 0, 50942: 50942, 2, 35, 18480235, 50964: 50964, 10, 9, 18480270, 50965: 50965, 10, 9, 18480342, 50966: 50966, 2, 26, 18480414, 50967: 50967, 2, 5, 18480440, 50969: 50969, 1, 16, 18480445, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 18480461, 50972: 50972, 1, 16, 18480487, 50981: 50981, 4, 3, 18480503, 50982: 50982, 11, 13824, 18480515, 51041: 51041, 12, 6, 18535811}}'

scaled_raw_image = [[0.891, 0.701, 0.739, 0.552, 0.604, 0.508, 0.821, 0.932, 0.04, 0.406, 0.359, 0.537, 0.196],
                    [0.826, 0.209, 0.452, 0.806, 0.54, 0.584, 0.424, 0.311, 0.954, 0.516, 0.229, 0.061, 0.433],
                    [0.624, 0.706, 0.202, 0.214, 0.535, 0.983, 0.024, 0.222, 0.561, 0.617, 0.373, 0.689, 0.469],
                    [0.827, 0.115, 0.316, 0.47, 0.401, 0.381, 0.195, 0.168, 0.465, 0.279, 0.105, 0.963, 0.932],
                    [0.199, 0.727, 0.514, 0.798, 0.467, 0.754, 0.646, 0.902, 0.284, 0.629, 0.507, 0.754, 0.602],
                    [0.062, 0.04, 0.646, 0.727, 0.816, 0.971, 0.797, 0.727, 0.77, 0.158, 0.939, 0.167, 0.168],
                    [0.715, 0.147, 0.625, 0.207, 0.552, 0.665, 0.008, 0.334, 0.951, 0.04, 0.406, 0.755, 0.563],
                    [0.56, 0.737, 0.344, 0.188, 0.717, 0.294, 0.008, 0.263, 0.106, 0.021, 0.908, 0.096, 0.48],
                    [0.517, 0.227, 0.308, 0.434, 0.614, 0.521, 0.123, 0.71, 0.724, 0.801, 0.893, 0.095, 0.949],
                    [0.791, 0.729, 0.701, 0.122, 0.999, 0.066, 0.546, 0.791, 0.362, 0.374, 0.08, 0.944, 0.544],
                    [0.507, 0.591, 0.154, 0.063, 0.342, 0.954, 0.398, 0.664, 0.502, 0.937, 0.858, 0.741, 0.03]]

unscaled_raw_image = [[[11627, 10188, 6201, 4102, 2952, 10260, 5174, 8853, 12169, 2681, 6603, 7360, 9013],
                       [3925, 3766, 9570, 11293, 4413, 11894, 9966, 6103, 10290, 6256, 4810, 6173, 12387],
                       [4597, 3346, 4884, 8722, 10608, 6491, 2706, 5412, 11331, 11687, 4488, 11610, 3872],
                       [9536, 8289, 11363, 4758, 3557, 11400, 4374, 4310, 7689, 10287, 10567, 8214, 6871],
                       [11377, 5300, 4822, 6518, 10022, 6405, 8819, 4732, 7461, 11750, 7302, 5155, 10361],
                       [6899, 5008, 6605, 2976, 4626, 11582, 10479, 4856, 8668, 7969, 7681, 5987, 10430],
                       [3769, 12228, 8179, 7339, 7533, 9285, 5901, 10224, 3645, 11380, 9306, 6363, 5111],
                       [7193, 11651, 9724, 2789, 6175, 11365, 6745, 9321, 10820, 10965, 3569, 5556, 4693],
                       [10920, 5870, 9036, 5517, 11533, 4130, 5341, 10943, 4795, 5165, 9778, 9954, 2875],
                       [5811, 10912, 6179, 3439, 4696, 8290, 4591, 11143, 7939, 6514, 5222, 3644, 2884],
                       [6699, 4230, 10386, 9713, 7563, 4266, 6164, 12018, 10039, 4478, 11432, 11847, 5929]],
                      [[11627, 10188, 6201, 4102, 2952, 10260, 5174, 8853, 12169, 2681, 6603, 7360, 9013],
                       [3925, 3766, 9570, 11293, 4413, 11894, 9966, 6103, 10290, 6256, 4810, 6173, 12387],
                       [4597, 3346, 4884, 8722, 10608, 6491, 2706, 5412, 11331, 11687, 4488, 11610, 3872],
                       [9536, 8289, 11363, 4758, 3557, 11400, 4374, 4310, 7689, 10287, 10567, 8214, 6871],
                       [11377, 5300, 4822, 6518, 10022, 6405, 8819, 4732, 7461, 11750, 7302, 5155, 10361],
                       [6899, 5008, 6605, 2976, 4626, 11582, 10479, 4856, 8668, 7969, 7681, 5987, 10430],
                       [3769, 12228, 8179, 7339, 7533, 9285, 5901, 10224, 3645, 11380, 9306, 6363, 5111],
                       [7193, 11651, 9724, 2789, 6175, 11365, 6745, 9321, 10820, 10965, 3569, 5556, 4693],
                       [10920, 5870, 9036, 5517, 11533, 4130, 5341, 10943, 4795, 5165, 9778, 9954, 2875],
                       [5811, 10912, 6179, 3439, 4696, 8290, 4591, 11143, 7939, 6514, 5222, 3644, 2884],
                       [6699, 4230, 10386, 9713, 7563, 4266, 6164, 12018, 10039, 4478, 11432, 11847, 5929]],
                      [[11627, 10188, 6201, 4102, 2952, 10260, 5174, 8853, 12169, 2681, 6603, 7360, 9013],
                       [3925, 3766, 9570, 11293, 4413, 11894, 9966, 6103, 10290, 6256, 4810, 6173, 12387],
                       [4597, 3346, 4884, 8722, 10608, 6491, 2706, 5412, 11331, 11687, 4488, 11610, 3872],
                       [9536, 8289, 11363, 4758, 3557, 11400, 4374, 4310, 7689, 10287, 10567, 8214, 6871],
                       [11377, 5300, 4822, 6518, 10022, 6405, 8819, 4732, 7461, 11750, 7302, 5155, 10361],
                       [6899, 5008, 6605, 2976, 4626, 11582, 10479, 4856, 8668, 7969, 7681, 5987, 10430],
                       [3769, 12228, 8179, 7339, 7533, 9285, 5901, 10224, 3645, 11380, 9306, 6363, 5111],
                       [7193, 11651, 9724, 2789, 6175, 11365, 6745, 9321, 10820, 10965, 3569, 5556, 4693],
                       [10920, 5870, 9036, 5517, 11533, 4130, 5341, 10943, 4795, 5165, 9778, 9954, 2875],
                       [5811, 10912, 6179, 3439, 4696, 8290, 4591, 11143, 7939, 6514, 5222, 3644, 2884],
                       [6699, 4230, 10386, 9713, 7563, 4266, 6164, 12018, 10039, 4478, 11432, 11847, 5929]]]

unlinearized_raw_image = [[[1, 6, 14, 12, 10, 3, 13, 5, 8, 7, 8, 12, 3],
                           [11, 2, 11, 7, 4, 13, 1, 10, 12, 3, 0, 8, 5],
                           [7, 4, 5, 9, 12, 5, 2, 10, 4, 2, 12, 3, 15],
                           [8, 5, 0, 12, 0, 3, 8, 5, 11, 6, 11, 15, 6],
                           [12, 6, 12, 5, 5, 2, 11, 3, 3, 10, 14, 10, 1],
                           [1, 11, 14, 0, 7, 7, 7, 5, 11, 8, 10, 14, 0],
                           [6, 15, 5, 6, 0, 0, 8, 12, 6, 5, 1, 8, 13],
                           [9, 7, 2, 13, 5, 9, 15, 3, 0, 2, 1, 13, 7],
                           [14, 7, 9, 8, 12, 10, 0, 8, 10, 11, 2, 4, 11],
                           [5, 5, 5, 1, 4, 6, 4, 13, 6, 4, 3, 2, 12],
                           [14, 11, 3, 14, 8, 5, 11, 15, 14, 12, 7, 1, 0]],
                          [[7, 1, 2, 13, 10, 12, 8, 1, 11, 11, 11, 10, 12],
                           [12, 1, 12, 7, 9, 3, 1, 1, 14, 13, 8, 13, 0],
                           [13, 5, 1, 4, 15, 6, 12, 10, 15, 5, 10, 10, 7],
                           [6, 9, 14, 5, 4, 0, 9, 6, 15, 5, 9, 8, 2],
                           [13, 7, 3, 8, 10, 0, 15, 2, 15, 14, 9, 14, 0],
                           [15, 3, 12, 3, 6, 12, 10, 12, 9, 14, 0, 4, 12],
                           [0, 11, 12, 10, 3, 2, 13, 5, 10, 8, 5, 11, 14],
                           [0, 3, 11, 2, 1, 10, 0, 11, 13, 4, 13, 8, 6],
                           [5, 5, 11, 4, 4, 9, 4, 15, 11, 3, 3, 6, 14],
                           [4, 7, 10, 12, 7, 3, 15, 1, 10, 11, 10, 15, 14],
                           [13, 8, 0, 10, 6, 8, 8, 4, 2, 1, 10, 15, 8]],
                          ]


def id_xmp_data(fixture_value):
    """A function to generate fixture IDs"""
    yield f'xmp({fixture_value[0]}, {fixture_value[1]})'


@pytest.fixture(params=xmp_to_try, ids=id_xmp_data)
def xmp_params(request):
    yield request.param


@pytest.fixture()
def xmp_buffer():
    yield xmp_data


@pytest.fixture(params=bounding_boxes)
def bounding_box_params(request):
    yield request.param


@pytest.fixture()
def used_ifd_fields_raw():
    yield used_fields_raw


@pytest.fixture()
def used_ifd_fields_thumbnail():
    yield used_fields_thumbnail


@pytest.fixture()
def dng_canon_6d(data_folder_path):
    from brilliantimagery.dng import DNG
    yield DNG(str(data_folder_path / 'dng_canon_6d.dng'))


@pytest.fixture()
def meta_image_canon_6d(data_folder_path):
    from brilliantimagery.meta_image import MetaImage
    yield MetaImage(str(data_folder_path / 'dng_canon_6d.dng'))


@pytest.fixture()
def dng_pixel2(data_folder_path):
    from brilliantimagery.dng import DNG
    yield DNG(str(data_folder_path / 'dng_Pixel2.dng'))


@pytest.fixture()
def post_save_ifds():
    yield saved_ifds


@pytest.fixture()
def numpy_cropped_canon_6d(data_folder_path):
    image = np.load(str(data_folder_path / 'test_image_canon_6d_cropped.np'))
    rendered_area = [1500 / 5030, 1450 / 3350, (1500 + 700) / 5030, (1450 + 760) / 3350]
    yield image, rendered_area


@pytest.fixture()
def numpy_thumbnail_canon_6d(data_folder_path):
    yield np.load(str(data_folder_path / 'test_image_canon_6d_thumb.np'))


@pytest.fixture()
def dng_xmp():
    yield expected_xmp


@pytest.fixture()
def updated_dng_xmp():
    yield updated_xmp, new_xmp_values


@pytest.fixture()
def storable_dng_xmp():
    yield xmp_to_be_stored, updated_xmp_data


@pytest.fixture()
def dng_file_io_ifd(dng_canon_6d):
    from brilliantimagery.dng import DNG
    with open(dng_canon_6d.path, 'rb', buffering=DNG._BUFFER_SIZE) as f:
        f.seek(8)
        yield dng_canon_6d, f


@pytest.fixture()
def canon_6d_idfs():
    yield ifds


@pytest.fixture()
def canon_6d_compressed_tiles(data_folder_path):
    import pickle
    rectangle = [0.1, 0.1, 0.5, 0.5]

    tiles = pickle.load(open(str(data_folder_path / 'compressed_tiles.p'), 'rb'))

    yield rectangle, tiles


@pytest.fixture()
def copied_dng_canon_6d(data_folder_path, dng_canon_6d, tmpdir):
    import shutil
    from brilliantimagery.dng import DNG

    shutil.copy(str(str(data_folder_path / 'dng_canon_6d.dng')), str(tmpdir / 'dng_canon_6d.dng'))
    yield DNG(str(tmpdir / 'dng_canon_6d.dng'))


@pytest.fixture()
def dng_rendered_to_rgb_even_offsets(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (28, 62)
    rectangle = [100, 100, 500, 400]

    # dng_canon_6d.parse()
    dng_canon_6d.get_default_shape()
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'renderer_render_raw_even_even.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, expected_renderd_area, active_area_offset, rectangle


@pytest.fixture()
def dng_rendered_to_rgb_odd_offsets(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (29, 63)
    rectangle = [101, 101, 500, 400]

    # dng_canon_6d.parse()
    dng_canon_6d.get_default_shape()
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'renderer_render_raw_odd_even.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, expected_renderd_area, active_area_offset, rectangle


@pytest.fixture()
def dng_rendered_to_rgb_even_odd_offsets(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (28, 62)
    rectangle = [100, 100, 501, 401]

    # dng_canon_6d.parse()
    dng_canon_6d.get_default_shape()
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'renderer_render_raw_even_odd.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, expected_renderd_area, active_area_offset, rectangle


@pytest.fixture()
def dng_thumbnail_rendered_to_rgb_even_offsets(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (28, 62)
    rectangle = [20, 20, 200, 100]

    # dng_canon_6d.parse()
    dng_canon_6d.get_image(rectangle, 'thumbnail')
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'renderer_render_thumbnail_even.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, expected_renderd_area, active_area_offset, rectangle


@pytest.fixture()
def dng_thumbnail_rendered_to_rgb_odd_offsets(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (29, 63)
    rectangle = [21, 2, 200, 100]

    # dng_canon_6d.parse()
    dng_canon_6d.get_image(rectangle, 'thumbnail')
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'renderer_render_thumbnail_odd.np'), 'rb') as f:
        expected_renderd_area = np.load(f)
    # expected_renderd_area = 1

    yield ifd, expected_renderd_area, active_area_offset, rectangle


@pytest.fixture()
def scaled_raw_data_w_ifd_0112_even_offset(data_folder_path):
    import numpy as np

    active_area_offset = (2, 2)

    ifd = {}
    ifd['cfa_pattern'] = [0, 1, 1, 2]
    ifd['cfa_repeat_pattern_dim'] = [2, 2]

    image = np.asarray(scaled_raw_image, dtype=np.float32)

    with open(str(data_folder_path / 'raw_data_to_rgb_0112_even_offset.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def scaled_raw_data_w_ifd_0112_odd_offset(data_folder_path):
    import numpy as np

    active_area_offset = (1, 1)

    ifd = {}
    ifd['cfa_pattern'] = [0, 1, 1, 2]
    ifd['cfa_repeat_pattern_dim'] = [2, 2]

    image = np.asarray(scaled_raw_image, dtype=np.float32)

    with open(str(data_folder_path / 'raw_data_to_rgb_0112_odd_offset.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def scaled_raw_data_w_ifd_1021_even_offset(data_folder_path):
    import numpy as np

    active_area_offset = (2, 2)

    ifd = {}
    ifd['cfa_pattern'] = [1, 0, 2, 1]
    ifd['cfa_repeat_pattern_dim'] = [2, 2]

    image = np.asarray(scaled_raw_image, dtype=np.float32)

    with open(str(data_folder_path / 'raw_data_to_rgb_1021_even_offset.np'), 'rb') as f:
        expected_renderd_area = np.load(f)
    # expected_renderd_area = 1

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def unscaled_raw_data_w_2x2_mask_1_sample_per_pix(data_folder_path):
    active_area_offset = (2, 2)

    ifd = {}
    ifd['black_level'] = [2506, 2508, 2507, 2505]
    ifd['black_level_delta_V'] = [34, 18, 25, 13, 30, 17, 49, 23, 40, 12, 47, 38, 24, 40, 47]
    ifd['black_level_delta_H'] = [32, 28, 34, 24, 34, 20, 14, 13, 46, 26, 12, 15, 35, 48, 35]
    ifd['black_level_repeat_dim'] = [2, 2]
    ifd['cfa_repeat_pattern_dim'] = [2, 2]
    ifd['samples_per_pix'] = 1
    ifd['white_level'] = [13000]

    image = np.asarray(unscaled_raw_image, dtype=np.int32)

    with open(str(data_folder_path / 'unscaled_raw_data_w_2x2_mask_1_sample_per_pix.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def unscaled_raw_data_w_2x2_mask_1_sample_per_pix_odd(data_folder_path):
    active_area_offset = (1, 1)

    ifd = {}
    ifd['black_level'] = [2506, 2508, 2507, 2505]
    ifd['black_level_delta_V'] = [34, 18, 25, 13, 30, 17, 49, 23, 40, 12, 47, 38, 24, 40, 47]
    ifd['black_level_delta_H'] = [32, 28, 34, 24, 34, 20, 14, 13, 46, 26, 12, 15, 35, 48, 35]
    ifd['black_level_repeat_dim'] = [2, 2]
    ifd['cfa_repeat_pattern_dim'] = [2, 2]
    ifd['samples_per_pix'] = 1
    ifd['white_level'] = [13000]

    image = np.asarray(unscaled_raw_image, dtype=np.int32)

    with open(str(data_folder_path / 'unscaled_raw_data_w_2x2_mask_1_sample_per_pix_odd.np'), 'rb') as f:
        expected_renderd_area = np.load(f)
    # expected_renderd_area = 0

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def unscaled_raw_data_w_3_sample_per_pix(data_folder_path):
    active_area_offset = (2, 2)

    ifd = {}
    ifd['black_level'] = [2506, 2508, 2507, 2505]
    ifd['black_level_delta_V'] = [34, 18, 25, 13, 30, 17, 49, 23, 40, 12, 47, 38, 24, 40, 47]
    ifd['black_level_delta_H'] = [32, 28, 34, 24, 34, 20, 14, 13, 46, 26, 12, 15, 35, 48, 35]
    ifd['black_level_repeat_dim'] = [1, 1]
    ifd['samples_per_pix'] = 3
    ifd['white_level'] = [13000, 12050, 13005]

    image = np.asarray(unscaled_raw_image, dtype=np.int32)

    with open(str(data_folder_path / 'unscaled_raw_data_w_3_sample_per_pix.np'), 'rb') as f:
        expected_renderd_area = np.load(f)
    # expected_renderd_area = 1

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def unscaled_raw_data_w_linearization(data_folder_path):
    active_area_offset = (2, 2)

    ifd = {}
    ifd['black_level'] = [2506, 2508, 2507, 2505]
    ifd['black_level_delta_V'] = [34, 18, 25, 13, 30, 17, 49, 23, 40, 12, 47, 38, 24, 40, 47]
    ifd['black_level_delta_H'] = [32, 28, 34, 24, 34, 20, 14, 13, 46, 26, 12, 15, 35, 48, 35]
    ifd['black_level_repeat_dim'] = [2, 2]
    ifd['cfa_repeat_pattern_dim'] = [2, 2]
    ifd['linearization_table'] = [i * 10 for i in range(14)]
    ifd['samples_per_pix'] = 1
    ifd['white_level'] = [13000]

    image = np.asarray(unlinearized_raw_image, dtype=np.int32)

    with open(str(data_folder_path / 'unscaled_raw_data_w_linearization.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, image, active_area_offset, expected_renderd_area


@pytest.fixture()
def rectangle_to_clip():
    rectangle = [2, 3, 8, 10]
    bounding_box = [1, 2, 3, 3]

    ifd = {}
    ifd['rendered_rectangle'] = rectangle
    ifd['rendered_section_bounding_box'] = bounding_box

    image = [[[5, 15, 8, 8, 14, 10, 1, 7, 3, 9, 13, 15, 1],
              [6, 10, 1, 7, 7, 12, 10, 13, 8, 12, 14, 12, 4],
              [10, 5, 11, 5, 12, 1, 10, 9, 12, 14, 10, 12, 3],
              [4, 8, 1, 6, 5, 4, 13, 8, 11, 11, 0, 14, 4],
              [6, 13, 8, 5, 4, 14, 2, 12, 13, 3, 10, 11, 11],
              [3, 15, 10, 4, 3, 15, 12, 7, 9, 14, 12, 15, 4],
              [9, 2, 13, 8, 0, 15, 14, 2, 8, 1, 10, 4, 1],
              [9, 15, 1, 13, 0, 1, 4, 0, 11, 10, 5, 5, 15],
              [6, 3, 4, 8, 3, 7, 1, 11, 12, 11, 7, 5, 12],
              [1, 12, 15, 14, 12, 6, 14, 2, 3, 9, 1, 0, 5],
              [11, 8, 8, 6, 5, 7, 10, 7, 6, 6, 7, 6, 1]],
             [[0, 15, 3, 5, 14, 4, 15, 11, 2, 8, 0, 11, 15],
              [4, 7, 3, 5, 13, 11, 4, 2, 8, 2, 5, 1, 6],
              [11, 3, 11, 7, 9, 2, 3, 8, 9, 4, 5, 7, 5],
              [1, 2, 4, 5, 14, 4, 4, 6, 15, 15, 11, 10, 14],
              [6, 8, 1, 15, 3, 1, 2, 1, 8, 3, 9, 12, 0],
              [14, 10, 0, 13, 9, 5, 5, 7, 11, 6, 13, 5, 8],
              [10, 15, 0, 11, 8, 3, 6, 14, 7, 1, 8, 12, 0],
              [12, 10, 3, 6, 15, 2, 13, 11, 6, 1, 14, 13, 3],
              [8, 3, 12, 1, 0, 7, 14, 6, 12, 9, 2, 1, 5],
              [13, 10, 8, 11, 3, 5, 8, 3, 7, 3, 8, 3, 0],
              [10, 9, 6, 7, 4, 12, 8, 1, 10, 5, 12, 8, 2]],
             [[12, 3, 11, 3, 9, 2, 10, 6, 4, 14, 15, 8, 5],
              [12, 0, 12, 2, 0, 4, 10, 5, 6, 9, 5, 0, 8],
              [7, 3, 13, 7, 13, 8, 3, 8, 7, 14, 1, 5, 8],
              [5, 8, 13, 6, 8, 13, 4, 14, 7, 12, 8, 12, 3],
              [10, 9, 7, 1, 12, 15, 15, 3, 14, 5, 6, 14, 6],
              [8, 4, 6, 9, 5, 12, 10, 3, 8, 13, 2, 3, 15],
              [10, 9, 6, 10, 12, 15, 5, 9, 12, 14, 8, 14, 6],
              [15, 7, 5, 11, 12, 5, 3, 8, 1, 11, 8, 9, 14],
              [0, 4, 11, 15, 15, 12, 5, 15, 10, 12, 6, 5, 4],
              [9, 3, 13, 12, 10, 7, 8, 15, 1, 0, 2, 5, 9],
              [4, 10, 1, 13, 1, 9, 1, 3, 4, 1, 12, 4, 12]]
             ]
    image = np.asarray(unscaled_raw_image, dtype=np.int32)

    cropped_image = image[:, 1: 7, 1: 8]

    yield ifd, image, cropped_image


@pytest.fixture()
def unpackable_ifd_w_compressed_tiles(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (28, 62)
    rectangle = [100, 100, 500, 400]

    # dng_canon_6d.parse()
    dng_canon_6d.get_default_shape()
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'unpacked_compressed_tiles.np'), 'rb') as f:
        expected_renderd_area = np.load(f)

    yield ifd, expected_renderd_area, active_area_offset, rectangle


@pytest.fixture()
def unpackable_ifd_w_uncompressed_strips(dng_pixel2, data_folder_path):
    import numpy as np

    active_area_offset = (28, 62)
    rectangle = [100, 100, 500, 400]

    # dng_pixel2.parse()
    dng_pixel2.get_default_shape()
    dng_pixel2._get_tile_or_strip_bytes(rectangle)
    ifd = dng_pixel2._used_fields

    with open(str(data_folder_path / 'unpacked_uncompressed_strips.np'), 'rb') as f:
        expected_renderd_area = np.load(f)
    # expected_renderd_area = 1

    yield ifd, expected_renderd_area, active_area_offset, rectangle
