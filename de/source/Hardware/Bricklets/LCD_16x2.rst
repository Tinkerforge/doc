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

Das LCD 16x2 :ref:`Bricklet <product_overview_bricklets>` ist mit einem 16x2
Zeichen Punktmatrix LCD Display, blauer Hintergrundbeleuchtung und drei Tastern
ausgestattet. Über einen :ref:`Bricks <product_overview_bricks>` der mit diesem
Bricklet verbunden ist kann es gesteuert werden. Die API ermöglicht es Zeichen
oder ganze Zeilen auf das LCD zu schreiben, den Status von jedem Taster
abzufragen und die Hintergrundbeleuchtung zu schalten. Zusätzlich können Events
definiert werden die durch die Taster ausgelöst werden.

Es kann genutzt werden um z.B. Song Informationen vom PC oder Messwerte anderer
Bricks/Bricklets anzuzeigen.


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

Teste dein LCD 16x2 Bricklet
----------------------------

Um das LCD 16x2 Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect the LCD 16x2 Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_lcd_16x2_master_600.jpg
   :scale: 100 %
   :alt: LCD 16x2 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "LCD 16x2 Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_lcd_16x2_brickv.jpg
   :scale: 100 %
   :alt: LCD 16x2 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_brickv.jpg

Input a string into the text field.
You can choose the line and the start position at which the text is displayed.
Press "Send Text" to display it. Press "Backlight On" to turn the backlight on.
Play around with the three on-board buttons and look how their values change.

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <lcd_16x2_programming_interfaces>` über das
API des LCD 16x2 Bricklets und Beispiele in verschiedenen
Programmiersprachen.


Change LCD's contrast
---------------------

To modify the contrast you have to
turn the potentiometer on the Bricklet with a screwdriver.
The potentiometer is attached next to the Bricklet connector.


.. _lcd_16x2_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: LCD_16x2_hlpi.table
