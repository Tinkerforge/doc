
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Dual Button Bricklet
:FIXME_shoplink: ../../../shop/bricklets/dual-button-bricklet.html

.. include:: Dual_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _dual_button_bricklet:

Dual Button Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_dual_button_tilted_350.jpg",
	               "Bricklets/bricklet_dual_button_tilted_600.jpg",
	               "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_vertical_100.jpg",
	             "Bricklets/bricklet_dual_button_vertical_600.jpg",
	             "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_horizontal_100.jpg",
	             "Bricklets/bricklet_dual_button_horizontal_600.jpg",
	             "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_tilted_back_100.jpg",
	             "Bricklets/bricklet_dual_button_tilted_back_600.jpg",
	             "Dual Button Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_button_brickv_100.jpg",
	             "Bricklets/bricklet_dual_button_brickv.jpg",
	             "Dual Button Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dual_button_bricklet_dimensions_100.png",
	             "Dimensions/dual_button_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Zwei Taster mit eingebauten blauen LEDs
* Auto-Toggle der LEDs möglich

Beschreibung
------------

Das Dual Button :ref:`Bricklet <product_overview_bricklets>` ist mit zwei
Drucktastern ausgestattet. Beide Taster haben eine eingebaute blaue LED. Der
aktuelle Zustand der Taster (gedrückt/nicht gedrückt) und der LEDs (an/aus) kann
jederzeit ausgelesen werden. Es ist möglich die LEDs selbst an/aus zu schalten
sowie Auto-Toggle zu aktivieren. Im Auto-Toggle Modus werden die LEDs
automatisch bei jedem Tastendruck umgeschaltet.

Es ist auch möglich Events zu nutzen. Dadurch kann auf einen
Tastendruck reagiert werden ohne zu pollen.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Taster Typ                        Drucktaster mit LED
Taster Betätigungskraft           150gf
Taster Bewegungsdistanz           2,5mm
LED Farbe                         Blau
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 20 x 10mm (1,77 x 0,79 x 0,39")
Gewicht                           6g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/dual-button-bricklet/raw/master/hardware/dual-button-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_button_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-button-bricklet/zipball/master>`__)


.. _dual_button_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun Tastendrücke beobachtet 
werden sowie die Zustände der LEDs verändert werden.

.. image:: /Images/Bricklets/bricklet_dual_button_brickv.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_brickv.jpg

|test_pi_ref|


.. _dual_button_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Dual_Button_hlpi.table
