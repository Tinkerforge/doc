
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Server Room Monitoring
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
 * Expandable: Simply add Sensors or I/O if you need them
 * API for many programming languages 

   * (|bindings|)

 * Open Source Soft- and Hardware

Description
-----------

The *Starter Kit: Server Room Monitoring* is an open source kit to
monitor server room installations. The basic kit is equipped with the following
Sensors: One :ref:`Ambient Light Bricklet <ambient_light_bricklet>` (e.g. to 
monitor the room illumination),
:ref:`Temperature Bricklet <temperature_bricklet>` (e.g. to monitor
the temperature in the server rack) and a
:ref:`PTC Bricklet <ptc_bricklet>` with attachable temperature sensor probe 
(e.g. to monitor the temperature in a server). The included enclosure lets you
mount the kit directly in a 10" or 19" server rack.

The kit uses the Tinkerforge building blocks, such that it can be extended 
easily by more temperature probes, other sensors types (e.g. motion detector), 
in- or outputs (to switch computers on/off or to monitor doors) and so on. 
This way it is adaptable flexibly to your needs. 

One or more external controlling devices, such as (Embedded-) PCs, smart phones 
or tablets, can be used to control the hardware from outside over the Ethernet 
connection. Therefore monitoring over the Internet is also possible. Power 
Supply is possible over onboard 
`Power over Ethernet (PoE) <https://en.wikipedia.org/wiki/Power_over_Ethernet>`__.

The kit allows to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for 
different :ref:`Bricklets <product_overview_bricklets>` and 
:ref:`Bricks <product_overview_bricks>` are provided, e.g.:

:ref:`Analog In Bricklet <analog_in_bricklet>`,
:ref:`Analog Out Bricklet <analog_in_bricklet>`,
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`,
:ref:`Industrial Digital Out 4 Bricklet <industrial_digital_out_4_bricklet>`,
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`,
and :ref:`IO-4 Bricklet <io4_bricklet>`.

Programming this kit can be done with all of the available
bindings (|bindings|). Example implementations for all supported programming 
languages and example applications for the usage with 
`Nagios <http://www.nagios.org/>`__, `Icinga <https://www.icinga.org/>`__ and 
other are available. This will give you a quick starting point into the 
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
 

First tests, firmware upgrade and configuration
------------------------------------------------

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
to see if everything is working correctly. Next you should configure the
Ethernet Extension. In our further examples we configure the hostname to 
"ServerMonitoring". To do that click on the Master Brick tab and
configure it to your needs. More information about how to configure 
a Ethernet Extension can be found 
:ref:`here <ethernet_configuration>`.


After testing the hardware and configuration you can be sure that 
the Bricks and Bricklets have versions that work together and that
everything will work if it is screwed together in the server 10"/19"
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

In this small test we use the :ref:`Shell Bindings <api_bindings_shell>` to 
read out the different sensor in the kit.

Todo: Installation link

.. code-block:: bash 

 tinkerforge --host ServerMonitoring enumerate
 
 >>uid=6Dct25
   connected-uid=0
   position=0
   hardware-version=1,0,0
   firmware-version=2,1,0
   device-identifier=master-brick
   enumeration-type=available

   uid=fow
   connected-uid=6Dct25
   position=a
   hardware-version=1,0,0
   firmware-version=2,0,0
   device-identifier=ptc-bricklet
   enumeration-type=available

   uid=SCT31
   connected-uid=6Dct25
   position=b
   hardware-version=1,1,0
   firmware-version=2,0,1
   device-identifier=temperature-bricklet
   enumeration-type=available

   uid=ajC
   connected-uid=6Dct25
   position=d
   hardware-version=1,1,0
   firmware-version=2,0,1
   device-identifier=ambient-light-bricklet
   enumeration-type=available

 tinkerforge --host ServerMonitoring call temperature-bricklet SCT31 get-temperature
 >>temperature=2487

 tinkerforge --host ServerMonitoring call ambient-light-bricklet ajC get-illuminance
 >>illuminance=41

 tinkerforge --host ServerMonitoring call ptc-bricklet fow get-temperature
 >>temperature=2603

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

Remote On/Off Switch
^^^^^^^^^^^^^^^^^^^^

Use Industrial Quad Relay to switch computers remotely on or off.

Server Room Motion Detector
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use a Motion Detector Bricklet (coming soon) to detect motion in your server
room. You can also add a Sound Intensity Bricklet to detect room intruders
by their noise.

Error Code Display
^^^^^^^^^^^^^^^^^^

With a Segment Display 4x7 Bricklet you can show information directly
on the case.


