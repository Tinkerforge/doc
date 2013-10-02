
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Dual Button Bricklet
:FIXME_shoplink: ../../../shop/bricklets/dual-button-bricklet.html

.. include:: Dual_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _dual_button_bricklet:

Dual Button Bricklet
====================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_dual_button_tilted_350.jpg",
	               "Bricklets/bricklet_dual_button_tilted_600.jpg",
	               "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_vertical_100.jpg",
	             "Bricklets/bricklet_dual_button_vertical_600.jpg",
	             "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_horizontal_100.jpg",
	             "Bricklets/bricklet_dual_button_horizontal_600.jpg",
	             "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_master_100.jpg",
	             "Bricklets/bricklet_dual_button_master_600.jpg",
	             "Dual Button Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_brickv_100.jpg",
	             "Bricklets/bricklet_dual_button_brickv.jpg",
	             "Dual Button Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dual_button_bricklet_dimensions_100.png",
	             "Dimensions/dual_button_bricklet_dimensions_600.png",
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
Taster Typ                        Drucktaster mit LED
Taster Betätigungskraft           150gf
Taster Bewegungsdistanz           2.5mm
LED Farbe                         Blau
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 20 x 10mm (1,77 x 0,79 x 0,39")
Gewicht                           6g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/dual-button-bricklet/raw/master/hardware/dual-button-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_button_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-button-bricklet/zipball/master>`__)


.. _dual_button_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_dual_button_master_600.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_dual_button_brickv.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_brickv.jpg

|test_pi_ref|

.. _dual_button_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Dual Button Bricklet <https://www.tinkerforge.com/de/shop/cases/case-dual-button-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_dual_button_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Dual Button Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_dual_button_case_built_up_1000.jpg

.. include:: Dual_Button.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/dual_button_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Dual Button Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_button_exploded.png

|bricklet_case_hint|


.. _dual_button_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Dual_Button_hlpi.table
