
:DISABLED_shoplink: ../../../shop/bricks/esp32-brick.html

.. include:: ESP32_Brick.substitutions


.. _esp32_brick:

ESP32 Brick
===========


.. raw:: html

	{% tfgallery %}

	{% tfgalleryend %}


Features
--------

* Ports for **six** 7-pole Bricklets
* Execute your own code directly on this Brick (**stand-alone**)
* Use the preprogrammed Brick to control Bricklets via **WIFI**

.. _esp32_brick_description:

Description
-----------

The ESP32 Brick offers **six** :ref:`Bricklet <primer_bricklets>` ports and is 
equipped with a powerful ESP32 microcontroller. The ESP32 is equipped with two CPU cores 
(up to 240MHz), 16MB SPI Flash, WIFI (802.11b/g/n) and Bluetooth (V4.2 BR/EDR, 
BLE). 

You can use this Brick for two use cases:

The Brick can be used for **stand-alone** applications where you want to flash
and execute your own code on the device. By integrating the
:ref:`C/C++ API Bindings for Microcontrollers <api_bindings_uc>` libraries in 
your code, you can easily access the connected Bricklets. Support for WIFI,
Bluetooth and other ESP32 features is available by the official Espressif ESP32 
plattform libraries. Your software can be flashed to the Brick by an onboard 
USB to UART converter directly connected to the ESP32 or by WIFI when using a 
appropriate firmware.

If you want to control the Brick with the high-level APIs from Tinkerforge
you can use the pre-programmed standard firmware that is flashed by default.
With this firmware you can access the connected Bricklets through the **WIFI**
connection of the Brick.
The standard firmware offers a web interface to manage the WIFI settings.
For the initial setup a **WIFI access point** is opened by the ESP32.
After the setup process this access point can be disabled.

A simultaneous use of stand-alone applications and an additional external
control through the high-level API is possible. As a consequence you
can react on specific events immediately (closed loop) while while
having other parts of the system controlled externally (open loop).

The Brick can eitehr be powered over its USB-C connector, by the
:ref:`ESP32 Power Supply <todo>` through the GPIO connector of the Brick.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Power Supply                      By USB-C jack, optional ESP32 Power Supply module
Current Consumption               TBDmW (TBDmA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    6 (7-pole)
ESP32 Variant                     ESP32WROOM32E with 16MB Flash (ESP32WRM32E128PH)
WIFI                              802.11b/g/n (with up to 150 Mbps)
Bluetooth                         V4.2 BR/EDR and Bluetooth LE
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            66 x 40 x 9mm (2.60 x 1.57 x 0.35")
Weight                            TBDg 
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/esp32-brick/raw/master/hardware/esp32-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/esp32_brick_dimensions.png>`__)
* Source code (`Download <https://github.com/Tinkerforge/esp32-firmware/zipball/master>`__)
* Design files (`Download <https://github.com/Tinkerforge/esp32-brick/zipball/master>`__)
* 3D model (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/esp32/esp32.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/esp32/esp32.FCStd>`__)


.. _esp32_brick_getting_started:

Getting Started
---------------

TODO: How to configure the WIFI connection of the default firmware of the
ESP32 Brick to use it as replacement for Master Brick with WIFI Extension?


.. _esp32_brick_firmware:

Firmware
--------

TODO: What firmware variations exists and how to use them?

:ref:`esp32_firmware`
