.. include:: LCD_20x4.substitutions


.. _lcd_20x4_bricklet:

LCD 20x4 Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_lcd_20x4_tilted_350.jpg",
	               "Bricklets/bricklet_lcd_20x4_tilted_600.jpg",
	               "LCD 20x4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_20x4_apart_100.jpg",
	             "Bricklets/bricklet_lcd_20x4_apart_600.jpg",
	             "LCD 20x4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_20x4_display_100.jpg",
	             "Bricklets/bricklet_lcd_20x4_display_600.jpg",
	             "LCD 20x4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_20x4_master_100.jpg",
	             "Bricklets/bricklet_lcd_20x4_master_600.jpg",
	             "LCD 20x4 Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_20x4_brickv_100.jpg",
	             "Bricklets/bricklet_lcd_20x4_brickv.jpg",
	             "LCD 20x4 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/lcd_20x4_bricklet_dimensions_100.png",
	             "Dimensions/lcd_20x4_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 20x4 Zeichen alphanumerisches Display
* Schaltbare blaue Hintergrundbeleuchtung
* 3 Taster


Beschreibung
------------

Das LCD 20x4 :ref:`Bricklet <product_overview_bricklets>` ist mit einem 20x4
Zeichen Punktmatrix LCD Display, blauer Hintergrundbeleuchtung und drei Tastern
ausgestattet. Über einen :ref:`Bricks <product_overview_bricks>` der mit diesem
Bricklet verbunden ist kann es gesteuert werden. Die API ermöglicht es Zeichen
oder ganze Zeilen auf das LCD zu schreiben, den Status von jedem Taster
abzufragen und die Hintergrundbeleuchtung zu schalten. Zusätzlich können Events
definiert werden die durch die Taster ausgelöst werden.

Es kann genutzt werden um z.B. Song Informationen vom PC oder Messwerte anderer
Bricks und Bricklets anzuzeigen.


Technische Spezifikation
------------------------

============================================  ============================================================
Eigenschaft                                   Wert
============================================  ============================================================
LCD                                           Alphanumerisch, 20 Zeichen per Zeile, 4 Zeilen
Stromverbrauch mit Hintergrundbeleuchtung     36mA
--------------------------------------------  ------------------------------------------------------------
--------------------------------------------  ------------------------------------------------------------
Hintergrundbeleuchtung                        Blau, per Software schaltbar
Kontrast                                      Einstellbar per Potentiometer
--------------------------------------------  ------------------------------------------------------------
--------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                       60 x 98 x 22mm (2,36 x 3,86 x 0,86")*
Gewicht                                       96g*
============================================  ============================================================

\* ohne Schrauben


Ressourcen
----------

* LCD Zeichensatz (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/standard_charset.pdf>`__)
* KS0066U Datenblatt (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 Datenblatt (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/hardware/lcd-20x4-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/lcd_20x4_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/zipball/master>`__)


.. _lcd_20x4_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_lcd_20x4_master_600.jpg
   :scale: 100 %
   :alt: LCD 20x4 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_20x4_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_lcd_20x4_brickv.jpg
   :scale: 100 %
   :alt: LCD 20x4 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_20x4_brickv.jpg

Um Text anzuzeigen muss dieser in das Textfeld eingegeben werden. Die Zeile und
die Spalte in der der Text angezeigt werden soll kann verändert werden. Ein Klick
auf den "Send Text" Knopf zeigt den Text auf dem LCD an. Ein weitere Klick auf
den "Backlight On" Knopf schaltet die Hintergrundbeleuchtung ein.
Werden die 3 Knöpfe am Bricklet gedrückt so wird dies angezeigt.

|test_pi_ref|


LCD Kontrast einstellen
-----------------------

Auf dem Bricklet befindet sich neben dem Bricklet Stecker ein Potentiometer.
Mit diesem kann der Kontrast des LCDs eingestellt werden.


.. _lcd_20x4_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: LCD_20x4_hlpi.table
