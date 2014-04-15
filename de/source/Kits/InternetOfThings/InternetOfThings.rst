
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
Abmessungen (B x T x H)                    11cm x 6,5cm x 4,5cm (zusammengebautes Kit)
Gewicht                                    130g (zusammengebautes Kit)
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

Das Starterkit: Internet der Dinge wird mit einem :ref:`Master Brick <master_brick>`,
einem :ref:`Remote Switch Bricklet <remote_switch_bricklet>`, einem 6cm 
Bricklet Kabel, zwei Befestigungskits und vier rutschfeste Gummifüsse 
ausgeliefert.

Das Gehäuse kann in vier einfachen Schritten aufgebaut werden.

.. image:: /Images/Kits/iot_construction_exploded_w_lines_500.jpg
   :scale: 100 %
   :alt: Exploded assembly drawing
   :align: center
   :target: ../../_images/Kits/iot_construction_exploded_w_lines.png


Schritt 0: Schutzfolie entfernen 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Als erstes müssen die Schutzfolien von allen Gehäuseteilen entfernt werden. 
Jeweils auf Front- und Rückseite befindet sich eine Schutzfolie. Ein Messer kann
bei der Entfernung der Folien helfen, sollten sich diese schwer entfernen 
lassen.

Schritt 1: Abstandshalter anschrauben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schraube die 10mm Abstandshalter (Gewinde innen/innen) an den Master Brick
und das Remote Switch Bricklet.

.. image:: /Images/Kits/iot_construction_step1_350.jpg
   :scale: 100 %
   :alt: Konstruktion Schritt 1
   :align: center
   :target: ../../_images/Kits/iot_construction_step1.png

Wenn die Ethernet Extension verwendet werden soll, kann diese auf mit
9mm Abstandshaltern (Gewinde innen/außen) auf den Master Brick geschraubt
werden.

.. image:: /Images/Kits/iot_construction_ethernet_step1_350.jpg
   :scale: 100 %
   :alt: Konstruktion Schritt 1 (Ethernet Extension)
   :align: center
   :target: ../../_images/Kits/iot_construction_ethernet_step1.png

Schritt 2: Gehäuseunterteil anschrauben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schraube den Master Brick (mit oder ohne Ethernet Extension) und das
Remote Switch Bricklet auf die Unterseite des Gehäuses. Dabei sollte
folgende Reihenfolge eingehalten werden:

* Stecke Vorderteil des Gehäuses in Unterteil
* Schraube Master Brick und Remote Switch Bricklet zur Unterseite
* Klebe rutschfeste Gummifüsse an Unterseite
* Verbinde Master Brick udn Remote Switch Bricklet mit Bricklet Kabel
* Schraube Antenne an Remote Switch Bricklet

.. image:: /Images/Kits/iot_construction_step2_350.jpg
   :scale: 100 %
   :alt: Konstruktion Schritt 2
   :align: center
   :target: ../../_images/Kits/iot_construction_step2.png

Schritt 3: Kuppel aufsetzen
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Im letzten Schritt muss nun noch das Rückteil des Gehäuses in das Unterteil
gesteckt werden. Danach kann dann das Oberteil geboten und angebracht werden.
Das war es schon, das Gehäuse ist fertig!

.. image:: /Images/Kits/iot_construction_step3_350.jpg
   :scale: 100 %
   :alt: Konstruktion Schritt 3
   :align: center
   :target: ../../_images/Kits/iot_construction_step3.png
