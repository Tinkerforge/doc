
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Delphi - API Bindings

.. _api_bindings_delphi:

Delphi - API Bindings
=====================

**Requirements**: Delphi 2007 or newer, or Lazarus (Free Pascal Compiler 2.4
or newer), other Delphi or Object Pascal compilers might work as well

The Delphi bindings (:ref:`download <downloads_bindings_examples>`) consist of
the bindings for all Tinkerforge Bricks and
Bricklets (in ``bindings/``) and all available Delphi examples (in
``examples/``).

To keep the Delphi bindings stupid and simple, they only have dependencies that
are available nearly everywhere, thus making it possible to compile into any
project hassle-free. We do not offer a pre-compiled library, since it would be
a pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the bindings should work on most architectures
(ARM, x86, etc.) and on most operating systems (Windows and POSIX systems such
as Linux and Mac OS X, etc.).


Testing an Example
------------------

As an example we will compile the Stepper Brick configuration example with
Lazarus and Delphi XE2.


Lazarus
^^^^^^^

As an example we will compile the Stepper Brick configuration example with
the Free Pascal Compiler (FPC) that comes with the Lazarus IDE. For that we
have to copy the IP Connection (``Base58.pas``, ``BlockingQueue.pas``, ``Device.pas``,
``IPConnection.pas``, ``LEConverter.pas`` and ``TimedSemaphore.pas``) and the Stepper
Brick bindings (``BrickStepper.pas``) from the ``bindings/`` folder as well as the
``ExampleConfiguration.pas`` from the ``examples/Brick/Stepper/`` folder into our
project::

 project_folder/
  -> Base58.pas
  -> BlockingQueue.pas
  -> Device.pas
  -> IPConnection.pas
  -> LEConverter.pas
  -> TimedSemaphore.pas
  -> BrickStepper.pas
  -> ExampleConfiguration.pas

FPC automatically finds the used units, therefore a compilation of the project
with FPC like::

 fpc ExampleConfiguration.pas

With Lazarus we can use our ``project_folder/`` by clicking:

* Project
* New Project from file ...
* Choose ``project_folder/ExampleConfiguration.pas``
* Click Open
* Choose "Console Application"
* Click OK
* Choose "Application Class Name" and "Title"
* Click OK


Delphi IDE
^^^^^^^^^^

With Delphi XE2 (older Delphi version should work similar) we can use our
``project_folder/`` as follows. First rename ``ExampleConfiguration.pas`` to
``ExampleConfiguration.dpr`` then click:

* Project
* Add Existing Project...
* Choose ``project_folder/ExampleConfiguration.dpr``
* Click Open


More Examples and Projects
--------------------------

All the small examples contained in the ZIP file of the bindings can also be
found in the API documentation of the :ref:`Bricks <product_overview_bricks>` and
:ref:`Bricklets <product_overview_bricklets>`.

Further project descriptions can be found in the :ref:`kits <index_kits>` section.

.. FIXME: add a list with direct links here
