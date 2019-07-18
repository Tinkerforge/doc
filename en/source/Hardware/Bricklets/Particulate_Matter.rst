
:shoplink: ../../../shop/bricklets/particulate-matter-bricklet.html

.. include:: Particulate_Matter.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _particulate_matter_bricklet:

Particulate Matter Bricklet
===========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_particulate_matter_tilted_[?|?].jpg           Particulate Matter Bricklet
	Bricklets/bricklet_particulate_matter_top_[?|?].jpg              Particulate Matter Bricklet
	Bricklets/bricklet_particulate_matter_front_[?|?].jpg            Particulate Matter Bricklet
	Bricklets/bricklet_particulate_matter_tilted2_[?|?].jpg          Particulate Matter Bricklet
	Cases/bricklet_particulate_matter_case_[?|?].jpg                 Particulate Matter Bricklet with case
	Cases/bricklet_particulate_matter_case_side_[?|?].jpg            Particulate Matter Bricklet with case
	Bricklets/bricklet_particulate_matter_brickv_[100|].jpg          Particulate Matter Bricklet in Brick Viewer
	Dimensions/particulate_matter_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures Particulate Matter concentration
* Measures in µg/m³ for different sizes
* Distinguishable particle sizes: PM1.0, PM2.5 and PM10
* Integrated fan for air flow

.. _particulate_matter_bricklet_description:

Description
-----------

The Particulate Matter :ref:`Bricklet <primer_bricklets>` can be used to extend the 
features of :ref:`Bricks <primer_bricks>` by the
capability to measure particulate matter concentration. 

The Bricklet supports the size classes PM1.0, PM2.5 and PM10. Additionally it is
possible to measure the count of particles in 100ml of air with the supported sizes of 
0.3µm, 0.5µm, 1.0µm, 2.5µm, 5.0µm and 10.0µm.

The Particulate Matter Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            PMS7003
Current Consumption               388mW (77.6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Particulate matter concentration  PM1.0, PM2.5, PM10
Particulate matter count          0.3µm, 0.5µm, 1.0µm, 2.5µm, 5.0µm, 10.0µm (in 100ml of air)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            70 x 40 x 15mm (2.76 x 1.57 x 0.59")
Weight                            36.3g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/particulate-matter-bricklet/raw/master/hardware/particulate-matter-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/particulate_matter_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/particulate-matter-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2rFjjDp>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/particulate_matter/particulate-matter.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/particulate_matter/particulate-matter.FCStd>`__)

.. _particulate_matter_bricklet_laser_diode:

Laser Diode Lifetime
--------------------

The Particulate Matter Bricklet uses a laser diode. The diode has a lifetime of about
8000 hours of continous use.

If you want to measure in an interval with a long idle time (e.g. hourly) you should
turn the laser diode off between the measurements to increase the longevity of the
Bricklet.

The sensor takes about 30 seconds after it is enabled to settle and produce stable
values.

.. _particulate_matter_bricklet_test:

Test your Particulate Matter Bricklet
-------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now read the Particulate Matter concentration.

.. image:: /Images/Bricklets/bricklet_particulate_matter_brickv.jpg
   :scale: 100 %
   :alt: Particulate Matter Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_particulate_matter_brickv.jpg

|test_pi_ref|


.. _particulate_matter_bricklet_case:

Case
----

A `laser-cut case for the Particulate Matter Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-particulate-matter-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_particulate_matter_case_350.jpg
   :scale: 100 %
   :alt: Case for Particulate Matter Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_particulate_matter_case_1000.jpg

.. include:: Particulate_Matter.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/particulate_matter_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Particulate Matter Bricklet
   :align: center
   :target: ../../_images/Exploded/particulate_matter_exploded.png

|bricklet_case_hint|


.. _particulate_matter_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Particulate_Matter_hlpi.table
