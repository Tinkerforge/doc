
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Doorbell Notifier Hardware Setup

.. _starter_kit_hardware_hacking_doorbell_notifier_hardware_setup:

Doorbell Notifier Hardware Setup
================================

General Idea
^^^^^^^^^^^^

The hardware setup is pretty simple. Typically doorbells are driven by 12V AC 
(Alternating Current). This voltage is measured by the Analog In Bricklet. 

The Analog In Bricklet can't measure AC voltages since it can't measure negative 
voltages, so it is only able to measure the positive part of the wave.
But this does not present a problem since we don't want to measure a value.
We only want to detect a trigger.

Hardware Setup
^^^^^^^^^^^^^^

The Analog In Bricklet is connected in 
parallel to the doorbell. The Brick Viewer can be used to find out if the 
Analog In Bricklet can detect if someone is using the doorbell.

TODO BrickV Screenshot

.. image:: /Images/Kits/hardware_hacking_doorbell3_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet attached to Doorbell
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell3.jpg

.. image:: /Images/Kits/hardware_hacking_doorbell2_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet attached to Doorbell
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell2.jpg

.. image:: /Images/Kits/hardware_hacking_doorbell_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet attached to Doorbell
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell.jpg

