
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Moisture Bricklet
:FIXME_shoplink: ../../../shop/bricklets/moisture-bricklet.html

.. include:: Moisture.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _moisture_bricklet:

Moisture Bricklet
=================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_moisture_tilted_350.jpg",
	               "Bricklets/bricklet_moisture_tilted_600.jpg",
	               "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_vertical_100.jpg",
	             "Bricklets/bricklet_moisture_vertical_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_horizontal_100.jpg",
	             "Bricklets/bricklet_moisture_horizontal_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_master_100.jpg",
	             "Bricklets/bricklet_moisture_master_600.jpg",
	             "Moisture Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_brickv_100.jpg",
	             "Bricklets/bricklet_moisture_brickv.jpg",
	             "Moisture Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/moisture_bricklet_dimensions_100.png",
	             "Dimensions/moisture_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Work In Progress


Beschreibung
------------


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           ? x ? x ?mm (? x ? x ?")
Gewicht                           ?g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/moisture-bricklet/raw/master/hardware/moisture-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/moisture_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/moisture-bricklet/zipball/master>`__)


.. _moisture_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_moisture_master_600.jpg
   :scale: 100 %
   :alt: Moisture Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_moisture_brickv.jpg
   :scale: 100 %
   :alt: Moisture Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_brickv.jpg

|test_pi_ref|

.. _moisture_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Moisture Bricklet <https://www.tinkerforge.com/de/shop/cases/case-moisture-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_moisture_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Moisture Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_case_built_up_1000.jpg

.. include:: Moisture.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/moisture_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Moisture Bricklet
   :align: center
   :target: ../../_images/Exploded/moisture_exploded.png

|bricklet_case_hint|


.. _moisture_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Moisture_hlpi.table
