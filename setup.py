#!/usr/bin/env python

from distutils.core import setup

setup(name='zenlog',
      version='0.1',
      description='Logging for the lazy',
      author='Ricardo Lafuente',
      author_email='r@manufacturaindependente.org',
      url='http://github.com/manufacturaind/zenlog/',
      download_url='https://github.com/ManufacturaInd/zenlog/tarball/master',
      packages=['zenlog'],
      license="GPL",
      install_requires=['colorlog'],
     )

