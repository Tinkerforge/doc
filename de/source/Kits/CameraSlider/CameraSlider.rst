
.. _starter_kit_camera_slider:

Starterkit: Kameraschlitten
===========================

.. raw:: html

	{% tfgallery %}

	Kits/kit_camera_slider_complete1_[100|800].jpg  Kameraschlitten: Komplettes Kit
	Kits/kit_camera_slider_content_[100|800].jpg    Kameraschlitten: Inhalt
	Kits/kit_camera_slider_camera1_[100|800].jpg    Kameraschlitten: Mit Videokamera
	Kits/kit_camera_slider_camera2_[100|800].jpg    Kameraschlitten: Mit Kamera
	Kits/kit_camera_slider_w_lcd1_[100|800].jpg     Kameraschlitten: Mit LCD
	Kits/kit_camera_slider_w_lcd2_[100|800].jpg     Kameraschlitten: Mit LCD

	{% tfgalleryend %}

.. note::

 Das Starterkit: Kameraschlitten ist abgekündigt und wird nicht mehr verkauft.

Features
--------

* Programmierbare Kamerafahrten und Zeitrafferaufnahmen
* Jederzeit einfach modifizierbar
* Mit MakerBeams eigene Halterungen bauen
* Weitere Funktionen mittels anderer Bricks und Bricklets

Beschreibung
------------

Das *Starterkit: Kamerschlitten* erlaubt eine flüssige automatische
Bewegung von Foto- und Videokameras. Über die angebotene Demo Anwendung kann
der Schlitten frei bewegt und Zeitrafferaufnahmen erstellt werden. Mit den
angebotenen APIs kann der Schlitten aber auch in eigene Projekte integriert
werden.

Das Kit ist aus `MakerBeams <https://www.tinkerforge.com/de/shop/makerbeam.html>`__
aufgebaut. Andere Beams können ohne großen Aufwand
befestigt werden, so dass sehr einfach für andere Geräte eigene Halterungen
konstruiert werden können. Damit wird das Kit zur Achse zum linearen
Bewegen von Lasten (Linearachse).

Ein :ref:`Stepper Brick <stepper_brick>`
bewegt den Schlitten millimetergenau und kann mit weiteren
:ref:`Bricks <primer_bricks>` und :ref:`Bricklets <primer_bricklets>`
erweitert werden. So kann zum Beispiel die Kamera automatisch von einem
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
ausgelöst werden oder zusammen mit
:ref:`RED Brick <red_brick>` und
`HDMI Touchscreen <https://www.tinkerforge.com/de/shop/accessories/red-brick/hdmi-display-5-inch.html>`__
eine autarke Lösung realisiert werden.

Das nachfolgende Video zeigt verschiedene Anwendungen und Erweiterungen:

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/lg0sdG7tfr4" frameborder="0" allowfullscreen></iframe>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Bewegungsspielraum                70cm (erweiterbar auf bis zu 275cm)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           94 x 15 x 4cm (37 x 5.9 x 5.5")
Gewicht                           1,3kg
================================  ============================================================


.. _starter_kit_camera_slider_resources:

Ressourcen
----------

* Kameraschlitten-Halterungen als FreeCAD CAD Dateien (`Download <https://github.com/Tinkerforge/camera-slider/tree/master/brackets>`__)
* :ref:`starter_kit_camera_slider_demo` (Download: `Windows <https://download.tinkerforge.com/kits/camera_slider/windows/starter_kit_camera_slider_demo_windows_latest.exe>`__, `Linux <https://download.tinkerforge.com/kits/camera_slider/linux/starter-kit-camera-slider-demo_linux_latest.deb>`__, `macOS <https://download.tinkerforge.com/kits/camera_slider/macos/starter_kit_camera_slider_demo_macos_latest.dmg>`__, `RED Brick <https://download.tinkerforge.com/kits/camera_slider/red_brick/starter_kit_camera_slider_demo_red_brick_latest.tfrba>`__, `Quelltext <https://github.com/Tinkerforge/camera-slider/tree/master/demo>`__)


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden.
Schließe das LED Strip Bricklet an den Master Brick an und verbinde es per USB
mit dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_brick_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_bricklet_plugin>`):

.. image:: /Images/Kits/kit_camera_slider_update.jpg
   :scale: 100 %
   :alt: Kameraschlitten Update im Brick Viewer
   :align: center

Im nächsten Schritt sollte der Stepper Brick mit Schrittmotor und 24V Netzteil
wie :ref:`hier <stepper_brick_test>` beschrieben getestet werden. Anschließend
kann damit begonnen werden das Kit zusammenzubauen.

Konstruktion
------------

Der Aufbau der Basisversion des Kits ist :ref:`hier
<starter_kit_camera_slider_construction_basic>` beschrieben.

.. toctree::
   :hidden:

   Basisversion <Construction_Basic>

.. image:: /Images/Kits/kit_camera_slider_construction_collage_800.jpg
   :scale: 100 %
   :alt: Konstruktionscollage des Kameraschlitten Kits
   :align: center
   :target: Construction_Basic.html

Anstatt 900mm MakerBeams können auch 1500mm MakerBeams oder sogar zwei 1500mm
MakerBeams hintereinander verwendet werden um einen Bewegungsbereich von bis
zu 3m zu erreichen. Wie der Rahmen der Basisversion dafür verändert werden kann
ist :ref:`hier <starter_kit_camera_slider_construction_longer_frame>`
beschrieben.

.. toctree::
   :hidden:

   Mit verlängertem Rahmen <Construction_LongerFrame>

.. image:: /Images/Kits/kit_camera_slider_longer_frame_complete1_600.jpg
   :scale: 100 %
   :alt: Kameraschlitten Kit mit 3m langem Rahmen
   :align: center
   :target: Construction_LongerFrame.html

Statt eines externen PCs kann der Kameraschlitten auch über ein RED Brick mit
HDMI Touchscreen bedient werden. Wie der RED Brick und der Touchscreen am Rahmen
befestigt werden können ist :ref:`hier
<starter_kit_camera_slider_construction_red_brick>` beschrieben.

.. toctree::
   :hidden:

   Mit RED Brick und Touchscreen <Construction_REDBrick>

.. image:: /Images/Kits/kit_camera_slider_red_brick_step8_600.jpg
   :scale: 100 %
   :alt: Kameraschlitten Kit mit RED Brick und Touchscreen
   :align: center
   :target: Construction_REDBrick.html


.. _starter_kit_camera_slider_demo:

Demo Anwendung
--------------

Die Demo Anwendung demonstriert zwei Verwendungsmöglichkeiten für das Kit:

* Linearbewegung
* Bewegte Zeitrafferaufnahmen

Als Erstes müssen Host und Port eingestellt werden. Wenn der Stepper Brick
per USB am PC angeschlossen ist, dann ist "localhost" und "4223" schon richtig.
Wenn das Kit um eine :ref:`Master Extension <primer_master_extensions>`
erweitert wurde oder an einem anderen PC angeschlossen ist, dann muss als Host
die IP Adresse oder der Hostname der Extension oder des anderen PCs, an dem
das Kit angeschlossen ist, angegeben werden. Jetzt auf den "Connect" Knopf
klicken, um die Verbindung herzustellen.

.. image:: /Images/Kits/kit_camera_slider_demo_connection_350.jpg
   :scale: 100 %
   :alt: Kameraschlitten Demo Anwendungs Screenshot: Connection Tab
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_demo_connection.jpg

Calibration Tab
^^^^^^^^^^^^^^^

Zu Beginn kennt die Demo weder die aktuelle Position des Wagens noch dessen
Bewegungsspielraum. Bevor die Demo den Wagen bewegen kann muss dessen minimale
und maximale Position kalibriert werden:

* Wählen den Stepper Brick aus, der am Kameraschlitten angebracht ist.
* Klicke auf den "Start" Knopf, um die Kalibrierung zu beginnen.
* Nutze die "Forward" und "Backward" Knöpfe, um den Wagen zu einem Ende des
  Rahmens zu fahren. Dann klicke auf den "Set Minimum" Knopf.
* Nutze die "Forward" und "Backward" Knöpfe, um den Wagen zum anderen Ende des
  Rahmens zu fahren. Dann klicke auf den "Set Maximum" Knopf.
* Klicke auf den "Apply" Knopf, um die Kalibrierung anzuschließen.

Jetzt kennt und speichert sich die Demo die aktuelle Position und den
Bewegungsspielraum des Wagens. Falls der Wagen nach der Kalibrierung von Hand
bewegt wird, z.B. beim Transport, dann muss die Kalibrierung wiederholt werden.

.. image:: /Images/Kits/kit_camera_slider_demo_calibration_350.jpg
   :scale: 100 %
   :alt: Kameraschlitten Demo Anwendungs Screenshot: Calibration Tab
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_demo_calibration.jpg

Automatic Power Control
"""""""""""""""""""""""

Wenn "Automatic Power Control" aktiviert ist, dann aktiviert die Demo
automatisch die Stromversorgung des Schrittmotors nur dann, wenn der Wagen sich
zu einer neuen Position bewegen soll. Die Stromversorgung wird automatisch
wieder deaktiviert sobald der Wagen die neue Position erreicht hat. Dadurch
werden der Stromverbrauch und die Motorgeräusche reduziert, wenn der Wagen sich
nicht bewegt.

Daraus ergibt sich, dass der Wagen nicht aktiv durch den Schrittmotor in der
aktuelle Position gehalten wird, wenn sich der Wagen gerade nicht bewegt.
Dies ist kein Problem solange der Kameraschlitten in einem waagerechten Aufbau
verwendet wird. Aber in einem geneigtem oder senkrechtem Aufbau wird der Wagen
von der Schwerkraft bewegt werden. In diesem Fall kann "Automatic Power
Control" abgeschaltet werden, um den Schrittmotor durchgehend mit Strom zu
versorgen und den Wagen durchgehend in seiner Position zu halten.

Linear Motion Tab
^^^^^^^^^^^^^^^^^

Auf diesem Tab können dem Wagen neue Zielpositionen vorgegeben werden, die dann
mit der eingestellten Geschwindigkeit und (De-)Beschleunigung angefahren
werden. Neue Zielpositionen können mit dem "Target Position" Regler oder mit
dem Eingabefeld rechts daneben vorgegeben werden. Sobald sich die Zielposition
ändert bewegt sich der Wagen auf die neue Position zu.

Die "Forward" und "Backward" Knöpfe funktionieren genauso wie auf dem
"Calibration" Tab. Allerdings bewegt sich der Wagen jetzt mit der eingestellten
Geschwindigkeit und (De-)Beschleunigung.

Die Zielposition kann nur geändert werden, wenn der Wagen stillsteht. Der
Wagen kann durch einen Klick auf den "Stop" Knopf mit der eingestellten
Debeschleunigung angehalten werden, oder durch einen Klick auf den "Full Break"
Knopf mit der maximalen Debeschleunigung.

.. image:: /Images/Kits/kit_camera_slider_demo_linear_motion_350.jpg
   :scale: 100 %
   :alt: Kameraschlitten Demo Anwendungs Screenshot: Linear Motion Tab
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_demo_linear_motion.jpg

Time Lapse Tab
^^^^^^^^^^^^^^

Auf diesem Tab können bewegte Zeitrafferaufnahmen konfiguriert werden. Die
Demo unterstützt es Bilder in festen Zeit- und Abstandsintervallen aufzunehmen.

Da es viele verschiedene Arten und Weisen gibt eine Kamera auszulösen, ist in
der Demo keine bestimmte Art und Weise vorgegeben. Stattdessen kann ein
Kommandozeilen-Befehl angegeben werden, der dann für das Auslösen der Kamera
sorgt. Standardmäßig verwendet die Demo `gphoto2 <http://www.gphoto.org/>`__,
das ein breites Spektrum an Kameras unterstützt::

  gphoto2 --capture-image

Die Windows und macOS Installer der Demo bringen gphoto2 direkt mit und das
Debian Package für Linux hängt vom Debian gphoto2 Package ab.

Der eingegebene Kommandozeilen-Befehl kann durch einen Klick auf den "Test"
Knopf getestet werden. Der Befehl wird ausgeführt und das Ergebnis auf dem
"Log" Tab angezeigt.

.. image:: /Images/Kits/kit_camera_slider_demo_time_lapse_350.jpg
   :scale: 100 %
   :alt: Kameraschlitten Demo Anwendungs Screenshot: Time Lapse Tab
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_demo_time_lapse.jpg

gphoto2 Support
"""""""""""""""

Üblicherweise funktioniert gphoto2 direkt unter Linux, benötigt aber etwas
Vorbereitung unter Windows und macOS.

Unter **Windows** hat der "Time Lapse" Tab oben einen weiteren Knopf namens
"Start Zadig". `Zadig <https://zadig.akeo.ie/>`__ kann einen USB Treiber für
eine angeschlossenen Kamera installieren, so dass gphoto2 mit der Kamera
kommunizieren kann:

* Schließe die Kamera an USB an.
* Klicke auf den "Start Zadig" Knopf.
* Wähle in Zadig die angeschlossenen Kamera aus. Möglicherweise wird diese als
  "Digital Still Camera" aufgeführt.
* Klicke auf den "Replace Driver" Knopf in Zadig.
* Schließe Zadig sobald der Treiber ersetzt wurde.

Jetzt sollte gphoto2 mit der Kamera kommunizieren können. Um den installierten
Treiber wieder zu entfernen muss im Windows Geräte-Manager die Kamera
ausgewählt und auf den "Deinstallieren" Knopf geklickt werden. Danach die
Kamera von USB abstecken und wieder anstecken. Windows sollte jetzt wieder den
vorherigen Treiber verwenden.

Auf **macOS** hat der "Time Lapse" Tab oben zwei weitere Knöpfe namens
"Enable" und "Disable". Diese deaktivieren und aktivieren macOS eigene
Behandlung für USB Kameras, die mit gphoto2 kollidiert. Klicke auf den "Enable",
um gphoto2 zu benutzen. Klicke auf den "Disable" Knopf, wenn gphoto2 nicht mehr
gebraucht wird und macOS eigene Behandlung für USB Kameras wieder aktiviert
werden soll.

Timing and Bewegung
"""""""""""""""""""

Nach einem Klick auf den "Start" Knopf bewegt sich der Wagen zur "Start
Position" und wartet dort für "Initial Delay" Sekunden bevor der
Auslösebefehl das erste Mal ausgeführt wird. Danach bewegt sich der Wagen zur
nächsten Position und wartet dort für "Interval" Sekunden bevor der
Auslösebefehl erneut ausgeführt wird. Dieser Ablauf wiederholt sich bis der
Auslösebefehl "Image Count" ausgeführt wurde und die "End Position" erreicht
ist, oder auf den "Abort" Knopf geklickt wurde.

Bei der Abarbeitung der initialen Verzögerung und des Intervalls wird die Zeit
berücksichtigt, die die Ausführung des Auslösebefehls und die Bewegung des
Wagens zur nächsten Position benötigt. Dadurch kann ein möglichst genaues
Timing erreicht werden, so lange die Zeit für die Ausführung des Auslösebefehls
und die Bewegung des Wagens zur nächsten Position nicht länger dauert als das
eingestellte Intervall.

Die Geschwindigkeit und (De-)Beschleunigung des Wagens kann auf dem "Linear
Motion" Tab eingestellt werden.

Industrial Quad Relay Bricklet als Auslöser
"""""""""""""""""""""""""""""""""""""""""""

Viele Kameras unterstützen Kabelauslöser die im wesentlichen einfache Schalter
sind. Ein :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
kann als Schalter für einen Kabelauslöser verwendet werden, anstatt gphoto2 als
Auslöser zu verwenden.

Die Canon EOS Kameraserie verwendet eine 3-polige 2,5mm Stereo-Klinkenbuchse
als Anschluss für einen Kabelauslöser mit Fokusier- und Auslösefunktion. Eine
detaillierte Übersicht über die genau Anschlussbelegung der Canon EOS Kameras
und anderer Kameraserien gibt es `hier
<https://www.doc-diy.net/photo/remote_pinout/>`__. Mit einem passendem Kabel und
einem Industrial Quad Relay Bricklet haben wir uns unseren eigenen Kabelauslöser
gebaut:

.. image:: /Images/Kits/kit_camera_slider_iqr_350.jpg
   :scale: 100 %
   :alt: Selbstgebauter Canon EOS Kabelauslöser
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_iqr_1500.jpg

Ein Auslöse-Skript für ein Industrial Quad Relay Bricklet kann
`hier <https://github.com/Tinkerforge/camera-slider/blob/master/demo/starter_kit_camera_slider_demo/trigger_iqr.py>`__
heruntergeladen werden. Um es nutzen zu können müssen Python und die
:ref:`Python API Bindings <api_bindings_python>` installiert sein. Seine
Kommandozeilen-Syntax ist wie folgt::

  python <path>/trigger_iqr.py <host> <port> <iqr-uid> <relay> <trigger-duration> <wait-duration>

Hier ein Beispiel für ein Industrial Quad Relay Bricklet mit UID ``n5d``
erreichbar unter localhost an Port 4223. Das Auslöse-Skript wurde zuvor auf
Karls Windows Desktop heruntergeladen::

  python C:/Users/Karl/Desktop/trigger_iqr.py localhost 4223 n5d 0 50 1000

Der Auslöse- und Masse-Pin des Kabelauslöser sind an Relais 0 angeschlossen.
Das Relais verbindet für 50 Millisekunden die beiden Pins. Danach wartet das
Skript für 1000 Millisekunden, um der Kamera Zeit zu geben, das aufgenommene
Bild zu verarbeiten und zu speichern.

RED Brick Programm als Auslöser
"""""""""""""""""""""""""""""""

Wenn der Zeitrafferaufbau einen :ref:`RED Brick <red_brick>` beinhaltet, dann
kann auch ein anderes :ref:`RED Brick Programm <red_brick_program_tab>` für
die Auslöselogik sorgen. Ein Auslöse-Skript dafür kann hier
`hier <https://github.com/Tinkerforge/camera-slider/blob/master/demo/starter_kit_camera_slider_demo/trigger_red.py>`__
heruntergeladen werden. Seine Kommandozeilen-Syntax ist wie folgt::

  python <path>/trigger_red.py <host> <port> <red-uid> <program-identifier> <wait-duration>

Hier ein Beispiel für ein RED Brick mit UID ``3JpHZL`` erreichbar unter
localhost an Port 4223, dass das Programm ``trigger-example`` einmal startet
und danach 1000 Millisekunden wartet. Die Demo für das RED Brick beinhaltet
das Auslöse-Skript schon, so das der Pfad zu Skript entfallen kann::

  python trigger_red.py localhost 4223 3JpHZL trigger-example 1000

Das Programm kann dann die spezielle Auslösesequenz für den Zeitrafferaufbau
ausführen.

.. _starter_kit_camera_slider_demo_red_brick_import:

Auf RED Brick importieren
^^^^^^^^^^^^^^^^^^^^^^^^^

Die Demo Anwendung kann zur autarken Verwendung auch auf ein :ref:`RED Brick
<red_brick>` hochgeladen werden. Lade dazu die aktuelle Version als `Archiv für
das  RED Brick
<https://download.tinkerforge.com/kits/camera_slider/red_brick/starter_kit_camera_slider_demo_red_brick_latest.tfrba>`__
herunter und importiere es mittels des :ref:`RED Brick Import/Export
<red_brick_brickv_import_export_tab>` Tab des Brick Viewers. Die Demo wird
dann automatisch im Vollbild starten.

.. image:: /Images/Kits/kit_camera_slider_w_lcd1_600.jpg
   :scale: 100 %
   :alt: Demo auf RED Brick
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_w_lcd1_1500.jpg
