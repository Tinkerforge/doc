
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Moisture Bricklet
:FIXME_shoplink: ../../../shop/bricklets/moisture-bricklet.html

.. include:: Moisture.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _moisture_bricklet:

Moisture Bricklet
=================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_moisture_tilted_350.jpg",
	               "Bricklets/bricklet_moisture_tilted_600.jpg",
	               "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_vertical_100.jpg",
	             "Bricklets/bricklet_moisture_vertical_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_horizontal_100.jpg",
	             "Bricklets/bricklet_moisture_horizontal_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_master_100.jpg",
	             "Bricklets/bricklet_moisture_master_600.jpg",
	             "Moisture Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_brickv_100.jpg",
	             "Bricklets/bricklet_moisture_brickv.jpg",
	             "Moisture Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/moisture_bricklet_dimensions_100.png",
	             "Dimensions/moisture_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures moisture between two probes
* 12 bit resolution

Description
-----------

The Moisture :ref:`Bricklet <product_overview_bricklets>` is intended to
measure moisture in soil.

Current is passed through two probes. With a increasing moisture level the
resistance between the probes will decrease (since water is a better conductor
than soil). The change in resistance is measured and returned as the moisture
value.

You can either stick the Bricklet directly into soil or you can solder two
probes to the Bricklet and put the probes in soil.

It is also possible to use the Moisture Bricklet as a detector for water
filling level. 

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Resolution                        12bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            20 x 45 x 5mm (0.79 x 1.77 x 0.2")
Weight                            3g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/moisture-bricklet/raw/master/hardware/moisture-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/moisture_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/moisture-bricklet/zipball/master>`__)


.. _moisture_bricklet_test:

Test your Moisture Bricklet
---------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_moisture_master_600.jpg
   :scale: 100 %
   :alt: Moisture Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_master_1200.jpg

|test_tab|
If everything went as expected you can now see changes of the moisture
value.

.. image:: /Images/Bricklets/bricklet_moisture_brickv.jpg
   :scale: 100 %
   :alt: Moisture Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_brickv.jpg

|test_pi_ref|

.. _moisture_bricklet_case:

Case
----

A `laser-cut case for the Moisture Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-moisture-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_moisture_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Moisture Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_case_built_up_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet,
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Moisture Bricklet case:

.. image:: /Images/Exploded/moisture_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Moisture Bricklet
   :align: center
   :target: ../../_images/Exploded/moisture_exploded.png

|bricklet_case_hint|


.. _moisture_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Moisture_hlpi.table
