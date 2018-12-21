
.. _api_bindings_go:

Go - API Bindings
===================

The Go bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Go programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``github.com/Tinkerforge/go-api-bindings`` the source code of the bindings
* in ``examples/`` the examples for every Brick and Bricklet

The Go bindings are also hosted on `GitHub <https://github.com/Tinkerforge/go-api-bindings>`_.


Requirements
------------

* The Go compiler.


.. _api_bindings_go_install:

Installation
------------

The Go bindings can either be installed from the zip file, or by running ``go get -u github.com/Tinkerforge/go-api-bindings``.

If you want to install them from the zip file, extract the ``github.com`` folder and emplace it in the ``src`` folder of the `go path <https://golang.org/cmd/go/#hdr-GOPATH_environment_variable>`_.


Testing an Example
------------------

To test a Go example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's compile the configuration example for the Stepper Brick
from the command line. For this we create a new folder ``example_project`` in the ``src`` folder of the go path,
and then copy the ``example_configuration.go``
file from the ``examples/StepperBrick/`` folder into the created folder. Rename the copied file to ``main.go``.::

 $GOPATH/src/example_project/main.go (was example_configuration.go)

In the example ``ADDR`` specifies at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost:4223`` is correct.
The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: go

    const ADDR string = "localhost:4223"
    const UID string = "XXYYZZ" // Change XXYYZZ to the UID of your Stepper Brick.

Now we can build and run the project with ``go run example_project``.

 
API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Go_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Go>
   Bricks <Bricks_Go>
   Bricks (Discontinued) <Bricks_Go_Discontinued>
   Bricklets <Bricklets_Go>
   Bricklets (Discontinued) <Bricklets_Go_Discontinued>
