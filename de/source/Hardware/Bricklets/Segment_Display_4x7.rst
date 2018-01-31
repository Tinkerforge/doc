
:shoplink: ../../../shop/bricklets/segment-display-4x7-bricklet.html

.. include:: Segment_Display_4x7.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _segment_display_4x7_bricklet:

Segment Display 4x7 Bricklet
============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_segment_display_4x7_tilted_[?|?].jpg           Segment Display 4x7 Bricklet
	Bricklets/bricklet_segment_display_4x7_horizontal_[?|?].jpg       Segment Display 4x7 Bricklet
	Cases/bricklet_segment_display_4x7_case_tilted_[?|?].jpg          Segment Display 4x7 Bricklet im Gehäuse
	Bricklets/bricklet_segment_display_4x7_leds_on_[100|600].jpg      Segment Display 4x7 Bricklet aktiv
	Bricklets/bricklet_segment_display_4x7_brickv_[100|].jpg          Segment Display 4x7 Bricklet im Brick Viewer
	Dimensions/segment_display_4x7_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Vier 7-Segment Anzeigen mit schaltbarem Doppelpunkt
* Helligkeit der Segmente konfigurierbar
* Konfigurierbare Zähler Funktion


.. _segment_display_4x7_bricklet_description:

Beschreibung
------------

Das Segment Display 4x7 :ref:`Bricklet <primer_bricklets>` kann
genutzt werden um vier 7-Segment-Anzeigen und einen Doppelpunkt über 
:ref:`Bricks <primer_bricks>` zu steuern.
Jedes der 29 Segmente kann eigenständig geschaltet werden. Es ist zusätzlich
möglich die Helligkeit der Segmente einzustellen. Neben der Möglichkeit des
Schaltens einzelner Segmente bietet die API auch einen Anwender-konfigurierbaren
Zähler.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    | 1mA (alle Segmente aus)
                                  | 6mA (alle Segmente an mit minimaler Helligkeit)
                                  | 62mA (alle Segmente an mit maximaler Helligkeit)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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

* TM1637 Datenblatt (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/datasheets/TM1637.pdf>`__)
* KHN40392ASR1D-2 Datenblatt (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/datasheets/KHN40392ASR1D-2.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/hardware/segment-display-4x7-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/segment_display_4x7_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2iV9qNf>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/segment_display_4x7/segment_display_4x7.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/segment_display_4x7/segment_display_4x7.FCStd>`__)


.. _segment_display_4x7_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird können die einzelnen Segmente
nun ein-/ausgeschaltet werden.

.. image:: /Images/Bricklets/bricklet_segment_display_4x7_brickv.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_brickv.jpg

|test_pi_ref|

.. _segment_display_4x7_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Segment Display 4x7 Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-segment-display-4x7-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_segment_display_4x7_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Segment Display 4x7 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_segment_display_4x7_case_tilted_1000.jpg

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


.. _segment_display_4x7_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Segment_Display_4x7_hlpi.table


Bekannte Fehler/Probleme
------------------------

Falls das Segment Display 4x7 Bricklet (Version 1.0) an ein Master Brick 
angeschlossen wird, sollte versucht werden dieses an Port A oder B anzuschließen 
(nicht C und D). Das Segment Display 4x7 Bricklet speist eine Spannung zurück 
zum Master, welches den Analog-Digital-Wandler des Mikrocontrollers stören kann.

Dieses Problem wird in der nächsten Produktversion gelöst.
