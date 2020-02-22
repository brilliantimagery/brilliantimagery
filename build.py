import os
from pathlib import Path
from setuptools import dist

dist.Distribution().fetch_build_eggs(['toml'])
import toml
path = Path(__file__).parent
try:
    toml_file = toml.load(str(path /'pyproject.toml'))
except:
    toml_file = toml.load(str(path /'pyproject.tmp'))
cython_version = toml_file.get('tool').get('poetry').get('dependencies').get('cython')

dist.Distribution().fetch_build_eggs([f'Cython>={cython_version.replace("^", "")}'])
from Cython.Build import cythonize
from setuptools import Extension

EXTENSIONS = [Extension(name='brilliantimagery.ljpeg._decode',
                        sources=['brilliantimagery/ljpeg/_decode.pyx']),
              Extension(name='brilliantimagery.ljpeg._encode',
                        sources=['brilliantimagery/ljpeg/_encode.pyx']),
              Extension(name='brilliantimagery.ppm._save',
                        sources=['brilliantimagery/ppm/_save.pyx']),
              Extension(name='brilliantimagery.dng._renderer',
                        sources=['brilliantimagery/dng/_renderer.pyx']),
              Extension(name='tests.unit.dng.renderer_exporter',
                        sources=['tests/unit/dng/renderer_exporter.pyx']),
              ]


def build(setup_kwargs):
    setup_kwargs.update({
        'ext_modules': cythonize(EXTENSIONS,
                                 compiler_directives={'cdivision': True,
                                                      'boundscheck': False,
                                                      'language_level': 3,
                                                      'embedsignature': True,
                                                      },
                                 include_path=[os.path.dirname(os.path.abspath(__file__))],
                                 )
    }
    )

# cython: profile=True
