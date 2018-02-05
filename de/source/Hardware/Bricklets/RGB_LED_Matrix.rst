
:shoplink: ../../../shop/bricklets/rgb-led-matrix-bricklet.html

.. include:: RGB_LED_Matrix.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_matrix_bricklet:

RGB LED Matrix Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_matrix_tilted_[?|?].jpg           RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_w_cable_[?|?].jpg          RGB LED Matrix Bricklet mit Kabel
	Bricklets/bricklet_rgb_led_matrix_rainbow_[?|?].jpg          RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_horizontal_[?|?].jpg       RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_detail_[?|?].jpg           RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_w_power_[?|?].jpg          RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_brickv_[100|].jpg          RGB LED Matrix Bricklet im Brick Viewer
	Dimensions/rgb_led_matrix_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 8x8 RGB LED Matrix
* Jedes Pixel kann einzeln gesteuert werden
* Jedes Pixel besitzt 8-Bit Auflösung für rot, grün und blau
* Eingangsspannung kann überwacht werden


.. _rgb_led_matrix_bricklet_description:

Beschreibung
------------

Das RGB LED Matrix :ref:`Bricklet <primer_bricklets>` ist mit einer 8x8 RGB LED Matrix
ausgestattet. Es erweitert :ref:`Bricks <primer_bricks>`.

Der Rot-, Grün- und Blau-Wert jeder LED kann einzeln mit einer Auflösung von
8-Bit gesteuert werden.

Es kann eine maximale Framerate von 120 Hz erreicht werden. Die Frames können mit einer
festen Framerate gesendet werden um gleichmäßige Animationen zu erlauben. Frames verfügen
über einen Double-Buffer um die Performance zu steigern und ein Flackern zu verhindern.

Das Bricklet wird mit einem 15cm Anschlusskabel geliefert. Über das Kabel
muss eine externe 5V Versorgung angeschlossen werden. 
Die LEDs können nicht über den Brickletanschluss versorgt werden.

Das RGB LED Matrix Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_rgb_led_matrix_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_rgb_led_matrix_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_rgb_led_matrix_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  =============================================================
Eigenschaft                       Wert
================================  =============================================================
Stromverbrauch                    39mW (7,8mA bei 5V) zuzüglich externer 5V Eingang für LEDs
--------------------------------  -------------------------------------------------------------
--------------------------------  -------------------------------------------------------------
Matrix-Größe                      8x8
LED Auflösung                     8-Bit pro Kanal
Kabellänge                        15cm

Eingangsspannung                  5V
Maximaler Eingangsstrom           Jede RGB LED kann bis zu 20mA pro Farbe verbrauchen, dies
                                  führt zu maximal 3,83A, wenn alle LEDs auf weiß gesetzt werden
--------------------------------  -------------------------------------------------------------
--------------------------------  -------------------------------------------------------------
Abmessungen (B x T x H)           75 x 55 x 14mm (2.95 x 2.17 x 0.55")
Gewicht                           23g
================================  =============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rgb-led-matrix-bricklet/raw/master/hardware/rgb-led-matrix-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rgb_led_matrix_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rgb-led-matrix-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BeekiV>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led_matrix/rgb-led-matrix.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led_matrix/rgb-led-matrix.FCStd>`__)


.. _rgb_led_matrix_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| und eine 5V Stromversorgung muss an die RGB LED Matrix Bricklet Schraubklemme angeschlossen werden.

|test_tab|
Wenn alles wie erwartet funktioniert können nun die LEDs des Bricklets gesteuert werden.

.. image:: /Images/Bricklets/bricklet_rgb_led_matrix_brickv.jpg
   :scale: 100 %
   :alt: RGB LED Matrix Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_matrix_brickv.jpg

|test_pi_ref|


.. _rgb_led_matrix_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RGB_LED_Matrix_hlpi.table
