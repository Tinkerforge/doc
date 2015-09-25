
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-perl">Software</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

The Perl bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Perl scripts. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``source/`` the source code of the bindings (installable with
  ``Makefile.PL`` script)
* in ``examples/`` the examples for every Brick and Bricklet


Requirements
------------

* Perl 5.14 or newer with thread support, ``Digest::HMAC_SHA1`` module and
  ``Thread::Queue`` module 3.02 or newer


.. _api_bindings_perl_install:

Installation
------------

There are two ways to install the Perl bindings: from :ref:`CPAN
<api_bindings_perl_install_cpan>` or from :ref:`source
<api_bindings_perl_install_source>`. But the bindings can also be used
:ref:`without installing <api_bindings_perl_install_without>` them first.


.. _api_bindings_perl_install_cpan:

From CPAN
^^^^^^^^^

The bindings are also available on the Comprehensive Perl Archive Network `CPAN
<http://search.cpan.org/dist/Tinkerforge/>`__. You can install them with the
CPANminus tool `cpanm
<http://search.cpan.org/dist/App-cpanminus/lib/App/cpanminus.pm>`__ using the
following command (in this case you don't even need the ZIP file for the
bindings). Depending on your Perl installation you might have to execute this
with ``sudo`` or as administrator::

 cpanm Tinkerforge

Now you're ready to test the examples. The CPAN package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.


.. _api_bindings_perl_install_source:

From Source
^^^^^^^^^^^

The ``source/`` directory contains a ``Makefile.PL`` script.
To install the bindings just execute the following commands in the ``source/``
directory. Depending on your Perl installation you might have to execute this
with ``sudo`` or as administrator::

 perl Makefile.PL
 make
 make test
 make install

Now you're ready to test the examples.


.. _api_bindings_perl_install_without:

Without Installation
^^^^^^^^^^^^^^^^^^^^

You can use the bindings without having to install them. Just put the
``Tinkerforge/`` folder from ``source/lib/`` folder in the same folder as your
Perl script. The section about testing an example has more details about this.


Testing an Example
------------------

To test a Perl example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``example_configuration.pl`` file from the
``examples/brick/stepper/`` folder into a new folder::

 example_project/
  -> example_configuration.pl

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: perl

  use constant HOST => 'localhost';
  use constant PORT => 4223;
  use constant UID => 'XYZ'; # Change to your UID

If you did install the bindings from :ref:`source
<api_bindings_perl_install_source>` or :ref:`CPAN
<api_bindings_perl_install_cpan>` then you're now ready to test this example::

 perl example_configuration.pl

If you did **not** install the bindings then you can also use the source of the
bindings directly. Just copy the ``Tinkerforge/`` folder from the ``source/lib/``
folder to your ``example_project/`` folder::

 example_project/
  -> Tinkerforge/
  -> example_configuration.pl

Then the following line has to be added to the beginning of the example to
make Perl find the ``Tinkerforge/`` folder:

.. code-block:: perl

 use lib './';

Now you're ready to test this example::

 perl example_configuration.pl


.. _api_bindings_perl_known_problems:

Known Problems
--------------

There are known deadlock problems on Windows with `Strawberry Perl
<http://strawberryperl.com/>`__ and `Active State Perl
<http://www.activestate.com/activeperl>`__. The recommended workaround is to
use `Cygwin <https://www.cygwin.com/>`__ Perl that doesn't
suffer from this problem. See this `PerlMonks thread
<http://perlmonks.org/?node_id=1078634>`__ for some details.


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Perl_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Perl>
   Bricks <Bricks_Perl>
   Bricklets <Bricklets_Perl>
