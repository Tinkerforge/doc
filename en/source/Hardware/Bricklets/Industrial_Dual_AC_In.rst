:shoplink: ../../../shop/bricklets/industrial-dual-ac-in-bricklet.html

.. include:: Industrial_Dual_AC_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_ac_in_bricklet:

Industrial Dual AC In Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_ac_in_tilted_[?|?].jpg           Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_horizontal_w_connector_[?|?].jpg      Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_horizontal_[?|?].jpg       Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_caption_[?|?].jpg          Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_brickv_[100|].jpg          Industrial Dual AC In Bricklet in Brick Viewer
	Dimensions/industrial_dual_ac_in_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Two inputs that can detect the presence of 230VAC mains voltage
* State LED per input


.. _industrial_dual_ac_in_bricklet_description:

Description
-----------

The Industrial Dual AC In :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by two inputs that
can detect the presence of 230VAC mains voltage. 
The state of each input is visualized by an LED. 

You can use this Bricklet to detect if a conductor is live with 230V AC. 

.. warning::
 Terminals and contacts are not insulated. This Bricklet should be
 placed in a casing. Touching the contacts is potentially life-threatening!

Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Input resistance                    249k Ohm (Photocoupler input with 249k series resistor)
Current Consumption                 50mW (10mA at 5V)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                              29g
==================================  ============================================================


Resources
---------

* HCPL2731 opto coupler (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/raw/master/datasheets/HCPL2731.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/raw/master/hardware/industrial-dual-ac-in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_ac_in_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/zipball/master>`__)
* 3D model (`View online <https://a360.co/3nvkxgh>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_in/industrial-dual-ac-in.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_in/industrial-dual-ac-in.FCStd>`__)


Connectivity
------------

The following picture shows how to connect the two inputs of the Industrial Dual AC In Bricklet.
Two live (L) wires can be monitored. Both share a common neutral (N) connection, which can
be accessed by two contacts.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_in_caption_front_and_top_800.jpg
   :scale: 100 %
   :alt: Industrial Dual AC In Bricklet Connectivity
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_in_caption_front_and_top_1200.jpg


.. _industrial_dual_ac_in_bricklet_test:

Test your Industrial Dual AC In Bricklet
-------------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_in_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual AC In Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_in_brickv.jpg

|test_pi_ref|


.. _industrial_dual_ac_in_bricklet_case:

Case
----
For the Industrial Dual AC In Bricklet the 
`laser-cut case for the Industrial Bricklets
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ can be used.

.. image:: /Images/Cases/bricklet_industrial_digital_in_4_v2_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Dual AC In Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_digital_in_4_v2_case_1000.jpg

.. include:: Industrial_Dual_AC_In.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Dual AC In Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|

.. _industrial_dual_ac_in_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Dual_AC_in_hlpi.table
