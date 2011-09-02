.. _joystick_bricklet:

Joystick
========


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

This :ref:`Bricklet <product_overview_bricklets>` can be connected to every 
:ref:`Brick <product_overview_bricks>` and can be used as input device. 
It is two directional moveable and equipped with a push button.
You can readout the position of the stick (X/Y coordinates) and
the state of the button. Additionally you can configure events triggered
when the stick is at a particular position or the button is pushed.

You can use this device to control robots, games etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        45mm x 25mm (1.77" x 0.98")
Weight
Joystick                          Two-axis with push button
Output: Joystick position         x/y axis position: -100/100, 0=center
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/joystick-bricklet/raw/master/hardware/joystick-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/joystick_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/joystick-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


.. _joystick_bricklet_test:

Test your Joystick Bricklet
---------------------------

* hold bricklet connector away from you
* up, down, right, left

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


.. _joystick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <joystick_bricklet_c_api>`", ":ref:`Examples <joystick_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <joystick_bricklet_csharp_api>`", ":ref:`Examples <joystick_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <joystick_bricklet_java_api>`", ":ref:`Examples <joystick_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <joystick_bricklet_python_api>`", ":ref:`Examples <joystick_bricklet_python_examples>`", "Installation"

