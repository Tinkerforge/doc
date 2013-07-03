
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Smoke Detector Hardware Setup

.. _starter_kit_hardware_hacking_smoke_detector_hardware_setup:

Smoke Detector Hardware Setup
=============================

Typically a smoke Detector is equipped with one or more LEDs that signal the
state. The number and behaviour of the LEDs will depend on the used model.

In this example we use an `ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
smoke detector. This smoke detector is wirelessly
interconnectable. That means, you can put a smoke detector in every room
and if smoke is detected, all of the smoke detectors will start making
noise.

This is perfect for our hacking purposes. We can hack one of the
smoke detectors and place it next to the PC. It will be triggered
by the other smoke detectors that are scattered throughout the house.


Taking a look at the Smoke Detector
-----------------------------------

The ELRO FA20RF/2 has two LEDs next to the "TEST" and "LEARN" buttons.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_leds_closeup_350.jpg
   :scale: 100 %
   :alt: Smoke detector LEDs
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_open_600.jpg

If we start a test alarm, we can see that the LED on the right side blinks
green everytime an alarm is triggered.

Now that we have located an LED that represents the state we want to
read out, we can open the casing of the detector.
In our case it looks like the following:

.. image:: /Images/Kits/hardware_hacking_smoke_detector_open_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_open_1200.jpg

The LED in question is the transparent LED on the top right. It is
a two-color LED and it can blink green as well as red. We will have
to find the pins that control the green color of the LED.

Since the LED is of through-hole type, the contacts are only exposed at the
bottom.

We have to remove the screws to get to the other side of the circuit board.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_inside_350.jpg
   :scale: 100 %
   :alt: Smoke detector bottom opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_inside_1200.jpg

The three solder pads at the top, left to the red sticker belong to
the LED. We will have to solder wires to them.

Connecting wires to the LED
---------------------------

See here (TODO) for a basic soldering tutorial and here (TODO) for instructions
how you can find the correct pins for the job.

In case of the ELRO FA20RF/2 the two pads at the left can be used.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_new_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened with soldered LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_new_1200.jpg

For the left pad we trace the circuit board trace until we find the resistor.
The cable is soldered on behind the resistor.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_closeup_w_trace_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened with soldered LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_closeup_w_trace_1200.jpg

After that we can screw the circuit board back to the casing.
We connect the wires to the + and - of port 0 of the Industrial Digital In 
Bricklet. We can check if the polarity is correct later on with the Brick Viewer.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_new_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened with soldered wires to LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_new_1200.jpg

Now we can test the hacked smoke detector. To do that, we can press the test
button. The reaction of the LED should be represented in the 
Brick Viewer. 

.. image:: /Images/Kits/hardware_hacking_doorbell_brickv_350.jpg
   :scale: 100 %
   :alt: LED voltage signal in Brick Viewer
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_brickv.jpg

If nothing shows up in the Brick Viewer the wires are most 
likely reversed. In this case you have to change the polarity 
(switch VIN and GND).
