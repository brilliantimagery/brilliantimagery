from distutils.core import setup
from Cython.Build import cythonize
from setuptools import find_packages


setup(
    name='BrilliantImagery',
    description='A DNG based photo editing package',

    version='19.0',
    author='Chad DeRosier',
    author_email='chad.derosier@gmail.com',
    url='http://www.brilliantimagery.org',

    packages=find_packages(where='src'),
    package_dir={'': 'src', 'tests': 'tests'},

    ext_modules=cythonize(['src/BrilliantImagery/ljpeg/_decode.pyx',
                           'src/BrilliantImagery/ljpeg/_encode.pyx',
                           'src/BrilliantImagery/dng/_renderer.pyx',
                           'src/BrilliantImagery/ppm/_save.pyx',
                           'tests/unit/dng/renderer_exporter.pyx',
                           ],
                          compiler_directives={'cdivision': True,
                                               'boundscheck': False,
                                               'language_level': 3,
                                               'embedsignature': True,
                                               },
                          # gdb_debug=True,
                          # annotate=True,
                          )
)

# python setup.py build_ext --inplace
#cython: profile=True