import multiprocessing

from tqdm import tqdm

from . import _stabilize_util as sutil


class Stabilizer:
    def __init__(self, images, rectangle):
        self._images = images
        self._rectangle = rectangle

    def _update_pbar(self, *a):
        self._pbar.update()

    def find_misalignments(self, keep_brightness=False):
        images = self._images
        ordered_times = sorted(images.keys())
        image0 = images[ordered_times[0]].get_image(self._rectangle)

        if keep_brightness:
            images[ordered_times[0]].get_brightness(image=image0)

        images[ordered_times[0]].misalignment = [0, 0]

        tasks = []
        pool = multiprocessing.Pool()
        self._pbar = tqdm(total=len(images) - 1, desc='Finding misalignments: ')
        for time0, time1 in zip(ordered_times[:-1], ordered_times[1:]):
            task = pool.apply_async(sutil.find_misalignment, (images[time0], images[time1], self._rectangle,
                                                              keep_brightness, time1),
                                    callback=self._update_pbar)
            tasks.append(task)
        pool.close()
        pool.join()
        for task in tasks:
            t, i = task.get()
            images[t] = i

        for time0, time1 in zip(ordered_times[:-1], ordered_times[1:]):
            images[time1].misalignment[0] += images[time0].misalignment[0]
            images[time1].misalignment[1] += images[time0].misalignment[1]

        for time in ordered_times:
            images[time].misalignment[0] = round(images[time].misalignment[0])
            images[time].misalignment[1] = round(images[time].misalignment[1])

        # TODO: this seems cleaner but is generating an error 'Process finished with exit code -1073741819 (0xC0000005)'
        # ordered_images = [images[time] for time in ordered_times[1:]]
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     tasks = list(tqdm(executor.map(sutil.find_misalignment, itertools.repeat(image0, len(ordered_images)),
        #                                    ordered_images, itertools.repeat(self._rectangle, len(ordered_images)),
        #                                    itertools.repeat(self._max_pix_of_misalignment, len(ordered_images)),
        #                                    itertools.repeat(keep_brightness, len(ordered_images)), ordered_times[1:]),
        #                  total=len(ordered_times[1:]),
        #                  desc='Find misalignments: '))
        # for time, image in tasks:
        #     self._images[time] = image

    def update_xmp_attributes(self):
        example_image = next(iter(self._images.values()))
        min_x, min_y, max_x, max_y = sutil.misalignment_bounding_box(self._images.values())
        shape = example_image.rendered_shape()
        left = example_image.get_xmp_attribute('CropLeft')
        top = example_image.get_xmp_attribute('CropTop')
        right = example_image.get_xmp_attribute('CropRight')
        bottom = example_image.get_xmp_attribute('CropBottom')
        if (max_x < left * shape[0] and max_y < top * shape[1] and
                -min_x < (1 - right) * shape[0] and -min_y < (1 - bottom) * shape[1]):
            for image in self._images.values():
                left = image.get_xmp_attribute('CropLeft') + image.misalignment[0] / shape[0]
                image.set_xmp_attribute('CropLeft', left)
                top = image.get_xmp_attribute('CropTop') + image.misalignment[1] / shape[1]
                image.set_xmp_attribute('CropTop', top)
                right = image.get_xmp_attribute('CropRight') + image.misalignment[0] / shape[0]
                image.set_xmp_attribute('CropRight', right)
                bottom = image.get_xmp_attribute('CropBottom') + image.misalignment[1] / shape[1]
                image.set_xmp_attribute('CropBottom', bottom)
        else:
            for image in self._images.values():
                left = image.get_xmp_attribute('CropLeft') + (max_x - min_x + image.misalignment[0]) / shape[0]
                image.set_xmp_attribute('CropLeft', left)
                top = image.get_xmp_attribute('CropTop') + (max_y - min_y + image.misalignment[1]) / shape[1]
                image.set_xmp_attribute('CropTop', top)
                right = image.get_xmp_attribute('CropRight') + (-max_x + min_x + image.misalignment[0]) / shape[0]
                image.set_xmp_attribute('CropRight', right)
                bottom = image.get_xmp_attribute('CropBottom') + (-max_y + min_y + image.misalignment[1]) / shape[1]
                image.set_xmp_attribute('CropBottom', bottom)
