
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / NFC/RFID Bricklet
:shoplink: ../../../shop/bricklets/nfc-rfid-bricklet.html

.. include:: NFC_RFID.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_rfid_bricklet:

NFC/RFID Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_nfc_rfid_tilted_350.jpg",
	               "Bricklets/bricklet_nfc_rfid_tilted_600.jpg",
	               "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_horizontal_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_horizontal_600.jpg",
	             "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_vertical_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_vertical_600.jpg",
	             "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_setup_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_setup_600.jpg",
	             "NFC/RFID Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_nfc_rfid_case_100.jpg",
	             "Cases/bricklet_nfc_rfid_case_600.jpg",
	             "NFC/RFID Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_brickv_100.png",
	             "Bricklets/bricklet_nfc_rfid_brickv.png",
	             "NFC/RFID Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/nfc_rfid_bricklet_dimensions_100.png",
	             "Dimensions/nfc_rfid_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* TODO: FIXME
* Measure power, voltage and current up to 720W/36V/20A
* 1mW, 1mV, 1mA resolution over the whole range
* Bidirectional current measurement (e.g. charge/discharge)
* Configurable averaging and ADC conversion time

Description
-----------

TODO: FIXME

The NFC/RFID :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend :ref:`Bricks <product_overview_bricks>` by the possibility to measure
power/voltage/current. To do this you only have to put the Bricklet between
your power supply (e.g. battery) and your load (e.g. motor).

In case of battery powered systems you can measure the state of the battery
by bidirectional current measurement (charge/discharge).


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            PN532
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
TODO                              TOOD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            TODO: 30 x 30 x 18mm (1.18 x 1.18 x 0.67")
Weight                            TODOg
================================  ============================================================


Resources
---------

* INA226 Datasheet (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/datasheets/PN532.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/hardware/nfc-rfid-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/nfc_rfid_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/zipball/master>`__)


.. _nfc_rfid_bricklet_test:

First Test
----------

|test_intro|

|test_connect|.

.. image:: /Images/Bricklets/bricklet_nfc_rfid_setup_600.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet with Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_setup_1200.jpg

|test_tab|

If everything went as expected you can now see TBD 

.. image:: /Images/Bricklets/bricklet_nfc_rfid_brickv.png
   :scale: 70 %
   :alt: NFC/RFID Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_brickv.png

|test_pi_ref|

.. _nfc_rfid_bricklet_case:

Case
----

A `laser-cut case for the NFC/RFID Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-nfc-rfid-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_nfc_rfid_case_350.jpg
   :scale: 100 %
   :alt: Case for NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_rfid_case_1000.jpg

.. include:: NFC_RFID.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/nfc_rfid_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Exploded/nfc_rfid_exploded.png

|bricklet_case_hint|


.. _nfc_rfid_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: NFC_RFID_hlpi.table
