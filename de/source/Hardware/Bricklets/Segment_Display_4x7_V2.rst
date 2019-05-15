
:DISABLED_shoplink: ../../../shop/bricklets/segment-display-4x7-v2-bricklet.html

.. include:: Segment_Display_4x7_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _segment_display_4x7_v2_bricklet:

Segment Display 4x7 Bricklet 2.0
================================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_segment_display_4x7_v2_tilted_[?|?].jpg           Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_horizontal_[?|?].jpg       Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_master_[100|600].jpg       Segment Display 4x7 Bricklet 2.0 mit Master Brick
	Cases/bricklet_segment_display_4x7_v2_case_[100|600].jpg             Segment Display 4x7 Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_segment_display_4x7_v2_brickv_[100|].jpg          Segment Display 4x7 Bricklet 2.0 im Brick Viewer
	Dimensions/segment_display_4x7_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Vier 7-Segment Anzeigen
* Schaltbarer Punkt pro Anzeige, Doppelpunkt und Hochkomma
* Helligkeit der Segmente konfigurierbar
* Konfigurierbare Zähler Funktion


.. _segment_display_4x7_v2_bricklet_description:

Beschreibung
------------

Das Segment Display 4x7 :ref:`Bricklet <primer_bricklets>` 2.0 kann
genutzt werden um vier 7-Segment-Anzeigen und einen Doppelpunkt über 
:ref:`Bricks <primer_bricks>` zu steuern.
Jedes der 29 Segmente kann eigenständig geschaltet werden. Es ist zusätzlich
möglich die Helligkeit der Segmente einzustellen. Neben der Möglichkeit des
Schaltens einzelner Segmente bietet die API auch einen Anwender-konfigurierbaren
Zähler.

Das Segment Display 4x7 Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ================================================================
Eigenschaft                       Wert
================================  ================================================================
Stromverbrauch                    | 30mW  (6mA bei 5V)  alle Segmente aus
                                  | 60mW  (12mA bei 5V) alle Segmente an mit minimaler Helligkeit
                                  | 400mW (80mA bei 5V) alle Segmente an mit maximaler Helligkeit
--------------------------------  ----------------------------------------------------------------
--------------------------------  ----------------------------------------------------------------
Segmentbreite                     6mm
Segmenthöhe                       10mm
Helligkeit eines Segments         Konfigurierbar in 8 Schritten
--------------------------------  ----------------------------------------------------------------
--------------------------------  ----------------------------------------------------------------
Abmessungen (B x T x H)           25 x 65 x 9mm (0,98 x 2,56 x 0,35")
Gewicht                           11g
================================  ================================================================


Ressourcen
----------

* TM1637 Datenblatt (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/raw/master/datasheets/TM1637.pdf>`__)
* LTC-4627JR Datenblatt (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/raw/master/datasheets/LTC-4627JR.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/raw/master/hardware/segment-display-4x7-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/segment_display_4x7_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2WFOtYT>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/segment_display_4x7_v2/segment-display-4x7-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/segment_display_4x7_v2/segment-display-4x7-v2.FCStd>`__)


.. _segment_display_4x7_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können die einzelnen Segmente
nun ein-/ausgeschaltet werden.

.. image:: /Images/Bricklets/bricklet_segment_display_4x7_v2_brickv.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_v2_brickv.jpg

|test_pi_ref|


.. _segment_display_4x7_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Segment Display 4x7 Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-segment-display-4x7-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_segment_display_4x7_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Segment Display 4x7 Bricklet 2.0
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
   :alt: Explosionszeichnung für Segment Display 4x7 Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/segment_display_4x7_exploded.png

|bricklet_case_hint|


.. _segment_display_4x7_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Segment_Display_4x7_V2_hlpi.table
