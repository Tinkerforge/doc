
.. _api_bindings_go:

Go - API Bindings
=================

The Go bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Go programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``github.com/Tinkerforge/go-api-bindings`` the source code of the bindings
* in ``examples/`` the examples for every Brick and Bricklet

Requirements
------------

* Go compiler 1.11 or newer

.. _api_bindings_go_install:

Installation
------------

There are two ways to install the Go bindings: from :ref:`GitHub
<api_bindings_go_install_github>` or from :ref:`source
<api_bindings_go_install_source>`.

.. _api_bindings_go_install_github:

From GitHub
^^^^^^^^^^^

The bindings are available from the `GitHub
<https://github.com/Tinkerforge/go-api-bindings>`__ (in this case you don't
even need the ZIP file for the bindings). Install the bindings using the
``go get`` tool::

 go get -u github.com/Tinkerforge/go-api-bindings

This does not include the examples. Those are available as part of
the bindings :ref:`ZIP file <downloads_bindings_examples>`.

.. _api_bindings_go_install_source:

From Source
^^^^^^^^^^^

Extract the ``github.com`` directory from the ZIP file to a directory of your choice.

Add the following line to the ``go.mod`` file of your Go program, to tell the Go
compiler where to find the Go bindings::

 replace github.com/Tinkerforge/go-api-bindings => /path/to/your/github.com/Tinkerforge/go-api-bindings

Replace the ``/path/to/your`` part with the directory you extracted the
``github.com`` directory from the ZIP file to.

Now you're ready to test an example.

Testing an Example
------------------

To test a Go example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's compile the configuration example for the Stepper Brick
from the command line. For this we use  the ``example_configuration.go``
file from the ``examples/StepperBrick/`` folder of the ZIP file.

In the example ``ADDR`` specifies at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost:4223`` is correct.
The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: go

    const ADDR string = "localhost:4223"
    const UID string = "XXYYZZ" // Change XXYYZZ to the UID of your Stepper Brick.

Now we can build and run the project with ``go run example_configuration.go``.


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_Go_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Go>
   Bricks <Bricks_Go>
   Bricks (Discontinued) <Bricks_Go_Discontinued>
   Bricklets <Bricklets_Go>
   Bricklets (Discontinued) <Bricklets_Go_Discontinued>
