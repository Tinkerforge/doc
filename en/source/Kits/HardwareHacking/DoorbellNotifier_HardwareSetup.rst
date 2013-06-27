
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
We only want to detect a trigger. On our tests we found an usable trigger 
everytime, if you don't try to add a diode for rectification.

Hardware Setup
^^^^^^^^^^^^^^

The Analog In Bricklet is connected in parallel to the doorbell. You can see 
the set-up in the next picture.




.. image:: /Images/Kits/hardware_hacking_doorbell_open_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet attached to Doorbell
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_open.jpg

After connecting the Analog In Bricklet to the doorbell
test it with the Brick Viewer. Trigger the bell, you should
see a voltage peak similar to the peak depicted below.
Trigger it multiple times to find out the minimum voltage
which you can used as save trigger point.

.. image:: /Images/Kits/hardware_hacking_doorbell_brickv_350.jpg
   :scale: 100 %
   :alt: Doorbell Voltage Signal in Brick Viewer
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_brickv.jpg

After closing the casing the installation will look as the following. Of course
you can increase the cable length such that you can install it less visible.

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet attached to Doorbell with closed casing
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed.jpg

Another option is to add a WIFI Master Extension or Ethernet Master Extension, 
such that no direct USB detection is necessary.

.. image:: /Images/Kits/hardware_hacking_doorbell_wifi_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet attached to Doorbell with WiFi Extension
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_wifi.jpg


