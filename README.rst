Brilliant Imagery
=================

A DNG based photo editing package

Instilation
-----------

The `Poetry <https://python-poetry.org/>`_ package and dependency manager is used by Brilliant Imagery so install it if you haven't already done so. Some of the project files must be compiles. This process is automated within the below instructions.

Clone the `git repo <https://github.com/brilliantimagery/brilliantimagery.git>`_.

From within the top ``/brilliantimagery`` folder, the one that contains the ``pyproject.toml`` file, install Brilliant Imagery:

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
