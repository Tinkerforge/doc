
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / RGB LED Bricklet
:FIXME_shoplink: ../../../shop/bricklets/rgb-led-bricklet.html

.. include:: RGB_LED.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_bricklet:

RGB LED Bricklet
================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_rgb_led_tilted_350.jpg",
	               "Bricklets/bricklet_rgb_led_tilted_600.jpg",
	               "RGB LED Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rgb_led_vertical_100.jpg",
	             "Bricklets/bricklet_rgb_led_vertical_600.jpg",
	             "RGB LED Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rgb_led_brickv_100.jpg",
	             "Bricklets/bricklet_rgb_led_brickv.jpg",
	             "RGB LED Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/rgb_led_bricklet_dimensions_100.png",
	             "Dimensions/rgb_led_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


.. _rgb_led_bricklet_description:

Beschreibung
------------

Mit dem RGB LED :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` eine eine RGB LED steuern. Jeder
Kanal der LED (rot, grün, blau) kann individuall mit 8 Bit
Auflösung gesteuert werden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
LED                               WS2812B
Stromverbrauch                    TBDmW (TBDmA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Lichstärke (R, G, B)              390-420mcd, 660-720mcd, 180-200mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0.98 x 0.79 x 0.19")*
Gewicht                           2g
================================  ============================================================

\*: Aufgrund einer Unachtsamkeit unsererseits hat das RGB LED Bricklet
mit Hardware Version 1.0 eine Grüße von 25 x 17.5 x 5mm (0.98 x 0.69 x 0.19")
und ist damit leider nicht auf dem 5mm-Raster. Dies wird mit Version
1.1 gefixt.

Ressourcen
----------

* WS2812B Datenblatt (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/raw/master/datasheets/WS2812B.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/raw/master/hardware/rgb-led-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rgb_led_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/zipball/master>`__)


.. _rgb_led_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|


.. image:: /Images/Bricklets/bricklet_rgb_led_brickv.png
   :scale: 100 %
   :alt: RGB LED Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_brickv.png

Wenn alles so funktioniert wie erwartet lässt sich die RGB LED jetzt
mit unterschiedlichen Schiebereglern steuern:

.. image:: /Images/Bricklets/bricklet_rgb_led_animation.gif
   :scale: 100 %
   :alt: RGB LED Bricklet Animation
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_animation.gif


|test_pi_ref|


.. _rgb_led_bricklet_case:

Gehäuse
-------

Commong soon...


.. _rgb_led_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RGB_LED_hlpi.table
