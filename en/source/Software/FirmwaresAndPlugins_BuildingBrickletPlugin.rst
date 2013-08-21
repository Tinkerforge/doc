
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="Firmwares_And_Plugins.html">Firmwares and Plugins</a> / Building a Bricklet Plugin

.. _building_bricklet_plugin:

Building a Bricklet Plugin
==========================

The Bricklet plugins are compiled as position independent code (so it is easy
for the Bricks to use them). This means that there are lots of C features you
might take for granted that will not work in Bricklet plugins. For example you
can not just call any library functions, the functions have to be provided
by the Brick through the Bricklet API (BA). Global variables have to be
written into the Bricklet Context (BC) and configuration for the Bricklet
can be read from the Bricklet Settings (BS). All of these are provided
by the Bricks to be used by Bricklet plugins. If you think you are up
to that, you should take a look at the source code to see how it exactly
works.

In the following a small overview on what you have to do to compile the
Joystick Bricklet plugin, as an example. This requires that the necessary
compiler and tools are installed as described :ref:`here
<firmwares_and_plugins_install>`.


Getting the Source Code
-----------------------

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`GitHub account <https://github.com/Tinkerforge/>`__. The repository for the
Joystick Bricklet can be found `here
<https://github.com/Tinkerforge/joystick-bricklet>`__.

You can either download the repository content as a `ZIP file
<https://github.com/Tinkerforge/joystick-bricklet/archive/master.zip>`__ or use
git directly to clone the repository::

 git clone https://github.com/Tinkerforge/joystick-bricklet.git

The brickletlib provides common functionality for all Bricklets. You can either
download the brickletlib repository content as a `ZIP file
<https://github.com/Tinkerforge/brickletlib/archive/master.zip>`__ or use git
directly to clone the repository. The brickletlib folder goes into the
``software/src/`` folder of the plugin (a symlink will also work)::

 cd joystick-bricklet/software/src/
 git clone https://github.com/Tinkerforge/brickletlib.git

In the downloaded ZIP files the bricklib folder is named ``brickletlib-master``,
ensure to rename it to ``brickletlib``. The folder structure is correct if the
path ``joystick-bricklet/software/src/brickletlib/bricklet_entry.h`` exists.

Beside the brickletlib the bricklib is also required. You can either
download the bricklib repository content as a `ZIP file
<https://github.com/Tinkerforge/bricklib/archive/master.zip>`__ or use git
directly to clone the repository. The bricklib folder goes into the
``software/src/`` folder of the plugin (a symlink will also work)::

 cd joystick-bricklet/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

In the downloaded ZIP files the bricklib folder is named ``bricklib-master``,
ensure to rename it to ``bricklib``. The folder structure is correct if the
path ``joystick-bricklet/software/src/bricklib/com/com.h`` exists.


Compiling the Source Code
-------------------------

First, a Makefile has to be generated from the CMake project configuration.
For this the ``generate_makefile`` script in the ``software/`` folder has to be
executed::

 cd joystick-bricklet/software/
 ./generate_makefile

On Windows ``generate_makefile.bat```has to be executed instead of
``./generate_makefile``. This has to be done initially once and if the CMake
project configuration is changed.

Now the firmware can be compiled::

 cd joystick-bricklet/software/build/
 make

You might see this error message at the end on Linux::

 make[2]: S: Command not found

or this one on Windows::

 process_begin: CreateProcess(NULL, S -O binary joystick-bricklet.elf joystick-bricklet.bin, ...) failed.
 make (e=2): The system cannot find the file specified.

In order to fix this you have to run the ``generate_makefile`` script a second
time. It is currently unknown why it helps but it does help. Then also run
``make`` again.

That's it. The ``software/build/`` folder now contains the newly compiled
plugin: ``joystick-bricklet.bin``. It can be flashed to be Bricklet with the
:ref:`Brick Viewer <brickv_flash_plugin>`. Just select "Custom..." instead of
"Joystick" in the Flashing dialog and pick the newly compiled plugin file.
