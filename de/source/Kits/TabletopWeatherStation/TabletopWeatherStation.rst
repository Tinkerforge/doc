
:shoplink: ../../../shop/kits/tabletop-weather-station.html

.. include:: TabletopWeatherStation.substitutions
   :start-after: >>>general
   :end-before: <<<general


.. _tabletop_weather_station:

Tisch-Wetterstation
===================

.. raw:: html

	{% tfgallery %}

	Kits/tabletop_weather_station_transparent_right_titled_[?|?].jpg    Tisch-Wetterstation
	Kits/tabletop_weather_station_content_[?|?].jpg                     Tisch-Wetterstation
	Kits/tabletop_weather_station_transparent_back_[?|?].jpg            Tisch-Wetterstation
	Kits/tabletop_weather_station_transparent_back_titled_[?|?].jpg     Tisch-Wetterstation
	Kits/tabletop_weather_station_transparent_titled_[?|?].jpg          Tisch-Wetterstation
	Kits/tabletop_weather_station_transparent_titled_pwr_[?|?].jpg      Tisch-Wetterstation
	Kits/tabletop_weather_station_complete_transparent_back_[?|?].jpg   Tisch-Wetterstation
	Kits/tabletop_weather_station_black_right_back_[?|?].jpg            Tisch-Wetterstation
	Kits/tabletop_weather_station_black_right_titled_[?|?].jpg          Tisch-Wetterstation
	Kits/tabletop_weather_station_blue_back_[?|?].jpg                   Tisch-Wetterstation
	Kits/tabletop_weather_station_blue_left_back_[?|?].jpg              Tisch-Wetterstation
	Kits/tabletop_weather_station_blue_right_titled_[?|?].jpg           Tisch-Wetterstation
	Kits/tabletop_weather_station_colors_[?|?].jpg                      Tisch-Wetterstation
	Kits/tabletop_weather_station_colors_side_by_side_[?|?].jpg         Tisch-Wetterstation
	Kits/tabletop_weather_station_frosted_back_[?|?].jpg                Tisch-Wetterstation
	Kits/tabletop_weather_station_frosted_right_titled_[?|?].jpg        Tisch-Wetterstation
	Kits/tabletop_weather_station_frosted_titled_[?|?].jpg              Tisch-Wetterstation
	Kits/tabletop_weather_station_screen_graph_[?|?].jpg                Tisch-Wetterstation
	Kits/tabletop_weather_station_screen_main_[?|?].jpg                 Tisch-Wetterstation
	Kits/tabletop_weather_station_screen_outdoor_[?|?].jpg              Tisch-Wetterstation
	Kits/tabletop_weather_station_screen_sensor_[?|?].jpg               Tisch-Wetterstation
	Kits/tabletop_weather_station_screen_settings_[?|?].jpg             Tisch-Wetterstation

	{% tfgalleryend %}

Features
--------

* Open Source touchfähige Tisch-Wetterstation
* Misst Temperatur, Luftfeuchtigkeit, Luftdruck und Luftqualität (Air Quality Index)
* Demo-Anwendung verfügbar (touchfähig, mit Graphen, Logging in Datenbank)
* Steuerbar über USB, WLAN, Ethernet oder mit RED Brick
* Internet der Dinge (IoT) fähig

Beschreibung
------------

Die Tisch-Wetterstation ist eine touchfähige Open Source Wetterstation.
Sie misst Temperatur, Luftfeuchtigkeit, Luftdruck und Luftqualität (Air Quality
Index) mit hoher Präzision. Das Basiskit basiert auf:

* :ref:`Master Brick <master_brick>`,
* :ref:`Air Quality Bricklet <air_quality_bricklet>` und
* `Tabletop Weather Station case <TBD>`__.

Sie kann per USB von einem (Embedded-) PC gesteuert werden. 
Auch eine Steuerung per WLAN ist über die :ref:`WIFI Extension <wifi_extension>`
möglich. Alternativ kann die Wetterstation auch mittels einer 
:ref:`Ethernet Extension <ethernet_extension>` in das lokale Netzwerk 
eingebunden werden. Für einen Standalone-Betrieb kann ein :ref:`RED Brick
<red_brick>` oder ein anderes Embedded Board, wie
z.B. das :ref:`Raspberry Pi <embedded_raspberry_pi>` genutzt werden.

Das Kit ermöglicht es nach eigenen Wünschen sowohl Soft- als auch Hardware
zu gestalten. Das Gehäuse besteht aus bastelfreundlichem PMMA und ist einfach
zu bearbeiten. Zusätzlich sind bereits Bohrlöcher für weiter Bricklets
vorhanden.

Die Wetterstation kann über alle verfügbaren Bindings (|bindings|) 
programmiert werden. Einfache Beispielimplementierungen für viele Programmiersprachen
stehen zur Verfügung. Eine Demo-Anwendung implementiert Steuerung über Touch,
Trendansicht per Graphen, Logging in einer Datenbank usw. Sie ist in Python
geschrieben und für Windows, Linux und macOS verfügbar.

Das Kit kann mit dem :ref:`Outdoor Weather Bricklet <outdoor_weather_bricklet>`
erweitert werden. Montagelöcher und eine Öffnung für die Antenne sind im Gehäuse
bereits vorgesehen. Mit dem Bricklet können die folgenden Funk-Außenwetterstationen und
Sensoren ausgelesen werden:

* `Außen-Wetterstation WS-6147 <https://www.tinkerforge.com/de/shop/outdoor-weather-station-ws-6147.html>`__
* `Temperatur/Luftfeuchte Sensor TH-6148 <https://www.tinkerforge.com/de/shop/temperature-humidity-sensor-th-6148.html>`__

Beide werden von der Demo-Anwendung unterstützt.

TODO: Video

..
	.. raw:: html

	 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/uwsseiiu_4A" frameborder="0" allowfullscreen></iframe>


Technische Spezifikation
------------------------

================================  =====================================================================
Eigenschaft                       Wert 
================================  =====================================================================
IAQ Index-Auflösung               1
Luftdruck-Auflösung               0,0018mbar
Luftfeuchte-Auflösung             0,008%RH
Temperatur-Auflösung              0,01°C
--------------------------------  ---------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------
IAQ Index-Genauigkeit             ±15 und ±15% des Wertes
Luftdruck-Genauigkeit             ±0,12mbar (700-900mbar bei 25-40°C), ±0,6mbar (gesamter Messbereich)
Luftfeuchte-Genauigkeit           ±3%RH (20-80%RH bei 25°C)
Temperatur-Genauigkeit            ±0,5°C (at 25°C), ±1,0°C (0-65°C)*
--------------------------------  ---------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------
Abmessungen (B x T x H)           110 x 125 x 65mm
Gewicht                           TBDg
================================  =====================================================================

.. _tabletop_weather_station_resources:

Ressourcen
----------

* Wetterstations-Gehäuse als FreeCAD CAD Dateien (`Download <TBD>`__)
* Demo-Anwendung Download: TODO
* Beispiele: |examples_download|

Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe alle Bricklets an den Master Brick an und verbinde es per USB mit
dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_brick_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_bricklet_plugin>`):

.. image:: /Images/Kits/tabletop_weather_station_update.jpg
   :scale: 100 %
   :alt: Tisch-Wetterstation mittels Brick Viewer aktualisieren
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_update.jpg

Danach sollten mit dem Brick Viewer alle Sensoren überprüft werden. Dazu klickt
man am besten durch die verschiedenen Tabs und überprüft die Sensorwerte.
Anschließend ist sichergestellt, dass der Master Brick und alle Bricklets
korrekt funktionieren auch nachdem alles in das Gehäuse geschraubt wurde.


.. _tabletop_weather_station_demo:

Demo-Anwendung
--------------

Die Demo-Anwendung für die Tisch-Wetterstation ist in Python geschrieben. Der
Source Code kann `hier <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/main>`__
gefunden werden. Ausführbare Dateien stehen für Linux, macOS und Windows `hier <TBD>`__ verfügbar.

Es werden die Daten des Air Quality Brickelts sowie der Außenwetterstation dargestellt.
Graphen können mit einer einstellbaren Zeitbasis angezeigt werden und die Daten werden
in einer sqlite Datenbank geloggt. Konfigurationen können per Touch-Bedienung über die
Wetterstation selbst eingestellt werden.

.. image:: /Images/Kits/tabletop_weather_station_gui_600.jpg
   :scale: 100 %
   :alt: GUI auf dem LCD 128x64 Bricklet
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_gui_1000.jpg

Die Anwendung ist in "Screens" aufgeteilt. Jeder Screen wird als ein Tab mit Text-Label
oder Icon dargestellt. Touch-Klick/Gesten und GUI-Callbacks werden zur einfachen
Nutzung vom LCD 128x64 zum selektierten Screen weitergeleitet.

Eigene Screens können über die 
`custom_screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/main/custom_screens.py>`__
hinzugefügt werden.

Ein einfacher Screen der die aktuelle Uhrzeit auf das Disply schreibt könnte wie folgt 
aussehen::

	class ClockScreen(Screen):
		# text/icon: Text is taken if no icon is available
		text = "Clock" # Text shown on tab
		icon = None    # Icon shown on tab (see icons.py and data/ sub-directory)

		# Called when tab is selected
		def draw_init(self):
			self.lcd.draw_text(40, 5, self.lcd.FONT_12X16, self.lcd.COLOR_BLACK, 'Time')
			self.draw_update()
		
		# Called when new data is available (usually once per second)
		def draw_update(self):
			# Get current time in HH:MM:SS format
			current_time = time.strftime("%H:%M:%S")
			self.lcd.draw_text(16, 30, self.lcd.FONT_12X16, self.lcd.COLOR_BLACK, current_time)

Minimalst muss der Tab-Text (oder optional ein icon) festgelegt und die ``draw_init``-
sowie ``draw_update``-Funktion implementiert werden. Beispiele für die Nutzung von
Touch-Gesten und ähnliches können in den bereits implementierten Screens in der 
`screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/main/screens.py>`__
gefunden werden.

Der obige Code fügt folgenden Tab zur Demo-Anwendung hinzu:

TODO: Foto

Pull Requests für neue Screens sind definitiv erwünscht, wir freuen uns schon darauf
eure schicken Screens in die Demo-Anwendung zu integrieren :-).


Konstruktion
------------

TODO


.. _tabletop_weather_station_examples:

Beispiele
---------

Wenn kein Python verwendet werden soll oder das Programm nicht auf der 
:ref:`Demo-Anwendung <tabletop_weather_station_demo>` basieren soll, gibt es Beispiele
für die folgenden Programmiersprachen:

.. include:: TabletopWeatherStation.substitutions
   :start-after: >>>example_list
   :end-before: <<<example_list

Diese Beispiele schreiben die gemessenen Daten mit einem Ein-Sekunden-Intervall auf das
Display. Sie sind so einfach wie möglich gehalten, aber mit einem robusten Ansatz. Die
Beispiele warten auf Verfügbarkeit des Brick Daemons, führen ein automatisches Reconnect
durch falls notwendig, enumerieren automatisch die UIDs der Bricklets und unterstützen
Hotplug.

Daher sind die Beispiele gut als Grundlage für eine eigene Anwendung geeignet.


.. _tabletop_weather_station_red:

Selbstständig mit RED Brick
---------------------------

TODO?


.. _tabletop_weather_station_openhab:

Smart Home Integration mit openHAB
----------------------------------

TODO
