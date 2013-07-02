
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Server Room Monitoring
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring.html

.. include:: ServerRoomMonitoring.substitutions

.. _starter_kit_server_room_monitoring:

Starter Kit: Server Room Monitoring
===================================

Features
--------

.. Einrueckung so beibehalten, da sonst kaputt

 * Allows Low Cost and Modular Server Room Monitoring 
 * 19" or 10" Rack Mountable
 * Accessible and Powered by Ethernet (PoE) 
 * Expandable: Simply add Sensors if you need them
 * API for many programming languages 

   * (|bindings|)

 * Open Source Soft- and Hardware

Description
-----------

The *Starter Kit: Server Room Monitoring* is an open source kit to
monitor server room installation. The basic kit is equipped with the following
Sensors: One :ref:`Ambient Light Bricklet <ambient_light_bricklet>`,
:ref:`Temperature Bricklet <temperature_bricklet>` and 
:ref:`PTC Bricklet <ptc_bricklet>`.

It can be extended by multiple other Bricklets probes, different other sensors, in/outputs e.g. 
to read case switches or doors or to switch warning devices on/off.
There are different options to mount miscellaneous :ref:`Bricklets <product_overview_bricklets>`.

One or more external controlling devices, such as (Embedded-) PCs, smart phones or
tablets, can be used to control the kit from outside over the Ethernet 
connection. Therefore monitoring over the internet is also possible.

The kit allows to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for 
:ref:`Analog In <analog_in_bricklet>`,
:ref:`Analog Out <analog_in_bricklet>`,
:ref:`Industrial Digital In 4 <industrial_digital_in_4_bricklet>`,
:ref:`Industrial Digital Out 4 <industrial_digital_out_4_bricklet>`,
:ref:`Industrial Quad Relay <industrial_quad_relay_bricklet>`,
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
Illumination                      0lux - 900lux in 0.1lux steps
Ambient Temperature               -40°C - 85°C in 0.01°C steps
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
* Example source code *Website* (Download: `PHP <https://github.com/Tinkerforge/weather-station/tree/master/website/php>`__)
 

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


Simple Monitoring
^^^^^^^^^^^^^^^^^

Server Room Monitoring with Nagios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Server Room Monitoring with Icinga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Upload Sensor Data to Xively
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

