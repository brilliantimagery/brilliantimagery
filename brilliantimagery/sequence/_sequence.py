# from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor
import concurrent.futures
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from typing import List

import numpy as np
from tqdm import tqdm

from brilliantimagery.sequence._stabilize import Stabilizer
from brilliantimagery.sequence._ramp import Ramper
from brilliantimagery.meta_image import MetaImage


class Sequence:
    """
    A class used to represent a sequence of images and process them as such.

    The two primary objectives are to stabilize shaky image sequences and
    to smooth transitions between different settings adjusted in photo
    editing software such as exposure and contrast.

    Stabilization is accomplished by adjusting each images crop. Additionally,
    it's assumed that each image is cropped in the same way so it's best
    practice to copy the first images crop adjustment and paste them to the
    rest of the images.

    Transitions are smoothed or ramped based ok "key frames" or reference
    frames that the interstitial frames are based off of by linearly
    extrapolating between key frames. Key frames are denoted by rating them
    with 3 stars.
    """

    def __init__(self, path: str):
        """
        Initializes an image sequence representation.

        :param str path: Path to the folder containing the relevant images.
        """
        tqdm.monitor_interval = 0
        self.path = path
        self._ordered_capture_times = []
        self._images = dict()
        files = [join(self.path, f) for f in listdir(self.path) if
                 isfile(join(self.path, f)) and f.lower().endswith('dng')]

        ###################### FASTER ##########################################
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     images = list(tqdm(executor.map(MetaImage, files),
        #                        total=len(files),
        #                        desc='Parsing files: '))
        ###################### Avoids apparend pytest/pycharm # bug ##############
        # images = [MetaImage(f) for f in files]
        # self.is_single_threaded = True
        ###################### End bug section #################################

        # since dict orders are guarantied, sort it up front before storing it
        # TODO: if the camera's numbers reset and pics end up with the
        #  name time then they'll end up out of order
        labeled_images = Sequence._parse_images(files)
        # labeled_images = {f'{i.get_capture_datetime()} {i.get_path()}': i for i in images}
        image_keys = sorted(list(labeled_images))
        self._images = {k: labeled_images[k] for k in image_keys}

    def get_reference_image(self, rectangle=[0, 0, 1, 1], sub_image_type='thumbnail',
                            index_order='cxy'):
        """
        Gets a reference image for the sequence.

        The first image in the image sequence is used as the reference.

        :param rectangle: The bounding box of the portion of the image that's
            to be rendered. In the format X1, Y1, X2, Y2 where:

            * X1 is the x position of the top left corner,
            * Y1 is the y position of the top left corner,
            * X2 is the x position of the bottom right corner,
            * Y2 is the y position of the top right corner.

            The numbers should be in the range 0 - 1, representing the
            percent of the way across the image that the position is.
        :type rectangle: list[int or float]
        :param str sub_image_type: 'thumbnail' or 'RAW' depending on which
            is to be rendered. If no thumbnail is embedded within the
            image then the raw image will be rendered.
        :param str index_order: The order of the array indexes. The two
        options are 'cxy' and 'yxc'.

            * 'cxy' equates to:

                index 0 being color channel,
                index 1 being pixel x position,
                index 2 being pixel y position

            * 'yxc' equates to:

                index 0 being pixel y position,
                index 1 being pixel x position,
                index 2 being color channel

        Returns: A 3D float array holding the rendered image where each array
        index represents the information specified by the 'index_order'
        attribute.
        """

        reference_image = self._images[next(iter(self._images))]
        # reference_image = self._images[list(self._images)[0]]
        reference_image.parse()
        image_array = reference_image.get_image(rectangle, sub_image_type)

        if index_order.lower() == 'cxy':
            return image_array
        elif index_order.lower() == 'yxc':
            shape = image_array.shape
            image_array = np.reshape(image_array, image_array.size, 'C')
            image_array = np.reshape(image_array, (shape[2], shape[1], shape[0]), 'F')
            return image_array
        else:
            raise ValueError('"index_order" must either be "cxy"or "yxc".')

    def ramp_minus_exmpsure(self):
        """
        Ramps the edited image setting other than the exposure.

        Won't adjust the exposure and is faster
        then also ramping exposure since image rendering isn't required.

        :return: None
        """
        ramper = Ramper(self._images)
        ramper.ramp_minus_exposure()

    def ramp_exposure(self, rectangle):
        """
        Ramps the image exposure but nothing else.

        :return: None
        """
        ramper = Ramper(self._images)
        ramper.ramp_exposure(rectangle)

    def ramp(self, rectangle):
        """
        Ramps all user edited settings.

        :return: None
        """
        ramper = Ramper(self._images)
        ramper.ramp_exposure(rectangle)
        ramper.ramp_minus_exposure()

    def ramp_and_stabilize(self, rectangle):
        """
        Ramps all user edited setting and stabilizes the sequence.

        :return: None
        """
        self.stabilize(rectangle, keep_brightness=True)
        self.ramp(rectangle)

    def ramp_minus_exposure_and_stabilize(self, rectangle):
        """
        Ramps all setting other than exposure and stabilizes the sequence.

        :return: None
        """

        self.stabilize(rectangle)
        self.ramp_minus_exmpsure(rectangle)

    def ramp_exposure_and_stabilize(self, rectangle):
        """
        Ramps only exposureand stabilizes the sequence.

        :return: None
        """
        self.stabilize(rectangle, keep_brightness=True)
        self.ramp_exposure(rectangle)

    def stabilize(self, rectangle, keep_brightness=False):
        """
        Stabilizes the image sequence but adjusts nothing else.

        :return: None
        """
        if list(self._images.values())[0].misalignment:
            return
        stabilizer = Stabilizer(self._images, rectangle)
        stabilizer.find_misalignments(keep_brightness)
        stabilizer.update_crop_xmp_attributes()

    # TODO: this isn't tested
    def save(self):
        """
        Saves each images ramp or crop changes.

        :return: None
        """
        for image in tqdm(self._images.values(), desc='Updating files: ', total=len(self._images)):
            image.store_xmp_field()
            image.save()

    def get_misalignments(self):
        return {os.path.basename(image.get_path()).lower(): image.misalignment
                for image in self._images}

    def get_brightnesses(self):
        return {os.path.basename(image.get_path()).lower(): image.brightness
                for image in self._images}

    def set_misalignments(self, misalignments):
        for image in self._images:
            file_name = os.path.basename(image.get_path())
            image.misalignment = misalignments.get(file_name, [0, 0])

    def set_brightnesses(self, brightnesses):
        for image in self._images:
            file_name = os.path.basename(image.get_path())
            image.brightness = brightnesses.get(file_name, 0)

    def parse_sequence(self):
        files = [join(self.path, f) for f in listdir(self.path) if
                 isfile(join(self.path, f)) and f.lower().endswith('dng')]

        labeled_images = Sequence._parse_images(files)

        # This seems hackey but it's allowing threading
        for name, image in self._images.items():
            image.image = labeled_images[name].image

    @staticmethod
    def _parse_images(images: List[str]):
        with concurrent.futures.ProcessPoolExecutor() as executer:
            images = list(tqdm(executer.map(MetaImage, images)))

        return {Sequence._name_image(i): i for i in images}

    @staticmethod
    def _name_image(image: MetaImage):
        return f'{image.get_capture_datetime()} {image.get_path()}'
