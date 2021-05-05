:shoplink: ../../../shop/bricklets/industrial-ptc-bricklet.html

.. include:: Industrial_PTC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_ptc_bricklet:

Industrial PTC Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_ptc_tilted_[?|?].jpg           Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_w_connector_[?|?].jpg      Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_tilted2_[?|?].jpg          Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_horizontal_[?|?].jpg       Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_w_ptc1_[?|?].jpg           Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_w_ptc2_[?|?].jpg           Industrial PTC Brickle
	Bricklets/bricklet_industrial_ptc_brickv_[100|].jpg          Industrial PTC Bricklet in Brick Viewer
	Dimensions/industrial_ptc_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

Features
--------

* Supports Pt100 and Pt1000 sensors
* Supports 2-wire, 3-wire and 4-wire type
* Measures temperature with 0.05% accuracy at the full scale of -246 to 849°C
* Resolution of 0.03125°C (15bit), output in 0.01°C steps


.. _industrial_ptc_bricklet_description:

Description
-----------

The Industrial PTC :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure temperature with Pt100 and Pt1000 sensors.

Pt100 and Pt1000 sensors of 2-wire, 3-wire or 4-wire type can be used.

The measured temperature can be read out in `°C
<https://en.wikipedia.org/wiki/Degree_Celsius>`__.
With configurable events it is possible to react on changing
temperatures without polling.

This Bricklet ist not galvanically isolated to the Tinkerforge system. 
This means that there is a direct electrical connection between the terminals 
of the Bricklet and the rest of the system. Dependent of the application 
this can lead to undesired connections, ground loops or short circuits. 
These problems can be prevented by using the Bricklet together with a :ref:`Isolator Bricklet <isolator_bricklet>`.

The Industrial PTC Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
RTD-to-Digital Converter          MAX31865
Current Consumption               50mW (10mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Supported Pt-Sensor Types         Pt100 and Pt1000 with 2-wire, 3-wire or 4-wire
Accuracy                          min 0.05% full scale
Input Protection                  +-50V
Temperature Resolution            0.03125°C (15bit)
Conversion Time                   21ms
Fault Detection                   Open RTD element, RTD value out-of-range, short across RTD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 12mm (1,57 x 1,57 x 0,47")
Weight                            11g
================================  ============================================================


Resources
---------

* MAX31865 datasheet (`Download <https://github.com/Tinkerforge/industrial-ptc-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-ptc-bricklet/raw/master/hardware/industrial-ptc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_ptc_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-ptc-bricklet/zipball/master>`__)
* 3D model (`View online <https://a360.co/3e42mLH>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_ptc/industrial-ptc.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_ptc/industrial-ptc.FCStd>`__)

.. _industrial_ptc_bricklet_jumper_configuration:

Jumper Configuration
--------------------

Configure the DIP switch for Pt100/Pt1000 sensor and 2/3/4-wire type as
shown below.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_pt_wire_600.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet jumper configuration
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_pt_wire_1000.jpg

.. _industrial_ptc_bricklet_connectivity:

Connectivity
------------

See below for connection diagrams for 2/3/4-wire type resistance temperature
device.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_caption_600.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet connection diagram
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_caption_1000.jpg

Additionally the number of wires has to be set with the API.

.. _industrial_ptc_bricklet_test:

Test your Industrial PTC Bricklet
---------------------------------

|test_intro|

|test_connect| and attach a Pt100/1000 sensor (see picture below).
In this example we use a 2-wire Pt100 sensor.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_w_ptc1_600.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet connected to 2-wire Pt100 sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_w_ptc1_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_brickv.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_brickv.jpg

Put the sensor in your hand to see the
temperature rising (or falling if it is extremely warm in your room).

|test_pi_ref|


.. _industrial_ptc_bricklet_case:

Case
----

A `laser-cut case for the Industrial PTC Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industria-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial PTC Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_PTC.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial PTC Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png


.. _industrial_ptc_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_PTC_hlpi.table
