
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-javascript">Software</a> / JavaScript - API Bindings

.. _api_bindings_javascript:

JavaScript - API Bindings
=========================

The JavaScript bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your JavaScript programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``nodejs/tinkerforge.tgz``, a Node.js NPM package (installable with `npm
  <https://www.npmjs.org/>`__ tool)
* in ``nodejs/source/`` the source code of ``tinkerforge.tgz``
* in ``nodejs/examples/`` the Node.js examples for every Brick and Bricklet
* in ``browser/source/`` the source code of the browser version of the bindings
* in ``browser/examples/`` the HTML examples for every Brick and Bricklet


Requirements
------------

* Node.js 0.10 or newer, or any recent browser with WebSocket support (tested
  with Chrome, Firefox and Internet Explorer)


.. _api_bindings_javascript_install:

Installation
------------

If and how the JavaScript bindings should or have to be installed depends on
how they should be used.

Node.js
^^^^^^^

The Node.js version of the bindings can be installed with the Node.js Package
Manager `npm <https://www.npmjs.org/>`__, but you don't have to.

From NPM Package
""""""""""""""""

There is a NPM package available for using the Bindings with Node.js. It is
available from the `Node.js Package Repository
<https://www.npmjs.org/package/tinkerforge>`__ and can be installed globally
with the following command which might has to execute with ``sudo`` or as
administrator::

 npm -g install tinkerforge

Alternatively, the NPM Package is also part of the ZIP file of the bindings. It
can be installed globally from there as well with the following command which
might has to execute with ``sudo`` or as administrator::

 npm -g install nodejs/tinkerforge.tgz

Now you're ready to test the examples. The NPM package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

Without Installation
""""""""""""""""""""

You can use the JavaScript bindings for Node.js without having to install them.
Just copy the ``Tinkerforge/`` folder and the ``Tinkerforge.js`` file from the
``nodejs/source/`` folder in the same folder as your JavaScript program. The
section about testing an example has more details about this.

HTML
^^^^

The browser version of the bindings can be found in the ``browser/source/``
folder. The ``Tinkerforge.js`` file contains the complete bindings. Just copy
this file into the same directory as your HTML file using the bindings. The
section about testing an example has more details about this.


Testing an Example
------------------

To test a JavaScript example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

Node.js
^^^^^^^

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``ExampleConfiguration.js`` file from the
``nodejs/examples/Brick/Stepper/`` folder into a new folder::

 example_project/
  -> ExampleConfiguration.js

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: javascript

  var HOST = 'localhost';
  var PORT = 4223;
  var UID = 'XYZ'; // Change to your UID

If you did install the bindings using the NPM package then you're now ready to
test this example::

 node ExampleConfiguration.js

If you did **not** install the bindings then you can also use the source of the
bindings directly. Just copy the ``Tinkerforge/`` folder and the
``Tinkerforge.js`` file from the ``nodejs/source/`` folder to your
``example_project/`` folder::

 example_project/
  -> Tinkerforge/
  -> Tinkerforge.js
  -> ExampleConfiguration.js

Then the  ``require`` statement in ``ExampleConfiguration.js`` has to be
modified as follows. Instead of:

.. code-block:: javascript

  var Tinkerforge = require('tinkerforge');

use:

.. code-block:: javascript

  var Tinkerforge = require('./Tinkerforge.js');

Now you're ready to test this example::

 node ExampleConfiguration.js


HTML
^^^^

The Browser version of the JavaScript bindings is using `WebSockets
<http://en.wikipedia.org/wiki/WebSocket>`__.
WebSockets are supported by Brick Daemon (since version 2.1.0) and the
Ethernet Extension (since Master Brick firmware version 2.2.0), but they are
disabled by default and need to be configured first:

* :ref:`Brick Daemon: WebSockets <brickd_websockets>`
* :ref:`Ethernet Extension: WebSockets <ethernet_configuration_websockets>`

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``ExampleConfiguration.html`` file from the
``browser/examples/Brick/Stepper/`` folder and the ``Tinkerforge.js`` file
from the ``browser/source/`` folder into a new folder::

 example_project/
  -> Tinkerforge.js
  -> ExampleConfiguration.html

Now you're ready to open this example in a browser.

The example contains input boxes for host and port information. You have to
specify at which network address the Stepper Brick can be found. If it is
connected locally to USB then ``localhost`` and 4280 is correct. The UID value
has to be changed to the UID of the connected Stepper Brick, which you can
figure out using Brick Viewer. If every<thing is configured correctly you can
start the example the clicking the "Start Example" button.


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_JavaScript_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_JavaScript>
   Bricks <Bricks_JavaScript>
   Bricklets <Bricklets_JavaScript>
