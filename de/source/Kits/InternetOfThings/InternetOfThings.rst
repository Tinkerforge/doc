
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starterkit: Internet der Dinge
:shoplink: ../../../shop/kits/starter-kit-internet-of-things.html


.. _starter_kit_iot:

Starterkit: Internet der Dinge 
==============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
		tfdocstart("Kits/iot_on_table_350.jpg",
				   "Kits/iot_on_table_800.jpg",
				   "Starterkit: Internet der Dinge")
	}}
	{{
		tfdocimg("Kits/iot_front_100.jpg",
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
* 433MHz Aktoren unterstützt
* Externe Antenne, große Reichweite
* Erweiterbar, frei programmierbar
* Steuerbar über `www.iot-remote.com <http://www.iot-remote.com/>`__ 

Beschreibung
------------

Das `Internet der Dinge <http://de.wikipedia.org/wiki/Internet_der_Dinge>`__ 
(engl. Internet of Things (IoT)) stellt eine Evolution des Internets dar und 
vernetzt nicht nur, wie bisher, Menschen und Computer sondern auch beliebige 
andere physische Objekte ("Dinge", "things").

Das *Starterkit: Internet der Dinge* bietet einen einfachen Einstieg in die Welt
des Internet der Dinge und ermöglicht es, nahezu beliebige Geräte über das 
Internet zu steuern. Dazu ist das Kit mit einem 
`Remote Switch Bricklet <remote_switch_bricklet>`__
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
Integriertes Funkmodul                     RFM69HW (Remote Switch Bricklet)
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

* Internet of Things Kit Gehäuse FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/case>`__)


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
getestet werden. Eine Anleitung zu den Konfigurationsmöglichkeiten
lässt sich hier finden: `Link <remote_switch_bricklet_addressing_types>`__.
Anschließend kann damit begonnen werden das Kit zusammenzubauen.


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

Ohne Programmieraufwand können direkt 433MHz Aktoren wie Funksteckdosen, Dimmer
oder Hausautomatisierungskomponenten über die Webseite 
`www.iot-remote.com <http://www.iot-remote.com/>`__ gesteuert werden.
Die Webseite nutzt Javascript, das direkt im Browser ausgeführt wird. Es 
erfolgt also nach dem Laden der Webseite und des Javascipts kein Datenaustausch 
über einen Server sondern nur zwischen dem lokalen Gerät und der zu steuernden
Hardware. Für eine offline Nutzung kann die Webseite heruntergeladen werden.

.. image:: /Images/Kits/iot_website_iot_remote_start_350.jpg
   :scale: 100 %
   :alt: Explosionszeichnung für Remote Switch Bricklet
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_start.jpg

Die Webseite ist sehr einfach aufgebaut. Über "+ New Remote..." können neue
Geräte hinzugefügt werden. "Settings" erlaubt das Laden/Speichern von 
Konfigurationen und die Liste links (leer im Bild) zeigt die konfigurierten 
Geräte und bietet Zugriff auf deren Steuerung.

**Neues Gerät hinzufügen**

Über "+ New Remote..." können neue Geräte hinzugefügt werden. Es gibt vier 
Typen: A (Schalter), B (Schalter), B(Dimmer), C (Schalter). Der einzustellende 
Typ ist nur von dem zu steuernden Aktor abhängig. Eine Liste der unterstützten 
Aktoren findet man hier: :ref:`Link <remote_switch_supported_devices>`.

Je nach Aktor sind verschiedene Angaben zu machen. Eine genauere Beschreibung
befindet sich in der `Remote Switch Bricklet Dokumentation 
<remote_switch_bricklet_addressing_types>`__

Typ A (Schalter):

.. image:: /Images/Kits/iot_website_iot_remote_configure_a_350.jpg
   :scale: 100 %
   :alt: Konfiguration für Typ A Schalter
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_configure_a.jpg

Typ B (Schalter):

.. image:: /Images/Kits/iot_website_iot_remote_configure_b_350.jpg
   :scale: 100 %
   :alt: Konfiguration für Typ B Schalter
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_configure_b.jpg

Typ B (Dimmer):

.. image:: /Images/Kits/iot_website_iot_remote_configure_b2_350.jpg
   :scale: 100 %
   :alt: Konfiguration für Typ B Dimmer
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_configure_b2.jpg

Typ C (Schalter):

.. image:: /Images/Kits/iot_website_iot_remote_configure_c_350.jpg
   :scale: 100 %
   :alt: Konfiguration für Typ C Schalter
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_configure_c.jpg

**Steuern eines Geräts**

Geräte können durch Klicken auf den jeweiligen Eintrag in der Liste
gesteuert werden. Als Beispiel nachfolgend die Steuerungssseite eines
Typ A Schalters.

.. image:: /Images/Kits/iot_website_iot_remote_switch_350.jpg
   :scale: 100 %
   :alt: Konfigurierter für Typ A Schalter
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_switch.jpg


**Speicher/Laden der Konfiguration**
Die Webseite `www.iot-remote.com <http://www.iot-remote.com/>`__ wurde 
absichtlich ohne Loginfunktion programmiert. Um eine einmal erstellte 
Konfiguration in verschiedenen Browsern zu nutzen kann diese gespeichert werden.

.. image:: /Images/Kits/iot_website_iot_remote_save_350.jpg
   :scale: 100 %
   :alt: Speichern/Laden der Konfiguration
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_save.jpg

Wurde eine Konfiguration erstellt, so kann diese gespeichert werden. Dazu klickt
man auf "Settings" und klickt anschließend "Save configuration". Der Server
erzeugt anschließend eine Konfigurations ID mit der die aktuelle Konfiguration
geladen werden kann.

Das Laden einer Konfiguration erfolgt analog. Dazu wird eine Konfigurations ID 
eingegeben und "Load configuration" geklickt. Anschließend sollten die zur ID 
gehörenen Geräte in der Liste angezeigt werden.

**Offline Betrieb / Lokale Nutzung**
Die komplette Webseite kann heruntergeladen werden (inkl. dem Javascript) und
lokal genutzt werden. Ein Aufruf von 
`www.iot-remote.com <http://www.iot-remote.com/>`__ ist dann nicht mehr 
notwendig. Am einfachsten kann das komplette Projekt von GitHub heruntergeladen
werden: 
`ZIP <https://github.com/Tinkerforge/internet-of-things/archive/master.zip>`__
Die Webseite inkl. JavaScript befindet sich im Verzeichnis "web".

Eigene Programme Entwickeln
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Neben der direkten Nutzung von 
`www.iot-remote.com <http://www.iot-remote.com/>`__ kann das Kit natürlich auch
in eigenen Anwendungen verwendet werden. Grundlage hierzu bildet die 
:ref:`ÀPI des Remote Switch Bricklets<remote_switch_bricklet_programming_interface>`,
die für verschiedene Programmiersprachen zur Verfügung steht. Die API 
Dokumentation der jeweiligen Sprache enthält zusätzlich kleine Beispielprogramme
die als Startpunkt für die eigenen Entwicklungen dienen können.

Ethernet Hardware Erweiterung
-----------------------------

Möchte man auf ein externes USB <-> Ethernet Gateway (PC, Raspberry Pi o.ä.)
verzichten, bietet sich der Einsatz einer 
:ref:`Ethernet Master Extension<ethernet_extension>` an.
Somit kann direkt mit dem Kit kommuniziert werden. Im Gehäuse ist Platz für 
eine Ethernet Master Extension vorgesehen, die nur auf das Master Brick gesteckt 
werden muss. Weitere Informationen zur Nutzung der Ethernet Extension
lassen sich hier finden: `Link <remote_switch_supported_devices>`.

Interaktion mit anderen Dingen
------------------------------

Das Kit kann mit den verschiedensten anderen "Dingen" kommunizieren.
Am einfachsten lassen sich andere Bricks und Bricklets des Baukastensystems 
nutzen. Über produktspezifische Schnittstellen oder on-line Services wie 
`Xively <https://xively.com/>`__, `Cumulocity <http://www.cumulocity.com/>`__,
`Carriots <http://www.carriots.com/>`__, oder ähnliche lässt sich aber auch ohne 
viel Aufwand mit anderen Geräten interagieren. Nachfolgend stellen wir einige 
Beispiele vor:

**Bewegungserkennung mit dem Motion Detektor Bricklet**
Das :ref:`Motion Detector Bricklet <motion_detector_bricklet>`
ermöglicht die Detektion von Bewegungen. Zusammen
mit dem Kit können somit Verbraucher in Abhängigkeit von der Anwesenheit von
Personen geschaltet werden.

**Temperaturbasiertes Steuern von Fenstermotoren**
Über Bricklets wie 
:ref:`Temperature <temperature_bricklet>`, 
:ref:`Temperature IR<temperature_ir_bricklet>` oder dem 
:ref:`PTC Bricklet <ptc_bricklet>` können
Temperaturen gemessen werden. Zusammen mit 433MHz 
Hausautomatisierungskomponenten können somit Fenster temperaturabhängig bewegt
werden.

**Tageslichtabhänige Jalousiesteuerung**
Das :ref:`Ambient Light Bricklet <ambient_light_bricklet>`
ermöglicht die Messung der Helligkeit von 
Sonnenlicht. Somit könnten Jalousien lichtabhängig gesteuert werden.

**GPS basierte Haussteuerung**
Über das :ref:`GPS Bricklet <gps_bricklet>`
oder ein Smartphone mit GPS könnte eigene Heim in 
Abhängigkeit der eigenen Position über das Internet gesteuert werden. Als 
Beispiel könnte die Außenbeleuchtung eingeschaltet werden wenn es dunkel ist und 
der Eigentümer sich dem Haus nähert.

**Strompreisbasierte Verbraucherschaltung**
In manchen Stromtarifen ist der Strompreis abhängig von der Uhrzeit oder richtet
sich direkt an den akutellen Strommarktpreisen. Verbraucher könnten in 
Abhängigkeit des aktuellen Strompreises Ein-/Ausgeschaltet werden.

**Verbrauchsabhängige Verbraucherschaltung**
Viele intelligente Stromzähler ermöglichen den Zugriff auf den aktuellen
Stromverbrauch. Eine Alternative stellt das Auslesen der Umdrehungen der 
Ferrarisscheibe in einem gewöhnlichen Stromzähler mittels eines 
:ref:`Hall-Effect Bricklets <hall_effect_bricklet>` dar. 
Abhängig vom aktuellen Verbrauch könnten somit Verbraucher geschaltet werden.




