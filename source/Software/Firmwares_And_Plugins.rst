.. _firmwares_and_plugins:

Firmwares and Plugins
=====================

.. note::

   If you accidentally erased the firmware of a Brick or Bricklet, you can 
   download the latest firmware and plugin versions 
   :ref:`here <downloads_firmwares_plugins>`.

   Only if you want to change something in a firmware of a Brick or a
   plugin of a Bricklet you will need to compile them yourself. 


Build a Brick firmware
----------------------

You can modify and build the Brick firmwares. At the moment there is no
official Brick API or documentation of the Brick firmware code. So you
will need some prior knowledge in C programming to do this.

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`github account <https://github.com/Tinkerforge/>`__. In the following
a small overview on what you have to do to compile the Servo Brick firmware,
as an example.

Clone the firmware git repository::

 git clone https://github.com/Tinkerforge/servo-brick.git

Clone the bricklib into the src/ directory of the firmware (a symlink will also work)::

 cd servo-brick/software/src
 git clone https://github.com/Tinkerforge/bricklib.git

Download and install the gcc none-eabi compiler from 
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`_

Generate the Makefile in the software/ folder (you will need cmake)::

 cd servo-brick/software 
 ./generate_makefile

Build the firmware::

 cd servo-brick/software/build/
 make

Thats it. The build/ folder now contains the newly compiled firmware.

.. _flash_firmware_on_brick:

Flash firmware on a Brick
-------------------------

To flash a Brick firmware onto a Brick, you need to install SAM-BA
and the SAM-BA Files from :ref:`here <downloads>`.

Extract the SAM-BA Files into the SAM-BA directory, it adds two new
bootloaders::

 at91sam3s2-brick
 at91sam3s4-brick

Then bring the Brick into the bootloader modus. Press the "Erase" button of 
the Brick and release it after a short press on the "Reset" button
(i.e. press erase, press reset, release reset, release erase).
The blue LED should be off.

Start SAM-BA, choose your connection and choose "at91sam3s4-brick" for the 
Master Brick and "at91sam3s2-brick" for all other Bricks.
Click connect, after this the blue LED should be on. 
Select your firmware (bin) file as "Send File Name" and click send. 
Answer "Yes" to lock regions. At the end select "Boot from Flash (GPNVM1)"
script and execute it. Power cycle the Brick and it should start with the 
new firmware.

.. note::
 If you have problems using SAM-BA on linux, you should take a look at
 `this site <http://www.at91.com/linux4sam/bin/view/Linux4SAM/SoftwareTools>`__.
 It contains tips for older linux versions and help for various
 distributions.

 Also, if you have an old linux kernel you may need to install the kernel
 driver from 
 `here <http://www.embedded-it.de/en/microcontroller/eNet-sam7X.php>`__
 (at the bottom: "SAM-BA Linux USB driver ")


Building a Bricklet plugin
--------------------------

You can modify and build the Bricklet plugins. 
You will need knowledge in C programming to do this. The plugins are
compiled as position independent code (so it is easy for the Bricks to
use them). This means that there are lots of C features you might take
for granted that will not work in Bricklet plugins. For example you
can not just call any library functions, the functions have to be provided
by the Brick through the Bricklet API (BA). Global variables have to be
written into the Bricklet Context (BC) and configurations for the Bricklet 
can be read from the Bricklet Settings (BS). All of these are provided
by the Bricks to be used by Bricklet plugins. If you think you are up
to that, you should take a look at the source code to see how it exactly
works.

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`github account <https://github.com/Tinkerforge/>`__. In the following
a small overview on what you have to do to compile the Joystick Bricklet 
plugin, as an example.

Clone the plugin git repository::

 git clone https://github.com/Tinkerforge/joystick-bricklet.git

Clone the bricklib and the brickletlib (you need both) into the src/ directory of the plugin (a symlink will also work)::

 cd joystick-bricklet/software/src
 git clone https://github.com/Tinkerforge/bricklib.git
 git clone https://github.com/Tinkerforge/brickletlib.git

Download and install the gcc none-eabi compiler from 
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`_

Generate the Makefile in the software/ folder (you will need cmake)::

 cd joystick-bricklet/software 
 ./generate_makefile

Build the plugin::

 cd servo-brick/software/build/
 make

Thats it. The build/ folder now contains the newly compiled plugin.


Flash plugin on a Bricklet
--------------------------

See :ref:`brickv_flash_plugin` in :ref:`brickv` documentation for more 
information.
