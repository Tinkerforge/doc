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

.. image:: /Images/Bricklets/distance_ir_brickv.jpg
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

The supported infrared sensors simply produce an output voltage
based on the measured distance. This voltage is measured by the ADC 
of the connected Brick. To compute the corresponding distance to this voltage
an voltage/distance mapping is needed. This mapping is stored on the 
Distance IR Bricklet. If you like to change the infrared distance sensor
you have to write this voltage/distance mapping if you want correct distances.


Store Voltage/Distance Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To write the voltage/distance mapping you have to connect the Bricklet
with an Brick to your PC. Start the :ref:`Brick Daemon <brickd>` and the 
:ref:`Brick Viewer <brickv>` 
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).

Press "connect" in the Brick Viewer and you should see the Distance IR tab.
Click on it. You should now see something like depicted below.

.. image:: /Images/Bricklets/distance_ir_brickv_sp.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet Brickv view to configure a sensor
   :align: center
   :target: ../../_images/Bricklets/distance_ir_brickv_sp.jpg

Press the "File.." Button (1) and choose an voltage/distance mapping file.
After this press "Save" Button (2) to write this data on to the Bricklet,
you will get an graphical representation of the written data.

After this press the reset button on the Brick or cycle power to
load the new stored voltage/distance mapping.



Voltage/Distance Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^

We provide the voltage/distance mappings for the following sensors:

.. csv-table::
   :header: "Type", "Range", "Mapping File"
   :widths: 15, 25, 10

	"GP2D120XJ00F", "4- 30cm (1.57" - 11.81")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2D120.txt>`__"
	"GP2Y0A21YK0F", "10- 80cm (3.94" - 31.50")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A21.txt>`__"
	"GP2Y0A02YK0F", "20-150cm (7.87" - 59.06")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A02.txt>`__"

Of course you can write your own voltage/distance mapping for a sensor we 
currently do not offer. Or you can modify an existing mapping file to achieve
a better quality of your sensor.

A voltage/distance mapping file consists of comments (lines beginning with '#')
and lines containing one "cm : analog value" tuple each. Look in the provided 
files above to get an idea.





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


