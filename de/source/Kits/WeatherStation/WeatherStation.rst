
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

Es gibt nicht nur eine Art die Wetterstation aufzubauen. Nachfolgend zeigen wir
den Aufbau verschiedener Varianten. Das Starterkit Wetterstation ist einfach
zu erweitern oder zu modifizieren. 

Zum Beispiel können Bricks und Bricklets mittels Abstandsbolzen befestigt 
werden oder auch direkt angeschraubt werden um Platz zu sparen. Es sind
weitere Bohrlöcher vorgesehen um Analog In, Temperature oder IO-4 Bricklets
zu befestigen um weitere Sensoren auszulesen.

Das benutzte PMMA Plastik ist einfach zu bearbeiten, so dass falls benötigt
eigene Bohrlöcher oder Öffnungen geschaffen werden können.

Wetterstation (Basisversion)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Basisversion des Starterkits Wetterstation ist mit einem Ambient Light,
Barometer, Humidity und LCD 20x4 Bricklet, Master Brick, das 
Wetterstationsgehäuse inkl. Austauschseitenteil für einen DC Jack Adapter,
Bricklet und USB Kabeln sowie jede Menge Schrauben, Abstandsbolzen,
Muttern und Unterlegscheiben.

.. image:: /Images/Kits/weather_station_content_350.jpg
   :scale: 100 %
   :alt: Wetterstationskit Inhalt
   :align: center
   :target: ../../_images/Kits/weather_station_content_1200.jpg

Es gibt verschiedene Möglichkeiten die Bricks und Bricklets
in dem Gehäuse zu befestigen. In dieser Aufbauanleitung stellen wir eine 
Möglichkeit vor.

Wir beginnen damit den Master Brick auf die Rückseite zu schrauben.
Dazu nutzen wir 10mm Abstandsbolzen und Schrauben und schrauben den 
Brick auf die Innenseite der Rückseitenplatte. Dabei sollte die USB Buchse 
nach außen zeigen.

.. image:: /Images/Kits/weather_station_construction_back_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 1 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_back_1200.jpg

Im nächsten Schritt befestigen wir das Ambient Light Bricklet an der Oberseite
des Gehäuses. Um sicherzustellen, dass auch das geringste Licht von dem Sensor
eingefangen werden kann schrauben wir es direkt an die Oberseite des Gehäuses.
Dazu nutzen wir die langen 12mm Schrauben, stecken diese von Außen durch das 
Gehäuseteil und Schrauben von Innen jeweils eine Unterlegscheibe mit einer 
Mutter dagegen. Diese nutzen wir um den korrekten Abstand einzustellen. 
Anschließend schrauben wir das Ambient Light Bricklet mit jeweils einer
Mutter ein.

Anschließend sollten die Schrauben an der Unterseite bündig sein und die
Bricklet Buchse sollte 1mm Luft nach oben haben. So sollte es möglich sein
einfach das Brickletkabel einzustecken und dennoch den Sensor an einer guten
Position zu haben um gute Messungen zu erhalten.

.. image:: /Images/Kits/weather_station_construction_top_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 2 (Basis Version)
   :alt: Basic Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_1200.jpg

Humidity und Barometer Bricklet werden an der Frontseite befestigt.
Wir schrauben sie mittels 10mm Abstandsbolzen und Schrauben an der Innenseite
fest.

Auf diese Art ist genügend Platz zwischen den Sensoren um gute Messergebnisse
zu  erlauben. Falls auf der Unterseite irgendwann größere Komponenten befestigt 
werden sollen, so können die Bricklets auch genauso wie das Ambient Light Bricklet
angeschraubt werden um Platz zu sparen.

Hiernach sollten die Brickletkabel angeschlossen werden um im nächsten Schritt
das LCD Bricklet einfacher installieren zu können.

.. image:: /Images/Kits/weather_station_construction_front1_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 3 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_front1_1200.jpg

Nun befestigen wir das LCD 20x4 Bricklet an dem Gehäuse. Die einfachste 
Möglichkeit ist vermutlich damit zu beginnen die 10mm Abstandsbolzen an
die schwarze LCD Bricklet-Platine zu schrauben. Anschließend steckt man
das LCD oben drauf und nutzt jeweils eine Mutter und eine Unterlegscheibe
um das komplette LCD Bricklet mit den langen 12mm Schrauben auf die Frontseite
des Gehäuses zu schrauben.

In dieser Anleitung verlegen wir die Bricklet Kabel unter dem LCD 20x4 Bricklet.
Es ist auch möglich diese zwischen den beiden Leiterplatten zu verlegen,
somit wären die Kabel etwas mehr verdeckt.

.. image:: /Images/Kits/weather_station_construction_front2_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 4 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_front2_1200.jpg

Um das Gehäuse nun zusammenzusetzen beginnen wir damit
die Oberseite in die Rückseite einzusetzen. Anschließend
schließen wir das Ambient Light Bricklet an den Master Brick an.

.. image:: /Images/Kits/weather_station_construction_top_to_back_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 5 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_to_back_1200.jpg

Als nächstes setzen wir die Seitenteile ein und bauen uns Abstandshalter.
Diese sollen eine Höhe von 40mm haben und werden jeweils aus zwei 9mm, einem
12mm und einem 10mm Abstandsbolzen zusammengesetzt. Die Abstandsbolzen 
werden anschließend auf die Rückseite des Gehäuses jeweils durch eine Schraube 
von Außen geschraubt.

.. image:: /Images/Kits/weather_station_construction_top_back_spacer_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 6 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_back_spacer_1200.jpg

Nun müssen nurnoch die drei anderen Bricklets angeschlossen werden.
Dies funktioniert am besten, wenn Front- und Rückseite nebeneinander liegen.

.. image:: /Images/Kits/weather_station_construction_cabling_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 7 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_cabling_1200.jpg

Zum Schluss müssen wir nurnoch die Frontseite auf die Rückseite stecken
und beides über die vier fehlenden Schrauben verbinden. Das war es! Nun ist
die Wetterstation aufgebaut.

.. image:: /Images/Kits/weather_station_construction_350.jpg
   :scale: 100 %
   :alt: Wetterstationsaufbau Schritt 8 (Basis Version)
   :align: center
   :target: ../../_images/Kits/weather_station_construction_1200.jpg


WLAN Wetterstation
^^^^^^^^^^^^^^^^^^

Die Wetterstation ist groß genug um eine WIFI Extension einzubauen um 
die Station drahtlos zu steuern. In dieser Anleitung werden wir eine Step-Down 
Power Supply zusammen mit einem DC Jack Adapter nutzen um die Station mit Strom
zu versorgen. Als Alternative wäre es auch möglich die Station über eine
USB Power Supply zu versorgen, dann wären DC Jack Adapter und Step-Down
Power Supply nicht notwenig.

Wir starter damit den Stapel, bestehend aus Step-Down Power Supply,
Master Brick und WIFI Extension auf die Rückseite des Gehäuses zu schrauben.
Es ist eine Aussparung vorhanden damit die Step-Down Power Supply
auch ohne Abstandsbolzen direkt auf die Rückseite geschraubt werden kann.

.. image:: /Images/Kits/weather_station_construction_wifi_stack_350.jpg
   :scale: 100 %
   :alt: WLAN Wetterstation Aufbau Schritt 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_stack_1200.jpg

Der DC Jack Adapter kann auf die Rückseite mit einem 21mm Abstandshalter 
aufgeschraubt werden. Dieser wird aus einem 9mm und einem 12mm Abstandshalter 
aufgebaut. Dieser Abstandshalter wird wiederrum über eine Schraube an der 
Rückseite des Gehäuses geschraubt. Der DC Jack Adapter wird mit einer Mutter
befestigt.

Wenn alles korrekt verschraubt ist, sollte der DC Jack Adapter in die 
Aussparung in dem Seitenteil passen.

.. image:: /Images/Kits/weather_station_construction_wifi_dc_jack_350.jpg
   :scale: 100 %
   :alt: WLAN Wetterstation Aufbau Schritt 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_dc_jack_1200.jpg

Das war es! Wir müssen nun nur wieder die Vorderseite auf die Rückseite 
schrauben. Falls eine Tinkerforge Antenne genutzt werden soll, so muss dies die 
große RP-SMA oder die Externe sein. Die kleine Antenne passt nicht.

.. image:: /Images/Kits/weather_station_construction_wifi_ready_350.jpg
   :scale: 100 %
   :alt: WLAN Wetterstation Aufbau Schritt 3
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_ready_1200.jpg


Raspberry Pi Wetterstation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Wetterstation kann über ein Embedded Board wie z.B. das Raspberry Pi
gesteuert werden. Das Raspberry Pi kann direkt in das Gehäuse eingebaut werden
auch wenn es nicht einfach ist alles zu integrieren.

Wir installieren ein Master Brick, eine Step-Down Power Supply, ein DC Jack
Adapter und das Raspberry Pi in dem Gehäuse. Das Raspberry Pi (und das Master 
Brick) werden über den DC Jack Adapter durch die Step-Down Power Supply 
versorgt.

Wie der DC Jack Adapter befestigt werden kann ist oben beschrieben
(WLAN Wetterstation).

Die Step-Down Power Supply (mit dem Master Brick obenauf) ist über
10mm Abstandsbolzen befestigt. Die SD Karte kann dabei unter die Step-Down
Power Supply geschoben werden. Der Micro USB Stecker führt dabei links
an dem Step-Down Power Supply Abstandsbolzen vorbei. Über die Ausschnitte
im Gehäuse kann das Raspberry Pi mittels Kabelbindern befestigt werden.

Der grüne 5V Ausgang auf der Step-Down Power Supply wird dazu genutzt
um das Raspberry Pi über einen Micro USB Stecker mit Strom zu versorgen.
Der schwarze Stecker ist hingegen mit dem DC Jack Adapter verbunden.
Der Master Brick wird einfach mit einem kurzen Mini USB Kabel an das Raspberry
Pi angeschlossen.

.. image:: /Images/Kits/weather_station_construction_rpi_front_350.jpg
   :scale: 100 %
   :alt: Raspberry Pi Weather Station construction step 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_front_1200.jpg

Auf der Rückansicht sehen wir wie das Raspberry Pi eingebaut wurde.

.. image:: /Images/Kits/weather_station_construction_rpi_back_350.jpg
   :scale: 100 %
   :alt: Raspberry Pi Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_back_1200.jpg

So wie das Raspberry Pi verbaut wurde kann auch ein Netzwerkkabel angeschlossen 
werden. Natürlich ist es auch möglich das Raspberry Pi 180° gedreht einzubauen.
Hierdurch kann ein kürzeres Mini USB Kabel verwendet werden, aber die Ethernet
Buchse ist nicht mehr so gut zugänglich.

Die Befestigung des Raspberry Pis an der Außenseite der Rückseite stellt eine 
weitere Möglichkeit dar.

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
