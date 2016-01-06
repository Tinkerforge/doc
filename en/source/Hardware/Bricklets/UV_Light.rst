
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / UV Light Bricklet
:FIXME_shoplink: ../../../shop/bricklets/uv-light-bricklet.html

.. include:: UV_Light.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _uv_light_bricklet:

UV Light Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_uv_light_tilted_350.jpg",
	               "Bricklets/bricklet_uv_light_tilted_600.jpg",
	               "UV Ligh Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_uv_light_horizontal_100.jpg",
	             "Bricklets/bricklet_uv_light_horizontal_600.jpg",
	             "UV Ligh Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_uv_light_brickv_100.jpg",
	             "Bricklets/bricklet_uv_light_brickv.jpg",
	             "UV Ligh Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/uv_light_bricklet_dimensions_100.png",
	             "Dimensions/uv_light_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures UV Light concentration in µW/cm² and UV Index

.. _uv_light_bricklet_description:

Description
-----------

The UV Light :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure
`UV Light <https://en.wikipedia.org/wiki/Ultraviolet>`__. The
measured UV Light can be read out in
`ppm <https://en.wikipedia.org/wiki/Parts-per_notation>`__.
With configurable events it is possible to react on changing 
values without polling.

Typical applications are sunscreen warning and environmental
data logging.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            VEML6070
Current Consumption               TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 0µW/cm² - 328mW/cm²
Resolution                        1µW/cm² (0.004 UV Index)
Range of spectral sensitivity     320-410nm (UVA)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Weight                            2g
================================  ============================================================

Resources
---------

* VEML6070 datasheet (`Download <https://github.com/Tinkerforge/uv-light-bricklet/raw/master/datasheets/veml6070.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/uv-light-bricklet/raw/master/hardware/uv-light-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/uv_light_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/uv-light-bricklet/zipball/master>`__)


.. _uv_light_bricklet_test:

Test your UV Light Bricklet
-----------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_uv_light_brickv.jpg
   :scale: 100 %
   :alt: UV Light Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_uv_light_brickv.jpg

|test_pi_ref|

.. _uv_light_bricklet_case:

Case
----

A `laser-cut case for the UV Light Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for UV Light Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: UV Light.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for UV Light Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|

.. _uv_light_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: UV_Light_hlpi.table
