.. _distance_ir_bricklet:

Distance IR Bricklet
====================


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_distance_ir_tilted_350.jpg", 
	             "Bricklets/bricklet_distance_ir_tilted_600.jpg", 
	             "Distance IR Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_distance_ir_front_100.jpg", 
	             "Bricklets/bricklet_distance_ir_front_600.jpg", 
	             "Distance IR Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_distance_ir_back_100.jpg", 
	             "Bricklets/bricklet_distance_ir_back_600.jpg", 
	             "Distance IR Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_distance_ir_master_100.jpg", 
	             "Bricklets/bricklet_distance_ir_master_600.jpg", 
	             "Distance IR Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_distance_ir_sensors_100.jpg", 
	             "Bricklets/bricklet_distance_ir_sensors_600.jpg", 
	             "Distance IR Bricklet sensors") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_distance_ir_brickv_100.jpg", 
	             "Bricklets/bricklet_distance_ir_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/dist_ir_bricklet_dimensions_100.png", 
	             "Dimensions/dist_ir_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Measures distances up to 150cm
 * Sensor can be changed
 * Outputs distance in mm
 * 12bit resolution


Description
-----------

The Distance IR :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by the
capability to measure distances. `Sharp <http://www.sharpsma.com>`_ analog
infrared proximity sensors can be attached to the Bricklet. 
After configuring the attached sensor you can read out the measured distance 
in millimeters. With configurable events it is possible to react on changing
distances without polling.

Typically these types of sensors are used in robotics to measure distances 
for mapping or localization purposes. But you can also use this sensors in 
other applications, such as a finding out if a door is opened or closed.

Technical Specifications
------------------------

================================  ==================================================================
Property                          Value
================================  ==================================================================
Dimensions                        13mm x 44.6mm (0.51" x 1.76") fits on backside of sensor
Weight                            2.0g (w/o cable and sensor)
Current Consumption               See IR Sensor Datasheet
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Sensor Range                      Depends on attached `Sharp <http://www.sharpsma.com>`_ IR Sensor:

                                  * GP2Y0A41SK0F:   4- 30cm (1.57" - 11.81")
                                  * GP2Y0A21YK0F:  10- 80cm (3.94" - 31.50")
                                  * GP2Y0A02YK0F:  20-150cm (7.87" - 59.06")

Output: Distance                  Unit mm, resolution 12bit.  
================================  ==================================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/hardware/distir-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dist_ir_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/zipball/master>`__)


.. _distance_ir_bricklet_test:

Test your Distance IR Bricklet
------------------------------

To test the Distance IR Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect an infrared distance sensor to the Bricklet and connect it
to a :ref:`Brick <product_overview_bricks>`. 
You should have received a suitable cable with the Bricklet.


.. image:: /Images/Bricklets/bricklet_distance_ir_master_600.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet with infrared distance sensor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_master_1200.jpg


If you then connect the Brick to the PC over USB,
you should see a tab named "Distance IR Bricklet" in the Brick Viewer after you
pressed "connect". Select it. 
If everything went as expected you can now see the measured distance
of the sensor, the output voltage of the IR distance sensor
and a graph that shows the distance over time. 

Click on the Distance IR tab and see if the measured values change
corresponding to the real distance. In the image below we slowly moved a hand
away from the sensor and to the sensor again.

.. image:: /Images/Bricklets/bricklet_distance_ir_brickv.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_brickv.jpg

You can now go on with writing your own application.
See the :ref:`Programming Interface <distir_programming_interfaces>` section 
for the API of the Distance IR Bricklet and examples in different programming 
languages.


.. _distir_conf_sensor:

Configure Infrared Sensor
-------------------------

The supported infrared sensors simply produce an output voltage
based on the measured distance. This voltage is measured by the ADC 
of the connected Brick. To compute the corresponding distance to this voltage
a voltage/distance mapping is needed. This mapping is stored on the 
Distance IR Bricklet. If you want to use an IR distance sensor not directly
supported by us, you have to calibrate this voltage/distance mapping 
yourself.


Store Voltage/Distance Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To write the voltage/distance mapping you have to connect the Bricklet
with a Brick to your PC. Start the :ref:`Brick Daemon <brickd>` and the 
:ref:`Brick Viewer <brickv>`.

Press "connect" in the Brick Viewer and you should see the Distance IR tab.
Click on it.

Press the "File.." Button and choose an voltage/distance mapping file.
After this press the "Save" Button to write the data onto the Bricklet,
you will get an graphical representation spline interpolation
that is written.

After this press the reset button on the Brick or power cycle to
load the newly stored voltage/distance mapping.



Voltage/Distance Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^

We provide the voltage/distance mappings for the following sensors:

.. csv-table::
   :header: "Type", "Range", "Mapping File"
   :widths: 15, 25, 10

	"GP2Y0A41SK0F and GP2D120XJ00F", "4- 30cm (1.57" - 11.81")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2D120.txt>`__"
	"GP2Y0A21YK0F", "10- 80cm (3.94" - 31.50")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A21.txt>`__"
	"GP2Y0A02YK0F", "20-150cm (7.87" - 59.06")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A02.txt>`__"

You can write your own voltage/distance mapping for a sensor we 
currently do not offer. Or you can modify an existing mapping file to achieve
a better quality of your sensor.

A voltage/distance mapping file consists of comments (lines beginning with '#')
and lines containing one "cm: analog value" tuple each. Look in the provided 
files above to get an idea.

.. _distir_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Distance_IR_hlpi.table

FAQ
---

The distances are wrong
^^^^^^^^^^^^^^^^^^^^^^^

This is likely some kind of calibration problem. First of all you should
check if the calibration for the correct infrared sensor is installed
(see :ref:`here <distir_conf_sensor>`) and calibrate the ADC of your
Brick (see :ref:`here <brickv_adc_calibration>`).

If the distance measurements are still not precise enough, you have to write
a voltage/distance mapping that is specific for your device. The
voltage/distance mapping files provided by us are averaged over several
sensors.
