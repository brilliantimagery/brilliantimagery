DNG Module and Workflow
=========================

.. note::
   While, between the DNG and LJPEG modules, much of the functionality exists which is required to edit the
   underlying raw data, this functionality is not yet implemented.

The DNG module allows DNG images to be read, rendered, edited, updated, and saved.

Usage
-----

**Example: Getting the top left quadrant of the raw image**

.. code-block:: python

  from BrilliantImagery.dng import DNG

  dng = DNG('path/to/dng.dng')

  image = dng.get_image([0, 0, 0.5, 0.5], 'RAW')

**Example: Get, update, and save XMP data**

Input:

.. code-block:: python

  from BrilliantImagery.dng import DNG

  dng = DNG('path/to/dng.dng')

  val = dng.get_xmp_attribute(b'xmp:attr')

  print(f'Was: {val}')

  val += 5

  print(f'Is: {val}')

  dng.set_xmp_attribute(b'xmp:attr', val)
  dng.store_xmp_field()
  dng.save()

  val = dng.get_xmp_attribute(b'xmp:attr')

  print(f'Is still: {val}')

Returns:

.. code-block:: Python

  Was: 5.5
  Is: 10.5
  Is still: 10.5

API
---

.. automodule:: BrilliantImagery.dng
   :members:
   :imported-members:
