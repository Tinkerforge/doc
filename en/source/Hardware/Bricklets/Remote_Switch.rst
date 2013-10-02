
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Remote Switch Bricklet
:FIXME_shoplink: ../../../shop/bricklets/remote-switch-bricklet.html

.. include:: Remote_Switch.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _remote_switch_bricklet:

Remote Switch Bricklet
======================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_remote_switch_tilted_350.jpg",
	               "Bricklets/bricklet_remote_switch_tilted_600.jpg",
	               "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_switch_vertical_100.jpg",
	             "Bricklets/bricklet_remote_switch_vertical_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_switch_horizontal_100.jpg",
	             "Bricklets/bricklet_remote_switch_horizontal_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_switch_master_100.jpg",
	             "Bricklets/bricklet_remote_switch_master_600.jpg",
	             "Remote Switch Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_switch_brickv_100.jpg",
	             "Bricklets/bricklet_remote_switch_brickv.jpg",
	             "Remote Switch Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/remote_switch_bricklet_dimensions_100.png",
	             "Dimensions/remote_switch_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Work In Progress


Description
-----------


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Radio Frequency                   433MHz
Supported Remote Mains Switches   All based on HX2262, (`complete list <TODO>`__)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 40 x 5mm (0.98 x 1.58 x 0.2") without antenna
Weight                            7g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/raw/master/hardware/remote-switch-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/remote_switch_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/zipball/master>`__)


.. _remote_switch_bricklet_test:

Test your Remote Switch Bricklet
--------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_remote_switch_master_600.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_master_1200.jpg

|test_tab|
If everything went as expected you can now ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_remote_switch_brickv.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_brickv.jpg

|test_pi_ref|

.. _remote_switch_bricklet_case:

Case
----

A `laser-cut case for the Remote Switch Bricklet <https://www.tinkerforge.com/en/shop/cases/case-remote-switch-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_remote_switch_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Remote Switch Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_remote_switch_case_built_up_1000.jpg

.. include:: Remote_Switch.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/remote_switch_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Remote Switch Bricklet
   :align: center
   :target: ../../_images/Exploded/remote_switch_exploded.png

|bricklet_case_hint|


.. _remote_switch_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Remote_Switch_hlpi.table
