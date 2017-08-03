
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Analog In Bricklet 2.0
:shoplink: ../../../shop/bricklets/analog-in-v2-bricklet.html

.. include:: Analog_In_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_v2_bricklet:

Analog In Bricklet 2.0
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_analog_in_v2_tilted1_[?|?].jpg          Analog In Bricklet 2.0
	Bricklets/bricklet_analog_in_v2_tilted2_[?|?].jpg          Analog In Bricklet 2.0
	Bricklets/bricklet_analog_in_v2_horizontal_[?|?].jpg       Analog In Bricklet 2.0
	Cases/bricklet_analog_in_v2_case_built_up_[?|?].jpg        Analog In Bricklet 2.0 in case
	Bricklets/bricklet_analog_in_v2_brickv_[100|].jpg          Analog In Bricklet 2.0 in Brick Viewer
	Dimensions/analog_in_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures voltages up to 42V (DC)
* Full-scale resolution of ~10mV

.. _analog_in_v2_bricklet_description:

Description
-----------

The Analog In :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the capability to
measure voltages. It is the successor of the :ref:`analog_in_bricklet`.
The voltage can be read out in `Volt
<https://en.wikipedia.org/wiki/Volt>`__ directly without conversions necessary.

With configurable events it is possible to react on changing
voltages without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               30mW (6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 42V (DC) in 1mV steps, 12bit resolution (~10mV)
Maximum Output Current            150mA (3.3V), 150mA (5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 14mm (1.38 x 1.18 x 0.55")
Weight                            8g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/analog-in-v2-bricklet/raw/master/hardware/analog_in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog_in_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-in-v2-bricklet/zipball/master>`__)
* 3D model (`View online <http://a360.co/2vshwVc>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/analog_in_v2/analog_in.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/analog_in_v2/analog_in.FCStd>`__)


Connectivity
------------

The Analog In Bricklet 2.0 has five terminals. With these terminals you can
access the following output signals: 5V, 3.3V as well as GND. The voltage you
want to measure can be applied between the VIN and the GND terminal.

.. image:: /Images/Bricklets/bricklet_analog_in_v2_horizontal_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet 2.0 Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v2_horizontal_1200.jpg


.. _analog_in_v2_bricklet_test:

Test your Analog In Bricklet 2.0
--------------------------------

|test_intro|

|test_connect|.
Additionally connect a DC voltage you want to measure to the Bricklet. For
testing purposes connect the 5V or 3.3V output terminal to the VIN terminal.
The GND terminals are already connected internally.

|test_tab|
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_analog_in_v2_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v2_brickv.jpg

|test_pi_ref|


.. _analog_in_v2_bricklet_case:

Case
----

A `laser-cut case for the Analog In Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-analog-in-out-v2-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_analog_in_v2_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Analog In Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_v2_case_built_up_1000.jpg

.. include:: Analog_In_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_v2_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Analog In Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/analog_v2_in_exploded.png

|bricklet_case_hint|


.. _analog_in_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Analog_In_V2_hlpi.table
