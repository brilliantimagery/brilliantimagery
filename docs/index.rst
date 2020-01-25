.. BrilliantImagery documentation master file, created by
   sphinx-quickstart on Tue May  7 11:23:35 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to BrilliantImagery's documentation!
============================================

The BrilliantImagery project aims to enable making beautiful photo based art. It has the dual goals of allowing users to use a few relatively simple functions to accomplish powerful tasks, and to allow the the underlying functionality to be leveraged to enable the creation of even more powerful functionality.

.. Note::
   This project is in an Alpha/Beta state of development. While every effort is made to have it work well and predictably, maybe the first project you use it on shouldn't be your wedding photos.

.. note::
   These docs are geared towards development with the package, not the workflow it's designed to be used with to edit photos. The API's functionality is covered in detail but in order to learn more about the photo editing workflow that it's expected to be used with go to `brilliantimagery.org <https://www.brilliantimagery.org/>`_.

Features
--------

- Read, write, and render DNG photos
- Edit DNG XMP data
- Smoothly transition DNG appearances
- Calculate representative image brightnesses
- Stabilize image sequences
- Align images

Top-Level Functionality
-----------------------
.. toctree::
   :maxdepth: 2

   sequence

Sub-Functionality
-----------------
.. toctree::
   :maxdepth: 2

   meta_image

.. toctree::
   :maxdepth: 2

   dng

.. toctree::
   :maxdepth: 2

   ljpeg

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
