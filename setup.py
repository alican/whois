#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='whois',
      version='0.0.1',
      description='Complete whois parser',
      long_description = open("README.rst").read(),
      author='Mikhail Kashkin',
      author_email='mkashkin@gmail.com',
      url='https://github.com/xen/whois',
      # more examples here http://docs.python.org/distutils/examples.html#pure-python-distribution-by-package
      #packages=[, ],
      license = "BSD",
      install_requires=[
          'pyyaml'
      ],
     )
