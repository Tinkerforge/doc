
:shoplink: ../../../shop/bricklets/io4-bricklet.html

.. include:: IO4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _io4_bricklet:

IO-4 Bricklet
=============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_io4_11_tilted_[?|?].jpg        IO-4 Bricklet
	Bricklets/bricklet_io4_11_vertical_[?|?].jpg      IO-4 Bricklet
	Bricklets/bricklet_io4_11_horizontal_[?|?].jpg    IO-4 Bricklet
	Bricklets/bricklet_io4_11_master_[100|600].jpg    IO-4 Bricklet with Master Brick
	Cases/bricklet_io4_case_[100|600].jpg             IO-4 Bricklet in Case
	Bricklets/bricklet_io4_brickv_[100|].jpg          IO-4 Bricklet in Brick Viewer
	Dimensions/io4_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4-channel digital input/output
* Fixed 3.3V logic voltage
* Configurable pull-ups and interrupts


.. _io4_bricklet_description:

Description
-----------

The IO-4 :ref:`Bricklet <primer_bricklets>` can be used to extend the
features of :ref:`Bricks <primer_bricks>` by external digital inputs
and outputs.

The Bricklet features 4 I/O pins that can be independently configured as
digital inputs or outputs. Each input pin can additionally be configured with
a pull-up or as interrupt source. Via terminal blocks all signals can be accessed.
Two additional terminal blocks deliver 3.3V and GND.

Human interfaces, such as switches, push-buttons and LEDs are typical
applications of this Bricklet.

Hardware version 1.1 adds GND pins nearby the 4 I/O pins to allow easier
access between I/O pins and GND.


Technical Specifications
------------------------

================================  =================================================================
Property                          Value
================================  =================================================================
I/O Pins                          4
Current Consumption               1mA
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
I/O Voltages                      Fixed 3.3V
Maximum Output Current            6mA (per output pin), 100mA (3.3V fixed output pin)
Maximum API Calls*                ``set-value`` (1kHz), ``get-value`` (0.5kHz), callbacks (1kHz)
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
Dimensions (W x D x H)            35 x 35 x 14mm (1.38 x 1.38 x 0.55")
Weight                            14g
================================  =================================================================

\* depends on your system (OS, CPU etc.)


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/io4-bricklet/raw/master/hardware/io4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/io4_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/io4-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2C1Ljoh>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/io4/io4.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/io4/io4.FCStd>`__)


.. _io4_bricklet_test:

Test your IO-4 Bricklet
-----------------------

|test_intro|

|test_connect|.
In our test we connected an LED with series resistor to the board
by attaching the anode to pin 3 and the cathode to a GND pin.
Additionally we connected a slide switch that can short pin 0 to GND
(see picture below).

Starting from hardware version 1.1 you can also use the GND pins directly
beside the I/O pins.

.. image:: /Images/Bricklets/bricklet_io4_master_600.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_master_1200.jpg

|test_tab|

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_io4_brickv.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_brickv.jpg

..
  FIXME: update screenshot and description for monoflop

In this tab you can change the "Debounce Period",
it is the debounce time for interrupt callbacks.
For example: If you set this value to 100, you will get interrupts
maximal every 100ms. This is necessary if something that bounces is
connected to the IO-4 Bricklet, such as a button. You can test the optimal
value in the Brick Viewer and use it later in your own program.

Below the debounce period configuration you can configure the pins.
Each pin can be configured as input/output and in case of an input pin
as pull-up. The current state is depicted in the table below.

To test the LED we configure pin 3 as output and change the value.
When the pin is high the LED should light up. To test the button
configure pin 0 as input pull-up. We need the pull-up to define a stable
state when the slide switch does not short pin 0 to GND. Now look in the
table, you should see that you can change the value of the pin by toggling
the slide switch.

If you don't have a button or a LED you can try to measure voltages with
a voltage meter or connect an input pin with GND or VCC to see changes in the
Brick Viewer.

|test_pi_ref|

.. _io4_bricklet_case:

Case
----

A `laser-cut case for the IO-4 Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-io-4-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_io4_case_350.jpg
   :scale: 100 %
   :alt: Case for IO-4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_io4_case_1000.jpg

.. include:: IO4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/io4_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for IO-4 Bricklet
   :align: center
   :target: ../../_images/Exploded/io4_exploded.png

|bricklet_case_hint|


.. _io4_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: IO4_hlpi.table
