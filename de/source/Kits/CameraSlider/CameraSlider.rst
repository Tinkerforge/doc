
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / Starterkit: Kameraschlitten
:FIXME_shoplink: ../../../shop/kits/starter-kit-camera-slider.html

.. _starter_kit_camera_slider:

Starterkit: Kameraschlitten
===========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/kit_camera_slider_complete1_350.jpg",
	               "Kits/kit_camera_slider_complete1_800.jpg",
	               "Kameraschlitten: Komplettes Kit")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_content_100.jpg",
	             "Kits/kit_camera_slider_content_800.jpg",
	             "Kameraschlitten: Inhalt")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_camera1_100.jpg",
	             "Kits/kit_camera_slider_camera1_800.jpg",
	             "Kameraschlitten: Mit Videokamera")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_camera2_100.jpg",
	             "Kits/kit_camera_slider_camera2_800.jpg",
	             "Kameraschlitten: Mit Kamera")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_w_lcd1_100.jpg",
	             "Kits/kit_camera_slider_w_lcd1_800.jpg",
	             "Kameraschlitten: Mit LCD")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_w_lcd2_100.jpg",
	             "Kits/kit_camera_slider_w_lcd2_800.jpg",
	             "Kameraschlitten: Mit LCD")
	}}
	{{ tfdocend() }}


.. note::
  Diese Kit ist noch in Entwicklung!


Features
--------

* Jederzeit einfach modifizierbar
* Mit MakerBeams eigene Halterungen bauen
* Weitere Funktionen mittels anderer Bricks und Bricklets

Beschreibung
------------

Das `Starterkit: Kamerschlitten <#>`__ erlaubt eine flüssige automatische
Bewegung von Foto- und Videokameras. Über die angebotene Demo Anwendung kann
der Schlitten frei bewegt und Zeitrafferaufnahmen erstellt werden. Mit den
angebotenen APIs kann der Schlitten aber auch in eigene Projekte integriert
werden.

Das Kit ist aus `MakerBeams <https://www.tinkerforge.com/de/shop/makerbeam.html>`__
aufgebaut. Andere Beams können ohne großen Aufwand
befestigt werden, so dass sehr einfach für andere Geräte eigene Halterungen
konstruiert werden können. Damit wird das Kit zur Achse zum linearen 
Bewegen von Lasten (Linearachse).

Ein `Stepper Brick <https://www.tinkerforge.com/de/shop/bricks/stepper-brick.html>`__
bewegt den Schlitten millimetergenau und kann mit weiteren 
`Bricks <https://www.tinkerforge.com/de/shop/bricks.html>`__
und 
`Bricklets <https://www.tinkerforge.com/de/shop/bricklets/industrial/industrial-quad-relay-bricklet.html>`__
erweitert werden. So kann zum Beispiel die Kamera automatisch von einem 
`Industrial Quad Relay Bricklet <https://www.tinkerforge.com/de/shop/bricklets/industrial/industrial-quad-relay-bricklet.html>`__
ausgelöst werden oder zusammen mit 
`RED Brick <https://www.tinkerforge.com/de/shop/bricks/red-brick.html>`__
und
`HDMI Display <https://www.tinkerforge.com/de/shop/accessories/red-brick/hdmi-display-5-inch.html>`__
eine autarke Lösung realisiert werden.


Technische Spezifikation
------------------------


.. _starter_kit_camera_slider_resources:

Ressourcen
----------


Firmware aktualisieren und erste Tests
--------------------------------------


Konstruktion
------------

Der Aufbau des Kits ist :ref:`hier <starter_kit_camera_slider_construction>`
beschrieben.

.. toctree::
   :hidden:

   Details <Construction>

.. image:: /Images/Kits/kit_camera_slider_construction_collage_800.jpg
   :scale: 100 %
   :alt: Konstruktionscollage des Kameraschlitten Kits
   :align: center
   :target: Construction.html


.. _starter_kit_camera_slider_demo:

Demo Anwendung
--------------
