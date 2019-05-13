
from distutils.core import setup
setup(
  name = 'testpackagediego',
  packages = ['testpackagediego'],
  install_requires=[
          'setuptools',
          'scipy',
          'numpy',
          'matplotlib',
  ],
  version = '0.29',
  description = 'Test Package',
  author='Diego Arab Cohen',
  author_email='diego.arab.cohen@gmail.com',
  url = 'https://github.com/diegoarabcohen/testpackage'
)