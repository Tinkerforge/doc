
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Hardware Hacking
:shoplink: ../../../shop/kits/starter-kit-hardware-hacking.html

.. include:: HardwareHacking.substitutions

.. _starter_kit_hardware_hacking:

Starter Kit: Hardware Hacking
=============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/hardware_hacking_remote_finished_350.jpg",
	               "Kits/hardware_hacking_remote_finished_800.jpg",
	               "Hardware Hacking: Kit with Remote Switches")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_smoke_detector_finished_100.jpg",
	             "Kits/hardware_hacking_smoke_detector_finished_800.jpg",
	             "Hardware Hacking: Kit with Smoke Detector")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_garage_remote_finished_100.jpg",
	             "Kits/hardware_hacking_garage_remote_finished_800.jpg",
	             "Hardware Hacking: Kit with Garage Door Remote")
	}}
	{{ tfdocend() }}


Features
--------

* Hack miscellaneous devices and make them controllable by:

  * PC, Smartphone or over the Internet (Internet of Things)

* Readout and control low voltage main stream devices

  * e.g. smoke detectors, remote switches and garage door openers

* Interaction over USB, Wi-Fi or Ethernet

Description
-----------

The *Starter Kit: Hardware Hacking* is about hacking low voltage main stream
devices to connect them with Tinkerforge modules. Then any (Embedded-) PC,
Smart Phone or Tablet can be used to interact with these hacked devices over USB.
Interaction via Wi-Fi is possible if a :ref:`WIFI Extension <wifi_extension>`
is added. Also a direct Ethernet interface is possible with the
:ref:`Ethernet Extension <ethernet_extension>`.

There are two groups of applications of this kit: control and readout. For
control applications an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` is included, that contains four on/off
switches. For readout applications an :ref:`Analog In Bricklet
<analog_in_bricklet>` is included, that can measure a single voltage.

Programming can be done with all of the available bindings (|bindings|).
Example implementations for each of the languages are available. This will
give you a starting point into the programming with Tinkerforge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Voltage Measurement               0V - 45V in 1mV steps, 12bit resolution
Maximum Switching Current         1.2A*
Maximum Switching Voltage         30V*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            ? x ? x ?mm (? x ? x ?")
Weight                            ?g
================================  ============================================================

\* per switch

Resources
---------

* Example source code *Smoke Detector* (Download: |smoke_detector_examples_download|)
* Example source code *Control Remote Switches* (Download: `C# <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch/csharp>`__)
* Example source code *Control Garage Door Openers* (Download: `Android (Java) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control/android>`__, `Windows Phone (C#) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control/windows_phone>`__)
* Example source code *Doorbell Notifier* (Download: `Python <https://github.com/Tinkerforge/hardware-hacking/tree/master/doorbell_notifier/python>`__)

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

.. image:: /Images/Kits/hardware_hacking_update_350.jpg
   :scale: 100 %
   :alt: Firmware update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/hardware_hacking_update.jpg

As next step click through the tabs of the Brick Viewer
to see if the Bricklets are working correctly. Now you can be sure that 
the Bricks and Bricklets have versions that work together.


How it works
------------

Basically there are two different options with this kit:

Measure voltages up to 45V
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to read out the state of an electronic device, maybe 
there is a voltage source somewhere which represents this state. If this voltage is 
below 45V you can connect the Analog In Bricklet to it and measure it. One 
good option are LEDs. If your device has an LED representing the state you 
can make it readable easily. But of course also other voltage sources are possible
if these are below 45V.

To measure a voltage source, connect it to the Analog In Bricklet to the VIN and GND
inputs.

.. warning:: Do not connect to 3.3V or 5V! These are outputs of the Bricklet.

If you don't see feasibly measurements in Brick Viewer you likely have to reverse 
polarity of your voltage source.

.. image:: /Images/Kits/hardware_hacking_analog_in_diode_350.jpg
   :scale: 100 %
   :alt: Example schematic: Analog In Bricklet measuring LED state
   :align: center
   :target: ../../_images/Kits/hardware_hacking_analog_in_diode.jpg


Short signals with a voltage up to 30V
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Industrial Quad Relay Bricklet you can switch (short circuit) signals. 
For example many devices have switches or push buttons which can be bypassed by 
the Bricklet. Remote controls are good examples for it.

.. image:: /Images/Kits/hardware_hacking_industrial_quad_switch_350.jpg
   :scale: 100 %
   :alt: Example schematic: Industrial Quad Relay Bricklet bypassing switch
   :align: center
   :target: ../../_images/Kits/hardware_hacking_industrial_quad_switch.jpg


Examples
--------

There are several low voltage devices that can be hacked. Here are some examples:

.. _starter_kit_hardware_hacking_smoke_detector:

Readout Smoke Detectors
^^^^^^^^^^^^^^^^^^^^^^^

Wireless interconnectable smoke detectors allow to readout the alarm signal of
a whole smoke detector network at a single point. We are going to hack such a
smoke detector and utilized this feature to trigger actions if smoke is
detected. For example, notify someone with an email or a text message about the
alarm.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Smoke Detector with connected Analog In Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

For this project we use the wireless smoke detector set `ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
and connect an :ref:`Analog In Bricklet <analog_in_bricklet>` to one of its
LEDs that light up during an alarm.

The full hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_smoke_detector_hardware_setup>`.

Example implementations with step-by-step instructions are available for:

|smoke_detector_examples|.

.. include:: SmokeDetector.toctree

.. toctree::
   :hidden:

   SmokeDetector_HardwareSetup


.. _starter_kit_hardware_hacking_remote_switch:

Control Remote Switches
^^^^^^^^^^^^^^^^^^^^^^^

Simple remote switches can be used as a first step towards home automation.
We are going to hack the remote control of such a switch and connect it to a PC
to create software controlled remote switches.

.. image:: /Images/Kits/hardware_hacking_remote_finished_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_finished_1200.jpg

For this project we use the remote switch set `ELRO AB440WD/2
<http://www.elro.eu/en/products/cat/home-automation/home-control/outdoor1/2-outdoor-switches-with-remote-control>`__
and connect an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` to the buttons of the `ELRO AB440RA
<http://www.elro.eu/en/products/cat/home-automation/home-control1/transmitters1/remote-control1>`__
remote control. There are a vast number of control remote switches available. Typically
all used remote controls used for them base on a IC HX2262 and the same hardware design, 
so this guide can be taken for all of these remote switches.

The full hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_remote_switch_hardware_setup>`.

An example implementation is available
in :ref:`C# <starter_kit_hardware_hacking_remote_switch_csharp>`.

.. toctree::
   :hidden:

   RemoteSwitch_HardwareSetup
   RemoteSwitch_CSharp


.. _starter_kit_hardware_hacking_garage_control:

Control Garage Door Openers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Garage door openers are quite useful. Typically they come with a remote control
and we are going to hack one. Then your smart phone can control the garage
door opener and you don't need to carry around the original remote control
anymore. Basically this project based this 
`project <http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__
in the wiki.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_350.jpg
   :scale: 100 %
   :alt: Garage Door Opener with Android Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_1200.jpg

A small hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_garage_control_hardware_setup>`.

Example apps for :ref:`Android (Java)
<starter_kit_hardware_hacking_garage_control_android>`
and :ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_garage_control_windows_phone>` are available.
The Android app is an improved version of this `project
<http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__
in the wiki.

.. toctree::
   :hidden:

   GarageControl_HardwareSetup
   GarageControl_Android
   GarageControl_WindowsPhone


Is someone at the Door? - Doorbell Notifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a project basically identical to
the smoke detector project. The Analog In Bricklet is connected
to a 12V doorbell. The Python script prints "Ring Ring Ring!" if someone
actuates the doorbell. Of course this project can be extended such that it will 
send an Email or SMS to your phone if someone is at your door.

.. image:: /Images/Kits/hardware_hacking_doorbell_350.jpg
   :scale: 100 %
   :alt: Doorbell notifier
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell.jpg

Description of the hardware setup and more pictures can be found
:ref:`here <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>`.

An example application is available
in :ref:`Python <starter_kit_hardware_hacking_doorbell_notifier_python>`.

.. toctree::
   :hidden:

   DoorbellNotifier_HardwareSetup
   DoorbellNotifier_Python
