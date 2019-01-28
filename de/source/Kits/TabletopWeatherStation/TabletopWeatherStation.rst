
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
* Steuerbar über USB, WLAN oder mit RED Brick
* Internet der Dinge (IoT) fähig

Beschreibung
------------

Die Tisch-Wetterstation ist eine touchfähige Open Source Wetterstation.
Sie misst Temperatur, Luftfeuchtigkeit, Luftdruck und Luftqualität (Air Quality
Index) mit hoher Präzision. Das Basiskit basiert auf:

* :ref:`Master Brick <master_brick>`,
* :ref:`Air Quality Bricklet <air_quality_bricklet>` und
* `Tabletop Weather Station case <https://www.tinkerforge.com/de/shop/tabletop-weather-station-case.html>`__.

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

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/dz18cRKUvgA" frameborder="0" allowfullscreen></iframe>


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
Temperatur-Genauigkeit            ±0,5°C (at 25°C), ±1,0°C (0-65°C)
--------------------------------  ---------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------
Abmessungen (B x T x H)           110 x 125 x 65mm
Gewicht                           238g (Basis), 288g (Basis + RED Brick + Outdoor Weather Bricklet)
================================  =====================================================================

.. _tabletop_weather_station_resources:

Ressourcen
----------

* Wetterstations-Gehäuse als FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/cases/tree/master/tabletop_weather_station>`__)
* Demo-Anwendung (Download: `Windows <http://download.tinkerforge.com/kits/tabletop_weather_station/windows/tabletop_weather_station_demo_windows_latest.exe>`__, `Linux <http://download.tinkerforge.com/kits/tabletop_weather_station/linux/tabletop-weather-station-demo-linux_latest.deb>`__, `macOS <http://download.tinkerforge.com/kits/tabletop_weather_station/macos/tabletop_weather_station_demo_macos_latest.dmg>`__, `Source Code <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/demo>`__)
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
Source Code kann `hier <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/demo>`__
gefunden werden. Ausführbare Dateien stehen für Linux, macOS und Windows 
`hier <https://www.tinkerforge.com/de/doc/Downloads.html#kit-demos>`__ zur Verfügung.

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
`custom_screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/demo/tabletop_weather_station_demo/custom_screens.py>`__
hinzugefügt werden.

Ein einfacher Screen der die aktuelle Uhrzeit auf das Display schreibt könnte wie folgt 
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
`screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/demo/tabletop_weather_station_demo/screens.py>`__
gefunden werden.

Der obige Code fügt folgenden Tab zur Demo-Anwendung hinzu:

.. image:: /Images/Kits/tabletop_weather_station_screen_clock_600.jpg
   :scale: 100 %
   :alt: Clock Screen
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_screen_clock_1000.jpg

Pull Requests für neue Screens sind definitiv erwünscht, wir freuen uns schon darauf
eure schicken Screens in die Demo-Anwendung zu integrieren :-).


Konstruktion
------------

Für den Zusammenbau der Tisch-Wetterstation empfehlen wir zuerst alle Bricks/Bricklets
an den Plastikteilen zu befestigen und diese danach zusammenzusetzen.

.. image:: /Images/Exploded/tabletop_weather_station_explosion_master_700.png
   :scale: 100 %
   :alt: Explosionszeichnung
   :align: center
   :target: ../../_images/Exploded/tabletop_weather_station_explosion_master.png

Wenn zusätzlich ein RED Brick und/oder Outdoor Weather Bricklet verwendet werden
soll, können diese auf die gleiche Platte wie der Master Brick geschraubt werden:

.. image:: /Images/Exploded/tabletop_weather_station_explosion_complete_700.png
   :scale: 100 %
   :alt: Explosionszeichnung
   :align: center
   :target: ../../_images/Exploded/tabletop_weather_station_explosion_complete.png

Wie in den Explosionszeichnungen zu erkennen ist befestigen wir das Air Quality Bricklet
auf der Außenseite der Wetterstation. Dies stellt sicher dass die Hitze die von den
anderen Komponenten (LCD 128x64 Bricklet, Master Brick, eventuell RED Brick) abgegeben
wird nicht die Temperaturmessung des Air Quality Bricklets beeinflussen kann.

Es ist auch möglich das Air Quality Bricklet auf die Innenseite zu schrauben. In diesem
Fall empfehlen wir die Temperatur über die Temperatur-Kalibrierungsfunktion des Bricklets
zu korrigieren. Dies ist wichtig, da die ermittelte Temperatur auch zur Bestimmung der
Luftqualität und der Luftfeuchte verwendet wird.

Das folgende Video zeigt den Zusammenbau im Zeitraffer. An den wichtigen Stellen wird
das Video verlangsamt.

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/-3BiX39U5_A" frameborder="0" allowfullscreen></iframe>


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

Ein RED Brick kann zur Tisch-Wetterstation hinzugefügt werden und wird
unter den Master Brick geschraubt. In diesem Fall erfolgt die Stromversorgung
über den USB-Stecker des RED Bricks.

.. image:: /Images/Kits/tabletop_weather_station_transparent_back2_600.jpg
   :scale: 100 %
   :alt: RED Brick im Gehäuse der Tisch-Wetterstation
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_transparent_back2_1000.jpg

Mit dem RED Brick kann die Anwendung der Tisch-Wetterstation selbständig
ausgeführt werden. Um die Demo-Anwendung auf den RED Brick hochzuladen
klicke im RED Brick Tab des Brick Viewers auf "Program" und "New".

Wähle einen Namen und Python als Programmiersprache.

.. image:: /Images/Kits/tabletop_weather_station_red1.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

Füge die Dateien der Demo-Anwendung hinzu. Die Daten können auf
`GitHub gefunden werden <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/demo/tabletop_weather_station_demo>`__.
Wenn die Wetterstation bereits zuvor gelaufen ist kann die SQLite
Datenkank mit hochgeladen werden (``.tabletop_weather_station_demo.db`` Datei
deinem Home-Verzeichnis) um die bereits gespeicherten Messwerte weiter zu
verwenden.

.. image:: /Images/Kits/tabletop_weather_station_red2.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

Wähle ``main.py`` als Startdatei.

.. image:: /Images/Kits/tabletop_weather_station_red3.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

Es gibt in der Demo kein Standard-Input, alle anderen Optionen
können auf den Standardwerten bleiben.

.. image:: /Images/Kits/tabletop_weather_station_red4.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

.. image:: /Images/Kits/tabletop_weather_station_red5.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

.. image:: /Images/Kits/tabletop_weather_station_red6.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

.. image:: /Images/Kits/tabletop_weather_station_red7.jpg
   :scale: 100 %
   :alt: Hochladen der Demo-Anwendung über Brick Viewer
   :align: center

Nach dem der Upload fertig ist sollte die Demo-Anwendung automatisch
auf dem RED Brick laufen sobald dieser gestartet wird!


..
	.. _tabletop_weather_station_openhab:
	Smart Home Integration mit openHAB
	----------------------------------
	TODO
