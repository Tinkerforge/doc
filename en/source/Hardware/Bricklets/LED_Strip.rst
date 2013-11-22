
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / LED Strip Bricklet
:FIXME_shoplink: ../../../shop/bricklets/led-strip-bricklet.html


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

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_led_strip_tilted_350.jpg",
	               "Bricklets/bricklet_led_strip_tilted_600.jpg",
	               "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_tilted_back_100.jpg",
	             "Bricklets/bricklet_led_strip_tilted_back_600.jpg",
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
	    tfdocimg("Bricklets/bricklet_led_strip_master_100.jpg",
	             "Bricklets/bricklet_led_strip_master_600.jpg",
	             "LED Strip Bricklet with Master Brick")
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

The LED Strip :ref:`Bricklet <product_overview_bricklets>` can be used to
control LED strips that are equipped with the WS2801 LED driver. It is possible
to independently control 320 RGB LEDs (960 individual LEDs).

The API allows to change all LEDs at the same time with a fixed update rate
of up to 100Hz.

TODO: Video

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Supported LED Driver              WS2801
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

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_led_strip_master_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_master_1200.jpg

|test_tab|
If everything went as expected you can now control a LED strip.

.. image:: /Images/Bricklets/bricklet_led_strip_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_brickv.jpg

|test_pi_ref|


.. _led_strip_bricklet_ws2801:

WS2801
------

At the moment the LED Strip Bricklets supports LED strips and pixels 
equipped with the WS2801 driver chip (more driver chip types will follow).

The WS2801 chip can control three LEDs independently.
Typically a RGB LED combined in one package is used. It is controlled over
a three wire chained data bus with clock, data signal and ground for 
reference (`daisy chain <http://en.wikipedia.org/wiki/Daisy_chain_(electrical_engineering)>`__).
Each WS2801 chip has a bus input connected to a controlling 
device such as the LED Strip Bricklet or to a WS2801 predecessor and a 
bus output which can be connected to a subsequent WS2801 chip.
Since it is a chained bus, a single bus output has to be connected only
to a single bus input. The bus is indexed beginning with the first WS2801 on the 
LED Strip Bricklet (API index 0).

.. image:: /Images/Bricklets/bricklet_led_strip_strip_example_600.jpg
   :scale: 100 %
   :alt: LED Strip with WS2801
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_example_800.jpg

The above picture depicts a typical WS2801 LED strip. You can see each module
equipped with one WS2801 chip and a connected RGB LED. Recognize the signal labels
for input (IN) and output (OUT): 5V, CK (clock), SD (serial data) and GND.


.. _led_strip_bricklet_connectivity:

Connectivity
------------

The following image depicts the interfaces of the LED Strip Bricklet.

.. image:: /Images/Bricklets/bricklet_led_strip_connection_350.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Interface Description
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_connection_800.jpg

As described in the :ref:`WS2801 section <led_strip_bricklet_ws2801>` above
the Bricklet supports LED strips and pixels with WS2801 driver.
The terminal labeled with "Output" has to be connected with the input of
the first WS2801 driver.

The output terminal consists of four signals:

* "DAT" is the data signal line to the WS2801 chip. It has to be connected to
  the data input of the first WS2801 chip. Unfortunately there is no
  general label on LED pixels or on LED strips for this input. Sometimes the 
  signal is marked with SD (Serial Data) or DI (Data Input). It is also 
  possible that the input of the pixel or strip is not marked, but the output 
  is marked (DO, Data Output). If the output is marked, the non 
  marked other side has to be the input.

* "CLK" is the clock signal line to the WS2801 chip. It has to be connected 
  with the clock input of the first WS2801 chip. This input is typically labeled
  with CLK, CK or CI (Clock Input). If only the output is labeled it can be 
  labeled with CO (Clock Output).

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
320 RGB LEDs with one Master Brick and one LED Strip Bricklet.

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
codes are against any agreements. In this example the :led-strip-black:`black`
wire is 5V, :led-strip-green:`green` is clock, :led-strip-red:`red` is data and
the :led-strip-blue:`blue` wire is ground.

Connect clock and data of the first strip to the LED Strip Bricklet and 
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
In the following example the :led-pixel-red:`red` wire is 5V,
:led-pixel-blue:`blue` is ground, :led-pixel-green:`clock` is green and
:led-pixel-white:`data` is the white wire.

Connect clock and data of the first bunch of pixels to the LED Strip Bricklet 
and connect ground to it. Pay attention to connect the clock and data **input**
of the first pixel to the clock and data **output** of the LED Strip Bricklet.
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
FrameRendered callback. The frame duration configures the amount of time
between each frame in ms. The FrameRendered callback is triggered after
a frame is transfered to the LEDs.

For example, if you want to have an animation with 20 frames per second, you
should set the frame duration to 50ms. After the frame duration is set you
need to send the first frame (i.e. you need to set all RGB values), wait
until the FrameRendered callback is triggered, write the next frame and so on.

.. image:: /Images/Bricklets/bricklet_led_strip_fixed_frame_rate_230.png
   :scale: 100 %
   :alt: Control LEDs with fixed frame rate
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_fixed_frame_rate.png

If you receive a FrameRendered callback before all LEDs are set, your frame
rate is too high.


.. _led_strip_bricklet_case:

Case
----

A `laser-cut case for the LED Strip Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-led-strip-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_led_strip_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for LED Strip Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_led_strip_case_built_up_1000.jpg

.. include:: LED_Strip.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/led_strip_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for LED Strip Bricklet
   :align: center
   :target: ../../_images/Exploded/led_strip_exploded.png

|bricklet_case_hint|


.. _led_strip_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: LED_Strip_hlpi.table
