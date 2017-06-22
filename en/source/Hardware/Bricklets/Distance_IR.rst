
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Distance IR Bricklet
:shoplink: ../../../shop/bricklets/distance-ir-bricklet.html

.. include:: Distance_IR.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_ir_bricklet:

Distance IR Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_ir_tilted_[?|?].jpg       Distance IR Bricklet
	Bricklets/bricklet_distance_ir_front_[?|?].jpg        Distance IR Bricklet
	Bricklets/bricklet_distance_ir_back_[100|600].jpg     Distance IR Bricklet
	Bricklets/bricklet_distance_ir_master_[100|600].jpg   Distance IR Bricklet with Master Brick
	Bricklets/bricklet_distance_ir_sensors_[100|600].jpg  Distance IR Bricklet sensors
	Cases/bricklet_distance_ir_case_[100|600].jpg         Distance IR Bricklet in Case
	Bricklets/bricklet_distance_ir_brickv_[100|].jpg      Distance IR Bricklet in Brick Viewer
	Dimensions/dist_ir_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures distances up to 150cm with IR light
* Sensor can be changed
* Output in 1mm steps (12bit resolution)


.. _distance_ir_bricklet_description:

Description
-----------

The Distance IR :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure distances. `Sharp <http://www.sharpsma.com>`__ analog
infrared proximity sensors can be attached to the Bricklet.
After configuring the attached sensor you can read out the measured distance
in millimeters. With configurable events it is possible to react on changing
distances without polling.

Infrared sensors with different distance ranges are available in the shop:

* `Infrared Sensor 4-30cm GP2Y0A41SK0F
  <https://www.tinkerforge.com/en/shop/accessories/sensors/infrared-sensor-gp2y0a41sk0f.html>`__
* `Infrared Sensor 10-80cm GP2Y0A21YK0F
  <https://www.tinkerforge.com/en/shop/accessories/sensors/infrared-sensor-gp2y0a21yk0f.html>`__
* `Infrared Sensor 20-150cm GP2Y0A02YK0F
  <https://www.tinkerforge.com/en/shop/accessories/sensors/infrared-sensor-gp2y0a02yk0f.html>`__

Typically these types of sensors are used in robotics to measure distances
for mapping or localization purposes. But you can also use this sensors in
other applications, such as a finding out if a door is opened or closed.


Technical Specifications
------------------------

================================  ==================================================================
Property                          Value
================================  ==================================================================
Sensor                            GP2Y0A41SK0F or GP2Y0A21YK0F or GP2Y0A02YK0F
Current Consumption               See sensor datasheet
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Distance                          Depends on attached `Sharp <http://www.sharpsma.com>`__ IR Sensor:

                                  * GP2Y0A41SK0F:   4cm -  30cm (1.57" - 11.81")
                                  * GP2Y0A21YK0F:  10cm -  80cm (3.94" - 31.50")
                                  * GP2Y0A02YK0F:  20cm - 150cm (7.87" - 59.06")

                                  in 1mm steps, 12bit resolution
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Dimensions (W x D x H)            45 x 13 x 5mm (1.76 x 0.51 x 0.19")*, fits on backside of sensor
Weight                            2g*
================================  ==================================================================

\* without cable and sensor

Resources
---------

* GP2Y0A41SK0F datasheet (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A41SK0F.pdf>`__)
* GP2Y0A21YK0F datasheet (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A21YK0F.pdf>`__)
* GP2Y0A02YK0F datasheet (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A02YK0F.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/hardware/distir-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dist_ir_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/zipball/master>`__)


.. _distance_ir_bricklet_test:

Test your Distance IR Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_distance_ir_master_600.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet with infrared sensor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_master_1200.jpg

|test_tab|
If everything went as expected you can now see the measured distance
of the sensor, the output voltage of the IR distance sensor and a graph that
shows the distance over time. In the image below we slowly moved a hand away
from the sensor and to the sensor again.

.. image:: /Images/Bricklets/bricklet_distance_ir_brickv.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_brickv.jpg

|test_pi_ref|


.. _distance_ir_sensor_configuration:

Configure Infrared Sensor
-------------------------

The supported infrared sensors simply produce an output voltage
based on the measured distance. This voltage is measured by the ADC
of the connected Brick. To compute the corresponding distance to this voltage
a voltage/distance mapping is needed. This mapping specific to the selected
sensor type is stored on the Distance IR Bricklet. If you want to use an IR
distance sensor not directly supported by us, you have to calibrate this
voltage/distance mapping yourself.


Changing the Voltage/Distance Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To write the voltage/distance mapping you have to connect the Bricklet
with a Brick to your PC with has :ref:`Brick Daemon <brickd>` and the
:ref:`Brick Viewer <brickv>` installed and running.

Press "connect" in the Brick Viewer and you should see the Distance IR tab.
Click on it.

Select the "Distance IR Bricklet" tab, press the "Browse" button and choose a
voltage/distance mapping file. After this press the "Save" button to write the
data onto the Bricklet. The sampling points from the mapping file are
interpolated by a spline to get equidistant sampling points for the whole
measurement range of the sensor..

After this press the reset button on the Brick or power cycle to
load the newly stored voltage/distance mapping.


Available Voltage/Distance Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We provide the voltage/distance mappings for the following sensors:

.. csv-table::
   :header: "Type", "Range", "Mapping File"
   :widths: 15, 25, 10

   "GP2D120*",     "4cm - 30cm (1.57"" - 11.81"")",   "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2D120.txt>`__"
   "GP2Y0A41SK0F", "4cm - 30cm (1.57"" - 11.81"")",   "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A41.txt>`__"
   "GP2Y0A21YK0F", "10cm - 80cm (3.94"" - 31.50"")",  "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A21.txt>`__"
   "GP2Y0A02YK0F", "20cm - 150cm (7.87"" - 59.06"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A02.txt>`__"

\* is no longer sold, replaced by GP2Y0A41SK0F

You can write your own voltage/distance mapping for a sensor we
currently do not offer. Or you can modify an existing mapping file to achieve
a better quality of your sensor.

A voltage/distance mapping file consists of comments (lines beginning with ``#``)
and lines containing one ``<distance in cm>: <analog value in mV>`` tuple each.
Look in the provided files above to get an idea.

.. _distance_ir_bricklet_case:

Case
----

A `laser-cut case for the Distance IR Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-distance-ir-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_distance_ir_case_350.jpg
   :scale: 100 %
   :alt: Case for Distance IR Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_distance_ir_case_1000.jpg

.. include:: Distance_IR.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/distance_ir_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Distance IR Bricklet
   :align: center
   :target: ../../_images/Exploded/distance_ir_exploded.png

|bricklet_case_hint|


.. _distance_ir_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Distance_IR_hlpi.table


FAQ
---

The distances are wrong
^^^^^^^^^^^^^^^^^^^^^^^

This can have different causes. The Sharp IR sensors require 5V power supply. If the
connected Brick is powered over USB, 5V may not be reached. The reason for this
is a voltage drop about 0.5V caused by protection diodes on our products. You
can use a stack supply, e.g. the :ref:`Step-Down Power Supply
<step_down_power_supply>` to provide the sensor with 5V and get a better
distance reading.

Another cause can be a calibration problem. First of all you should
check if the calibration for the correct infrared sensor is installed
(see :ref:`here <distance_ir_sensor_configuration>`) and calibrate the ADC of your
Brick (see :ref:`here <brickv_adc_calibration>`).

If the distance measurements are still not precise enough, you have to write
a voltage/distance mapping that is specific for your device. The
voltage/distance mapping files provided by us are averaged over several
sensors.
