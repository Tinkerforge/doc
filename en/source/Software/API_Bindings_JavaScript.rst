
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / JavaScript - API Bindings

.. _api_bindings_javascript:

JavaScript - API Bindings
=========================

The JavaScript binding (:ref:`download <downloads_bindings_examples>`) consists
of a Node.js NPM package ``tinkerforge.tgz`` and the browser version (in ``browser/``)
of the bindings for all Tinkerforge Bricks and Bricklets. The source and examples of
the Node.js implementation (in ``nodejs/source``) and (in ``nodejs/examples``),
the examples of the browser API (in ``browser/exmaples``) for all Tinkerforge Bricks and
Bricklets are included as well. The source of the browser implementation
(in ``browser/source/``).

You can install the NPM Package locally with ``sudo npm -g install tinkerforge.tgz``
or from NPM registry with ``sudo npm -g install tinkerforge``. After that you
can use the examples as they are.

Testing an Example
------------------

If you can't or don't want to use the NPM package, you can also use the source
directly, just create a folder for your project and copy the ``Tinkerforge`` folder
from ``source/`` and the example you want to try in there (e.g. the Stepper Brick
configuration example from ``examples/brick/stepper/ExampleConfiguration.js``)::

 example_folder/
 -> Tinkerforge/
 -> ExampleConfiguration.js

The required statements must be modified in this case as follows,

instead of,

.. code-block::javascript
 var Tinkerforge = require('Tinkerforge');
 var ipcon = new Tinkerforge.IPConnection();
 var stepper = new Tinkerforge.BrickStepper();

use,

.. code-block::javascript
 var IPConnection = require('./Tinkerforge/IPConnection');
 var BrickStepper = require('./Tinkerforge/BrickStepper');
 var ipcon = new IPConnection();
 var stepper = new BrickStepper();

For using the HTML examples, just put the browser implementation source
file from ``browser/source/Tinkerforge.js`` and the HTML file of the example
that you want to try in the same directory and simply open the HTML file with
a browser.

API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table.

.. include:: API_Bindings_JavaScript_links.table

Further project descriptions can be found in the :ref:`kits <index_kits>` section.
