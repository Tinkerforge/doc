.. _rotary_poti_bricklet:

Rotary Poti
===========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #2") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #3") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #4") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #5") }}
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
Weight
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

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

After installing our software (Brickd, Brickv) you can see the connected Ambient
Light Bricklet in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Ambient Light tab and see how the measured values change dependend 
on device illumination. You can now go on with writing your own application.
See :ref:`Interface and Coding <ambl_programming_interfaces>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


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


