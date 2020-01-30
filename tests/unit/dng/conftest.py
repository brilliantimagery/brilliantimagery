from collections import namedtuple

import pytest
import numpy as np

xmp_data = '<?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?>.<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c128 79.159124, 2016/03/18-14:01:55        ">. <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">.  <rdf:Description rdf:about="".    xmlns:xmp="http://ns.adobe.com/xap/1.0/".    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/".    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/".    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/".    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#".    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#".    xmlns:dc="http://purl.org/dc/elements/1.1/".    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/".    xmlns:lr="http://ns.adobe.com/lightroom/1.0/".   xmp:ModifyDate="2018-12-23T16:20:34-08:00".   xmp:CreateDate="2017-09-07T16:01:38.03".   xmp:MetadataDate="2018-12-25T16:04:27-08:00".   xmp:Rating="3".   xmp:CreatorTool="Adobe Photoshop Lightroom 6.12 (Windows)".   aux:SerialNumber="222020003981".   aux:LensInfo="24/1 105/1 0/0 0/0".   aux:Lens="EF24-105mm f/4L IS USM".   aux:LensID="237".   aux:LensSerialNumber="0000712524".   aux:ImageNumber="0".   aux:ApproximateFocusDistance="100/100".   aux:FlashCompensation="0/1".   aux:Firmware="1.1.6".   photoshop:DateCreated="2017-09-07T16:01:38.03".   xmpMM:DocumentID="xmp.did:c4db0699-4104-4f40-b561-27c7c7b028dd".   xmpMM:OriginalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8".   xmpMM:InstanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2".   dc:format="image/dng".   crs:Version="9.12".   crs:ProcessVersion="6.7".   crs:WhiteBalance="Cloudy".   crs:AutoWhiteVersion="134348800".   crs:Temperature="6500".   crs:Tint="+10".   crs:Saturation="+35".   crs:Sharpness="25".   crs:LuminanceSmoothing="0".   crs:ColorNoiseReduction="25".   crs:VignetteAmount="0".   crs:ShadowTint="0".   crs:RedHue="0".   crs:RedSaturation="0".   crs:GreenHue="0".   crs:GreenSaturation="0".   crs:BlueHue="0".   crs:BlueSaturation="0".   crs:Vibrance="+29".   crs:HueAdjustmentRed="0".   crs:HueAdjustmentOrange="0".   crs:HueAdjustmentYellow="0".   crs:HueAdjustmentGreen="0".   crs:HueAdjustmentAqua="0".   crs:HueAdjustmentBlue="0".   crs:HueAdjustmentPurple="0".   crs:HueAdjustmentMagenta="0".   crs:SaturationAdjustmentRed="0".   crs:SaturationAdjustmentOrange="0".   crs:SaturationAdjustmentYellow="0".   crs:SaturationAdjustmentGreen="0".   crs:SaturationAdjustmentAqua="0".   crs:SaturationAdjustmentBlue="0".   crs:SaturationAdjustmentPurple="0".   crs:SaturationAdjustmentMagenta="0".   crs:LuminanceAdjustmentRed="0".   crs:LuminanceAdjustmentOrange="0".   crs:LuminanceAdjustmentYellow="0".   crs:LuminanceAdjustmentGreen="0".   crs:LuminanceAdjustmentAqua="0".   crs:LuminanceAdjustmentBlue="0".   crs:LuminanceAdjustmentPurple="0".   crs:LuminanceAdjustmentMagenta="0".   crs:SplitToningShadowHue="0".   crs:SplitToningShadowSaturation="0".   crs:SplitToningHighlightHue="0".   crs:SplitToningHighlightSaturation="0".   crs:SplitToningBalance="0".   crs:ParametricShadows="0".   crs:ParametricDarks="0".   crs:ParametricLights="0".   crs:ParametricHighlights="0".   crs:ParametricShadowSplit="25".   crs:ParametricMidtoneSplit="50".   crs:ParametricHighlightSplit="75".   crs:SharpenRadius="+1.0".   crs:SharpenDetail="25".   crs:SharpenEdgeMasking="0".   crs:PostCropVignetteAmount="0".   crs:GrainAmount="0".   crs:ColorNoiseReductionDetail="50".   crs:ColorNoiseReductionSmoothness="50".   crs:LensProfileEnable="0".   crs:LensManualDistortionAmount="0".   crs:PerspectiveVertical="0".   crs:PerspectiveHorizontal="0".   crs:PerspectiveRotate="0.0".   crs:PerspectiveScale="100".   crs:PerspectiveAspect="0".   crs:PerspectiveUpright="0".   crs:PerspectiveX="0.00".   crs:PerspectiveY="0.00".   crs:AutoLateralCA="0".   crs:Exposure2012="-0.10".   crs:Contrast2012="0".   crs:Highlights2012="+24".   crs:Shadows2012="48".   crs:Whites2012="+31".   crs:Blacks2012="-10".   crs:Clarity2012="0".   crs:DefringePurpleAmount="0".   crs:DefringePurpleHueLo="30".   crs:DefringePurpleHueHi="70".   crs:DefringeGreenAmount="0".   crs:DefringeGreenHueLo="40".   crs:DefringeGreenHueHi="60".   crs:Dehaze="0".   crs:ToneMapStrength="0".   crs:ConvertToGrayscale="False".   crs:ToneCurveName="Medium Contrast".   crs:ToneCurveName2012="Linear".   crs:CameraProfile="Adobe Standard".   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975".   crs:LensProfileSetup="LensDefaults".   crs:UprightVersion="151388160".   crs:UprightCenterMode="0".   crs:UprightCenterNormX="0.5".   crs:UprightCenterNormY="0.5".   crs:UprightFocalMode="0".   crs:UprightFocalLength35mm="35".   crs:UprightPreview="False".   crs:UprightTransformCount="6".   crs:UprightFourSegmentsCount="0".   crs:HasSettings="True".   crs:CropTop="0.142125".   crs:CropLeft="0.050467".   crs:CropBottom="0.969144".   crs:CropRight="0.969144".   crs:CropAngle="0".   crs:CropConstrainToWarp="0".   crs:HasCrop="True".   crs:AlreadyApplied="False".   crs:RawFileName="dng_canon_6d.dng">.   <xmpMM:History>.    <rdf:Seq>.     <rdf:li.      stEvt:action="derived".      stEvt:parameters="converted from image/x-canon-cr2 to image/dng, saved to new location"/>.     <rdf:li.      stEvt:action="saved".      stEvt:instanceID="xmp.iid:c4db0699-4104-4f40-b561-27c7c7b028dd".      stEvt:when="2018-12-23T16:20:34-08:00".      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)".      stEvt:changed="/"/>.     <rdf:li.      stEvt:action="saved".      stEvt:instanceID="xmp.iid:c813d0e0-8fd2-6740-98f3-0fdecd7152d2".      stEvt:when="2018-12-25T16:04:27-08:00".      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.12 (Windows)".      stEvt:changed="/metadata"/>.    </rdf:Seq>.   </xmpMM:History>.   <xmpMM:DerivedFrom.    stRef:documentID="6BF93FCB1F578C3204916BCCDEAD23D8".    stRef:originalDocumentID="6BF93FCB1F578C3204916BCCDEAD23D8"/>.   <dc:subject>.    <rdf:Bag>.     <rdf:li>Jelleybean</rdf:li>.    </rdf:Bag>.   </dc:subject>.   <crs:ToneCurve>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>32, 22</rdf:li>.     <rdf:li>64, 56</rdf:li>.     <rdf:li>128, 128</rdf:li>.     <rdf:li>192, 196</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurve>.   <crs:ToneCurveRed>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveRed>.   <crs:ToneCurveGreen>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveGreen>.   <crs:ToneCurveBlue>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurveBlue>.   <crs:ToneCurvePV2012>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012>.   <crs:ToneCurvePV2012Red>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Red>.   <crs:ToneCurvePV2012Green>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Green>.   <crs:ToneCurvePV2012Blue>.    <rdf:Seq>.     <rdf:li>0, 0</rdf:li>.     <rdf:li>255, 255</rdf:li>.    </rdf:Seq>.   </crs:ToneCurvePV2012Blue>.   <lr:hierarchicalSubject>.    <rdf:Bag>.     <rdf:li>Jelleybean</rdf:li>.    </rdf:Bag>.   </lr:hierarchicalSubject>.  </rdf:Description>. </rdf:RDF>.</x:xmpmeta> <?xpacket end="w"?>'
xmp_data = bytes(xmp_data, 'utf-8')

updated_xmp_data = b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c011 79.156380, 2014/05/21-23:38:37        ">\n <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n  <rdf:Description rdf:about=""\n    xmlns:dc="http://purl.org/dc/elements/1.1/"\n    xmlns:xmp="http://ns.adobe.com/xap/1.0/"\n    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/"\n    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"\n    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"\n    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"\n    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#"\n    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"\n    xmlns:lr="http://ns.adobe.com/lightroom/1.0/"\n   dc:format="image/dng"\n   xmp:CreatorTool="Adobe DNG Converter 9.2 (Windows)"\n   xmp:ModifyDate="2020-01-29T14:51:18-08:00"\n   xmp:CreateDate="2016-05-24T07:14:56.19"\n   xmp:MetadataDate="2020-01-29T14:51:18-08:00"\n   xmp:Rating="3"\n   aux:SerialNumber="222020003981"\n   aux:LensInfo="24/1 105/1 0/0 0/0"\n   aux:Lens="EF24-105mm f/4L IS USM"\n   aux:LensID="237"\n   aux:LensSerialNumber="0000712524"\n   aux:ImageNumber="0"\n   aux:ApproximateFocusDistance="119/10"\n   aux:FlashCompensation="0/1"\n   aux:Firmware="1.1.6"\n   aux:DistortionCorrectionAlreadyApplied="True"\n   aux:LateralChromaticAberrationCorrectionAlreadyApplied="True"\n   aux:VignetteCorrectionAlreadyApplied="True"\n   photoshop:DateCreated="2016-05-24T07:14:56.19"\n   xmpMM:DocumentID="xmp.did:46e5fbdc-0819-6345-807c-4e3addeb789c"\n   xmpMM:OriginalDocumentID="8B99E42CA2FB533F6842C19153BD50E7"\n   xmpMM:InstanceID="xmp.iid:46e5fbdc-0819-6345-807c-4e3addeb789c"\n   crs:Version="9.7"\n   crs:ProcessVersion="6.7"\n   crs:WhiteBalance="Custom"\n   crs:AutoWhiteVersion="134348800"\n   crs:Temperature="+7135"\n   crs:Tint="+10"\n   crs:Saturation="+11"\n   crs:Sharpness="+25"\n   crs:LuminanceSmoothing="0"\n   crs:ColorNoiseReduction="25"\n   crs:VignetteAmount="0"\n   crs:ShadowTint="0"\n   crs:RedHue="+4"\n   crs:RedSaturation="0"\n   crs:GreenHue="0"\n   crs:GreenSaturation="0"\n   crs:BlueHue="0"\n   crs:BlueSaturation="0"\n   crs:Vibrance="+76"\n   crs:HueAdjustmentRed="0"\n   crs:HueAdjustmentOrange="0"\n   crs:HueAdjustmentYellow="0"\n   crs:HueAdjustmentGreen="0"\n   crs:HueAdjustmentAqua="0"\n   crs:HueAdjustmentBlue="+27"\n   crs:HueAdjustmentPurple="0"\n   crs:HueAdjustmentMagenta="0"\n   crs:SaturationAdjustmentRed="0"\n   crs:SaturationAdjustmentOrange="0"\n   crs:SaturationAdjustmentYellow="0"\n   crs:SaturationAdjustmentGreen="0"\n   crs:SaturationAdjustmentAqua="0"\n   crs:SaturationAdjustmentBlue="-31"\n   crs:SaturationAdjustmentPurple="0"\n   crs:SaturationAdjustmentMagenta="0"\n   crs:LuminanceAdjustmentRed="0"\n   crs:LuminanceAdjustmentOrange="0"\n   crs:LuminanceAdjustmentYellow="0"\n   crs:LuminanceAdjustmentGreen="0"\n   crs:LuminanceAdjustmentAqua="0"\n   crs:LuminanceAdjustmentBlue="0"\n   crs:LuminanceAdjustmentPurple="0"\n   crs:LuminanceAdjustmentMagenta="0"\n   crs:SplitToningShadowHue="0"\n   crs:SplitToningShadowSaturation="0"\n   crs:SplitToningHighlightHue="0"\n   crs:SplitToningHighlightSaturation="0"\n   crs:SplitToningBalance="0"\n   crs:ParametricShadows="0"\n   crs:ParametricDarks="0"\n   crs:ParametricLights="0"\n   crs:ParametricHighlights="0"\n   crs:ParametricShadowSplit="25"\n   crs:ParametricMidtoneSplit="50"\n   crs:ParametricHighlightSplit="75"\n   crs:SharpenRadius="+1.0"\n   crs:SharpenDetail="25"\n   crs:SharpenEdgeMasking="0"\n   crs:PostCropVignetteAmount="0"\n   crs:GrainAmount="0"\n   crs:ColorNoiseReductionDetail="50"\n   crs:ColorNoiseReductionSmoothness="50"\n   crs:LensProfileEnable="1"\n   crs:LensManualDistortionAmount="0"\n   crs:PerspectiveVertical="0"\n   crs:PerspectiveHorizontal="0"\n   crs:PerspectiveRotate="0.0"\n   crs:PerspectiveScale="100"\n   crs:PerspectiveAspect="0"\n   crs:PerspectiveUpright="0"\n   crs:PerspectiveX="0.00"\n   crs:PerspectiveY="0.00"\n   crs:AutoLateralCA="1"\n   crs:Exposure2012="+0.4"\n   crs:Contrast2012="0"\n   crs:Highlights2012="-100"\n   crs:Shadows2012="-28"\n   crs:Whites2012="+71"\n   crs:Blacks2012="+2"\n   crs:Clarity2012="+29"\n   crs:DefringePurpleAmount="0"\n   crs:DefringePurpleHueLo="30"\n   crs:DefringePurpleHueHi="70"\n   crs:DefringeGreenAmount="0"\n   crs:DefringeGreenHueLo="40"\n   crs:DefringeGreenHueHi="60"\n   crs:Dehaze="+10"\n   crs:ToneMapStrength="0"\n   crs:ConvertToGrayscale="False"\n   crs:ToneCurveName="Medium Contrast"\n   crs:ToneCurveName2012="Linear"\n   crs:CameraProfile="Adobe Standard"\n   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975"\n   crs:LensProfileSetup="LensDefaults"\n   crs:LensProfileName="Adobe (Canon EF 24-105mm f/4 L IS USM)"\n   crs:LensProfileFilename="Canon EOS-1Ds Mark III (Canon EF 24-105mm f4 L IS USM) - RAW.lcp"\n   crs:LensProfileDigest="F59965C057650927AFD8E60143A071CA"\n   crs:LensProfileDistortionScale="100"\n   crs:LensProfileChromaticAberrationScale="100"\n   crs:LensProfileVignettingScale="100"\n   crs:UprightVersion="151388160"\n   crs:UprightCenterMode="0"\n   crs:UprightCenterNormX="0.5"\n   crs:UprightCenterNormY="0.5"\n   crs:UprightFocalMode="0"\n   crs:UprightFocalLength35mm="35"\n   crs:UprightPreview="False"\n   crs:UprightTransformCount="6"\n   crs:UprightFourSegmentsCount="0"\n   crs:HasSettings="True"\n   crs:CropTop="0.06"\n   crs:CropLeft="0.048838"\n   crs:CropBottom="0.852893"\n   crs:CropRight="0.89261"\n   crs:CropAngle="0"\n   crs:CropConstrainToWarp="0"\n   crs:HasCrop="True"\n   crs:AlreadyApplied="False"\n   crs:RawFileName="_MG_1601.DNG">\n   <dc:subject>\n    <rdf:Bag>\n     <rdf:li>Dual-ISO</rdf:li>\n    </rdf:Bag>\n   </dc:subject>\n   <xmpMM:History>\n    <rdf:Seq>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:d10cee0e-0500-9843-ac18-38fd7e409480"\n      stEvt:when="2016-05-24T19:25:52-07:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.5 (Windows)"\n      stEvt:changed="/metadata"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:99c42cb0-fb96-964a-a704-5a5b644cc03b"\n      stEvt:when="2016-10-31T13:08:15-07:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.7 (Windows)"\n      stEvt:changed="/metadata"/>\n     <rdf:li\n      stEvt:action="derived"\n      stEvt:parameters="saved to new location"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:46e5fbdc-0819-6345-807c-4e3addeb789c"\n      stEvt:when="2020-01-29T14:51:18-08:00"\n      stEvt:softwareAgent="Adobe DNG Converter 9.2 (Windows)"\n      stEvt:changed="/"/>\n    </rdf:Seq>\n   </xmpMM:History>\n   <xmpMM:DerivedFrom\n    stRef:instanceID="xmp.iid:99c42cb0-fb96-964a-a704-5a5b644cc03b"\n    stRef:documentID="8B99E42CA2FB533F6842C19153BD50E7"\n    stRef:originalDocumentID="8B99E42CA2FB533F6842C19153BD50E7"/>\n   <crs:ToneCurve>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>32, 22</rdf:li>\n     <rdf:li>64, 56</rdf:li>\n     <rdf:li>128, 128</rdf:li>\n     <rdf:li>192, 196</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurve>\n   <crs:ToneCurveRed>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveRed>\n   <crs:ToneCurveGreen>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveGreen>\n   <crs:ToneCurveBlue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveBlue>\n   <crs:ToneCurvePV2012>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012>\n   <crs:ToneCurvePV2012Red>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Red>\n   <crs:ToneCurvePV2012Green>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Green>\n   <crs:ToneCurvePV2012Blue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Blue>\n   <lr:hierarchicalSubject>\n    <rdf:Bag>\n     <rdf:li>Dual-ISO</rdf:li>\n    </rdf:Bag>\n   </lr:hierarchicalSubject>\n  </rdf:Description>\n </rdf:RDF>\n</x:xmpmeta>\n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                       \n<?xpacket end="w"?>'

xmp_to_try = ((b'xmp:Rating', '3'),
              (b'crs:Saturation', '+35'),
              (b'crs:Exposure2012', '-0.10'),
              (b'crs:Shadows2012', '48'),
              (b'crs:RedHue', '0'),
              (b'crs:CropTop', '0.142125'),
              (b'hello', None),
              # (b'crs:AlreadyApplied', 'False'),
              )

expected_xmp = {b'crs:Temperature': 7135.0, b'crs:Tint': 10.0, b'crs:Saturation': 35.0, b'crs:Vibrance': 76.0, b'crs:Sharpness': 25.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': 0.0, b'crs:RedSaturation': 0.0, b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0, b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0, b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 27.0, b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0, b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0, b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0, b'crs:SaturationAdjustmentBlue': -31.0, b'crs:SaturationAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0, b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0, b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0, b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0, b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0, b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0, b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0, b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0, b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0, b'crs:ColorNoiseReductionDetail': 50.0, b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0, b'crs:Contrast2012': 0.0, b'crs:Highlights2012': -100.0, b'crs:Shadows2012': 48.0, b'crs:Whites2012': 71.0, b'crs:Blacks2012': 2.0, b'crs:Clarity2012': 29.0, b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0, b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0, b'crs:Dehaze': 10.0, b'crs:CropLeft': 0.048838, b'crs:CropBottom': 0.852893, b'crs:CropRight': 0.89261, b'crs:CropTop': 0.142125, b'xmp:Rating': 3.0, b'crs:Exposure2012': -0.1}

new_xmp_values = {b'xmp:Rating': 3,
                  b'crs:Saturation': '+11',
                  b'crs:Exposure2012': '+0.40',
                  b'crs:Shadows2012': '-28',
                  b'crs:RedHue': '4',
                  b'crs:CropTop': 0.06,
                  b'crs:AlreadyApplied': 'True',
                  }

updated_xmp = {b'crs:Temperature': 7135.0, b'crs:Tint': 10.0, b'crs:Saturation': '+11', b'crs:Vibrance': 76.0, b'crs:Sharpness': 25.0, b'crs:ShadowTint': 0.0, b'crs:RedHue': '4', b'crs:RedSaturation': 0.0, b'crs:GreenHue': 0.0, b'crs:GreenSaturation': 0.0, b'crs:BlueHue': 0.0, b'crs:BlueSaturation': 0.0, b'crs:HueAdjustmentRed': 0.0, b'crs:HueAdjustmentOrange': 0.0, b'crs:HueAdjustmentYellow': 0.0, b'crs:HueAdjustmentGreen': 0.0, b'crs:HueAdjustmentAqua': 0.0, b'crs:HueAdjustmentBlue': 27.0, b'crs:HueAdjustmentPurple': 0.0, b'crs:HueAdjustmentMagenta': 0.0, b'crs:SaturationAdjustmentRed': 0.0, b'crs:SaturationAdjustmentOrange': 0.0, b'crs:SaturationAdjustmentYellow': 0.0, b'crs:SaturationAdjustmentGreen': 0.0, b'crs:SaturationAdjustmentAqua': 0.0, b'crs:SaturationAdjustmentBlue': -31.0, b'crs:SaturationAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentRed': 0.0, b'crs:LuminanceAdjustmentOrange': 0.0, b'crs:LuminanceAdjustmentYellow': 0.0, b'crs:LuminanceAdjustmentGreen': 0.0, b'crs:LuminanceAdjustmentAqua': 0.0, b'crs:LuminanceAdjustmentBlue': 0.0, b'crs:LuminanceAdjustmentPurple': 0.0, b'crs:LuminanceAdjustmentMagenta': 0.0, b'crs:ParametricShadows': 0.0, b'crs:ParametricDarks': 0.0, b'crs:ParametricLights': 0.0, b'crs:ParametricHighlights': 0.0, b'crs:ParametricShadowSplit': 25.0, b'crs:ParametricMidtoneSplit': 50.0, b'crs:ParametricHighlightSplit': 75.0, b'crs:SharpenRadius': 1.0, b'crs:SharpenDetail': 25.0, b'crs:SharpenEdgeMasking': 0.0, b'crs:GrainAmount': 0.0, b'crs:LuminanceSmoothing': 0.0, b'crs:ColorNoiseReduction': 25.0, b'crs:ColorNoiseReductionDetail': 50.0, b'crs:ColorNoiseReductionSmoothness': 50.0, b'crs:LensManualDistortionAmount': 0.0, b'crs:Contrast2012': 0.0, b'crs:Highlights2012': -100.0, b'crs:Shadows2012': '-28', b'crs:Whites2012': 71.0, b'crs:Blacks2012': 2.0, b'crs:Clarity2012': 29.0, b'crs:DefringePurpleAmount': 0.0, b'crs:DefringePurpleHueLo': 30.0, b'crs:DefringePurpleHueHi': 70.0, b'crs:DefringeGreenAmount': 0.0, b'crs:DefringeGreenHueLo': 40.0, b'crs:DefringeGreenHueHi': 60.0, b'crs:Dehaze': 10.0, b'crs:CropLeft': 0.048838, b'crs:CropBottom': 0.852893, b'crs:CropRight': 0.89261, b'crs:CropTop': 0.06, b'xmp:Rating': 3, b'crs:Exposure2012': '+0.40'}

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

used_fields_raw = {'bits_per_sample': [16], 'tile_offsets': [323756, 381160, 444526, 508528, 573598, 648380, 724366, 798340, 869020, 933310, 1001154, 1063918, 1125742, 1188588, 1253456, 1315392, 1378298, 1441750, 1504386, 1566954, 1628456, 1690368, 1744604, 1808826, 1878574, 1944834, 2012350, 2086600, 2162890, 2231018, 2309924, 2377310, 2454048, 2520382, 2589516, 2654208, 2724552, 2788734, 2856142, 2921528, 2985154, 3049632, 3113788, 3178222, 3233818, 3299174, 3367014, 3432614, 3498906, 3566060, 3631642, 3697022, 3779344, 3854578, 3924982, 3994178, 4063846, 4128520, 4194460, 4257976, 4323950, 4390136, 4453878, 4518492, 4583586, 4647616, 4702324, 4766640, 4836642, 4902620, 4971362, 5041926, 5114412, 5182908, 5268384, 5355122, 5425972, 5493148, 5560426, 5625870, 5689486, 5753464, 5817964, 5882372, 5946560, 6011674, 6076248, 6130310, 6177556, 6230770, 6303056, 6381818, 6457056, 6536266, 6613214, 6690402, 6770714, 6851274, 6933090, 7008208, 7076576, 7140926, 7204452, 7268304, 7332532, 7396888, 7461636, 7526030, 7588022, 7640518, 7686964, 7736384, 7790328, 7844924, 7901994, 7960408, 8019014, 8081496, 8151554, 8228350, 8298912, 8369356, 8435858, 8500182, 8564604, 8628982, 8691798, 8751646, 8805634, 8861366, 8912650, 8963660, 9010316, 9056818, 9108458, 9157574, 9210902, 9267094, 9325624, 9383276, 9447612, 9514002, 9583112, 9653338, 9721798, 9788788, 9846840, 9902002, 9959254, 10013956, 10067234, 10118674, 10168884, 10219160, 10264348, 10309028, 10355906, 10403324, 10451460, 10504286, 10562132, 10620002, 10680460, 10744822, 10808642, 10872634, 10937314, 11001392, 11057766, 11114148, 11166954, 11220504, 11269510, 11318054, 11368660, 11416244, 11459150, 11499742, 11543992, 11587266, 11630404, 11677468, 11730848, 11783180, 11843698, 11903876, 11979030, 12056502, 12121900, 12180858, 12233962, 12285492, 12329814, 12372342, 12415230, 12461702, 12505946, 12551170, 12593378, 12632626, 12673154, 12717674, 12759958, 12804336, 12850814, 12900400, 12954386, 13009098, 13061708, 13110842, 13160654, 13214474, 13269126, 13315222, 13366750, 13414896, 13466184, 13515836, 13565416, 13612558, 13655988, 13701192, 13747364, 13795416, 13843558, 13894048, 13949362, 14005302, 14061230, 14116910, 14173794, 14230274, 14286194, 14342778, 14396370, 14438418, 14492594, 14548738, 14603008, 14654810, 14703708, 14750668, 14793236, 14842192, 14897180, 14950798, 15008802, 15067286, 15126446, 15186946, 15250822, 15313638, 15374670, 15433656, 15488954, 15537420, 15577842, 15622634, 15675302, 15736318, 15797928, 15859974, 15919670, 15978934, 16027984, 16063542, 16100912, 16139078, 16178920, 16221212, 16263734, 16306792, 16350294, 16393364, 16437414, 16481594, 16527318, 16570988, 16618716, 16671602, 16728606, 16780334, 16826348, 16874580, 16922240, 16971286, 17015314, 17047130, 17080268, 17113562, 17146846, 17180516, 17215178, 17250280, 17284590, 17320620, 17359722, 17399858, 17439554, 17482830, 17527370, 17574594, 17627334, 17685342, 17735316, 17787486, 17840264, 17891690, 17934526, 17955858, 17978558, 18002594, 18024364, 18045892, 18067948, 18090106, 18112428, 18134842, 18157258, 18179530, 18202202, 18226298, 18249562, 18284028, 18315542, 18347006, 18374502, 18404254, 18436508, 18469348], 'tile_byte_counts': [57403, 63365, 64002, 65069, 74782, 75985, 73974, 70679, 64290, 67844, 62764, 61824, 62846, 64867, 61936, 62905, 63452, 62635, 62568, 61501, 61912, 54235, 64221, 69747, 66260, 67516, 74250, 76290, 68128, 78906, 67385, 76737, 66333, 69134, 64691, 70343, 64181, 67407, 65385, 63625, 64477, 64156, 64434, 55595, 65356, 67840, 65600, 66291, 67153, 65582, 65379, 82321, 75233, 70403, 69195, 69667, 64673, 65940, 63515, 65973, 66186, 63741, 64613, 65093, 64030, 54707, 64315, 70001, 65978, 68742, 70564, 72486, 68496, 85475, 86738, 70850, 67175, 67278, 65443, 63615, 63978, 64499, 64407, 64187, 65113, 64574, 54062, 47245, 53213, 72286, 78761, 75237, 79209, 76948, 77188, 80312, 80559, 81815, 75118, 68367, 64350, 63526, 63851, 64228, 64355, 64747, 64393, 61991, 52496, 46446, 49420, 53944, 54596, 57070, 58413, 58606, 62482, 70057, 76795, 70562, 70444, 66502, 64324, 64422, 64378, 62816, 59848, 53988, 55732, 51283, 51010, 46655, 46502, 51639, 49115, 53328, 56191, 58529, 57651, 64336, 66390, 69110, 70226, 68460, 66989, 58052, 55161, 57252, 54701, 53278, 51439, 50210, 50275, 45188, 44680, 46877, 47417, 48135, 52826, 57845, 57869, 60457, 64362, 63819, 63992, 64679, 64078, 56374, 56382, 52806, 53550, 49006, 48544, 50605, 47584, 42905, 40591, 44249, 43274, 43138, 47063, 53380, 52331, 60518, 60178, 75154, 77471, 65397, 58957, 53103, 51530, 44321, 42528, 42888, 46471, 44243, 45223, 42208, 39247, 40528, 44520, 42283, 44377, 46478, 49585, 53985, 54711, 52609, 49133, 49812, 53820, 54651, 46095, 51528, 48146, 51287, 49652, 49580, 47141, 43429, 45204, 46172, 48052, 48141, 50489, 55313, 55940, 55927, 55680, 56883, 56480, 55920, 56583, 53592, 42047, 54176, 56143, 54270, 51801, 48897, 46960, 42568, 48955, 54987, 53618, 58004, 58484, 59159, 60500, 63876, 62815, 61031, 58985, 55297, 48466, 40422, 44792, 52668, 61016, 61610, 62045, 59696, 59264, 49049, 35558, 37369, 38165, 39841, 42291, 42521, 43058, 43502, 43070, 44050, 44180, 45723, 43669, 47728, 52885, 57004, 51727, 46014, 48231, 47659, 49045, 44027, 31815, 33137, 33294, 33283, 33669, 34662, 35101, 34309, 36030, 39101, 40136, 39696, 43275, 44539, 47224, 52740, 58007, 49974, 52170, 52777, 51426, 42836, 21332, 22700, 24035, 21769, 21527, 22056, 22158, 22321, 22413, 22416, 22272, 22672, 24095, 23264, 34465, 31514, 31463, 27495, 29752, 32254, 32840, 26460], 'cfa_repeat_pattern_dim': [2, 2], 'cfa_pattern': [0, 1, 1, 2], 'black_level_repeat_dim': [1, 1], 'black_level': [8184.0], 'white_level': [40172], 'default_scale': [1.0, 1.0], 'default_crop_origin': [0.0, 0.0], 'default_crop_size': [5496.0, 3670.0], 'active_area': [38, 72, 3708, 5568], 'image_width': 5568, 'image_length': 3708, 'compression': 7, 'photometric_interpretation': 32803, 'samples_per_pix': 1, 'planar_configuration': 1, 'tile_width': 256, 'tile_length': 256, 'cfa_plane_color': 0, 'cfa_layout': 1, 'orientation': 1}

used_fields_thumbnail = {'bits_per_sample': [8, 8, 8], 'strip_offsets': [145728], 'strip_byte_counts': [110592], 'sub_ifds': [141564, 144650], 'image_width': 256, 'image_length': 144, 'compression': 1, 'photometric_interpretation': 2, 'orientation': 1, 'samples_per_pix': 3, 'rows_per_strip': 144, 'planar_configuration': 1, 'xmp': b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c011 79.156380, 2014/05/21-23:38:37        ">\n <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n  <rdf:Description rdf:about=""\n    xmlns:dc="http://purl.org/dc/elements/1.1/"\n    xmlns:xmp="http://ns.adobe.com/xap/1.0/"\n    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/"\n    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"\n    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"\n    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"\n    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#"\n    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"\n    xmlns:lr="http://ns.adobe.com/lightroom/1.0/"\n   dc:format="image/dng"\n   xmp:CreatorTool="Adobe DNG Converter 9.2 (Windows)"\n   xmp:ModifyDate="2020-01-29T14:51:18-08:00"\n   xmp:CreateDate="2016-05-24T07:14:56.19"\n   xmp:MetadataDate="2020-01-29T14:51:18-08:00"\n   xmp:Rating="3"\n   aux:SerialNumber="222020003981"\n   aux:LensInfo="24/1 105/1 0/0 0/0"\n   aux:Lens="EF24-105mm f/4L IS USM"\n   aux:LensID="237"\n   aux:LensSerialNumber="0000712524"\n   aux:ImageNumber="0"\n   aux:ApproximateFocusDistance="119/10"\n   aux:FlashCompensation="0/1"\n   aux:Firmware="1.1.6"\n   aux:DistortionCorrectionAlreadyApplied="True"\n   aux:LateralChromaticAberrationCorrectionAlreadyApplied="True"\n   aux:VignetteCorrectionAlreadyApplied="True"\n   photoshop:DateCreated="2016-05-24T07:14:56.19"\n   xmpMM:DocumentID="xmp.did:46e5fbdc-0819-6345-807c-4e3addeb789c"\n   xmpMM:OriginalDocumentID="8B99E42CA2FB533F6842C19153BD50E7"\n   xmpMM:InstanceID="xmp.iid:46e5fbdc-0819-6345-807c-4e3addeb789c"\n   crs:Version="9.7"\n   crs:ProcessVersion="6.7"\n   crs:WhiteBalance="Custom"\n   crs:AutoWhiteVersion="134348800"\n   crs:Temperature="+7135"\n   crs:Tint="+10"\n   crs:Saturation="+35"\n   crs:Sharpness="+25"\n   crs:LuminanceSmoothing="0"\n   crs:ColorNoiseReduction="25"\n   crs:VignetteAmount="0"\n   crs:ShadowTint="0"\n   crs:RedHue="0"\n   crs:RedSaturation="0"\n   crs:GreenHue="0"\n   crs:GreenSaturation="0"\n   crs:BlueHue="0"\n   crs:BlueSaturation="0"\n   crs:Vibrance="+76"\n   crs:HueAdjustmentRed="0"\n   crs:HueAdjustmentOrange="0"\n   crs:HueAdjustmentYellow="0"\n   crs:HueAdjustmentGreen="0"\n   crs:HueAdjustmentAqua="0"\n   crs:HueAdjustmentBlue="+27"\n   crs:HueAdjustmentPurple="0"\n   crs:HueAdjustmentMagenta="0"\n   crs:SaturationAdjustmentRed="0"\n   crs:SaturationAdjustmentOrange="0"\n   crs:SaturationAdjustmentYellow="0"\n   crs:SaturationAdjustmentGreen="0"\n   crs:SaturationAdjustmentAqua="0"\n   crs:SaturationAdjustmentBlue="-31"\n   crs:SaturationAdjustmentPurple="0"\n   crs:SaturationAdjustmentMagenta="0"\n   crs:LuminanceAdjustmentRed="0"\n   crs:LuminanceAdjustmentOrange="0"\n   crs:LuminanceAdjustmentYellow="0"\n   crs:LuminanceAdjustmentGreen="0"\n   crs:LuminanceAdjustmentAqua="0"\n   crs:LuminanceAdjustmentBlue="0"\n   crs:LuminanceAdjustmentPurple="0"\n   crs:LuminanceAdjustmentMagenta="0"\n   crs:SplitToningShadowHue="0"\n   crs:SplitToningShadowSaturation="0"\n   crs:SplitToningHighlightHue="0"\n   crs:SplitToningHighlightSaturation="0"\n   crs:SplitToningBalance="0"\n   crs:ParametricShadows="0"\n   crs:ParametricDarks="0"\n   crs:ParametricLights="0"\n   crs:ParametricHighlights="0"\n   crs:ParametricShadowSplit="25"\n   crs:ParametricMidtoneSplit="50"\n   crs:ParametricHighlightSplit="75"\n   crs:SharpenRadius="+1.0"\n   crs:SharpenDetail="25"\n   crs:SharpenEdgeMasking="0"\n   crs:PostCropVignetteAmount="0"\n   crs:GrainAmount="0"\n   crs:ColorNoiseReductionDetail="50"\n   crs:ColorNoiseReductionSmoothness="50"\n   crs:LensProfileEnable="1"\n   crs:LensManualDistortionAmount="0"\n   crs:PerspectiveVertical="0"\n   crs:PerspectiveHorizontal="0"\n   crs:PerspectiveRotate="0.0"\n   crs:PerspectiveScale="100"\n   crs:PerspectiveAspect="0"\n   crs:PerspectiveUpright="0"\n   crs:PerspectiveX="0.00"\n   crs:PerspectiveY="0.00"\n   crs:AutoLateralCA="1"\n   crs:Exposure2012="-0.10"\n   crs:Contrast2012="0"\n   crs:Highlights2012="-100"\n   crs:Shadows2012="+48"\n   crs:Whites2012="+71"\n   crs:Blacks2012="+2"\n   crs:Clarity2012="+29"\n   crs:DefringePurpleAmount="0"\n   crs:DefringePurpleHueLo="30"\n   crs:DefringePurpleHueHi="70"\n   crs:DefringeGreenAmount="0"\n   crs:DefringeGreenHueLo="40"\n   crs:DefringeGreenHueHi="60"\n   crs:Dehaze="+10"\n   crs:ToneMapStrength="0"\n   crs:ConvertToGrayscale="False"\n   crs:ToneCurveName="Medium Contrast"\n   crs:ToneCurveName2012="Linear"\n   crs:CameraProfile="Adobe Standard"\n   crs:CameraProfileDigest="98BA1AFA1155D0472068BB57D3655975"\n   crs:LensProfileSetup="LensDefaults"\n   crs:LensProfileName="Adobe (Canon EF 24-105mm f/4 L IS USM)"\n   crs:LensProfileFilename="Canon EOS-1Ds Mark III (Canon EF 24-105mm f4 L IS USM) - RAW.lcp"\n   crs:LensProfileDigest="F59965C057650927AFD8E60143A071CA"\n   crs:LensProfileDistortionScale="100"\n   crs:LensProfileChromaticAberrationScale="100"\n   crs:LensProfileVignettingScale="100"\n   crs:UprightVersion="151388160"\n   crs:UprightCenterMode="0"\n   crs:UprightCenterNormX="0.5"\n   crs:UprightCenterNormY="0.5"\n   crs:UprightFocalMode="0"\n   crs:UprightFocalLength35mm="35"\n   crs:UprightPreview="False"\n   crs:UprightTransformCount="6"\n   crs:UprightFourSegmentsCount="0"\n   crs:HasSettings="True"\n   crs:CropTop="0.142125"\n   crs:CropLeft="0.048838"\n   crs:CropBottom="0.852893"\n   crs:CropRight="0.89261"\n   crs:CropAngle="0"\n   crs:CropConstrainToWarp="0"\n   crs:HasCrop="True"\n   crs:AlreadyApplied="False"\n   crs:RawFileName="_MG_1601.DNG">\n   <dc:subject>\n    <rdf:Bag>\n     <rdf:li>Dual-ISO</rdf:li>\n    </rdf:Bag>\n   </dc:subject>\n   <xmpMM:History>\n    <rdf:Seq>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:d10cee0e-0500-9843-ac18-38fd7e409480"\n      stEvt:when="2016-05-24T19:25:52-07:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.5 (Windows)"\n      stEvt:changed="/metadata"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:99c42cb0-fb96-964a-a704-5a5b644cc03b"\n      stEvt:when="2016-10-31T13:08:15-07:00"\n      stEvt:softwareAgent="Adobe Photoshop Lightroom 6.7 (Windows)"\n      stEvt:changed="/metadata"/>\n     <rdf:li\n      stEvt:action="derived"\n      stEvt:parameters="saved to new location"/>\n     <rdf:li\n      stEvt:action="saved"\n      stEvt:instanceID="xmp.iid:46e5fbdc-0819-6345-807c-4e3addeb789c"\n      stEvt:when="2020-01-29T14:51:18-08:00"\n      stEvt:softwareAgent="Adobe DNG Converter 9.2 (Windows)"\n      stEvt:changed="/"/>\n    </rdf:Seq>\n   </xmpMM:History>\n   <xmpMM:DerivedFrom\n    stRef:instanceID="xmp.iid:99c42cb0-fb96-964a-a704-5a5b644cc03b"\n    stRef:documentID="8B99E42CA2FB533F6842C19153BD50E7"\n    stRef:originalDocumentID="8B99E42CA2FB533F6842C19153BD50E7"/>\n   <crs:ToneCurve>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>32, 22</rdf:li>\n     <rdf:li>64, 56</rdf:li>\n     <rdf:li>128, 128</rdf:li>\n     <rdf:li>192, 196</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurve>\n   <crs:ToneCurveRed>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveRed>\n   <crs:ToneCurveGreen>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveGreen>\n   <crs:ToneCurveBlue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurveBlue>\n   <crs:ToneCurvePV2012>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012>\n   <crs:ToneCurvePV2012Red>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Red>\n   <crs:ToneCurvePV2012Green>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Green>\n   <crs:ToneCurvePV2012Blue>\n    <rdf:Seq>\n     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>\n    </rdf:Seq>\n   </crs:ToneCurvePV2012Blue>\n   <lr:hierarchicalSubject>\n    <rdf:Bag>\n     <rdf:li>Dual-ISO</rdf:li>\n    </rdf:Bag>\n   </lr:hierarchicalSubject>\n  </rdf:Description>\n </rdf:RDF>\n</x:xmpmeta>\n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                       \n<?xpacket end="w"?>'}

ifds = '{141564: {254: 254, 4, 1, 0, 256: 256, 4, 1, 5568, 257: 257, 4, 1, 3708, 258: 258, 3, 1, 16, 259: 259, 3, 1, 7, 262: 262, 3, 1, 32803, 277: 277, 3, 1, 1, 284: 284, 3, 1, 1, 322: 322, 4, 1, 256, 323: 323, 4, 1, 256, 324: 324, 4, 330, 141894, 325: 325, 4, 330, 143214, 33421: 33421, 3, 2, 131074, 33422: 33422, 1, 4, 33620224, 50710: 50710, 1, 3, 131328, 50711: 50711, 3, 1, 1, 50713: 50713, 3, 2, 65537, 50714: 50714, 5, 1, 144534, 50717: 50717, 3, 1, 40172, 50718: 50718, 5, 2, 144542, 50719: 50719, 5, 2, 144558, 50720: 50720, 5, 2, 144574, 50733: 50733, 4, 1, 0, 50738: 50738, 5, 1, 144590, 50780: 50780, 5, 1, 144598, 50829: 50829, 4, 4, 144606, 51008: 51008, 7, 28, 144622}, 144650: {254: 254, 4, 1, 1, 256: 256, 4, 1, 1024, 257: 257, 4, 1, 576, 258: 258, 3, 3, 144896, 259: 259, 3, 1, 7, 262: 262, 3, 1, 6, 273: 273, 4, 1, 256320, 277: 277, 3, 1, 3, 278: 278, 4, 1, 576, 279: 279, 4, 1, 67436, 284: 284, 3, 1, 1, 529: 529, 5, 3, 144902, 530: 530, 3, 2, 131074, 531: 531, 3, 1, 2, 532: 532, 5, 6, 144926, 50966: 50966, 2, 20, 144974, 50967: 50967, 2, 4, 3288633, 50969: 50969, 1, 16, 144994, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 145010}, 145036: {33434: 33434, 5, 1, 145390, 33437: 33437, 5, 1, 145398, 34850: 34850, 3, 1, 1, 34855: 34855, 3, 1, 100, 34864: 34864, 3, 1, 2, 34866: 34866, 4, 1, 100, 36864: 36864, 7, 4, 808661552, 36867: 36867, 2, 20, 145406, 36868: 36868, 2, 20, 145426, 37377: 37377, 10, 1, 145446, 37378: 37378, 5, 1, 145454, 37380: 37380, 10, 1, 145462, 37381: 37381, 5, 1, 145470, 37383: 37383, 3, 1, 5, 37385: 37385, 3, 1, 16, 37386: 37386, 5, 1, 145478, 37521: 37521, 2, 3, 14641, 37522: 37522, 2, 3, 14641, 41486: 41486, 5, 1, 145486, 41487: 41487, 5, 1, 145494, 41488: 41488, 3, 1, 3, 41985: 41985, 3, 1, 0, 41986: 41986, 3, 1, 1, 41987: 41987, 3, 1, 1, 41990: 41990, 3, 1, 0, 42033: 42033, 2, 13, 145502, 42034: 42034, 5, 4, 145516, 42036: 42036, 2, 23, 145548, 42037: 42037, 2, 11, 145572}, 8: {254: 254, 4, 1, 1, 256: 256, 4, 1, 256, 257: 257, 4, 1, 144, 258: 258, 3, 3, 698, 259: 259, 3, 1, 1, 262: 262, 3, 1, 2, 271: 271, 2, 6, 704, 272: 272, 2, 13, 710, 273: 273, 4, 1, 145728, 274: 274, 3, 1, 1, 277: 277, 3, 1, 3, 278: 278, 4, 1, 144, 279: 279, 4, 1, 110592, 284: 284, 3, 1, 1, 305: 305, 2, 34, 724, 306: 306, 2, 20, 758, 330: 330, 4, 2, 778, 700: 700, 1, 12232, 786, 34665: 34665, 4, 1, 145036, 37393: 37393, 4, 1, 0, 50706: 50706, 1, 4, 1025, 50707: 50707, 1, 4, 257, 50708: 50708, 2, 13, 13018, 50721: 50721, 10, 9, 13032, 50722: 50722, 10, 9, 13104, 50727: 50727, 5, 3, 13176, 50728: 50728, 5, 3, 13200, 50730: 50730, 10, 1, 13224, 50731: 50731, 5, 1, 13232, 50732: 50732, 5, 1, 13240, 50734: 50734, 5, 1, 13248, 50735: 50735, 2, 13, 13256, 50736: 50736, 5, 4, 13270, 50739: 50739, 5, 1, 13302, 50740: 50740, 1, 7786, 13310, 50778: 50778, 3, 1, 17, 50779: 50779, 3, 1, 21, 50781: 50781, 1, 16, 21096, 50932: 50932, 2, 10, 21112, 50933: 50933, 4, 1, 145584, 50936: 50936, 2, 15, 21122, 50937: 50937, 4, 3, 21138, 50938: 50938, 11, 8100, 21150, 50939: 50939, 11, 8100, 53550, 50941: 50941, 4, 1, 0, 50942: 50942, 2, 35, 85950, 50964: 50964, 10, 9, 85986, 50965: 50965, 10, 9, 86058, 50966: 50966, 2, 20, 86130, 50967: 50967, 2, 4, 3288633, 50969: 50969, 1, 16, 86150, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 86166, 50981: 50981, 4, 3, 86192, 50982: 50982, 11, 13824, 86204, 51041: 51041, 12, 6, 141500, 51111: 51111, 1, 16, 141548}}'

saved_ifds = '{111377: {254: 254, 4, 1, 0, 256: 256, 4, 1, 5568, 257: 257, 4, 1, 3708, 258: 258, 3, 1, 16, 259: 259, 3, 1, 7, 262: 262, 3, 1, 32803, 277: 277, 3, 1, 1, 284: 284, 3, 1, 1, 322: 322, 4, 1, 256, 323: 323, 4, 1, 256, 324: 324, 4, 330, 111707, 325: 325, 4, 330, 18284916, 33421: 33421, 3, 2, 131074, 33422: 33422, 1, 4, 33620224, 50710: 50710, 1, 3, 131328, 50711: 50711, 3, 1, 1, 50713: 50713, 3, 2, 65537, 50714: 50714, 5, 1, 18286236, 50717: 50717, 3, 1, 40172, 50718: 50718, 5, 2, 18286244, 50719: 50719, 5, 2, 18286260, 50720: 50720, 5, 2, 18286276, 50733: 50733, 4, 1, 0, 50738: 50738, 5, 1, 18286292, 50780: 50780, 5, 1, 18286300, 50829: 50829, 4, 4, 18286308, 51008: 51008, 7, 28, 18286324}, 18286352: {254: 254, 4, 1, 1, 256: 256, 4, 1, 1024, 257: 257, 4, 1, 576, 258: 258, 3, 3, 18286598, 259: 259, 3, 1, 7, 262: 262, 3, 1, 6, 273: 273, 4, 1, 18286604, 277: 277, 3, 1, 3, 278: 278, 4, 1, 576, 279: 279, 4, 1, 67436, 284: 284, 3, 1, 1, 529: 529, 5, 3, 18354040, 530: 530, 3, 2, 131074, 531: 531, 3, 1, 2, 532: 532, 5, 6, 18354064, 50966: 50966, 2, 20, 18354112, 50967: 50967, 2, 4, 3288633, 50969: 50969, 1, 16, 18354132, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 18354148}, 18366407: {33434: 33434, 5, 1, 18366761, 33437: 33437, 5, 1, 18366769, 34850: 34850, 3, 1, 1, 34855: 34855, 3, 1, 100, 34864: 34864, 3, 1, 2, 34866: 34866, 4, 1, 100, 36864: 36864, 7, 4, 808661552, 36867: 36867, 2, 20, 18366777, 36868: 36868, 2, 20, 18366797, 37377: 37377, 10, 1, 18366817, 37378: 37378, 5, 1, 18366825, 37380: 37380, 10, 1, 18366833, 37381: 37381, 5, 1, 18366841, 37383: 37383, 3, 1, 5, 37385: 37385, 3, 1, 16, 37386: 37386, 5, 1, 18366849, 37521: 37521, 2, 3, 14641, 37522: 37522, 2, 3, 14641, 41486: 41486, 5, 1, 18366857, 41487: 41487, 5, 1, 18366865, 41488: 41488, 3, 1, 3, 41985: 41985, 3, 1, 0, 41986: 41986, 3, 1, 1, 41987: 41987, 3, 1, 1, 41990: 41990, 3, 1, 0, 42033: 42033, 2, 13, 18366873, 42034: 42034, 5, 4, 18366886, 42036: 42036, 2, 23, 18366918, 42037: 42037, 2, 11, 18366941}, 8: {254: 254, 4, 1, 1, 256: 256, 4, 1, 256, 257: 257, 4, 1, 144, 258: 258, 3, 3, 698, 259: 259, 3, 1, 1, 262: 262, 3, 1, 2, 271: 271, 2, 6, 704, 272: 272, 2, 13, 710, 273: 273, 4, 1, 723, 274: 274, 3, 1, 1, 277: 277, 3, 1, 3, 278: 278, 4, 1, 144, 279: 279, 4, 1, 110592, 284: 284, 3, 1, 1, 305: 305, 2, 34, 111315, 306: 306, 2, 20, 111349, 330: 330, 4, 2, 111369, 700: 700, 1, 12232, 18354174, 34665: 34665, 4, 1, 18366407, 37393: 37393, 4, 1, 0, 50706: 50706, 1, 4, 1025, 50707: 50707, 1, 4, 257, 50708: 50708, 2, 13, 18366952, 50721: 50721, 10, 9, 18366965, 50722: 50722, 10, 9, 18367037, 50727: 50727, 5, 3, 18367109, 50728: 50728, 5, 3, 18367133, 50730: 50730, 10, 1, 18367157, 50731: 50731, 5, 1, 18367165, 50732: 50732, 5, 1, 18367173, 50734: 50734, 5, 1, 18367181, 50735: 50735, 2, 13, 18367189, 50736: 50736, 5, 4, 18367202, 50739: 50739, 5, 1, 18367234, 50740: 50740, 1, 7786, 18367242, 50778: 50778, 3, 1, 17, 50779: 50779, 3, 1, 21, 50781: 50781, 1, 16, 18375028, 50932: 50932, 2, 10, 18375044, 50933: 50933, 4, 1, 145584, 50936: 50936, 2, 15, 18375054, 50937: 50937, 4, 3, 18375069, 50938: 50938, 11, 8100, 18375081, 50939: 50939, 11, 8100, 18407481, 50941: 50941, 4, 1, 0, 50942: 50942, 2, 35, 18439881, 50964: 50964, 10, 9, 18439916, 50965: 50965, 10, 9, 18439988, 50966: 50966, 2, 20, 18440060, 50967: 50967, 2, 4, 3288633, 50969: 50969, 1, 16, 18440080, 50970: 50970, 4, 1, 2, 50971: 50971, 2, 26, 18440096, 50981: 50981, 4, 3, 18440122, 50982: 50982, 11, 13824, 18440134, 51041: 51041, 12, 6, 18495430, 51111: 51111, 1, 16, 18495478}}'

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
    yield DNG(str(data_folder_path / 'dng' / 'sequence' / 'dng_canon_6d_0001.dng'))


@pytest.fixture()
def meta_image_canon_6d(data_folder_path):
    from brilliantimagery.meta_image import MetaImage
    yield MetaImage(str(data_folder_path / 'dng' / 'sequence' / 'dng_canon_6d_0001.dng'))


@pytest.fixture()
def dng_pixel2(data_folder_path):
    from brilliantimagery.dng import DNG
    yield DNG(str(data_folder_path / 'dng' / 'dng_Pixel2.dng'))


@pytest.fixture()
def post_save_ifds():
    yield saved_ifds


@pytest.fixture()
def numpy_cropped_canon_6d(data_folder_path):
    image = np.load(str(data_folder_path / 'dng' / 'test_image_canon_6d_cropped.npy'))
    rendered_area = [1500 / 5030, 1450 / 3350, (1500 + 700) / 5030, (1450 + 760) / 3350]
    yield image, rendered_area


@pytest.fixture()
def numpy_thumbnail_canon_6d(data_folder_path):
    yield np.load(str(data_folder_path / 'dng' / 'test_image_canon_6d_thumb.npy'))


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

    tiles = pickle.load(open(str(data_folder_path / 'dng' / 'compressed_tiles.p'), 'rb'))

    yield rectangle, tiles


@pytest.fixture()
def copied_dng_canon_6d(data_folder_path, dng_canon_6d, tmpdir):
    import shutil
    from brilliantimagery.dng import DNG

    # shutil.copy(str(str(data_folder_path / 'dng_canon_6d.dng')), str(tmpdir / 'dng_canon_6d.dng'))
    shutil.copy(str(data_folder_path / 'dng' / 'sequence' / 'dng_canon_6d_0001.dng'),
                str(tmpdir / 'dng_canon_6d_0001.dng'))
    yield DNG(str(tmpdir / 'dng_canon_6d_0001.dng'))


@pytest.fixture()
def dng_rendered_to_rgb_even_offsets(dng_canon_6d, data_folder_path):
    import numpy as np

    active_area_offset = (28, 62)
    rectangle = [100, 100, 500, 400]

    # dng_canon_6d.parse()
    dng_canon_6d.get_default_shape()
    dng_canon_6d._get_tile_or_strip_bytes(rectangle)
    ifd = dng_canon_6d._used_fields

    with open(str(data_folder_path / 'dng' / 'renderer_render_raw_even_even.npy'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'renderer_render_raw_odd_even.npy'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'renderer_render_raw_even_odd.npy'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'renderer_render_thumbnail_even.npy'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'renderer_render_thumbnail_odd.npy'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'raw_data_to_rgb_0112_even_offset.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'raw_data_to_rgb_0112_odd_offset.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'raw_data_to_rgb_1021_even_offset.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'unscaled_raw_data_w_2x2_mask_1_sample_per_pix.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'unscaled_raw_data_w_2x2_mask_1_sample_per_pix_odd.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'unscaled_raw_data_w_3_sample_per_pix.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'unscaled_raw_data_w_linearization.np'), 'rb') as f:
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

    with open(str(data_folder_path / 'dng' / 'unpacked_compressed_tiles.npy'), 'rb') as f:
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
