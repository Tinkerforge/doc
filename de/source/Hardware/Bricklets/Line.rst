
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Line Bricklet
:FIXME_shoplink: ../../../shop/bricklets/line-bricklet.html

.. include:: Line.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _line_bricklet:

Line Bricklet
====================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

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
	    tfdocimg("Bricklets/bricklet_line_master_100.jpg",
	             "Bricklets/bricklet_line_master_600.jpg",
	             "Line Bricklet mit Master Brick")
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

* Misst die Reflektivität einer Fläche
* Kann genutzt werden um Linien zu erkennen/zu folgen
* Kann genutzt werden um Entfernungen von ~0-10mm zu messen

Beschreibung
------------

Das Line Bricklet ist mit einem optisch-reflektierenden Sensor ausgestattet.
Der Sensor besteht aus einem Infrarot Sender und Fototransistor. Ausgabe des
Sensors ist die Reflektivität der Fläche.

Der Reflektivitätswert kann genutzt werden um Linien zu erkennen (Beispiel:
Eine schwarze Linie hat eine andere Reflektivität als ein weißer Hintergrund).

Das Line Bricklet kann auch genutzt werden um Entfernungen zu einer Fläche
zu messen, da die Reflektivität mit steigender Entfernung abnimmt.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Auflösung                         12 Bit
Emitter-Wellenlänge               950nm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 9mm (0,98 x 0,59 x 0,35")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/line-bricklet/raw/master/hardware/line-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/line_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/line-bricklet/zipball/master>`__)


.. _line_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_line_master_600.jpg
   :scale: 100 %
   :alt: Line Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_line_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die aktuell gemessene Reflektivität
angezeigt.

.. image:: /Images/Bricklets/bricklet_line_brickv.jpg
   :scale: 100 %
   :alt: Line Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_line_brickv.jpg

|test_pi_ref|


.. _line_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Line_hlpi.table
