import os
from distutils.core import setup
from Cython.Build import cythonize

import brilliantimagery

setup(
    name='brilliant-imagery',
    description='A DNG based photo editing package',

    version=brilliantimagery.__version__,
    author='Chad DeRosier',
    author_email='chad.derosier@gmail.com',
    url='http://www.brilliantimagery.org',

    packages=['brilliantimagery'],

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
