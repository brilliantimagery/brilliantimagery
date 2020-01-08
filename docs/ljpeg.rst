LJPEG Module and Workflow
=========================

.. note:: While this could be extensible to handle more common lossy JPEGs, it only presently handles lossless JPEGs.

.. note:: This isn't a complete implementation of the lossless JPEG standard.
   Only enough has been implemented to render the available reference DNG files.

This is a lossless jpeg encoder and encoder utility. It's based on the 1992 standard T.81, 10918.1.

While images are often stored and/or represented as 1D arrays; this module does not follow that pattern.
Following the more typical pattern can require frequent and verbose calculations to extract actual pixel values
from arrays in higher level functions. Using this format, pixel values fall out of the array values:

.. code-block:: python

    pixel_color_channel_value = image[color_channel, x_position, y_position]

    pixel_color_value = image[:, x_position, y_position]

Additionally, this format is easily reshaped to a more standard shape with :func:`numpy.reshape`.

Usage
-----

Decoding
~~~~~~~~

**Example: Decode a lossless Jpeg and get the red, green, and blue components for the top left pixel.**

This assumes that the image is RGB and has all color channels are present in each pixel.

.. code-block:: python

  import numpy as np

  from BrilliantImagery.ljpeg import decode

  image_bytes = np.fromfile('path/to/image.ljpeg', np.uint8).astype(np.intc)
  image_array = decode(image_bytes)

  red = image_array[0, 0, 0]
  green = image_array[1, 0, 0]
  blue = image_array[2, 0, 0]


Encoding
~~~~~~~~

**Example: Encode a lossless Jpeg given a 3D numpy array of integer**

.. code-block:: python

  import numpy as np

  from BrilliantImagery.ljpeg import encode

  image_bytes = np.fromfile('path/to/image.ljpeg', np.uint8).astype(np.intc)
  image_array = encode(image_bytes, 8, 2)

  red = image_array[0, 0, 0]
  green = image_array[1, 0, 0]
  blue = image_array[2, 0, 0]

encode something

get pixel values from a decoded pixel

API
---

.. automodule:: BrilliantImagery.ljpeg
   :members:
   :imported-members:
