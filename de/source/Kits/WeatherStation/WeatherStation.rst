
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / Starterkit: Wetterstation

.. include:: WeatherStation.substitutions

.. _starter_kit_weather_station:

Starterkit: Wetterstation
=========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/weather_station_cosm_graphs_350.jpg",
	               "Kits/weather_station_cosm_graphs_600.jpg",
	               "Wetterstation: Cosm Graphen")
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

Das *Starterkit: Wetterstation* ist eine vollwertige Open Source Wetterstation.
Sie misst Temperatur, Luftfeuchtigkeit, Luftdruck und Helligkeit mit hoher
Präzision.

Sie kann Über einen PC oder :ref:`Raspberry Pi <embedded_raspberry_pi>` 
über USB oder, falls eine :ref:`WIFI Extension <wifi_extension>` eingebaut
wird, auch über Wi-Fi gesteuert werden. Die Messwerte können auf einem 20x4 Zeichen
LCD angezeigt, auf einer Webseite oder z.B. auf `Cosm <https://cosm.com/>`__ 
hochgeladen werden. Über vier Taster auf dem 
:ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` ist es möglich zwischen 
verschiedenen Modi umzuschalten.

Das Kit ermöglicht es nach eigenen Wünschen sowohl Soft- als auch Hardware
zu gestalten. Das Gehäuse besteht aus bastelfreundlichem PMMA und ist einfach
zu bearbeiten. Zusätzlich sind bereits Bohrlöcher für 
:ref:`Analog In <analog_in_bricklet>` und :ref:`IO-4 <io4_bricklet>` Bricklets 
vorhanden. So können auch noch weitere Sensoren (Anemometer, Pluviometer etc.)
angeschlossen werden.

Die Wetterstation kann über alle verfügbaren Bindings (|bindings|) 
programmiert werden. Beispiele Implementierungen für alle Programmiersprachen 
erleichtern den Einstieg in die Programmierung.


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe alle Bricklets an das Master Brick an und verbinde es per USB mit
dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren<brickv_flash_firmware>`, 
:ref:`Bricklets <brickv_flash_plugin>`):

.. image:: /Images/Kits/weather_station_update_350.jpg
   :scale: 100 %
   :alt: Wetterstation mittels Brick Viewer aktualisieren
   :align: center
   :target: ../../_images/Kits/weather_station_update_orig.jpg

Danach sollten mit dem Brick Viewer alle Sensoren überprüft werden. Dazu klickt
man am besten durch die verschiedenen Tabs und überprüft die Sensorwerte.
Anschließend ist sichergestellt, dass das Master Brick und alle Bricklets
korrekt funktionieren auch nachdem alles in das Gehäuse geschraubt wurde.

.. batti: screenshot brickv with all tabs?

Konstruktion
------------

TODO: Images of construction and instructions

Projekte
--------

Es gibt verschiedene Anwendungen für das Wetterstations-Starterkit:

Messwerte auf dem LCD anzeigen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die offensichtlichste Anwendung für das Starterkit Wetterstation ist die 
Anzeige der Umgebungsmesswerte auf dem LCD 20x4 Bricklet. Hierfür gibt es drei 
Möglichkeiten:

* USB Verbindung zu einem PC: Installiere Brickd und die Anwendung auf dem PC
  und verbinde das Master Brick per USB
* Wi-Fi Verbindung zu einem PC: Installiere die Anwendung auf dem PC und
  Verbinde die Wetterstation direct per Wi-Fi oder über einen Accesspoint.
* Raspberry Pi oder ein anderes Embedded Board integriert in die Wetterstation:
  Installiere Brickd  und die Anwendung auf dem Embedded Board und verbinde das
  Master Brick der Wetterstation per USB.

.. batti: link to further enhancement section? how to use rasp with weather station etc.

Die drei Möglichkeiten können den selben Source Code benutzen.

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
die die Wetterdaten mit Cosm austauscht is verfügbar
in :ref:`Python <starter_kit_weather_station_cosm>`.

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

Spätere Erweiterungen
---------------------

Gerne führen wir hier Mods, Erweiterungen oder Verbesserungen der Wetterstation 
auf. Bitte gebt uns bescheid, wir verlinken hier gerne eure Projekte.

.. FIXME: Regenmesser, windgeschwindigkeit etc
