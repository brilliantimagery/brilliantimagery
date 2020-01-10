from BrilliantImagery.dng._renderer import render as _render
from BrilliantImagery.dng._renderer cimport _raw_to_rgb as rtr
from BrilliantImagery.dng._renderer cimport _clip_to_rendered_rectangle as ctrr
from BrilliantImagery.dng._renderer cimport _set_blacks_whites_scale_and_clip as sbwsac
from BrilliantImagery.dng._renderer cimport _rescale_and_clip as rac
from BrilliantImagery.dng._renderer cimport _unpack_section_data as usd

def render(ifd, rectangle, active_area_offset):
    return _render(ifd, rectangle, active_area_offset)

cpdef _raw_to_rgb(ifd, float[:,:] raw_scaled, active_area_offset):
    return rtr(ifd, raw_scaled, active_area_offset)

cpdef int[:,:,:] _clip_to_rendered_rectangle(ifd, int[:,:,:] raw_image):
    return ctrr(ifd, raw_image)

cpdef float[:,:,:] _set_blacks_whites_scale_and_clip(ifd, int[:,:,:] raw_image, tuple active_area_offset):
    return sbwsac(ifd, raw_image, active_area_offset)

cpdef float _rescale_and_clip(float color_value, int black_level, int white_level):
    return rac(color_value, black_level, white_level)

cpdef int[:,:,:] _unpack_section_data(ifd):
    return usd(ifd)
