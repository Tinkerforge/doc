:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Motorized Linear Poti Bricklet
:shoplink: ../../../shop/bricklets/motorized-linear-poti-bricklet.html

.. include:: Motorized_Linear_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _motorized_linear_poti_bricklet:

Motorized Linear Poti Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_motorized_linear_poti_tilted1_[?|?].jpg          Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_tilted2_[?|?].jpg          Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_motor_[?|?].jpg            Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_bottom_[?|?].jpg           Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_side_[?|?].jpg             Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_front_[?|?].jpg            Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_brickv_[100|].jpg          Motorized Linear Poti Bricklet in Brick Viewer
	Dimensions/motorized_linear_poti_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Linear Potentiometer with 100mm fader travel
* Fader position can be controlled by user and with a motor
* No additional power supply necessary
* Automatic calibration


.. _motorized_linear_poti_bricklet_description:

Description
-----------

The Motorized Linear Poti :ref:`Bricklet <primer_bricklets>` is equipped with
a motor controllable 100mm linear `potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`__.
It can be connected to a :ref:`Brick <primer_bricks>`.

The position of the potentiometer ranges from 0 (slider down) to 100 (slider up). A user
can change the position of the potentiometer and it is possible to drive the potentiometer 
to any position with an integrated motor.

You can configure the potentiometer to hold the position. In this case it automatically
drives back to the set-point when a user changes the position. If it is not configured
to hold a position, the Bricklet will only drive to the set-point once and after that
the user can control the position again.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_motorized_linear_poti_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_motorized_linear_poti_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_motorized_linear_poti_video.webm" type="video/webm">
	</video> 

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption (motor off)   48.5mW (9.7mA at 5V)
Current Consumption (motor on)    465mW (93mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Fader Travel                      100mm

Mounting hole size                M3
Distance between mounting holes   120mm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            145 x 20 x 28mm (5.70 x 0.79 x 1.10")
Weight                            67g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/motorized-linear-poti-bricklet/raw/master/hardware/motorized-linear-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/motorized_linear_poti_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/motorized-linear-poti-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2mTL23j>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/motorized_linear_poti/motorized-poti.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/motorized_linear_poti/motorized-poti.FCStd>`__)



.. _motorized_linear_poti_bricklet_test:

Test your Motorized Linear Poti Bricklet
----------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now control the position of the
potentiometer with the GUI.

.. image:: /Images/Bricklets/bricklet_motorized_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Motorized Linear Poti Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motorized_linear_poti_brickv.jpg

|test_pi_ref|

.. _motorized_linear_poti_bricklet_case:

Case
----

A `laser-cut case for the Motorized Linear Poti Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-motorized-linear-poti-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_motorized_linear_poti_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Case for Motorized Linear Poti Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_motorized_linear_poti_case_built_up1_800.jpg

The assembly is easiest if you follow the following steps:

* Screw 12mm screws to bottom plate with nut,
* screw bricklet on 12mm screws with another nut,
* attach the two small plates from the backside of the bricklet to the bottom plate,
* attach one of the side plates,
* attach small plate from the frontside of the bricklet to the side plate,
* screw 12mm and 10mm spacer to small plates at both sides,
* attach left and right plate,
* attach other side plate and
* attach top plate and screw it to spacers.

Below you can see an exploded assembly drawing of the Motorized Linear Poti Bricklet case:

.. image:: /Images/Exploded/motorized_linear_poti_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Motorized Linear Poti Bricklet
   :align: center
   :target: ../../_images/Exploded/motorized_linear_poti_exploded.png

|bricklet_case_hint|


.. _motorized_linear_poti_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Motorized_Linear_Poti_hlpi.table
