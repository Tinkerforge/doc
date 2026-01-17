Doc
===

This repository contains the Sphinx (https://sphinx-doc.org/) documentation for
all Bricks and Bricklets.

Requirements
------------

- Python 3.9+
- Sphinx 7.0+

Setup
-----

Clone the repository::

    git clone https://github.com/Tinkerforge/doc
    cd doc

Create and activate a virtual environment::

    python3 -m venv sphinx-virtualenv
    source sphinx-virtualenv/bin/activate

Install dependencies::

    pip install -r requirements.txt

Install custom Pygments lexers::

    pip install ./pygments-mathematica
    pip install ./pygments-octave-fixed

Generating Documentation
------------------------

The documentation is partly auto-generated. Clone the generators repository
and run the generation scripts::

    git clone https://github.com/Tinkerforge/generators
    cd generators/
    python3 generate_all.py
    python3 copy_all.py
    cd ..

Note: Device examples are in their own repositories. To create the complete
documentation including all examples, all repositories from
https://github.com/Tinkerforge need to be cloned.

Building
--------

Build HTML documentation for English::

    cd en
    source ../sphinx-virtualenv/bin/activate
    sphinx-build -j auto -b html source build/html

Build HTML documentation for German::

    cd de
    source ../sphinx-virtualenv/bin/activate
    sphinx-build -j auto -b html source build/html

Alternatively, use ``make html`` in the ``en`` or ``de`` directories.

Rebuilding
----------

To rebuild with the latest changes, pull the doc and generators repositories
and re-run the generation scripts before building::

    cd generators/
    git pull
    python3 generate_all.py
    python3 copy_all.py
    cd ../doc
    git pull
