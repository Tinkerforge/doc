
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Doorbell Notifier Hardware Setup

.. _starter_kit_hardware_hacking_doorbell_notifier_hardware_setup:

Doorbell Notifier Hardware Setup
================================

General Idea
^^^^^^^^^^^^

The hardware setup is pretty simple. Typically doorbells are driven by 12V AC 
(Alternating Current), this current is applied on the doorbell by two wires.
If you have such a doorbell you can connect an Industrial Digital In 4 Bricklet
to it, by connecting one input port of the Bricklet to the doorbell.
This way the input port will be triggered if someone triggers the doorbell.
A more detailed description how to connect it can be found in the following
:ref:`hardware setup <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup_setup>`
section.

More precise description
^^^^^^^^^^^^^^^^^^^^^^^^

This part is for those who are interested in a more technical description.

If you take a closer look at alternating currents you will see positive and 
negative half-waves. 

.. image:: /Images/Kits/hardware_hacking_doorbell_ac_current_plot_350.jpg
   :scale: 100 %
   :alt: Plot of AC Current
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_ac_current_plot.jpg

A connected input port of an Industrial Digital In 4 
Bricklet basically consists of a light emitting diode (LED inside optocoupler).
If you connect it to an AC source the LED will light up every positive 
half-wave and will be off every negative half wave. So if the doorbell is 
triggered the AC current will flow through the doorbell for some time.
Since you have connected the input port of the Industrial Digital In 4
in parallel to the doorbell the current flows also through the inside LED
and thus your input port will be triggered.

.. _starter_kit_hardware_hacking_doorbell_notifier_hardware_setup_setup:

Hardware Setup
^^^^^^^^^^^^^^

The Industrial Digital In 4 Bricklet is connected in parallel to the doorbell. You can see 
the set-up in the next picture. The big blue and black wire are the original
installed doorbell triggering wires. We have connected a smaller red and
black wire in parallel to the doorbell which are connected to the first
input port of the Industrial Digital In 4 Bricklet.

.. image:: /Images/Kits/hardware_hacking_doorbell_open_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet attached to Doorbell
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_open.jpg

After connecting the Industrial Digital In 4 Bricklet to the doorbell
test it with the Brick Viewer. Trigger the bell, you should
see that the connected input port will change its state from Low to High.

.. image:: /Images/Kits/hardware_hacking_doorbell_brickv_350.jpg
   :scale: 100 %
   :alt: Doorbell Trigger Signal in Brick Viewer
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_brickv.jpg

After closing the casing the installation will look as the following. Of course
you can increase the cable length such that you can install it less visible.

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet attached to Doorbell with closed casing
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed.jpg

Another option is to add a WIFI Master Extension or Ethernet Master Extension, 
such that no direct USB detection is necessary.

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_wifi_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet attached to Doorbell with WiFi Extension
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed_wifi.jpg
