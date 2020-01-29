import math
import multiprocessing

from tqdm import tqdm


class Ramper:

    # _BLACKS_EXPOSURE_COMPENSATION = 15 #higher number makes brighter images (higher iso) darker
    _EARLY_MID_TRANSITION = 221
    _EARLY_BLACKS_EXPOSURE_COMPENSATION = -15

    _MID_LATE_TRANSITION = 326
    _MID_BLACKS_EXPOSURE_COMPENSATION = 0

    _LATE_BLACKS_EXPOSURE_COMPENSATION = 20

    def __init__(self, images):
        self._images = images
        self._key_frames = []
        self._key_frame_gaps = []

        self._sorted_times = sorted(self._images.keys())
        example_image = self._images[self._sorted_times[0]]
        xmp_attributes = example_image.get_xmp()
        possible_xmp = {attr: prop.is_ramped
                        for attr, prop in example_image.get_relevant_xmp_attributes().items()}
        self._xmp_attributes = [attr
                                for attr in xmp_attributes.keys()
                                if possible_xmp.get(attr, False)]

        index = -1
        for time in self._sorted_times:
            if self._images[time].is_key_frame:
                self._key_frames.append(time)
                self._key_frame_gaps.append(1)
                index += 1
            else:
                self._key_frame_gaps[index] += 1

    def ramp_minus_exposure(self, ramp_blacks=False):
        ramps = {}
        for index, key_frame in enumerate(self._key_frames[:-1]):
            for attr in self._xmp_attributes:
                if attr not in ramps:
                    ramps[attr] = []
                ramps[attr].append((self._images[self._key_frames[index + 1]].get_xmp_attribute(attr)
                                    - self._images[key_frame].get_xmp_attribute(attr))
                                   / self._key_frame_gaps[index])
        for attr in self._xmp_attributes:
            ramps[attr].append(0.0)

        targets = {}
        for attr in self._xmp_attributes:
            targets[attr] = self._images[self._sorted_times[0]].get_xmp_attribute(attr)

        key_frame_index = -1
        for time in self._sorted_times:
            for attr in self._xmp_attributes:
                self._images[time].set_xmp_attribute(attr, targets[attr])
            if time in self._key_frames:
                key_frame_index += 1
            for attr in self._xmp_attributes:
                targets[attr] += ramps[attr][key_frame_index]
        if ramp_blacks:
            self._ramp_blacks()

    # TODO this needs better implementation and testing
    def _ramp_blacks(self):
        ramps = {}
        _xmp_attributes = ['Blacks', 'Exposure']
        for index, key_frame in enumerate(self._key_frames[:-1]):
            for attr in _xmp_attributes:
                if attr not in ramps:
                    ramps[attr] = []
                ramps[attr].append((self._images[self._key_frames[index + 1]].get_xmp_attribute(attr)
                                    - self._images[key_frame].get_xmp_attribute(attr))
                                   / self._key_frame_gaps[index])
        for attr in _xmp_attributes:
            ramps[attr].append(0.0)

        targets = {}
        for attr in _xmp_attributes[:-1]:
            targets[attr] = self._images[self._sorted_times[0]].get_xmp_attribute(attr)

        key_frame_index = 0
        last_exposure = self._images[self._sorted_times[0]].get_xmp_attribute('Exposure')
        for index, time in enumerate(self._sorted_times[1:]):
            this_exposure = self._images[time].get_xmp_attribute('Exposure')

            if index < Ramper._EARLY_MID_TRANSITION:
                exposure_compensation = Ramper._EARLY_BLACKS_EXPOSURE_COMPENSATION
            elif index < Ramper._MID_LATE_TRANSITION:
                exposure_compensation = Ramper._MID_BLACKS_EXPOSURE_COMPENSATION
            else:
                exposure_compensation = Ramper._LATE_BLACKS_EXPOSURE_COMPENSATION

            for attr in _xmp_attributes[:-1]:
                targets[attr] += ramps[attr][key_frame_index] \
                                 + (this_exposure - last_exposure - ramps['Exposure'][key_frame_index]) \
                                 * exposure_compensation

            for attr in _xmp_attributes[:-1]:
                self._images[time].set_xmp_attribute(attr, targets[attr])

            if time in self._key_frames:
                key_frame_index += 1

            last_exposure = this_exposure

    def _update_pbar(self, *a):
        self._pbar.update()

    def ramp_exposure(self, rectangle):
        if self._images[self._sorted_times[0]].brightness == None:
            ###################### FASTER ##########################################
            tasks = []
            pool = multiprocessing.Pool()
            self._pbar = tqdm(total=len(self._images) - 1, desc='Exposure Ramping: ')
            for time, image in self._images.items():
                task = pool.apply_async(Ramper._get_brightness, (time, image, rectangle), callback=self._update_pbar)
                tasks.append(task)
            pool.close()
            pool.join()
            for task in tasks:
                t, i = task.get()
                self._images[t].brightness = i
            ###################### Avoids apparend pytest/pycharm # bug ##############
            # for time, image in self._images.items():
            #     _, image.brightness = self._get_brightness(time, image, rectangle)
            # self.is_single_threaded = True
            ###################### End bug section #################################

        ramp = []
        for index, key_frame in enumerate(self._key_frames[:-1]):
            next_brightness = self._images[self._key_frames[index + 1]].brightness * \
                              2 ** self._images[self._key_frames[index + 1]].get_xmp_attribute('Exposure')
            this_brightness = self._images[key_frame].brightness * \
                              2 ** self._images[key_frame].get_xmp_attribute('Exposure')
            ramp.append((next_brightness - this_brightness) / self._key_frame_gaps[index])

        ramp.append(0)


        key_frame_index = -1
        for time in self._sorted_times:
            if time in self._key_frames:
                target = self._images[time].brightness * 2 ** self._images[time].get_xmp_attribute('Exposure')
                key_frame_index += 1
            else:
                exposure = math.log(target / self._images[time].brightness, 2)
                self._images[time].set_xmp_attribute('Exposure', exposure)
            target += ramp[key_frame_index]

    @staticmethod
    def _get_brightness(time, image, rectangle):
        return time, image.get_brightness(rectangle=rectangle)
