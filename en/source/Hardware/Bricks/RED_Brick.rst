
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

The Rapid Embedded Development :ref:`Brick <primer_bricks>` (RED Brick) can 
control other :ref:`Bricks <primer_bricks>` and 
:ref:`Bricklets <primer_bricklets>`. Currently supported languages as: C/C++, C#, 
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

For each supported programming language the :ref:`Tinkerforge API <api_bindings>` 
and commonly used software libraries are preinstalled on the system. Other 
necessary libraries can be manually installed.

The Brick is equipped with a `Micro-HDMI <http://en.wikipedia.org/wiki/HDMI>`__
connector, such that it can also used 
for programs with graphical user interface. An onboard 
`USB2.0 <http://en.wikipedia.org/wiki/USB>`__ Host connector supports input and 
pointing devices, such that keyboards, mouses or touchscreens can be also 
connected and used.

With an :ref:`Ethernet Master Extension <ethernet_extension>` the RED Brick can 
be extended by an Ethernet interface. The 
:ref:`RS485 Master Extension <rs485_extension>` is also supported by the Brick 
and let you interconnect the controlling RED Brick with other remote stacks of 
Bricks and Bricklets.

Advanced users can use the module with full access on the underlying 
`Debian <http://www.debian.org>`__ 
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

As a first step install the :ref:`Brick Daemon <brickd>` and the
:ref:`Brick Viewer <brickv>` software on your PC or Mac. Insert the SD Card into 
the :ref:`SD Card slot <red_brick_sd_card_slot>` (you can order a SD Card with
preinstalled image or you have to 
:ref:`copy it on your card <red_brick_copy_image>`). After that your RED Brick
is ready to go and can be connected to your PC or Mac with a micro USB cable.

TODO: Image RED Brick with micro USB cable connected

If you start the Brick Viewer software and press "connect". A tab should show up
labeled with "RED Brick". Click on it.

TODO: Image RED Brick Tab.

On the left side of the tab you see different additional tabs. The "Overview" 
tab should be selected and should show different information about the CPU load, 
memory usage and different other status informations. This means your RED Brick
works as expected and you can start to upload your program. See the 
:ref:`Brick Viewer Chapter <red_brick_brickv>` on how to configure the Brick
and how to upload your programs.

Users of the :ref:`Full image <red_brick_images>` can test the graphical 
interface. To do so, connect an monitor to the 
:ref:`HDMI Port <red_brick_hdmi_port>` and a USB hub with keyboard and 
mouse to the :ref:`USB2.0 Port <red_brick_usb2_port>` of the RED Brick and see 
the LXDE desktop environment booting. After the boot process you should work 
with it as expected.

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

.. _red_brick_sd_card_slot:

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

.. _red_brick_usb2_port:

USB2.0 Host Port
^^^^^^^^^^^^^^^^

TODO: Image of USB Port

The RED Brick is equipped with a standard 
`USB2.0 <http://en.wikipedia.org/wiki/USB>`__ (480Mbps) type A jack.
All human input devices, which are supported by a standard Debian Linux system,
are supported and can be directly used to control the graphical user interface
(for :ref:`full image <red_brick_images>`).

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


.. _red_brick_hdmi_port:

Micro-HDMI Port
^^^^^^^^^^^^^^^

TODO: Image HDMI connector

With the Micro `HDMI <http://en.wikipedia.org/wiki/HDMI>`__ connector 
(also called type D), all standard monitors and televisions can be connected to 
the RED Brick. The connector is active only in the 
:ref:`full image <red_brick_images>`. HDMI Ethernet Channel (HEC) is not 
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
connected USB2.0 devices in.

.. _red_brick_images:

RED Brick Software Images
-------------------------

The RED Brick software image is stored on a Micro SD-Card. It is a modified
`Debian <http://www.debian.org/>`__ image and available in two different 
versions. The ''full'' and the ''fast'' image. Both images supports the 
execution of your code. 

The **full image** comes with installed `HDMI <http://en.wikipedia.org/wiki/HDMI>`__
drivers and all necessary graphical user interface libraries. 
It boots an X server and the `LXDE desktop environment <http://www.lxde.org>`__ 
with auto login. If the program you run on the RED Brick uses a graphical 
interface it will show up on the desktop. The typical screen resolution is TODO. 
To change the screen resolution you have to configure it over LXDE. Of course 
you don't have to use the HDMI port and can execute non graphical programs on 
this image.

The **fast image** comes without graphical interface support and has no X, LXDE 
and other graphical libraries preinstalled. Drivers for HDMI are also missing. 
It is optimized for a fast boot time.

TODO: Check. On both images new software can be installed.
See the `installing section TODO <TODO>` on how to install new software.

The complete list of installed libraries and programs can be found below:

* `Full Image Installed Programs List <TODO_Link_to_download_page>`__.
* `Fast Image Installed Programs List <TODO_Link_to_download_page>`__.

If you want to log in the linux system by command line or LXDE, the standard 
user is **tf** with default password **tf**. The user is a sudoer, such that you 
can gain root access.

The images can be downloaded from the:
`Download Page <TODO_Link_to_download_page>`__.




.. _red_brick_build_image:

Build your Own Image
^^^^^^^^^^^^^^^^^^^^

TODO: Explain here?

.. _red_brick_copy_image:

Copy Image on SD Card
^^^^^^^^^^^^^^^^^^^^^

 1) At first you should download the 
 :ref:`full image or the fast image <red_brick_images>` of the RED Brick:
 `Download Page  <TODO_Link_to_download_page>`__


 2) Choose a suitable SD Card. We recommend a fast SD Card (e.g. class 10) with
 enough space. You find the size of the image on the download page.

 3) Transfer the image on the SD Card:
 
 * On Windows use a tool like Win32DiskImager to transfer the image to the card.

   * `Download Link <https://http://sourceforge.net/projects/win32diskimager/files/latest/download>`__ 
   * `Documentation <http://sourceforge.net/p/win32diskimager/wiki/Home/>`__

 * On Mac OS and Linux

   * Connect the SD Card to your PC 
   * Identify the path to your SD Card (e.g. dmesg)
   * sudo dd if=path_of_your_image.img of=path_to_sdcard bs=1M

      * e.g.: dd if=/tmp/red_full_image.img of=/dev/sdb bs=1M


.. _red_brick_brickv:

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
