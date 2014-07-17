
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-php">Software</a> / PHP - API Bindings

.. _api_bindings_php:

PHP - API Bindings
==================

**Requirements**: PHP 5.3 or newer with ``bcmath`` and ``sockets`` extension

The PHP bindings (:ref:`download <downloads_bindings_examples>`) consist of a
PEAR package with the bindings for all
Tinkerforge Bricks and Bricklets (``Tinkerforge.tgz``), the source of the
PEAR package (in ``source/``) and all available PHP examples (in ``examples/``).

You can install the PEAR package with the pear tool::

 pear install Tinkerforge.tgz

After that you can use all examples as they are.


.. _api_bindings_php_install:

Installation
------------

TODO


Testing an Example
------------------

If you can't or don't want to use the PEAR package, you can also use the source
directly, just create a folder for your project and copy the ``Tinkerforge``
folder from ``source/`` and the example you want to try in there
(e.g. the Stepper configuration example from
``examples/brick/stepper/ExampleConfiguration.php``)::

 example_folder/
  -> Tinkerforge/
  -> ExampleConfiguration.php

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need ``IPConnection.php`` and
``BrickStepper.php``. After copying these in the project folder::

 example_folder/
  -> IPConnection.php
  -> BrickStepper.php
  -> ExampleConfiguration.php

we have to remove the ``Tinkerforge`` folder from the examples, i.e. instead of:

.. code-block:: php

    <?php

    require_once('Tinkerforge/IPConnection.php');
    require_once('Tinkerforge/BrickStepper.php');
    ...

    ?>

we use:

.. code-block:: php

    <?php

    require_once('IPConnection.php');
    require_once('BrickStepper.php');
    ...

    ?>

After that, the example can be executed again.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`kits <index_kits>` section.

.. include:: API_Bindings_PHP_links.table
