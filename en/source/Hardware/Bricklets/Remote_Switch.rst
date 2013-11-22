
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Remote Switch Bricklet
:FIXME_shoplink: ../../../shop/bricklets/remote-switch-bricklet.html

.. include:: Remote_Switch.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _remote_switch_bricklet:

Remote Switch Bricklet
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_remote_tilted_350.jpg",
	               "Bricklets/bricklet_remote_tilted_600.jpg",
	               "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_vertical_100.jpg",
	             "Bricklets/bricklet_remote_vertical_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_horizontal_100.jpg",
	             "Bricklets/bricklet_remote_horizontal_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_tilted_wo_antenna_100.jpg",
	             "Bricklets/bricklet_remote_tilted_wo_antenna_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_w_antenna_100.jpg",
	             "Bricklets/bricklet_remote_w_antenna_600.jpg",
	             "Remote Switch Bricklet und Antenne")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_switch_brickv_100.jpg",
	             "Bricklets/bricklet_remote_switch_brickv.jpg",
	             "Remote Switch Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/remote_bricklet_dimensions_100.png",
	             "Dimensions/remote_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Wireless house automation
* Controls remote mains switches (:ref:`supported devices <remote_switch_supported_devices>`)
* Can control remote mains switches with dimming function

Description
-----------

The Remote Switch :ref:`Bricklet <product_overview_bricklets>` is equipped with
a 433MHz RF transceiver (433MHz SMA Antenna is included). It can be used to
control remote mains switches that are based on the PT2262 and HX2262 ICs.

House code as well as receiver code can be configured with the API.

Technical Specifications
------------------------

================================  ========================================================================================
Property                          Value
================================  ========================================================================================
Radio Module                      RFM69HW
--------------------------------  ----------------------------------------------------------------------------------------
--------------------------------  ----------------------------------------------------------------------------------------
Radio Frequency                   433MHz
Supported Remote Mains Switches   All based on PT2262 and HX2262, (:ref:`complete list <remote_switch_supported_devices>`)
--------------------------------  ----------------------------------------------------------------------------------------
--------------------------------  ----------------------------------------------------------------------------------------
Dimensions (W x D x H)            25 x 40 x 5mm (0.98 x 1.58 x 0.2")*
Weight                            7g*
================================  ========================================================================================

\* without antenna

Resources
---------

* RFM69HW datasheet (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/raw/master/datasheets/RFM69HW.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/raw/master/hardware/remote-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/remote_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/zipball/master>`__)


.. _remote_switch_supported_devices:

List of Supported Devices
-------------------------

The following devices are known to be controllable with the 
Remote Switch Bricklet. If you found another remote mains switch
that is compatible please write us an email, we would like to add it.

=============== ====================================
Manufacturer    Models
=============== ====================================
BAT             * RC 3500-A
                * RC AAA1000-A
                * RC AAA3680-A
--------------- ------------------------------------
--------------- ------------------------------------
Brennstuhl      * RC 2044 Indoor
                * RC 2044 Outdoor
                * RC 3600
                * RCS 1000 N Comfort
                * RCS 1044 N Comfort
                * RCS 2044 N Comfort Indoor
                * RCS 2044 N Comfort Outdoor
--------------- ------------------------------------
--------------- ------------------------------------
ELRO            * AB440D
                * AB440ID
                * AB440IS
                * AB440L
                * AB440S
                * AB440W
--------------- ------------------------------------
--------------- ------------------------------------
Intertechno     * CMR-300
                * CMR-500
                * CMR-1000
                * CMR-1224
                * GRR-300
                * GRR-3500
                * IT-1500
                * IT-2300
                * ITL-150
                * ITL-210
                * ITL-230
                * ITL-250
                * ITL-300
                * ITL-500
                * ITL-1000
                * ITL-3500
                * ITR-300
                * ITR-1500
                * ITR-3500
                * ITR-7000
                * ITDL-1000
                * ITDR-3500
                * ITDR-3500T
                * LBUR-100
                * PA3-1000
--------------- ------------------------------------
--------------- ------------------------------------
Mumbi           * m-FS300
--------------- ------------------------------------
--------------- ------------------------------------
Vivanco         * FSS 31000W
                * FSS 33600W
=============== ====================================

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
If everything went as expected you can now control remote mains switches. 

.. image:: /Images/Bricklets/bricklet_remote_switch_brickv.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_brickv.jpg

|test_pi_ref|


House Code and Receiver Code
----------------------------

To control remote switches or dimmers the house code and the receiver code
must be known. These codes are typically configurable with small DIP-switches
inside the remote switch or dimmer.

TODO Image


.. _remote_switch_bricklet_case:

Case
----

A `laser-cut case for the Remote Switch Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-remote-switch-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_remote_switch_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Remote Switch Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_remote_switch_case_built_up_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet,
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Temperature IR Bricklet case:

.. image:: /Images/Exploded/remote_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Remote Switch Bricklet
   :align: center
   :target: ../../_images/Exploded/remote_exploded.png

|bricklet_case_hint|


.. _remote_switch_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Remote_Switch_hlpi.table
