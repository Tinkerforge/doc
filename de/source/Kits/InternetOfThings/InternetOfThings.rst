
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starterkit: Internet der Dinge
:shoplink: ../../../shop/kits/starter-kit-internet-of-things.html


.. _starter_kit_iot:

Starterkit: Internet der Dinge 
==============================

..
	.. raw:: html

		{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
		{{
			tfdocstart("Kits/kit_blinkenlights_fire_350.jpg",
					   "Kits/kit_blinkenlights_fire_600.jpg",
					   "Blinkenlights: Feuer Simulation")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_fire_daylight_100.jpg",
					 "Kits/kit_blinkenlights_fire_daylight_600.jpg",
					 "Blinkenlights: Feuer Simulation bei Tageslicht")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_on_wall_100.jpg",
					 "Kits/kit_blinkenlights_on_wall_600.jpg",
					 "Blinkenlights: An der Wand")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_pong_100.jpg",
					 "Kits/kit_blinkenlights_pong_600.jpg",
					 "Blinkenlights: Pong")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_pong_daylight_100.jpg",
					 "Kits/kit_blinkenlights_pong_daylight_600.jpg",
					 "Blinkenlights: Pong bei Tageslicht")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_tetris_100.jpg",
					 "Kits/kit_blinkenlights_tetris_600.jpg",
					 "Blinkenlights: Tetris")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_text_daylight_100.jpg",
					 "Kits/kit_blinkenlights_text_daylight_600.jpg",
					 "Blinkenlights: Text-Anzeige")
		}}
		{{
			tfdocimg("Kits/kit_blinkenlights_rainbow_near_far_dark_100.jpg",
					 "Kits/kit_blinkenlights_rainbow_near_far_dark_600.jpg",
					 "Blinkenlights: Regenbogen mit verschiedenen Frontplatten")
		}}
		{{ tfdocend() }}

Features
--------

* TODO
* TODO
* TODO
* TODO


Beschreibung
------------

Das *Starterkit: Blinkenlights* ist ...

Technische Spezifikation
------------------------

=========================================  ============================================================
Eigenschaft                                Wert
=========================================  ============================================================
Funkmodul                                  RFM69HW
Stromverbrauch                             10mA (inaktiv), 40mA (senden)
Funkfrequenz                               433MHz
-----------------------------------------  ------------------------------------------------------------
-----------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                    TBD 
Gewicht                                    TBD (zusammengebautes Kit)
=========================================  ============================================================


.. _starter_kit_iot_resources:

Ressourcen
----------

* TODO
* TODO
* TODO
* TODO

Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe das Remote Switch Bricklet an den Master Brick an und verbinde es per USB 
mit dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_plugin>`):

.. image:: /Images/Kits/iot_update.jpg
   :scale: 100 %
   :alt: Internet der Dinge Update im Brick Viewer
   :align: center

   
Im nächsten Schritt sollte das Remote Switch Bricklet mit einer Funksteckdose
getestet werden. Anschließend kann damit begonnen werden das Kit zusammenzubauen.


Konstruktion
------------

TODO
