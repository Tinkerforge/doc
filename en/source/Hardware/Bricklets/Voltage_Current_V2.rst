
:shoplink: ../../../shop/bricklets/voltage-current-v2-bricklet.html

.. include:: Voltage_Current_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _voltage_current_v2_bricklet:

Voltage/Current Bricklet 2.0
============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_voltage_current_v2_tilted_[?|?].jpg           Voltage/Current Bricklet 2.0
	Bricklets/bricklet_voltage_current_v2_tilted2_[?|?].jpg          Voltage/Current Bricklet 2.0
	Bricklets/bricklet_voltage_current_v2_top_[?|?].jpg              Voltage/Current Bricklet 2.0
	Bricklets/bricklet_voltage_current_v2_brickv_[100|].jpg          Voltage/Current Bricklet 2.0 in Brick Viewer
	Dimensions/voltage_current_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measure power, voltage and current up to 720W/36V/20A
* 1mW, 1mV, 1mA resolution over the whole range
* Bidirectional current measurement (e.g. charge/discharge)
* Configurable averaging and ADC conversion time


.. _voltage_current_v2_bricklet_description:

Description
-----------

The Voltage/Current :ref:`Bricklet <primer_bricklets>` 2.0 can be used to 
extend :ref:`Bricks <primer_bricks>` by the possibility to measure
power/voltage/current. To do this you only have to put the Bricklet between
your power supply (e.g. battery) and your load (e.g. motor).

In case of battery powered systems you can measure the state of the battery
by bidirectional current measurement (charge/discharge).

This Bricklet ist not galvanically isolated to the Tinkerforge system. 
This means that there is a direct electrical connection between the terminals 
of the Bricklet and the rest of the system. Dependent of the application 
this can lead to undesired connections, ground loops or short circuits. 
These problems can be prevented by using the Bricklet together with a :ref:`Isolator Bricklet <isolator_bricklet>`.

The Voltage/Current Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            INA226 with 4mΩ Shunt Resistor
Current Consumption               30mW (6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximum Current                   ±20A
Maximum Input Voltage             36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 18mm (1.18 x 1.18 x 0.67")
Weight                            10g
================================  ============================================================


Resources
---------

* INA226 datasheet (`Download <https://github.com/Tinkerforge/voltage-current-v2-bricklet/raw/master/datasheets/ina226.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/voltage-current-v2-bricklet/raw/master/hardware/voltage-current-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/voltage_current_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/voltage-current-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2KdgYGx>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/voltage_current_v2/voltage-current-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/voltage_current_v2/voltage-current-v2.FCStd>`__)


Connectivity
------------

You have to connect the Voltage/Current Bricklet 2.0 between your power supply and 
your load. Connect the power supply with the terminal marked with "IN" and the
load with the terminal marked "OUT". The polarity is marked with "+" and "-".

.. warning::
 
 Keep the polarity in mind! This Bricklet is not protected against polarity 
 reversal!

The Bricklet measures the voltage between "+" and "-" of the "IN" terminal as
well as the current flow from "+" of the "IN" terminal to "+" of the "OUT"
terminal.


.. _voltage_current_v2_bricklet_test:

Test your Voltage/Current Bricklet 2.0
--------------------------------------

|test_intro|

|test_connect|.
Connect a motor and a battery to the Bricklet as displayed in the following
picture.

.. image:: /Images/Bricklets/bricklet_voltage_current_setup_600.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet with Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_setup_1200.jpg

|test_tab|

If everything went as expected you can now see the current used by the motor 
and a graph that shows the current over time.

.. image:: /Images/Bricklets/bricklet_voltage_current_v2_brickv.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_v2_brickv.jpg

|test_pi_ref|


Calibration
-----------

The current measurement of the Voltage/Current Bricklet is factory calibrated
at room temperature. The readings can shift by a few mA if the environment
is very cold or very hot. In this case you can recalibrate the Bricklet
with a precise multimeter:

.. image:: /Images/Bricklets/bricklet_voltage_current_v2_brickv_calibration.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet 2.0 calibration in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_v2_brickv_calibration.jpg

Start Brick Viewer and click on "Calibration..." and follow the steps that are
described in the GUI. 

You can calibrate the voltage as well as the current
measurement. In our experience you don't need to calibrate the voltage, it is
within 0.5% accuracy without any calibration.

If you remove the factory current calibration a recalibration is necessary because
of tolerances in the shunt resistor.

.. _voltage_current_v2_bricklet_case:

Case
----

A `laser-cut case for the Voltage/Current Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-voltage-current-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_voltage_current_case_350.jpg
   :scale: 100 %
   :alt: Case for Voltage/Current Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_voltage_current_case_1000.jpg

.. include:: Voltage_Current_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/voltage_current_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Voltage/Current Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/voltage_current_exploded.png

|bricklet_case_hint|


.. _voltage_current_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Voltage_Current_V2_hlpi.table
