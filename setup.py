#!/usr/bin/env python3
from setuptools import setup

setup(name='rtunnel',
      version='0.1',
      description='Reverse SSH tunnel tool',
      url='https://github.com/ConnorDillon/rtunnel',
      author='Connor Dillon',
      author_email='connor@cdillon.nl',
      license='GPLv3',
      packages=['rtunnel'],
      scripts=['scripts/rtunnel'],
      install_requires=['cmdtool==0.2', 'psutil>=2'],
      zip_safe=False)