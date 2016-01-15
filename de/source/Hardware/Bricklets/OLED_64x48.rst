
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / OLED 64x48 Bricklet
:shoplink: ../../../shop/bricklets/oled-64x48-bricklet.html

.. include:: OLED_64x48.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _oled_64x48_bricklet:

OLED 64x48 Bricklet
===================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_oled_64x48_tilted_[?|?].jpg           OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_front_[?|?].jpg            OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_horizontal_[?|?].jpg       OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_bottom_[?|?].jpg           OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_brickv_[100|].jpg          OLED 64x48 Bricklet im Brick Viewer
	Bricklets/bricklet_oled_font_[100|314].png               OLED 64x48 Bricklet Zeichensatz
	Dimensions/oled_64x48_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Schwarz/Weiß OLED
* Größe von 1,68cm (0,66") mit 64x48 Auflösung


.. _oled_64x48_bricklet_description:

Beschreibung
------------

Mit dem OLED 64x48 :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Information auf einem kleinen 64x48
`OLED Display <https://de.wikipedia.org/wiki/Organische_Leuchtdiode>`__
anzeigen.

Da jedes Pixel einzeln gesetzt werden kann, ist das Display grafikfähig
und ermöglicht so vielseitigere und detailliertere Anzeigen als z.B. das
:ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` mit seiner festen Zeichenanzeige.

Zusätzlich kann mit dem eingebetteten :ref:`Zeichensatz
<oled_64x48_bricklet_font>` des Bricklets aber auch schnell und einfach Text
auf dem Display angezeigt werden.

Hohe Update-Raten bis zu 100Hz sind möglich.

Eine `Demo <https://github.com/Tinkerforge/oled-128x64-bricklet/blob/master/software/examples/python/example_draw_servo_poti.py>`__
der 128x64 Pixel Version zusammen mit einem Servo Brick und einem Rotary Poti
Bricklet ist auf Youtube verfügbar:

.. raw:: html

 <center><iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/8RSEs6cKwXc" frameborder="0" allowfullscreen></iframe></center>

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    | 10mW (2mA bei 5V, alle Pixel schwarz)
                                  | 110mW (22mA bei 5V, alle Pixel weiß)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         64x48 Pixel, 13x6 Zeichen
Größe                             1,68cm (0,66")
Farben                            Schwarz/Weiß
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             35 x 20 x 7mm (1,38 x 0,79 x 0,28")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* Display Datenblatt (`Download <https://github.com/Tinkerforge/oled-64x48-bricklet/raw/master/datasheets/OLED_64X48_Datasheet.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/oled-64x48-bricklet/raw/master/hardware/temperature-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/oled_64x48_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/oled-64x48-bricklet/zipball/master>`__)

.. _oled_64x48_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

Im Brick Viewer kann auf dem Display freihand gezeichnet und Text angezeigt
werden. Mit einem Schieberegler kann der verfügbare Zeichensatz durchgescrollt
werden.

.. image:: /Images/Bricklets/bricklet_oled_64x48_brickv.jpg
   :scale: 100 %
   :alt: OLED 64x48 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_oled_64x48_brickv.jpg

|test_pi_ref|

Benutzung
---------

Bricklets haben leider nur eine kleine Menge an RAM (256 Byte) und Flash
(4096 Byte) zur Verfügung. Dies ist ist nicht genug um zum Beispiel ein
64x48 schwarz/weiß Bild zwischenzuspeichern. Daher können wir keine
konfortablen APIs wie ``draw_line(x1, y1, x2, y2)`` anbieten.

Um auf das OLED Display zu zeichnen empfehlen wir eine Image Library
zu nutzen die für eine spezifische Programmiersprache entwickelt wurde
(zum Beispiel PIL für Python). Dadurch können die Zeichen-Primitiven der
und Schriftarten der Library verwendet werden und das fertig gezeichnete
Bild kann dann zum Bricklet übertragen werden.

Wir haben Beispiele für

* `C# <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/csharp/ExampleScribble.cs>`__,
* `Java <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/java/ExampleScribble.java>`__,
* `JavaScript (Node.js) <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/javascript/ExampleScribble.js>`__
  (mit `gm <https://www.npmjs.com/package/gm>`__ und `get-pixels <https://www.npmjs.com/package/get-pixels>`__) und
* `Python <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/python/example_scribble.py>`__
  (mit `PIL <https://python-pillow.github.io/>`__).

.. _oled_64x48_bricklet_font:

Zeichensatz
-----------

Das Bricklet beinhaltet folgenden Zeichensatz (ASCII ist grün markiert), mit
dem schnell und einfach Text (bis zu 13x6 Zeichen) auf dem Display angezeigt
werden kann:

.. image:: /Images/Bricklets/bricklet_oled_font.png
   :scale: 100 %
   :alt: OLED 64x48 Bricklet Zeichensatz
   :align: center
   :target: ../../_images/Bricklets/bricklet_oled_font.png


.. _oled_64x48_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: OLED_64x48_hlpi.table
