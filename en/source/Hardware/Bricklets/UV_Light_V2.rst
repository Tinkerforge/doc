
:shoplink: ../../../shop/bricklets/uv-light-v2-bricklet.html

.. include:: UV_Light_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _uv_light_v2_bricklet:

UV Light Bricklet 2.0
=====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_uv_light_v2_tilted_[?|?].jpg           UV Light Bricklet 2.0
	Bricklets/bricklet_uv_light_v2_top_[?|?].jpg              UV Light Bricklet 2.0
	Bricklets/bricklet_uv_light_v2_brickv_[100|].jpg          UV Light Bricklet 2.0 in Brick Viewer
	Dimensions/uv_light_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures UV-A, UV-B and UV index


.. _uv_light_v2_bricklet_description:

Description
-----------

The UV Light :ref:`Bricklet <primer_bricklets>` 2.0 measures
UV-A as well as UV-B and uses the measurements to calculate 
the `UV index <https://en.wikipedia.org/wiki/Ultraviolet_index>`__.

With configurable events it is possible to react on changing 
values without polling.

Typical applications are sunscreen warning and environmental
data logging.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            VEML6076
Current Consumption               35mW (7mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
UV-A resolution                   0.93 µW/cm²
UV-B resolution                   2.1 µW/cm²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2.1g
================================  ============================================================


Resources
---------

* VEML6075 datasheet (`Download <https://github.com/Tinkerforge/uv-light-v2-bricklet/raw/master/datasheets/veml6075.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/uv-light-v2-bricklet/raw/master/hardware/uv-light-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/uv_light_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/uv-light-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2KcOI6s>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/uv_light_v2/uv-light-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/uv_light_v2/uv-light-v2.FCStd>`__)


.. _uv_light_v2_bricklet_test:

Test your UV Light Bricklet 2.0
-------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should show UV-A and
UV-B measurements as well as the UV index.

.. image:: /Images/Bricklets/bricklet_uv_light_v2_brickv.jpg
   :scale: 100 %
   :alt: UV Light Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_uv_light_v2_brickv.jpg

|test_pi_ref|



.. _uv_light_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: UV_Light_V2_hlpi.table
