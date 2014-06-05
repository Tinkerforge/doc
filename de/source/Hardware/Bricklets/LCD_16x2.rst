
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / LCD 16x2 Bricklet

.. include:: LCD_16x2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _lcd_16x2_bricklet:

LCD 16x2 Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_lcd_16x2_tilted_350.jpg",
	               "Bricklets/bricklet_lcd_16x2_tilted_600.jpg",
	               "LCD 16x2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_apart_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_apart_600.jpg",
	             "LCD 16x2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_display_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_display_600.jpg",
	             "LCD 16x2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_master_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_master_600.jpg",
	             "LCD 16x2 Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_brickv_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_brickv.jpg",
	             "LCD 16x2 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/lcd_16x2_bricklet_dimensions_100.png",
	             "Dimensions/lcd_16x2_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 16x2 Zeichen alphanumerisches Display
* Schaltbare blaue Hintergrundbeleuchtung
* 3 Taster


Beschreibung
------------

Das LCD 16x2 :ref:`Bricklet <primer_bricklets>` ist mit einem 16x2
Zeichen Punktmatrix LCD Display, blauer Hintergrundbeleuchtung und drei Tastern
ausgestattet. Über einen :ref:`Bricks <primer_bricks>` der mit diesem
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
LCD                                           Alphanumerisch, 16 Zeichen per Zeile, 2 Zeilen
Stromverbrauch mit Hintergrundbeleuchtung     28mA
--------------------------------------------  ------------------------------------------------------------
--------------------------------------------  ------------------------------------------------------------
Hintergrundbeleuchtung                        Blau, per Software schaltbar
Kontrast                                      Einstellbar per Potentiometer
--------------------------------------------  ------------------------------------------------------------
--------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                       31 x 80 x 22mm (1,22 x 3,15 x 0,86")*
Gewicht                                       51g*
============================================  ============================================================

\* ohne Schrauben


Ressourcen
----------

* LCD Zeichensatz (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/standard_charset.pdf>`__)
* LCD Datenblatt (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/el1602a.pdf>`__)
* KS0066U Datenblatt (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 Datenblatt (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/hardware/lcd-16x2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/lcd_16x2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/zipball/master>`__)


.. _lcd_16x2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_lcd_16x2_master_600.jpg
   :scale: 100 %
   :alt: LCD 16x2 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_lcd_16x2_brickv.jpg
   :scale: 100 %
   :alt: LCD 16x2 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_brickv.jpg

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


.. _lcd_16x2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: LCD_16x2_hlpi.table
