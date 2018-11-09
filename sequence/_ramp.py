class Ramper:
    def __init__(self, images, rectangle):
        self._images = images
        self._ref_frames = dict()

        example_image = next(iter(self._images.values()))
        if example_image.median_green_value == 0:
            for image in self._images.values():
                image.set_median_green_value(image.get_image(rectangle))

        for time, image in self._images.items():
            if image.is_reference_frame():
                self._ref_frames[time] = image
                image.median_green_value *= 1 + image.get_xmp_attribute('Exposure')

    def ramp(self):
        ref_frames = sorted(self._ref_frames.keys())
        self._ref_frames
