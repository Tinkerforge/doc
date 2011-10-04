.. _rotary_poti_bricklet:

Rotary Poti
===========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_tilted_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_tilted_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_tilted_800.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_front_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_front_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_front_800.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_vertical_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_vertical_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_vertical_800.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_horizontal_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_horizontal_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_horizontal_800.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_knob_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_knob_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_knob_800.jpg", 
	             "Rotary Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_master_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_master_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_master_1200.jpg", 
	             "Rotary Poti Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_rotary_poti_brickv_350.jpg", 
	             "Bricklets/bricklet_rotary_poti_brickv_100.jpg", 
	             "Bricklets/bricklet_rotary_poti_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/rotary_poti_bricklet_dimensions_350.png", 
	             "Dimensions/rotary_poti_bricklet_dimensions_100.png", 
	             "Dimensions/rotary_poti_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Description
-----------

This :ref:`Bricklet <product_overview_bricklets>` is equipped with a 1-turn rotary 
`potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`_. 
After connecting it to a :ref:`Brick <product_overview_bricks>` you
can readout the position of the potentiometer. Additionally you can configure 
different events triggered when the potentiometer reaches a specific position.

You can use this Bricklet for purposes like speed or volume control.


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
* Project (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


.. _rotary_poti_bricklet_test:

Test your Rotary Poti Bricklet
------------------------------

To test your Rotary Poti Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For an installation guide click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your Rotary Potentiometer Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricklets/bricklet_rotary_poti_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Rotary Poti Bricklet" in the Brick Viewer after you pressed "connect", 
select it.
If everything went as expected you the Brick Viewer should look like
depicted below.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg

Play around by turning the potentiometer.
You should be able to create a similar graph by turning the potentiometer full left
and then right.

After this you can go on with writing your own application.
See :ref:`Interface and Coding <rotary_poti_programming_interfaces>` section for the API of
the Rotary Poti Bricklet and examples in your programming language.


.. _rotary_poti_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <rotary_poti_bricklet_c_api>`", ":ref:`Examples <rotary_poti_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <rotary_poti_bricklet_csharp_api>`", ":ref:`Examples <rotary_poti_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <rotary_poti_bricklet_java_api>`", ":ref:`Examples <rotary_poti_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <rotary_poti_bricklet_python_api>`", ":ref:`Examples <rotary_poti_bricklet_python_examples>`", "Installation"


