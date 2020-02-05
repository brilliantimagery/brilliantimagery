DNG Module and Workflow
***********************

.. note::
   While, between the DNG and LJPEG modules, much of the functionality exists which is required to edit the underlying raw data, this functionality has not yet been fully stitched together to make it fully operational. This will likely happen either when the primary developer has a need for this or when someone reaches out requesting it.

The DNG module allows DNG images to be read, rendered, edited, updated, and saved. Like with most other digital image technology, the top left corner of the image is the origin.

Usage
=====

**Example: Getting the top left quarter of the raw image**

In this example, a piece of the total image is rendered and returned. Since the area to render is input at ``[0, 0, 0.5, 0.5]``, the rendered portion is from the top left corner to the center of the image.

.. code-block:: python

  from brilliantimagery.dng import DNG

  dng = DNG('path/to/dng.dng')

  image = dng.get_image([0, 0, 0.5, 0.5], 'RAW')

**Example: Get, update, and save XMP data**

When the below code it run:

.. code-block:: python

  from brilliantbmagery.dng import DNG

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

The below lines would be printed assuming the ``xmp:attr`` attribute started with a value of 5.5.

.. code-block:: Python

  Was: 5.5
  Is: 10.5
  Is still: 10.5

API
===

.. automodule:: brilliantimagery.dng
    :members:
    :imported-members:
