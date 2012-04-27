.. _rotary_poti_bricklet:

Rotary Poti Bricklet
====================


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_rotary_poti_tilted_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_tilted_600.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_front_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_front_600.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_vertical_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_vertical_600.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_horizontal_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_horizontal_600.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_knob_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_knob_600.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_master_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_master_600.jpg", 
	             "Rotary Poti Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_brickv_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/rotary_poti_bricklet_dimensions_100.png", 
	             "Dimensions/rotary_poti_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Outputs position 
 * Configurable events
 * 300 degree rotation


Description
-----------

The Rotary Poti :ref:`Bricklet <product_overview_bricklets>` is equipped with 
a 1-turn rotary `potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`_. 
It can be connected to a 
:ref:`Brick <product_overview_bricks>`, with which the position of the 
slider can be read out. With configurable events it is possible to react on
changing positions without polling.

You can use this Bricklet for speed, volume control or similar purposes.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        30mm x 25mm (1.18" x 0.98")
Weight                            5.3g (w/o knob) 6.7g (w knob)
Rotary potentiometer              1-turn, 300 degree
Output: Potentiometer position    -150 to 150 (left to right)
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/raw/master/hardware/rotary-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rotary_poti_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/zipball/master>`__)



.. _rotary_poti_bricklet_test:

Test your Rotary Poti Bricklet
------------------------------

To test the Rotary Poti Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Rotary Potentiometer Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable 
(see picture below).

.. image:: /Images/Bricklets/bricklet_rotary_poti_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Rotary Poti Bricklet" in the Brick Viewer after you pressed "connect". 
Select it.
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg

Turn the potentiometer.
You should be able to create a similar graph by turning the potentiometer 
from left left to right and back to left.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <rotary_poti_programming_interfaces>` 
section for the API of the Rotary Poti Bricklet and examples in different 
programming languages.


.. _rotary_poti_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <rotary_poti_bricklet_c_api>`", ":ref:`Examples <rotary_poti_bricklet_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <rotary_poti_bricklet_csharp_api>`", ":ref:`Examples <rotary_poti_bricklet_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <rotary_poti_bricklet_java_api>`", ":ref:`Examples <rotary_poti_bricklet_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <rotary_poti_bricklet_python_api>`", ":ref:`Examples <rotary_poti_bricklet_python_examples>`", ":ref:`Installation <api_bindings_python>`"


