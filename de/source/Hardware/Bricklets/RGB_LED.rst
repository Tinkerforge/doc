
:shoplink: ../../../shop/bricklets/rgb-led-bricklet.html

.. include:: RGB_LED.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_bricklet:

RGB LED Bricklet
================

Features
--------

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_tilted_[?|?].jpg           RGB LED Bricklet
	Bricklets/bricklet_rgb_led_vertical_[?|?].jpg         RGB LED Bricklet
	Bricklets/bricklet_rgb_led_brickv_[100|].png          RGB LED Bricklet im Brick Viewer
	Dimensions/rgb_led_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das RGB LED Bricklet ist abgekündigt. Wir verkaufen noch unseren restlichen Lagerbestand.
 Als Ersatz wird das :ref:`RGB LED Bricklet 2.0 <rgb_led_v2_bricklet>`
 empfohlen.


Features
--------

* 1x RGB LED
* 24 Bit Farbauflösung

.. _rgb_led_bricklet_description:

Beschreibung
------------

Mit dem RGB LED :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` eine eine RGB LED steuern. Jeder
Kanal der LED (rot, grün, blau) kann individuell mit 8 Bit
Auflösung gesteuert werden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
LED                               WS2812B
Stromverbrauch                    | Schwarz: 25mW (5mA bei 5V)
                                  | Weiß: 225mW (45mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Lichtstärke (R, G, B)             390-420mcd, 660-720mcd, 180-200mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0,98 x 0,79 x 0,19")*
Gewicht                           2g
================================  ============================================================

\* Aufgrund einer Unachtsamkeit unsererseits hat das RGB LED Bricklet
mit Hardware Version 1.0 eine Größe von 25 x 17.5 x 5mm (0.98 x 0.69 x 0.19")
und war damit leider nicht auf dem 5mm-Raster. Dies wurde mit Version
1.1 gefixt.

Ressourcen
----------

* WS2812B Datenblatt (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/raw/master/datasheets/WS2812B.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/raw/master/hardware/rgb-led-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rgb_led_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2iW4cAV>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/rgb_led/rgb-led.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/rgb_led/rgb-led.FCStd>`__)


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

Coming soon...


.. _rgb_led_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RGB_LED_hlpi.table
