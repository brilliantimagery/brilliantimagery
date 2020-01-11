MetaImage Module and Workflow
=============================

The MetaImage class is meant to act as an abstraction layer for between high level processes like image sequence editing and lower level processes like parsing image files. It presently only supports DNG files but the intention was to allow it to be expanded to be able to handle any kind of image file.

.. note::
    Since the MetaImage class and module is an abstraction layer intended to allow expansion beyond DNG files, but DNG files are all that's currently supported, their APIs are presently very similar, but if more file types are supported that could change as functionality increases.

Usage
-----

**Example: Getting the top left quarter of the image**

In this example, a piece of the total image is rendered and returned. Since the area to render is input at ``[0, 0, 0.5, 0.5]``, the rendered portion is from the top left corner to the center of the image.

.. code-block:: python

  from brilliantimagery.meta_image import MetaImage

  meta_image = MetaImage('path/to/image.file')

  image = meta_image.get_image([0, 0, 0.5, 0.5], 'RAW')

**Example: Get, update, and save XMP data**

Input:

.. code-block:: python

  from brilliantimagery.meta_image import MetaImage

  meta_iamge = MetaImage('path/to/image.file')

  val = meta_image.get_xmp_attribute(b'xmp:attr')

  print(f'Was: {val}')

  val += 5

  print(f'Is: {val}')

  meta_image.set_xmp_attribute(b'xmp:attr', val)
  meta_image.store_xmp_field()
  meta_image.save()

  val = meta_image.get_xmp_attribute(b'xmp:attr')

  print(f'Is still: {val}')

Returns:

.. code-block:: Python

  Was: 5.5
  Is: 10.5
  Is still: 10.5

API
---

.. automodule:: brilliantimagery.meta_image
   :members:
   :imported-members:
