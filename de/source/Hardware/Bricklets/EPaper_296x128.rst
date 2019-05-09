
:DISABLED_shoplink: ../../../shop/bricklets/e-paper-296x128-bricklet.html

.. include:: EPaper_296x128.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _e_paper_296x128_bricklet:

E-Paper 296x128 Bricklet
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_e_paper_296x128_tilted_[?|?].jpg           E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_horizontal_[?|?].jpg       E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_master_[100|600].jpg       E-Paper 296x128 Bricklet mit Master Brick
	Cases/bricklet_e_paper_296x128_case_[100|600].jpg             E-Paper 296x128 Bricklet im Gehäuse
	Bricklets/bricklet_e_paper_296x128_brickv_[100|].jpg          E-Paper 296x128 Bricklet im Brick Viewer
	Dimensions/e_paper_296x128_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 7,4cm (2,9") E-Paper Display mit einer Auflösung von 296x128 Pixel
* Zwei Dreifarb-Displays verfügbar: Schwarz/Weiß/Rot und Schwarz/Weiß/Grau
* Eingebetteter Font für einfache Textdarstellung


.. _e_paper_296x128_bricklet_description:

Beschreibung
------------

Das E-Paper 296x128 :ref:`Bricklet <primer_bricklets>` Ist ein E-Paper Display mit
einer Auflösung von 296x128 Pixel.

Jedes Pixel kann individuell gesetzt werden, das Display kann also Grafiken anzeigen.
Der Inhalt des Displays bleibt bestehen wenn das Bricklet vom Strom getrennt wird.

Eine Dreifarb-Aktualisierung des Bildschirminhalts dauert ungefähr 7,5 Sekunden. Mit
unterschiedlichen Aktualisierungs-Modi ist es möglich Aktualisierungsraten von bis zu
1Hz zu erreichen wenn nur Schwarz und Weiß genutzt wird.

Das E-Paper 296x128 Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    | 45mW (9mA bei 5V) inaktiv
                                  | 95mW (19mA bei 5V) während des setzen eines Bildes
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Display-Auflösung                 296x128 Pixel
Display-Größe                     7,4cm (2,9")
Display-Farben                    Schwarz/Weiß/Rot oder Schwarz/Weiß/Grau
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           100 x 40 x 6mm (3,93 x 1,57 x 0,24")
Gewicht                           20g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/raw/master/hardware/e-paper-296x128-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/e_paper_296x128_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _e_paper_296x128_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte das Tab im Brick Viewer wie folgt aussehen.

Es ist möglich per Maus auf dem Display zu zeichnen und Text zu schreiben.

Hinweis: Beim starten des Bricklet kann der Inhalt des Displays nicht ausgelesen werden.
Daher zeigt der Brick Viewer nach dem starten erst schwarzes Display, auch wenn etwas
auf dem Display dargestellt wird. Nach dem ersten schreiben auf dem Display kann der
Brick Viewer den Display-Inhalt auslesen bis das Bricklet wieder neugestartet wird.

.. image:: /Images/Bricklets/bricklet_e_paper_296x128_brickv.jpg
   :scale: 100 %
   :alt: E-Paper 296x128 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_e_paper_296x128_brickv.jpg

|test_pi_ref|


.. _e_paper_296x128_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das E-Paper 296x128 Bricklet
	<https://www.tinkerforge.com/de/shop/cases/case-e-paper-296x128-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_e_paper_296x128_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für E-Paper 296x128 Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_e_paper_296x128_case_1000.jpg

	.. include:: EPaper_296x128.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/e_paper_296x128_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für E-Paper 296x128 Bricklet
	   :align: center
	   :target: ../../_images/Exploded/e_paper_296x128_exploded.png

	|bricklet_case_hint|


.. _e_paper_296x128_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: EPaper_296x128_hlpi.table
