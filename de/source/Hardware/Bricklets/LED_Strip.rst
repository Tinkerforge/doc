
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / LED Strip Bricklet
:FIXME_shoplink: ../../../shop/bricklets/led-strip-bricklet.html

.. include:: LED_Strip.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _led_strip_bricklet:

LED Strip Bricklet
==================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_led_strip_tilted_350.jpg",
	               "Bricklets/bricklet_led_strip_tilted_600.jpg",
	               "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_vertical_100.jpg",
	             "Bricklets/bricklet_led_strip_vertical_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_horizontal_100.jpg",
	             "Bricklets/bricklet_led_strip_horizontal_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_master_100.jpg",
	             "Bricklets/bricklet_led_strip_master_600.jpg",
	             "LED Strip Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_brickv_100.jpg",
	             "Bricklets/bricklet_led_strip_brickv.jpg",
	             "LED Strip Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/led_strip_bricklet_dimensions_100.png",
	             "Dimensions/led_strip_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Schaltet bis zu 960 LEDs (320 RGB LEDs)
* Alle LEDs können unabhängig voneinander geschaltet werden
* Aktualisierungsrate von bis zu 100Hz für jede LED möglich

Beschreibung
------------

Das LED Strip Bricklet kann genutzt werden um LED Strips zu steuern
die mit einem WS2801 LED-Treiber ausgestattet sind. Es ist möglich
960 LEDs unabhängig voneinander zu schalten.

Mit Hilfe der API können alle LEDs gleichzeitig mit einer festen
Aktualisierungsrate von bis zu 100Hz gesteuert werden.

TODO: Video

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Unterstützer LED-Treiber          WS2801
Auflösung                         8 Bit pro LED
Anzahl kontrollierbarer LEDs      Maximal 960 (320 RGB LEDs)
Aktualisierungsrate               Maximal 100 Aktualisierungen pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 12mm (1,18 x 1,18 x 0,47")
Gewicht                           10g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/led-strip-bricklet/raw/master/hardware/led-strip-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/led_strip_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/led-strip-bricklet/zipball/master>`__)


.. _led_strip_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_led_strip_master_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert, kann nun ein LED Strip gesteuert werden.

.. FIXME image:: /Images/Bricklets/bricklet_led_strip_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_brickv.jpg

|test_pi_ref|

.. _led_strip_led_strips:

LED Strips
----------

TODO:

* How to use them?
* Where to inject power?

.. _led_strip_led_pixels:

LED Pixels
----------

TODO:

* How to use them?
* Where to inject power?


.. _led_strip_fixed_frame_rate:

Feste Aktualisierungsrate
-------------------------

Um eine flüssige Animation zu erreichen wird eine feste Aktualisierungsrate
benötigt. Eine feste Aktualisierungsrate kann einfach mit einer
korrekt konfigurierten Framelänge und dem FrameRendered Callback erreicht
werden. Die Framelänge stellt die Zeit in ms dar, die zwischen zwei
Frames verstreicht. Der FrameRendered Callback wird ausgelöst nachdem
ein neues Frame auf die LEDs übertragen wurde.

Wenn als Beispiel eine Aktualisierungsrate von 20 Frames pro Sekunde
erreicht werden soll, sollte die Framelänge auf 50ms gesetzt werden.
Nachdem die Framelänge gesetzt ist, muss das erste Frame übertragen werden
(d.h. es müssen alle RGB Werte gesetzt werden). Danach muss auf den
FrameRendered Callback gewartet werden woraufhin das nächste Frame
übertragen werden muss usw.

.. image:: /Images/Bricklets/bricklet_led_strip_fixed_frame_rate.png
   :scale: 100 %
   :alt: LEDs mit fester Aktualisierungsrate steuern
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_fixed_frame_rate.png

Wenn ein FrameRendered Callback empfangen wird bevor alle LEDs eines frames
gesetzt wurden, ist die Aktualisierungsrate zu hoch.

.. _led_strip_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das LED Strip Bricklet <https://www.tinkerforge.com/de/shop/cases/case-led-strip-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_led_strip_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für LED Strip Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_led_strip_case_built_up_1000.jpg

.. include:: LED_Strip.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/led_strip_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für LED Strip Bricklet
   :align: center
   :target: ../../_images/Exploded/led_strip_exploded.png

|bricklet_case_hint|


.. _led_strip_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: LED_Strip_hlpi.table
