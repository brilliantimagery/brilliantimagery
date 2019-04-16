import timeit


def test_decode_time():
    number = 10

    setup = '''
from pathlib import Path

import numpy as np

from BrilliantImagery.dng import DNG
from BrilliantImagery.dng import _renderer

active_area_offset = (1787, 1646)
rectangle = [1859, 1684, 2558, 2444]
path = str(Path.cwd().parent / 'data' / 'test_image_canon_6d.dng')

dng = DNG(path)
dng.parse()
dng.default_shape()
dng._get_tile_or_strip_bytes(rectangle)
ifd = dng._used_fields

    '''

    run = '''
_renderer.render(ifd, rectangle, active_area_offset)
    '''

    print('Total _renderer.render time:', timeit.timeit(run, setup, number=number) / number)
