
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-php">Software</a> / PHP - API Bindings

.. _api_bindings_php:

PHP - API Bindings
==================

The PHP bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your PHP scripts. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``Tinkerforge.tgz``, a PEAR package (installable with `pear
  <http://pear.php.net/>`__ tool)
* in ``source/`` the source code of ``Tinkerforge.tgz``
* in ``examples/`` the examples for every Brick and Bricklet


Requirements
------------

* PHP 5.3 or newer with ``bcmath`` and ``sockets`` extension


.. _api_bindings_php_install:

Installation
------------

The bindings can be installed, but can also be used without installation.

From PEAR Package
^^^^^^^^^^^^^^^^^

The bindings are available as a PEAR package. You can install it with the
`pear <http://pear.php.net/>`__ tool using the following command. Depending on
your PHP installation you might have to execute this with ``sudo`` or as
administrator::

 pear install Tinkerforge.tgz

Now you're ready to test the examples. The PEAR package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

Without Installation
^^^^^^^^^^^^^^^^^^^^

You can use the bindings without having to install them. Just copy the
``Tinkerforge/`` folder from the ``source/`` folder in the same folder as your
PHP script. The section about testing an example has more details about this.


Testing an Example
------------------

To test a PHP example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``ExampleConfiguration.php`` file from the
``examples/Brick/Stepper/`` folder into a new folder::

 example_project/
  -> ExampleConfiguration.php

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: php

  <?php

  const HOST = 'localhost';
  const PORT = 4223;
  const UID = 'XYZ'; // Change to your UID

  ?>

If you did install the bindings then you're now ready to test this example::

 php ExampleConfiguration.php

If you did **not** install the bindings then you can also use
the source of the bindings directly. Just copy the ``Tinkerforge/`` folder from
the ``source/`` folder to your ``example_project/`` folder and PHP will
automatically find the bindings::

 example_project/
  -> Tinkerforge/
  -> ExampleConfiguration.php

Now you're ready to test this example::

 php ExampleConfiguration.php


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_PHP_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_PHP>
   Bricks <Bricks_PHP>
   Bricklets <Bricklets_PHP>
