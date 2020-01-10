cpdef render(ifd, rectangle, active_area_offset)

cdef float[:,:,:] _raw_to_rgb(ifd, float[:,:] raw_scaled, active_area_offset)

cdef int[:,:,:] _clip_to_rendered_rectangle(ifd, int[:,:,:] raw_image)

cdef float[:,:,:] _set_blacks_whites_scale_and_clip(ifd, int[:,:,:] raw_image, tuple active_area_offset)

cdef float _rescale_and_clip(float color_value, int black_level, int white_level)

cdef int[:,:,:] _unpack_section_data(ifd)
