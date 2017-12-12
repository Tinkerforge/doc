
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Moisture Bricklet
:shoplink: ../../../shop/bricklets/moisture-bricklet.html

.. include:: Moisture.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _moisture_bricklet:

Moisture Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_moisture_v11_tilted1_[?|?].jpg          Moisture Bricklet
	Bricklets/bricklet_moisture_v11_horizontal_[?|?].jpg       Moisture Bricklet
	Bricklets/bricklet_moisture_v11_tilted2_[?|?].jpg          Moisture Bricklet
	Cases/bricklet_moisture_v11_case_built_up_[?|?].jpg        Moisture Bricklet in Case
	Bricklets/bricklet_moisture_plant1_[100|600].jpg           Moisture Bricklet in Soil of Plant
	Bricklets/bricklet_moisture_plant2_[100|600].jpg           Moisture Bricklet in Soil of Plant
	Bricklets/bricklet_moisture_brickv_[100|].jpg              Moisture Bricklet in Brick Viewer
	Dimensions/moisture_bricklet_v11_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures soil moisture
* 12bit resolution


.. _moisture_bricklet_description:

Description
-----------

The Moisture :ref:`Bricklet <primer_bricklets>` is intended to
measure moisture in soil. It can extend :ref:`Bricks <primer_bricks>` by this
feature. It is also possible to use the Moisture Bricklet as a detector for
water filling level.

Since hardware version 1.1 a capacitive method of measurement is used. The
previous method of measurement used bare metal contacts that could result
in a :ref:`corrosion problem <moisture_bricklet_corrosion>`.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               < 5mW (< 1mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        12bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 86 x 5mm (0.99 x 3.39 x 0.2")
Weight                            5g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/moisture-bricklet/raw/master/hardware/moisture-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/moisture_bricklet_v11_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/moisture-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2BcPjEW>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/moisture/moisture.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/moisture/moisture.FCStd>`__)


.. _moisture_bricklet_test:

Test your Moisture Bricklet
---------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see changes of the moisture
value.

.. image:: /Images/Bricklets/bricklet_moisture_brickv.jpg
   :scale: 100 %
   :alt: Moisture Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_brickv.jpg

|test_pi_ref|


.. _moisture_bricklet_corrosion:

Corrosion problem with hardware version 1.0
-------------------------------------------

Hardware version 1.0 of the Moisture Bricklets used bare metal contacts to
measure the soil moisture. Some customers ran into corrosion problems with
this setup. Because of this, hardware version 1.1 now uses a capacitive
method of measurement without bare metal contacts. Therefore, corrosion can not
occur anymore.

.. image:: /Images/Bricklets/bricklet_moisture_tilted_350.jpg
   :scale: 100 %
   :alt: Moisture Bricklet hardware version 1.0
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_tilted_1000.jpg

.. _moisture_bricklet_case:

Case
----

A `laser-cut case for the Moisture Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-moisture-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_moisture_v11_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Moisture Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_v11_case_built_up_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet,
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Moisture Bricklet case:

.. image:: /Images/Exploded/moisture_v11_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Moisture Bricklet
   :align: center
   :target: ../../_images/Exploded/moisture_v11_exploded.png

|bricklet_case_hint|


.. _moisture_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Moisture_hlpi.table
