========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/myproj/badge/?style=flat
    :target: https://readthedocs.org/projects/myproj
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/github/pythonsavvy/myproj/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/pythonsavvy/myproj

.. |version| image:: https://img.shields.io/pypi/v/myproj.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/myproj

.. |commits-since| image:: https://img.shields.io/github/commits-since/pythonsavvy/myproj/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/pythonsavvy/myproj/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/myproj.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/myproj

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/myproj.svg
    :alt: Supported versions
    :target: https://pypi.org/project/myproj

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/myproj.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/myproj


.. end-badges

this is a demo project

* Free software: Apache Software License 2.0

Installation
============

::

    pip install myproj

Documentation
=============


https://myproj.readthedocs.io/


Development
===========

To run the all tests run::

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
