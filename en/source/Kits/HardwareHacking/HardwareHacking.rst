
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Hardware Hacking
:shoplink: ../../../shop/kits/starter-kit-hardware-hacking.html

.. include:: HardwareHacking.substitutions

.. _starter_kit_hardware_hacking:

Starter Kit: Hardware Hacking
=============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/hardware_hacking_remote_finished_new_350.jpg",
	               "Kits/hardware_hacking_remote_finished_new_800.jpg",
	               "Hardware Hacking: Kit with Remote Switches")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_smoke_detector_finished_new_100.jpg",
	             "Kits/hardware_hacking_smoke_detector_finished_new_800.jpg",
	             "Hardware Hacking: Kit with Smoke Detector")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_garage_remote_finished_new_100.jpg",
	             "Kits/hardware_hacking_garage_remote_finished_new_800.jpg",
	             "Hardware Hacking: Kit with Garage Door Remote")
	}}
	{{ tfdocend() }}


Features
--------

* Hack any low voltage electronic appliance and make it controllable by

  * PC, smart phone/tablet or over the internet (Internet of Things).
  * Demo applications for Android, Windows Phone and iPhone* are available.

* Read out and control low voltage mainstream devices,

  * e.g. smoke detectors, remote mains switches, garage door openers and doorbells.

* Interaction over USB, Wi-Fi or Ethernet possible.

\*: Demo for iPhone comming soon

Description
-----------

The *Starter Kit: Hardware Hacking* is about hacking low voltage mainstream
devices to connect them with Tinkerforge modules. Any (Embedded-) PC,
Smart Phone or Tablet can be used to interact with devices hacked by this kit.
Interaction is possible over USB or via Wi-Fi if a :ref:`WIFI Extension <wifi_extension>`
is added. Also a direct Ethernet interface with the
:ref:`Ethernet Extension <ethernet_extension>` can be achieved.

There are two groups of applications of this kit: controlling and reading 
out. For control applications an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` is included. It contains four on/off
switches. For read-out applications an :ref:`Industrial Digital In 4 Bricklet
<industrial_digital_in_4_bricklet>` is included. It can read out galvanically 
isolated four digital signals with voltages up to 36V.

* Forwarding smoke detector alarm to a PC.
* Controlling remote mains switches with a PC.
* Opening/Closing garage doors over a smart phone/tablet (Android, Windows Phone and iPhone).
* Forwarding door bell ringing to a PC.

Many more applications are possible, anything that is controlled by
a remote control or output digital signals is easily hackable by this Kit.
The given examples applications should be enough to give you the power
to hack any electronic appliance in this category.

Programming can be done with all of the available bindings (|bindings|).
Example implementations for each of the languages are available. This Kit
will also give you a good starting point into the programming with Tinkerforge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Digital Inputs                    Four
Digital Input Low Level Voltage   0-2V
Digital Input High Level Voltage  3-36V
Digital Outputs                   Four
Maximum Switching Current         1.2A per switch
Maximum Switching Voltage         30V per switch
================================  ============================================================

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
if all of the firmwares are up to date (Updates / Flashing button). If not, you can
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

Detect Digital Signals up to 36V
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to read out the state of an electronic device, often 
there is a voltage source somewhere that represents this state. If it is a digital signal
and the voltage is below 36V, you can connect the Industrial Digital In 4 Bricklet to it and read 
it out. One good option are LEDs. If your device has an LED representing the state you 
can easily read the state. But of course also other voltage sources are possible.
It is important to keep in mind that a high signal level is detected starting on 3V
and a low signal level is detected below 2V.

To read out a signal, connect it to one of the input ports of the Industrial Digital In 4 Bricklet.
If you don't see any reaction of the input port in Brick Viewer you likely have to reverse 
the polarity of the input. You don't have to bother since the Bricklet can't be damaged
with voltages below 36V.

.. image:: /Images/Kits/hardware_hacking_idi4_resistor_diode.jpg
   :scale: 100 %
   :alt: Example schematic: Industrial Digital In 4 Bricklet measuring LED state
   :align: center


Short Signals with a Voltage up to 30V
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Industrial Quad Relay Bricklet you can switch (short circuit) signals. 
Many devices have switches or push buttons that can be hacked by 
the Bricklet. Remote controls are good examples for it.

.. image:: /Images/Kits/hardware_hacking_idq_switch.jpg
   :scale: 100 %
   :alt: Example schematic: Industrial Quad Relay Bricklet bypassing switch
   :align: center


Hardware Hacking for beginners
------------------------------

To connect the Industrial Digital In 4 or the Industrial Quad Relay Bricklet
you have to accomplish two things:

* Find solder pads that can be used to measure or switch a voltage.
* Solder cables to these pads.

If you have never done this, click :ref:`here <starter_kit_hardware_hacking_for_beginners>`
for an in-depth guide that explains both steps.

Examples
--------

There are many low voltage appliances that can be hacked. Here are some examples:

.. _starter_kit_hardware_hacking_smoke_detector:

Readout Smoke Detectors
^^^^^^^^^^^^^^^^^^^^^^^

Wireless interconnectable smoke detectors allow to read out the alarm signal of
a whole smoke detector network at a single point. We are going to hack such a
smoke detector and utilized this feature to trigger actions if smoke is
detected. For example, notify someone with an email or a text message about the
alarm.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_new_350.jpg
   :scale: 100 %
   :alt: Smoke Detector with connected Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_new_1200.jpg

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

Control Remote Mains Switches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Simple remote switches can be used as a first step towards home automation.
We are going to hack the remote control of such a switch and connect it to a PC
to create software controlled remote switches.

.. image:: /Images/Kits/hardware_hacking_remote_finished_new_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_finished_new_1200.jpg

For this project we use the remote switch set `ELRO AB440WD/2
<http://www.elro.eu/en/products/cat/home-automation/home-control/outdoor1/2-outdoor-switches-with-remote-control>`__
and connect an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` to the buttons of the `ELRO AB440RA
<http://www.elro.eu/en/products/cat/home-automation/home-control1/transmitters1/remote-control1>`__
remote control. There are a vast number of control remote switches available. 
Most of the commercially available remote controls use the HX2262 IC
with the same hardware design, so this guide can be used for most 
remote switches.

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
and we are going to hack one. After the hack your smart phone can control the garage
door and you don't need to carry around the original remote control
anymore. This project is based on this
`project <http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_new_350.jpg
   :scale: 100 %
   :alt: Garage Door Opener with Android Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_new_1200.jpg

A small hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_garage_control_hardware_setup>`.

Example apps for :ref:`Android (Java)
<starter_kit_hardware_hacking_garage_control_android>`
and :ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_garage_control_windows_phone>` are available.
The Android app is an improved version of this `project
<http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__
in the wiki.

A Demo app for iPhone is comming soon.

.. toctree::
   :hidden:

   GarageControl_HardwareSetup
   GarageControl_Android
   GarageControl_WindowsPhone


Is someone at the Door? - Doorbell Notifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this project on port of the Industrial Digital In 4 Bricklet is connected
to a 12V Doorbell. The python script prints "Ring Ring Ring!" if someone 
actuates the doorbell. You can extend this project such that it will 
send an SMS or let your phone ring if someone is at your door. Be creative! 

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Doorbell notifier
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed.jpg

Description of the hardware setup and more pictures can be found
:ref:`here <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>`.

An example application is available
in :ref:`Python <starter_kit_hardware_hacking_doorbell_notifier_python>`.

.. toctree::
   :hidden:

   DoorbellNotifier_HardwareSetup
   DoorbellNotifier_Python
