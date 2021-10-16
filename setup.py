#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with open('README.md','r') as fh:
        return fh.read()


setup(
    name='pdfextractor',
    version='1.0',
    license='BSD-2-Clause',
    description='This Project Extract Images,Text and Tables from a single package',
    long_description=read(),
    long_description_content_type = 'text/markdown',
    author='Shehroz Kapoor',
    author_email='shehrozkapoor@gmail.com',
    url='https://https://github.com/shehrozkapoor/PDFEXTRACTOR.git/shehrozkapoor/PDFEXTRACTOR',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://PDFEXTRACTOR.readthedocs.io/',
        'Changelog': 'https://PDFEXTRACTOR.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://https://github.com/shehrozkapoor/PDFEXTRACTOR.git/shehrozkapoor/PDFEXTRACTOR/issues',
    },
    keywords=[
        'extractImages','extractTable','extractText','extractTableCsv','extractTableJson','extractTableHTML','extractSpecPageTableHTML','extractSpecPageTableCsv','extractSpecPageTableJson','extractImageAll','extractImageSpecPage','extractTextAll','extractTextSpecPage','summarizer'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    install_requires=[
        'pip',
        'tabula-py',
        'camelot-py[cv]',
        'PyPDF2',
        'PyMuPDF',
        'pillow',
        'numpy',
        'spacy',
        'pdfminer',
        'pdfminer.six'
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    dependency_links=['https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz'],
    entry_points={
        'console_scripts': [
            'pdfextractor = pdfextractor.cli:main',
        ]
    },
)
