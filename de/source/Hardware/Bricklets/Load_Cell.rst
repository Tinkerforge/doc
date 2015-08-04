
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Load Cell Bricklet
:shoplink: ../../../shop/bricklets/load-cell-bricklet.html

.. include:: Load_Cell.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _load_cell_bricklet:

Load Cell Bricklet
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_load_cell_tilted1_350.jpg",
	               "Bricklets/bricklet_load_cell_tilted1_600.jpg",
	               "Load Cell Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_load_cell_tilted2_100.jpg",
	             "Bricklets/bricklet_load_cell_tilted2_600.jpg",
	             "Load Cell Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_load_cell_horizontal_100.jpg",
	             "Bricklets/bricklet_load_cell_horizontal_600.jpg",
	             "Load Cell Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_load_cell_case_built_up1_100.jpg",
	             "Cases/bricklet_load_cell_case_built_up1_600.jpg",
	             "Load Cell Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Cases/bricklet_load_cell_case_built_up2_100.jpg",
	             "Cases/bricklet_load_cell_case_built_up2_600.jpg",
	             "Load Cell Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_load_cell_brickv_100.jpg",
	             "Bricklets/bricklet_load_cell_brickv.jpg",
	             "Load Cell Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/load_cell_bricklet_dimensions_100.png",
	             "Dimensions/load_cell_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst die Ausgabe von Wägezelle
* 24Bit A/D-Wandler für hohe Auflösung
* Bis zu 80 Gewichts-Messungen pro Sekunde


.. _load_cell_bricklet_description:

Beschreibung
------------

Mit dem Load Cell :ref:`Bricklet <primer_bricklets>` können Bricks
:ref:`Bricks <primer_bricks>` Wägezellen auslesen. Für die Kalibrierung der
Wägezelle wird nur ein einziges bekanntes Gewicht benötigt. Es ist möglich
Gewichtsunterschiede von wenige Gramm zwischen Objekten zu bestimmen die
selbst viele Kilogramm wiegen.

Im Shop sind Wägezellen für verschiedene Maximalgewichte verfügbar:

* `Wägezelle 1kg CZL635
  <https://www.tinkerforge.com/de/shop/accessories/sensors/load-cell-1kg-czl635.html>`__
* `Wägezelle 5kg CZL635
  <https://www.tinkerforge.com/de/shop/accessories/sensors/load-cell-5kg-czl635.html>`__
* `Wägezelle 20kg CZL601
  <https://www.tinkerforge.com/de/shop/accessories/sensors/load-cell-20kg-czl601.html>`__
* `Wägezelle 50kg CZL601
  <https://www.tinkerforge.com/de/shop/accessories/sensors/load-cell-50kg-czl601.html>`__

Auf dem Bricklet befindet sich eine LED die mittels API ein- und ausgeschaltet
werden kann, um z.B. anzuzeigen, dass das gemessene Gewicht in einem bestimmten
Bereich liegt.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            HX711
Stromverbrauch                    150mW (28mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         24Bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 14mm (1,18 x 1,18 x 0,55")
Gewicht                           7g
================================  ============================================================


Ressourcen
----------

* HX711 Datenblatt (`Download <https://github.com/Tinkerforge/load-cell-bricklet/raw/master/datasheets/hx711.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/load-cell-bricklet/raw/master/hardware/load-cell-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/load_cell_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/load-cell-bricklet/zipball/master>`__)


.. _load_cell_bricklet_connectivity:

Anschlussmöglichkeiten
----------------------

Das Load Cell Bricklet hat vier Anschlussklemmen. Die PWR und GND
Anschlussklemmen sind für die Excitation-Spannung und die IN+ und IN-
Anschlussklemmen sind für die Signalmessung.

.. image:: /Images/Bricklets/bricklet_load_cell_horizontal_350.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet Anschlussklemmen
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_horizontal_1200.jpg

Eine typsiche Wägezelle hat vier oder fünf Drähte. In der Spezifikation der
Wägezelle sollte die Belegung der Drähte dokumentiert sein. Schließe die
Wägezelle entsprechend der folgenden Tabelle an.

============== ================ ================================================
Anschluss      Anschlussklemme  Mögliche Drahtfarben
============== ================ ================================================
Excitation +   PWR              rot
Excitation -   GND              schwarz, gelb
Signal +       IN+              grün, blau
Signal -       IN-              weiss
============== ================ ================================================

Wenn die Wägezelle entsprechend des angebrachten Pfeils belastet wird dann
sollte ein positives Gewicht gemessen werden. Falls ein negatives Gewicht
gemessen wird müssen die Drähten an den IN+ und IN- Anschlussklemmen vertauscht
werden.


.. _load_cell_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss eine eine Wägezelle :ref:`angeschlossen
<load_cell_bricklet_connectivity>` und :ref:`kalibriert
<load_cell_bricklet_calibration>` werden.

|test_tab|
Wenn alles wie erwartet funktioniert wird das gemessene Gewicht in Gramm
angezeigt. Der Graph gibt den zeitlichen Verlauf des Gewichts wieder.

.. image:: /Images/Bricklets/bricklet_load_cell_brickv.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_brickv.jpg

|test_pi_ref|


.. _load_cell_bricklet_calibration:

Kalibrierung
------------

Das Load Cell Bricklet muss für die angeschlossenen Wägezelle und den
aktuellen Aufbau kalibriert werden.

.. image:: /Images/Screenshots/load_cell_bricklet_calibration.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet Kalibrierung im Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/load_cell_bricklet_calibration.jpg

Schließe eine Wägezelle, wie :ref:`oben <load_cell_bricklet_connectivity>`
beschrieben, an das Load Cell Bricklet an. Starte dann Brick Viewer und klicke
den "Calibration" Knopf im "Load Cell Bricklet" Tab. Klicke dann ohne Gewicht
auf der Wägezelle den "Calibrate Zero" Knopf. Belaste dann die Wägezelle mit
einem bekannten Gewicht, gib das Gewicht in Gramm als "Current Weight" ein und
klicke den "Calibrate Weight" Knopf.

Das Load Cell Bricklet ist nun für die angeschlossenen Wägezelle und den
aktuellen Aufbau kalibriert.


.. _load_cell_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Load Cell Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-load-cell-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_load_cell_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Load Cell Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_load_cell_case_built_up1_1000.jpg

.. include:: Load_Cell.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/load_cell_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Load Cell Bricklet
   :align: center
   :target: ../../_images/Exploded/load_cell_exploded.png

|bricklet_case_hint|


.. _load_cell_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Load_Cell_hlpi.table
