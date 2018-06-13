
:shoplink: ../../../shop/bricklets/rgb-led-button-bricklet.html

.. include:: RGB_LED_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_button_bricklet:

RGB LED Button Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_button_tilted_[?|?].jpg           RGB LED Button Bricklet
	Bricklets/bricklet_rgb_led_button_bottom_[?|?].jpg           RGB LED Button Bricklet oben
	Bricklets/bricklet_rgb_led_button_top_[?|?].jpg              RGB LED Button Bricklet unten
	Bricklets/bricklet_rgb_led_button_finger_[?|?].jpg           RGB LED Button Bricklet mit Finger
	Bricklets/bricklet_rgb_led_button_brickv_[100|].jpg          RGB LED Button Bricklet im Brick Viewer
	Dimensions/rgb_led_button_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Qualitativ hochwertiger 15x15mm Taster
* Einstellbare RGB LED Hintergrundbeleuchtung
* Austauschbares/bedruckbares Tasterinnenteil


.. _rgb_led_button_bricklet_description:

Beschreibung
------------


Das RGB LED :ref:`Bricklet <primer_bricklets>` ist mit einem Taster ausgestattet,
dessen Hintergrundbeleuchtung per Software gesteuert werden kann.
Das Bricklet erweitert :ref:`Bricks <primer_bricks>`.

Der Zustand der Tasters (gedrückt, nicht gedrückt) kann ausgelesen werden und die 
Farbe der LED kann gesteuert werden. Der Rot-, Grün- und Blauanteil der LED
kann jeweils mit 8 Bit Auflösung gesteuert werden.

Ein weißes Innenteil liegt unter der Tasterkappe. Dieses Innenteil kann
durch ein eigenes gedrucktes Papier-Innenteil ausgetauscht werden. Somit kann der
Taster zum Beispiel mit einem Pfeil oder ähnliches beschriftet werden.

Um nicht den Zustand des Tasters dauernd abfragen zu müssen (pollen) können
auch Event genutzt werden.

Das RGB LED Button Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_rgb_led_button_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_rgb_led_button_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_rgb_led_button_video.webm" type="video/webm">
	</video> 

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch (LEDs aus)         31mW (6,2mA bei 5V)
Stromverbrauch (LEDs an)          207mW (41,4mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
LED Auflösung                     8 Bit pro Kanal
Einlagengröße (Beschriftung)      14 x 14mm
Tastergröße                       15 x 15mm
Kappengröße                       17,4 x 17,4mm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 30mm (0,98 x 0,98 x 1,18")
Gewicht                           7g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rgb-led-button-bricklet/raw/master/hardware/rgb-led-button-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rgb_led_button_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rgb-led-button-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BUxGXm>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led_button/rgb-led-button.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led_button/rgb-led-button.FCStd>`__)

Taster-Knopfbeschriftung
------------------------

Das RGB LED Button Bricklet besteht aus vier Teilen:

* Bricklet mit Taster und RGB LED,
* Weißes Kappeninnenteil,
* Kappeneinlage (optional, 14x14mm) und
* Transparente Kappe.

.. image:: /Images/Bricklets/bricklet_rgb_led_button_disassembled_800.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklet zerlegt
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_disassembled_1200.jpg

Es können sehr einfach eigene Kappeneinlagen hergestellt werden. Zum Beispiel können Symbole
mit einem Drucker auf eine durchsichtige Folie gedruckt werden. Die Einlage sollte eine Größe
von 14x14mm haben und zwischen dem weißen Kappeninnenteil und der transparenten Kappe gelegt werden.

Anstatt einer Folie kann natürlich auch einfaches Papier verwendet werden, dies
beeinflusst aber die LED Helligkeit ein wenig.

Im nachfolgenden Foto haben wir drei verschiedene RGB LED Button Bricklets mit drei verschiedenen
Einlagen einmal bei Umgebungslicht und einmal bei Dunkelheit abgebildet. Die Symbole wurden auf
eine Folie mittels Laserdrucker gedruckt.

.. image:: /Images/Bricklets/bricklet_rgb_led_button_3on_bright_600.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklets mit Einlagen
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_3on_bright_1000.jpg

.. image:: /Images/Bricklets/bricklet_rgb_led_button_3on_dark_600.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklets mit Einlagen in Dunkelheit
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_3on_dark_1000.jpg




.. _rgb_led_button_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun in der GUI die Farbe der Hintergrundbeleuchtung
eingestellt und der Zustand des Tasters abgelesen werden.

.. image:: /Images/Bricklets/bricklet_rgb_led_button_brickv.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_brickv.jpg

|test_pi_ref|


.. _rgb_led_button_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das RGB LED Button Bricklet 
<https://www.tinkerforge.com/de/shop/cases/case-rgb-led-button-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_rgb_led_button_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für RGB LED Button Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rgb_led_button_case_built_up_800.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube 2x10mm Abstandshalter und Unterseite des Bricklets,
* schraube Unterteil an Abstandshalter,
* schraube 2x9mm und 1x10mm Abstandshalter an Unterteil,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Unterteil und
* schraube Oberteil auf obere Abstandshalter.

Im Folgenden befindet sich eine Explosionszeichnung des RGB LED Button Bricklet Gehäuses:

.. image:: /Images/Exploded/rgb_led_button_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für RGB LED Button Bricklet
   :align: center
   :target: ../../_images/Exploded/rgb_led_button_exploded.png

|bricklet_case_hint|


.. _rgb_led_button_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RGB_LED_Button_hlpi.table
