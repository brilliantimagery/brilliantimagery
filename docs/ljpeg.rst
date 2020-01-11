LJPEG Module and Workflow
=========================

.. note:: While this could be extensible to handle more common lossy JPEGs, it only presently handles lossless JPEGs.

.. note:: This isn't a complete implementation of the lossless JPEG standard.
   Only enough has been implemented to render the available reference DNG files.

.. note:: While initial validates have made the encode function appear to work, it's only seen minimal testing refinement so it's likely slow and potentially has bugs in some edge cases. I'll get polished when it becomes a priority (the developer needs it or someone reaches out about it).

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

**Example: Decode a lossless Jpeg and get the red, green, and blue components for the top left pixel as well as the image dimensions.**

This assumes that the image is RGB and has all color channels present in each pixel.

.. code-block:: python

  import numpy as np

  from brilliantimagery.ljpeg import decode

  image_bytes = np.fromfile('path/to/image.ljpeg', np.uint8).astype(np.intc)
  image_array = decode(image_bytes)

  red = image_array[0, 0, 0]
  green = image_array[1, 0, 0]
  blue = image_array[2, 0, 0]

  width = image_array.shape[1]
  height = image_array.shape[2]


Encoding
~~~~~~~~

**Example: Encode a lossless Jpeg given a 3D numpy array of integers.**

This assumes that ``image_data`` is a a 3D numpy array of ints and that white is represented by a number no larger than 255 since 8 bits of precision are being used to store the intensity values. Also, the ``predictor`` is 2.

.. code-block:: python

  import numpy as np

  from brilliantimagery.ljpeg import encode

  image = encode(image_data, 8, 2)

API
---

.. automodule:: brilliantimagery.ljpeg
   :members:
   :imported-members:
