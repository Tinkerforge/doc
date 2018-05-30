
:DISABLED_shoplink: ../../../shop/bricklets/ptc-v2-bricklet.html

.. include:: PTC_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ptc_v2_bricklet:

PTC Bricklet 2.0
================

.. note::
  This Bricklet is currently work-in-progress!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ptc_v2_tilted_[?|?].jpg           PTC Bricklet 2.0
	Bricklets/bricklet_ptc_v2_tilted2_[?|?].jpg          PTC Bricklet 2.0
	Bricklets/bricklet_ptc_v2_top_[?|?].jpg              PTC Bricklet 2.0
	Cases/bricklet_ptc_v2_case_[100|600].jpg             PTC Bricklet 2.0 with case
	Bricklets/bricklet_ptc_v2_brickv_[100|].jpg          PTC Bricklet 2.0 in Brick Viewer
	Dimensions/ptc_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Supports Pt100 and Pt1000 sensors
* Supports 2-wire, 3-wire and 4-wire type
* Measures temperature with 0.5% accuracy at the full scale of -246 to 849°C
* Resolution of 0.03125°C (15bit)


.. _ptc_v2_bricklet_description:

Description
-----------

The PTC :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure temperature with Pt100 and Pt1000 sensors.

Pt100 and Pt1000 sensors of 2-wire, 3-wire or 4-wire type can be used.

The measured temperature can be read out in `°C
<https://en.wikipedia.org/wiki/Degree_Celsius>`__.
With configurable events it is possible to react on changing
temperatures without polling.

The PTC Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
RTD-to-Digital Converter          MAX31865
Current Consumption               40mW (8mA at 5V)
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
Weight                            9g
================================  ============================================================


Resources
---------

* MAX31865 datasheet (`Download <https://github.com/Tinkerforge/ptc-v2-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ptc-v2-bricklet/raw/master/hardware/ptc-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ptc_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ptc-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2rjjW4L>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/ptc_v2/ptc-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/ptc_v2/ptc-v2.FCStd>`__)


.. _ptc_v2_bricklet_jumper_configuration:

Jumper Configuration
--------------------

Configure the jumper for Pt100/Pt1000 sensor and 2/3/4-wire type as
shown below. The pins of the pin headers that are marked red have to be closed
by a jumper for the corresponding sensor type.

TODO: Update image?

.. image:: /Images/Bricklets/bricklet_ptc_pt_wire_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 jumper configuration
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_pt_wire_1000.jpg

.. _ptc_v2_bricklet_connectivity:

Connectivity
------------

See below for connection diagrams for 2/3/4-wire type resistance temperature
device.

TODO: Update image?

.. image:: /Images/Bricklets/bricklet_ptc_connectivity_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 connection diagram
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_connectivity_1000.jpg

Additionally the number of wires has to be set with the API.

.. _ptc_v2_bricklet_test:

Test your PTC Bricklet 2.0
--------------------------

|test_intro|

|test_connect|  and attach a Pt100/1000 sensor (see picture below).
In this example we use a 3-wire Pt100 sensor.

TODO: Update image

.. image:: /Images/Bricklets/bricklet_ptc_sensor_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 connected to 2-wire Pt100 sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_sensor_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_ptc_v2_brickv.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_v2_brickv.jpg

Put the sensor in your hand to see the
temperature rising (or falling if it is extremely warm in your room).

|test_pi_ref|


.. _ptc_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the PTC Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-ptc-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_ptc_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for PTC Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_ptc_v2_case_1000.jpg

	.. include:: PTC_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/ptc_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for PTC Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/ptc_v2_exploded.png

	|bricklet_case_hint|


.. _ptc_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: PTC_V2_hlpi.table
