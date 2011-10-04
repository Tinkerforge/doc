.. _linear_poti_bricklet:

Linear Poti
===========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_tilted_350.jpg", 
	             "Bricklets/bricklet_linear_poti_tilted_100.jpg", 
	             "Bricklets/bricklet_linear_poti_tilted_800.jpg", 
	             "Linear Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_front_350.jpg", 
	             "Bricklets/bricklet_linear_poti_front_100.jpg", 
	             "Bricklets/bricklet_linear_poti_front_800.jpg", 
	             "Linear Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_vertical_350.jpg", 
	             "Bricklets/bricklet_linear_poti_vertical_100.jpg", 
	             "Bricklets/bricklet_linear_poti_vertical_800.jpg", 
	             "Linear Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_horizontal_350.jpg", 
	             "Bricklets/bricklet_linear_poti_horizontal_100.jpg", 
	             "Bricklets/bricklet_linear_poti_horizontal_800.jpg", 
	             "Linear Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_knob_350.jpg", 
	             "Bricklets/bricklet_linear_poti_knob_100.jpg", 
	             "Bricklets/bricklet_linear_poti_knob_800.jpg", 
	             "Linear Poti Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_master_350.jpg", 
	             "Bricklets/bricklet_linear_poti_master_100.jpg", 
	             "Bricklets/bricklet_linear_poti_master_1200.jpg", 
	             "Linear Poti Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_linear_poti_brickv_350.jpg", 
	             "Bricklets/bricklet_linear_poti_brickv_100.jpg", 
	             "Bricklets/bricklet_linear_poti_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/linear_poti_bricklet_dimensions_350.png", 
	             "Dimensions/linear_poti_bricklet_dimensions_100.png", 
	             "Dimensions/linear_poti_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Description
-----------

This :ref:`Bricklet <product_overview_bricklets>` is equipped with a linear 
`potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`_
("fader", "slider"). After connecting it to a :ref:`Brick <product_overview_bricks>` you
can readout the position of the slider. Additionally you can configure different
events triggered when the slider reaches a specific position.

You can use this Bricklet for purposes like speed or volume control.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        85mm x 25mm (3.35" x 0.98")
Weight                            14.1g (w/o knob) 15.2g (w knob)
Linear potentiometer              59mm (2.32") adjustable length
Output: Slider position           0 - 100 (slider down - slider up)
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/raw/master/hardware/linear-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/linear_poti_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _linear_poti_bricklet_test:

Test your Linear Poti Bricklet
------------------------------

To test your Linear Poti Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For an installation guide click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your Linear Poti Brickler to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable 
(see picture below).

.. image:: /Images/Bricklets/bricklet_linear_poti_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Linear Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_linear_poti_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Linear Poti Bricklet" in the Brick Viewer after you pressed "connect", 
select it.
If everything went as expected you the Brick Viewer should look like
depicted below.

.. image:: /Images/Bricklets/bricklet_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Linear Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_current12_brickv.jpg

Move the potentiometer.
You should be able to create a graph like that one depicted in the image above 
by moving the potentiometer from lower to top.

After this you can go on with writing your own application.
See :ref:`Interface and Coding <linear_poti_programming_interfaces>` section 
for the API of the Linear Poti Bricklet and examples in your programming 
language.


.. _linear_poti_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <linear_poti_bricklet_c_api>`", ":ref:`Examples <linear_poti_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <linear_poti_bricklet_csharp_api>`", ":ref:`Examples <linear_poti_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <linear_poti_bricklet_java_api>`", ":ref:`Examples <linear_poti_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <linear_poti_bricklet_python_api>`", ":ref:`Examples <linear_poti_bricklet_python_examples>`", "Installation"

