
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="Firmwares_And_Plugins.html">Firmwares and Plugins</a> / Building a Brick Firmware

.. _building_brick_firmware:

Building a Brick Firmware
=========================

In the following a small overview on what you have to do to compile the
Servo Brick firmware is given as an example. This requires that the necessary
compiler and tools are installed as described :ref:`here
<firmwares_and_plugins_install>`.


Getting the Source Code
-----------------------

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`GitHub account <https://github.com/Tinkerforge/>`__. The repository for the
Servo Brick can be found `here <https://github.com/Tinkerforge/servo-brick>`__.

You can either download the repository content as a `ZIP file
<https://github.com/Tinkerforge/servo-brick/archive/master.zip>`__ or use git
directly to clone the repository::

 git clone https://github.com/Tinkerforge/servo-brick.git

The bricklib provides common functionality for all Bricks. You can either
download the bricklib repository content as a `ZIP file
<https://github.com/Tinkerforge/bricklib/archive/master.zip>`__ or use git
directly to clone the repository. The bricklib folder goes into the
``software/src/`` folder of the firmware (a symlink will also work)::

 cd servo-brick/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

In the downloaded ZIP files the bricklib folder is named ``bricklib-master``,
ensure to rename it to ``bricklib``. The folder structure is correct if the
path ``servo-brick/software/src/bricklib/com/com.h`` exists.


Compiling the Source Code
-------------------------

First, a Makefile has to be generated from the CMake project configuration.
For this the ``generate_makefile`` script in the ``software/`` folder has to be
executed::

 cd servo-brick/software/
 ./generate_makefile

On Windows ``generate_makefile.bat`` has to be executed instead of
``./generate_makefile``. This has to be done initially once and if the CMake
project configuration is changed.

Now the firmware can be compiled::

 cd servo-brick/software/build/
 make

You might see this error message at the end on Linux::

 make[2]: S: Command not found

or this one on Windows::

 process_begin: CreateProcess(NULL, S -O binary servo-brick.elf servo-brick.bin, ...) failed.
 make (e=2): The system cannot find the file specified.

In order to fix this you have to run the ``generate_makefile`` script a second
time. It is currently unknown why it helps but it does help. Then also run
``make`` again.

That's it. The ``software/build/`` folder now contains the newly compiled
firmware: ``servo-brick.bin``. It can be flashed to be Brick with the
:ref:`Brick Viewer <brickv_flash_firmware>`. Just select "Custom..." instead
of "Servo" in the Flashing dialog and pick the newly compiled firmware file.
