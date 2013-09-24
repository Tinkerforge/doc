
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / Starterkit: Serverraum-Überwachung
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring.html

.. include:: ServerRoomMonitoring.substitutions

.. _starter_kit_server_room_monitoring:

Starterkit: Serverraum-Überwachung
==================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/server_room_monitoring_back_350.jpg",
	               "Kits/server_room_monitoring_back_800.jpg",
	               "Serverraum-Überwachungskit: Rückseite")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_in_rack3_100.jpg",
	             "Kits/server_room_monitoring_in_rack3_800.jpg",
	             "Serverraum-Überwachungskit: Im Serverrack")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_front_100.jpg",
	             "Kits/server_room_monitoring_front_800.jpg",
	             "Serverraum-Überwachungskit: Vorderseite")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_content_100.jpg",
	             "Kits/server_room_monitoring_content_800.jpg",
	             "Serverraum-Überwachungskit: Inhalt")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_extended_100.jpg",
	             "Kits/server_room_monitoring_extended_800.jpg",
	             "Serverraum-Überwachungskit: Erweiterte Version")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_iqr_100.jpg",
	             "Kits/server_room_monitoring_iqr_800.jpg",
	             "Serverraum-Überwachungskit: An/Aus-Schalter")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_in_rack1_100.jpg",
	             "Kits/server_room_monitoring_in_rack1_800.jpg",
	             "Serverraum-Überwachungskit: Im Serverrack")
	}}
	{{
	    tfdocimg("Kits/server_room_monitoring_in_rack2_100.jpg",
	             "Kits/server_room_monitoring_in_rack2_800.jpg",
	             "Serverraum-Überwachungskit: Im Serverrack")
	}}
	{{ tfdocend() }}

Features
--------

* Modulare Low-Cost Serverraum-Überwachung 
* 19" Rack montierbar (1HE)
* Steuerung und Versorgung über Ethernet (`PoE <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__)
* Erweiterbar: Falls nötig können Sensoren und Ein-/Ausgabe Module einfach hinzugesteckt werden
* API für viele Programmiersprachen: |bindings|
* Open Source Soft- und Hardware
* Nagios und Icinga Unterstützung

Beschreibung
------------

Das *Starterkit: Serverraum-Überwachung* ist ein Open Source Kit um
Serverraum Installationen zu überwachen. Das Basiskit ist mit folgenden Sensoren
ausgestattet: :ref:`Ambient Light Bricklet <ambient_light_bricklet>`
(überwacht z.B. die Raumbeleuchtung),
:ref:`Temperature Bricklet <temperature_bricklet>` (überwacht die Temperatur im
Rack) und ein :ref:`PTC Bricklet <ptc_bricklet>` mit Pt100 Temperatursensor
(z.B. zum Überwachen der Temperatur in einem Server). Ein
:ref:`Master Brick <master_brick>` und eine :ref:`Ethernet Extension
<ethernet_extension>`, mit `Power over Ethernet (PoE)
<https://de.wikipedia.org/wiki/Power_over_Ethernet>`__ Unterstützung, sind ebenfalls
enthalten. Das Kit-Gehäuse kann direkt in einem 19" Server Rack befestigt werden
und mittels weiterer Temperatursensoren und anderen Module (z.B. 
Bewegungsdetektoren, Ein-/Ausgabe Modulen (um Computer ein-/auszuschalten oder 
um Türen zu überwachen) etc.) erweitert werden. Mit den Tinkerforge
:ref:`Bausteinen<product_overview>` kann das Kit flexibel an die eigenen 
Anforderungen angepasst werden.

Ein oder mehrere steuernde Geräte, wie z.B. (Embedded-) PCs, Smartphones
oder Tables, können genutzt werden um die Module per Ethernet auszulesen und zu 
steuern. Eine Überwachung direkt per Internet ist daher möglich. Das System
kann per 
`Power over Ethernet (PoE) <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__
oder USB versorgt werden.

Die Soft- und Hardware des Kits können modifiziert werden. Das Gehäuse besteht 
aus bastelfreundlichem PMMA in das einfach neue Befestigungslöcher gebohrt
werden können. Befestigungslöcher für verschiedene
:ref:`Bricks <product_overview_bricks>` und
:ref:`Bricklets <product_overview_bricklets>` sind bereits vorhanden.
Folgende Module können direkt befestigt werden:

:ref:`Analog In Bricklet <analog_in_bricklet>`,
:ref:`Analog Out Bricklet <analog_in_bricklet>`,
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`,
:ref:`Industrial Digital Out 4 Bricklet <industrial_digital_out_4_bricklet>`,
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`,
:ref:`IO-4 Bricklet <io4_bricklet>`,
Motion Detector Bricklet (bald verfügbar)
und Segment Display 4x7 Bricklet (bald verfügbar).

Das Kit kann über alle verfügbaren Bindings (|bindings|) erfolgen.
Beispiel Implementierungen und Anwendungen für die Benutzung mit
`Nagios <http://www.nagios.org/>`__, `Icinga <https://www.icinga.org/>`__ und
weitere werden nachfolgend zur Verfügung gestellt.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Beleuchtungsstärke                0Lux - 900Lux in 0,1Lux Schritten
Temperatur (Ambient)              -40°C - 85°C in 0,01°C Schritten
Pt100 Sensor                      -20°C - 450°C
PTC Bricklet                      0,03125°C (15Bit) Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (L x B x H)           482 x 92 x 44mm (19.0 x 3.62 x 1.75")
Gewicht                           TBDg
================================  ============================================================

.. _starter_kit_server_room_monitoring_resources:

Ressourcen
----------

* Serverraum-Überwachung Kit Gehäuse FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/case>`__)
* Beispielcode *Simple Monitoring* (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/simple_monitoring/check_tf_temp_simple.sh>`__)
* Beispielcode *Nagios/Icinga Plugin* (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/nagios_icinga/check_tf_temp.py>`__)
* Beispielcode *Nagios/Icinga Extended Plugin* (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/nagios_icinga/check_tf_temp_ext.py>`__)
* Beispielcode *Sensordaten an Xively übertragen* (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/xively/server_room_monitoring.py>`__)

Erste Tests, Firmware-Aktualisierung und Konfiguration
------------------------------------------------------

Als ersten Schritt sollten die Bricks und Bricklets getestet werden
und deren Firmware gegebenenfalls aktualisiert werden.

Dazu muss der :ref:`Brick Daemon <brickd_installation>` und
der :ref:`Brick Viewer <brickv_installation>` installiert werden.

Als nächstes sollte das PTC Bricklet konfiguriert und der 
Temperatursensor (2-Leiter) angeschlossen werden. Wie dies funktioniert
ist :ref:`hier <ptc_bricklet_jumper_configuration>` und
:ref:`hier <ptc_bricklet_connectivity>` dokumentiert.

Anschließend wird die Ethernet Extension auf den Master Brick
gesteckt und alle Bricklets angeschlossen. Der Master Brick wird per USB
mit dem PC verbunden. Mit dem Brick Viewer können nun die Module getestet.
Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_plugin>`):

.. image:: /Images/Kits/server_room_monitoring_update_350.jpg
   :scale: 100 %
   :alt: Serverraum-Überwachung Hardware Update im Brick Viewer
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_update_orig.jpg

Im nächsten Schritt sollte jedes Modul überprüft werden. Im Brick Viewer besitzt
jedes Modul einen Reiter über dem eine modulspezifische Ansicht geöffnet werden
kann. Zeigen alle Ansichten sinnvolle Werte, funktioniert alles wie erwartet.
Als nächstes sollte die Ethernet Extension konfiguriert werden. 
In den folgenden Beispielen ist diese auf den Hostnamen
"ServerMonitoring" und DHCP konfiguriert. Zur Konfiguration muss der Master 
Brick Reiter geöffnet werden. Die weitere Konfiguration ist 
:ref:`hier <ethernet_configuration>` beschrieben.

Nach den Tests und der Konfiguration ist sichergestellt, dass die Hardware
auch nach dem Einbau in das 19" Rack Gehäuse wie gewünscht funktioniert.


Konstruktion
------------

Der Aufbau der Basisversion des Kits ist
:ref:`hier <starter_kit_server_room_monitoring_construction>` beschrieben.

.. toctree::
   :hidden:

   Construction


.. _starter_kit_server_room_monitoring_projects:

Projekte
--------

Es gibt verschiedene Anwendungen für das Starterkit: Serverraum-Überwachung. 
Nachfolgend werden Beispiele präsentiert, die als Startpunkt für eigene Projekte
dienen können.

Einfaches Monitoring
^^^^^^^^^^^^^^^^^^^^

In diesem Beispiel werden die :ref:`Shell Bindings <api_bindings_shell>` genutzt
um die Sensoren des Kits auszulesen.

Enumerierung der Bricks und Bricklets ("Ist alles angeschlossen?"):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring enumerate
 uid=6Dct25
 connected-uid=0
 position=0
 hardware-version=1,0,0
 firmware-version=2,1,0
 device-identifier=master-brick
 enumeration-type=available

 uid=fow
 connected-uid=6Dct25
 position=a
 hardware-version=1,0,0
 firmware-version=2,0,0
 device-identifier=ptc-bricklet
 enumeration-type=available

 uid=SCT31
 connected-uid=6Dct25
 position=b
 hardware-version=1,1,0
 firmware-version=2,0,1
 device-identifier=temperature-bricklet
 enumeration-type=available

 uid=ajC
 connected-uid=6Dct25
 position=d
 hardware-version=1,1,0
 firmware-version=2,0,1
 device-identifier=ambient-light-bricklet
 enumeration-type=available

Auslesen der verbundenen Sensoren (die UID ist anzupassen):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring call temperature-bricklet SCT31 get-temperature
 temperature=2487

 $ tinkerforge --host ServerMonitoring call ambient-light-bricklet ajC get-illuminance
 illuminance=41

 $ tinkerforge --host ServerMonitoring call ptc-bricklet fow get-temperature
 temperature=2603

Die Shell Bindings unterstützen die Ausführung von weiteren Shell Befehlen mit der
``--execute`` Option (siehe :ref:`Shell Bindings <ipcon_shell_output>` für weitere 
Informationen). Das nachfolgende Skript zeigt ein Beispiel wie der Rückgabewert
in Grad Celsius umgerechnet und anschließend in einer Variable für die 
weitere Benutzung gespeichert werden kann.

.. code-block:: bash

 #!/bin/sh

 HOST=ServerMonitoring
 UID=SCT31

 temp=$(tinkerforge --host $HOST call temperature-bricklet $UID get-temperature\
        --execute "echo '{temperature} / 100' | bc | xargs printf '%.2f\n'")
 echo $temp


Serverraum-Überwachung mit Nagios oder Icinga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Icinga <https://www.icinga.org/>`__ und `Nagios <http://www.nagios.org/>`__ 
sind Computer Überwachungswerkzeuge. Icinga ist ein Fork von Nagios
und gilt als rückwärtskompatibel zu Nagios. Die dokumentierten Beispiele 
beziehen sich auf die Nagios API sind aber ebenfalls mit Icinga kompatibel.

Beide Überwachungswerkzeuge nutzen Plugins, instantiiert als Service,
um die Auslastung des Prozessors, die Speicherbelegung, spezifische Software 
Prozesse oder physikalische Werte wie die Temperatur zu überwachen.

In diesem Beispiel wird ein eigenes Plugin geschrieben welches die Temperatur
überwacht. Mit ein paar Modifikationen kann dieses Plugin genutzt werden um 
andere Tinkerforge Module auszulesen und so eine spezifische Überwachung
zu ermöglichen.

.. image:: /Images/Kits/server_room_monitoring_icinga_screenshot_350.jpg
   :scale: 100 %
   :alt: Icinga Screenshot
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_icinga_screenshot_orig.jpg

Die vollständige Projektbeschreibung kann :ref:`hier
<starter_kit_server_room_monitoring_nagios_or_icinga>` hier gefunden werden.

.. toctree::
   :hidden:

   NagiosOrIcinga


Sensordaten an Xively übertragen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bei `Xively <https://xively.com/>`__ handelt es sich um einen Dienst, der die
Möglichkeit bietet das "Internet der Dinge" zu analysieren und zu visualisieren.
Der Dienst kann dazu genutzt werden verschiedene Geräte über das Internet
miteinander zu verbinden. Er kann eine Historie von Messwerten speichern und
visualisieren.

.. image:: /Images/Kits/server_room_monitoring_xively_350.jpg
   :scale: 100 %
   :alt: Xively Datenstrom konfiguration
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_xively_orig.jpg

Die vollständige Projektbeschreibung kann :ref:`hier
<starter_kit_server_room_monitoring_upload_sensor_data_to_xively>`
gefunden werden.

.. toctree::
   :hidden:

   UploadSensorDataToXively


Erweiterungsmöglichkeiten
-------------------------

Gerne führen wir hier Mods, Erweiterungen oder Verbesserungen des Kits auf. 
Bitte gebt uns Bescheid, wir verlinken hier gerne eure Projekte.

Bewegungs-Detektor und Fehlercode Anzeige
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das 19" Gehäuse ist bereits mit Aussparungen für ein Motion Detector Bricklet
(bald verfügbar) und ein Segment Display 4x7 Bricklet (ebenfalls bald verfügbar)
versehen. Das Motion Detector Bricklet kann dazu genutzt werden Bewegung im
Server Raum zu detektieren. Mittels des Segment Display 4x7 Bricklets können
spezifische Fehlercodes angezeigt werden.

Die vollständige Projektbeschreibung kann 
:ref:`hier <starter_kit_server_room_monitoring_extended_nagios>` gefunden 
werden.

.. image:: /Images/Kits/server_room_monitoring_extended_350.jpg
   :scale: 100 %
   :alt: Erweiterte Version des Kits
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_extended_1000.jpg

.. toctree::
   :hidden:

   ExtendedNagios

Remote Ein/Aus Schalter
^^^^^^^^^^^^^^^^^^^^^^^

Ein Industrial Quad Relay kann dazu genutzt werden einen Computer
Ein- bzw. Auszuschalten. Dazu muss nur der entsprechende Schalter des Computers
mit einem der Relais des Industrial Quad Relay Bricklets überbrückt werden. 
Als Software kann eine modifizierte Variante der zuvor vorgestellten Beispiele 
genutzt werden. Eine Anleitung wie ein Schalter mit dem Quad Relay überbrückt 
werden kann, kann im 
:ref:`Hardware Hacking für Anfänger Tutorial <starter_kit_hardware_hacking_for_beginners>`
gefunden werden.

.. image:: /Images/Kits/server_room_monitoring_iqr_350.jpg
   :scale: 100 %
   :alt: Kit Mit Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_iqr_1000.jpg
