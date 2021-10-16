========
Overview
========

This Project Extract Images,Text and Tables from a single package

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pdfextractor

You can also install the in-development version with::

    pip install git+ssh://git@https://github.com/shehrozkapoor/PDFEXTRACTOR.git/shehrozkapoor/PDFEXTRACTOR.git@master

Documentation
=============


https://PDFEXTRACTOR.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
