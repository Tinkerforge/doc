
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Server Room Monitoring
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring.html

.. include:: ServerRoomMonitoring.substitutions

.. _starter_kit_server_room_monitoring:

Starter Kit: Server Room Monitoring
===================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/server_room_monitoring_back_350.jpg",
	               "Kits/server_room_monitoring_back_800.jpg",
	               "Server Room Monitoring Kit: Back")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_in_rack3_100.jpg",
	             "Kits/server_room_monitoring_in_rack3_800.jpg",
	             "Server Room Monitoring Kit: In Rack")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_front_100.jpg",
	             "Kits/server_room_monitoring_front_800.jpg",
	             "Server Room Monitoring Kit: Front")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_content_100.jpg",
	             "Kits/server_room_monitoring_content_800.jpg",
	             "Server Room Monitoring Kit: Content")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_extended_100.jpg",
	             "Kits/server_room_monitoring_extended_800.jpg",
	             "Server Room Monitoring Kit: Extended Version")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_iqr_100.jpg",
	             "Kits/server_room_monitoring_iqr_800.jpg",
	             "Server Room Monitoring Kit: Switching Power")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_in_rack1_100.jpg",
	             "Kits/server_room_monitoring_in_rack1_800.jpg",
	             "Server Room Monitoring Kit: In Rack")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_in_rack2_100.jpg",
	             "Kits/server_room_monitoring_in_rack2_800.jpg",
	             "Server Room Monitoring Kit: In Rack")
	}}
	{{ tfdocend() }}


Features
--------

* Allows Low Cost and Modular Server Room Monitoring 
* 19" Rack Mountable (1U)
* Accessible and Powered over Ethernet (`PoE <https://en.wikipedia.org/wiki/Power_over_Ethernet>`__) 
* Expandable: Simply add extra Sensors and I/O moduls as needed
* API for many programming languages: |bindings|
* Open Source Soft- and Hardware
* `Nagios <http://www.nagios.org/>`__ and `Icinga <https://www.icinga.org/>`__ supported

Description
-----------

The *Starter Kit: Server Room Monitoring* is an open source kit to
monitor server room installations. The basic kit is equipped with the following
Sensors: :ref:`Ambient Light Bricklet <ambient_light_bricklet>`
(monitors room illumination),
:ref:`Temperature Bricklet <temperature_bricklet>` (monitors
temperature in the server rack) and a
:ref:`PTC Bricklet <ptc_bricklet>` with attachable Pt100 temperature sensor
probe (monitors temperature in a server). A :ref:`Master Brick <master_brick>`
and a :ref:`Ethernet Extension <ethernet_extension>`, with
`Power over Ethernet (PoE) <https://en.wikipedia.org/wiki/Power_over_Ethernet>`__
support, are included
as well. The kits enclosure can be mounted directly in a 19" server rack
and can be extended by more temperature probes, other modules (e.g. motion
detector), in- or outputs (to switch computers on/off or to monitor doors) and 
so on. With the Tinkerforge :ref:`building blocks<product_overview>` you can
flexibly adapt it to your needs.

One or more external controlling devices, such as (Embedded-) PCs, smart phones 
or tablets, can be used to control the hardware over the Ethernet 
connection. Monitoring directly over the Internet is possible. Power can
be supplied with PoE or USB.

The soft- and hardware of the kit can be modified. The casing consists of
tinker-friendly PMMA, you can drill new holes with 
simple wood drill. Mounting holes for 
different :ref:`Bricks <product_overview_bricks>` and 
:ref:`Bricklets <product_overview_bricklets>` are provided, by default you can
mount:

:ref:`Analog In Bricklet <analog_in_bricklet>`,
:ref:`Analog Out Bricklet <analog_in_bricklet>`,
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`,
:ref:`Industrial Digital Out 4 Bricklet <industrial_digital_out_4_bricklet>`,
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`,
:ref:`IO-4 Bricklet <io4_bricklet>`,
Motion Detector Bricklet (coming soon)
and Segment Display 4x7 Bricklet (coming soon).

Programming this kit can be done with all of the available
bindings (|bindings|). Example implementations and applications for the usage with 
`Nagios <http://www.nagios.org/>`__, `Icinga <https://www.icinga.org/>`__ and 
other are available (see below). 

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Illumination                      0lux - 900lux in 0.1lux steps
Ambient Temperature               -40°C - 85°C in 0.01°C steps
Pt100 Sensor Probe                -20°C - 450°C
PTC Bricklet                      0.03125°C (15bit) resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            482 x 92 x 44mm (19.0 x 3.62 x 1.75")
Weight                            250g
================================  ============================================================

.. _starter_kit_server_room_monitoring_resources:

Resources
---------

* Server Room Monitoring Kit case FreeCAD CAD files (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/case>`__)
* Example source code for :ref:`Simple Monitoring <starter_kit_server_room_monitoring_simple_monitoring>` (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/simple_monitoring/check_tf_temp_simple.sh>`__)
* Example source code for :ref:`Nagios/Icinga Plugin <starter_kit_server_room_monitoring_nagios_or_icinga_index>` (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/nagios_icinga/check_tf_temp.py>`__)
* Example source code for :ref:`Nagios/Icinga Extended Plugin <starter_kit_server_room_monitoring_extended_nagios_index>` (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/nagios_icinga/check_tf_temp_ext.py>`__)
* Example source code for :ref:`Upload Sensor Data to Xively <starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index>` (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/xively/server_room_monitoring.py>`__)

First tests, firmware upgrade and configuration
------------------------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. At next you should
configure the PTC Bricklet and attach the temperature probe (2-wire).
documented :ref:`here <ptc_bricklet_jumper_configuration>` and 
:ref:`here <ptc_bricklet_connectivity>`.

After this put the Ethernet Extension on top of the Master Brick, connect all
Bricklets to it and connect it via USB to your PC. 
Afterwards use Brick Viewer to check if all firmwares are up to 
date (Updates / Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_firmware>` and
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick
Viewer, too:

.. image:: /Images/Kits/server_room_monitoring_update_350.jpg
   :scale: 100 %
   :alt: Server Room Monitoring Hardware update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_update_orig.jpg

As next step click through the tabs of the Brick Viewer to see if everything is
working correctly. Next you should configure the Ethernet Master Extension. In 
our further examples we configure the hostname to "ServerMonitoring"
and use DHCP. To do that 
click on the Master Brick tab and configure it to your needs. More information 
about the configuration of the Ethernet Extension can be found 
:ref:`here <ethernet_configuration>`.

After testing the hardware and configuration you can be sure that the Bricks 
and Bricklets have versions that work together and that everything will work if
it is screwed together in the 19" server enclosure.


Construction
------------

The construction of the basic kit is described 
:ref:`here <starter_kit_server_room_monitoring_construction>`.

.. toctree::
   :hidden:

   Construction


.. _starter_kit_server_room_monitoring_projects:

Projects
--------

There are several applications for the Starter Kit: Server Room Monitoring. In 
the following we are showing some examples which can act as a starting point
for your own projects.


.. _starter_kit_server_room_monitoring_simple_monitoring:

Simple Monitoring
^^^^^^^^^^^^^^^^^

In this example we use the :ref:`Shell Bindings <api_bindings_shell>` to read 
out the different sensors in the kit. 

Enumerate the Bricks and Bricklets ("is all connected?"):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring enumerate
 uid=6Dct25
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

Read out connected sensors (adapt the UID):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring call temperature-bricklet SCT31 get-temperature
 temperature=2487

 $ tinkerforge --host ServerMonitoring call ambient-light-bricklet ajC get-illuminance
 illuminance=41

 $ tinkerforge --host ServerMonitoring call ptc-bricklet fow get-temperature
 temperature=2603

The shell bindings support the execution of additional shell commands with the
``--execute`` option (see `Shell Bindings <ipcon_shell_output>`__ for more
information). The following script shows how to convert the returned value into
degree Celsius and how to save it in a variable for further use.

.. code-block:: bash

 #!/bin/sh

 HOST=ServerMonitoring
 UID=SCT31

 temp=$(tinkerforge --host $HOST call temperature-bricklet $UID get-temperature\
        --execute "echo '{temperature} / 100' | bc | xargs printf '%.2f\n'")
 echo $temp


.. _starter_kit_server_room_monitoring_nagios_or_icinga_index:

Server Room Monitoring with Nagios or Icinga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Icinga <https://www.icinga.org/>`__ and `Nagios <http://www.nagios.org/>`__ 
are computer system monitoring tools. Icinga is a fork of Nagios and is 
said to be backward compatible to Nagios. In the following examples we are
referring to the Nagios API to be also compatible with Icinga.

These monitoring tools use plugins, instantiated as services to 
monitor processor load, memory utilization, specific software processes or 
physical values like temperature.

In this example we write our own plugin to use the kits hardware for ambient
temperature measuring. With a few modifications you can use the plugin to
support other Tinkerforge hardware modules and create the physical monitoring
you need.

.. image:: /Images/Kits/server_room_monitoring_icinga_screenshot_350.jpg
   :scale: 100 %
   :alt: Icinga Screenshot
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_icinga_screenshot_orig.jpg

Find the full project description :ref:`here
<starter_kit_server_room_monitoring_nagios_or_icinga>`.

.. toctree::
   :hidden:

   NagiosOrIcinga


.. _starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index:

Upload Sensor Data to Xively
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Xively <https://xively.com/>`__ is a service that provides the possibility to
analyze and visualize the "Internet of Things". It can be used to interconnect
different devices over the Internet and can store a history of 
measured values and can display it with pretty graphs.

.. image:: /Images/Kits/server_room_monitoring_xively_350.jpg
   :scale: 100 %
   :alt: Xively datastream configuration
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_xively_orig.jpg

The full project description can be found :ref:`here
<starter_kit_server_room_monitoring_upload_sensor_data_to_xively>`.

.. toctree::
   :hidden:

   UploadSensorDataToXively


.. _starter_kit_server_room_monitoring_further_enhancements:

Further Enhancements
--------------------

If you have modded, extended or improved the kit
in any way and you have published your results on our 
`Wiki <http://www.tinkerunity.org/wiki/>`__, on your blog or similar: 
Please give us a notice. We would love to add a link to your project here!


.. _starter_kit_server_room_monitoring_extended_nagios_index:

Motion Detector and Error Code Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The casing has already the necessary cut-outs for a Motion Detector Bricklet
(coming soon) and a Segment Display 4x7 Bricklet (coming soon). Use a Motion 
Detector Bricklet to detect motion in your server room. An additional Segment 
Display 4x7 Bricklet can be used to show error code information on the case.

The full project description can be found 
:ref:`here <starter_kit_server_room_monitoring_extended_nagios>`.

.. image:: /Images/Kits/server_room_monitoring_extended_350.jpg
   :scale: 100 %
   :alt: Extended version of kit
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_extended_1000.jpg

.. toctree::
   :hidden:

   ExtendedNagios

Remote On/Off Switch
^^^^^^^^^^^^^^^^^^^^

Use Industrial Quad Relay to switch computers on or off remotely.
You can use the previous examples to modify them to your needs.
The wiring is really simple, you only have to bypass the on/off switch
of the computer with one of the relays of the Industrial Quad Relay Bricklet.
A tutorial how a switch can be bypassed can be found at the
:ref:`Hardware Hacking for Beginners Tutorial <starter_kit_hardware_hacking_for_beginners>`.

.. image:: /Images/Kits/server_room_monitoring_iqr_350.jpg
   :scale: 100 %
   :alt: Kit with Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_iqr_1000.jpg
