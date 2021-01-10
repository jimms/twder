#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twder
from setuptools import setup

setup(name='twder',
      version=twder.__version__,
      description='新台幣匯率擷取 (New Taiwan Dollar Exchange Rate)',
      long_description=open('./README.md', 'rb').read().decode('utf8'),
      long_description_content_type='text/markdown',
      author=twder.__author__,
      author_email='jimms.hsieh@gmail.com',
      url='https://github.com/jimms/twder',
      packages=['twder'],
      license=twder.__license__,
      keywords="NTD TWD 匯率 exchange rate",
      install_requires=['lxml'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Chinese (Traditional)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Topic :: Office/Business :: Financial :: Investment',
          ],
     )
