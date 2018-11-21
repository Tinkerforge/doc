
.. _api_bindings_rust:

Rust - API Bindings
===================

The Rust bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Rust programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``src/`` the source code of the bindings
* in ``examples/`` the examples for every Brick and Bricklet

The Rust bindings are also hosted on `crates.io <https://crates.io/crates/tinkerforge>`_.


Requirements
------------

* The Rust compiler version 1.31 or greater.


.. _api_bindings_rust_install:

Installation
------------

The Rust bindings can either be installed from the zip file, or by downloading
them from crates.io.

If you add ``tinkerforge = "2.0"`` to your ``Cargo.toml``'s ``[dependencies]`` section, cargo
will download the bindings and all dependencies on the next run.

If you want to install them from the zip file, download and extract it and register the dependency by adding
``tinkerforge = {path=[your/path/here]}`` to the ``[dependencies]`` section of your
``Cargo.toml``, specifing the correct path (without ``src`` at the end) instead of the placeholder. The next run of cargo will download the binding's dependencies.


Testing an Example
------------------

To test a Rust example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's compile the configuration example for the Stepper Brick
from the command line. For this we create a new folder ``example_project``,
run ``cargo init`` in this folder, and then copy the ``example_configuration.rs``
file from the ``examples/StepperBrick/`` folder into the ``src`` folder which was
created by cargo. Rename the copied file to ``main.rs`` (overwriting the one
created by cargo)::

 example_project/
  -> Cargo.toml
  -> src/main.rs (was example_configuration.rs)
  
Then add either ``tinkerforge = "2.0"`` or ``tinkerforge = {path=[your/path/here]}`` 
into the ``[dependencies]`` section of your project's ``Cargo.toml``.

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: rust

    const HOST: &str = "localhost";
    const PORT: u16 = 4223;
    const UID: &str = "XXYYZZ"; // Change XXYYZZ to the UID of your Stepper Brick.

Now we can build and run the project with ``cargo run``.

 
API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Rust_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Rust>
   Bricks <Bricks_Rust>
   Bricks (Discontinued) <Bricks_Rust_Discontinued>
   Bricklets <Bricklets_Rust>
   Bricklets (Discontinued) <Bricklets_Rust_Discontinued>
