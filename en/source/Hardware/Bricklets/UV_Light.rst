
:shoplink: ../../../shop/bricklets/uv-light-bricklet.html

.. include:: UV_Light.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _uv_light_bricklet:

UV Light Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_uv_light_tilted_[?|?].jpg           UV Ligh Bricklet
	Bricklets/bricklet_uv_light_horizontal_[?|?].jpg       UV Ligh Bricklet
	Bricklets/bricklet_uv_light_brickv_[100|].jpg          UV Ligh Bricklet in Brick Viewer
	Dimensions/uv_light_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The UV Light Bricklet is discontinued. We are selling our remaining stock. The
 :ref:`UV Light Bricklet 2.0 <uv_light_v2_bricklet>` is the recommended
 replacement.

Features
--------

* Measures UV light intensity in µW/cm² and UV Index

.. _uv_light_bricklet_description:

Description
-----------

The UV Light :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure
`UV light <https://en.wikipedia.org/wiki/Ultraviolet>`__. The
measured UV light can be read out in µW/cm². 1 µW/cm² equals
0.004 UV Index.
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
Current Consumption               < 5mW (< 1mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 0mW/cm² to 328mW/cm²
Resolution                        1µW/cm² (0.004 UV Index)
Spectral Range                    320nm to 410nm (UVA)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* VEML6070 datasheet (`Download <https://github.com/Tinkerforge/uv-light-bricklet/raw/master/datasheets/veml6070.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/uv-light-bricklet/raw/master/hardware/uv-light-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/uv_light_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/uv-light-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BfEWjJ>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/uv_light/uv-light.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/uv_light/uv-light.FCStd>`__)

.. _uv_light_bricklet_test:

Test your UV Light Bricklet
---------------------------

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

.. include:: UV_Light.substitutions
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
