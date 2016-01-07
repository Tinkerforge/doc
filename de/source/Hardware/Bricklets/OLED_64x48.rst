
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / OLED 64x48 Bricklet
:shoplink: ../../../shop/bricklets/oled-64x48-bricklet.html

.. include:: OLED_64x48.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _oled_64x48_bricklet:

OLED 64x48 Bricklet
===================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_oled_64x48_tilted_350.jpg",
	               "Bricklets/bricklet_oled_64x48_tilted_600.jpg",
	               "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_front_100.jpg",
	             "Bricklets/bricklet_oled_64x48_front_600.jpg",
	             "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_horizontal_100.jpg",
	             "Bricklets/bricklet_oled_64x48_horizontal_600.jpg",
	             "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_bottom_100.jpg",
	             "Bricklets/bricklet_oled_64x48_bottom_600.jpg",
	             "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_brickv_100.jpg",
	             "Bricklets/bricklet_oled_64x48_brickv.jpg",
	             "OLED 64x48 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_font_100.png",
	             "Bricklets/bricklet_oled_font_314.png",
	             "OLED 64x48 Bricklet Zeichensatz")
	}}
	{{
	    tfdocimg("Dimensions/oled_64x48_bricklet_dimensions_100.png",
	             "Dimensions/oled_64x48_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Schwarz/Weiß OLED
* Größe von 0,66" mit 64x48 Auflösung


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

Eine Demo der 128x64 Pixel Version zusammen mit einem Servo Brick und einem
Rotary Poti Bricklet ist auf Youtube verfügbar:

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
Größe                             0,66"
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
