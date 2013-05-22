
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Hardware Hacking
:shoplink: ../../../shop/kits/starter-kit-hardware-hacking.html

.. include:: HardwareHacking.substitutions

.. _starter_kit_hardware_hacking:

Starter Kit: Hardware Hacking
=============================

Features
--------

* Readout and control low voltage main stream devices

  * e.g. smoke detectors, remote switches and garage door openers

* Interaction over USB or Wi-Fi

Description
-----------

The *Starter Kit: Hardware Hacking* is about hacking low voltage main stream
devices to connect them with Tinkerforge modules. Then any (Embedded-) PC,
Smartphone or Tablet can be used to interact with these hacked devices over USB.
Interaction via Wi-Fi is possible if a :ref:`WIFI Extension <wifi_extension>`
is added.

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

Projects
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

For this project we use the wireless smoke detector set `ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
and connect an :ref:`Analog In Bricklet <analog_in_bricklet>` to one of its
LEDs that light up during an alarm.

Example implementations with step-by-step instructions are available for:

|smoke_detector_examples|.

.. include:: SmokeDetector.toctree


.. _starter_kit_hardware_hacking_remote_switch:

Control Remote Switches
^^^^^^^^^^^^^^^^^^^^^^^

Simple remote switches can be used as a first step towards home automation.
We are going to hack the remote control of such a switch and connect it to a PC
to create software controlled remote switches.

For this project we use the remote switch set `ELRO AB440WD/2
<http://www.elro.eu/en/products/cat/home-automation/home-control/outdoor1/2-outdoor-switches-with-remote-control>`__
and connect an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` to the buttons of the `ELRO AB440RA
<http://www.elro.eu/en/products/cat/home-automation/home-control1/transmitters1/remote-control1>`__
remote control. So this instructions apply to all ELRO remote switches that
come with this specific remote control.

An example implementation is available
in :ref:`C# <starter_kit_hardware_hacking_remote_switch_csharp>`.

.. toctree::
   :hidden:

   RemoteSwitch_CSharp

Control Garage Door Openers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

