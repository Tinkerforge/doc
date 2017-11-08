:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RGB LED Matrix Bricklet
:FIXME_shoplink: ../../../shop/bricklets/rgb-led-matrix-bricklet.html

.. include:: RGB_LED_Matrix.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_matrix_bricklet:

RGB LED Matrix Bricklet
=======================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_matrix_tilted_[?|?].jpg           RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_horizontal_[?|?].jpg       RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_master_[100|600].jpg       RGB LED Matrix Bricklet mit Master Brick
	Cases/bricklet_rgb_led_matrix_case_[100|600].jpg             RGB LED Matrix Bricklet im Gehäuse
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

Eine externe 5V Versorgung ist notwendig und muss an der Anschlussklemme des Bricklets
angeschlossen werden. Die LEDs können nicht über den Brickletanschluss versorgt werden.


Technische Spezifikation
------------------------

================================  =============================================================
Eigenschaft                       Wert
================================  =============================================================
Stromverbrauch                    TBDmA
--------------------------------  -------------------------------------------------------------
--------------------------------  -------------------------------------------------------------
Matrix-Größe                      8x8
LED Auflösung                     8-Bit

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
* 3D Modell (`Online ansehen <http://autode.sk/2xZlMJ4>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led_matrix/rgb-led-matrix.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led_matrix/rgb-led-matrix.FCStd>`__)


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


.. _rgb_led_matrix_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das RGB LED Matrix Bricklet 
	<https://www.tinkerforge.com/de/shop/cases/case-rgb-led-matrix-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_rgb_led_matrix_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für RGB LED Matrix Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_rgb_led_matrix_case_1000.jpg

	.. include:: RGB_LED_Matrix.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/rgb_led_matrix_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für RGB LED Matrix Bricklet
	   :align: center
	   :target: ../../_images/Exploded/rgb_led_matrix_exploded.png

	|bricklet_case_hint|


.. _rgb_led_matrix_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RGB_LED_Matrix_hlpi.table
