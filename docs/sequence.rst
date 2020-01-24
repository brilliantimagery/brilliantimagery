Sequence Module and Workflow
============================

The :attr:`Sequence` class is used for editing sequences of images. It's primary functions are to smoothly adjust settings between images in the sequence such as exposure, color temperature, and saturation, and to stabilize shaky sequences.

.. note::
    In order to avoid exploding memory requirements, image data typically isn't kept so a lot of time can be saved or waisted by running processes in particular orders with particular settings. As a result, in order to make things simpler for the user, a number of helper functions have been made to simplify this. Unless there's a specific reason no to, and the consequences are well understood, using correct helper function is cleaner and sometimes faster than chaining helper functions together.

Usage
-----

In the below examples it's assumed that the photos are in a single folder and have been appropriately edited in Adobe Lightroom. The editing process workflow can be learned about at `brilliantimagery.org <https://www.brilliantimagery.org/>`_

**Example: Smooth the exposure transitions but nothing else.**

.. code-block:: python

  from brilliantimagery.sequence import Sequence

  sequence = Sequence('path/to/folder/of/images')

  sequence.ramp_exposure([0.25, 0.25, 0.5, 0.5])

**Example: Stabilize the image sequence.**

.. code-block:: python

  from brilliantimagery.sequence import Sequence

  sequence = Sequence('path/to/folder/of/images')

  sequence.stabilize([0.25, 0.25, 0.5, 0.5])

**Example: Stabilize the image sequence and smooth all transitions.**

.. code-block:: python

  from brilliantimagery.sequence import Sequence

  sequence = Sequence('path/to/folder/of/images')

  sequence.ramp_and_stabilize([0.25, 0.25, 0.5, 0.5])

.. automodule:: brilliantimagery.sequence.Sequence
   :members:
   :imported-members:
