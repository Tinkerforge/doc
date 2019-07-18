
:shoplink: ../../../shop/bricklets/lcd20x4-bricklet.html

.. include:: LCD_20x4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _lcd_20x4_bricklet:

LCD 20x4 Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_lcd12_20x4_tilted_[?|?].jpg         LCD 20x4 Bricklet
	Bricklets/bricklet_lcd12_20x4_top_[?|?].jpg            LCD 20x4 Bricklet
	Bricklets/bricklet_lcd_20x4_display_[100|600].jpg      LCD 20x4 Bricklet
	Bricklets/bricklet_lcd_20x4_master_[100|600].jpg       LCD 20x4 Bricklet mit Master Brick
	Cases/bricklet_lcd_20x4_case_[100|600].jpg             LCD 20x4 Bricklet im Gehäuse
	Bricklets/bricklet_lcd_20x4_brickv_[100|].jpg          LCD 20x4 Bricklet im Brick Viewer
	Dimensions/lcd_20x4_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 20x4 Zeichen alphanumerisches Display
* Schaltbare blaue Hintergrundbeleuchtung
* 4 Taster


.. _lcd_20x4_bricklet_description:

Beschreibung
------------

Das LCD 20x4 :ref:`Bricklet <primer_bricklets>` ist mit einem 20x4
Zeichen Punktmatrix LCD Display, blauer Hintergrundbeleuchtung und vier Tastern
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
* 3D Modell (`Online ansehen <https://autode.sk/2BeYMM8>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/lcd_20x4/lcd-20x4.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/lcd_20x4/lcd-20x4.FCStd>`__)


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
Werden die 4 Knöpfe am Bricklet gedrückt so wird dies angezeigt.

|test_pi_ref|


LCD Kontrast einstellen
-----------------------

Auf dem Bricklet befindet sich neben dem Bricklet Stecker ein Potentiometer.
Mit diesem kann der Kontrast des LCDs eingestellt werden.


Externe Taster anschließen
--------------------------

Das LCD Bricklet kann auf der rechten Seite mit einer Stiftleiste bestückt
werden. Über diese können externe Schalter oder Taster
angeschlossen werden. Normalerweise verbindet man jeweils einen Eingang
(BTN0 bis BTN3) über einen Taster oder Schalter mit GND.

.. _lcd_20x4_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das LCD 20x4 Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-lcd20x4-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_lcd_20x4_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_lcd_20x4_case_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Befestige die langen Schrauben mit den mitgelieferten Muttern am Oberteil,
* Schraube LCD an Oberteil mit Abstandshalter (10mm) von unten und den langen Schrauben von oben,
* Schraube Bricklet an LCD mit Abstandshalter (12mm)
* baue Seitenteile auf,
* stecke Taster-Verlängerung in Seitenteil,
* stecke zusammengebaute Seitenteile in Oberteil und
* schraube Unterteil auf unteren Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des LCD 20x4 Bricklet-Gehäuse:

.. image:: /Images/Exploded/lcd20x4_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Exploded/lcd20x4_exploded.png

|bricklet_case_hint|


.. _lcd_20x4_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: LCD_20x4_hlpi.table
