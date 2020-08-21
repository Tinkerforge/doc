Doc
===

This repository contains the Sphinx (https://sphinx-doc.org/) documentation for
all Bricks and Bricklets.

Setup
-----

The following steps are necessary to be able to build the documentation

Note: Device examples are in their own repositories
To create the complete documentation including
all examples, all repositories from
https://github.com/Tinkerforge have to be cloned

$ git clone https://github.com/Tinkerforge/doc

Create virtualenv

$ virtualenv sphinx-virtualenv
$ source sphinx-virtualenv/bin/activate

Install dependencies

$ pip install sphinx==1.4.9
$ pip install pygments==2.0.0
$ pip install PyEnchant==1.6.11
$ pip install sphinxcontrib-spelling==2.2.0

Install patched pygments packages

$ cd doc/pygments-mathematica/
$ python setup.py install
$ cd pygments-octave-fixed/
$ python setup.py install
$ cd ../..

The documentation is partly auto generated, so you need to clone the
generators (https://github.com/Tinkerforge/generators) first and execute
the generator and copy scripts.

$ git clone https://github.com/Tinkerforge/generators
$ cd generators/
$ python3 generate_all.py
$ python3 copy_all.py

Usage
-----
You can compile the HTML for the different languages with "make html" in the doc folder.

To be sure the latest version is built, pull the doc and generator gits and re-run
$ python3 generate_all.py
$ python3 copy_all.py
in the generators folder every time before compiling the HTML with make html.
