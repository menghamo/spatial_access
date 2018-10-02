import platform, distutils.core, distutils.extension, Cython.Build, setuptools
from setuptools.command.install import install

import sys
import os

class CustomInstallCommand(install):
    """Customized setuptools install command"""
    def run(self):
        os.system('pip3 install -r requirements.txt')
        print('running...')
        if sys.platform == "darwin":
            os.system('brew install spatialindex')
            print('installing on osx')
        elif sys.platform.startswith('linux'):
            sos.system('curl -L https://github.com/libspatialindex/libspatialindex/archive/1.8.5.tar.gz | tar xz')
            os.system('cd spatialindex-src-1.8.5')
            os.system('./configure')
            os.system('make')
            os.system('sudo make install')
            os.system('sudo ldconfig')
            print('installing on linux')
        else:
            raise Exception('You are trying to install spatial_access on an unsupported platform', os.system)
        os.system('pip3 install rtree')
        install.run(self)

## Macs require this extra build option.
ouff_mac = []
if sys.platform == "darwin":
  ouff_mac = ['-mmacosx-version-min=10.9']

EXTENSION = distutils.extension.Extension(
    name = 'pyengine', language = 'c++',
    sources = ['spatial_access/pyengine.pyx'],
    extra_compile_args = ['-Wno-unused-function', 
                          '-std=c++11', '-Wall', '-O3'
                          ] + ouff_mac,
    undef_macros       = ["NDEBUG"],
    extra_link_args    = ouff_mac
    )

EXT_MODULES=Cython.Build.cythonize([EXTENSION],
                                    #include_path = ["/usr/local/include/"],
                                   language='c++')

REQUIRED_DEPENDENCIES = ['fiona>=1.7.12',
                         'cython>=0.28.2',
                         'matplotlib>=2.0.2',
                         'jellyfish>=0.5.6',
                         'geopandas>=0.3.0',
                         'psutil>=5.4.3',
                         'pandas>=0.19.2',
                         'numpy>=1.12.0',
                         'rtree>=0.8.3',
                         'pandana>=0.4.0',
                         'scipy>=0.18.1',
                         'geopy>=1.11.0',
                         'Shapely>=1.6.1',
                         'scikit_learn>=0.19.1',
                         'atlas>=0.27.0',
                         'jupyter_contrib_nbextensions>=0.5.0',
                         'jupyter_nbextensions_configurator>=0.1.7'
]

setuptools.setup(
    cmdclass = {'install':CustomInstallCommand},
    name = 'spatial_access',
    author = 'Logan Noel (lmnoel)',
    url='https://github.com/GeoDaCenter/spatial_access',
    author_email='lnoel@uchicago.edu',
    version='0.1.0',
    ext_modules=EXT_MODULES,
    install_requires=REQUIRED_DEPENDENCIES,
    py_modules=['spatial_access.p2p', 'spatial_access.ScoreModel', 'spatial_access.CommunityAnalytics']
    )
