
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../Software.html">Software</a> / Firmwares and Plugins

.. _firmwares_and_plugins:

Firmwares and Plugins
=====================

.. note::
 If you accidentally erased the firmware of a Brick or Bricklet, you can
 download the latest firmware and plugin
 versions :ref:`here <downloads_firmwares_plugins>`.

 Only if you want to change something in a firmware of a Brick or a
 plugin of a Bricklet you will need to compile them yourself.

.. _building_brick_firmware:

Building a Brick firmware
-------------------------

You can modify and build the Brick firmwares. At the moment there is no
official Brick API or documentation of the Brick firmware code. So you
will need some prior knowledge in C programming to do this.

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`github account <https://github.com/Tinkerforge/>`__. In the following
a small overview on what you have to do to compile the Servo Brick firmware,
as an example.

Clone the Servo Brick repository::

 git clone https://github.com/Tinkerforge/servo-brick.git

Clone the bricklib into the ``software/src/`` folder of the firmware (a symlink
will also work)::

 cd servo-brick/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

Download and install the GCC none-eabi compiler for ARM from
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__.
Ensure to use a :ref:`compatible compiler <compiler_compatibility>` version.

Ensure that the ``bin`` folder of the CodeSourcery installation is added to the
``PATH`` environment variable, otherwise CMake will not be able to find the
compiler tools.

Generate the Makefile in the ``software/`` folder (you will need CMake)::

 cd servo-brick/software/
 ./generate_makefile

Build the firmware::

 cd servo-brick/software/build/
 make

That's it. The ``software/build/`` folder now contains the newly compiled firmware.
``servo-brick.bin``.


.. _flash_firmware_on_brick:

Flash firmware on a Brick
-------------------------

See :ref:`brickv_flash_firmware` in :ref:`Brick Viewer <brickv>` documentation
for more information.

.. _building_bricklet_plugin:

Building a Bricklet plugin
--------------------------

You can modify and build the Bricklet plugins.
You will need knowledge in C programming to do this. The plugins are
compiled as position independent code (so it is easy for the Bricks to
use them). This means that there are lots of C features you might take
for granted that will not work in Bricklet plugins. For example you
can not just call any library functions, the functions have to be provided
by the Brick through the Bricklet API (BA). Global variables have to be
written into the Bricklet Context (BC) and configuration for the Bricklet
can be read from the Bricklet Settings (BS). All of these are provided
by the Bricks to be used by Bricklet plugins. If you think you are up
to that, you should take a look at the source code to see how it exactly
works.

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`Github account <https://github.com/Tinkerforge/>`__. In the following
a small overview on what you have to do to compile the Joystick Bricklet
plugin, as an example.

Clone the Joystick Bricklet repository::

 git clone https://github.com/Tinkerforge/joystick-bricklet.git

Clone the bricklib and the brickletlib (you need both) into the ``software/src/``
folder of the plugin (a symlink will also work)::

 cd joystick-bricklet/software/src
 git clone https://github.com/Tinkerforge/bricklib.git
 git clone https://github.com/Tinkerforge/brickletlib.git

Download and install the GCC none-eabi compiler for ARM from
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__.
Ensure to use a :ref:`compatible compiler <compiler_compatibility>` version.

Generate the Makefile in the ``software/`` folder (you will need CMake)::

 cd joystick-bricklet/software
 ./generate_makefile

Build the plugin::

 cd joystick-bricklet/software/build/
 make

That's it. The ``software/build/`` folder now contains the newly compiled plugin:
``joystick-bricklet.bin``


Flash plugin on a Bricklet
--------------------------

See :ref:`brickv_flash_plugin` in :ref:`Brick Viewer <brickv>` documentation for
more information.


.. _compiler_compatibility:

Compiler Compatibility
----------------------

The GCC none-eabi compiler for ARM from
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__.
is required.
There are versions of this compiler that do not produce working firmwares.
It's recommended to only use compiler versions that are known to work correctly,
see the following list:

.. csv-table::
   :header: "Version", "Works"
   :widths: 25, 5

   "Sourcery CodeBench Lite 2011.09-69, GCC 4.6.1", "Yes"
   "Sourcery CodeBench Lite 2012.03-56, GCC 4.6.3", "Yes"
   "Sourcery CodeBench Lite 2012.09-63, GCC 4.7.2", "No"
   "Sourcery CodeBench Lite 2013.05-23, GCC 4.7.3", "Yes"
