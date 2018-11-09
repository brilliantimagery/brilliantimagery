from os import listdir
from os.path import isfile, join

from ._stabilize import Stabilizer
from ._ramp import Ramper
from meta_image import MetaImage


class Sequence:
    def __init__(self, path):
        self._path = path
        self._ordered_capture_times = []
        self._images = dict()
        files = [join(self._path, f) for f in listdir(self._path) if
                 isfile(join(self._path, f)) and f[-3:].lower() == 'dng']
        for path in files:
            file = MetaImage(path)
            self._images[file.get_capture_datetime()] = file

    def ramp(self, rectangle):
        ramper = Ramper(self._images, rectangle)

    def stabilize(self, rectangle, max_pix_of_misalignment=5, keep_brightness=False):
        stabilizer = Stabilizer(self._images, rectangle, max_pix_of_misalignment)
        stabilizer.find_misalignments(keep_brightness)
        stabilizer.update_xmp_attributes()
        self._images = stabilizer.images

    def store_xmp_field(self):
        for image in self._images.values():
            image.store_xmp_field()

    def save(self):
        for image in self._images.values():
            image.store_xmp_field()
            image.save()
