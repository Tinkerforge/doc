.. _joystick_bricklet:

Joystick
========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_joystick_tilted_350.jpg", 
	             "Bricklets/bricklet_joystick_tilted_600.jpg", 
	             "Joystick Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_joystick_front_100.jpg", 
	             "Bricklets/bricklet_joystick_front_600.jpg", 
	             "Joystick Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_joystick_horizontal_100.jpg", 
	             "Bricklets/bricklet_joystick_horizontal_600.jpg", 
	             "Joystick Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_joystick_knob_100.jpg", 
	             "Bricklets/bricklet_joystick_knob_600.jpg", 
	             "Joystick Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_joystick_master_100.jpg", 
	             "Bricklets/bricklet_joystick_master_600.jpg", 
	             "Joystick Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_joystick_brickv_100.jpg", 
	             "Bricklets/bricklet_joystick_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/joystick_bricklet_dimensions_100.png", 
	             "Dimensions/joystick_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Description
-----------

The Joystick :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by joystick
functionality.

The Joystick is two directional and equipped with a push button.
You can read out the position of the stick (X/Y coordinates) and
the state of the button. With configurable events it is possible to react on 
changing positions and an button presses without polling.

You can use this device to control robots, games etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        45mm x 25mm (1.77" x 0.98")
Weight                            11.8g (w/o knob), 14.7g (w/ knob)
Joystick                          Two-axis with push button
Output: Joystick position         X/Y axis position: -100/100, 0=center
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/joystick-bricklet/raw/master/hardware/joystick-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/joystick_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/joystick-bricklet/zipball/master>`__)



.. _joystick_bricklet_test:

Test your Joystick Bricklet
---------------------------

To test the Joystick Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Joystick Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable 
(see picture below).

.. image:: /Images/Bricklets/bricklet_joystick_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Joystick Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Joystick Bricklet" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricklets/bricklet_joystick_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Joystick Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_brickv.jpg

The tab consists of a coordinate system that shows the current position of 
the joystick and if the button is pressed.
Below this coordinate system you can find a graph that visualizes the
movements over time.
You should be able to  reproduce the depicted graph when you move the 
joystick first up, then down, then right and then end left.

If the Brick Viewer does not show Position (0,0) when the joystick is
in resting position, press the "Calibrate (0,0)" button.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <joystick_programming_interfaces>` section 
for the API of the Joystick Bricklet and examples in different programming 
languages.


.. _joystick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <joystick_bricklet_c_api>`", ":ref:`Examples <joystick_bricklet_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <joystick_bricklet_csharp_api>`", ":ref:`Examples <joystick_bricklet_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <joystick_bricklet_java_api>`", ":ref:`Examples <joystick_bricklet_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <joystick_bricklet_python_api>`", ":ref:`Examples <joystick_bricklet_python_examples>`", ":ref:`Installation <api_bindings_python>`"

