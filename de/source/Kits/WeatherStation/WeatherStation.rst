
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / Starterkit: Wetterstation
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
	    tfdocimg("Kits/weather_station_demo_100.jpg",
	             "Kits/weather_station_demo.jpg",
	             "Wetterstation: Demo Anwendung")
	}}
	{{
	    tfdocimg("Kits/weather_station_xively_graphs_100.jpg",
	             "Kits/weather_station_xively_graphs_800.jpg",
	             "Wetterstation: Xively-Graphen")
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
	{{
	    tfdocimg("Kits/weather_station_buttons_assembled_100.jpg",
	             "Kits/weather_station_buttons_assembled_800.jpg",
	             "Wetterstation: Mit großen Drucktastern auf der linken Seite")
	}}
	{{ tfdocend() }}

Features
--------

.. Einrueckung so beibehalten, da sonst kaputt

* Vollwertige Open Source Wetterstation
* Misst Temperatur, Luftfeuchtigkeit, Luftdruck und Helligkeit
* Hohe Präzision und Auflösung

  * z.B. Luftdruck 0,012mbar und Temperatur 0,01°C

* Steuerung über USB, WLAN und Ethernet oder mit RED Brick und Raspberry Pi
* Modifizierbar: Mehr Taster, mehr Sensoren und eigene Software
* Demo-Anwendung verfügbar
* Internet der Dinge fähig

Beschreibung
------------

Das *Starterkit: Wetterstation* ist eine vollwertige Open Source Wetterstation.
Sie misst Temperatur, Luftfeuchtigkeit, Luftdruck und Helligkeit mit hoher
Präzision.

Sie kann per USB von einem (Embedded-) PC gesteuert werden. 
Auch eine Steuerung per WLAN ist über die :ref:`WIFI Extension <wifi_extension>`
möglich. Alternativ kann die Wetterstation auch mittels einer 
:ref:`Ethernet Extension <ethernet_extension>` in das lokale Netzwerk 
eingebunden werden. Für einen Standalone-Betrieb kann ein :ref:`RED Brick
<red_brick>` oder ein anderes Embedded Board, wie
z.B. das :ref:`Raspberry Pi <embedded_raspberry_pi>`, direkt ins Gehäuse 
eingebaut werden. Auch Internet der Dinge (Internet of Things, IoT) Anwendungen
sind somit möglich (siehe z.B. das 
:ref:`Xively Beispiel <starter_kit_weather_station_xively>`).

Für die Wetterstation sind verschiedene Beispielprojekte verfügbar, so können 
die Messwerte auf einem 20x4 Zeichen LCD angezeigt, 
auf einer Webseite oder z.B. auf `Xively (Cosm) <https://xively.com/>`__ 
hochgeladen werden. Über vier Taster auf dem 
:ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` kann zwischen 
verschiedenen Modi umgeschaltet werden.

Ein Teil dieser Beispielprojekte ist in einer Demo-Anwendung implementiert 
worden. Diese ist für Windows, Linux und Mac OS X verfügbar und kann benutzt
werden um die Station zu testen.

Das Kit ermöglicht es nach eigenen Wünschen sowohl Soft- als auch Hardware
zu gestalten. Das Gehäuse besteht aus bastelfreundlichem PMMA und ist einfach
zu bearbeiten. Zusätzlich sind bereits Bohrlöcher für 
:ref:`Analog In <analog_in_bricklet>` und :ref:`IO-4 <io4_bricklet>` Bricklets 
vorhanden. So können auch noch weitere Sensoren
(`Anemometer <https://de.wikipedia.org/wiki/Anemometer>`__,
`Pluviometer <https://de.wikipedia.org/wiki/Pluviometer>`__ etc.)
angeschlossen werden.

Die Wetterstation kann über alle verfügbaren Bindings (|bindings|) 
programmiert werden. Beispielimplementierungen für viele Programmiersprachen
und eine Demo-Anwendung erleichtern den Einstieg in die Programmierung mit 
Tinkerforge.

Ein kurzes Video über den Zusammenbau und einige Anwendungen gibt es auf Youtube:

.. raw:: html

 <center><iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/uwsseiiu_4A" frameborder="0" allowfullscreen></iframe></center>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert 
================================  ============================================================
Luftdruck                         10mbar - 1200mbar in 0,012mbar Schritten
Beleuchtungsstärke                0Lux - 900Lux in 0,1Lux Schritten
Relative Luftfeuchtigkeit         0% RH - 100% RH in 0,1% RH Schritten
Temperatur                        -40°C - 85°C in 0,01°C Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           240 x 46 x 100mm (9,45 x 1,81 x 3,94")
Gewicht                           376g
================================  ============================================================

.. _starter_kit_weather_station_resources:

Ressourcen
----------

* Wetterstationsgehäuse als FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/weather-station/tree/master/case>`__)
* Beispielquelltexte für :ref:`starter_kit_weather_station_write_to_lcd` (Download: |write_to_lcd_examples_download|)
* Beispielquelltext für :ref:`starter_kit_weather_station_xively` (Download: `Python <https://github.com/Tinkerforge/weather-station/tree/master/xively/python>`__)
* Beispielquelltext für :ref:`starter_kit_weather_station_website` (Download: `PHP <https://github.com/Tinkerforge/weather-station/tree/master/website/php>`__)
* Beispielquelltext für :ref:`starter_kit_weather_station_button_control` (Download: `C# <https://github.com/Tinkerforge/weather-station/tree/master/button_control/csharp>`__)
* Beispielkonfiguration für :ref:`starter_kit_weather_station_openhab` (`Download <https://github.com/Tinkerforge/weather-station/tree/master/openhab>`__)
* :ref:`starter_kit_weather_station_demo` (Download: `Windows <http://download.tinkerforge.com/kits/weather_station/windows/starter_kit_weather_station_demo_windows_latest.exe>`__, `Linux <http://download.tinkerforge.com/kits/weather_station/linux/starter-kit-weather-station-demo_linux_latest.deb>`__, `Mac OS X <http://download.tinkerforge.com/kits/weather_station/macos/starter_kit_weather_station_demo_macos_latest.dmg>`__, `Quelltext <https://github.com/Tinkerforge/weather-station/tree/master/demo>`__)

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

.. _starter_kit_weather_station_demo:

Demo Anwendung
^^^^^^^^^^^^^^

Wenn die Hardware korrekt funktioniert kann die Demo Anwendung zum
Starterkit: Wetterstation getestet werden. Diese implementiert für
Demonstrationszwecke drei der vorgestellten :ref:`Projekte
<starter_kit_weather_station_projects>`:

1. :ref:`starter_kit_weather_station_write_to_lcd`
2. :ref:`starter_kit_weather_station_button_control`
3. :ref:`starter_kit_weather_station_xively`

Jedes Projekt besitzt sein eigenes Tab in der Anwendung. Das erste Projekt
zeigt nur die gemessenen Werte an. Das zweite Projekt ist komplexer und
zeigt Min-, Max- und Durchschnittswerte sowie Graphen der Messungen an.
Die Anzeige kann hierbei über die vier Taster des LCD 20x4 Bricklets oder
über die Taster in der Anwendung geändert werden. In manchen Modi kann über 
ein mehrfaches Drücken des Tasters der Sensor geändert werden.

Zum Schluss bietet das Xively Projekt die Möglichkeit die Messwerte 
hochzuladen. Dazu muss sich auf `xively.com <https://xively.com>`__
registriert werden. Anschließend können dort Feed ID und API Key 
sowie für jeden Sensor ein Channel angelegt werden 
(AirPressure, AmbientLight, Humidity und Temperature).
Feed ID, API Key und das Upload-Intervall müssen anschließend
in der Demo Anwendung konfiguriert werden. Für weitere Informationen
siehe die Projektbeschreibung.

Die Demo Anwendung kann aus den :ref:`Ressourcen <starter_kit_weather_station_resources>`
heruntergeladen werden.

.. image:: /Images/Kits/weather_station_demo_350.jpg
   :scale: 100 %
   :alt: Screenshot Wetterstation Demo Anwendung
   :align: center
   :target: ../../_images/Kits/weather_station_demo.jpg


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
* :ref:`RED Brick Wetterstation <starter_kit_weather_station_construction_red_brick>`
* :ref:`Raspberry Pi Wetterstation <starter_kit_weather_station_construction_raspberry_pi>`

.. toctree::
   :hidden:

   Construction_Basic
   Construction_Wifi
   Construction_REDBrick
   Construction_RaspberryPi

RS485, Ethernet, etc.
"""""""""""""""""""""

Die Wetterstation kann auch über RS485 oder Ethernet Extension
gesteuert werden. Der Aufbau ist hierbei der selbe wie bei "WLAN Wetterstation"
beschrieben, es muss nur die WIFI Extension durch eine RS485 oder Ethernet 
Extension ausgetauscht werden.

Wird die Ethernet Extension mit PoE genutzt, so kann der Stapel auch gleich
über das integrierte PoE versorgt werden, so dass Step-Down Power Supply
und der DC Jack Adapter nicht mehr notwendig sind.


.. _starter_kit_weather_station_projects:

Projekte
--------

Im Folgenden werden verschiedene Anwendungen für die Wetterstation
vorgestellt:

.. _starter_kit_weather_station_write_to_lcd:

Messwerte auf dem LCD anzeigen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die offensichtlichste Anwendung für das Starterkit: Wetterstation ist die
Anzeige der Umgebungsmesswerte auf dem LCD 20x4 Bricklet. Hierfür gibt es vier
Möglichkeiten:

* USB Verbindung zu einem PC: Installiere den Brick Daemon und die Anwendung
  auf dem PC und verbinde den Master Brick per USB.
* WLAN Verbindung zu einem PC: Installiere die Anwendung auf dem PC und
  Verbinde die Wetterstation direkt per WLAN oder über einen Access Point.
* RED Brick: Lade die Anwendung mit Hilfe des Brick Viewers auf den RED Brick
  hoch. Wie dies genau funktioniert ist in der :ref:`RED Brick Dokumenation
  <red_brick_program_tab>` im Detail beschrieben.
* Raspberry Pi oder ein anderes Embedded Board integriert in die Wetterstation:
  Installiere den Brick Daemon und die Anwendung auf dem Embedded Board und
  verbinde den Master Brick der Wetterstation per USB.

.. batti: link to further enhancement section? how to use rasp with weather station etc.

Die vier Möglichkeiten können das gleiche Programm benutzen.

Beispielanwendungen mit Schritt-für-Schritt Anleitungen existieren für: |write_to_lcd_examples|.

.. include:: WriteToLCD.toctree


.. _starter_kit_weather_station_xively:

Internet der Dinge / Xively Anbindung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Xively <https://xively.com/>`__ ist ein Service der die Möglichkeit bietet
das "Internet der Dinge" zu analysieren und zu visualisieren. Dieser kann eine
Historie der Wetterstationsdaten speichern, sowie nette Graphen zeichnen:

.. image:: /Images/Kits/weather_station_xively_graphs_600.jpg
   :scale: 100 %
   :alt: Xively Datastreams als Graph
   :align: center
   :target: ../../_images/Kits/weather_station_xively_graphs_orig.jpg

Eine Beispiel-Implementierung mit Schritt-für-Schritt Instruktionen
die die Wetterdaten auf Xively veröffentlicht ist verfügbar
in :ref:`Python <starter_kit_weather_station_python_to_xively>`.

.. toctree::
   :hidden:

   PythonToXively

Die Wetterstation in unserem Labor hat den Xively Feed
`125881 <https://xively.com/feeds/125881>`__. Viel Spass beim
überprüfen unserer Arbeitsbedingungen ;-)!


.. _starter_kit_weather_station_website:

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

Eine Beispielimplementierung ist 
in :ref:`PHP <starter_kit_weather_station_website_php>` verfügbar.

.. toctree::
   :hidden:

   PHPToWebsite


.. _starter_kit_weather_station_button_control:

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
in :ref:`C# <starter_kit_weather_station_button_control_csharp>` verfügbar.

.. toctree::
   :hidden:

   CSharpToButtonControl


.. _starter_kit_weather_station_openhab:

Smart Home Integration mit openHAB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Wetterstation kann in ein `openHAB <http://www.openhab.org/>`__ verwaltetes
Smart Home integriert werden mittels der `openHAB Tinkerforge Bindings
<https://github.com/openhab/openhab/wiki/Tinkerforge-Binding/>`__.

.. image:: /Images/Kits/weather_station_openhab_orig.jpg
   :scale: 100 %
   :alt: openHAB example sitemap
   :align: center
   :target: ../../_images/Kits/weather_station_openhab_orig.jpg

Als Beispiel werden wir die nötigen :ref:`openHAB Konfigurationsschritte
<starter_kit_weather_station_openhab_red_brick>` für die Integration mit einem
RED Brick demonstrieren.

.. toctree::
   :hidden:

   OpenHABOnREDBrick


Zusätzlich Erweiterungen
------------------------

Gerne führen wir hier Mods, Erweiterungen oder Verbesserungen der Wetterstation 
auf. Bitte gebt uns Bescheid, wir verlinken hier gerne eure Projekte.


Größere Drucktaster
^^^^^^^^^^^^^^^^^^^

Die Drucktaster des LCD 20x4 Bricklet sind ein wenig fummelig. Als
Erweiterung für die Wetterstation bieten wir große Drucktaster
mit der `Wetterstation Drucktaster-Erweiterung
<https://www.tinkerforge.com/de/shop/kits/weather-station-push-button-add-on.html>`__ an.


.. image:: /Images/Kits/weather_station_buttons_assembled_600.jpg
   :scale: 100 %
   :alt: Wetterstation mit großen Drucktastern
   :align: center
   :target: ../../_images/Kits/weather_station_buttons_assembled_1200.jpg

Die Erweiterung besteht aus vier großen Drucktastern, einem Ersatzseitenteil
für die linke Seite des Gehäuses der Wetterstation und einer rechtwinkligen
2x3 Stiftleiste.

Ein Lötkolben und ein paar Käbelchen werden benötigt um die Drucktaster
mit dem LCD 20x4 Bricklet zu verbinden.

.. image:: /Images/Kits/weather_station_buttons_soldered_350.jpg
   :scale: 100 %
   :alt: Verkabelung der Drucktaster
   :align: center
   :target: ../../_images/Kits/weather_station_buttons_soldered_1200.jpg

.. image:: /Images/Kits/weather_station_buttons_and_lcd_350.jpg
   :scale: 100 %
   :alt: Drucktaster verbunden mit dem LCD 20x4
   :align: center
   :target: ../../_images/Kits/weather_station_buttons_and_lcd_1200.jpg

Änderungen in der Software werden nicht benötigt.

Um einen Taster an das LCD 20x4 Bricklet anzuschließen muss der eine Pin des Tasters mit 
GND und der andere mit einem Eingang (BTN0-BTN3) verbunden werden. In den vorhergehenden 
Fotos haben wir eine schwarze Leitung genommen und GND durchzuschleifen und rote Leitungen
um jeden Taster mit einem Eingang zu verbinden.

.. image:: /Images/Kits/weather_station_button_wiring_350.jpg
   :scale: 100 %
   :alt: Taster Verdrahtung mit dem LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Kits/weather_station_button_wiring.jpg

Als Spaß-Anwendung haben wir einen Demonstrator für ein Spiel wie
Guitar Hero in Java geschrieben. Die Anwendung zeigt zufällig erzeugte Balken 
auf dem LCD an, die sich zu einer Seite bewegen. Über die vier großen 
Drucktaster lassen sich verschiedene Töne erzeugen und das dafür benutzte
Instrument lässt sich aus der 
`General MIDI <http://en.wikipedia.org/wiki/General_MIDI>`__ Definition 
wählen. Die Logik des Spiels fehlt allerdings komplett.

Dieser Demonstrator soll zeigen, dass auch andere Anwendungen als die typischen
Wetterstationsanwendungen möglich sind.

.. image:: /Images/Kits/weather_station_guitar_350.jpg
   :scale: 100 %
   :alt: Spieleanwedung auf der Wetterstation
   :align: center
   :target: ../../_images/Kits/weather_station_guitar_1200.jpg

Der Quelltext kann hier herunter geladen werden: `Download
<https://raw.githubusercontent.com/Tinkerforge/weather-station/master/examples/GuitarStation.java>`__

.. FIXME: Regenmesser, windgeschwindigkeit etc
