# distutils: language=c++
import numpy as np

from BrilliantImagery import ljpeg

def render(ifd, rectangle, active_area_offset):
    if ifd['photometric_interpretation'] == 2:
        if ifd['compression'] == 1:
            assert len(ifd['section_bytes']) == 1
            raw_image = _unpack_strip_data(ifd)
            return raw_image[:, ifd['rendered_rectangle'][0]: ifd['rendered_rectangle'][2],
                             ifd['rendered_rectangle'][1]: ifd['rendered_rectangle'][3]].base

    elif ifd['photometric_interpretation'] in [32803, 34892]:
        # print(ifd)
        assert 'white_level' in ifd
        assert len(ifd['black_level']) in [1, 3, 4]      # otherwise _render_utils.black_white_rescale breaks
        assert ifd['bits_per_sample'][0] in [8, 16]
        if 'black_level' not in ifd and ifd['cfa_repeat_pattern_dim'] == [2, 2]:
            ifd['black_level'] = [0, 0, 0, 0]
            ifd['black_level_repeat_dim'] = [2, 2]
        if len(ifd['black_level']) == 1 and ifd['cfa_repeat_pattern_dim'] == [2, 2]:
            ifd['black_level'] = ifd['black_level'] * len(ifd['cfa_pattern'])
            ifd['black_level_repeat_dim'] = [2, 2]
        if 'black_level_delta_H' not in ifd:
            ifd['black_level_delta_H'] = [0] * ifd['image_width']
        if 'black_level_delta_V' not in ifd:
            ifd['black_level_delta_V'] = [0] * ifd['image_length']

        if 'tile_offsets' in ifd:
            raw_image = _unpack_tile_data(ifd)
        elif 'strip_offsets' in ifd:
            raw_image = _unpack_strip_data(ifd)
        raw_image = _clip_to_rendered_rectangle(ifd, raw_image)
        raw_scaled = _set_blacks_whites_scale_and_clip(ifd, raw_image, active_area_offset)
        if ifd['photometric_interpretation'] == 32803:
            raw_scaled = _raw_to_rgb(ifd, raw_scaled[0,:,:], active_area_offset)
        return raw_scaled.base


cdef float[:,:,:] _raw_to_rgb(ifd, float[:,:] raw_scaled, active_area_offset):
    cdef int width = raw_scaled.shape[0] - 1
    cdef int height = raw_scaled.shape[1] - 1

    cdef float[:,:,:] rgb_image_middle_pixel_value = np.full((3, raw_scaled.shape[0], raw_scaled.shape[1]),
                                                             -1, dtype=np.float32)
    cdef float[:,:,:] rgb_image = np.copy(rgb_image_middle_pixel_value)

    cdef int ix
    cdef int iy
    cdef int ic
    cdef list cfa_pattern = ifd['cfa_pattern']
    cdef list cfa_repeat_pattern_dim = ifd['cfa_repeat_pattern_dim']
    for ix in range(width + 1):
        for iy in range(height + 1):
            ic = cfa_pattern[((iy + active_area_offset[1]) % cfa_repeat_pattern_dim[1] * cfa_repeat_pattern_dim[0]
                              + (ix + active_area_offset[0]) % cfa_repeat_pattern_dim[0])]
            rgb_image_middle_pixel_value[ic, ix, iy] = raw_scaled[ix, iy]

    cdef float sample = 0
    cdef int n_samples = 0
    cdef int dx
    cdef int dy
    for iy in range(height+1):
        for ix in range(width+1):
            for ic in range(3):
                if rgb_image_middle_pixel_value[ic, ix, iy] != -1:
                    rgb_image[ic, ix, iy] = rgb_image_middle_pixel_value[ic, ix, iy]
                else:
                    sample = 0
                    n_samples = 0
                    if 0 < ix < width and 0 < iy < height:
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif ix == 0 and iy == 0:
                        for dy in range(0, 2):
                            for dx in range(0, 2):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif 0 < ix < width and iy == 0:
                        for dy in range(0, 2):
                            for dx in range(-1, 2):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif ix == width and iy == 0:
                        for dy in range(0, 2):
                            for dx in range(-1, 1):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif ix == width and 0 < iy < height:
                        for dy in range(-1, 2):
                            for dx in range(-1, 1):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif ix == width and iy == height:
                        for dy in range(-1, 1):
                            for dx in range(-1, 1):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif 0 < ix < width and iy == height:
                        for dy in range(-1, 1):
                            for dx in range(-1, 2):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif ix == 0 and iy == height:
                        for dy in range(-1, 1):
                            for dx in range(0, 2):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    elif ix == 0 and 0 < iy < height:
                        for dy in range(-1, 2):
                            for dx in range(0, 2):
                                if rgb_image_middle_pixel_value[ic, ix + dx, iy + dy] != -1:
                                    sample += rgb_image_middle_pixel_value[ic, ix + dx, iy + dy]
                                    n_samples += 1
                    rgb_image[ic, ix, iy] = sample / n_samples

    return rgb_image


cdef int[:,:,:] _clip_to_rendered_rectangle(ifd, int[:,:,:] raw_image):
    return raw_image[:,
                     (ifd['rendered_rectangle'][0] - ifd['rendered_section_bounding_box'][0]):
                     (ifd['rendered_rectangle'][2] - ifd['rendered_section_bounding_box'][0]),
                     (ifd['rendered_rectangle'][1] - ifd['rendered_section_bounding_box'][1]):
                     (ifd['rendered_rectangle'][3] - ifd['rendered_section_bounding_box'][1])]


cdef float[:,:,:] _set_blacks_whites_scale_and_clip(ifd, int[:,:,:] raw_image, tuple active_area_offset):
    cdef int ix
    cdef int iy
    cdef int ic
    cdef float[:,:,:] raw_scaled = np.zeros_like(raw_image, dtype=np.float32)
    cdef list black_level = ifd['black_level']
    cdef list black_level_repeat_dim = ifd['black_level_repeat_dim']
    cdef list black_level_delta_v = ifd['black_level_delta_V']
    cdef list black_level_delta_h = ifd['black_level_delta_H']
    cdef list white_level = ifd['white_level']
    cdef list linearization_table = []
    cdef int black
    cdef int white

    if 'linearization_table' in ifd:
        linearization_table = ifd['linearization_table']
        for ic in range(raw_image.shape[0]):
            for iy in range(raw_image.shape[2]):
                for ix in range(raw_image.shape[1]):
                    if raw_image[ic, ix, iy] > len(linearization_table):
                        raw_image[ic, ix, iy] = linearization_table[-1]
                    else:
                        raw_image[ic, ix, iy] = linearization_table[raw_image[ic, ix, iy]]

    # TODO Bug assumes ifd['black_level_repeat_dim'] == [2, 2]
    if ifd['black_level_repeat_dim'] == [2, 2] and ifd['samples_per_pix'] == 1:
        assert len(ifd['white_level']) == 1
        if active_area_offset[0] % ifd['cfa_repeat_pattern_dim'][0] == 1:
            black_level = [black_level[1], black_level[0], black_level[3], black_level[2]]
        if active_area_offset[1] % ifd['cfa_repeat_pattern_dim'][1] == 1:
            black_level = [black_level[2], black_level[3], black_level[0], black_level[1]]
        for iy in range(raw_scaled.shape[2]):
            for ix in range(raw_scaled.shape[1]):
                black = (black_level[iy % black_level_repeat_dim[0] * black_level_repeat_dim[1]
                                     + ix % black_level_repeat_dim[1]]
                         + black_level_delta_h[active_area_offset[0] + ix]
                         + black_level_delta_v[active_area_offset[1] + iy])
                raw_scaled[0, ix, iy] = _rescale_and_clip(raw_image[0, ix, iy], black, white_level[0])
    elif black_level_repeat_dim == [1, 1] and ifd['samples_per_pix'] == 3:
        for ic in range(raw_scaled.shape[0]):
            for iy in range(raw_scaled.shape[2]):
                for ix in range(raw_scaled.shape[1]):
                    black = (black_level[ic]
                             + black_level_delta_h[active_area_offset[0] + ix]
                             + black_level_delta_v[active_area_offset[1] + iy])
                    raw_scaled[ic, ix, iy] = _rescale_and_clip(raw_image[ic, ix, iy], black, white_level[ic])
    else:
        print(ifd)
        assert False

    return raw_scaled


cdef float _rescale_and_clip(float color_value, int black_level, int white_level):
    color_value = (color_value - black_level) / (white_level - black_level)
    if color_value < 0:
        color_value = 0
    if color_value > 1:
        color_value = 1

    return color_value


cdef int[:,:,:] _unpack_tile_data(ifd):
    # print(ifd)
    cdef int samples_per_pix = ifd['samples_per_pix']
    cdef int n_tiles_wide = max([n[0] for n in ifd['section_bytes'].keys()]) + 1
    cdef int n_tiles_long = max([n[1] for n in ifd['section_bytes'].keys()]) + 1
    cdef tuple section_number
    cdef int[:] section_bytes
    cdef int tile_width
    cdef int tile_length
    cdef int[:,:,:] image_data
    cdef int[:,:,:] image_data_reshaped
    cdef int nominal_tile_width = ifd['tile_width']
    cdef int nominal_tile_length = ifd['tile_length']
    cdef int compression = ifd['compression']
    cdef int[:,:,:] raw_scaled = np.empty((samples_per_pix,
                                           ifd['rendered_section_bounding_box'][2]
                                           - ifd['rendered_section_bounding_box'][0],
                                           ifd['rendered_section_bounding_box'][3]
                                           - ifd['rendered_section_bounding_box'][1]),
                                          dtype=np.intc)

    for section_number, section_bytes in ifd['section_bytes'].items():
        if section_number[0] < n_tiles_wide - 1:
            tile_width = nominal_tile_width
        else:
            tile_width = raw_scaled.shape[1] - nominal_tile_width * (n_tiles_wide - 1)

        if section_number[1] < n_tiles_long - 1:
            tile_length = nominal_tile_length
        else:
            tile_length = raw_scaled.shape[2] - nominal_tile_length * (n_tiles_long - 1)

        if compression == 7:
            image_data = ljpeg.decode(section_bytes)
        else:
            assert False

        image_data_reshaped = np.reshape(image_data,
                                         (samples_per_pix, nominal_tile_width, nominal_tile_length),
                                         order='F')
        raw_scaled[:,
                   section_number[0] * nominal_tile_width: (section_number[0]+1) * nominal_tile_width,
                   section_number[1] * nominal_tile_length: (section_number[1]+1) * nominal_tile_length] = \
            image_data_reshaped[:, :tile_width, :tile_length]

    return raw_scaled


# TODO: consolidate with _unpack_jpeg_data
cdef int[:, :, :] _unpack_strip_data(ifd):
    cdef int samples_per_pix = ifd['samples_per_pix']
    cdef int[:,:,:] raw_scaled = np.empty((3,
                                           ifd['rendered_section_bounding_box'][2]
                                         - ifd['rendered_section_bounding_box'][0],
                                         ifd['rendered_section_bounding_box'][3]
                                         - ifd['rendered_section_bounding_box'][1]),
                                        dtype=np.intc)
    cdef int n_strips_wide = 1
    cdef int n_strips_long = max([n[1] for n in ifd['section_bytes'].keys()]) + 1
    cdef tuple section_number
    cdef int[:] section_bytes
    cdef int[:, :, :] section_bytes_reshaped
    cdef int section_width = ifd['image_width']
    cdef int section_length = ifd['image_length']

    for section_number, section_bytes in ifd['section_bytes'].items():
        return np.reshape(section_bytes, (3, section_width, section_length), order='F')

#cython: profile=True
#cython: linetrace=True
