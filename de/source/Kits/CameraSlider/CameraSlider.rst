
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

Das Starterkit: Kamerschlitten erlaubt eine flüssige automatische
Bewegung von Foto- und Videokameras. Über die angebotene Demo Anwendung kann
der Schlitten frei bewegt und Zeitrafferaufnahmen erstellt werden. Mit den
angebotenen APIs kann der Schlitten aber auch in eigene Projekte integriert
werden.

Das Kit ist aus `MakerBeams <https://www.tinkerforge.com/de/shop/makerbeam.html>`__
aufgebaut. Andere Beams können ohne großen Aufwand
befestigt werden, so dass sehr einfach für andere Geräte eigene Halterungen
konstruiert werden können. Damit wird das Kit zur Achse zum linearen
Bewegen von Lasten (Linearachse).

Ein :ref:`Stepper Brick <stepper_brick>`
bewegt den Schlitten millimetergenau und kann mit weiteren
:ref:`Bricks <primer_bricks>` und :ref:`Bricklets <primer_bricklets>`
erweitert werden. So kann zum Beispiel die Kamera automatisch von einem
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
ausgelöst werden oder zusammen mit
:ref:`RED Brick <red_brick>` und
`HDMI Display <https://www.tinkerforge.com/de/shop/accessories/red-brick/hdmi-display-5-inch.html>`__
eine autarke Lösung realisiert werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Bewegungsbereich                  TBDcm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           TBDmm (TBD")
Gewicht                           TBDg
================================  ============================================================


.. _starter_kit_camera_slider_resources:

Ressourcen
----------

* Kameraschlitten-Halterungen als FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/camera-slider/tree/master/brackets>`__)
* :ref:`starter_kit_camera_slider_demo` (Download: `Windows <http://download.tinkerforge.com/kits/camera_slider/windows/starter_kit_camera_slider_demo_windows_latest.exe>`__, `Linux <http://download.tinkerforge.com/kits/camera_slider/linux/starter-kit-weather-station-demo_linux_latest.deb>`__, `Mac OS X <http://download.tinkerforge.com/kits/camera_slider/macos/starter_kit_camera_slider_demo_macos_latest.dmg>`__, `RED Brick <http://download.tinkerforge.com/kits/camera_slider/red_brick/starter_kit_camera_slider_demo_red_brick_latest.tfrba>`__, `Source Code <https://github.com/Tinkerforge/camera-slider/tree/master/demo>`__)


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
