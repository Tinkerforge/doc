
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-delphi">Software</a> / Delphi/Lazarus - API Bindings

.. _api_bindings_delphi:

Delphi/Lazarus - API Bindings
=============================

The Delphi/Lazarus bindings allow you to control :ref:`Bricks <primer_bricks>`
and :ref:`Bricklets <primer_bricklets>` from your Delphi/Lazarus programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``source/`` the source code of the bindings
* in ``examples/`` the examples for every Brick and Bricklet


Requirements
------------

* Delphi 2007 or newer, or Lazarus (Free Pascal Compiler 2.4 or newer), other
  Delphi or Object Pascal compilers might work as well


.. _api_bindings_delphi_install:

Installation
------------

To keep the Delphi/Lazarus bindings stupid and simple, they only have dependencies that
are available nearly everywhere, thus making it possible to compile into any
project hassle-free. We do not offer a precompiled library, since it would be
a pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the bindings should work on most architectures
(ARM, x86, etc.) and on most operating systems (Windows and POSIX systems such
as Linux and Mac OS X, etc.).

Because there is no precompiled library for the Delphi/Lazarus bindings there is nothing
to install as such. The recommended way of using the bindings is to include their
source code directly into your Delphi/Lazarus project. The next section shows some examples
about how to do that.


Testing an Example
------------------

To test a Delphi/Lazarus example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example we will compile the Stepper Brick configuration example with
the Free Pascal Compiler (FPC), as well as the Lazarus IDE and the Delphi IDE.
For that we have to copy the IP Connection and the Stepper Brick bindings from
the ``source/`` folder as well as the ``ExampleConfiguration.pas`` from the
``examples/Brick/Stepper/`` folder into a new folder::

 example_project/
  -> Base58.pas
  -> BlockingQueue.pas
  -> BrickDaemon.pas
  -> Device.pas
  -> DeviceBase.pas
  -> IPConnection.pas
  -> LEConverter.pas
  -> SHA1.pas
  -> TimedSemaphore.pas
  -> BrickStepper.pas
  -> ExampleConfiguration.pas

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: delphi

  const
    HOST = 'localhost';
    PORT = 4223;
    UID = 'XYZ'; { Change to your UID }


Free Pascal Compiler (FPC)
^^^^^^^^^^^^^^^^^^^^^^^^^^

FPC automatically finds the used units, therefore a compilation of the project
with FPC looks like this::

 fpc ExampleConfiguration.pas

Runtime Error 211
"""""""""""""""""

If you get Runtime Error 211 on starting your program or it prints::

 Threading has been used before cthreads was inizialized.

Then you need to add ``CThreads`` to the front of your ``Uses`` list of your
program.


Lazarus IDE
^^^^^^^^^^^

With Lazarus we can use our ``example_project/`` folder by clicking:

* Project
* New Project from file ...
* Choose ``example_project/ExampleConfiguration.pas``
* Click Open
* Choose "Console Application"
* Click OK
* Choose "Application Class Name" and "Title"
* Click OK

That's it, now the project can be compiled an executed!

Runtime Error 211
"""""""""""""""""

If you get Runtime Error 211 on starting your program or it prints::

 Threading has been used before cthreads was initialized.

Then you need to add ``-dUseCThreads`` to the Lazarus compiler options at:

* Project
* Project Options ...
* Compiler Options
* Other

Then recompile the project. If that does not fix the problem then you need to
add ``CThreads`` to the front of your ``Uses`` list of your program.


Delphi IDE
^^^^^^^^^^

With Delphi XE2 (older Delphi version should work similar) we can use our
``example_project/`` as follows. First rename ``ExampleConfiguration.pas`` to
``ExampleConfiguration.dpr`` then click:

* Project
* Add Existing Project...
* Choose ``example_project/ExampleConfiguration.dpr``
* Click Open

That's it, now the project can be compiled an executed!


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Delphi_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Delphi>
   Bricks <Bricks_Delphi>
   Bricklets <Bricklets_Delphi>
