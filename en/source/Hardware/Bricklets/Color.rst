
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Color Bricklet
:shoplink: ../../../shop/bricklets/color-bricklet.html

.. include:: Color.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _color_bricklet:

Color Bricklet
==============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_color_tilted_350.jpg",
	               "Bricklets/bricklet_color_tilted_600.jpg",
	               "Color Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_vertical_100.jpg",
	             "Bricklets/bricklet_color_vertical_600.jpg",
	             "Color Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_horizontal_100.jpg",
	             "Bricklets/bricklet_color_horizontal_600.jpg",
	             "Color Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_master_100.jpg",
	             "Bricklets/bricklet_color_master_600.jpg",
	             "Color Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_color_case_built_up_100.jpg",
	             "Cases/bricklet_color_case_built_up_600.jpg",
	             "Color Bricklet in Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_brickv_100.jpg",
	             "Bricklets/bricklet_color_brickv.jpg",
	             "Color Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/color_bricklet_dimensions_100.png",
	             "Dimensions/color_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* TODO: FIXME
* Measures ambient light up to 900lux
* Output in 0.1lux steps (12bit resolution)


Description
-----------

TODO: FIXME


The Color :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` with the
capability to measure ambient light. The measured illuminance can be read
out in `lux <http://en.wikipedia.org/wiki/Lux>`__. With configurable events
it is possible to react on changing illuminance without polling.

Typical applications are illuminance dependent switching of
backlights, motors etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            TCS34725
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Illumination                      TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            TBDg
================================  ============================================================


Resources
---------

* TEMT6000 datasheet (`Download <https://github.com/Tinkerforge/color-bricklet/raw/master/datasheets/TCS34725.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/color-bricklet/raw/master/hardware/color-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/color_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/color-bricklet/zipball/master>`__)


.. _color_bricklet_test:

Test your Color Bricklet
--------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_color_master_600.jpg
   :scale: 100 %
   :alt: Color Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_master_1200.jpg

|test_tab|
If everything went as expected you can now see TBD 

.. image:: /Images/Bricklets/bricklet_color_brickv.jpg
   :scale: 100 %
   :alt: Color Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_brickv.jpg

|test_pi_ref|


.. _color_bricklet_case:

Case
----

A `laser-cut case for the Color Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-color-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_color_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Color Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_color_case_built_up_1000.jpg

.. include:: Color.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/color_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Color Bricklet
   :align: center
   :target: ../../_images/Exploded/color_exploded.png

|bricklet_case_hint|


.. _color_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Color_hlpi.table
