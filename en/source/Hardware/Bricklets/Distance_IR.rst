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
	             "Distance IR Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dist_ir_bricklet_dimensions_100.png",
	             "Dimensions/dist_ir_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures distances up to 150cm with IR light
* Sensor can be changed
* Output in 1mm steps (12bit resolution)


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
Sensor                            GP2Y0A41 or GP2Y0A21 or GP2Y0A02
Current Consumption               See sensor datasheet
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Distance                          Depends on attached `Sharp <http://www.sharpsma.com>`_ IR Sensor:

                                  * GP2Y0A41:   4cm -  30cm (1.57" - 11.81")
                                  * GP2Y0A21:  10cm -  80cm (3.94" - 31.50")
                                  * GP2Y0A02:  20cm - 150cm (7.87" - 59.06")

                                  in 1mm steps, 12bit resolution
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Dimensions (W x D x H)            45 x 13 x 5mm (1.76 x 0.51 x 0.19")*, fits on backside of sensor
Weight                            2g*
================================  ==================================================================

\* without cable and sensor

Resources
---------

* GP2Y0A41 datasheet (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A41.pdf>`__)
* GP2Y0A21 datasheet (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A21.pdf>`__)
* GP2Y0A02 datasheet (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A02.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/hardware/distir-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dist_ir_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/zipball/master>`__)


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
   :alt: Distance IR Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_brickv.jpg

You can now go on with writing your own application.
See the :ref:`Programming Interface <distance_ir_programming_interfaces>` section
for the API of the Distance IR Bricklet and examples in different programming
languages.


.. _distance_ir_sensor_configuration:

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

   "GP2Y0A41 and GP2D120", "4cm - 30cm (1.57"" - 11.81"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2D120.txt>`__"
   "GP2Y0A21", "10cm - 80cm (3.94"" - 31.50"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A21.txt>`__"
   "GP2Y0A02", "20cm - 150cm (7.87"" - 59.06"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A02.txt>`__"

You can write your own voltage/distance mapping for a sensor we
currently do not offer. Or you can modify an existing mapping file to achieve
a better quality of your sensor.

A voltage/distance mapping file consists of comments (lines beginning with '#')
and lines containing one "cm: analog value" tuple each. Look in the provided
files above to get an idea.


.. _distance_ir_programming_interfaces:

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
(see :ref:`here <distance_ir_sensor_configuration>`) and calibrate the ADC of your
Brick (see :ref:`here <brickv_adc_calibration>`).

If the distance measurements are still not precise enough, you have to write
a voltage/distance mapping that is specific for your device. The
voltage/distance mapping files provided by us are averaged over several
sensors.
