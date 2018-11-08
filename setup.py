from distutils.core import setup
from Cython.Build import cythonize


setup(ext_modules=cythonize(
    ['ljpeg/_decode.pyx',
     'ljpeg/_encode.pyx',
     'dng/_renderer.pyx'],
    language="c++",
    compiler_directives={'cdivision': True,
                         'boundscheck': False,
                         },
    annotate=True)
)


# python setup.py build_ext --inplace
#cython: profile=True