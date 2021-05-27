
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring-v2.html

.. include:: ServerRoomMonitoringV2.substitutions

.. _starter_kit_server_room_monitoring_v2:

Starter Kit: Server Room Monitoring 2.0
=======================================

.. raw:: html

	{% tfgallery %}

	Kits/server_room_monitoring_v2_complete_front_right_[100|800].jpg         Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_basic_parts_[100|800].jpg                  Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_complete_back_left_[100|800].jpg           Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_complete_front_left_[100|800].jpg          Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_complete_front_left_rasppi_[100|800].jpg   Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_complete_front_left_zoom_[100|800].jpg     Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_exploded_[100|800].jpg                     Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_rasp_back_[100|800].jpg                    Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_rasp_front_ethernet_[100|800].jpg          Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_rasp_open_front_ethernet_[100|800].jpg     Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_standard_back_ethernet_[100|800].jpg       Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_basic_cover_[100|800].jpg                  Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_basic_ethernet_backward_[100|800].jpg      Server Room Monitoring Kit 2.0
	Kits/server_room_monitoring_v2_basic_ethernet_backward_back_[100|800].jpg Server Room Monitoring Kit 2.0

	{% tfgalleryend %}


Features
--------

* Low Cost and Modular Server Room Monitoring (19" Rack, 1U)
* Standalone with RED Brick or Raspberry Pi
* Expandable: Simply add extra Sensors and I/O modules as needed
* Powered over Ethernet (`PoE <https://en.wikipedia.org/wiki/Power_over_Ethernet>`__),USB or Power Supply (with HAT Brick)
* Configuration of customized solution without programming possible
* For Programmers: API for many programming languages: 

  * |bindings|

* Open Source Soft- and Hardware with `Nagios <https://www.nagios.org/>`__ and
  `Icinga <https://www.icinga.com/>`__ support

Description
-----------

The *Starter Kit: Server Room Monitoring 2.0* is an open source kit that can 
monitor server room installations. The basic kit is equipped with the following 
Sensors: :ref:`Ambient Light Bricklet 3.0 <ambient_light_v3_bricklet>` 
(monitors room illumination), :ref:`Humidity Bricklet 2.0 <humidity_v2_bricklet>` 
(monitors humidity), :ref:`Temperature Bricklet 2.0 <temperature_v2_bricklet>` 
(monitors temperature in the server rack) and a :ref:`PTC Bricklet 2.0 <ptc_v2_bricklet>` 
with attachable Pt100 temperature sensor probe (monitors temperature in a server). 
Place for up to eight PTC Bricklets with up to eight temperature sensors is provided. 
To show error codes you can use the E-Paper Bricklet or the 
Segment Display 4x7 Bricklet 2.0, which are inlcuded to the basic version of the kit.

The kits enclosure can be mounted directly in a 19" server rack and can 
be extended by other Tinkerforge :ref:`building blocks <primer_products>`, 
e.g. more temperature probes, motion detector, in- or outputs (to switch 
computers on/off or to monitor doors), to flexibly adapt the kit to your needs.

For the standalone version it is possible to use our RED Brick or the 
Raspberry Pi with an HAT Brick. For using the Raspberry Pi there are 
special mounting holes.

Content of this kit:

* :ref:`2x Master Brick <master_brick>`,
* :ref:`1x Ethernet Extension (with PoE) <ethernet_extension>`
* :ref:`1x Ambient Light Bricklet 3.0 <ambient_light_v3_bricklet>`,
* :ref:`1x PTC Bricklet 2.0 <ptc_v2_bricklet>`,
* :ref:`1x Temperature Bricklet 2.0 <temperature_v2_bricklet>`,
* :ref:`1x Humidity Bricklet 2.0 <humidity_v2_bricklet>`,
* :ref:`1x Segment Display 4x7 Bricklet 2.0 <segment_display_4x7_v2_bricklet>`,
* :ref:`1x E-Paper 296x128 Bricklet (schwarz/weiß/rot) <e_paper_296x128_bricklet>`,
* 1x Case for Server Room Monitoring 2.0,
* 1x USB Cable 180cm,
* Bricklet Cables,
* Mounting kits,

The kit can be ordered in three different variations:

1. **Non-standalone monitoring** (Standard kit + Ethernet Extension (with PoE))

   The sensors of the kit are read out via Ethernet or USB by a computer with
   the offered APIs (|bindings|). Individual solutions can be realized with ease.
   Examples for 
   :ref:`Bash <starter_kit_server_room_monitoring_v2_simple_monitoring>` and
   :ref:`Nagios/Icinga <starter_kit_server_room_monitoring_v2_nagios_or_icinga_index>`
   demonstrate different possibilities.

2. **Standalone monitoring for Raspberry Pi** (Standard kit + HAT Brick, Standalone with own Raspberry Pi)

   The Kit can be used with your Raspberry Pi. Just mount the HAT Brick on 
   the RaspPi and connect the Bricklets with it. In this option the Ethernet 
   connection of the Raspberry PI will be used to get access to the Kit.
   You can write your own script that runs on the Raspberry Pi.
   
   To get started quickly you can use our example python script for
   Raspberry PI.

2. **Standalone monitoring with RED Brick** (Standard kit + HAT Brick, Standalone with own Raspberry Pi)

   With an additional :ref:`RED Brick <red_brick>` external control 
   by another computer is not necessary anymore. You can configure your own 
   monitoring solution using just :ref:`Brick Viewer <brickv>` without any
   programming.

   The value range for each sensor can be defined with sliders. It is possible
   to enable email notifications for monitoring values that are out of range.
   Rules can be defined for sensors that are directly connected, but also for other 
   Tinkerforge sensors available in the network. The defined rules 
   configure an instance of Nagios that runs on the RED Brick. The Nagios 
   web interface shows current monitoring values and currently existing problems.
   More information can be found in the 
   :ref:`RED Brick section <starter_kit_server_room_monitoring_v2_red_brick>`  
   of the Server Room Monitoring documentation.

   Advanced users can easily modify the Nagios installation that runs on the
   RED Brick to change configurations that go beyond the Brick Viewer
   possibilities.
   
The kit can be powered through 
`Power over Ethernet (PoE) <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__, 
USB (e.g. USB Power Supply) or in the variant with RaspPi over the power 
connector of the HAT Brick with an external power supply.

The soft- and hardware of the kit can be modified. The casing, 
except of the powder coated aluminum front panel, consists of PMMA. Mounting 
holes for different :ref:`Bricks <primer_bricks>` and 
:ref:`Bricklets <primer_bricklets>` and Raspberry Pi are provided.

You can mount a :ref:`Motion Detector Bricklet 2.0 <motion_detector_v2_bricklet>` 
in the front panel.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Illumination                      0lux - 64000lux in 0.01lux steps
Ambient Temperature               -40°C - 85°C in 0.01°C steps
Pt100 Sensor Probe                -20°C - 450°C
PTC Bricklet 2.0                  0.03125°C (15bit) resolution
Humidity Bricklet 2.0             0% - 100% relative humidity
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            482 x 92 x 44mm (19.0 x 3.62 x 1.75")
Weight                            250g
================================  ============================================================

.. _starter_kit_server_room_monitoring_v2_resources:

Resources
---------

* Server Room Monitoring Kit 2.0 Case FreeCAD CAD files (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/case>`__)
* Example Source Code for :ref:`Simple Monitoring <starter_kit_server_room_monitoring_v2_simple_monitoring>` (Download: `Shell <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/simple_monitoring/check_tf_temp_simple.sh>`__)
* Example Source Code for :ref:`Nagios/Icinga Plugin <starter_kit_server_room_monitoring_v2_nagios_or_icinga_index>` (Download: `Python <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp.py>`__)
* Example Source Code for :ref:`Nagios/Icinga Extended Plugin <starter_kit_server_room_monitoring_v2_extended_nagios_index>` (Download: `Python <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp_ext.py>`__)

First tests, firmware upgrade and configuration
------------------------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. At next you should
configure the PTC Bricklet 2.0 and attach the temperature probe (2-wire).
documented :ref:`here <ptc_v2_bricklet_jumper_configuration>` and 
:ref:`here <ptc_v2_bricklet_connectivity>`.

After this put the Ethernet Extension on top of the Master Brick, connect all
Bricklets to it and connect it via USB to your PC. 
Afterwards use Brick Viewer to check if all firmwares are up to 
date (Updates / Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_brick_firmware>` and
:ref:`update the Bricklets <brickv_flash_bricklet_plugin>` with the Brick
Viewer, too:

.. image:: /Images/Kits/server_room_monitoring_update_600.png
   :scale: 100 %
   :alt: Server Room Monitoring Hardware update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_update_orig.png

As next step click through the tabs of the Brick Viewer to see if everything is
working correctly. Next you should configure the Ethernet Master Extension. In 
our further examples we configure the hostname to "ServerMonitoring"
and use DHCP. To do that 
click on the Master Brick tab and configure it to your needs. More information 
about the configuration of the Ethernet Extension can be found 
:ref:`here <ethernet_extension_configuration>`.

After testing the hardware and configuration you can be sure that the Bricks 
and Bricklets have versions that work together and that everything will work if
it is screwed together in the 19" server enclosure.


Construction
------------

The construction of the basic kit is described 
:ref:`here <starter_kit_server_room_monitoring_v2_construction>`.

.. toctree::
   :hidden:

   Details <Construction>


.. _starter_kit_server_room_monitoring_v2_red_brick:

RED Brick
---------

If the kit is used together with a RED Brick then Nagios running on the
RED Brick can be configured directly using Brick Viewer.

.. image:: /Images/Screenshots/brickv_srm_600.jpg
   :scale: 100 %
   :alt: Nagios configuration in Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/brickv_srm.jpg

To enable the Server Monitoring service (requires RED Brick Image >= 1.6 and
Brick Viewer >= 2.2.3) go to the :ref:`services tab
<red_brick_brickv_settings_services>` and tick the Server Monitoring checkbox.

If the Server Monitoring service is enabled, it is possible to add rules.
A rule basically consists of the Bricklet type (Temperature, Ambient Light,
Humidity or PTC), its UID and a warning as well as a critical range. Just add
as many rules as you need and configure them as required. 

You can also configure automatic email notification for each of the
warning/critical ranges. Just tick the ``Enable Email Notification`` checkbox
and add the required information.

Click *Save* to save the configuration on the RED Brick. You can now visit
``http://<red-brick-ip>/nagios/`` or ``http://<red-brick-ip>/nagios3/ (RED Brick image version 1.19 and older)``
to view the current Nagios status.

.. image:: /Images/Screenshots/nagios_srm_600.jpg
   :scale: 100 %
   :alt: Nagios webpage
   :align: center
   :target: ../../_images/Screenshots/nagios_srm.jpg

The default username:password is ``nagiosadmin``:``tf``. You can change the
password through the console with::

 sudo htpasswd -c -b /usr/local/nagios/etc/htpasswd.users nagiosadmin <PASSWORD>

For RED Brick image version 1.9 and older::

 sudo htpasswd -c -b /etc/nagios3/htpasswd.users nagiosadmin <PASSWORD>

Each of the rules will be shown as a service in Nagios. An overview over all 
services is available if you click on ``Services`` in the ``Current Status``
category.


.. _starter_kit_server_room_monitoring_v2_rasppi_hat:

Raspberry Pi + HAT Brick
------------------------

.. note::
	The Raspberry Pi example is currently still in development

..
 If the Raspberry Pi with the HAT Brick is used we have an example script 
 to run on the Raspberry Pi. Before the Brick Daemon have to install on 
 the Raspberry Pi. How to do it you can see here.

You can adapt the example script according to your needs. By default
the following rules are activated:

* TBD
* TBD
* TBD
* TBD

.. _starter_kit_server_room_monitoring_v2_projects:

Projects
--------

There are several applications for the Starter Kit: Server Room Monitoring. In 
the following we are showing some examples which can act as a starting point
for your own projects.


.. _starter_kit_server_room_monitoring_v2_simple_monitoring:

Simple Monitoring
^^^^^^^^^^^^^^^^^

In this example we use the :ref:`Shell Bindings <api_bindings_shell>` to read 
out the different sensors in the kit. 

Enumerate the Bricks and Bricklets ("is all connected?"):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring enumerate
 uid=5VGUhR
 connected-uid=0
 position=0
 hardware-version=2,1,0
 firmware-version=2,4,10
 device-identifier=master-brick
 enumeration-type=available
 
 uid=Jn6
 connected-uid=5VGUhR
 position=a
 hardware-version=1,0,0
 firmware-version=2,0,1
 device-identifier=e-paper-296x128-bricklet
 enumeration-type=available
 
 uid=Jk3
 connected-uid=5VGUhR
 position=b
 hardware-version=1,0,0
 firmware-version=2,0,1
 device-identifier=temperature-v2-bricklet
 enumeration-type=available
 
 uid=HyH
 connected-uid=5VGUhR
 position=c
 hardware-version=1,0,0
 firmware-version=2,0,1
 device-identifier=ambient-light-v3-bricklet
 enumeration-type=available
 
 uid=Dkq
 connected-uid=5VGUhR
 position=d
 hardware-version=1,0,0
 firmware-version=2,0,6
 device-identifier=humidity-v2-bricklet
 enumeration-type=available
 
 uid=6esErP
 connected-uid=5VGUhR
 position=1
 hardware-version=2,1,0
 firmware-version=2,4,10
 device-identifier=master-brick
 enumeration-type=available
 
 uid=JmM
 connected-uid=6esErP
 position=a
 hardware-version=1,0,0
 firmware-version=2,0,2
 device-identifier=motion-detector-v2-bricklet
 enumeration-type=available
 
 uid=Jop
 connected-uid=6esErP
 position=b
 hardware-version=1,0,0
 firmware-version=2,0,1
 device-identifier=segment-display-4x7-v2-bricklet
 enumeration-type=available
 
 uid=J7d
 connected-uid=6esErP
 position=c
 hardware-version=1,0,0
 firmware-version=2,0,2
 device-identifier=ptc-v2-bricklet
 enumeration-type=available

Read out connected sensors (adapt the UID):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring call temperature-bricklet SCT31 get-temperature
 temperature=2487

 $ tinkerforge --host ServerMonitoring call ambient-light-v2-bricklet ajC get-illuminance
 illuminance=410

 $ tinkerforge --host ServerMonitoring call ptc-bricklet fow get-temperature
 temperature=2603

The shell bindings support the execution of additional shell commands with the
``--execute`` option (see :ref:`Shell Bindings <ip_connection_shell_output>` for more
information). The following script shows how to convert the returned value into
degree Celsius and how to save it in a variable for further use.

.. code-block:: bash

 #!/bin/sh
 
 HOST=ServerMonitoring
 TEMP_UID=Jk3
 
 temp=$(tinkerforge --host $HOST call temperature-v2-bricklet $TEMP_UID get-temperature\
        --execute "echo '{temperature} / 100' | bc -l | xargs printf '%.2f\n'")
 echo $temp


The next script shows how to show text on the :ref:`E-Paper 296x128 Bricklet<e_paper_296x128_bricklet>`

 code-block:: bash

 #!/bin/sh
 
 HOST=ServerMonitoring
 E_PAPER_UID=Jn6
 
 tinkerforge --host $HOST call e-paper-296x128-bricklet $E_PAPER_UID fill-display 1
 tinkerforge --host $HOST call e-paper-296x128-bricklet $E_PAPER_UID draw-text 0 0 4 2 0 $1
 tinkerforge --host $HOST call e-paper-296x128-bricklet $E_PAPER_UID draw

Using the last script (saved as print_e_paper.sh) with the following will print the current
temperature on the E-Paper Bricklet.

.. code-block:: bash

 #!/bin/sh
 
 HOST=ServerMonitoring
 TEMP_UID=Jk3
 
 temp=$(./tinkerforge_shell --host $HOST call temperature-v2-bricklet $TEMP_UID get-temperature\
        --execute "echo '{temperature} / 100' | bc -l | xargs printf '%.2f\n'")
 ./print_e_paper.sh "Temperature:$temp\xF8C"
 
.. _starter_kit_server_room_monitoring_v2_nagios_or_icinga_index:

Server Room Monitoring with Nagios or Icinga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
	A ready-to-use Icinga Check Plugin that is maintained by `Netways <https://www.netways.de>`__
	can be found on the icinga exchange: `https://exchange.icinga.com/netways/check_tinkerforge <https://exchange.icinga.com/netways/check_tinkerforge>`__

`Icinga <https://www.icinga.com/>`__ and `Nagios <https://www.nagios.org/>`__
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
<starter_kit_server_room_monitoring_v2_nagios_or_icinga>`.

.. toctree::
   :hidden:

   Details <NagiosOrIcinga>

The section about :ref:`further enhancements
<starter_kit_server_room_monitoring_v2_further_enhancements>` lists more
Nagios/Icinga examples.


.. _starter_kit_server_room_monitoring_v2_further_enhancements:

Further Enhancements
--------------------

If you have modded, extended or improved the kit
in any way and you have published your results on our 
`forum <https://www.tinkerunity.org/>`__, on your blog or similar:
Please give us a notice. We would love to add a link to your project here!


.. _starter_kit_server_room_monitoring_v2_extended_nagios_index:

Motion Detector and Error Code Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The casing already has the necessary cut-outs for a :ref:`Motion Detector Bricklet 2.0 <motion_detector_v2_bricklet>`
Use a Motion Detector Bricklet to detect motion in your server room. With the 
:ref:`Segment Display 4x7 Bricklet 2.0 <segment_display_4x7_v2_bricklet>` or 
the E-Paper Bricklet can be used to show error codes. With the E-Paper 
Bricklet the codes can be shown even after a blackout.

The full project description can be found 
:ref:`here <starter_kit_server_room_monitoring_v2_extended_nagios>`.

.. image:: /Images/Kits/server_room_monitoring_front_right_seg_motion_close_350.jpg
   :scale: 100 %
   :alt: Extended version of kit
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_front_right_seg_motion_close_1000.jpg

.. toctree::
   :hidden:

   Details <ExtendedNagios>


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
