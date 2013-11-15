
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Hardware Hacking
:shoplink: ../../../shop/kits/starter-kit-hardware-hacking.html

.. include:: HardwareHacking.substitutions

.. _starter_kit_hardware_hacking:

Starter Kit: Hardware Hacking
=============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/hardware_hacking_kit_tilted_350.jpg",
	               "Kits/hardware_hacking_kit_tilted_800.jpg",
	               "Hardware Hacking: Soldered Kit with Mains Sockets")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_remote_finished_100.jpg",
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
	{{
	    tfdocimg("Kits/hardware_hacking_smoke_detector_and_remote_new_100.jpg",
	             "Kits/hardware_hacking_smoke_detector_and_remote_new_800.jpg",
	             "Hardware Hacking: Kit with Remote Switches and Smoke Detector")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_content_100.jpg",
	             "Kits/hardware_hacking_content_800.jpg",
	             "Hardware Hacking: Content")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_remote_soldered_closeup_remote_100.jpg",
	             "Kits/hardware_hacking_remote_soldered_closeup_remote_800.jpg",
	             "Hardware Hacking: Remote soldered")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_remote_soldered_closeup_iqr_top_100.jpg",
	             "Kits/hardware_hacking_remote_soldered_closeup_iqr_top_800.jpg",
	             "Hardware Hacking: Quad Relay wiring")
	}}

	{{ tfdocend() }}


Features
--------

* Hack any low voltage electronic appliance and make it controllable by

  * PC, smart phone/tablet, Raspberry Pi or over the Internet (Internet of Things).
  * Demo applications for Android, Windows Phone and iOS* are available.

* Ready to Hack: Two Remote Control Mains Switches included.

* Read out and control low voltage mainstream devices,

  * e.g. smoke detectors, remote mains switches, garage door openers and doorbells.

* Interaction over USB, Wi-Fi or Ethernet possible.


\* Coming soon


Description
-----------

The *Starter Kit: Hardware Hacking* is about hacking low voltage mainstream
devices to connect them with Tinkerforge modules. Any (Embedded-) PC,
Smart Phone or Tablet can be used to interact with devices hacked by this kit.
Interaction is possible over USB or via Wi-Fi if a :ref:`WIFI Extension <wifi_extension>`
is added. Also a direct Ethernet interface with the
:ref:`Ethernet Extension <ethernet_extension>` can be achieved.

Two remote control mains switches are included in this kit, so you can directly
start to hack something. A :ref:`step-by-step guide
<starter_kit_hardware_hacking_remote_switch_hardware_setup>` will tell you how to do it
(soldering iron, solder and a screwdriver are required).

There are two groups of applications of this kit: controlling and reading 
out. For control applications an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` is included. It contains four on/off
switches. For read-out applications an :ref:`Industrial Digital In 4 Bricklet
<industrial_digital_in_4_bricklet>` is included. It can read out four digital
galvanically isolated signals with voltages up to 36V.

Documented example applications are:

* Forwarding smoke detector alarm to a PC.
* Controlling remote mains switches with a PC and smart 
  phone/tablet (Android, Windows Phone and iOS).
* Opening/Closing garage doors over a smart phone/tablet (Android, 
  Windows Phone and iOS).
* Forwarding door bell ringing to a PC.

Many more applications are possible, anything that is controlled by
a remote control or output digital signals is easily hackable by this Kit.
The given examples applications should be enough to give you the power
to hack any electronic appliance in this category.

Programming can be done with all of the available bindings (|bindings|).
Example implementations for many of the languages are available. This kit
will also give you a good starting point into the programming with Tinkerforge.

A how-to video that shows how to hack the mains switches and some applications
can be found on Youtube:

.. raw:: html

 <center><iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/hHnhflS3260" frameborder="0" allowfullscreen></iframe></center>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Digital Inputs                    4
Digital Input Low Level Voltage   0-2V
Digital Input High Level Voltage  3-36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Digital Outputs                   4
Maximum Switching Current         1.2A per switch
Maximum Switching Voltage         30V per switch
================================  ============================================================

Resources
---------

* Example source code :ref:`Control Remote Mains Switches <starter_kit_hardware_hacking_remote_switch>` (Download: |remote_switch_examples_download|)
* Example source code :ref:`Control Remote Mains Switches with GUI <starter_kit_hardware_hacking_remote_switch_gui_csharp>` (Download: `C# <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch_gui/csharp>`__)
* Example source code :ref:`Read out Smoke Detectors <starter_kit_hardware_hacking_smoke_detector>` (Download: |smoke_detector_examples_download|)
* Example source code :ref:`Control Garage Door over smart phone <starter_kit_hardware_hacking_garage_control>` (Download: `Android (Java) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/android>`__, `Windows Phone (C#) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/windows_phone>`__, iOS* (ObjC))
* Example source code :ref:`Doorbell Notifier <starter_kit_hardware_hacking_doorbell_notifier>` (Download: `Python <https://github.com/Tinkerforge/hardware-hacking/tree/master/doorbell_notifier/python>`__)
* Demo application :ref:`Control Remote Mains Switches with GUI <starter_kit_hardware_hacking_remote_switch_gui_csharp>` (Download: `Windows (.NET), Linux (Mono), Mac OS X (Mono) <https://github.com/Tinkerforge/hardware-hacking/raw/master/remote_switch_gui/csharp/RemoteSwitchGUI.exe>`__)
* Demo apps :ref:`Control Remote Mains Switches over smart phone <starter_kit_hardware_hacking_remote_switch>` (Download: `Android <https://play.google.com/store/apps/details?id=com.tinkerforge.poweroutletcontrol>`__, `Windows Phone <http://www.windowsphone.com/s?appid=52e1f6a9-707c-4961-9e68-5736e6d29b73>`__, iOS*)
* Demo apps :ref:`Control Garage Door over smart phone <starter_kit_hardware_hacking_garage_control>` (Download: `Android <https://play.google.com/store/apps/details?id=com.tinkerforge.garagecontrol>`__, `Windows Phone <http://www.windowsphone.com/s?appid=4c9a8f61-d9ed-4fd2-b4e6-a332b617c596>`__, iOS*)

\* Coming soon


Required Tools
--------------

* Soldering Iron
* Solder
* Screwdriver (to open casings etc.)


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

Basically there are two different options with this kit: Detect digital signals
and short-circuit signals. A detailed description of the basics can be found
in the :ref:`Hardware Hacking for Beginners
<starter_kit_hardware_hacking_for_beginners>` tutorial.


.. warning:: Keep voltages in mentioned limitations and don't hack devices 
  which are supplied by dangerous high voltages (e.g. mains voltage)!


Detect Digital Signals up to 36V
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to read out the state of an electronic device, often 
there is a voltage source somewhere that represents this state. If it is 
a digital signal and the voltage is below 36V, you can connect the 
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>` to
it and read it out. A good option are LEDs. If your device has an LED
representing a state you can easily read the state.

It is important to keep in mind that a high signal level is detected 
starting at 3V and a low signal level is detected below 2V. In between
the behavior is undefined.

To read out a signal, connect it to one of the input ports of the 
Industrial Digital In 4 Bricklet. If you don't see any reaction of the 
input port in the Brick Viewer you likely have to reverse 
the polarity of the input. You can find the correct polarity by trial and
error, the Bricklet is protected against reversed polarity.

Below you can find a connection diagram that shows a possible setup
if you want to detect the state of an LED. The series resistor is included
to obtain suffice levels for high/low detection.

.. image:: /Images/Kits/hardware_hacking_idi4_resistor_diode.jpg
   :scale: 100 %
   :alt: Example schematic: Industrial Digital In 4 Bricklet measuring LED state
   :align: center


Short Signals with a Voltage up to 30V
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
you can switch (short circuit) signals.
Many devices have switches or push buttons that can be hacked with this
the Bricklet. Remote controls are good examples.

Below you can find a connection diagram that shows a possible setup
if you want to operate a switch with the Industrial Quad Relay Bricklet.

.. image:: /Images/Kits/hardware_hacking_idq_switch.jpg
   :scale: 100 %
   :alt: Example schematic: Industrial Quad Relay Bricklet bypassing switch
   :align: center


Hardware Hacking for Beginners
------------------------------

To connect the Industrial Digital In 4 or the Industrial Quad Relay Bricklet
to a device you have to accomplish two things:

* Find solder pads that can be used to measure or switch a voltage.
* Solder wires to these pads.

If you have never done this, take a look at the :ref:`Hardware Hacking for
Beginners <starter_kit_hardware_hacking_for_beginners>` tutorial for an
in-depth guide that explains both steps.

.. toctree::
   :hidden:

   ForBeginners


Examples
--------

There are many low voltage appliances that can be hacked. Here are some examples:

.. _starter_kit_hardware_hacking_remote_switch:

Control Mains Switches Remotely
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This kit includes the remote switch set `ELRO AB440WD/2
<http://www.elro.eu/en/products/cat/home-automation/home-control/outdoor1/2-outdoor-switches-with-remote-control>`__.
These remote control mains switches can be used as a first step
towards home automation. We are going to hack the remote control of these 
switches and connect it to a PC to create software controlled remote switches.

.. image:: /Images/Kits/hardware_hacking_remote_finished_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_finished_1200.jpg

We connect an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` to the buttons of the `ELRO AB440RA
<http://www.elro.eu/en/products/cat/home-automation/home-control1/transmitters1/remote-control1>`__
remote control. There are a vast number of remote switches available on the
market. Most of the commercially available remote controls use the HX2262 IC
with the same hardware design as the ELRO remote control.
So this guide can be applied to most remote switches.

The full description of the hardware setup can be found
:ref:`here <starter_kit_hardware_hacking_remote_switch_hardware_setup>`.

Example apps for :ref:`Android (Java)
<starter_kit_hardware_hacking_power_outlet_control_android>`
and :ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_power_outlet_control_windows_phone>` are available.
An example app for iOS is coming soon.

.. toctree::
   :hidden:

   PowerOutletControl_Android
   PowerOutletControl_WindowsPhone

An example implementation of a GUI (compatible to Windows (.NET),
Linux (Mono) and Mac OS X (Mono)) is available in :ref:`C#
<starter_kit_hardware_hacking_remote_switch_gui_csharp>`.

Minimalistic examples are available in:

|remote_switch_examples|

.. include:: SmokeDetector.toctree

.. toctree::
   :hidden:

   RemoteSwitch_HardwareSetup
   RemoteSwitchGUI_CSharp


.. _starter_kit_hardware_hacking_smoke_detector:

Read out Smoke Detectors
^^^^^^^^^^^^^^^^^^^^^^^^

Wirelessly interconnectable smoke detectors allow to read out the alarm signal of
a whole smoke detector network at a single point. We are going to hack such a
smoke detector and utilized this feature to trigger actions if smoke is
detected. For example, notify someone with an email or a text message about the
alarm.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Smoke Detector with connected Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

For this project we use the wireless smoke detector set `ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
and connect an :ref:`Industrial Digital In 4 <industrial_digital_in_4_bricklet>` to one of its
LEDs that light up during an alarm.

The full description of the hardware setup can be found
:ref:`here <starter_kit_hardware_hacking_smoke_detector_hardware_setup>`.

Example implementations with step-by-step instructions are available for:

|smoke_detector_examples|

.. include:: SmokeDetector.toctree

.. toctree::
   :hidden:

   SmokeDetector_HardwareSetup


.. _starter_kit_hardware_hacking_garage_control:

Control Garage Doors Remotely
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Garage door openers are quite useful. Typically they come with a remote control
and we are going to hack one. After the hack your smart phone can control the garage
door and you don't need to carry around the original remote control
anymore. This project is based on this
`project <http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_350.jpg
   :scale: 100 %
   :alt: Garage Door Opener with Android Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_1200.jpg

A small description of the hardware setup can be found
:ref:`here <starter_kit_hardware_hacking_garage_control_hardware_setup>`.

Example apps for :ref:`Android (Java)
<starter_kit_hardware_hacking_garage_control_android>`
and :ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_garage_control_windows_phone>` are available.
An example app for iOS is coming soon.

.. toctree::
   :hidden:

   GarageControl_HardwareSetup
   GarageControl_Android
   GarageControl_WindowsPhone


.. _starter_kit_hardware_hacking_doorbell_notifier:

Is someone at the Door? - Doorbell Notifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this project one port of the Industrial Digital In 4 Bricklet is connected
to a typical 12V driven Doorbell. A Python script prints "Ring Ring Ring!" if someone 
actuates the doorbell. You can extend this project such that it will 
send an SMS or let your phone ring if someone is at your door. Be creative! 

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Doorbell notifier with Industrial Digital In 4
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
