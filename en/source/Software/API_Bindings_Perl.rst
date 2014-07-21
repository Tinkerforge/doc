
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-perl">Software</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

**Requirements**: Perl 5.014 or newer with Thread::Queue 3.02 or newer

The Perl bindings (:ref:`download <downloads_bindings_examples>`) consist of
a CPAN package with the bindings for all Tinkerforge Bricks and Bricklets
(``Tinkerforge.tar.gz``), the source (in ``source/``) and all available Perl
examples (in ``examples/``).

There are known deadlock problems on Windows with Strawberry Perl and Active
State Perl. The recommended workaround is to use Cygwin's Perl that doesn't
suffer from this problem. See this `PerlMonks thread
<http://perlmonks.org/?node_id=1078634>`__ for some details.

You can install the package from `CPAN <http://www.cpan.org/>`__ with the
following command (we recommend the `CPANminus
<http://search.cpan.org/dist/App-cpanminus/lib/App/cpanminus.pm>`__ commandline
tool ``cpanm`` for this task)::

 cpanm Tinkerforge

Yon can also install the local version of the CPAN package by unpacking
``Tinkerforge.tar.gz`` and running the following commands::

 perl Makefile.PL
 make
 make test
 make install

After that you can use the examples as they are.


.. _api_bindings_perl_install:

Installation
------------

TODO


Testing an Example
------------------

If you can't or don't want to use the CPAN package, you can also use the source
directly, just create a folder for your project and copy the ``Tinkerforge``
folder from ``source/`` and the example you want to try in there
(e.g. the Stepper configuration example from
``examples/brick/stepper/example_configuration.pl``)::

 example_folder/
  -> Tinkerforge/
  -> example_configuration.pl

You have to add a line on top of the file ``example_configuration.pl``:

.. code-block:: perl

 use lib './';

After that, the example can be executed again.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Perl_links.table
