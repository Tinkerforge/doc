
:shoplink: ../../../shop/kits/starter-kit-server-room-monitoring.html

.. include:: ServerRoomMonitoring.substitutions

.. _starter_kit_server_room_monitoring:

Starterkit: Serverraum-Überwachung
==================================

.. raw:: html

	{% tfgallery %}

	Kits/server_room_monitoring_right_basic_[100|800].jpg                  Server Room Monitoring Kit
	Kits/server_room_monitoring_left_front_open_basic_[100|800].jpg        Server Room Monitoring Kit
	Kits/server_room_monitoring_left_front_close_basic_[100|800].jpg       Server Room Monitoring Kit
	Kits/server_room_monitoring_front_right_red_close_[100|800].jpg        Server Room Monitoring Kit
	Kits/server_room_monitoring_back_right_red_open_[100|800].jpg          Server Room Monitoring Kit
	Kits/server_room_monitoring_front_right_seg_motion_close_[100|800].jpg Server Room Monitoring Kit
	Kits/server_room_monitoring_back_open_[100|800].jpg                    Server Room Monitoring Kit
	Kits/server_room_monitoring_case_front_open_[100|800].jpg              Server Room Monitoring Kit
	Kits/server_room_monitoring_side_close_[100|800].jpg                   Server Room Monitoring Kit
	Kits/server_room_monitoring_top_[100|800].jpg                          Server Room Monitoring Kit: Inhalt
	Kits/server_room_monitoring_alu_surface_[100|800].jpg                  Server Room Monitoring Kit: Oberfläche Aluminium
	Kits/server_room_monitoring_alu_in_hand_[100|800].jpg                  Server Room Monitoring Kit
	Kits/server_room_monitoring_in_rack3_[100|800].jpg                     Server Room Monitoring Kit: Im Serverrack
	Kits/server_room_monitoring_in_rack1_[100|800].jpg                     Server Room Monitoring Kit: Im Serverrack
	Kits/server_room_monitoring_in_rack2_[100|800].jpg                     Server Room Monitoring Kit: Im Serverrack

	{% tfgalleryend %}

Features
--------

* Modulare Low-Cost Serverraum-Überwachung (19" Rack, 1HE)
* Erweiterbar: Weitere Sensoren und Ein-/Ausgabe Module können einfach hinzugesteckt werden
* Stromversorgung per Ethernet (`PoE <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__) oder USB
* Konfiguration der eigenen Überwachungslösung ohne Programmierung möglich
* Für Programmierer: APIs für viele Sprachen verfügbar: 

  * |bindings|

* Open Source Soft- und Hardware mit `Nagios <https://www.nagios.org/>`__ und
  `Icinga <https://www.icinga.com/>`__ Unterstützung

Beschreibung
------------

Das *Starterkit: Serverraum-Überwachung* ist ein Open Source Kit um
Serverraum-Installationen zu überwachen. Das Basiskit ist mit folgenden Sensoren
ausgestattet: :ref:`Ambient Light Bricklet 3.0 <ambient_light_v3_bricklet>`
(überwacht z.B. die Raumbeleuchtung), :ref:`Humidity Bricklet 2.0 <humidity_v2_bricklet>`
(überwacht Luftfeuchtigkeit),
:ref:`Temperature Bricklet 2.0 <temperature_v2_bricklet>` (überwacht die Temperatur im
Rack) und ein :ref:`PTC Bricklet 2.0 <ptc_v2_bricklet>` mit Pt100 Temperaturfühler
(z.B. zum Überwachen der Temperatur in einem Server). Es ist Platz für bis zu acht PTC
Bricklets mit bis zu acht Temperaturfühlern vorgesehen.

Das Kit-Gehäuse kann direkt in einem 19" Server Rack befestigt werden (1HE). Mit 
weiteren Modulen des Tinkerforge :ref:`Baukastensystems<primer_products>`, 
wie zum Beispiel Bewegungsdetektoren, Ein-/Ausgabe Modulen (um Computer 
ein-/auszuschalten oder um Türen zu überwachen), kann das Kit flexibel an die 
eigenen Anforderungen angepasst werden.

Eine Nutzung ist auf zwei verschiedene Arten möglich:

1. **Nicht-Eigenständige Überwachung** (Standardkit)

   Alle Sensoren des Kits können aus der Ferne von anderen Rechnern per Ethernet
   über die angebotenen APIs (|bindings|) abgefragt werden. Somit können 
   individuelle Lösungen einfach realisiert werden. Beispiele für
   :ref:`Bash <starter_kit_server_room_monitoring_simple_monitoring>`,
   :ref:`Nagios/Icinga <starter_kit_server_room_monitoring_nagios_or_icinga_index>` und
   :ref:`Xively <starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index>`
   demonstrieren die Nutzungsmöglichkeiten.

2. **Eigenständige Überwachung** (Standardkit + RED Brick)

   Wird zusätzlich ein :ref:`RED Brick <red_brick>` im Kit verbaut, so kann 
   das Kit auch ohne externen Rechner betrieben werden. Über die 
   :ref:`Brick Viewer <brickv>` Software kann, ganz ohne Programmieraufwand, 
   die eigene Überwachungslösung realisiert werden. 

   Dazu müssen nur, mittels einfacher Schieberegler, für jeden Sensor 
   Wertebereiche definiert werden. Wird der definierte Wertebereich verlassen, 
   so kann unter anderem eine Benachrichtigung per E-Mail erfolgen.
   Es können Regeln sowohl für direkt angeschlossene Sensoren, aber auch für 
   andere, über das Netzwerk verfügbare, Tinkerforge Sensoren konfiguriert 
   werden. Intern läuft dazu eine Nagios-Installation, die über den Brick Viewer 
   konfiguriert wird. Das Nagios Web Interface ist über die Ethernetverbindung des
   RED Bricks erreichbar und ermöglicht die Ansicht der aktuellen Messwerte und 
   eventueller Probleme. Weitere Informationen können im  
   :ref:`RED Brick Kapitel <starter_kit_server_room_monitoring_red_brick>` der
   Serverraum-Überwachungsdokumentation gefunden werden.

   Erfahrene Nutzer können darüber hinaus die im Hintergrund laufende Nagios
   Installation modifizieren und über die Möglichkeiten des Brick Viewers hinaus
   konfigurieren.

Die Stromversorgung des Kits kann per 
`Power over Ethernet (PoE) <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__
oder USB (z.B. USB Steckernetzteil) erfolgen.

Sowohl Software als auch Hardware des Kits können modifiziert werden. Das 
Gehäuse besteht, mit Ausnahme der Frontblende die aus eloxiertem Aluminium 
besteht, 
aus bastelfreundlichem PMMA in das einfach neue Befestigungslöcher gebohrt
werden können. Befestigungslöcher für verschiedene
:ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` sind bereits vorhanden.

In der Frontblende können zusätzlich ein
:ref:`Motion Detector Bricklet 2.0 <motion_detector_v2_bricklet>`
und ein :ref:`Segment Display 4x7 Bricklet<segment_display_4x7_bricklet>`
befestigt werden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Beleuchtungsstärke                0Lux - 64000Lux in 0,01Lux Schritten
Temperatur (Ambient)              -40°C - 85°C in 0,01°C Schritten
Pt100 Sensor                      -20°C - 450°C
PTC Bricklet 2.0                  0,03125°C (15Bit) Auflösung
Humidity Bricklet 2.0             0% - 100% relative Luftfeuchtigkeit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (L x B x H)           482 x 92 x 44mm (19.0 x 3.62 x 1.75")
Gewicht                           250g
================================  ============================================================

.. _starter_kit_server_room_monitoring_resources:

Ressourcen
----------

* Serverraum-Überwachung Kit Gehäuse FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/server-room-monitoring/tree/master/case>`__)
* Beispielquelltext für :ref:`Einfaches Monitoring <starter_kit_server_room_monitoring_simple_monitoring>` (Download: `Shell <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/simple_monitoring/check_tf_temp_simple.sh>`__)
* Beispielquelltext für :ref:`Nagios/Icinga Plugin <starter_kit_server_room_monitoring_nagios_or_icinga_index>` (Download: `Python <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp.py>`__)
* Beispielquelltext für :ref:`Nagios/Icinga Extended Plugin <starter_kit_server_room_monitoring_extended_nagios_index>` (Download: `Python <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp_ext.py>`__)
* Beispielquelltext für :ref:`Sensordaten an Xively übertragen <starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index>` (Download: `Python <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/xively/server_room_monitoring.py>`__)

Erste Tests, Firmware-Aktualisierung und Konfiguration
------------------------------------------------------

Als ersten Schritt sollten die Bricks und Bricklets getestet werden
und deren Firmware gegebenenfalls aktualisiert werden.

Dazu muss der :ref:`Brick Daemon <brickd_installation>` und
der :ref:`Brick Viewer <brickv_installation>` installiert werden.

Als nächstes sollte das PTC Bricklet 2.0 konfiguriert und der 
Temperaturfühler (2-Leiter) angeschlossen werden. Wie dies funktioniert
ist :ref:`hier <ptc_v2_bricklet_jumper_configuration>` und
:ref:`hier <ptc_v2_bricklet_connectivity>` dokumentiert.

Anschließend wird die Ethernet Extension auf den Master Brick
gesteckt und alle Bricklets angeschlossen. Der Master Brick wird per USB
mit dem PC verbunden. Mit dem Brick Viewer können nun die Module getestet.
Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_brick_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_bricklet_plugin>`):

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
:ref:`hier <ethernet_extension_configuration>` beschrieben.

Nach den Tests und der Konfiguration ist sichergestellt, dass die Hardware
auch nach dem Einbau in das 19" Rack Gehäuse wie gewünscht funktioniert.


Konstruktion
------------

Der Aufbau der Basisversion des Kits ist
:ref:`hier <starter_kit_server_room_monitoring_construction>` beschrieben.

.. toctree::
   :hidden:

   Details <Construction>


.. _starter_kit_server_room_monitoring_red_brick:

RED Brick
---------

Wenn das Kit zusammen mit einem RED Brick benutzt wird, kann Nagios auf dem
RED Brick direkt über den Brick Viewer konfiguriert werden.

.. image:: /Images/Screenshots/brickv_srm_600.jpg
   :scale: 100 %
   :alt: Nagios Konfiguration im Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/brickv_srm.jpg

Der Server Monitoring Service (benötigt RED Brick Image >= 1.6 und Brick
Viewer >= 2.2.3) kann im :ref:`Services Tab <red_brick_brickv_settings_services>`
aktiviert werden.

Wenn der Server Monitoring Service aktiviert ist, ist es möglich Regeln
hinzuzufügen. Eine Regel besteht aus dem Typ des Bricklets (Temperature, Ambient
Light, Humidity oder PTC), dessen UID und einem Wertebereich für Warning und
Critical. Es können so viele Regeln hinzugefügt und konfiguriert
werden wie benötigt.

Es ist zusätzlich möglich automatische E-Mail-Benachrichtigungen für die
Warning/Critical Bereiche zu aktivieren. Dazu muss einfach die 
``Enable Email Notification`` Checkbox angeklickt und die
benötigten Informationen eingetragen werden.

Durch Klicken des *Save* Buttons wird die Konfiguration auf dem RED Brick
gespeichert. Nun kann über die Seite ``http://<red-brick-ip>/nagios/`` oder ``http://<red-brick-ip>/nagios3/ (für RED Brick Image Version 1.9 und älter)``
der aktuelle Zustand von Nagios abgerufen werden.

.. image:: /Images/Screenshots/nagios_srm_600.jpg
   :scale: 100 %
   :alt: Nagios Webseite
   :align: center
   :target: ../../_images/Screenshots/nagios_srm.jpg

Die Standardeinstellung für Username:Password lautet ``nagiosadmin``:``tf``.
Das Passwort kann über die Console durch folgenden Befehl geändert werden::

 sudo htpasswd -c -b /usr/local/nagios/etc/htpasswd.users nagiosadmin <PASSWORT>

RED Brick Image Version 1.9 und älter::

 sudo htpasswd -c -b /etc/nagios3/htpasswd.users nagiosadmin <PASSWORT>

Jede der Regeln wird in Nagios als ein Service angezeigt. Die Übersicht aller
Nagios Services kann über den ``Services`` Link in der Kategorie
``Current Status`` erreicht werden.

.. _starter_kit_server_room_monitoring_projects:

Projekte
--------

Es gibt verschiedene Anwendungen für das Starterkit: Serverraum-Überwachung. 
Nachfolgend werden Beispiele präsentiert, die als Startpunkt für eigene Projekte
dienen können.

.. _starter_kit_server_room_monitoring_simple_monitoring:

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
 hardware-version=2,0,0
 firmware-version=2,0,0
 device-identifier=ambient-light_v2-bricklet
 enumeration-type=available

Auslesen der verbundenen Sensoren (die UID ist anzupassen):

.. code-block:: bash

 $ tinkerforge --host ServerMonitoring call temperature-bricklet SCT31 get-temperature
 temperature=2487

 $ tinkerforge --host ServerMonitoring call ambient-light-v2-bricklet ajC get-illuminance
 illuminance=410

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


.. _starter_kit_server_room_monitoring_nagios_or_icinga_index:

Serverraum-Überwachung mit Nagios oder Icinga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
	Ein fertiges Icinga Check Plugin welches von `Netways <https://www.netways.de>`__
	getwartet wird kann im icinga exchange gefunden werden:
	`https://exchange.icinga.com/netways/check_tinkerforge <https://exchange.icinga.com/netways/check_tinkerforge>`__

`Icinga <https://www.icinga.com/>`__ und `Nagios <https://www.nagios.org/>`__
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

   Details <NagiosOrIcinga>

Der Abschnitt über :ref:`Erweiterungsmöglichkeiten
<starter_kit_server_room_monitoring_further_enhancements>` beinhaltet weitere
Nagios/Icinga Beispiele.


.. _starter_kit_server_room_monitoring_upload_sensor_data_to_xively_index:

Sensordaten an Xively übertragen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bei `Xively <https://www.xively.com/>`__ handelt es sich um einen Dienst, der die
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

   Details <UploadSensorDataToXively>


.. _starter_kit_server_room_monitoring_further_enhancements:

Erweiterungsmöglichkeiten
-------------------------

Gerne führen wir hier Mods, Erweiterungen oder Verbesserungen des Kits auf. 
Bitte gebt uns Bescheid, wir verlinken hier gerne eure Projekte.


.. _starter_kit_server_room_monitoring_extended_nagios_index:

Bewegungsmelder und Fehlercode Anzeige
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das 19" Gehäuse ist bereits mit Aussparungen für ein :ref:`Motion Detector Bricklet 2.0 <motion_detector_v2_bricklet>`
und ein :ref:`Segment Display 4x7 Bricklet <segment_display_4x7_bricklet>`
versehen. Das Motion Detector Bricklet 2.0 kann dazu genutzt werden Bewegung im
Server Raum zu detektieren. Mittels des Segment Display 4x7 Bricklets können
spezifische Fehlercodes angezeigt werden.

Die vollständige Projektbeschreibung kann 
:ref:`hier <starter_kit_server_room_monitoring_extended_nagios>` gefunden 
werden.

.. image:: /Images/Kits/server_room_monitoring_front_right_seg_motion_close_350.jpg
   :scale: 100 %
   :alt: Erweiterte Version des Kits
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_front_right_seg_motion_close_1000.jpg

.. toctree::
   :hidden:

   Details <ExtendedNagios>


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


Serverschranktür-Überwachung mit Distance IR Bricklet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Martin Seener hat einen Check für Nagios entwickelt, der mittels Distance IR
Bricklet überwacht, ob die Serverschranktür geöffnet wurde. Dazu ist das
Distance IR Bricklet im Serverschrank montiert und misst die Distanz zur
geschlossenen Tür. Ändert sich die Distanz signifikant wurde die Tür geöffnet.

Um einen passenden Schwellwert für den Check zu ermitteln wird über einen
längeren Zeitraum die Standardabweichung der Messwerte des Distance IR Bricklets
ermittelt. Auch dafür stellt Martin Seener ein Skript zur Verfügung.

Dieser Check ist der erste in einer `Sammlung
<https://github.com/martinseener/tinkerforge-nagios-checks>`__ von Nagios Checks
für Tinkerforge.
