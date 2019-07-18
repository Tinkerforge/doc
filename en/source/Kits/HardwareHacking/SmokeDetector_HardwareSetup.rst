
.. _starter_kit_hardware_hacking_smoke_detector_hardware_setup:

Smoke Detector Hardware Setup
=============================

Typically a smoke Detector is equipped with one or more LEDs that signal the
state. The number and behavior of the LEDs will depend on the used model.

In this example we use an `ELRO FA20RF/2
<https://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
smoke detector. This smoke detector is wirelessly
interconnectable. That means, you can put a smoke detector in different rooms
and if smoke is detected, all of the smoke detectors will start making
noise.

This is perfect for our hacking purposes. We can hack one of the
smoke detectors and place it next to the PC. It will be triggered
by the other smoke detectors that are scattered throughout the house
and we can read out its state.


The innards of the Smoke Detector
---------------------------------

The ELRO FA20RF/2 has two LEDs next to the "TEST" and "LEARN" buttons.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_leds_closeup_350.jpg
   :scale: 100 %
   :alt: Smoke detector LEDs
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_open_600.jpg

If we start a test alarm, we can see that the LED on the right side blinks
green every time an alarm is triggered.

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

Since the LED is of through-hole type (not SMD), the contacts are only exposed 
at the bottom.

We have to remove the screws to get to the other side of the circuit board.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_inside_350.jpg
   :scale: 100 %
   :alt: Smoke detector bottom opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_inside_1200.jpg

The three solder pads at the top, left to the red sticker belong to
the LED. We will have to solder wires to them.

Soldering Wires to the LED and its Series Resistor
--------------------------------------------------

See :ref:`here  <starter_kit_hardware_hacking_for_beginners_soldering>`
for a basic soldering tutorial and 
:ref:`here <starter_kit_hardware_hacking_for_identify_series_resistor>`
for instructions how you can find the correct pins of the LED and its series
resistor.

In case of the ELRO FA20RF/2 the transparent LED consists in fact of two
LEDs (one green and one red) in one casing. Both LEDs have one common pin 
(center) and one individual pin (pin left, right).
To light the green LED the left pin is used.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened with soldered LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_1200.jpg

We solder one wire to the center pin of the LED and trace the circuit from the
left pin until we find the resistor
(marked in red). The cable is soldered behind this resistor.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_closeup_w_trace_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened with soldered LED closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_closeup_w_trace_1200.jpg

After that we can screw the circuit board back to the casing.
We connect the wires to the + and - of port 0 of the Industrial Digital In 4
Bricklet. We can check if the polarity is correct later with the Brick Viewer.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Smoke detector opened with soldered wires to LED connected to Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

Now we can test the hacked smoke detector. To do that, we press the test
button. The reaction of the LED should be represented in the 
Brick Viewer. 

.. image:: /Images/Kits/hardware_hacking_doorbell_brickv_350.jpg
   :scale: 100 %
   :alt: Brick Viewer: Industrial Digital In 4
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_brickv.jpg

If the state of the input does not change in Brick Viewer the wires are most 
likely reversed. In this case you have to swap them.
