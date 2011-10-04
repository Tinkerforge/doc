.. _tools_installation:

Tools Installation
==================

.. _tools_installation_brickdv:

Brickd/ Brickv
--------------


.. _tools_installation_bindings:

Programming Language Bindings
-----------------------------

C/C++
^^^^^

MinGW (Windows)
"""""""""""""""

Visual Studio (Windows)
"""""""""""""""""""""""

GCC/G++ (Linux/ MacOS)
""""""""""""""""""""""

C#
^^

Java
^^^^

Python
^^^^^^


Build our firmwares
-------------------

You can build our supplied firmwares from scratch and apply your own
code modifications. What you have to do:

* Check out the firmware git repository::

    e.g.: git clone https://github.com/Tinkerforge/servo-brick.git

* Check out our bricklib src directory of the firmware (a symlink will also work)::

    e.g.: cd servo-brick/software/src; git clone https://github.com/Tinkerforge/bricklib.git

* Download and install an gcc none-eabi compiler:

   e.g. from `CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`_

* Download and install cmake::

    e.g. apt-get install cmake

* Generate the Makefile in software folder::

    e.g.: cd ../; ./generate_makefile

* build the firmware::

    e.g.: cd build/; make


Flash firmware on a Brick
-------------------------

TODOTODOTODO: kernel treiber bei linux?

* Download SAM-BA

   from `Atmel <http://www.atmel.com/dyn/products/tools_card.asp?tool_id=3883>`_

* Copy all files in tcl_lib of the brickboot repository to the tcl_lib folder 
  of SAM-BA::

    e.g. git clone https://github.com/Tinkerforge/bricklib.git
         cp -r bricklib/tcl_lib/* /srv/sam-ba/tcl-lib/

* Append the following lines to `array set boards` in file `tcl_lib\boards_tcl`
  of your SAM-BA installation::

    "at91sam3s2-brick"     "at91sam3s2-brick/at91sam3s2-brick.tcl"
    "at91sam3s4-brick"     "at91sam3s4-brick/at91sam3s4-brick.tcl"

* Set Brick in bootloader

   Press `Erase` botton of the Brick and release it after a short press on 
   `Reset` button. The blue LED should be off.


* Start SAM-BA, choose your connection and choose `at91sam3s4-brick` for our 
   Master Brick and `at91sam3s2-brick` for all other Bricks.
   Click connect, after this the blue LED should be on. 
   Select your firmware (bin) file as `Send File Name` and click send. 
   Answer `Yes` to lock regions.
   At the end select `Boot from Flash (GPNVM1)` script and execute it. 
   Reset the Brick or cycle power and it should start with the new firmware.


Building a plugin for a Bricklet
--------------------------------

Basically it is the same like building a Brick firmware but additionally you need
the brickletlib. What you have to do:

* Check out the plugin git repository::

    e.g.: git clone https://github.com/Tinkerforge/joystick-bricklet.git

* Check out our bricklib src directory of the firmware (a symlink will also work)::

    e.g.: cd joystick-bricklet/software/src; git clone https://github.com/Tinkerforge/bricklib.git

* Check out our brickletlib src directory of the firmware (a symlink will also work)::

    e.g.: git clone https://github.com/Tinkerforge/brickletlib.git

* Download and install an gcc none-eabi compiler:

   e.g. from `CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`_

* Download and install cmake::

    e.g. apt-get install cmake

* Generate the Makefile in software folder::

    e.g.: cd ../; ./generate_makefile

* build the firmware::

    e.g.: cd build/; make


Flash plugin on a Bricklet
--------------------------

See :ref:`brickv_flash_plugin` in :ref:`brickv` documentation for more information.
