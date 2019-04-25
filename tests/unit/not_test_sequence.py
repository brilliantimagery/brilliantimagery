from pathlib import Path

from BrilliantImagery.dng import DNG
from BrilliantImagery.ppm import save


def main():
    file = Path.cwd().parent / 'data' / 'dng_Pixel2.dng'
    dng = DNG(str(file))
    dng.parse()
    image = dng.get_image([0.3, 0.3, 0.7, 0.7])

    max_pix = max(max(max(image.tolist())))

    save(image * 255 / max_pix / 2, 'pixel2.ppm', 255)



if __name__ == '__main__':
    main()

