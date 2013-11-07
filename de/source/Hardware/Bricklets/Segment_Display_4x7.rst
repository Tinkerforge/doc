
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Segment Display 4x7 Bricklet
:FIXME_shoplink: ../../../shop/bricklets/segment-display-4x7-bricklet.html

.. include:: Segment_Display_4x7.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _segment_display_4x7_bricklet:

Segment Display 4x7 Bricklet
============================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_segment_display_4x7_tilted_350.jpg",
	               "Bricklets/bricklet_segment_display_4x7_tilted_600.jpg",
	               "Segment Display 4x7 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_vertical_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_vertical_600.jpg",
	             "Segment Display 4x7 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_horizontal_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_horizontal_600.jpg",
	             "Segment Display 4x7 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_master_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_master_600.jpg",
	             "Segment Display 4x7 Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_brickv_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_brickv.jpg",
	             "Segment Display 4x7 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/segment_display_4x7_bricklet_dimensions_100.png",
	             "Dimensions/segment_display_4x7_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Vier 7-Segment Anzeigen mit Schaltbarem Doppelpunkt
* Helligkeit von Segmenten konfigurierbar.
* Konfigurierbare Counter Funktion

Beschreibung
------------

Da Segment Display 4x7 kann genutzt werden um vier 7-Segment-Anzeigen zu
und ein Doppelpunkt zu steuern. Jedes der 29 Segmente kann eigenständig
geschaltet werden. Es ist zusätzlich möglich die Helligkeit der Segmente
einzustellen. Neben der Möglichkeit des Schaltens einzelner Segmente bietet
die API auch einen Anwender konfigurierbaren Counter.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Segmentbreite                     6mm
Segmenthöhe                       10mm
Helligkeit eines Segments         Konfigurierbar, bis zu 70mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 65 x 9mm (0,98 x 2,56 x 0,35")
Gewicht                           11g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/hardware/segment-display-4x7-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/segment_display_4x7_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/zipball/master>`__)


.. _segment_display_4x7_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_segment_display_4x7_master_600.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird können die einzelnen Segmente
nun an-/ausgeschaltet werden.

.. image:: /Images/Bricklets/bricklet_segment_display_4x7_brickv.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_brickv.jpg

|test_pi_ref|

.. _segment_display_4x7_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Segment Display 4x7 Bricklet <https://www.tinkerforge.com/de/shop/cases/case-segment-display-4x7-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_segment_display_4x7_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Segment Display 4x7 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_segment_display_4x7_case_built_up_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Bricklet an Oberteil mit Abstandshalter von unten und den langen Schrauben von oben,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Oberteil und
* schraube Unterteil auf unteren Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Segment Display 4x7 Bricklet-Gehäuse:

.. image:: /Images/Exploded/segment_display_4x7_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Segment Display 4x7 Bricklet
   :align: center
   :target: ../../_images/Exploded/segment_display_4x7_exploded.png

|bricklet_case_hint|


.. _segment_display_4x7_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Segment_Display_4x7_hlpi.table
