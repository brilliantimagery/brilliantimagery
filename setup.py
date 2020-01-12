import os
from distutils.core import setup
from Cython.Build import cythonize

import brilliantimagery

README_rst = ''
with open('README.rst', mode='r', encoding='utf-8') as fd:
    README_rst = fd.read()

setup(
    name='brilliant-imagery',
    description='A DNG based photo editing package',

    version=brilliantimagery.__version__,
    author='Chad DeRosier',
    author_email='chad.derosier@gmail.com',
    url='http://www.brilliantimagery.org',

    packages=['brilliantimagery'],
    include_package_data=True,
    long_description=README_rst,

    ext_modules=cythonize(['brilliantimagery/ljpeg/_decode.pyx',
                           'brilliantimagery/ljpeg/_encode.pyx',
                           'brilliantimagery/ppm/_save.pyx',
                           'brilliantimagery/dng/_renderer.pyx',
                           'tests/unit/dng/renderer_exporter.pyx',
                           ],
                          compiler_directives={'cdivision': True,
                                               'boundscheck': False,
                                               'language_level': 3,
                                               'embedsignature': True,
                                               },
                          include_path=[os.path.dirname(os.path.abspath(__file__))],

                          # gdb_debug=True,
                          # annotate=True,
                          )
)

# cython: profile=True
