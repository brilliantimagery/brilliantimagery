Brilliant Imagery
=================

A DNG based photo editing package. It can do things such as:

* Decode and render lossless JPG images.
* Encode lessless JPG images.
* Render DNG images.
* Edit DNG metadata.
* Ramp Adobe Lightroom edits for image sequences.
* Stabilize shaky image sequences using the Adobe Lightroom crop property.

Documentation
-------------

Docs can be found at `brilliantimagery.org/docs <https://www.brilliantimagery.org/docs/>`_

Installation
------------

From PyPI
~~~~~~~~~

::

$ pip install brilliantimagery

From Source
~~~~~~~~~~~

The `Poetry <https://python-poetry.org/>`_ package and dependency manager is used by BrilliantImagery so install it if you haven't already done so. Some of the project files must be compiled. This accomplished within the below instructions.

Clone the `git repo <https://github.com/brilliantimagery/brilliantimagery.git>`_.

From within the top ``/brilliantimagery`` folder, the one that contains the ``pyproject.toml`` file, install BrilliantImagery:

::

$ poetry install


Development
-----------

Testing
~~~~~~~

Running the included tests can be used as a way to ensure that the package has been properly installed.

**Running Tests**

To run all of the tests:

::

$ poetry run pytest

**Coverage Reports**

Terminal coverage reports can be generated:

::

$ poetry run pytest --cov=brilliantimagery

HTML coverage reports can be generated when tests are run:

::

$ poetry run pytest --cov=brilliantimagery --cov-report=html

Docs
~~~~

After making changes to the docs, to update them, assuming ``./brilliantiamgery`` is the current working directory, activate a poetry shell:

::

$ poetry shell

Change the working directory to the ``/docs`` folder:

::

$ cd docs

And then run clean and make the html docs:

::

$ make clean && make html

Changelog
---------

* 0.2.0: Enabled saving and loading projects as well as reusing offsets and brightnesses between runs.

* 0.1.1: Fixed bug affecting sequences where multiple images have the same stored capture time.
