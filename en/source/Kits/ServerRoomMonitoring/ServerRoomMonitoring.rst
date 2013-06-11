
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Server Room Monitoring
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring.html

.. include:: ServerRoomMonitoring.substitutions

.. _starter_kit_server_room_monitoring:

Starter Kit: Server Room Monitoring
===================================

Features
--------

.. Einrueckung so beibehalten, da sonst kaputt

* Open Source Server Room Monitoring
* 19" or 10" Rack Mountable
* Accessible and Powered by Ethernet (PoE) 
* Modular: Expandable to fullfill your Requirements
* Demo Application available

Description
-----------

The *Starter Kit: Server Room Monitoring* is an open source kit to
monitor server room installation. The basic kit is equipped with the following
Sensors: One Ambient Light Bricklet, Temperature Bricklet and PTC Bricklet.

It can be extended by multiple other Bricklets probes, different other sensors, in/outputs e.g. 
to read case switches or doors or to switch warning devices on/off.
There are different options to mount miscellaneous :ref:`Bricklets <bricklets>`.

One or more external controlling devices, such as (Embedded-) PCs, smart phones or
tablets, can be used to control the kit from outside over the Ethernet 
connection. Therefore monitoring over the internet is also possible.

The kit allows to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for 
:ref:`Analog In <analog_in_bricklet>`,
:ref:`Analog Out <analog_in_bricklet>`,
:ref:`Industrial Digital In <industrial_digital_in_bricklet>`,
:ref:`Industrial Digital Out <industrial_digital_out_bricklet>`,
:ref:`Industrial Quad Relay <industrial_quar_relay_bricklet>`,
and :ref:`IO-4 <io4_bricklet>` Bricklets are provided.

Programming this kit can be done with all of the available
bindings (|bindings|). Example implementations for all supported programming languages 
and a demo application are available. This will give you a starting point into the 
programming with Tinkerforge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Air Pressure                      10mbar - 1200mbar in 0.012mbar steps
Illumination                      0lux - 900lux in 0.1lux steps
Relative Humidity                 0% RH - 10% RH in 0.1% RH steps
Temperature                       -40°C - 85°C in 0.01°C steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions 10" (W x D x H)        240 x 46 x 100mm (9.45 x 1.81 x 3.94")
Dimensions 19" (W x D x H)        240 x 46 x 100mm (9.45 x 1.81 x 3.94")
Weight 10"                        376g
Weight 19"                        376g
================================  ============================================================

.. _starter_kit_server_room_monitoring_resources:

Resources
---------

* Server Room Monitoring Kit case FreeCAD CAD files (`Download <https://github.com/Tinkerforge/weather-station/tree/master/case>`__)
* Example source code *Write to LCD* (Download: |write_to_lcd_examples_download|)
* Example source code *Xively* (Download: `Python <https://github.com/Tinkerforge/weather-station/tree/master/xively/python>`__)
* Example source code *Website* (Download: `PHP <https://github.com/Tinkerforge/weather-station/tree/master/website/php>`__)
* Example source code *Button Monitoring* (Download: `C# <https://github.com/Tinkerforge/weather-station/tree/master/button_monitoring/csharp>`__)
* Demo Application (Download: `Windows <http://download.tinkerforge.com/kits/server_room_monitoring/windows/starter_kit_server_room_monitoring_demo_windows_latest.exe>`__, `Linux <http://download.tinkerforge.com/kits/server_room_monitoring/linux/starter-kit-weather-station-demo_linux_latest.deb>`__, `Mac OS X <http://download.tinkerforge.com/kits/server_room_monitoring/macos/starter_kit_server_room_monitoring_demo_macos_latest.dmg>`__)
 

Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Connect all Bricklets to the Master 
Brick and connect it via USB to your PC. Afterwards use Brick Viewer to find out
if all of the firmwares up to date (Updates / Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_firmware>` and
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick
Viewer, too:

.. image:: /Images/Kits/server_room_monitoring_update_350.jpg
   :scale: 100 %
   :alt: Weather Station update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_update_orig.jpg

As next step click through the tabs of the Brick Viewer
to see if all of the sensors are working correctly. Now you can be sure that 
the Bricks and Bricklets have versions that work together and that
everything will work if it is screwed together in the weather station
enclosure.

Demo Application
^^^^^^^^^^^^^^^^

If the hardware is running correctly you can also try the demo application for 
this Starter Kit: Weather Station. It implements three of the presented
:ref:`projects <starter_kit_server_room_monitoring_projects>` for demonstration
purposes:

1. :ref:`Display Environment Measurements on LCD <starter_kit_server_room_monitoring_write_to_lcd>`
2. :ref:`Show Statistics with Button Monitoring <starter_kit_server_room_monitoring_button_monitoring>`
3. :ref:`Connect to Xively <starter_kit_server_room_monitoring_xively>`

Each project can be selected with its own tab. The first project only displays
the measured values. The second project is more complex and displays 
min, max and average values as well as graphs for these measurements.
The display mode can be changed by pressing the buttons at the LCD 20x4 
Bricklet or in the application. In some modi the buttons can be pressed 
multiple times, such that other measurements will be shows. 

Finally the Xively projects lets you upload your measurements.
At first you have to register on `xively.com <https://xively.com>`__.
Next you have to create a Feed ID, API key and four
channels to Upload the values (AirPressure, AmbientLight, Humidity and 
Temperature). Feed ID, API Key and the upload interval have to be configured in 
the demo application. Please take a look at the project description for further
information

The download link is in the :ref:`resources <starter_kit_server_room_monitoring_resources>`.

.. image:: /Images/Kits/server_room_monitoring_demo_350.jpg
   :scale: 100 %
   :alt: Weather Station Demo Application Screenshot
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_demo.jpg

Construction
------------

Begin with 10"

19" Case
^^^^^^^^

Extend 10" kit


.. _starter_kit_server_room_monitoring_projects:

Projects
--------

There are several applications for the Weather Station:


.. _starter_kit_server_room_monitoring_write_to_lcd:

Simple Monitoring
^^^^^^^^^^^^^^^^^


Upload to Xively
^^^^^^^^^^^^^^^^

`Xively <https://xively.com/>`__ is a service that provides the possibility to
analyze and visualize the "Internet of Things". They can store a history of our
Weather Station data and we get pretty graphs:


Further Enhancements
--------------------

If you modded, extended or improved the Starter Kit: Server Room Monitoring
in any way and you have published your results on our 
`Wiki <http://www.tinkerunity.org/wiki/>`__, on your blog or similar: 
Please give us a notice. We would love to add a link
to your project here!

