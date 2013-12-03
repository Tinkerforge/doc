
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Line Bricklet
:shoplink: ../../../shop/bricklets/line-bricklet.html

.. include:: Line.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _line_bricklet:

Line Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_line_tilted_350.jpg",
	               "Bricklets/bricklet_line_tilted_600.jpg",
	               "Line Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_vertical_100.jpg",
	             "Bricklets/bricklet_line_vertical_600.jpg",
	             "Line Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_horizontal_100.jpg",
	             "Bricklets/bricklet_line_horizontal_600.jpg",
	             "Line Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_tilted_back_100.jpg",
	             "Bricklets/bricklet_line_tilted_back_600.jpg",
	             "Line Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_line_case1_tilted_100.jpg",
	             "Bricklets/bricklet_line_case1_tilted_600.jpg",
	             "Line Bricklet Befestigungsplatte Version 1")
	}}
	{{
	    tfdocimg("Cases/bricklet_line_case2_tilted1_100.jpg",
	             "Bricklets/bricklet_line_case2_tilted1_600.jpg",
	             "Line Bricklet Befestigungsplatte Version 2")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_brickv_100.jpg",
	             "Bricklets/bricklet_line_brickv.jpg",
	             "Line Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/line_bricklet_dimensions_100.png",
	             "Dimensions/line_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst die Reflektivität einer Oberfläche
* Kann genutzt werden um Linien zu erkennen/verfolgen
* Kann Entfernungen von ca. 0-10mm zu messen

Beschreibung
------------

Das Line :ref:`Bricklet <product_overview_bricklets>` ist mit einem
optisch-reflektierenden Sensor ausgestattet. Der Sensor besteht aus einem
Infrarot Sender und einem Fototransistor. Ausgabe des Sensors ist die Reflektivität
der Fläche.

Der Reflektivitätswert kann genutzt werden um Linien zu erkennen (Beispiel:
Eine schwarze Linie hat eine andere Reflektivität als ein weißer Hintergrund).
Das Line Bricklet kann aber auch genutzt werden um Entfernungen zu einer Fläche
zu messen, da das empfangene Licht mit steigender Entfernung abnimmt.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            CNY70
Stromverbrauch                    33mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         12Bit
Emitter-Wellenlänge               950nm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 9mm (0,98 x 0,59 x 0,35")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* CNY70 Datenblatt (`Download <https://github.com/Tinkerforge/line-bricklet/raw/master/datasheets/cny70.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/line-bricklet/raw/master/hardware/line-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/line_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/line-bricklet/zipball/master>`__)


.. _line_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die aktuell gemessene Reflektivität
angezeigt. Um das Bricklet zu testen kann dieses zum Beispiel über ein weißes
Blatt Papier mit schwarzen Streifen geführt werden.

.. image:: /Images/Bricklets/bricklet_line_brickv.jpg
   :scale: 100 %
   :alt: Line Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_line_brickv.jpg

|test_pi_ref|

Line Bricklet montieren
-----------------------

Um als Linien-Detektor verwendet werden zu können, muss das Bricklet mit einem
fixen Abstand zu Linie angebracht sein. Der richtige Abstand hängt von der
Reflektivität der Linie und des Untergrundes ab und kann durch Ausprobieren
ermittelt werden.

Im `Shop <https://www.tinkerforge.com/de/shop/mounting-plate-line-bricklet.html>`__
ist eine Montageplatte-Kit für das Line Bricklet verfügbar, das die Montage 
vereinfacht. Dieses besteht aus einer Montageplatte mit festem Abstand:


.. image:: /Images/Cases/bricklet_line_case1_tilted_350.jpg
   :scale: 100 %
   :alt: Line Bricklet Montageplatte Version 1
   :align: center
   :target: ../../_images/Cases/bricklet_line_case1_tilted_600.jpg

Und einer Montageplatte mit einstellbarem Abstand:

.. image:: /Images/Cases/bricklet_line_case2_tilted1_350.jpg
   :scale: 100 %
   :alt: Line Bricklet Montageplatte Version 2
   :align: center
   :target: ../../_images/Cases/bricklet_line_case2_tilted1_600.jpg




.. _line_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Line_hlpi.table
