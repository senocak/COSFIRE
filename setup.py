from __future__ import print_function
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print('\'setuptools\' package is required during installation')
    sys.exit(1)

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

setup(name='COSFIRE',
      version='0.0.4',
      description='COSFIRE machine learning and image processing',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      )
