
:shoplink: ../../../shop/kits/starter-kit-internet-of-things.html

.. _starter_kit_iot:

Starterkit: Internet der Dinge 
==============================

.. raw:: html

	{% tfgallery %}

	Kits/iot_on_table_[100|800].jpg                   Starterkit: Internet der Dinge
	Kits/iot_front_[?|?].jpg                          Starterkit: Internet der Dinge
	Kits/iot_back_ethernet_[100|800].jpg              Internet der Dinge: Rückseite mit Ethernet
	Kits/iot_rpi_[100|800].jpg                        Internet der Dinge: An Raspberry PI
	Kits/iot_half_open_[100|800].jpg                  Internet der Dinge: Offen
	Kits/iot_half_open_ethernet_[100|800].jpg         Internet der Dinge: Offen mit Ethernet
	Kits/iot_content_[100|800].jpg                    Internet der Dinge: Inhalt
	Kits/iot_packaging_open_[100|800].jpg             Internet der Dinge: Verpackung
	Kits/iot_website_iot_remote_switch_[100|600].jpg  Screenshot von iot-remote.com

	{% tfgalleryend %}

Features
--------

* Ermöglicht das Steuern von Geräten über das Internet
* Unterstützt 433MHz Aktoren
* Externe Antenne, große Reichweite
* Erweiterbar, frei programmierbar
* Steuerbar über `www.iot-remote.com <http://www.iot-remote.com/>`__ 

Beschreibung
------------

Das `Internet der Dinge <https://de.wikipedia.org/wiki/Internet_der_Dinge>`__
(engl. Internet of Things (IoT)) stellt eine Evolution des Internets dar und 
vernetzt nicht nur, wie bisher Menschen und Computer, sondern auch beliebige 
andere physische Objekte ("Dinge", "things").

Das *Starterkit: Internet der Dinge* bietet einen einfachen Einstieg in die Welt
des Internets der Dinge und ermöglicht es, nahezu beliebige Geräte über das
Internet zu steuern. Dazu ist das Kit mit einem 
:ref:`Remote Switch Bricklet 2.0 <remote_switch_v2_bricklet>`
ausgestattet über das verschiedenste 433MHz Funksteckdosen, Funkdimmer und 
Hausautomatisationskomponenten gesteuert werden können. In der Dokumentation
des Bricklets gibt es eine
:ref:`Liste der unterstützten Funkaktoren <remote_switch_v2_supported_devices>`.

Über die :ref:`API Bindings <api_bindings>` können diese Funkaktoren von 
jedem (Embedded-) PC, Smartphone oder Tablet über das Internet gesteuert werden. 
Dem Einschalten der Kaffeemaschine von unterwegs über das eigene Smartphone, 
oder das Dimmen der Wohnungsbeleuchtung gesteuert aus der eigenen Cloud oder
von einem Raspberry Pi steht mit dem Kit nichts im Wege. Die Webseite
`www.iot-remote.com <http://www.iot-remote.com/>`__ stellt eine direkte 
Möglichkeit zur Verfügung diese Aktoren von jedem internetfähigen Gerät zu 
steuern.

Das Kit besteht im wesentlichen aus einem :ref:`Master Brick <master_brick>`
und einem :ref:`Remote Switch Bricklet 2.0 <remote_switch_v2_bricklet>`,
welches mit einem 433MHz Sender ausgestattet ist. Über die USB
Verbindung des Master Bricks können somit Steckdosen o.ä. gesteuert werden.
Ein angeschlossener (Embedded-) PC (z.B. Raspberry Pi) kann direkt die Steuerung
übernehmen oder als Gateway dienen. Mit einer zusätzlichen
:ref:`Ethernet Master Extension <ethernet_extension>`
kann auf ein Gateway verzichtet werden.

Mittels weiterer Module aus dem Baukastensystem kann das Kit erweitert 
werden. So können zum Beispiel Temperaturen erfasst werden
(:ref:`Temperature <temperature_bricklet>`,
:ref:`Temperature IR <temperature_ir_bricklet>` oder
:ref:`PTC Bricklet <ptc_bricklet>`) oder auf Bewegungen reagiert werden
(:ref:`Motion Detector Bricklet <motion_detector_bricklet>`).

Dieses Kit wurde am 20. März 2018 aktualisiert. Das Kit kommt ab sofort mit
der neuen Version 2.0 des Remote Switch Bricklet und das Bricklet-Kabel ist
von der 7p-10p Variante. Die komplette Software ist kompatibel zu beiden Versionen.

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/j4MfrewCRe4" frameborder="0" allowfullscreen></iframe>


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

* Internet of Things Gehäuse als FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/case>`__)
* iot-remote.com Webseite (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/web>`__)
* iot-remote.com Server Implementierung (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/server>`__)


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe das Remote Switch Bricklet an den Master Brick an und verbinde es per USB 
mit dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_brick_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_bricklet_plugin>`):

.. image:: /Images/Kits/iot_update.jpg
   :scale: 100 %
   :alt: Internet der Dinge Update im Brick Viewer
   :align: center

   
Im nächsten Schritt sollte das Remote Switch Bricklet mit einer Funksteckdose
getestet werden. Eine Anleitung zu den Konfigurationsmöglichkeiten
ist :ref:`hier <remote_switch_v2_bricklet_addressing_types>` zu finden.
Anschließend kann damit begonnen werden das Kit zusammenzubauen.


Konstruktion
------------

Das Starterkit: Internet der Dinge wird mit einem :ref:`Master Brick <master_brick>`,
einem :ref:`Remote Switch Bricklet 2.0 <remote_switch_v2_bricklet>`, einem 6cm 
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
12mm Abstandshaltern (Gewinde innen/außen) auf den Master Brick geschraubt
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
* Verbinde Master Brick und Remote Switch Bricklet mit Bricklet Kabel
* Schraube Antenne an Remote Switch Bricklet

.. image:: /Images/Kits/iot_construction_step2_350.jpg
   :scale: 100 %
   :alt: Konstruktion Schritt 2
   :align: center
   :target: ../../_images/Kits/iot_construction_step2.png

Schritt 3: Kuppel aufsetzen
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Im letzten Schritt muss nun noch das Rückteil des Gehäuses in das Unterteil
gesteckt werden. Danach kann dann das Oberteil gebogen und angebracht werden.
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
Die Webseite nutzt JavaScript, das direkt im Browser ausgeführt wird. Es
erfolgt also nach dem Laden der Webseite und des JavaScipts kein Datenaustausch
über einen Server sondern nur zwischen dem lokalen Gerät und der zu steuernden
Hardware. Für eine offline Nutzung kann die Webseite heruntergeladen werden.

.. image:: /Images/Kits/iot_website_iot_remote_start_350.jpg
   :scale: 100 %
   :alt: iot-remote.com Webseite 
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_start.jpg

Die Webseite ist sehr einfach aufgebaut. Über "+ New Remote..." können neue
Geräte hinzugefügt werden. "Settings" erlaubt das Laden/Speichern von 
Konfigurationen und die Liste links (leer im Bild) zeigt die konfigurierten 
Geräte und bietet Zugriff auf deren Steuerung.

**Neues Gerät hinzufügen**

Über "+ New Remote..." können neue Geräte hinzugefügt werden. Es gibt vier 
Typen: A (Schalter), B (Schalter), B (Dimmer), C (Schalter). Der einzustellende 
Typ ist nur von dem zu steuernden Aktor abhängig (siehe :ref:`Liste der unterstützten
Aktoren <remote_switch_v2_supported_devices>`).

Je nach Aktor sind verschiedene Angaben zu machen. Eine genauere Beschreibung
befindet sich in der :ref:`Dokumentation <remote_switch_v2_bricklet_addressing_types>`
des Remote Switch Bricklets:

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
gesteuert werden. Als Beispiel nachfolgend die Steuerungsseite eines
Typ A Schalters.

.. image:: /Images/Kits/iot_website_iot_remote_switch_350.jpg
   :scale: 100 %
   :alt: Konfigurierter Typ A Schalter
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_switch.jpg


**Speichern/Laden der Konfiguration**

Die Webseite `www.iot-remote.com <http://www.iot-remote.com/>`__ wurde 
absichtlich ohne Loginfunktion programmiert. Dies macht es einfacher
eine eigene Instanz der Webseite aufzusetzen. Die Konfiguration wird lokal im
Browser in einem Cookie gespeichert und standardmäßig nicht an den Server
übertragen. Für die Nutzung der Webseite von einem Browser aus ist dies
ausreichend.

Um eine einmal erstellte Konfiguration in verschiedenen Browsern zu nutzen
kann diese auf www.iot-remote.com gespeichert werden, um sie dann in einem
anderen Browser wieder zu laden.

.. image:: /Images/Kits/iot_website_iot_remote_save_350.jpg
   :scale: 100 %
   :alt: Speichern/Laden der Konfiguration
   :align: center
   :target: ../../_images/Kits/iot_website_iot_remote_save.jpg

Wurde eine Konfiguration erstellt, so kann diese gespeichert werden. Dazu klickt
man auf "Settings" und klickt anschließend "Save configuration". Der Server
erzeugt anschließend eine Konfigurations-ID mit der die aktuelle Konfiguration
geladen werden kann.

Das Laden einer Konfiguration erfolgt analog. Dazu wird eine Konfigurations-ID
eingegeben und "Load configuration" geklickt. Anschließend sollten die zur ID 
gehörenden Geräte in der Liste angezeigt werden.

**Offline Betrieb / Lokale Nutzung**

Die komplette Webseite kann heruntergeladen werden (inklusive JavaScript) und
lokal genutzt werden. Ein Aufruf von 
`www.iot-remote.com <http://www.iot-remote.com/>`__ ist dann nicht mehr 
notwendig. Am einfachsten kann das komplette 
`Projekt von GitHub <https://github.com/Tinkerforge/internet-of-things>`__ als
`ZIP <https://github.com/Tinkerforge/internet-of-things/archive/master.zip>`__
heruntergeladen werden. Die Webseite inklusive JavaScript befindet sich
im Verzeichnis "web".

Leider unterstützt Chrome/Chromium standardmäßig keine File-Cookies, welche
benötigt werden um Cookies bei Offline Nutzung zu speichern. Um dieses
Problem zu umgehen kann Chrome/Chromium mit folgendem Parameter gestartet 
werden:

.. code-block:: none

 --enable-file-cookies

Die Webseite kann bei Lokale Nutzung immer noch den www.iot-remote.com Server
nutzen um Konfigurationen zu speichern/laden. Dieser Server kann aber auch leicht
selbst aufgesetzt werden. Dazu müssen folgende Programmteile angepasst werden:

* ``web/js/remote/pages/PageSettings``: ``this.HOST``,  ``this.PORT`` sowie
* ``server/server.py``: ``CONFIGURATION_PATH`` und ``LOCAL_PROXY_PORT``.

Die Abhängigkeiten des Python Servers bestehen aus python-twisted und 
python-autobahn. Der Server kann einfach mit Python gestartet werden::

 python server.py

Und schon ist man im Besitzt eines eigenen Internet of Things Webserver der
über WebSockets Konfigurationen speichern kann!

Eigene Programme Entwickeln
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Neben der direkten Nutzung von 
`www.iot-remote.com <http://www.iot-remote.com/>`__ kann das Kit natürlich auch
in eigenen Anwendungen verwendet werden. Grundlage hierzu bildet die 
:ref:`API des Remote Switch Bricklets <remote_switch_v2_bricklet_programming_interface>`,
die für verschiedene Programmiersprachen zur Verfügung steht. Die API 
Dokumentation der jeweiligen Sprache enthält zusätzlich kleine Beispielprogramme
die als Startpunkte für die eigenen Entwicklungen dienen können.

Ethernet Hardware Erweiterung
-----------------------------

Möchte man auf ein externes USB <-> Ethernet Gateway (PC, Raspberry Pi o.ä.)
verzichten, bietet sich der Einsatz einer 
:ref:`Ethernet Master Extension <ethernet_extension>` an.
Somit kann direkt mit dem Kit kommuniziert werden. Im Gehäuse ist Platz für 
eine Ethernet Master Extension vorgesehen. Diese muss nur auf das Master Brick gesteckt 
werden. In der Dokumentation gibt es :ref:`weitere Informationen zur Nutzung der
Ethernet Extension <remote_switch_v2_supported_devices>`.

Interaktion mit anderen Dingen
------------------------------

Das Kit kann mit den verschiedensten anderen "Dingen" kommunizieren.
Am einfachsten lassen sich andere Bricks und Bricklets des Baukastensystems 
nutzen. Über produktspezifische Schnittstellen oder Online-Services wie
`Xively <https://www.xively.com/>`__, `Cumulocity <https://www.cumulocity.com/>`__,
`Carriots <https://www.carriots.com/>`__, oder ähnliche lässt sich aber auch ohne
viel Aufwand mit anderen Geräten interagieren. Nachfolgend stellen wir einige 
Beispiele vor:

**Bewegungserkennung mit dem Motion Detektor Bricklet:**
Das :ref:`Motion Detector Bricklet <motion_detector_bricklet>`
ermöglicht die Detektion von Bewegungen. Zusammen
mit dem Kit können somit Verbraucher in Abhängigkeit von der Anwesenheit von
Personen geschaltet werden.

**Temperaturbasiertes Steuern von Fenstermotoren:**
Über Bricklets wie 
:ref:`Temperature <temperature_bricklet>`, 
:ref:`Temperature IR <temperature_ir_bricklet>` oder dem
:ref:`PTC Bricklet <ptc_bricklet>` können
Temperaturen gemessen werden. Zusammen mit 433MHz 
Hausautomatisierungskomponenten können somit Fenster temperaturabhängig bewegt
werden.

**Tageslichtabhänige Jalousiesteuerung:**
Das :ref:`Ambient Light Bricklet 2.0 <ambient_light_v2_bricklet>`
ermöglicht die Messung der Helligkeit von 
Sonnenlicht. Somit könnten Jalousien lichtabhängig gesteuert werden.

**GPS basierte Haussteuerung:**
Über das :ref:`GPS Bricklet <gps_bricklet>`
oder ein Smartphone mit GPS könnte das eigene Heim in 
Abhängigkeit der eigenen Position über das Internet gesteuert werden. Als 
Beispiel könnte die Außenbeleuchtung eingeschaltet werden wenn es dunkel ist und 
der Eigentümer sich dem Haus nähert.

**Strompreisbasierte Verbraucherschaltung:**
In manchen Stromtarifen ist der Strompreis abhängig von der Uhrzeit oder richtet
sich direkt an den aktuellen Strommarktpreisen. Verbraucher könnten in 
Abhängigkeit des aktuellen Strompreises Ein-/Ausgeschaltet werden.

**Verbrauchsabhängige Verbraucherschaltung:**
Viele intelligente Stromzähler ermöglichen den Zugriff auf den aktuellen
Stromverbrauch. Eine Alternative stellt das Auslesen der Umdrehungen der 
Ferrarisscheibe in einem gewöhnlichen Stromzähler mittels eines 
:ref:`Hall-Effect Bricklets <hall_effect_bricklet>` dar. 
Abhängig vom aktuellen Verbrauch könnten somit Verbraucher geschaltet werden.
