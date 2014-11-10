
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
* Executes your program directly
* Supports many high level programming languages

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
:ref:`Bricklets <primer_bricklets>`. The programming languages C/C++, C#, 
Delphi/Lazarus, Java, JavaScript, Octave, Perl, PHP, Python, Ruby, Shell
and Visual Basic .NET can be executed on the Brick.

A program that controls Bricks and Bricklets can be written and tested 
on a normal PC/Mac. Afterwards the program can be transferred to the RED Brick
by the press of a button and can then be executed without any changes. Multiple 
programs can be executed simultaneously. The execution of programs can be
scheduled (execution on boot up, every hour, etc.) and monitored.

This approach enables a very easy and very fast solution for embedded 
programming. To our knowledge there is no other solution available that is
even remotely comparable. 

For each supported programming language the :ref:`Tinkerforge API <api_bindings>` 
and commonly used software libraries are pre-installed on the system. Other 
necessary libraries can be installed manually.

The Brick is equipped with a `Micro-HDMI <http://en.wikipedia.org/wiki/HDMI>`__
connector, which can be used by programs to show a graphical user interface. A
`USB 2.0 <http://en.wikipedia.org/wiki/USB>`__ Host connector can be used to
connect WIFI dongles, mice, keyboards, touchscreens and similar.

With an :ref:`Ethernet Master Extension <ethernet_extension>` the RED Brick can 
be extended by an Ethernet interface. The 
:ref:`RS485 Master Extension <rs485_extension>` can be used to connect
other remote stacks of Bricks and Bricklets.

Advanced users can use the RED Brick with full access to the underlying 
`Debian <http://www.debian.org>`__ system. Over a GPIO FPC header, 
the expert user can directly access gpio/spi/i2c pins for individual
hardware development.




Technical Specifications
------------------------

=============================  ==============================================================================
Property                       Value
=============================  ==============================================================================
Dimensions (W x D x H)         40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                         TBD g
Power Consumption              TBD mW or 5V/TBDmA (idle), TBD mW or 5V/TBDmA (100% load)
-----------------------------  ------------------------------------------------------------------------------

-----------------------------  ------------------------------------------------------------------------------
Processor                      Allwinner A10s, Cortex A8 1GHz, 3D Mali400 GPU, NEON
Memory                         512MB DDR3 SDRAM, Micro SD Card as Flash
Connectors                     USB 2.0, micro HDMI (type D), micro USB, Stack connectors, GPIO FPC connector
=============================  ==============================================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/red-brick/raw/master/hardware/red-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/red_brick_dimensions.png>`__)
* Linux image and hardware design files (`Download <https://github.com/Tinkerforge/red-brick/zipball/master>`__)

.. _red_brick_test:

First Steps / Test your RED Brick
---------------------------------

With the following instructions you can test your RED Brick.

A full step-by-step tutorial regarding the RED Brick can be found here: 
:ref:`RED Brick Tutorial <tutorial_red_brick>`.

First install the :ref:`Brick Daemon <brickd>` and the
:ref:`Brick Viewer <brickv>` software on your PC or Mac. Insert the micro SD 
card into the :ref:`Micro SD Card slot <red_brick_micro_sd_card_slot>` of the 
RED Brick. The location of it and an overview of the different hardware 
interfaces of the RED Brick is given in the 
:ref:`Hardware Section <red_brick_hardware>`. You can order a SD card with 
pre-installed image in our shop. Otherwise you have to 
:ref:`copy the image to your card <red_brick_copy_image>`. 

After that your RED Brick is ready to go and can be connected to your PC or Mac 
with a mini USB cable.

TODO: Image RED Brick with micro USB cable connected

If you start the Brick Viewer software and press "connect". A tab should show up
labeled with "RED Brick". Click on it.

TODO: Image RED Brick Tab.

On the left side of the tab you see different additional tabs. The "Overview" 
tab shows information about the CPU load, 
memory usage and other status information. This means that your RED Brick
works as expected and you can start to upload your programs. See the 
:ref:`Brick Viewer Chapter <red_brick_brickv>` on how to configure the Brick
and how to upload your programs.

Users of the :ref:`Full image <red_brick_images>` can test the graphical 
user interface. To do so, connect a monitor to the 
:ref:`HDMI port <red_brick_hdmi>` and a USB hub with keyboard and
mouse to the :ref:`USB port <red_brick_usb_host>` of the RED Brick. If you
power the Brick you can see the LXDE desktop environment booting. After 
the boot process you should be able to use it as a normal desktop PC.


.. _red_brick_brickv:

Brick Viewer
------------

This section describes the configuration of the RED Brick with the 
:ref:`Brick Viewer <brickv>` software. The RED Brick can also be configured by 
the :ref:`RED Brick API <red_brick_programming_interface>` (not recommended).

.. image:: /Images/Screenshots/brickv_red_tab_and_labels.jpg
   :scale: 60 %
   :alt: Screenshot of tab selection and labels.
   :align: center

The RED Brick representation in Brick Viewer consists of different tabs, each 
described in detail below. Additionally the UID of the RED Brick, the position
in the stack, the name of the used image, number of timeouts and the word
*System* is shown. If you click on it, you can restart the Brick Daemon on the 
RED Brick and reboot or shut down the RED Brick itself.

Overview Tab (Status Information)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tab is selected by default. It shows the uptime of your RED Brick
and the usage of CPU, memory (RAM) and storage. You can see 
the top processes based on CPU or memory usage and the up- and download speed
of the configured network interfaces. 

.. image:: /Images/Screenshots/brickv_red_tab_overview.jpg
   :scale: 60 %
   :alt: Screenshot of overview tab.
   :align: center

The list can contain the following network interfaces

* ``lo``: This is the loopback interface. It is a local interface, used for
  the communication between your program and the local Brick Daemon.
* ``wlan0`` : This is a WIFI interface. It is created if you attach a WIFI 
  dongle to the :ref:`USB Host connector <red_brick_usb_host>`.
* ``eth0`` : This is a Ethernet interface. It is created if you attach a 
  Ethernet dongle to the :ref:`USB Host connector <red_brick_usb_host>`.
* ``tf0`` : This is the Ethernet interface created if you add an 
  :ref:`Ethernet Extension <ethernet_extension>` on top of the RED Brick.

The data in the overview tab is refreshed every 3 seconds.

.. _red_brick_brick_settings:

Settings Tab (Network, Brick Daemon, Date/Time)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _red_brick_brick_settings_network:

In the **Network section** of this tab you can configure settings
related to networking.

TODO Image General subsection

In the *General* subsection you can set the hostname and get the current network 
status. It additionally shows you the currently used network interface.

TODO Image Wireless subsection

The *Wireless* subsection is only active if you attach a USB WIFI dongle.
Supported dongles can be found in our shop (TODO Link). You can see the
currently used interface and its status, can select the interface which should 
be used. You can select an Access Point to connect, configure encryption and
set a static or dynamic IP.

TODO Image Wired subsection

The *Wired* subsection is only active if you attach a USB Ethernet dongle
or an Ethernet Master Extension. The USB dongle will show up as ``eth0``, the
Ethernet Extension as ``tf0``. To configure an interface, choose it, select if 
it should be used with a static IP or with DHCP and configure it properly.
If you have configured everything press the *Save* button.

Please note that it can take a few seconds to obtain an IP through DHCP or
to connect to a WIFI network. If the new configuration doesn't immediately
show up in the *General* subsection you likely just have to wait a little
bit and press the refresh button again.

.. _red_brick_brick_settings_brickd:

In the **Brick Daemon section** of this tab you can configure
all of the Brick Daemon settings.

.. image:: /Images/Screenshots/brickv_red_tab_settings_brickd.jpg
   :scale: 60 %
   :alt: Screenshot of settings tab showing brickd configurations.
   :align: center

The configuration includes the listen address, port, port for web sockets
and the authentication secret in the *General* subsection as well as more
low level configurations in the *Advanced* subsection. The LED trigger
for the red and green LED can also be set here.

.. _red_brick_brick_settings_date:

In the **Date/Time section** you can sync the clock of the RED Brick to
the clock of your PC. There is no battery on the RED Brick, so the
time won't be incremented if the RED Brick is not powered.

.. image:: /Images/Screenshots/brickv_red_tab_settings_date.jpg
   :scale: 60 %
   :alt: Screenshot of settings tab showing date/time configurations.
   :align: center

If you have a connection to the internet (trough the Ethernet Extension
or a USB WIFI dongle), the date and time are automatically set by
NTP. You only have to configure the timezone, which is saved even if
the RED Brick is powered down.


.. _red_brick_brickv_program:

Program Tab (Upload and Execution)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TODO: Describe GUI and link to RED Brick Tutorial

.. _red_brick_brickv_console:

Console Tab (Remote Access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you have attached the RED Brick over its 
`Mini USB Connector <red_brick_mini_usb>`__ to your PC it will also register
a USB serial interface. This serial interface can be used to access the Linux
shell of the Brick. Select the serial port of the Brick and press *Connect*.
Under Linux the typical interface is ``/dev/ttyACM0`` under Windows it is
``TODO`` and on OS X usually shows up as ``TODO``. You can log in as user 
**tf** with password **tf**. If you are not sure what the right port is test
them all, until you see the shell. It might be necessary to press ENTER to 
see the prompt. 

Below you can see a screenshot of the console showing ``htop``.

.. image:: /Images/Screenshots/brickv_red_tab_console.jpg
   :scale: 60 %
   :alt: Screenshot of console tab showing htop.
   :align: center

A good shell tutorial can be found at 
`linuxcommand.org <http://linuxcommand.org/lc3_learning_the_shell.php>`__.

Versions Tab (Daemon, Bindings and Libraries)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The versions tab shows version information of the installed Brick Daemon and
RED Brick API Daemon as well as the installed Bindings and their associated 
libraries.

.. image:: /Images/Screenshots/brickv_red_tab_versions.jpg
   :scale: 60 %
   :alt: Screenshot of versions tab.
   :align: center

If you want to use other libraries than the installed ones, you can 
:ref:`upload <red_brick_brickv_program>` them with your program or use the 
:ref:`console <red_brick_brickv_console>` to install them via ``apt-get``, 
``pip``, ``pear``, ``npm`` or similar package managers. They are all
installed in both images.

Extensions Tab (Configure, Manage)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Two :ref:`Master Extensions <master_extension>` are supported by the 
RED Brick: :ref:`Ethernet Extension <ethernet_extension>` and 
:ref:`RS485 Extension <rs485_extension>`.

**Ethernet Extension**

.. image:: /Images/Screenshots/brickv_red_tab_extension_ethernet.jpg
   :scale: 60 %
   :alt: Screenshot of extension tab showing Ethernet Extension configuration.
   :align: center

Only MAC address of the Ethernet Extension can be changed here.
Since the Ethernet Extension shows up as a normal network interface in the
underlying Linux, you can configure it like any other network interface
through the :ref:`Settings Tab <red_brick_brick_settings>`.

**RS485 Extension**

.. image:: /Images/Screenshots/brickv_red_tab_extension_rs485.jpg
   :scale: 60 %
   :alt: Screenshot of extension tab showing RS485 Extension configuration.
   :align: center

The configuration of the RS485 Extension is the same as it can be
done through a Master Brick. See the  
:ref:`RS485 Extension documentation <rs485_configuration>`.

The recommended baudrates to be used on the RED Brick are 500000, 250000,
166666, 125000, 100000, 83333, 71428, 62500, 55555, 50000, 45454 or 
41666 baud.

Changing the settings on either of the Extensions will restart the
Brick Daemon on the RED Brick, i.e. your RED Brick tab in the Brick 
Viewer will disappear for a few seconds and then pop up again. 

.. _red_brick_web_interface:

RED Brick Web Interface
-----------------------

If your RED Brick is equipped with a USB WIFI dongle, an Ethernet 
Extension or has other network connectivity, you can access a
web interface. The web interface is available at the IP of the
RED Brick or the hostname (``red-brick`` by default).

The RED Brick web interface shows the installed programs. You
can view the logs and configs of the programs as well as the
uploaded binaries.

.. image:: /Images/Screenshots/red_brick_web_interface.jpg
   :scale: 40 %
   :alt: Screenshot of RED Brick web interface.
   :align: center

Besides the default web interface you can also put your own
web interfaces on the RED Brick. Currently we support web applications
written in HTML/JavaScript, Python and PHP. If you upload an ``index.py``, 
``index.php`` or ``index.html`` the respective file will be used as 
directory index for the binary folder.

Example: If you want to write a PHP website that controls 
Bricks/Bricklets you can upload your program ``EXAMPLE`` with id 
``EXAMPLEID`` that includes an index.php as starting point. If you now 
go to the RED Brick web interface and click on the "Bin" button for the 
newly created program, you will get a link to 
``/programs/EXAMPLEID/bin``, which will directly execute the index.php 
if opened.

This way you can easily implement a webpage that shows environment information
gathered from Temperature/Barometer/Humidity Bricklets or you can
have a webpage with buttons that control Relay Bricklets, etc.

With the RED Brick it is super simple to write web applications that can
control hardware.

HTML/JavaScript
^^^^^^^^^^^^^^^

If you upload HTML with embedded JavaScript you can use the JavaScript
Bindings. They are available in the root directory, import them with::

 <script src="/Tinkerforge.js" type='text/javascript'></script>

Note that the JavaScript is executed in the browser of the user and not
on the RED Brick, so you have to connect to the IP of the RED Brick,
not localhost.

Python
^^^^^^

The webserver on the RED Brick is configured to recognize an index.py.
In your python program you have to define an index function::

 def index(req):

It will be called by the webserver.

A minimal hello world index.py might look like this::

 def index(req):
     return '<html><body>Hello World!</body></html>'

To control Bricks/Bricklets you can just import the Tinkerforge Bindings::

 from tinkerforge.ip_connection import IPConnection
 from tinkerforge.bricklet_temperature import Temperature
 # ...

The default web interface of the RED Brick uses Python. You can find it
`on github <https://github.com/Tinkerforge/red-brick/blob/master/image/patches/root-fs/common/tmp/index.py>`__.

PHP
^^^

The webserver on the RED Brick is configured to recognize an index.php.

An minimal hello world index.php might look like this::

 <?php $greeting = 'Hello World!'; ?>

 <html>
  <head>
   <title>PHP Example</title>
  </head>
  <body>
   <p><?php echo $greeting; ?><p>
   <p><?php phpinfo(); ?><p>
  </body>
 </html>

To control Bricks/Bricklets you can import the Tinkerforge Bindings::

 require_once('Tinkerforge/IPConnection.php');
 require_once('Tinkerforge/BrickletTemperature.php');
 // ...

.. _red_brick_images:

RED Brick Software Images
-------------------------

The RED Brick software image is stored on a Micro SD-Card. It is a modified
`Debian <http://www.debian.org/>`__ image and available in two different 
versions. The ''full'' and the ''fast'' image. Both images support the 
execution of your code and come with the full suite of Tinkerforge
libraries. 

The **full image** comes with a driver for the GPU 
and all necessary graphical user interface libraries. 
It boots an X server and the `LXDE desktop environment <http://www.lxde.org>`__ 
with auto login. If the program you run on the RED Brick uses a graphical 
interface it will show up on the desktop. The screen resolution should
automatically adapt to the preferred resolution of the connected HDMI monitor. 
If you want to change it, you can configure the screen resolution through LXDE. 
You don't have to use the HDMI port and can execute non graphical 
programs on this image.

The **fast image** comes without graphical interface support and has no X, LXDE 
and other graphical libraries pre-installed. GPU drivers are not loaded,
which means that the RED Brick has more available RAM (the RAM is shared between
CPU and GPU). It is optimized for a fast boot time and can boot in ~10s.

New software can be installed on both images.
See the `installing section <TODO>`__ on how to install new software.

The list of pre-installed programming language libraries can be found below:

* `Full Image Installed Programs List <TODO_Link_to_download_page>`__.
* `Fast Image Installed Programs List <TODO_Link_to_download_page>`__.

If you want to log into the linux system by command line or LXDE, the standard 
user is **tf** with default password **tf**. The user is a sudoer, i.e.
you can get root access by calling::

 sudo su

The images can be downloaded from the:
`download page <TODO_Link_to_download_page>`__.


.. _red_brick_build_image:

Build your Own Image
^^^^^^^^^^^^^^^^^^^^

For the building steps we are assuming a `Debian Linux <https://www.debian.org/>`__
or derivative (Ubuntu etc) as the host platform.

1. Check out RED Brick Git::

    git clone https://github.com/Tinkerforge/red-brick

2. Move into the folder *image*, open the README.rst file and execute the documented 
   steps.

The build process will take at least 4-6 hours, depending on the processing power
of your PC it might also take considerably longer.


.. _red_brick_copy_image:

Copy Image on SD Card
^^^^^^^^^^^^^^^^^^^^^

1. Download the 
   :ref:`full image or the fast image <red_brick_images>` from the RED Brick:
   `Download page  <TODO_Link_to_download_page>`__

2. Choose a suitable SD card. We recommend a fast SD card (e.g. class 10) with
   enough space. You can find the size of the image on the download page.

3. Transfer the image to the SD card:

    * On Windows use a tool like Win32DiskImager to transfer the image to the card.

        * `Download Link <https://sourceforge.net/projects/win32diskimager/files/latest/download>`__ 
        * `Documentation <http://sourceforge.net/p/win32diskimager/wiki/Home/>`__

    * On OS X and Linux

        * Connect the SD card to your PC 
        * Identify the path to your SD card (e.g. dmesg)
        * sudo dd if=path_of_your_image.img of=path_to_sdcard bs=1M

            * e.g.: ``dd if=/tmp/red_full_image.img of=/dev/sdb bs=1M``


.. _red_brick_hardware:

Hardware Description
--------------------

TODO: Overview Image with Top and Bottom Side


Power Button
^^^^^^^^^^^^

TODO: Image of Power Button

The button on the RED Brick is a power button. Press it longer than 5 seconds
and the RED Brick will turn off immediately. 
If the Brick is off, press the button until the blue LED lights up and 
the Brick will boot again. 

.. _red_brick_leds:

LEDs
^^^^

TODO: Image of RED Brick with arrows to LEDs

The RED Brick has three LEDs on the top side: A blue, a red and a green LED.

The blue LED is directly connected to the internal power supply of the 
processor. The LED is on if the Brick is powered.

The red LED shows if an error is present. If the red LED stays on during 
startup, no image could be found. There may be no SD card inserted or there is 
no valid image on the SD card.

The green LED shows the current state. If on startup the red LED is off
and the green LED does not turn on, Linux couldn't boot properly. During
boot-time the green LED turns on. After the RED Brick has booted up
and all of the services are available the green led starts showing a
heartbeat.

To summarize, a proper boot up of the RED Brick will result in the following
sequence:

1. Blue and red on, green off (power on).
2. Red turns off (U-Boot loaded).
3. Green turns on (Linux boots).
4. Green starts heartbeat (Linux booted successfully and all services available).

You can change the function of the green and red LED. They can also 
:ref:`show cpu or sd card usage <red_brick_brick_settings_brickd>` instead of a 
heartbeat.

.. _red_brick_micro_sd_card_slot:

Micro SD Card Slot
^^^^^^^^^^^^^^^^^^

TODO: Image of SD Card Slot

The Linux system and your data is stored on a Micro SD card. The slot
is located at the bottom side of the Brick. 
Micro SD (1.0), Micro SDHC (2.0) and Micro SDXC (3.0) cards
are supported. As a minimum we recommend a class 10 Micro SD Card to ensure
fast reads and writes.

A description of the images can be found in the 
:ref:`image section <red_brick_images>`.

.. _red_brick_usb_host:

USB 2.0 Host
^^^^^^^^^^^^

TODO: Image of USB Port

The RED Brick is equipped with a standard 
`USB 2.0 <http://en.wikipedia.org/wiki/USB>`__ (480Mbps) type A jack. It can
power other USB devices with up to 7.5W (5V/1.5A) and is short circuit 
protected. Both, full and fast image are based on Debian Linux and support 
typical USB devices like WIFI or Ethernet dongles, webcams, printers, keyboards, 
mouses or USB touchscreens. 

Some Ethernet or WIFI dongles can be directly configured with the Brick Viewer. 
Supported dongles can be found in our shop (TODO Link). Other devices might have
to be configured directly in the Linux system and can't be configured with the 
Brick Viewer.

The :ref:`full image <red_brick_images>` supports a graphical user interface,
which can be controlled by standard USB keyboards, mouses or touchscreens.


.. _red_brick_mini_usb:

Mini USB
^^^^^^^^

With the Mini USB connector, the RED Brick can be configured through the
:ref:`Brick Viewer <red_brick_brickv>`. It can also be used to power the Brick.


.. _red_brick_hdmi:

Micro HDMI
^^^^^^^^^^

TODO: Image HDMI connector

With the Micro `HDMI <http://en.wikipedia.org/wiki/HDMI>`__ connector 
(also called type D), all standard HDMI monitors and TVs can be connected to 
the RED Brick. The connector is only active in the 
:ref:`full image <red_brick_images>`. HDMI Ethernet Channel (HEC) is not 
supported.


Brick Stack Connector
^^^^^^^^^^^^^^^^^^^^^

TODO: Image Stack connector

The RED Brick can control up to eight Bricks through the stack connectors.
Additionally up to two Master Extensions can be used with the RED Brick. 
Currently only the RS485 Extension all versions of
the Ethernet Extension are supported. 

The WIFI Extension is currently not supported. We recommend to use a USB 
WIFI dongle to add WIFI connectivity to the RED Brick. 

The Ethernet Extension shows up as a
normal Ethernet interface in the underlying Linux system.

A Step-Down Power Supply can be put below the RED Brick and can 
power the whole stack.

GPIO Header
^^^^^^^^^^^

.. note:: 

   This header is intended for advanced users to connect their own hardware. 
   Currently there is no software support for any of the functions of this 
   GPIO connector.

TODO Image Header

The RED Brick is equipped with a 21 pin, 0.25mm pitch, FPC GPIO connector
(Molex 502078-2110).

All signals of Port E of the A10s processor are connected to this GPIO 
connector. These signals can be configured for several functions:

General Purpose Input/Output, Transport Stream Controller (TS), Camera Sensor
Interface (CSI), Serial Peripheral Interface (SPI), Secure Digital Memory 3.0 
Card Controller (SDC), Universal Asynchronous Receiver Transmitter (UART), 
Interrupt capable. Additionally a I2C (TWI) interface is connected to this GPIO.

==== ======== =========================================================
Pin  Signal   Description
==== ======== =========================================================
1    5V       5V Power Supply
2    3V3      3.3V Power Supply
3    PE0      TS Clock, CSI Pixel Clock, SPI Chip Select 0, INT14, GPIO
4    GND      Ground
5    PE1      TS Error, CSI Sensor Clock, SPI Clock, INT15, GPIO
6    GND      Ground
7    PE2      TS Sync, CSI Horizontal Sync, SPI MOSI, GPIO
8    GND      Ground
9    PE3      TS Data Valid, CSI Vertical Sync, SPI MISO, GPIO
10   GND      Ground
11   PE4      TS Data 0, CSI Data 0, SD Controller Data 0, GPIO
12   PE5      TS Data 1, CSI Data 1, SD Controller Data 1, GPIO
13   PE6      TS Data 2, CSI Data 2, SD Controller Data 2, GPIO
14   PE7      TS Data 3, CSI Data 3, SD Controller Data 3, GPIO
15   PE8      TS Data 4, CSI Data 4, SD Controller Command, GPIO
16   PE9      TS Data 5, CSI Data 5, SD Controller Clock, GPIO
17   PE10     TS Data 6, CSI Data 6, UART TX, GPIO
18   PE11     TS Data 7, CSI Data 7, UART RX, GPIO
19   GND      Ground
20   PB15     I2C Clock (with 2k2 Pullup), GPIO
21   PB16     I2C Data (with 2k2 Pullup), GPIO
==== ======== =========================================================


Power Supply
^^^^^^^^^^^^

The RED Brick needs to be powered by a 5V supply. It can be powered through 
the Mini USB connector or a Step-Down Power Supply. A single RED Brick needs
up to TODO Watts, so that a typical 5W (5V/1A) USB power supply will suffice to
power it and a Master Brick with a few connected Bricklets. If you use a 
larger setup, calculate the power requirements and choose a suitable power 
supply with enough power reserves. Don't forget to add the consumption of 
additionally connected USB devices.


.. _red_brick_faq:


FAQ
---

* Q: I connected the RED Brick to my Linux PC. Why is there no ``/dev/ttyACM0``
  device to access its serial console?
* A: The ``cdc_acm`` driver has to be loaded for this to work.

* Q: The red and blue LED are on. But nothing happens.
* A: The image is not booting. Please check your micro SD Card.



.. _red_brick_programming_interface:

Programming Interface
---------------------

The RED Brick API is meant to be used by the Brick Viewer to implement the
offered  functionality (getting status information, managing programs etc.).
Normal users will not need to use this API, it may only be interesting for
power users.

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RED_Brick_hlpi.table
