
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / LED Strip Bricklet
:FIXME_shoplink: ../../../shop/bricklets/led-strip-bricklet.html

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

The LED Strip Bricklet can be used to control LED strips that are equipped
with the WS2801 LED driver. It is possible to independently control 320 RGB LEDs
(960 different LEDs). 

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
Number of Controllable LEDs       Max 960 (320 RGB LEDs)
Update Rate                       Max 100 updates per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 12mm (1.18 x 1.18 x 0.47")
Weight                            10g
================================  ============================================================


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



.. _led_strip_ws2801:

WS2801
------

At the moment the LED Strip Bricklets only supports LED strips and pixels 
equipped with WS2801 controllers. 

Technical speaking the WS2811 IC can control three LEDs independently, 
typically used for R,G,B LEDs combined in one package. It is controlled over
a three wire chained data bus with clock and data signal (and ground for 
reference). Each WS2811 chip has a bus input 
,connected to a controlling device like the LED Strip Bricklet or to a WS2801 
predecessor, and a bus output which can be connected to a subsequent 
WS2801. Since it is a chained bus, a signle bus output has to be connected only 
to a single bus input. The bus is indexed beginning with the first WS2811 on the 
LED Strip Bricklet (API index 0).

TODO Image: LED Strip Bricklet + LED Strip with marked signals and WS2811

.. _led_strip_connectivity:

Connectivity
------------

The following picture depicts the interfaces of the LED Strip Bricklet.

.. FIXME image:: /Images/Bricklets/bricklet_led_strip_connection_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Interface Description
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_connection_800.jpg

As described in the :ref:`WS2811 section <led_strip_ws2811>` above
the Bricklet supports pixels and stripes with WS2811 controller.
The terminal labeled with "Output" has to be connected with the input of
the first WS2811 controller.

The output terminal consisting of four signals:

 * "DAT" is the data signal line to the WS2801 chip. It has to be connected with
   the data input of the first WS2801. Unfortunately there is no 
   general label on LED pixels or on LED strips for this input. Sometimes the 
   signal is marked with SD (Serial Data) or DI (Data Input). It is also 
   possible that the input of the pixel or strip is not marked, but the output 
   is marked (DO, Data Output). Therefore, if the output is marked, the non 
   marked other side has to be the input.

 * "CLK" is the clock signal line to the WS2801 chip. It has to be connected 
   with the clock input of the first WS2801. This input is typically labeled 
   with CLK, CK or CI (Clock Input). If only the output is labeled it can be 
   labeled with CO (Clock Output).

 * "-" is the ground signal line. Ground is necessary to give a reference for the
   DAT and CLK signals. So it has to be connected.

 * "+" is the supply voltage output. It is connected to the "+" signal of the
   "Input" terminal and should not be used to power LED Strips or pixels. So 
   leave it unconnected.
  

The input terminal consisting of two signals:

 * "+" voltage supply input. It can be connected to the power supply for the 
   LEDs to measure the supplied voltage. If you don't need this feature you
   can leave it unconnected.

 * "-" is the ground input. It is internally connected with the "-" ground of 
   the "OUTPUT" terminal. 
   
.. _led_strip_led_strips:

LED Strips
----------

TODO:

* How to use them?
* Where to inject power?

.. _led_strip_led_pixels:

LED Pixels
----------

TODO:

* How to use them?
* Where to inject power?


.. _led_strip_fixed_frame_rate:

Fixed Frame Rate
----------------

To achieve a smooth animation a fixed frame rate is desirable. A fixed frame
rate is easy to achieve with a properly configured frame duration and the 
FrameRendered callback. The frame duration configures the amount of time
between each frame in ms. The FrameRendered callback is triggered after
a frame is transfered to the LEDs.

For example, if you want to have an animation with 20 frames per second, you
should set the frame duration to 50ms. After the frame duration is set you
need to send the first frame (i.e. you need to set all rgb values), wait 
until the FrameRendered callback is triggered, write the next frame and so on.

.. image:: /Images/Bricklets/bricklet_led_strip_fixed_frame_rate.png
   :scale: 100 %
   :alt: Control LEDs with fixed frame rate
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_fixed_frame_rate.png

If you receive a FrameRendered callback before all LEDs are set, your frame
rate is too high.

.. _led_strip_bricklet_case:

Case
----

A `laser-cut case for the LED Strip Bricklet <https://www.tinkerforge.com/en/shop/cases/case-led-strip-bricklet.html>`__ is available.

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
