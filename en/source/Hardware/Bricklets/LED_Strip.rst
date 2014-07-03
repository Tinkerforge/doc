
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / LED Strip Bricklet
:shoplink: ../../../shop/bricklets/led-strip-bricklet.html


.. role:: led-strip-red

.. role:: led-strip-green

.. role:: led-strip-blue

.. role:: led-strip-black

.. role:: led-pixel-red

.. role:: led-pixel-green

.. role:: led-pixel-blue

.. role:: led-pixel-white


.. include:: LED_Strip.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _led_strip_bricklet:

LED Strip Bricklet
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_led_strip_tilted_350.jpg",
	               "Bricklets/bricklet_led_strip_tilted_600.jpg",
	               "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_vertical_100.jpg",
	             "Bricklets/bricklet_led_strip_vertical_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_horizontal_100.jpg",
	             "Bricklets/bricklet_led_strip_horizontal_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_tilted_back_100.jpg",
	             "Bricklets/bricklet_led_strip_tilted_back_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_led_strip_case_tilted_100.jpg",
	             "Cases/bricklet_led_strip_case_tilted_600.jpg",
	             "LED Strip Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_50_pixel_100.jpg",
	             "Bricklets/bricklet_led_strip_50_pixel_600.jpg",
	             "LED Strip Bricklet with 50 RGB LED Pixels")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_w_reel_100.jpg",
	             "Bricklets/bricklet_led_strip_w_reel_600.jpg",
	             "LED Strip Bricklet with RGB LED Strip")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_brickv_100.jpg",
	             "Bricklets/bricklet_led_strip_brickv.jpg",
	             "LED Strip Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/led_strip_bricklet_dimensions_100.png",
	             "Dimensions/led_strip_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Controls up to 320 RGB LEDs
* All LEDs can be switched independently
* Update rate of up to 100Hz for each LED possible

Description
-----------

The LED Strip :ref:`Bricklet <primer_bricklets>` can be used to
control LED strips and LED pixels that are equipped with the WS2801, WS2811 or
WS2812 LED driver.
It is possible to independently control 320 RGB LEDs (960 individual LEDs) over
the connected :ref:`Brick <primer_bricks>`.

The API allows to change all LEDs at the same time with a fixed update rate
of up to 100Hz. A possible application can be found in the 
:ref:`Starter Kit: Blinken Lights <starter_kit_blinkenlights>`: 
`Video <http://www.youtube.com/watch?v=mmNRa-lLaXM>`__

Brick Daemon 2.0.10 or newer is recommended for this Bricklet.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Supported LED Drivers             WS2801, WS2811 and WS2812
Current Consumption               1mA (idle), 4mA (active)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        8bit per LED
Maximum Number of LEDs            960 (320 RGB LEDs)*
Maximum Update Rate               100 updates per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 12mm (1.18 x 1.18 x 0.47")
Weight                            10g
================================  ============================================================

\* with a Master Brick, 480 with other Bricks

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/led-strip-bricklet/raw/master/hardware/led-strip-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/led_strip_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/led-strip-bricklet/zipball/master>`__)


.. _led_strip_bricklet_test:

Test your LED Strip Bricklet
----------------------------

|test_intro|

|test_connect|. After that connect a LED strip or bunch of pixels
to the Bricklet as described below.

|test_tab|
If everything went as expected you can now control a LED strip.

.. image:: /Images/Bricklets/bricklet_led_strip_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_brickv.jpg

|test_pi_ref|


.. _led_strip_bricklet_ws28xy:

WS2801, WS2811 und WS2812
-------------------------

The LED Strip Bricklet supports LED strips and pixels equipped with the
WS2801, WS2811 or WS2812 driver chip. WS28xy refers to any of these chips.

You have to configure which of this driver chips you want to use with the
Brick Viewer or the ``set_chip_type()`` function of the LED Strip Bricklet.
WS2811 and WS2812 requires LED Strip Bricklet plugin version 2.0.2 or newer.

The WS28xy chips can control three LEDs independently. Typically a RGB LED
combined in one package is used. It is controlled over a three or two wire
chained data bus with clock (WS2801 only), data signal and ground as voltage
reference (`daisy chain <http://en.wikipedia.org/wiki/Daisy_chain_(electrical_engineering)>`__).
Each WS28xy chip has a bus input connected to a controlling
device such as the LED Strip Bricklet or to a WS28xy predecessor and a
bus output which can be connected to a subsequent WS28xy chip.
Since it is a chained bus, a single bus output has to be connected only
to a single bus input. The bus is indexed beginning with the first WS28xy on the
LED Strip Bricklet (API index 0).

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


.. _led_strip_bricklet_connectivity:

Connectivity
------------

The following image depicts the interfaces of the LED Strip Bricklet.

.. image:: /Images/Bricklets/bricklet_led_strip_connection_350.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Interface Description
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_connection_800.jpg

As described in the :ref:`WS28xy section <led_strip_bricklet_ws28xy>` above,
the Bricklet supports LED strips and pixels with WS2801, WS2811 or WS2812 driver.
The terminal labeled with "Output" has to be connected with the input of
the first WS28xy driver.

The output terminal consists of four signals:

* "DAT" is the data signal line to the WS28xy chip. It has to be connected to
  the data input of the first WS28xy chip. Unfortunately there is no
  general label on LED pixels or on LED strips for this input. Sometimes the 
  signal is marked with SD (Serial Data) or DI (Data Input). It is also 
  possible that the input of the pixel or strip is not marked, but the output 
  is marked (DO, Data Output). If the output is marked, the non 
  marked other side has to be the input.

* "CLK" is the clock signal line to the WS2801 chip. It has to be connected 
  with the clock input of the first WS2801 chip. This input is typically labeled
  with CLK, CK or CI (Clock Input). If only the output is labeled it can be 
  labeled with CO (Clock Output).

  The WS2811 and WS2812 chips don't have a clock signal, leave the "CLK"
  terminal unconnected form them.

* "-" is the ground signal line. Ground is necessary to give a reference for the
  DAT and CLK signals.

* "+" is the supply voltage output. It is connected to the "+" signal of the
  "Input" terminal and should not be used to power LED Strips or pixels. 
  Leave it unconnected.

The input terminal consisting of two signals:

* "+" voltage supply input. It can be connected to the power supply for the 
  LEDs to measure the supplied voltage. If you don't need this feature you
  can leave it unconnected.

* "-" is the ground input. It is internally connected with the "-" ground of 
  the "OUTPUT" terminal. 


.. _led_strip_bricklet_ram_constraints:

RAM Constraints
---------------

The LED Strip Bricklet needs lots of RAM to store the color data for the LEDs.
Normally the LED Strip Bricklet would only be able to control up to 80 RGB
LEDs with the RAM that is available per Bricklet.

To circumvent this limitation, the LED Strip Bricklet is able to use the
RAM of the remaining unconnected Bricklets. This allows to control up to
320 RGB LEDs with one Master Brick and one LED Strip Bricklet. As described above
these used ports can't be used by other Bricklets.

The maximum number of controllable LEDs is as follows:

================================  ============================================================
Free Bricklet Ports               Maximum number of RGB LEDs
================================  ============================================================
0                                 80
1                                 160
2                                 240
3                                 320
================================  ============================================================


.. _led_strip_bricklet_led_strips:

LED Strips
----------

There is no general color code for LED strips. Especially sometimes the color 
codes are against any agreements. In this example the black wire is
:led-strip-black:`5V`, green is :led-strip-green:`clock` (WS2801 only), red is
:led-strip-red:`data` and the blue wire is :led-strip-blue:`ground`.

Connect clock (WS2801 only) and data of the first strip to the LED Strip Bricklet and
connect ground of your power supply to it. Pay attention to connect the clock 
and data **input** of the first strip to the clock and data **output** of the
LED Strip Bricklet.

If you want to measure your supply voltage connect 5V to the Bricklet, too.
You can connect more LED strips to the first strip in series (have the 
:ref:`RAM constraints <led_strip_bricklet_ram_constraints>` in mind).

It is not sufficient to power the LED strips only at one point. We recommend to
feed power to the strip at least every two meters. This can be done
by connecting a cable between the strip and the power supply for each supply 
point. This will reduce the resistance and minimize the conduction losses.
See the following image as an example for it.

.. image:: /Images/Bricklets/bricklet_led_strip_strip_wiring_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet wiring for LED Strip
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_wiring_1500.jpg


.. _led_strip_bricklet_led_pixels:

LED Pixels
----------

The connection of LED pixels to the LED Strip Bricklet is similar to the
connection of LED strips. There is no general color code for LED pixels. 
In the following example the red wire is :led-pixel-red:`5V`,
blue is :led-pixel-blue:`ground`, :led-pixel-green:`clock` (WS2801 only) is
green and :led-pixel-white:`data` is the white wire.

Connect clock (WS2801 only) and data of the first bunch of pixels to the
LED Strip Bricklet and connect ground to it. Pay attention to connect
the clock (WS2801 only) and data **input** of the first pixel to the
clock (WS2801 only) and data **output** of the LED Strip Bricklet.
If you want to measure the voltage of your power supply connect 5V to the 
Bricklet, too. You can connect more bunches of LED pixel to the first bunch in 
series (have the :ref:`RAM constraints <led_strip_bricklet_ram_constraints>` in 
mind). 

Typically each bunch has power supply wires at the beginning and the end
of the bunch. Connect these over additional wires to the power supply. 
You can unite nearby wires. This will reduce the resistance and minimize the 
conduction losses.

.. image:: /Images/Bricklets/bricklet_led_strip_pixel_wiring_800.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet wiring for Pixel
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_pixel_wiring_1500.jpg


   
.. _led_strip_bricklet_fixed_frame_rate:

Fixed Frame Rate
----------------

To achieve a smooth animation a fixed frame rate is desirable. A fixed frame
rate is easy to achieve with a properly configured frame duration and the 
``FrameRendered`` callback. The frame duration configures the amount of time
between each frame in ms. The ``FrameRendered`` callback is triggered after
a frame is transfered to the LEDs.

For example, if you want to have an animation with 20 frames per second, you
should set the frame duration to 50ms. After the frame duration is set you
need to send the first frame (i.e. you need to set all RGB values), wait
until the ``FrameRendered`` callback is triggered, write the next frame and so on.

.. image:: /Images/Bricklets/bricklet_led_strip_fixed_frame_rate_230.png
   :scale: 100 %
   :alt: Control LEDs with fixed frame rate
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_fixed_frame_rate.png

If you receive a ``FrameRendered`` callback before all LEDs are set, your frame
rate is too high.


.. _led_strip_bricklet_case:

Case
----

A `laser-cut case for the LED Strip Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-led-strip-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_led_strip_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for LED Strip Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_led_strip_case_tilted_1000.jpg

.. include:: LED_Strip.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/led_strip_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for LED Strip Bricklet
   :align: center
   :target: ../../_images/Exploded/led_strip_exploded.png

|bricklet_case_hint|


.. _led_strip_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: LED_Strip_hlpi.table
