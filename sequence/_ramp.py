import math


class Ramper:
    def __init__(self, images):
        self._images = images
        self._ref_frames = []
        self._ref_frame_gaps = []

        self._sorted_times = sorted(self._images.keys())
        example_image = self._images[self._sorted_times[0]]
        xmp_attributes = example_image.get_xmp()
        possible_xmp = {attr: prop.is_ramped for attr, prop
                        in example_image.get_possible_xmp_attributes().items()}
        self._xmp_attributes = [attr for attr in xmp_attributes.keys() if possible_xmp.get(attr, False)]

        index = -1
        for time in self._sorted_times:
            if self._images[time].is_reference_frame():
                self._ref_frames.append(time)
                self._ref_frame_gaps.append(1)
                index += 1
            else:
                self._ref_frame_gaps[index] += 1

    def ramp_minus_exposure(self):
        ramps = {}
        for index, ref_frame in enumerate(self._ref_frames[:-1]):
            for attr in self._xmp_attributes:
                if attr not in ramps:
                    ramps[attr] = []
                ramps[attr].append((self._images[self._ref_frames[index + 1]].get_xmp_attribute(attr)
                                    - self._images[ref_frame].get_xmp_attribute(attr))
                                   / self._ref_frame_gaps[index])
        for attr in self._xmp_attributes:
            ramps[attr].append(0)

        targets = {}
        for attr in self._xmp_attributes:
            targets[attr] = self._images[self._sorted_times[0]].get_xmp_attribute(attr)

        reference_frame_index = -1
        for time in self._sorted_times:
            for attr in self._xmp_attributes:
                self._images[time].set_xmp_attribute(attr, targets[attr])
            if time in self._ref_frames:
                reference_frame_index += 1
            for attr in self._xmp_attributes:
                targets[attr] += ramps[attr][reference_frame_index]

    def ramp_exposure(self, rectangle):
        if self._images[self._sorted_times[0]].median_green_value == 0:
            for image in self._images.values():
                image.set_median_green_value(image.get_image(rectangle))

        ramp = []
        for index, ref_frame in enumerate(self._ref_frames[:-1]):
            next_brightness = self._images[self._ref_frames[index + 1]].median_green_value * \
                              2 ** self._images[self._ref_frames[index + 1]].get_xmp_attribute('Exposure')
            this_brightness = self._images[ref_frame].median_green_value * \
                              2 ** self._images[ref_frame].get_xmp_attribute('Exposure')
            ramp.append((next_brightness - this_brightness) / self._ref_frame_gaps[index])

        ramp.append(0)

        target = self._images[self._sorted_times[0]].median_green_value * \
                 2 ** self._images[self._sorted_times[0]].get_xmp_attribute('Exposure')

        reference_frame_index = -1
        for time in self._sorted_times:
            if time in self._ref_frames:
                target = self._images[self._sorted_times[0]].median_green_value * \
                         2 ** self._images[self._sorted_times[0]].get_xmp_attribute('Exposure')
                reference_frame_index += 1
            else:
                exposure = math.log(target / self._images[time].median_green_value, 2)
                self._images[time].set_xmp_attribute('Exposure', exposure)
            target += ramp[reference_frame_index]

    def _calc_image_brightness(self, time):
        return self._images[time].median_green_value * 2 ** self._images[time].get_xmp_attribute('Exposure')
