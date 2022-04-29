
:shoplink: ../../../shop/power-supplies/esp32-power-supply.html

.. _esp32_power_supply:

ESP32 Power Supply
==================

.. raw:: html

	{% tfgallery %}

	Power_Supplies/psu_esp32_tilted_[?|?].jpg                  ESP32 Power Supply
	Power_Supplies/psu_esp32_tilted_bottom_[?|?].jpg           ESP32 Power Supply
	Power_Supplies/psu_esp32_w_esp_[?|?].jpg                   ESP32 Power Supply with ESP32 Brick
	Power_Supplies/psu_esp32_w_esp_ethernet_[?|?].jpg          ESP32 Power Supply with ESP32 Ethernet Brick

	{% tfgalleryend %}

Features
--------

* Powers a ESP32 Brick or ESP32 Ethernet Brick with 5V
* Input voltage 7V to 27V DC

Description
-----------

The ESP32 Power Supply can be used to power :ref:`ESP32 Brick <esp32_brick>`
or a :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` and its connected
:ref:`Bricklets <primer_bricklets>`. The power supply generates 5VDC from an
input voltage between 7V and 27V DC.

The power supply module is 40 x 40mm in size and can be mounted on top of
the Bricklet connectors of the Brick with 10mm standoffs. Electrical connection
is established by the GPIO header of the ESP32 (Ethernet) Brick.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               20-30mA, depending on Input Voltage
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Minimum/Maximum Input Voltage     7V/27V DC
Maximum Output Current            | 5V Supply: 1A
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            9g
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/esp32-power-supply/raw/master/hardware/esp32-power-supply-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/esp32_power_supply_dimensions.png>`__)
* Project design files (`Download <https://github.com/Tinkerforge/esp32-power-supply/zipball/master>`__)
* 3D model (`View online <https://autode.sk/x>`__ | Download: `STEP <https://download.tinkerforge.com/3d/power_supplies/esp32_power_supply/esp32-power-supply.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/power_supplies/esp32_power_supply/esp32-power-supply.FCStd>`__)

Connectivity and Mounting
-------------------------

To attach the ESP32 Power Supply to an ESP32 Brick or ESP32 Ethernet Brick
you have to solder in the male header for the Brick.

Afterwards the power supply is attached to the Brick with four 10mm standoffs.

..
 The following picture shows the electrical connection to the ESP32 Power
 Supply.

 .. image:: /Images/Power_Supplies/esp32_caption_600.jpg
    :scale: 100 %
    :alt: ESP32 Power Supply with caption
    :align: center
    :target: ../../_images/Power_Supplies/esp32_caption_800.jpg
