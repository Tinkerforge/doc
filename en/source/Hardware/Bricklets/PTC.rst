
.. include:: PTC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ptc_bricklet:

PTC Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ptc_tilted_[?|?].jpg      PTC Bricklet
	Bricklets/bricklet_ptc_vertical_[?|?].jpg    PTC Bricklet
	Bricklets/bricklet_ptc_horizontal_[?|?].jpg  PTC Bricklet
	Bricklets/bricklet_ptc_sensor_[100|600].jpg  PTC Bricklet with 3-wire Pt100 RTD
	Bricklets/bricklet_ptc_jumper_[100|600].jpg  PTC Bricklet
	Cases/bricklet_ptc_case_[100|600].jpg        PTC Bricklet in Case
	Bricklets/bricklet_ptc_brickv_[100|].jpg     PTC Bricklet in Brick Viewer
	Dimensions/ptc_dimensions_[100|600].png      Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The PTC Bricklet is discontinued and is no longer sold. The
 :ref:`PTC Bricklet 2.0 <ptc_v2_bricklet>` is the recommended
 replacement.

Features
--------

* Supports Pt100 and Pt1000 sensors
* Supports 2-wire, 3-wire and 4-wire type
* Measures temperature with 0.5% accuracy at the full scale of -246 to 849°C
* Resolution of 0.03125°C (15bit), output in 0.01°C steps


.. _ptc_bricklet_description:

Description
-----------

The PTC :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure temperature with Pt100 and Pt1000 sensors.

Pt100 and Pt1000 sensors of 2-wire, 3-wire or 4-wire type can be used.

The measured temperature can be read out in `°C
<https://en.wikipedia.org/wiki/Degree_Celsius>`__.
With configurable events it is possible to react on changing
temperatures without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
RTD-to-Digital Converter          MAX31865
Current Consumption               2mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Supported Pt-Sensor Types         Pt100 and Pt1000 with 2-wire, 3-wire or 4-wire
Accuracy                          min 0.5% full scale
Input Protection                  +-50V
Temperature Resolution            0.03125°C (15bit)
Conversion Time                   21ms
Fault Detection                   Open RTD element, RTD value out-of-range, short across RTD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 15mm (1.38 x 1.18 x 0.59")
Weight                            8g
================================  ============================================================

Resources
---------

* MAX31865 datasheet (`Download <https://github.com/Tinkerforge/ptc-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ptc-bricklet/raw/master/hardware/ptc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ptc_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ptc-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2knGTQP>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/ptc/ptc.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/ptc/ptc.FCStd>`__)

.. _ptc_bricklet_jumper_configuration:

Jumper Configuration
--------------------

Configure the jumper for Pt100/Pt1000 sensor and 2/3/4-wire type as
shown below. The pins of the pin headers that are marked red have to be closed
by a jumper for the corresponding sensor type.

.. image:: /Images/Bricklets/bricklet_ptc_pt_wire_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet jumper configuration
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_pt_wire_1000.jpg

.. _ptc_bricklet_connectivity:

Connectivity
------------

See below for connection diagrams for 2/3/4-wire type resistance temperature
device.

.. image:: /Images/Bricklets/bricklet_ptc_connectivity_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet connection diagram
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_connectivity_1000.jpg

Additionally the number of wires has to be set with the API.

.. _ptc_bricklet_test:

Test your PTC Bricklet
----------------------

|test_intro|

|test_connect| and attach a Pt100/1000 sensor (see picture below).
In this example we use a 3-wire Pt100 sensor.

.. image:: /Images/Bricklets/bricklet_ptc_sensor_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet connected to 3-wire Pt100 sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_sensor_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_ptc_brickv.jpg
   :scale: 100 %
   :alt: PTC Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_brickv.jpg

Put the sensor in your hand to see the
temperature rising (or falling if it is extremely warm in your room).

|test_pi_ref|


.. _ptc_bricklet_case:

Case
----

A `laser-cut case for the PTC Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-ptc-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ptc_case_350.jpg
   :scale: 100 %
   :alt: Case for PTC Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ptc_case_1000.jpg

.. include:: PTC.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ptc_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for PTC Bricklet
   :align: center
   :target: ../../_images/Exploded/ptc_exploded.png


.. _ptc_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: PTC_hlpi.table
