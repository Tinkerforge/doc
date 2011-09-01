.. _distance_ir_bricklet:

Distance IR
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

The Distance IR :ref:`Bricklet <product_overview_bricklets>` can extend the features of
every :ref:`Brick <product_overview_bricks>` by the possibility to
measure distances. The Bricklet can be attached to `Sharp <http://www.sharpsma.com>`_ 
analog infrared proximity sensors. 
After configuring the attached sensor you can read out the measured distance 
directly in millimeters. You can configure events triggered when a specified distance
is exceeded, this supersede polling.

Typically these sensors are used in robotics to measure distances for mapping or 
localization purposes. But you can also use these sensors in other applications.
For example you may like to switch something when someone enters a room. 
You can install the sensor in the entrance in that way that if someone enters the room 
the measured distance will be smaller.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        13mm x 44.6mm (0.51" x 1.76") fitting on backside of sensor
Weight
Current Consumption
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor Range                      Depends on attached Sharp IR Sensor:

                                  * GP2D120XJ00F:   4- 30cm (1.57" - 11.81")
                                  * GP2Y0A21YK0F:  10- 80cm (3.94" - 31.50")
                                  * GP2Y0A02YK0F:  20-150cm (7.87" - 59.06")

                                  and others...
Output: Distance                  Distance range depends on sensor, unit mm, resolution 12bit.                     
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/hardware/distir-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dist_ir_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _distance_ir_bricklet_test:

Test your Distance IR Bricklet
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


.. _distir_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <distance_ir_bricklet_c_api>`", ":ref:`Examples <distance_ir_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <distance_ir_bricklet_csharp_api>`", ":ref:`Examples <distance_ir_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <distance_ir_bricklet_java_api>`", ":ref:`Examples <distance_ir_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <distance_ir_bricklet_python_api>`", ":ref:`Examples <distance_ir_bricklet_python_examples>`", "Installation"

