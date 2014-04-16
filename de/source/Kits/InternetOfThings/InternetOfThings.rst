
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starterkit: Internet der Dinge
:shoplink: ../../../shop/kits/starter-kit-internet-of-things.html


.. _starter_kit_iot:

Starterkit: Internet der Dinge 
==============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
		tfdocstart("Kits/iot_front_350.jpg",
				   "Kits/iot_front_800.jpg",
				   "Starterkit: Internet der Dinge")
	}}
	{{
		tfdocimg("Kits/iot_back_ethernet_100.jpg",
				 "Kits/iot_back_ethernet_800.jpg",
				 "Internet der Dinge: Rückseite mit Ethernet")
	}}
	{{
		tfdocimg("Kits/iot_rpi_100.jpg",
				 "Kits/iot_rpi_800.jpg",
				 "Internet der Dinge: An Raspberry PI")
	}}
	{{
		tfdocimg("Kits/iot_half_open_100.jpg",
				 "Kits/iot_half_open_800.jpg",
				 "Internet der Dinge: Offen")
	}}
	{{
		tfdocimg("Kits/iot_half_open_ethernet_100.jpg",
				 "Kits/iot_half_open_ethernet_800.jpg",
				 "Internet der Dinge: Offen mit Ethernet")
	}}
	{{
		tfdocimg("Kits/iot_content_100.jpg",
				 "Kits/iot_content_800.jpg",
				 "Internet der Dinge: Inhalt")
	}}
	{{
		tfdocimg("Kits/iot_packaging_open_100.jpg",
				 "Kits/iot_packaging_open_800.jpg",
				 "Internet der Dinge: Verpackung")
	}}
	{{ tfdocend() }}

Features
--------

* Ermöglicht das Steuern von Geräten über das Internet
* 433MHz, externe Antenne, große Reichweite
* Erweiterbar, frei programmierbar
* TODO


Beschreibung
------------

Das `Internet der Dinge <http://de.wikipedia.org/wiki/Internet_der_Dinge>`__ 
(engl. Internet of Things (IoT)) stellt eine Evolution des Internets dar und 
vernetzt nicht nur, wie bisher, Menschen und Computer sondern auch beliebige 
andere physische Objekte ("Dinge", "things").

Das *Starterkit: Internet der Dinge* bietet einen einfachen Einstieg in die Welt
des Internet der Dinge und ermöglicht es, nahezu beliebige Geräte über das 
Internet zu steuern. Dazu ist das Kit mit einem Remote Switch Bricklet 
ausgestattet über das verschiedenste 433MHz Funk- steckdosen, dimmer und 
Hausautomatisationskomponenten gesteuert werden können. Eine Liste der 
unterstützten Funkaktoren kann hier gefunden werden: 
:ref:`Link <remote_switch_supported_devices>`.

Über die :ref:`API Bindings <api_bindings>` können diese Funkaktoren von 
jedem (Embedded-) PC, Smartphone oder Tablet über das Internet gesteuert werden. 
Dem Einschalten der Kaffeemaschine von unterwegs über das eigene Smartphone, 
oder das Dimmen der Wohnungsbeleuchtung gesteuert aus der eigenen Cloud oder
von einem Raspberry Pi steht mit dem Kit nichts im Wege. Die Webseite
`www.iot-remote.com <http://www.iot-remote.com/>`__ stellt eine direkte 
Möglichkeit zur Verfügung diese Aktoren von jedem internetfähigen Gerät zu 
steuern.

Das Kit besteht im wesentlichen aus einem Master Brick und einem Remote Switch 
Bricklet, welches mit einem 433MHz Sender ausgestattet ist. Über die USB 
Verbindung des Master Bricks können somit Steckdosen o.ä. gesteuert werden.
Ein angeschlossener (Embedded-) PC (z.B. Raspberry Pi) kann direkt die Steuerung
übernehmen oder als Gateway dienen. Über eine zusätzliche WIFI- oder Ethernet 
Master Extension kann auf ein Gateway verzichtet werden.

Mittels weiterer Module aus dem Baukastensystem kann das Kit weiter erweitert 
werden. So können zum Beispiel Temperaturen erfasst werden (Temperature, 
Temperature-IR oder PTC Bricklet) oder auf Bewegungen reagiert werden (Motion 
Detector Bricklet).





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

Anwendungen
-----------

Über das eigene Tablet, Smartphone oder PC steuern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO: How to use `www.iot-remote.com <http://www.iot-remote.com/>`__ ?

Eigene Programme Entwickeln
^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO: Link Remote Switch Bricklet Examples

Ethernet Hardware Erweiterung
-----------------------------

Möchte man auf ein externes USB <-> Ethernet Gateway (PC, Raspberry Pi o.ä.)
verzichten, bietet sich der Einsatz einer Ethernet Master Extension an.
Somit kann direkt mit dem Kit kommuniziert werden. Im Gehäuse ist Platz für 
eine Ethernet Master Extension vorgesehen, die nur auf das Master Brick gesteckt 
werden muss. Weitere Informationen zur Nutzung der Ethernet Extension
lassen sich hier finden: Link.

Interaktion mit anderen Dingen
------------------------------

Das Kit kann mit den verschiedensten anderen "Dingen" kommunizieren.
Am einfachsten lassen sich andere Bricks und Bricklets des Baukastensystems 
nutzen. Über produktspezifische Schnittstellen oder on-line Services wie 
Xively oder Carriots lässt sich aber auch ohne viel Aufwand mit anderen Geräten
interagieren. Nachfolgend stellen wir einige Beispiele vor:

Bewegungserkennung mit dem Motion Detektor Bricklet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Temperaturbasiertes Steuern von Fenstermotoren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tageslichtabhänige Jalousiesteuerung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GPS basierte Haussteuerung
^^^^^^^^^^^^^^^^^^^^^^^^^^

Strompreisbasierte Verbraucherschaltung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Verbrauchsabhängige Verbraucherschaltung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Intelligenter Strompreiszähler oder Hall-Effect Bricklet










Weitere Bricks/Bricklets
^^^^^^^^^^^^^^^^^^^^^^^^

Sollen Motoren gesteuert werden, oder eine IMU hinzugefügt werden können
weitere Bricks auf das Master Brick gesteckt werden. 

Über Bricklets kann das Kit um verschiedene Sensoren und I/O Module erweitert
werden. Diese werden einfach zusätzlich zum Remote Switch Bricklet an das Master
Brick angeschlossen.

TODO FOTO Temperature Bricklet im offenen Gehäuse




