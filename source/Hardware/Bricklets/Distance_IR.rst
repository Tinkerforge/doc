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

To test your Distance IR Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect an infrared distance sensor to the Bricklet and connect it
to an arbitrary :ref:`Brick <product_overview_bricks>`. 
You should have received a suitable cable with the Bricklet.


.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet with infrared distance sensor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg


If you then connect the Brick to the PC over USB,
you should see a tab named "Distance IR" in the Brick Viewer after you
pressed "connect". 
If everything went as expected you can now see the measured distance
of the sensor, the output voltage of the distance sensor
and a graph that shows the distance over time. 

Click on the Distance IR tab and see how the measured values change dependend 
on the distance in front of sensor. Move your hand in direction
of the sensor and see how the distance will decrease. When you move your 
hand away from the sensor the measured distance should increase.
A typical graph for this test is depicted in the image below.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg

You can now go on with writing your own application.
See :ref:`Interface and Coding <distir_programming_interfaces>` section for the API of
the Distance IR Bricklet and examples in your programming language.


.. _distir_conf_sensor:

Configure Infrared Sensor
-------------------------

TBD



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


Troubleshoot
------------

The measured distance is wrong
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**You have configured the wrong infrared sensor**

* Configure the correct infrared sensor, see section :ref:`Configure Infrared Sensor <distir_conf_sensor>`.

**The ADC of your Brick is uncalibrated:**

* Configure the ADC of your Brick, see :ref:`Brickv documentation <brickv_adc_calibration>`.


