
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Rotary Encoder Bricklet
:FIXME_shoplink: ../../../shop/bricklets/rotary-encoder-bricklet.html

.. include:: Rotary_Encoder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _rotary_encoder_bricklet:

Rotary Encoder Bricklet
=======================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_rotary_encoder_tilted_350.jpg",
	               "Bricklets/bricklet_rotary_encoder_tilted_600.jpg",
	               "Rotary Encoder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_vertical_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_vertical_600.jpg",
	             "Rotary Encoder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_horizontal_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_horizontal_600.jpg",
	             "Rotary Encoder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_master_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_master_600.jpg",
	             "Rotary Encoder Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_brickv_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_brickv.jpg",
	             "Rotary Encoder Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/rotary_encoder_bricklet_dimensions_100.png",
	             "Dimensions/rotary_encoder_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 360° Drehencoder
* Zählt 24 Schritte pro Umdrehung (Schrittwinkel 15°)

Beschreibung
------------

* Work In Progress

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Anzahl Klicks pro Rotation        24 (Winkel pro Schritt 15°)
Taster Betätigungskraft           200gf
Taster Bewegungsdistanz           0.5mm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 23mm (1,18 x 0,98 x 0,9")
Gewicht                           5g*
================================  ============================================================

* ohne Knopf

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rotary-encoder-bricklet/raw/master/hardware/rotary-encoder-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rotary_encoder_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rotary-encoder-bricklet/zipball/master>`__)


.. _rotary_encoder_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_rotary_encoder_master_600.jpg
   :scale: 100 %
   :alt: Rotary Encoder Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_encoder_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_rotary_encoder_brickv.jpg
   :scale: 100 %
   :alt: Rotary Encoder Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_encoder_brickv.jpg

|test_pi_ref|

.. _rotary_encoder_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Rotary Encoder Bricklet <https://www.tinkerforge.com/de/shop/cases/case-rotary-encoder-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_rotary_encoder_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Rotary Encoder Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_encoder_case_built_up_1000.jpg

.. include:: Rotary_Encoder.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/rotary_encoder_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Rotary Encoder Bricklet
   :align: center
   :target: ../../_images/Exploded/rotary_encoder_exploded.png

|bricklet_case_hint|


.. _rotary_encoder_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Rotary_Encoder_hlpi.table
