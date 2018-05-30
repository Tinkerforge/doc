
:DISABLED_shoplink: ../../../shop/bricklets/led-strip-v2-bricklet.html


.. role:: led-strip-red

.. role:: led-strip-green

.. role:: led-strip-blue

.. role:: led-strip-black

.. role:: led-strip-white

.. role:: led-pixel-red

.. role:: led-pixel-green

.. role:: led-pixel-blue

.. role:: led-pixel-white


.. include:: LED_Strip_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _led_strip_v2_bricklet:

LED Strip Bricklet 2.0
======================

.. note::
  This Bricklet is currently work-in-progress!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_led_strip_v2_tilted_[?|?].jpg           LED Strip Bricklet 2.0
	Bricklets/bricklet_led_strip_v2_tilted2_[?|?].jpg          LED Strip Bricklet 2.0
	Bricklets/bricklet_led_strip_v2_top_[?|?].jpg              LED Strip Bricklet 2.0
	Cases/bricklet_led_strip_v2_case_[100|600].jpg             LED Strip Bricklet 2.0 with case
	Bricklets/bricklet_led_strip_v2_brickv_[100|].jpg          LED Strip Bricklet 2.0 in Brick Viewer
	Dimensions/led_strip_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Controls up to 2048 RGB or 1536 RGBW LEDs
* All LEDs can be switched independently
* Update rate of up to 100Hz for each LED possible


.. _led_strip_v2_bricklet_description:

Description
-----------

The LED Strip :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
control LED strips and LED pixels that are equipped with the WS2801, WS2811,
WS2812/SK6812 (NeoPixel RGB), SK6812RGBW (NeoPixel RGBW), LPD8806 or
APA102 (DotStar) LED driver.
It is possible to independently control 2048 RGB or 1536 RGBW LEDs (6144 individual LEDs) over
the connected :ref:`Brick <primer_bricks>`.

The API allows to change all LEDs at the same time with a fixed update rate
of up to 100Hz. A possible application can be found in the 
:ref:`Starter Kit: Blinken Lights <starter_kit_blinkenlights>`: 
`Video <https://www.youtube.com/watch?v=mmNRa-lLaXM>`__

The LED Strip Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Supported LED Drivers             | WS2801, WS2811, WS2812/SK6812 (NeoPixel RGB),
                                  | SK6812RGBW (NeoPixel RGBW), LPD8806 and APA102 (DotStar)
Current Consumption               64mW (12.8mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        8bit per LED
Maximum Number of LEDs            6144 (2048 RGB or 1536 RGBW LEDs)
Maximum Update Rate               100 updates per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 12mm (1.18 x 1.18 x 0.47")
Weight                            8.1g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/led-strip-v2-bricklet/raw/master/hardware/led-strip-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/led_strip_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/led-strip-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2rAcbZ9>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/led_strip_v2/led-strip-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/led_strip_v2/led-strip-v2.FCStd>`__)


.. _led_strip_v2_bricklet_test:

Test your LED Strip Bricklet 2.0
--------------------------------

|test_intro|

|test_connect|. After that connect a LED strip or bunch of pixels
to the Bricklet as described below.

|test_tab|
If everything went as expected you can now control a LED strip.

.. image:: /Images/Bricklets/bricklet_led_strip_v2_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_v2_brickv.jpg

|test_pi_ref|


.. _led_strip_v2_bricklet_ws28xy:

Supported LEDs
--------------


The LED Strip Bricklet 2.0 supports LED strips and pixels equipped with the
WS2801, WS2811 or WS2812, SK6812 (NeoPixel RGB), SK6812RGBW (NeoPixel RGBW), 
LPD8806 and APA102 (DotStar) driver ICs. *Driver ICs* refers to any of these chips.

You have to configure which of this driver chips you want to use with the
Brick Viewer or the ``set_chip_type()`` function of the LED Strip Bricklet 2.0.

The driver ICs can control up to four LEDs independently. Typically a RGB(W) LED
combined in one package is used. It is controlled over a three or two wire
chained data bus with clock, data signal and ground as voltage
reference (`daisy chain <https://en.wikipedia.org/wiki/Daisy_chain_(electrical_engineering)>`__).
Each Driver has a bus input connected to a controlling
device such as the LED Strip Bricklet 2.0 or to a driver predecessor and a
bus output which can be connected to a subsequent LED driver.
Since it is a chained bus, a single bus output has to be connected only
to a single bus input. The bus is indexed beginning with the first LED driver on the
LED Strip Bricklet 2.0 (API index 0).

.. image:: /Images/Bricklets/bricklet_led_strip_strip_example_600.jpg
   :scale: 100 %
   :alt: LED Strip with WS2801
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_example_800.jpg

The above picture depicts a typical WS2801 LED strip. You can see each module
equipped with one WS2801 chip and a connected RGB LED. Recognize the signal
labels for input (IN) and output (OUT): 5V, CK (clock), SD (serial data) and GND.
In contrast to the WS2801, the WS2811 and WS2812 driver chips don't have a
clock signal.


.. _led_strip_v2_bricklet_connectivity:

Connectivity
------------

The following image depicts the interfaces of the LED Strip Bricklet 2.0.

TODO: Update image?

.. image:: /Images/Bricklets/bricklet_led_strip_connection_350.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 Interface Description
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_connection_800.jpg

As described in the :ref:`Supported LEDs section <led_strip_v2_bricklet_ws28xy>` above,
the Bricklet supports LED strips and pixels with WS2801, WS2811, WS2812, 
SK6812 (NeoPixel RGB), SK6812RGBW (NeoPixel RGBW), LPD8806 and APA102 (DotStar) driver.
The terminal labeled with "Output" has to be connected with the input of
the first LED driver.

The output terminal consists of four signals:

* "DAT" is the data signal line to the LED driver chip. It has to be connected to
  the data input of the first driver chip. Unfortunately there is no
  general label on LED pixels or on LED strips for this input. Sometimes the 
  signal is marked with SD (Serial Data) or DI (Data Input). It is also 
  possible that the input of the pixel or strip is not marked, but the output 
  is marked (DO, Data Output). If the output is marked, the non 
  marked other side has to be the input.

* "CLK" is the clock signal line to the driver chip. It has to be connected 
  with the clock input of the first LED driver chip. This input is typically labeled
  with CLK, CK or CI (Clock Input). If only the output is labeled it can be 
  labeled with CO (Clock Output).

  The WS2811, WS2812 and SK6812 chips don't have a clock signal, leave the "CLK"
  terminal unconnected form them.

* "-" is the ground signal line. Ground is necessary to give a reference for the
  DAT and CLK signals.

* "+" is the supply voltage output. It is connected to the "+" signal of the
  "Input" terminal and should not be used to power LED Strips or pixels. 
  Leave it unconnected and power the connected strip or pixels directly from
  your supply.

The input terminal consisting of two signals:

* "+" voltage supply input. It can be connected to the power supply for the 
  LEDs to measure the supplied voltage. If you don't need this feature you
  can leave it unconnected.

* "-" is the ground input. It is internally connected with the "-" ground of 
  the "OUTPUT" terminal. 


.. _led_strip_v2_bricklet_ws2812b_led_strips:

LED Strips with Clock Signal (e.g. WS2812B)
-------------------------------------------

There is no general color code for LED strips. Especially sometimes the color 
codes are against any agreements. In this WS2812B LED strip example the red 
wire is :led-strip-red:`5V`, green is :led-strip-green:`data` the white wire is 
:led-strip-white:`ground`.

Connect data of the first strip to the LED Strip Bricklet 2.0 and
connect ground of your power supply to it. Pay attention to connect the data 
**input** of the first strip to the data **output** of the LED Strip Bricklet 2.0.

If you want to measure your supply voltage connect 5V to the Bricklet, too.
You can connect more LED strips to the first strip in series.

It is not sufficient to power the LED strips only at one point. We recommend to
feed power to the strip at least every two meters. This can be done
by connecting a cable between the strip and the power supply for each supply 
point. This will reduce the resistance and minimize the conduction losses.
See the following image as an example for it.

.. image:: /Images/Bricklets/bricklet_led_strip_ws2812b_wiring_600.png
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 wiring for WS2812B LED Strip
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_ws2812b_wiring_1500.png


.. _led_strip_v2_bricklet_ws2801_led_strips:

LED Strips without Clock signal (e.g. WS2801)
---------------------------------------------

There is no general color code for LED strips. Especially sometimes the color 
codes are against any agreements. In this WS2801 LED strip example the black 
wire is :led-strip-black:`5V`, green is :led-strip-green:`clock`, red is
:led-strip-red:`data` and the blue wire is :led-strip-blue:`ground`.

Connect clock and data of the first strip to the LED Strip Bricklet 2.0 and
connect ground of your power supply to it. Pay attention to connect the clock 
and data **input** of the first strip to the clock and data **output** of the
LED Strip Bricklet 2.0.

If you want to measure your supply voltage connect 5V to the Bricklet, too.
You can connect more LED strips to the first strip in series.

It is not sufficient to power the LED strips only at one point. We recommend to
feed power to the strip at least every two meters. This can be done
by connecting a cable between the strip and the power supply for each supply 
point. This will reduce the resistance and minimize the conduction losses.
See the following image as an example for it.

.. image:: /Images/Bricklets/bricklet_led_strip_strip_wiring_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 wiring for WS2801 LED Strip
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_wiring_1500.jpg


.. _led_strip_v2_bricklet_led_pixels:

LED Pixels
----------

The connection of LED pixels to the LED Strip Bricklet 2.0 is similar to the
connection of LED strips. There is no general color code for LED pixels. 
In the following example the red wire is :led-pixel-red:`5V`,
blue is :led-pixel-blue:`ground`, :led-pixel-green:`clock` (WS2801 only) is
green and :led-pixel-white:`data` is the white wire.

Connect clock (WS2801 only) and data of the first bunch of pixels to the
LED Strip Bricklet 2.0 and connect ground to it. Pay attention to connect
the clock (WS2801 only) and data **input** of the first pixel to the
clock (WS2801 only) and data **output** of the LED Strip Bricklet 2.0.
If you want to measure the voltage of your power supply connect 5V to the 
Bricklet, too. You can connect more bunches of LED pixel to the first bunch in 
series. 

Typically each bunch has power supply wires at the beginning and the end
of the bunch. Connect these over additional wires to the power supply. 
You can unite nearby wires. This will reduce the resistance and minimize the 
conduction losses.

.. image:: /Images/Bricklets/bricklet_led_strip_pixel_wiring_800.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 wiring for Pixel
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_pixel_wiring_1500.jpg


   
.. _led_strip_v2_bricklet_fixed_frame_rate:

Fixed Frame Rate
----------------

To achieve a smooth animation a fixed frame rate is desirable. A fixed frame
rate is easy to achieve with a properly configured frame duration and the 
``FrameStarted`` callback. The frame duration configures the amount of time
between each frame in ms. The ``FrameStarted`` callback is triggered when a new
frame transfer to the LEDs is started (the data is double-buffered).

For example, if you want to have an animation with 20 frames per second, you
should set the frame duration to 50ms. After the frame duration is set you
need to send the first frame (i.e. you need to set all RGB values), wait
until the ``FrameStarted`` callback is triggered, write the next frame and so on.

.. image:: /Images/Bricklets/bricklet_led_strip_v2_fixed_frame_rate.png
   :scale: 100 %
   :alt: Control LEDs with fixed frame rate
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_v2_fixed_frame_rate.png

If you receive a ``FrameStarted`` callback before all LEDs are set, your frame
rate is too high.


.. _led_strip_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the LED Strip Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-led-strip-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_led_strip_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for LED Strip Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_led_strip_v2_case_1000.jpg

	.. include:: LED_Strip_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/led_strip_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for LED Strip Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/led_strip_v2_exploded.png

	|bricklet_case_hint|


.. _led_strip_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: LED_Strip_V2_hlpi.table
