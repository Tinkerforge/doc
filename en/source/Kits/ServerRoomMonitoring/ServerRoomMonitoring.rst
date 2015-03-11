
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Server Room Monitoring
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring.html

.. include:: ServerRoomMonitoring.substitutions

.. _starter_kit_server_room_monitoring:

Starter Kit: Server Room Monitoring
===================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/server_room_monitoring_alu_front_350.jpg",
	               "Kits/server_room_monitoring_alu_front_800.jpg",
	               "Server Room Monitoring Kit: Front")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_alu_surface_100.jpg",
	             "Kits/server_room_monitoring_alu_surface_800.jpg",
	             "Server Room Monitoring Kit: Surface Aluminum")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_alu_in_hand_100.jpg",
	             "Kits/server_room_monitoring_alu_in_hand_800.jpg",
	             "Server Room Monitoring Kit")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_back_100.jpg",
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

* Low Cost and Modular Server Room Monitoring (19" Rack, 1U)
* Expandable: Simply add extra Sensors and I/O modules as needed
* Powered over Ethernet (`PoE <https://en.wikipedia.org/wiki/Power_over_Ethernet>`__) or USB
* Configuration of customized solution without programming possible
* For Programmers: API for many programming languages: 

  * |bindings|

* Open Source Soft- and Hardware with `Nagios <http://www.nagios.org/>`__ and `Icinga <https://www.icinga.org/>`__ support

Description
-----------

The *Starter Kit: Server Room Monitoring* is an open source kit that can
monitor server room installations. The basic kit is equipped with the following
Sensors: :ref:`Ambient Light Bricklet <ambient_light_bricklet>`
(monitors room illumination), :ref:`Humidity Bricklet <humidity_bricklet>`
(monitors humidity), 
:ref:`Temperature Bricklet <temperature_bricklet>` (monitors
temperature in the server rack) and a
:ref:`PTC Bricklet <ptc_bricklet>` with attachable Pt100 temperature sensor
probe (monitors temperature in a server). 

The kits enclosure can be mounted directly in a 19" server rack
and can be extended by other Tinkerforge 
:ref:`building blocks <primer_products>`, e.g. more temperature probes, motion
detector, in- or outputs (to switch computers on/off or to monitor doors), 
to flexibly adapt the kit to your needs.

Two different applications are possible:

1. **Non-stand-alone monitoring** (standard kit)

   The sensors of the kit are read out via Ethernet or USB by a computer with
   the offered APIs (|bindings|). Individual solutions can be realized with ease.
   Examples for 
   :ref:`Bash <starter_kit_server_room_monitoring_simple_monitoring>`,
   :ref:`Nagios/Icinga <starter_kit_server_room_monitoring_nagios_or_icinga_index>` and
   :ref:`Xively <starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index>`
   demonstrate different possibilities.

2. **Stand-alone monitoring** (standard kit + RED Brick)

   With an additional :ref:`RED Brick <red_brick>` external control 
   by another computer is not necessary anymore. You can configure your own 
   monitoring solution with the :ref:`Brick Viewer <brickv>` without any 
   programming.

   The value range for each sensor can be defined with sliders. It is possible
   to enable email notifications for monitoring values that are out of range.
   Rules can be defined for sensors that are directly connected, but also for other 
   Tinkerforge sensors available in the network. The defined rules 
   configure an instance of Nagios that runs on the RED Brick. The Nagios 
   web interface shows current monitoring values and currrently existing problems.
   More information can be found in the 
   :ref:`RED Brick section <starter_kit_server_room_monitoring_red_brick>`  
   of the Server Room Monitoring documentation.

   Advanced users can easily modify the Nagios installation that runs on the
   RED Brick to change configurations that go beyond the Brick Viewer
   possbilities.
   
The kit can be powered through 
`Power over Ethernet (PoE) <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__
or USB.

The soft- and hardware of the kit can be modified. The casing, 
except of the powder coated aluminum front panel, consists of tinker-friendly 
PMMA, you can drill new holes with a wood drill. Mounting holes for 
different :ref:`Bricks <primer_bricks>` and 
:ref:`Bricklets <primer_bricklets>` are provided, by default you can
mount:

:ref:`Analog In Bricklet <analog_in_bricklet>`,
:ref:`Analog Out Bricklet <analog_in_bricklet>`,
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`,
:ref:`Industrial Digital Out 4 Bricklet <industrial_digital_out_4_bricklet>`,
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`,
:ref:`IO-4 Bricklet <io4_bricklet>`,
:ref:`Motion Detector Bricklet <motion_detector_bricklet>`,
and :ref:`Segment Display 4x7 Bricklet <segment_display_4x7_bricklet>`

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Illumination                      0lux - 900lux in 0.1lux steps
Ambient Temperature               -40°C - 85°C in 0.01°C steps
Pt100 Sensor Probe                -20°C - 450°C
PTC Bricklet                      0.03125°C (15bit) resolution
Humidity Bricklet                 0% - 100% relative humidity
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            482 x 92 x 44mm (19.0 x 3.62 x 1.75")
Weight                            250g
================================  ============================================================

.. _starter_kit_server_room_monitoring_resources:

Resources
---------

* Server Room Monitoring Kit Case FreeCAD CAD files (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/case>`__)
* Example Source Code for :ref:`Simple Monitoring <starter_kit_server_room_monitoring_simple_monitoring>` (Download: `Shell <https://github.com/Tinkerforge/server-room-monitoring/tree/master/simple_monitoring/check_tf_temp_simple.sh>`__)
* Example Source Code for :ref:`Nagios/Icinga Plugin <starter_kit_server_room_monitoring_nagios_or_icinga_index>` (Download: `Python <https://github.com/Tinkerforge/server-room-monitoring/tree/master/nagios_icinga/check_tf_temp.py>`__)
* Example Source Code for :ref:`Nagios/Icinga Extended Plugin <starter_kit_server_room_monitoring_extended_nagios_index>` (Download: `Python <https://github.com/Tinkerforge/server-room-monitoring/tree/master/nagios_icinga/check_tf_temp_ext.py>`__)
* Example Source Code for :ref:`Upload Sensor Data to Xively <starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index>` (Download: `Python <https://github.com/Tinkerforge/server-room-monitoring/tree/master/xively/server_room_monitoring.py>`__)

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


.. _starter_kit_server_room_monitoring_red_brick:

RED Brick
---------

If the Server Room Monitoring Kit is used together with a RED Brick,
Nagios can be configured directly through the Brick Viewer.

.. image:: /Images/Screenshots/brickv_srm_600.jpg
   :scale: 100 %
   :alt: Nagios configuration in Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/brickv_srm.jpg

To enable the Server Monitoring service (requires RED Brick Image >= 1.6 and
Brick Viewer >= 2.2.3) go to the :ref:`services tab
<red_brick_brickv_settings_services>` and tick the Server Monitoring checkbox.

If the Server Monitoring service is enabled, it is possible to add rules.
A rule basically consists of a Bricklet-type (Temperature, Ambient Light,
Humidity or PTC), the UID and a warning as well as a critical range. Just add 
as many rules as you need and configure them as required. 

You can also configure automatic email notification for each of the
warning/critical ranges. Just tick the ``Enable Email Notification`` checkbox
and add the required information.

Click *Save* to save the configuration on the RED Brick. You can now visit
``http://<red-brick-ip>/nagios3/`` to view the current Nagios status.

.. image:: /Images/Screenshots/nagios_srm_600.jpg
   :scale: 100 %
   :alt: Nagios webpage
   :align: center
   :target: ../../_images/Screenshots/nagios_srm.jpg

The default user:password is ``nagiosadmin``:``tf``. You can change the
password through the console with::

 sudo htpasswd -c -b  /etc/nagios3/htpasswd.users nagiosadmin NEWPASSWORD

Each of the rules will be shown as a service in Nagios. An overview over all 
services is available if you click on ``Services`` in the ``Current Status``
category.

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

The section about :ref:`further enhancements
<starter_kit_server_room_monitoring_further_enhancements>` lists more
Nagios/Icinga examples.


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

The casing has already the necessary cut-outs for a :ref:`Motion Detector Bricklet <motion_detector_bricklet>`
and a :ref:`Segment Display 4x7 Bricklet <segment_display_4x7_bricklet>`. Use a Motion 
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


Monitoring Server Rack Door with Distance IR Bricklet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Martin Seener developed a check for Nagios that uses a Distance IR Bricklet to
detect if the door of a server rack was opened. The Distance IR Bricklet is
mounted inside the server rack and measures the distance towards the closed
door. If the distance changes significantly then the door was opened.

To get a proper threshold the standard deviation of the distance measurements
of the Distance IR Bricklets is calculated over a longer time. Martin Seener
included a script for this task.

This check is the first one in a `collection
<https://github.com/martinseener/tinkerforge-nagios-checks>`__ of Nagios checks
for Tinkerforge.
