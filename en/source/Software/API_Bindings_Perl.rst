
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

**Requirements**: Perl 5.014 or newer

The Perl bindings (:ref:`download <downloads_bindings_examples>`) consist of
a CPAN package with the bindings for all Tinkerforge Bricks and Bricklets
(``Tinkerforge.tar.gz``), the source (in ``source/``) and all available Perl
examples (in ``examples/``).

You can install the package with CPAN::

 sudo cpan install Tinkerforge

After that you can use the examples as they are.


Testing an Example
------------------

If you can't or don't want to use CPAN, you can also use the source
directly, just create a folder for your project and copy the ``Tinkerforge``
folder from ``source/`` and the example you want to try in there
(e.g. the Stepper configuration example from
``examples/brick/stepper/example_configuration.pl``)::

 example_folder/
  -> Tinkerforge/
  -> example_configuration.pl

we have to add a line on top of the file example_configuration.pl:

.. code-block:: perl

 use lib './';

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need ``IPConnection.pm`` and
``BrickStepper.pm``. After copying these in the project folder::

 example_folder/
  -> IPConnection.pm
  -> BrickStepper.pm
  -> example_configuration.pl

we have to remove the ``Tinkerforge::`` package from the examples, i.e. instead of:

.. code-block:: perl

 use Tinkerforge::IPConnection;
 use Tinkerforge::Device;
 use Tinkerforge::BrickStepper;

we use:

.. code-block:: perl

 use lib './';
 use IPConnection;
 use Device;
 use BrickStepper;

After that, the example can be executed again.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table.

.. include:: API_Bindings_Perl_links.table

Further project descriptions can be found in the :ref:`kits <index_kits>` section.
