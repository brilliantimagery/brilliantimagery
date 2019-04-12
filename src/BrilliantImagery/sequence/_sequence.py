# from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor
import concurrent.futures
from os import listdir
from os.path import isfile, join

from tqdm import tqdm

from ._stabilize import Stabilizer
from ._ramp import Ramper
from BrilliantImagery.meta_image import MetaImage


class Sequence:
    def __init__(self, path):
        tqdm.monitor_interval = 0
        self._path = path
        self._ordered_capture_times = []
        self._images = dict()
        files = [join(self._path, f) for f in listdir(self._path) if
                 isfile(join(self._path, f)) and f[-3:].lower() == 'dng']

        ###################### FASTER ##########################################
        with concurrent.futures.ProcessPoolExecutor() as executor:
            images = list(tqdm(executor.map(MetaImage, files), total=len(files), desc='Parsing files: '))

        ###################### Avoids apparend pytest/pycharm # bug ##############
        # images = [MetaImage(f) for f in files]
        ###################### End bug section #################################

        self._images = {i.get_capture_datetime(): i for i in images}

    def ramp_minus_exmpsure(self):
        ramper = Ramper(self._images)
        ramper.ramp_minus_exposure()

    def ramp_exposure(self, rectangle):
        ramper = Ramper(self._images)
        ramper.ramp_exposure(rectangle)

    def ramp(self, rectangle):
        ramper = Ramper(self._images)
        ramper.ramp_exposure(rectangle)
        ramper.ramp_minus_exposure()

    def ramp_and_stabilize(self, rectangle):
        self.stabilize(rectangle, keep_brightness=True)
        self.ramp(rectangle)

    def stabilize(self, rectangle, keep_brightness=False):
        stabilizer = Stabilizer(self._images, rectangle)
        stabilizer.find_misalignments(keep_brightness)
        stabilizer.update_crop_xmp_attributes()

    # TODO: this isn't tested
    def save(self):
        for image in tqdm(self._images.values(), desc='Updating files: ', total=len(self._images)):
            image.store_xmp_field()
            image.save()
