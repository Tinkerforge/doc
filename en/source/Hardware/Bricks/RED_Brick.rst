
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. note::
 This Brick is under development and not yet available. 

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_red_prototype_350.jpg",
	               "Bricks/brick_red_prototype_600.jpg",
	               "RED Brick Prototype")
	}}
	{{ tfdocend() }}


Features
--------

* Controls other Bricks and Bricklets
* Executes directly your program
* Supports nearly every language

.. _red_brick_description:

Description
-----------

.. note::
 This Brick is under development and not yet available. Planned release: Dec. 2014. 

 You can find news in our `blog <http://www.tinkerforge.com/en/blog/>`__.  Blog posts so far:

 * `Tinkerforge goes Stand-Alone aka RED Brick <http://www.tinkerforge.com/en/blog/2014/2/21/tinkerforge-goes-stand-alone-aka-red-brick>`__
 * `RED Brick circuit boards arrived <http://www.tinkerforge.com/en/blog/2014/4/10/red-brick-circuit-boards-arrived>`__
 * `RED Brick news <http://www.tinkerforge.com/en/blog/2014/5/13/red-brick-news>`__
 * `RED Brick: Does it work? <http://www.tinkerforge.com/en/blog/2014/5/23/red-brick:-does-it-work>`__
 * `RED Brick Software Infrastructure <http://www.tinkerforge.com/en/blog/2014/6/20/red-brick-software-infrastructure>`__
 * `RED Brick in EMC laboratory <http://www.tinkerforge.com/en/blog/2014/8/28/red-brick-in-emc-laboratory>`__
 * `RED Brick status report <http://www.tinkerforge.com/en/blog/2014/10/16/red-brick-status-report>`__

The Rapid Embedded Development Brick (RED Brick) can control other
Bricks and Bricklets. Currently supported languages as: C/C++, C#, 
Delphi/Lazarus, Java, JavaScript, MATLAB/Octave, Perl, PHP, Python, Ruby, Shell 
and Visual Basic .NET can be directly executed on the Brick.

A program that controls Bricks and Bricklets can be written and tested 
on a normal PC/Mac. Afterwards the program can be transferred to the RED Brick
by the press of a button and can be executed without any changes. Multiple 
programs can be executed simultaneously, whereas their execution can be 
configurated (permanently execution, every X seconds etc.) and monitored.

This approach enables a very easy and very fast solution for embedded 
programming. To our knowledge there is no other solution available that is
even remotely comparable. 

For each supported programming language the Tinkerforge API and commonly used 
software libraries are preinstalled on the system. Other necessary libraries can 
be manually installed.

The Brick is equipped with a Micro-HDMI connector, such that it can also used 
for programs with graphical user interface. A onboard USB 2.0 Host connector 
supports input and pointing devices, such that keyboards, mouses or touchscreens 
can be also connected and used.

With an Ethernet Master Extension the RED Brick can be extended by an Ethernet 
interface. The RS485 Master Extension is also supported by the Brick and let you 
interconnect the controlling RED Brick with other remote stacks of Bricks and 
Bricklets.

Advanced users can use the module with full access on the underlying Debian 
system. Over a GPIO FPC header, the export user can directly access 
different processor pins and can use them in his own developments.




Technical Specifications
------------------------

=============================  ============================================================================
Property                       Value
=============================  ============================================================================
Dimensions (W x D x H)         40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                         TBD g
Power Consumption              TBD mW or 5V/TBDmA (idle), TBD mW or 5V/TBDmA (100% load)
-----------------------------  ----------------------------------------------------------------------------

-----------------------------  ----------------------------------------------------------------------------
Processor                      Allwinner A10s, Cortex A8 1GHz, 3D Mali400 GPU, NEON
Memory                         512MB DDR3 SDRAM, Micro SD Card as Flash
Connectors                     USB2.0, micro HDMI (type D), micro USB, Stack connectors, GPIO FPC connector
=============================  ============================================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/red-brick/raw/master/hardware/red-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/red_brick_dimensions.png>`__)
* Linux image and hardware design files (`Download <https://github.com/Tinkerforge/red-brick/zipball/master>`__)

.. _red_brick_test:

Quickstart / Test your RED Brick
--------------------------------

* Install Brick Viewer, Bricks
* Insert Micro SD Card with Fast or Full Image
  * ready to use images from shop
  * copy image (min. class 10 recommended)
* Connect RED Brick to PC by Micro USB
* Click through tabs

Full image users can connect HDMI monitor and USB hub with keyboard and mouse
and work with the LXDE desktop environment.

.. _red_brick_hardware:

Hardware Description
--------------------

TODO: Overview Image


Power Button
^^^^^^^^^^^^

TODO: Image of Power Button

The button on the RED Brick is a power button. Press it longer than 5 seconds
and the RED Brick will immediately turn off. If you press it shorter, the 
Brick will not start to power down. This feature is not supported at the 
moment. If the Brick is off, press the button until the blue LED lights up and 
the Brick starts booting. 

.. _red_brick_leds:

LEDs
^^^^

TODO: Image of RED Brick with arrows to LEDs

The RED Brick has three LEDs on the top side: A blue, a red and a green LED.

The blue LED is directly connected to the internal power supply of the 
processor. The LED is on if the Brick is powered.

The red LED shows if an error is present. If the red LED stays on during 
startup, no image could be found. There may be no sd card inserted or there is 
no valid image on the sd card.

The green LED shows the current state. If on startup the red LED is off
and the green LED does not turn on, Linux couldn't start booting. During
boottime the green LED turns on. After the RED Brick has booted up
and all of the services are available the green led starts showing a
heartbeat.

You can change the function of the green LED after bootup to `show
cpu or sd card usage <TODO>`__ instead of a heartbeat.

SD Card Slot
^^^^^^^^^^^^

TODO: Image of SD Card Slot

The linux system and your data is stored on a Micro SD card. The slot
is located on the bottom side of Brick. 
Micro SD cards (Version 1.0), Micro SDHC (2.0) and Micro SDXC (3.0) cards
are supported. We recommend as a minimum a class 10 Micro SD Card to ensure
fast reads and writes.

A description of the images can be found in the 
:ref:`image section <red_brick_images>`.


USB 2.0 Host Port
^^^^^^^^^^^^^^^^^

TODO: Image of USB Port

The RED Brick is equipped with a standard USB 2.0 (480Mbps) type A jack.
All human input devices, which are supported by a standard Debian Linux system,
are supported and can be directly used to control the graphical user interface
(for :ref:`full image <red_brick_images_full>`).

Other devices, like webcams, printers etc. are also supported but may have to be
configured directly on the linux system.

The RED Brick can power other USB devices with up to 7.5W (5V/1.5A). The port is
short circuit protected.

USB Mini Connector
^^^^^^^^^^^^^^^^^^

TODO: Image of USB Mini connector

With the mini USB connector, the RED Brick can be configured and is controllable
by the :ref:`RED Brick API <red_brick_programming_interface>`. It can also be 
used to power the Brick.

Micro-HDMI Connector
^^^^^^^^^^^^^^^^^^^^

TODO: Image HDMI connector

With the Micro `HDMI <http://en.wikipedia.org/wiki/HDMI>`__ connector 
(also called type D), all standard monitors and televisions can be connected to 
the RED Brick. The connector is active only in the 
:ref:`full image <red_brick_images_full>`. HDMI Ethernet Channel (HEC) is not 
supported.


Brick Stack Connector
^^^^^^^^^^^^^^^^^^^^^

TODO: Image Stack connector

Up to eight other Bricks can be stacked on top of the RED Brick and can be 
directly controlled by it. Additionally up to two Master Extensions can
be used with the RED Brick. At the moment the RS485 Extension all versions of 
the Ethernet Extension are supported and can be used as a typical Ethernet 
interface. A Step Down Power Supply can be stacked below the RED Brick and can 
power it.

GPIO Header
^^^^^^^^^^^

.. note:: 

   This header is intended for advanced users to connect their own hardware. 
   There is no software support in the moment for any function of this GPIO
   connector.

TODO Image Header

The RED Brick is equipped with a 21 pin, 0.25mm pitch, FPC GPIO connector
(Type Molex 502078-2110).

All signals of Port E of the A10s processor are connected to this GPIO 
connector. These signals can be configured for several functions:

General Purpose Input/Output, Transport Stream Controller (TS), Camera Sensor
Interface (CSI), Serial Peripheral Interface (SPI), Secure Digital Memory 3.0 
Card Controller (SDC), Universal Asynchronous Receiver Transmitter (UART), 
Interrupt capable. Additionally a I2C (TWI) interface is connected to this GPIO.

==== ======== ===================================================
Pin  Signal   Description
==== ======== ===================================================
1    5V       5V Power Supply
2    3V3      3V3 Power Supply
3    PE0      TS Clock, CSI Pixel Clock, SPI Chip Select 0, INT14
4    GND      Ground
5    PE1      TS Error, CSI Sensor Clock, SPI Clock, INT15
6    GND      Ground
7    PE2      TS Sync, CSI Horizontal Sync, SPI MOSI
8    GND      Ground
9    PE3      TS Data Valid, CSI Vertical Sync, SPI MISO
10   GND      Ground
11   PE4      TS Data 0, CSI Data 0, SD Controller Data 0
12   PE5      TS Data 1, CSI Data 1, SD Controller Data 1
13   PE6      TS Data 2, CSI Data 2, SD Controller Data 2
14   PE7      TS Data 3, CSI Data 3, SD Controller Data 3
15   PE8      TS Data 4, CSI Data 4, SD Controller Command
16   PE9      TS Data 5, CSI Data 5, SD Controller Clock
17   PE10     TS Data 6, CSI Data 6, UART TX
18   PE11     TS Data 7, CSI Data 7, UART RX
19   GND      Ground
20   PB15     I2C Clock (with 2k2 Pullup)
21   PB16     I2C Data (with 2k2 Pullup)
==== ======== ===================================================


Power Supply
^^^^^^^^^^^^

The RED Brick needs to be powered by a 5V supply. It can be powered by 
the mini USB connector or a Step Down Power Supply. The single RED Brick needs
up to TODO Watts, so that a typical 5W (5V/1A) USB power supply will suffice to
power it and a Master Brick with a few connected Bricklets. If you use a 
larger setup, calculate the power requirements and choose a suitable power 
supply with enough power reserves. Don't forget to calculate the consumption of 
connected USB 2.0 devices in.

.. _red_brick_images:

RED Brick Software Images
-------------------------

The RED Brick software image is stored on a Micro SD-Card. It is a modified
Debian image and available in two different versions. The ''Full'' and the 
''Fast'' image. Both images supports the execution of your code. The difference 
between both image is the support of graphical user interfaces.


.. _red_brick_images_full:

Full Image
^^^^^^^^^^

TODO: user/password?

This image comes with installed HDMI drivers and all necessary graphical user 
interface libraries. The complete List of installed libraries and programs can
be found `here <TODO_Link>`.

It boots an X server and the LXDE desktop environment with auto login. 
If the program you run on the RED Brick uses a graphical interface it will show
up on the desktop. The typical screen resolution is TODO. If you want to change 
the screen resolution configure it over LXDE. Of course you don't have to use 
the HDMI port and can execute non graphical programs on this image.

See the `installing section TODO <TODO>` on how to install new software.

The full image can be downloaded `here <TODO_Link_to_download_page>`__.


.. _red_brick_images_fast:

Fast Boot Image
^^^^^^^^^^^^^^^

TODO: user/password?

The fast boot image is optimized for a fast boot. It lacks the support of HDMI
and graphical user interfaces. The complete List of installed libraries and 
programs can be found `here <TODO_Link>`.

The fast image can be downloaded `here <TODO_Link_to_download_page>`__.



Build your Own Image
^^^^^^^^^^^^^^^^^^^^

TODO: Explain here?

Copy Image on SD Card
^^^^^^^^^^^^^^^^^^^^^

TODO: on Windows, Linux, Mac, (micro sd card size minimum?)



Configuration (in Brick Viewer)
-------------------------------

This section describes the configuration of the RED Brick with the Brick Viewer
Software. The configuration can also be done by the 
:ref:`RED Brick API <red_brick_programming_interface>`.

TODO: Necessary software, connecting process, tab description

Program Upload and Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TODO: Describe GUI and link to RED Brick Tutorial

Ethernet
^^^^^^^^

RS485
^^^^^

Shell (Remote Access)
^^^^^^^^^^^^^^^^^^^^^

TODO: HINT to ACM0, Link Beginners shell tutorial

Version and Library Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _red_brick_faq:

FAQ
---

* Q: I connected the RED Brick to my Linux PC. Why is there no ``/dev/ttyACM0``
  device to access its serial console?
* A: The ``cdc_acm`` driver has to be loaded for this to work.




.. _red_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RED_Brick_hlpi.table
