
:DISABLED_shoplink: ../../../shop/bricklets/load-cell-v2-bricklet.html

.. include:: Load_Cell_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _load_cell_v2_bricklet:

Load Cell Bricklet 2.0
======================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_load_cell_v2_tilted_[?|?].jpg           Load Cell Bricklet 2.0
	Bricklets/bricklet_load_cell_v2_tilted2_[?|?].jpg          Load Cell Bricklet 2.0
	Bricklets/bricklet_load_cell_v2_top_[?|?].jpg              Load Cell Bricklet 2.0
	Cases/bricklet_load_cell_v2_case_[?|?].jpg                 Load Cell Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_load_cell_v2_brickv_[100|].jpg          Load Cell Bricklet 2.0 im Brick Viewer
	Dimensions/load_cell_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst die Ausgabe von Wägezelle
* 24Bit A/D-Wandler für hohe Auflösung
* Bis zu 80 Gewichts-Messungen pro Sekunde


.. _load_cell_v2_bricklet_description:

Beschreibung
------------

Mit dem Load Cell :ref:`Bricklet <primer_bricklets>` 2.0 können 
:ref:`Bricks <primer_bricks>` Wägezellen auslesen. Für die Kalibrierung der
Wägezelle wird nur ein einziges bekanntes Gewicht benötigt. Es ist möglich
Gewichtsunterschiede von wenigen Gramm zwischen Objekten zu bestimmen die
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

Das Load Cell Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            HX711
Stromverbrauch                    54mW (10,8mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         24Bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 14mm (1,18 x 1,18 x 0,55")
Gewicht                           7,3g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/load-cell-v2-bricklet/raw/master/hardware/load-cell-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/load_cell_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/load-cell-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2IeyZE6>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/load_cell_v2/load-cell-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/load_cell_v2/load-cell-v2.FCStd>`__)


.. _load_cell_v2_bricklet_connectivity:

Anschlussmöglichkeiten
----------------------

Das Load Cell Bricklet 2.0 hat vier Anschlussklemmen. Die PWR und GND
Anschlussklemmen sind für die Excitation-Spannung und die IN+ und IN-
Anschlussklemmen sind für die Signalmessung.

.. image:: /Images/Bricklets/bricklet_load_cell_v2_top_350.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet 2.0 Anschlussklemmen
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_v2_top_1200.jpg

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


.. _load_cell_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss eine Wägezelle :ref:`angeschlossen
<load_cell_bricklet_connectivity>` und :ref:`kalibriert
<load_cell_bricklet_calibration>` werden.

|test_tab|
Wenn alles wie erwartet funktioniert wird das gemessene Gewicht in Gramm
angezeigt. Der Graph gibt den zeitlichen Verlauf des Gewichts wieder.

.. image:: /Images/Bricklets/bricklet_load_cell_v2_brickv.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_v2_brickv.jpg

|test_pi_ref|


.. _load_cell_bricklet_v2_calibration:

Kalibrierung
------------

Das Load Cell Bricklet 2.0 muss für die angeschlossenen Wägezelle und den
aktuellen Aufbau kalibriert werden.

.. image:: /Images/Screenshots/load_cell_bricklet_calibration.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet Kalibrierung im Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/load_cell_bricklet_calibration.jpg

Schließe eine Wägezelle, wie :ref:`oben <load_cell_bricklet_connectivity>`
beschrieben, an das Load Cell Bricklet 2.0 an. Starte dann Brick Viewer und klicke
den "Calibration" Knopf im "Load Cell Bricklet 2.0" Tab. Klicke dann ohne Gewicht
auf der Wägezelle den "Calibrate Zero" Knopf. Belaste dann die Wägezelle mit
einem bekannten Gewicht, gib das Gewicht in Gramm als "Current Weight" ein und
klicke den "Calibrate Weight" Knopf.

Das Load Cell Bricklet 2.0 ist nun für die angeschlossenen Wägezelle und den
aktuellen Aufbau kalibriert.

.. _load_cell_bricklet_v2_scale_kit:

Waagenkit
---------

Das Waagenkit setzt sich aus `MakerBeam <https://www.tinkerforge.com/de/shop/makerbeam.html>`__,
einer `1kg Wägezelle <https://www.tinkerforge.com/de/shop/accessories/sensors/load-cell-1kg-czl635.html>`__,
sowie laser-geschnittenen Plastikteilen zusammen. Es ist im 
`Tinkerforge Shop <https://www.tinkerforge.com/de/shop/kits/scale-kit.html>`__ verfügbar.
Die Anleitung kann allerdings auch als Quelle dienen um eine grundsätzliche Idee
zu bekommen wie der mechanischen Aufbau von Waagen mit einer Wägezelle aussieht.


.. image:: /Images/Misc/scale_w_master_600.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet mit Master Brick und Waagenkit
   :align: center
   :target: ../../_images/Misc/scale_w_master_1200.jpg

* Der Aufbau des Waagenkits ist sehr einfach. Starte mit dem entfernen der 
  Schutzfolie von den Plastikteilen (die Schutzfolie befindet sich auf beiden Seiten).

* Schraube die 60mm MakerBeam und die Wägezelle auf das obere Plastikteil. Stelle
  sicher, dass der Pfeil auf der Wägezelle auf der Seite des Plastikteils ist und vom
  Plastikteil wegzeigt.

.. image:: /Images/Misc/scale_setup_part0_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 0
   :align: center
   :target: ../../_images/Misc/scale_setup_part0_1000.jpg

.. image:: /Images/Misc/scale_setup_part1_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 1
   :align: center
   :target: ../../_images/Misc/scale_setup_part1_1000.jpg

* Schraube die 100mm MakerBeam und die Wägezelle an das untere Plastikteil.

.. image:: /Images/Misc/scale_setup_part2_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 2
   :align: center
   :target: ../../_images/Misc/scale_setup_part2_1000.jpg

.. image:: /Images/Misc/scale_setup_part3_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 3
   :align: center
   :target: ../../_images/Misc/scale_setup_part3_1000.jpg

.. image:: /Images/Misc/scale_setup_part4_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 4
   :align: center
   :target: ../../_images/Misc/scale_setup_part4_1000.jpg

* Nutze das doppelseitige Klebeband um die runde Platte an den 60mm MakerBeam zu befestigen.

.. image:: /Images/Misc/scale_setup_part5_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 5
   :align: center
   :target: ../../_images/Misc/scale_setup_part5_1000.jpg

.. image:: /Images/Misc/scale_setup_part6_350.jpg
   :scale: 100 %
   :alt: Waagenkit Teil 6
   :align: center
   :target: ../../_images/Misc/scale_setup_part6_1000.jpg

* Die mechanische Konstruktion ist fertig! Nun kann das Load Cell Bricklet noch
  wie im, :ref:`Anschlussmöglichkeiten <load_cell_bricklet_connectivity>`-Abschnitt
  angeschlossen werden.

.. image:: /Images/Misc/scale3_350.jpg
   :scale: 100 %
   :alt: Zusammengebaute Waage
   :align: center
   :target: ../../_images/Misc/scale3_1000.jpg


.. _load_cell_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Load Cell Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-load-cell-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_load_cell_v2_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Load Cell Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_load_cell_v2_case_1000.jpg

.. include:: Load_Cell.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/load_cell_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Load Cell Bricklet
   :align: center
   :target: ../../_images/Exploded/load_cell_exploded.png

|bricklet_case_hint|


.. _load_cell_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Load_Cell_V2_hlpi.table
