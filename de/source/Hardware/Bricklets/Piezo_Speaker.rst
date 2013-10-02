
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Piezo Speaker Bricklet
:FIXME_shoplink: ../../../shop/bricklets/piezo-speaker-bricklet.html

.. include:: Piezo_Speaker.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _piezo_speaker_bricklet:

Piezo Speaker Bricklet
========================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_piezo_speaker_tilted_350.jpg",
	               "Bricklets/bricklet_piezo_speaker_tilted_600.jpg",
	               "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_vertical_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_vertical_600.jpg",
	             "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_horizontal_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_horizontal_600.jpg",
	             "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_master_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_master_600.jpg",
	             "Piezo Speaker Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_brickv_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_brickv.jpg",
	             "Piezo Speaker Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/piezo_speaker_bricklet_dimensions_100.png",
	             "Dimensions/piezo_speaker_bricklet_dimensions_600.png",
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
Frequenzbereich                   585 - 7100Hz (konfigurierbar)
Schalldruck                       60 - 82dB/10cm (abhängig von Frequenz)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 30 x 13mm (0,98 x 1,18 x 0,51")
Gewicht                           5g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/raw/master/hardware/piezo-speaker-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/piezo_speaker_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/zipball/master>`__)


.. _piezo_speaker_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_piezo_speaker_master_600.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_piezo_speaker_brickv.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_brickv.jpg

|test_pi_ref|

.. _piezo_speaker_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Piezo Speaker Bricklet <https://www.tinkerforge.com/de/shop/cases/case-piezo-speaker-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_piezo_speaker_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Piezo Speaker Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_piezo_speaker_case_built_up_1000.jpg

.. include:: Piezo_Speaker.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/piezo_speaker_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Piezo Speaker Bricklet
   :align: center
   :target: ../../_images/Exploded/piezo_speaker_exploded.png

|bricklet_case_hint|


.. _piezo_speaker_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Piezo_Speaker_hlpi.table
