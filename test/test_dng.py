import time

import numpy as np

from dng import DNG
import ppm

t = time.time()
# print('start', t)
img = DNG('test_input.dng')
# img = dng.DNG('E:\\Pictures\\2016\\2016-12-19\\_MG_0121.dng')
print('one', time.time() - t, 'and more')
image = np.asarray(img.get_image(rectangle=[0.0, 0.0, 0.3, 0.3]), dtype=np.float32) * 255
# image = np.asarray(img.get_image(rectangle=[0.5, 0.65, 0.7, 0.85]), dtype=np.float32) * 255
# img.update_xmp_data()
print('two', time.time() - t, 'and more')
ppm.save(image.astype(dtype=np.int), 'output.ppm', 255)
# print('done')
