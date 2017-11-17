:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RGB LED Button Bricklet
:FIXME_shoplink: ../../../shop/bricklets/rgb-led-button-bricklet.html

.. include:: RGB_LED_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_button_bricklet:

RGB LED Button Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_button_tilted_[?|?].jpg           RGB LED Button Bricklet
	Bricklets/bricklet_rgb_led_button_bottom_[?|?].jpg           RGB LED Button Bricklet oben
	Bricklets/bricklet_rgb_led_button_top_[?|?].jpg              RGB LED Button Bricklet unten
	Bricklets/bricklet_rgb_led_button_finger_[?|?].jpg           RGB LED Button Bricklet mit Finger
	Bricklets/bricklet_rgb_led_button_brickv_[100|].jpg          RGB LED Button Bricklet im Brick Viewer
	Dimensions/rgb_led_button_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Shopeintrag sowie Brick Viewer und Bindings Support für das RGB LED Button Bricklet
 werden spätestens am Dienstag den 21. November veröffentlicht. Wir bitten um ein
 wenig Geduld.

Features
--------

* Qualitativer 15x15mm Taster
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


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
LED Auflösung                     8 bit
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
* 3D Modell (`Online ansehen <http://autode.sk/2zqJEtU>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led_button/rgb-button-bricklet.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led_button/rgb-button-bricklet.FCStd>`__)

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

Folgt in Kürze...

..
	Ein `laser-geschnittenes Gehäuse für das RGB LED Button Bricklet 
	<https://www.tinkerforge.com/de/shop/cases/case-rgb-led-button-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_rgb_led_button_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für RGB LED Button Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_rgb_led_button_case_1000.jpg

	.. include:: RGB_LED_Button.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

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
