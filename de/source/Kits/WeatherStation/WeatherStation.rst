
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / Starterkit: Wetterstation
:shoplink: ../../../shop/kits/starter-kit-weather-station.html

.. include:: WeatherStation.substitutions

.. _starter_kit_weather_station:

Starterkit: Wetterstation
=========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/weather_station_table_350.jpg",
	               "Kits/weather_station_table_800.jpg",
	               "Wetterstation: Basiskit auf Tisch")
	}}
	{{
	    tfdocimg("Kits/weather_station_black_table_100.jpg",
	             "Kits/weather_station_black_table_800.jpg",
	             "Wetterstation (schwarz): Basiskit auf Tisch")
	}}
	{{
	    tfdocimg("Kits/weather_station_wall_far_100.jpg",
	             "Kits/weather_station_wall_far_800.jpg",
	             "Wetterstation: Mit WLAN an Wand")
	}}
	{{
	    tfdocimg("Kits/weather_station_wall_near_100.jpg",
	             "Kits/weather_station_wall_near_800.jpg",
	             "Wetterstation: Mit WLAN an Wand")
	}}
	{{
	    tfdocimg("Kits/weather_station_construction_rpi_front_100.jpg",
	             "Kits/weather_station_construction_rpi_front_800.jpg",
	             "Wetterstation: Mit Raspberry Pi")
	}}
	{{
	    tfdocimg("Kits/weather_station_cosm_graphs_100.jpg",
	             "Kits/weather_station_cosm_graphs_800.jpg",
	             "Wetterstation: Cosm-Graphen")
	}}
	{{
	    tfdocimg("Kits/weather_station_lcd_all_100.jpg",
	             "Kits/weather_station_lcd_all_orig.jpg",
	             "Wetterstation: Verschiedene Modi")
	}}
	{{
	    tfdocimg("Kits/weather_station_website_100.jpg",
	             "Kits/weather_station_website_orig.jpg",
	             "Wetterstation: Eingebettet in einer Webseite")
	}}
	{{ tfdocend() }}

Features
--------

.. Einrueckung so beibehalten, da sonst kaputt

* Vollwertige Open Source Wetterstation.
* Misst Temperatur, Luftfeuchtigkeit, Luftdruck und Helligkeit.
* Hohe Präzision und Auflösung

  * z.B. Luftdruck 0,012mbar und Temperatur 0,01°C. 

* Steuerung über USB, WLAN oder mit Raspberry Pi.
* Modifizierbar mit mehr Tastern, mehr Sensoren und veränderter Software.

Beschreibung
------------

Das *Starterkit: Wetterstation* ist eine vollwertige Open Source Wetterstation.
Sie misst Temperatur, Luftfeuchtigkeit, Luftdruck und Helligkeit mit hoher
Präzision.

Sie kann per USB von einem (Embedded-) PC gesteuert werden. 
Auch eine Steuerung per WLAN ist über die :ref:`WIFI Extension <wifi_extension>`
möglich. Für einen Standalone-Betrieb kann ein Embbeded Board, wie z.B. das
:ref:`Raspberry Pi <embedded_raspberry_pi>`, direkt ins Gehaeuse eingebaut 
werden.
Die Messwerte können auf einem 20x4 Zeichen
LCD angezeigt, auf einer Webseite oder z.B. auf `Cosm <https://cosm.com/>`__ 
hochgeladen werden. Über vier Taster auf dem 
:ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` ist es möglich zwischen 
verschiedenen Modi umzuschalten.

Das Kit ermöglicht es nach eigenen Wünschen sowohl Soft- als auch Hardware
zu gestalten. Das Gehäuse besteht aus bastelfreundlichem PMMA und ist einfach
zu bearbeiten. Zusätzlich sind bereits Bohrlöcher für 
:ref:`Analog In <analog_in_bricklet>` und :ref:`IO-4 <io4_bricklet>` Bricklets 
vorhanden. So können auch noch weitere Sensoren (
`Anemometer <https://de.wikipedia.org/wiki/Anemometer>`__, 
`Pluviometer <https://de.wikipedia.org/wiki/Pluviometer>`__ etc.)
angeschlossen werden.

Die Wetterstation kann über alle verfügbaren Bindings (|bindings|) 
programmiert werden. Beispielimplementierungen für alle Programmiersprachen 
erleichtern den Einstieg in die Programmierung mit Tinkerforge.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert 
================================  ============================================================
Luftdruck                         10mbar - 1200mbar in 0,012mbar Schritten
Beleuchtungsstärke                0Lux - 900Lux in 0,1Lux Schritten
Relative Luftfeuchtigkeit         0% RH - 10% RH in 0,1% RH Schritten
Temperatur                        -40°C - 85°C in 0,01°C Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           240 x 46 x 100mm (9,45 x 1,81 x 3,94")
Gewicht                           376g
================================  ============================================================


Ressourcen
----------

* Wetterstationsgehäuse FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/weather-station/tree/master/case>`__)
* Beispielquelltexte *Write to LCD* (Download: |write_to_lcd_examples_download|)
* Beispielquelltext *Cosm* (Download: `Python <https://github.com/Tinkerforge/weather-station/tree/master/cosm/python>`__)
* Beispielquelltext *Webseite* (Download: `PHP <https://github.com/Tinkerforge/weather-station/tree/master/website/php>`__)
* Beispielquelltext *Button Control* (Download: `C# <https://github.com/Tinkerforge/weather-station/tree/master/button_control/csharp>`__)


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe alle Bricklets an den Master Brick an und verbinde es per USB mit
dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_plugin>`):

.. image:: /Images/Kits/weather_station_update_350.jpg
   :scale: 100 %
   :alt: Wetterstation mittels Brick Viewer aktualisieren
   :align: center
   :target: ../../_images/Kits/weather_station_update_orig.jpg

Danach sollten mit dem Brick Viewer alle Sensoren überprüft werden. Dazu klickt
man am besten durch die verschiedenen Tabs und überprüft die Sensorwerte.
Anschließend ist sichergestellt, dass der Master Brick und alle Bricklets
korrekt funktionieren auch nachdem alles in das Gehäuse geschraubt wurde.

.. batti: screenshot brickv with all tabs?

Konstruktion
------------

Es gibt nicht nur eine Art die Wetterstation aufzubauen. Nachfolgend zeigen wir
den Aufbau verschiedener Varianten. Das Starterkit: Wetterstation ist einfach
zu erweitern und zu modifizieren.

Zum Beispiel können Bricks und Bricklets mittels Abstandsbolzen befestigt 
werden oder auch direkt angeschraubt werden um Platz zu sparen. Es sind
weitere Bohrlöcher vorgesehen um Analog In, Temperature oder IO-4 Bricklets
zu befestigen um weitere Sensoren auszulesen.

Das benutzte PMMA Plastik ist einfach zu bearbeiten, so dass falls benötigt
eigene Bohrlöcher oder Öffnungen geschaffen werden können.

Verschiedene Aufbauvarianten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`Wetterstation (Basisversion) <starter_kit_weather_station_construction_basic>`
* :ref:`WLAN Wetterstation <starter_kit_weather_station_construction_wifi>`
* :ref:`Raspberry Pi Wetterstation <starter_kit_weather_station_construction_rpi>`

RS485, Ethernet, etc.
^^^^^^^^^^^^^^^^^^^^^

Die Wetterstation kann auch über RS485 oder Ethernet Extension
gesteuert werden. Der Aufbau ist hierbei der selbe wie bei WLAN Wetterstation
beschrieben, es muss nur die WIFI Extension durch RS485 oder Ethernet Extension
ausgetauscht werden.

Wird die Ethernet Extension benutzt, so kann der Stapel auch gleich
über das integrierte PoE versorgt werden, so dass Step-Down Power Supply
und der DC Jack Adapter nicht mehr notwendig sind.

Projekte
--------

Es gibt verschiedene Anwendungen für die Wetterstation:

Messwerte auf dem LCD anzeigen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die offensichtlichste Anwendung für das Starterkit: Wetterstation ist die
Anzeige der Umgebungsmesswerte auf dem LCD 20x4 Bricklet. Hierfür gibt es drei 
Möglichkeiten:

* USB Verbindung zu einem PC: Installiere den Brick Daemon und die Anwendung
  auf dem PC und verbinde den Master Brick per USB.
* WLAN Verbindung zu einem PC: Installiere die Anwendung auf dem PC und
  Verbinde die Wetterstation direct per WLAN oder über einen Accesspoint.
* Raspberry Pi oder ein anderes Embedded Board integriert in die Wetterstation:
  Installiere den Brick Daemon und die Anwendung auf dem Embedded Board und
  verbinde den Master Brick der Wetterstation per USB.

.. batti: link to further enhancement section? how to use rasp with weather station etc.

Die drei Möglichkeiten können das gleiche Programm benutzen.

Beispielanwendungen mit Schritt-für-Schritt Anleitungen existieren für:

|write_to_lcd_examples|.

Cosm Anbindung
^^^^^^^^^^^^^^

`Cosm <https://cosm.com/>`__ ist ein Service der die Möglichkeit bietet
das "Internet der Dinge" zu analysieren und zu visualisieren. Dieser kann eine
Historie der Wetterstationsdaten speichern, sowie nette Graphen zeichnen:

.. image:: /Images/Kits/weather_station_cosm_graphs_600.jpg
   :scale: 100 %
   :alt: Cosm Datastreams als Graph
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_graphs_orig.jpg

Eine Beispiel-Implementierung mit Schritt-für-Schritt Instruktionen
die die Wetterdaten auf Cosm veröffentlicht is verfügbar
in :ref:`Python <starter_kit_weather_station_cosm>`.

Die Wetterstation in unserem Labor hat den Cosm Feed
`125881 <https://cosm.com/feeds/125881>`__. Viel Spass beim
überprüfen unserer Arbeitsbedingungen ;-)!

Live-Anzeige von Messdaten auf einer Webseite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eine weitere Anwendung für die Wetterstation ist die Anzeige von Wetterdaten
auf eine Webseite:

.. image:: /Images/Kits/weather_station_website_orig.jpg
   :scale: 100 %
   :alt: Messwerte live auf einer Webseite
   :align: center
   :target: ../../_images/Kits/weather_station_website_orig.jpg

In diesem Projekt werden wir JavaScript/AJAX nutzen um die Messwerte
alle 5 Sekunden auf einer Webseite neu zu laden.

Eine Beispiel-Implementierung ist 
in :ref:`PHP <starter_kit_weather_station_website>` verfügbar.

Anzeige von Statistiken mit Umschaltung per Taster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Da das :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` über vier Taster verfügt
können wir die erste Anwendung um die Anzeige weiterer Daten erweitern
indem diese mit den Tastern durchgeschaltet werden.

.. image:: /Images/Kits/weather_station_lcd_all_orig.jpg
   :scale: 100 %
   :alt: Verschiedene Modi
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_all_orig.jpg

Die vier Taster werden in diesem Projekt genutzt um zwischen

* Standard Wetter Messung,
* 24h Min/Max/Durchschnitt,
* 24h Graph und
* Zeit und Datum.

Eine Beispielimplementierung ist
in :ref:`C# <starter_kit_weather_station_button_control>` verfügbar.

Zusätzlich Erweiterungen
------------------------

Gerne führen wir hier Mods, Erweiterungen oder Verbesserungen der Wetterstation 
auf. Bitte gebt uns Bescheid, wir verlinken hier gerne eure Projekte.

.. FIXME: Regenmesser, windgeschwindigkeit etc
