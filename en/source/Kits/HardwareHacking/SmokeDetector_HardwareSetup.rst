
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Smoke Detector Hardware Setup

.. _starter_kit_hardware_hacking_smoke_detector_hardware_setup:

Smoke Detector Hardware Setup
=============================

Typically a smoke Detector is equipped with one or more LEDs which signal the
state. The number and behaviour of the LEDs will depend on the used model.

In this example we use an `ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
smoke detector. It is equipped with two different LEDs. One lights up during
alarm red, it is a combined green/red LED.

Take a look at the Smoke Detector
---------------------------------

After locating the correct LED we have to open the casing of the detector.
In our case it looks like the following:

.. image:: /Images/Kits/hardware_hacking_smoke_detector_open_350.jpg
   :scale: 100 %
   :alt: Smoke Detector Opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_open_1200.jpg

Next we will remove the screws and the other side of the casing.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_inside_350.jpg
   :scale: 100 %
   :alt: Smoke Detector Bottom Opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_inside_1200.jpg

Now we have access to the LED contacts so we can solder wires to it.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_closeup_350.jpg
   :scale: 100 %
   :alt: Smoke Detector Openend with soldered LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_closeup_1200.jpg

We connect these wires to the Analog In Bricklet. We will check for the right polarity later.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_350.jpg
   :scale: 100 %
   :alt: Smoke Detector OPenend with soldered wires to LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_1200.jpg

After that we can close the casing.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_closed_350.jpg
   :scale: 100 %
   :alt: Smoke Detector Openend with soldered wires to LED Closed
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_closed_1200.jpg

At the end we can thest the hardware setup. We trigger the test button and can use the
Brick Viewer to see the reaction of the LED. If we do not see anything our wires are
most likely reversed. So change the polarity.
