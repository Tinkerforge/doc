
:shoplink: ../../../shop/bricklets/rgb-led-v2-bricklet.html

.. include:: RGB_LED_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_v2_bricklet:

RGB LED Bricklet 2.0
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_v2_tilted_[?|?].jpg           RGB LED Bricklet 2.0
	Bricklets/bricklet_rgb_led_v2_top_[?|?].jpg              RGB LED Bricklet 2.0
	Bricklets/bricklet_rgb_led_v2_bright_vs_dark_[?|?].jpg   RGB LED Bricklet 2.0
	Bricklets/bricklet_rgb_led_v2_brickv_[100|].jpg          RGB LED Bricklet 2.0 im Brick Viewer
	Dimensions/rgb_led_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 1x RGB LED
* 24 Bit Farbauflösung
* Leuchtkraft wird für menschliche Lichtempfindleichkeit korrigiert (CIE 1931)


.. _rgb_led_v2_bricklet_description:

Beschreibung
------------

Mit dem RGB LED :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` eine RGB LED steuern. Jeder
Kanal der LED (rot, grün, blau) kann individuell mit 8 Bit
Auflösung gesteuert werden.

Die Leuchtkraft der LED wird automatisch für die menschliche Lichtempfindleichkeit
nach CIE 1931 korrigiert. Das bedeutet, dass jeder Wechsel einer Farbe von aus
zu voller Helligkeit für das menschliche Auge wie ein gleichmäßiger Farbverlauf
erscheint.

Das RGB LED Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="400px" height="auto" controls loop>
	  <source src="../../_images/Videos/bricklet_rgb_led_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_rgb_led_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_rgb_led_v2_video.webm" type="video/webm">
	</video>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
LED                               QBLP679E-RGB
Stromverbrauch                    | Aus: 35mW (7mA bei 5V)
                                  | Weiß: 180mW (36mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Lichtstärke (R, G, B)             400-630mcd, 1000-1500mcd, 200-285mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Gewicht                           3g
================================  ============================================================


Ressourcen
----------

* QBLP679E-RGB Datenblatt (`Download <https://github.com/Tinkerforge/rgb-led-v2-bricklet/raw/master/datasheets/QBLP679E-RGB.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/rgb-led-v2-bricklet/raw/master/hardware/rgb-led-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rgb_led_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rgb-led-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/30ouYWQ>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/rgb_led_v2/rgb-led-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/rgb_led_v2/rgb-led-v2.FCStd>`__)


.. _rgb_led_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles so funktioniert wie erwartet lässt sich die RGB LED jetzt
mit unterschiedlichen Schiebereglern steuern:

.. image:: /Images/Bricklets/bricklet_rgb_led_v2_brickv.jpg
   :scale: 100 %
   :alt: RGB LED Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_v2_brickv.jpg

|test_pi_ref|



.. _rgb_led_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RGB_LED_V2_hlpi.table
