
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_red_tilted_top_front_350.jpg",
	               "Bricks/brick_red_tilted_top_front_800.jpg",
	               "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_hand_100.jpg",
	             "Bricks/brick_red_hand_800.jpg",
	             "RED Brick in einer Hand")
	}}
	{{
	    tfdocimg("Bricks/brick_red_master_temp_eth_100.jpg",
	             "Bricks/brick_red_master_temp_eth_800.jpg",
	             "RED Brick mit Master Brick, Temperature Bricklet und Ethernet Extension")
	}}
	{{
	    tfdocimg("Bricks/brick_red_w_monitor_100.jpg",
	             "Bricks/brick_red_w_monitor_800.jpg",
	             "RED Brick mit Step-Down Power Supply und HDMI-Monitor")
	}}
	{{
	    tfdocimg("Bricks/brick_red_tilted_top_back_100.jpg",
	             "Bricks/brick_red_tilted_top_back_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_tilted_bottom_front_100.jpg",
	             "Bricks/brick_red_tilted_bottom_front_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_tilted_bottom_back_100.jpg",
	             "Bricks/brick_red_tilted_bottom_back_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_side_front_100.jpg",
	             "Bricks/brick_red_side_front_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_side_back_100.jpg",
	             "Bricks/brick_red_side_back_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_top_100.jpg",
	             "Bricks/brick_red_top_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_bottom_100.jpg",
	             "Bricks/brick_red_bottom_800.jpg",
	             "RED Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_red_big_stack_100.jpg",
	             "Bricks/brick_red_big_stack_800.jpg",
	             "RED Brick mit großem Stapel")
	}}
	{{
	    tfdocimg("Bricks/brick_red_caption_top_100.jpg",
	             "Bricks/brick_red_caption_top_800.jpg",
	             "RED Brick mit Beschreibung")
	}}
	{{
	    tfdocimg("Bricks/brick_red_caption_bottom_100.jpg",
	             "Bricks/brick_red_caption_bottom_800.jpg",
	             "RED Brick mit Beschreibung")
	}}
	{{
	    tfdocimg("Dimensions/red_brick_dimensions_100.png",
	             "Dimensions/red_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}



Features
--------

* Steuert andere Bricks und Bricklets
* Führt direkt dein geschriebenes Programm auf dem Brick aus
* Unterstützt nahezu alle Programmiersprachen

.. _red_brick_description:

Beschreibung
------------

Der Rapid Embedded Development :ref:`Brick <primer_bricks>` (RED Brick) kann
andere Bricks und :ref:`Bricklets <primer_bricklets>`
steuern. Die aktuell unterstützten Sprachen: C/C++, C#, Delphi/Lazerus, Java,
JavaScript, MATLAB/Octave, Perl, PHP, Python, Ruby, Shell und Visual Basic .NET,
können direkt auf dem Brick ausgeführt werden.

Ein Programm, das Bricks und Bricklets steuert, kann auf einem normalen
PC oder Mac geschrieben und getestet werden. Anschließend kann es per Knopfdruck
auf den RED Brick übertragen und ohne Änderungen auf diesen ausgeführt werden.
Es können mehrere Programme gleichzeitig ausgeführt werden. Deren Ausführung
kann konfiguriert (direkt nach dem Booten, jede Stunde, etc.) sowie überwacht
werden.

Eigene Projekte können somit sehr schnell und einfach realisiert werden.
Unseres Wissens nach ist keine, auch nur im Ansatz vergleichbare Lösung,
erhältlich.

Für jede unterstützte Programmiersprache sind die
:ref:`Tinkerforge API <api_bindings>` und häufig genutzte Bibliotheken
vorinstalliert. Weitere Bibliotheken können nachinstalliert werden.

Der Brick ist mit einem `Micro-HDMI <https://de.wikipedia.org/wiki/HDMI>`__
Anschluss ausgestattet, so dass auch
Programme mit grafischer Benutzeroberfläche ausgeführt werden können. Eine
`USB 2.0 <https://de.wikipedia.org/wiki/USB>`__ Host Schnittstelle kann genutzt
werden, um Eingabe- und Zeigegeräte, wie Tastaturen, Mäuse oder Touchscreens,
zu nutzen.

Mit der :ref:`Ethernet Master Extension <ethernet_extension>` kann der RED Brick
um eine Ethernet-Schnittstelle erweitert werden. Die
:ref:`RS485 Master Extension <rs485_extension>` wird ebenfalls unterstützt, so
dass auch entfernte Stapel von Bricks und Bricklets vom RED Brick gesteuert
werden können.

Fortgeschrittene Nutzer können den Brick mit vollem Zugriff auf dem
zugrundeliegenden `Debian <http://www.debian.org>`__ System nutzen.

Ein Einführungsvideo gibt es auf Youtube:

.. raw:: html

 <center><iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/BaS06VwU5Tw" frameborder="0" allowfullscreen></iframe></center>

Technische Spezifikation
------------------------

================================  ======================================================================================
Eigenschaft                       Wert
================================  ======================================================================================
Prozessor                         Allwinner A10s, Cortex A8 1GHz, 3D Mali400 GPU, NEON
Speicher                          512MB DDR3 SDRAM, Micro-SD-Karte als Flash Speicher
Anschlüsse                        USB 2.0 Host, Micro-HDMI (Typ D), Mini-USB, Stapelverbinder
--------------------------------  --------------------------------------------------------------------------------------
--------------------------------  --------------------------------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           14g
Stromverbrauch                    0,75W (5V/150mA, Leerlauf); 1,1W (5V/220mA, 100% Last)
================================  ======================================================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/red-brick/raw/master/hardware/red-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/red_brick_dimensions.png>`__)
* Linux Image und Platinenlayout (`Download <https://github.com/Tinkerforge/red-brick/zipball/master>`__)

.. _red_brick_test:

Erste Schritte / Teste den RED Brick
------------------------------------

Mit den folgenden Schritten kann der RED Brick getestet werden.
Ein Schritt für Schritt Tutorial zum RED Brick steht ebenfalls bereit:
:ref:`RED Brick Tutorial <tutorial_red_brick>`.

Als erstes müssen :ref:`Brick Daemon <brickd>` und :ref:`Brick Viewer <brickv>`
Software auf einem PC oder Mac installiert werden. Anschließend sollte die
vorbereitet Micro-SD-Karte in den :ref:`Micro-SD-Kartenslot
<red_brick_micro_sd_card_slot>` des RED Bricks gesteckt werden. Die Position
des Kartenslot und eine Übersicht aller Schnittstellen des Bricks gibt es in der
:ref:`Hardware Beschreibung <red_brick_hardware>`. `SD Karten mit
vorinstalliertem Image <https://www.tinkerforge.com/de/shop/accessories/red-brick.html>`__
können in unserem Shop bestellt werden. Ansonsten
kann ein passenden SD Karte aber auch selber vorbereitet werden, siehe den
:ref:`Image auf SD Karte kopiert <red_brick_copy_image>` Abschnitt.

Danach ist der RED Brick einsatzbereit und kann mit dem PC oder Mac mit einem
Mini-USB Kabel verbunden werden.

.. image:: /Images/Bricks/brick_red_mini_usb_600.jpg
   :scale: 100 %
   :alt: RED Brick mit Mini-USB Kabel
   :align: center
   :target: ../../_images/Bricks/brick_red_mini_usb_800.jpg

Nachdem die Brick Viewer Software gestartet wurde muss auf "Connect" geklickt
werden. Ein Tab (Reiter), beschriftet mit "RED Brick", sollte auftauchen. Diesen
Tab anklicken.

Auf der linken Seite des Tabs sind weitere Tabs vorhanden. Der "Overview" Tab
gibt eine Übersicht über die Auslastung der CPU, die Speicherbelegung und
andere Statusinformationen. Erscheinen diese Anzeigen, so bedeute dies, dass
der RED Brick wie erwartet funktioniert und Programme hochgeladen werden
können. Im :ref:`Brick Viewer Abschnitt <red_brick_brickv>` wird beschrieben,
wie der RED Brick konfiguriert werden kann und wie Programme hochgeladen werden.

Zusätzlich kann die grafische Nutzerschnittstelle (HDMI) getestet werden. Dazu
muss ein Monitor an den :ref:`HDMI Anschluss <red_brick_hdmi>` und ein
USB Hub mit Tastatur und Maus an dem :ref:`USB Anschluss <red_brick_usb_host>`
des RED Bricks angeschlossen werden. Während des Bootvorgangs kann das Starten
des LXDE Desktop Environments beobachtet werden, das anschließend wie ein ganz
normaler Desktop PC verwendet werden kann.

Auf dem Linux kann man sich mittels Nutzer ``tf`` und Passwort ``tf`` anmelden.
Der ``tf`` Nutzer ist sudoer.

.. note:: Aus Sicherheitsgründen kann es sinnvoll sein das Passwort zu ändern.
          Die Prozedur ist :ref:`hier <red_brick_change_password>` beschrieben.

.. _red_brick_brickv:

Brick Viewer
------------

Dieser Abschnitt beschreibt die Konfiguration des RED Bricks mit der
:ref:`Brick Viewer <brickv>` Software. Der RED Brick kann ebenfalls über die
:ref:`RED Brick API <red_brick_programming_interface>` konfiguriert werden (nur
für Power User gedacht).

.. image:: /Images/Screenshots/brickv_red_tab_and_labels.jpg
   :scale: 60 %
   :alt: Screenshot der Tabauswahl und Labels.
   :align: center

Die RED Brick Darstellung im Brick Viewer besteht aus verschiedenen Tabs. Jeder
wird nachfolgend im Detail beschrieben. Die UID des RED Bricks, die Position im
Stapel, der Name des benutzten Images, Anzahl der Timeouts und das Wort *System*
werden als erstes aufgeführt. Über *System* kann der Brick Daemon auf dem RED
Brick neugestartet werden, oder aber der RED Brick selber neugestartet oder
heruntergefahren werden.

Overview Tab (Statusinformation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dieser Tab ist standardmäßig selektiert. Er zeigt die Zeit, die der RED Brick
bereits läuft (Uptime), sowie die CPU- und Speicher- Nutzung an. Weiter unten
werden die Top-Prozesse nach CPU oder Speichernutzung angezeigt, die aktuell
auf dem RED Brick laufen. Die Tabelle *Network Interfaces* zeigt den Status
der aktuell konfigurierten Netzwerkschnittstellen.

.. image:: /Images/Screenshots/brickv_red_tab_overview.jpg
   :scale: 60 %
   :alt: Screenshot der Overview Tabs.
   :align: center

Die Liste kann folgende Netzwerkschnittstellen enthalten
(X steht für eine Zahl, typischerweise 0):

* ``lo``: Dies ist die sogenannte Loopback-Schnittstelle. Sie ist rein lokal und
  dient unter anderem der Kommunikation zwischen Anwenderprogrammen und dem
  lokalen Brick Daemon.
* ``wlanX``: Dies ist die WLAN-Schnittstelle. Sie wird erzeugt wenn ein WLAN USB
  Stick an die :ref:`USB Host Buchse <red_brick_usb_host>` angeschlossen wird.
* ``ethX``: Dies ist eine Ethernet-Schnittstelle. Sie wird erzeugt wenn ein
  Ethernet USB Stick an die :ref:`USB Host Buchse <red_brick_usb_host>`
  angeschlossen wird.
* ``tfX``: Ist die Ethernet-Schnittstelle, die erzeugt wird, wenn eine
  :ref:`Ethernet Extension <ethernet_extension>` auf den RED Brick gesteckt
  wird.

Die Statusanzeigen werden alle 3 Sekunden automatisch aktualisiert.

.. _red_brick_brickv_settings:

Settings Tab
^^^^^^^^^^^^

Der Settings Tab ist in verschiedene Unterbereiche aufgeteilt.

.. _red_brick_brickv_settings_network:

Netzwerk
""""""""

Im Network Abschnitt dieses Tabs können alle Einstellungen zu Netzwerken
vorgenommen werden.

.. image:: /Images/Screenshots/brickv_red_tab_settings_network.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Netzwerk Konfiguration.
   :align: center

Der *Current Network Status* Abschnitt zeigt den Status der konfigurierten und
aktuell genutzten Netzwerkschnittstelle an. Der angezeigte Status wird
automatisch alle 3 Sekunden aktualisiert.

Initial ist der RED Brick für keine Schnittstelle konfiguriert. Er wird initial
von sich aus keine Schnittstelle nutzen, selbst wenn eine vorhanden ist.
Es muss erst eine Schnittstelle im *Configuration* Abschnitt konfiguriert
werden. Als erstes muss die Schnittstelle gewählt werden. Ein Ethernet USB Stick
wird als ``ethX``, eine Ethernet Extension als ``tfX`` und ein WLAN USB Stick
als ``wlanX`` angezeigt (X ist eine Zahl). Abhängig von der gewählten
Schnittstelle gibt es verschiedenen Einstellungsoptionen:

* **Konfiguration einer Ethernet-Schnittstelle:**

  Nachdem eine Ethernet-Schnittstelle gewählt wurde kann zwischen DHCP oder
  statischer IP gewählt werden. Klicke anschließend *Connect*.
* **Konfiguration einer WLAN-Schnittstelle:**

  Nachdem eine WLAN-Schnittstelle gewählt wurde, können WLAN-Netze durch Klicken
  auf den *Scan* Button gesucht werden. Dies dauert ein paar Sekunden.

  Wähle den gewünschten Access Point und gebe den dazugehörigen Key ein.
  Anschließend muss nur noch zwischen DHCP oder statischer IP Adresse gewählt
  werden. Durch Klicken auf *Connect* wird die Verbindung zum Netzwerk
  hergestellt. Unterstützte WLAN USB Sticks finden sich in unserem
  `Shop <https://www.tinkerforge.com/de/shop/accessories/red-brick.html>`__.

Ab jetzt verbindet sich der RED Brick nach einem Neustart automatisch über
die konfigurierte Schnittstelle.

.. _red_brick_brickv_settings_ap:

WLAN Access Point
"""""""""""""""""

Im WLAN Access Point Abschnitt (benötigt Image >= 1.4 und
Brick Viewer >= 2.2.2) kann der RED Brick in einen WLAN Access
Point verwandelt werden. Dieser Abschnitt ist erst verfügbar, wenn der
:ref:`Access Point Service <red_brick_brickv_settings_services>` aktiviert ist
und ein `WLAN USB Stick
<https://www.tinkerforge.com/de/shop/accessories/red-brick/wifi-usb-adapter.html>`__
eingesteckt ist.

.. image:: /Images/Screenshots/brickv_red_tab_settings_access_point.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tab mit Konfiguration des Access Point
   :align: center

Im Access Point Modus stellt der RED Brick einen DHCP und DNS Server zur
Verfügung. Diese geben Geräten, die sich mit dem RED Brick verbinden eine IP
Adresse und stellt eine Domain zur Verfügung. Die IP Adresse, SSID, WPA
Passwort, DHCP Pool, DNS Domain und andere Optionen die von einem Access Point
erwartet werden, können konfiguriert werden.

Die aktuellen DHCP Leases werden angezeigt, so dass verbundene Geräte einfach 
identifiziert werden können.

Im Access Point Modus ist keine externe Netzwerkinfrastruktur notwendig. 
Smartphone, Tablet oder Laptop können direkt mit dem RED Brick verbunden werden.

.. _red_brick_brickv_settings_mobile_internet:

Mobile Internet
"""""""""""""""

Im Mobile Internet Abschnitt (benötigt Image >= 1.7 und Brick Viewer >= 2.2.6)
kann eine mobile Internet-Verbindung konfiguriert werden. Dieser Abschnitt
ist erst verfügbar, wenn der :ref:`Mobile Internet Service
<red_brick_brickv_settings_services>` aktiviert ist und ein `3G USB Stick
<https://www.tinkerforge.com/de/shop/accessories/red-brick/3g-usb-adapter.html>`__
eingesteckt ist.

.. image:: /Images/Screenshots/brickv_red_tab_settings_mobile_internet.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tab mit Konfiguration der mobilen Internet-Verbindung
   :align: center

Voreinstellungen für verschiedene Mobilfunkbetreiber können über denn "Provider
Presets" Knopf ausgewählt werden.

.. image:: /Images/Screenshots/brickv_red_tab_settings_mobile_internet_presets.jpg
   :scale: 60 %
   :alt: Screenshot des Mobile Internet Provider Presets Dialogs.
   :align: center

Nach einem Klick auf den "Connect" Knopf wird die Verbindung hergestellt, dies
kann einige Minuten dauern. Es muss immer ein SIM Karten PIN eingegeben werden.
Ist die PIN auf der SIM Karte deaktiviert worden, so kann eine beliebige PIN 
angegeben werden.

Wenn WLAN Access Point und Mobile Internet gleichzeitig aktive sind, dann teilt
der RED Brick als WLAN Router seine Internet-Verbindung automatisch mit den
verbundenen WLAN Teilnehmern.

.. _red_brick_brickv_settings_server_monitoring:

Serverüberwachung
"""""""""""""""""

.. image:: /Images/Screenshots/brickv_red_tab_settings_srm.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Server Monitoring Konfiguration.
   :align: center

Die Serverüberwachungs-Funktion (benötigt Image >= 1.6 und
Brick Viewer >= 2.2.3) ist für die Zusammenarbeit mit dem
:ref:`Starterkit: Serverraum-Überwachung <starter_kit_server_room_monitoring_red_brick>`
entworfen worden. Für weitere Details siehe die Dokumentation des Kits.

.. _red_brick_brickv_settings_openhab:

openHAB
"""""""

.. image:: /Images/Screenshots/brickv_red_tab_settings_openhab.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: openHAB Konfiguration.
   :align: center

Im `openHAB <http://www.openhab.org/>`__ Abschnitt (benötigt Image >= 1.6 und
Brick Viewer >= 2.2.3) kann der openHAB Service auf dem RED Brick konfiguriert
werden. Dieser Abschnitt ist erst verfügbar, wenn der :ref:`openHAB Service
<red_brick_brickv_settings_services>` aktiviert ist.

Über die *New* und *Delete* Knöpfe können neue ``.items``, ``.rules`` und
``.sitemap`` Dateien angelegt und bestehende Dateien wieder gelöscht werden.
Abhängig von der Endung der Datei speichert Brick Viewer sie automatisch im
richtigen openHAB Konfigurationsverzeichnis.

Nachdem Änderungen einer Konfigurationsdatei vorgenommen wurden können diese
über den *Apply Changes* Knopf gespeichert oder über den *Discard Changes*
Knopf verworfen werden. Dateien mit ungespeicherten Änderungen werden als
``(modified)`` angezeigt.

Ein openHAB Konfigurationsbeispiel ist in der Dokumentation des
:ref:`Starterkits: Wetterstation <starter_kit_weather_station_openhab>`
beschrieben.

.. _red_brick_brickv_settings_brickd:

Brick Daemon
""""""""""""

Im Brick Daemon Abschnitt des Tabs können Einstellungen zum lokalen
Brick Daemon vorgenommen werden.

.. image:: /Images/Screenshots/brickv_red_tab_settings_brickd.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Brickd Konfiguration.
   :align: center

Zu den Konfigurationsmöglichkeiten gehören die Adresse auf dem der Brick Daemon
lauscht, der dazugehörige Port, der Port für die Nutzung von WebSockets,
das Authentifizierungsgeheimnis und weitere Einstellungen u.a. die Funktion der
roten und grünen LED.

WebSockets werden von der Browser-Version der
:ref:`JavaScript Bindings <api_bindings_javascript>` verwendet um Bricks und
Bricklets zu steuern.

.. _red_brick_brickv_settings_date:

Datum/Uhrzeit
"""""""""""""

Im Date/Time Abschnitt kann die Uhr des RED Bricks, mit der Uhr des
angeschlossenen PCs, synchronisiert werden. Es gibt keine Batterie auf dem RED
Brick, so dass die Uhr nicht weiterläuft, wenn der RED Brick nicht aktiv ist.

.. image:: /Images/Screenshots/brickv_red_tab_settings_date.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Datum und Uhrzeit Konfiguration.
   :align: center

Wenn eine Verbindung zum Internet besteht (Ethernet Extension oder WLAN USB
Stick), werden Datum und Uhrzeit automatisch mittels NTP gesetzt. Dazu muss nur
die Zeitzone gesetzt werden. Diese wird gespeichert und wieder hergestellt,
wenn der RED Brick das nächste mal hochfährt.

Falls die Zeit nach dem Booten immer vorhanden sein muss, ein Verbindung zum
Internet aber nicht garantiert werden kann, dann kann auch das
:ref:`GPS Bricklet <gps_bricklet>` oder das :ref:`Real-Time Clock Bricklet
<real_time_clock_bricklet>`benutzt werden. Dazu muss nur ein entsprechendes
kleines `Programm von GitHub <https://github.com/Tinkerforge/red-brick/tree/master/programs>`__
heruntergeladen und auf den RED Brick geladen werden, um die Uhrzeit
mittels GPS Uhrzeit (``gps_time`` Programm) oder Real-Time Clock Bricklet
Uhrzeit (``rtc_time`` Programm) zu synchronisieren.

.. _red_brick_brickv_settings_file_system:

Dateisystem
"""""""""""

Im File System Abschnitt (benötigt Brick Viewer >= 2.2.1) kann das Dateisystem
auf der Micro-SD-Karte vergrößert werden.

.. image:: /Images/Screenshots/brickv_red_tab_settings_file_system.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Dateisystem Vergrößerung.
   :align: center

Abhängig von der Image Größe und der Kapazität der Micro-SD-Karte wird
möglicherweise nicht die volle Kapazität der Micro-SD-Karte genutzt. In diesem
Fall kann durch eine Vergrößerung des Dateisystems mehr Speicherplatz nutzbar
gemacht werden. Wenn das Dateisystem weniger als 95% der Micro-SD-Karte
einnimmt dann kann es vergrößert werden. Um dies zu tun einfach den Anweisungen
in Brick Viewer folgen.

.. _red_brick_brickv_settings_services:

Services
""""""""

.. image:: /Images/Screenshots/brickv_red_tab_settings_services.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Services.
   :align: center

Im Services Abschnitt (benötigt Image >= 1.4 und Brick Viewer >= 2.2.2)
können verschiedene Services des RED Brick ein- und
ausgeschaltet werden. Wenn Webserver oder Desktop Umgebung nicht benötigt
werden können diese abgeschaltet werden, wodurch der RED Brick schneller bootet.
Ebenfalls kann hier der :ref:`WLAN Access Point Modus
<red_brick_brickv_settings_ap>` eingeschaltet werden, wodurch sich Smartphones
und Notebooks direkt mit dem RED Brick verbinden können.

* GPU: Aktiviert die Hardwarebeschleunigung für die Grafikausgabe. Wird
  diese aktiviert, wird ein Teil des RAMs von der GPU genutzt. Wird HDMI nicht
  genutzt empfehlen wir die GPU zu deaktivieren.
* Desktop Environment: Der Start der Desktopumgebung (LXDE) benötigt
  Zeit, wird diese nicht benutzt kann sie deaktiviert werden um Bootzeit zu
  sparen.
* Web Server: Der Webserver ist notwendig wenn Webservices genutzt werden
  sollen. Diese Option fügt ungefähr 10 Sekunden Bootzeit hinzu.
* Splash Screen: Falls aktiviert, wird ein Splash Screen beim Bootvorgang
  angezeigt. Ist dieser deaktiviert, so werden Kernelmeldungen angezeigt.
* Access Point: Ist der Access Point Modus aktiviert, kann der RED Brick
  als Access Point genutzt werden (siehe
  :ref:`Access Point im Settings Tab <red_brick_brickv_settings_ap>`).
* Server Monitoring: Aktiviert das `Nagios <https://www.nagios.org/>`__
  Monitoring System (siehe :ref:`Serverüberwachung im Settings Tab
  <red_brick_brickv_settings_server_monitoring>`).
* openHAB: Aktiviert die `openHAB <http://www.openhab.org/>`__ Runtime (siehe
  :ref:`openHAB im Settings Tab <red_brick_brickv_settings_openhab>`).
* Mobile Internet: Wenn Mobile Internet aktiviert ist, dann kann eine
  :ref:`mobile Internet-Verbindung im Settings Tab
  <red_brick_brickv_settings_mobile_internet>` konfiguriert werden.

Werden Services geändert und gespeichert, so startet der RED Brick neu. Nach dem 
Neustart stehen die Änderungen zur Verfügung.


.. _red_brick_brickv_program:

Program Tab (Programme hochladen und ausführen)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Beschreibung des Tabs befindet auf einer
:ref:`separaten Seite <red_brick_program_tab>`.

.. toctree::
   :hidden:

   Wizard Schritte <RED_Brick_Program_Tab>

.. image:: /Images/Screenshots/red_brick_program_overview.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Program Tabs.
   :align: center

.. _red_brick_brickv_console:

Console Tab (Konsole, Fernsteuerung)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn der RED Brick mittels `Mini-USB Anschluss <red_brick_mini_usb>`__ mit einem
PC verbunden ist, registriert er eine serielle Schnittstelle. Diese Schnittstelle
kann dazu genutzt werden um auf die Linux Shell des RED Bricks zuzugreifen. Dazu
muss nur die entsprechende Schnittstelle gewählt werden und *Connect* geklickt
werden. Die Schnittstelle ist typischerweise unter Linux ``/dev/ttyACMX`` (X ist
eine Zahl), unter Windows ``Serial Port X`` (X ist Zahl) mit dem Gerätenamen
``RED Brick Serial Console`` und unter OS X ``/dev/tty.usbmodemXYZ``, wobei XYZ
ein Teil der UID des RED Bricks ist. Mit dem Nutzer ``tf`` und Passwort
``tf`` kann man sich einloggen. Falls unbekannt ist welche Schnittstelle die
richtig ist, kann diese durch Ausprobieren bestimmt werden. Es kann notwendig
sein die ENTER Taste zu drücken um die Kommandozeile zu sehen.

Nachfolgend ein Screenshot, das die Konsole bei der Ausführung des Befehls
``htop`` zeigt.

.. image:: /Images/Screenshots/brickv_red_tab_console.jpg
   :scale: 60 %
   :alt: Screenshot des Console Tab.
   :align: center

Ein gutes Shell Tutorial steht auf
`linuxcommand.org <http://linuxcommand.org/lc3_learning_the_shell.php>`__
zur Verfügung.

.. _red_brick_brickv_versions_tab:

Versions Tab (Daemon, Bindings und Bibliotheken)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der Version Tab gibt Informationen über den installierten Brick Daemon, RED
Brick API Daemon sowie die installierten Bindings und deren Bibliotheken.

.. image:: /Images/Screenshots/brickv_red_tab_versions.jpg
   :scale: 60 %
   :alt: Screenshot des Versions Tab.
   :align: center

Wenn andere Bibliotheken, wie die Installierten genutzt werden sollen, dann
können diese entweder mit dem eigenen Programm
:ref:`hochgeladen werden <red_brick_brickv_program>` oder aber mittels
``apt-get``, ``pip``, ``pear``, ``npm`` oder ähnlichen Paketmanagern
installiert werden. Die genannten Paketmanager sind in allen RED Brick Images
vorinstalliert.

Extensions Tab (Konfiguration, Verwaltung)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zwei :ref:`Master Extensions <primer_master_extensions>` werden vom RED Brick
unterstützt: :ref:`Ethernet Extension <ethernet_extension>` und
:ref:`RS485 Extension <rs485_extension>`.

Eine Änderung der Einstellungen einer Extension führt zu einem Neustart des
Brick Daemons, d.h. der RED Brick Tab verschwindet kurz aus dem Brick Viewer
und taucht kurze Zeit später wieder auf.

Ethernet Extension
""""""""""""""""""

.. image:: /Images/Screenshots/brickv_red_tab_extension_ethernet.jpg
   :scale: 60 %
   :alt: Screenshot des Extension Tabs: Ethernet Extension Konfiguration.
   :align: center

Nur die MAC Adresse der Ethernet Extension kann hier geändert werden. Da diese
als normale Netzwerkschnittstelle auftaucht, können die Netzwerkeinstellungen im
:ref:`Settings Tab <red_brick_brickv_settings>` verändert werden.

RS485 Extension
"""""""""""""""

.. image:: /Images/Screenshots/brickv_red_tab_extension_rs485.jpg
   :scale: 60 %
   :alt: Screenshot des Extension Tabs: RS485 Extension Konfiguration.
   :align: center

Die Konfiguration der RS485 Extension ist identisch zu der mit einem Master
Brick. Siehe :ref:`RS485 Extension Dokumentation <rs485_configuration>`.

Wir empfehlen Baudraten von 500000, 250000, 166666, 125000, 100000, 83333,
71428, 62500, 55555, 50000, 45454 oder 41666 Baud bei der Nutzung eines RED
Bricks.

.. _red_brick_brickv_import_export_tab:

Import/Export
^^^^^^^^^^^^^

Der Import/Export Tab (benötigt Brick Viewer >= 2.2.2) erlaubt es System Logs
und Programme zu importieren und exportieren.

System Logs
"""""""""""

.. image:: /Images/Screenshots/brickv_red_tab_imexport_system_logs.jpg
   :scale: 60 %
   :alt: Screenshot des Import/Export Tabs: System Logs.
   :align: center

Wähle eine Logdatei und klicke auf ``Refresh``. Die Logdatei wird vom RED Brick
heruntergeladen und im Brick Viewer angezeigt. Mit ``Save`` kann die Datei 
gespeichert werden.

Import
""""""

.. image:: /Images/Screenshots/brickv_red_tab_imexport_import.jpg
   :scale: 60 %
   :alt: Screenshot des Import/Export Tabs: Import.
   :align: center

Wähle ein Datei mit zuvor exportierten Programmen (siehe unten) und wähle die 
Programme, die importiert werden sollen. Drücke ``Import`` um diese hochzuladen.

Export
""""""

.. image:: /Images/Screenshots/brickv_red_tab_imexport_export.jpg
   :scale: 60 %
   :alt: Screenshot des Import/Export Tabs: Export
   :align: center

Im Export Tab können Programme exportiert werden. Drücke ``Export`` um diese auf
der Festplatte zu speichern.

Die Exportdatei enthält die Konfiguration des Programms, alle Dateien und die 
Logs die sich über die Zeit angesammelt haben. Wenn das zu exportierende 
Programm läuft und dauerhaft Dateien schreibt bietet es sich an dieses vor dem 
Export zu beenden, um teilweise geschriebene Dateien zu verhindern.

Mit dieser Option können Programme exportiert werden und auf anderen RED Bricks
importiert (siehe oben) werden.


.. _red_brick_web_interface:

RED Brick Web Interface
-----------------------

Wenn der RED Brick mit einem WLAN USB Stick, einer Ethernet Extension oder einer
anderen Netzwerkverbindung ausgestattet ist, kann auf das Web Interface
zugegriffen werden. Das Web Interface ist unter der IP Adresse des RED Bricks
oder unter dessen Hostnamen (Voreinstellung: ``red-brick``) erreichbar.

Das RED Brick Web Interface zeigt die installierten Programme, deren Logs und
Konfiguration, als auch die hochgeladenen Dateien. Seit Image Version 1.6 werden
auch die verfügbaren :ref:`openHAB <red_brick_brickv_settings_openhab>` Sitemaps und
ein Link zur :ref:`Serverüberwachungs <red_brick_brickv_settings_server_monitoring>`
Webseite mit aufgeführt.

.. image:: /Images/Screenshots/red_brick_web_interface.jpg
   :scale: 40 %
   :alt: Screenshot des RED Brick Web Interfaces.
   :align: center

Neben dem vorinstallierten Web Interface können auch eigene installiert werden.
Es werden Webanwendungen, die in HTML/JavaScript, Python oder PHP geschrieben
sind, unterstützt. Wenn eine ``index.py``, ``index.php`` oder ``index.html``
Datei hochgeladen wird, so wird diese als Index Datei des binary Ordners genutzt.

**Beispiel zur Erklärung:** Es soll eine PHP Webseite entwickelt werden, die
Bricks/Bricklets steuert. Dazu wird das PHP Programm ``EXAMPLE`` mit der ID
``EXAMPLE-ID`` hochgeladen, das eine ``index.php`` als Startpunkt enthält. Wird
anschließend das RED Brick Web Interface aufgerufen und der "Bin" Button der
``EXAMPLE`` Anwendung geklickt, so wird der Link zu ``/programs/EXAMPLE-ID/bin``
geöffnet. Dieser Link führt direkt die ``index.php`` aus, da diese als Index Datei
des Verzeichnisses fungiert.

Webseiten, die Umwelt-Messungen von einem Temperature/Barometer/Humidity
Bricklets anzeigt können somit sehr einfach erstellt werden. Es können aber auch
Aktoren, zum Beispiel ein Relay Bricklet, über Buttons gesteuert werden.

Mit dem RED Brick ist es also sehr einfach Web-Anwendungen zu entwickeln, die
Hardware steuern.

HTML/JavaScript
^^^^^^^^^^^^^^^

Wenn eine HTML Datei mit eingebettetem JavaScript hochgeladen wird, können die
JavaScript Bindings genutzt werden. Diese sind direkt im Root Verzeichnis
verfügbar.

.. code-block:: html

 <script src="/Tinkerforge.js" type='text/javascript'></script>

Das JavaScript wird im Browser des Benutzers ausgeführt und nicht auf dem RED
Brick. Aus diesem Grund muss sich mit der IP Adresse des RED Bricks verbunden
werden und nicht mit localhost!

Python
^^^^^^
Auf dem Webserver (Apache) des RED Bricks wird WSGI
(`mod_wsgi <https://github.com/GrahamDumpleton/mod_wsgi>`__) von Python genutzt
um Webseiten darzustellen. Dieser ist konfiguriert um eine ``index.py`` als
Startpunkt für ein WSGI Skript zu nutzen. Alle verbreiteten Python Web
Frameworks unterstützen WSGI. Das `Flask framework <http://flask.pocoo.org/>`__
ist auf dem RED Brick vorinstalliert (beinhaltet
`Werkzeug <http://werkzeug.pocoo.org/>`__ und
`Jinja <http://jinja.pocoo.org/>`__).

Ein minimales Flask Web Interface, das auf den RED Brick hochgeladen werden kann,
ist eine ``index.py`` mit folgenden Inhalt:

.. code-block:: python

 from flask import Flask       # Use Flask framework
 application = Flask(__name__) # Function "application" is used by Apache/wsgi
 app = application             # Use shortcut for routing

 @app.route('/')
 def index():
     return '<html><body>Hello World!</body></html>'

Soll ein Programm Bricks/Bricklets steuern, so müssen nur die Tinkerforge
Bindings, wie bei jedem Python Programm, eingebunden werden::

 from tinkerforge.ip_connection import IPConnection
 from tinkerforge.bricklet_temperature import Temperature

 # ...

Das standardmäßig installierte Web Interface auf dem RED Brick nutzt
Python/Flask. Der Code steht auf
`GitHub <https://github.com/Tinkerforge/red-brick/blob/master/image/patches/root-fs/common/tmp/index.py>`__
zur Verfügung.

Es können natürlich auch Templates, statische Dateien und so weiter benutzt
werden. Diese können genauso benutzt werden wie in den meisten Flask Tutorials
gezeigt.

..
  Ein `etwas komplexeres Flask Beispiel <TODO>`__, dass mehr
  Features nutzt, liegt ebenfalls auf GitHub.

PHP
^^^

Der Webserver auf dem RED Brick ist dazu eingerichtet eine ``index.php`` zu
erkennen.

Eine minimale Hallo Welt ``index.php`` könnte wie folgt aussehen:

.. code-block:: php

 <?php $greeting = 'Hello World!'; ?>

 <html>
  <head>
   <title>PHP Example</title>
  </head>
  <body>
   <p><?php echo $greeting; ?><p>
   <p><?php phpinfo(); ?><p>
  </body>
 </html>

Um Bricks/Bricklets zu steuern müssen die Tinkerforge Bindings eingebunden
werden::

 require_once('Tinkerforge/IPConnection.php');
 require_once('Tinkerforge/BrickletTemperature.php');

 // ...

.. _red_brick_images:

RED Brick Software Image
------------------------

Das RED Brick Software Image basiert auf `Debian <http://www.debian.org/>`__
und ist auf einer Micro-SD-Karte gespeichert. Zu Anfang gab es das Image in
zwei Varianten: Das "Full" und das "Fast" Image. Seit Image Version 1.4 gibt es
nur noch ein Image (ehemals das "Full" Image) mit einstellbaren Services
(Desktop-Umgebung, Web Server, WLAN Access Point, usw.), die es erlauben das
Image an verschiedenen Anforderungen anzupassen.

Das Image verfügt über GPU Treiber und besitzt alle notwendigen
Bibliotheken für die Nutzung von grafischen Nutzerschnittstellen (GUIs).
Falls aktiviert, startet ein X Server während des Bootvorgangs und das
`LXDE Desktop Environment <http://lxde.org/>`__ wird mit Autologin gestartet.
Wenn das eigene Programm eine grafische Nutzerschnittstelle nutzt, so wird
diese auf dem Desktop angezeigt. Die Bildschirmauflösung passt sich der
Voreinstellung des angeschlossenen HDMI Monitors an. Über LXDE kann diese aber
auch konfiguriert werden. Die HDMI-Schnittstelle muss aber nicht benutzt werden
und es können auch Programme ohne grafische Nutzerschnittstelle ausgeführt
werden.

Neue Software kann installiert werden. Siehe die :ref:`Beschreibung des Versions
Tab <red_brick_brickv_versions_tab>`, wie neue Software installiert wird.

Eine Liste der vorinstallierten Bibliotheken steht zur Verfügung:
:ref:`Installierte Bibliotheken <red_brick_installed_versions>`.

.. toctree::
   :hidden:

   Installierte Bibliotheken <RED_Brick_Installed_Versions>

Der Nutzer ``tf`` ist der Standardnutzer auf den Images. Beim Einloggen über die
Konsole oder in LXDE kann dieser Nutzer mit dem Standardpasswort ``tf`` benutzt
werden. Der Nutzer ist ein sudoer, so dass Root-Zugriff mittels::

 sudo -s

erhalten werden kann. Die Images können von der
:ref:`Download Seite <downloads_red_images>` herunter geladen werden.

.. _red_brick_build_image:

Baue dein eigenes Image
^^^^^^^^^^^^^^^^^^^^^^^
Bei dieser Anleitung nehmen wir an, dass ein
`Debian Linux <https://www.debian.org/>`__ als Host Plattform genutzt wird.

1. `RED Brick Repository <https://github.com/Tinkerforge/red-brick>`__ von GitHub clonen
2. In den Ordner ``image`` wechseln, die Datei ``README.rst`` öffnen und die
   dokumentierten Schritte durchführen.

Das Bauen eines Images kann 4-6 Stunden dauern, abhängig von der
Leistungsfähigkeit des genutzten Rechners kann es auch deutlich
länger dauern.

.. _red_brick_copy_image:

Image auf SD Karte kopieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zuerst das :ref:`Image <red_brick_images>` von der
:ref:`Download Seite <downloads_red_images>` herunterladen, entpacken und
eine geeignete Micro-SD-Karte samt Kartenleser zur Hand haben. Wir empfehlen
eine schnelle Karte (z.B. Class 10, > 30MB/s Lesen) mit genügend Speicherplatz
(mindestens 8GB).

Windows
"""""""

Für Windows empfehlen wir ein Tool wie `Win32DiskImager
<http://sourceforge.net/p/win32diskimager/wiki/Home/>`__ um das Image auf die
Karte zu kopieren.

1. Verbinde die SD Karte über den Kartenleser mit dem PC.
2. Starte Win32DiskImager als Administrator.
3. Wähle Image und SD Karte und klicke auf "Write".

Linux
"""""

1. Verbinde die SD Karte über den Kartenleser mit dem PC.
2. Identifiziere den Pfad zu der SD Karte (z.B. mit ``dmesg``) mit diesem
   Format: ``/dev/sdX``, wobei ``X`` ein Buchstabe ist.
3. Mittels ``dd`` das Image (z.B. ``/tmp/red_image_1_5_full.img``) auf die
   SD Karte (z.B. ``/dev/sdb``) schreiben:

.. code-block:: bash

  sudo dd bs=64M if=/tmp/red_image_1_5_full.img of=/dev/sdb

Mac OS X
""""""""

1. Verbinde die SD Karte über den Kartenleser mit dem Mac.
2. Möglicherweise meldet Mac OS X, dass die SD Karte nicht lesbar ist,
   ignoriere diese Meldung.
3. Identifiziere den Pfad zu der SD Karte (z.B. mit ``diskutil list``), er
   sollte dieses Format haben: ``/dev/diskN``, wobei ``N`` ein Zahl ist.
4. Unmounte die SD Karte (z.B. mit ``diskutil unmountDisk /dev/diskN``).
5. Mittels ``dd`` das Image (z.B. ``/tmp/red_image_1_5_full.img``) auf die SD
   Karte (z.B. ``/dev/disk4``) schreiben, dabei aber ``/dev/rdiskN`` statt
   ``/dev/diskN`` für erhöhten Durchsatz verwenden:

.. code-block:: bash

  sudo dd bs=64m if=/tmp/red_image_1_5_full.img of=/dev/rdisk4

Falls dies nicht funktioniert (z.B. wenn der RED Brick nicht von der SD Karte
bootet) dann kann alternativ diese langsamer Methode verwendet werden:

.. code-block:: bash

  sudo dd bs=1m if=/tmp/red_image_1_5_full.img of=/dev/disk4


.. _red_brick_change_password:

Standard Passwort ändern
^^^^^^^^^^^^^^^^^^^^^^^^

Das Standard-Passwort des Benutzers ``tf`` lautet ``tf``. Um dieses zu ändern
öffnet man den :ref:`Console Tab <red_brick_brickv_console>`. Anschließend wählt
man die korrekte serielle Schnittstelle und klickt auf den *Connect* Button.
Man wird als Nutzer ``tf`` eingeloggt (die Enter-Taste drücken falls die Konsole
nichts anzeigt). Als nächstes gibt man den Befehl ``passwd`` ein und es wird
nach dem aktuellen Passwort gefragt. Man gibt ``tf`` ein. Anschließend
kann man das neue Passwort eingeben und bestätigen.


.. _red_brick_change_hdmi_resolution:

HDMI Monitor Auflösung ändern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der RED Brick stellt automatisch die richtige Monitor Auflösung für einen
angeschlossenen Monitor ein. Dazu wird die `Extended Display Identification
Data <https://de.wikipedia.org/wiki/Extended_Display_Identification_Data>`__
(EDID) Schnittstelle des Monitor verwendet. Allerdings funktioniert EDID nur
dann zuverlässig, wenn der Monitor bereits per HDMI anschlossen und
eingeschaltet ist bevor der RED Brick bootet.

Wenn der Monitor erst an HDMI angeschlossen wird oder erst eingeschaltet wird,
wenn der RED Brick schon läuft, dann kann es passieren, dass EDID nicht richtig
funktioniert und eine falsche Auflösung eingestellt wird. Die einfachste
Möglichkeit dies zu beheben ist es den RED Brick neuzustarten, sodass der
Monitor bereits angeschlossen und eingeschaltet, wenn der RED Brick bootet.

Wenn dies nicht möglich ist und der Monitor erst angeschlossen oder
eingeschaltet werden kann, wenn der RED Brick bereits läuft oder die automatisch
eingestellt Auflösung aus anderen Gründen falsch ist, dann kann die Auflösung
auch manuell mit dem ``tf-set-resolution`` Tool eingestellt werden.

Mit tf-set-resolution
"""""""""""""""""""""

Um die Monitor Auflösung zu ändern öffnet man den :ref:`Console Tab
<red_brick_brickv_console>`. Anschließend wählt man die korrekte serielle
Schnittstelle und klickt auf den *Connect* Button. Man wird als Nutzer ``tf``
eingeloggt (die Enter-Taste drücken falls die Konsole nichts anzeigt).
Als nächstes gibt man den folgenden Befehl ein (möglicherweise wird nach dem
Passwort für tf gefragt, das Standard-Passwort lautet ``tf``)::

 sudo tf-set-resolution hdmi mode <mode-number>

Anstatt ``<mode-number>`` muss die Nummer des Modus angegeben werden, der
aktiviert werden soll. Folgenden manuell setzbare Modi werden derzeit
unterstützt:

* 0 = 480i
* 1 = 576i
* 2 = 480p
* 3 = 576p
* 4 = 720p @ 50Hz
* 5 = 720p @ 60Hz
* 6 = 1080i @ 50Hz
* 7 = 1080i @ 60Hz
* 8 = 1080p @ 24Hz
* 9 = 1080p @ 50Hz
* 10 = 1080p @ 60Hz
* 11 = PAL
* 12 = PAL (S-Video)
* 14 = NTSC
* 15 = NTSC (S-Video)
* 17 = PAL-M
* 18 = PAL-M (S-Video)
* 20 = PAL-NC
* 21 = PAL-NC (S-Video)
* 23 = 1080p @ 24Hz (3D)
* 24 = 720p @ 50Hz (3D)
* 25 = 720p @ 60Hz (3D)
* 26 = 1360 x 768 @ 60Hz
* 27 = 1280 x 1024 @ 60Hz
* 28 = 800 x 480 @ 60Hz (benötigt Image Version >= 1.6)

Wenn die gewünschte Auflösung nicht in der Liste der setzbaren Modi enthalten
ist, dann können wir die Kernel Tabellen um einen neuen Modus erweitern. Dafür
müssen wir die relevanten Informationen für den entsprechenden Monitor kennen.
Als erstes muss sichergestellt werden, dass beim Booten die Auflösung des
Monitors automatisch richtig eingestellt wurde. Dann den folgenden Befehl
eingeben::

 dmesg | egrep "(PCLK=|disp clks:)"

und uns eine E-Mail (info@tinkerforge.com) mit der Ausgabe des Befehls schicken.

.. _red_brick_examples:

Beispielprogramme
-----------------

Auf `GitHub <https://github.com/Tinkerforge/red-brick/tree/master/programs>`__
stehen verschiedene Beispielprogramme zur Verfügung:

* `GPS Uhrzeit als Systemzeit verwenden
  <https://github.com/Tinkerforge/red-brick/tree/master/programs/gps_time>`__:
  Wenn NTP nicht verwendet werden kann, um die Systemzeit zu synchronisieren,
  z.B. wegen fehlender Internetanbindung, dann kann alternativ dieses Programm
  verwendet werden, um die Systemzeit mit dem GPS Bricklet zu synchronisieren.
* `Real-Time Clock Bricklets Uhrzeit als Systemzeit verwenden
  <https://github.com/Tinkerforge/red-brick/tree/master/programs/rtc_time>`__:
  Wenn NTP nicht verwendet werden kann, um die Systemzeit zu synchronisieren,
  z.B. wegen fehlender Internetanbindung, dann kann alternativ dieses Programm
  verwendet werden, um die Systemzeit mit dem Real-Time Clock Bricklet zu
  synchronisieren.
* `Systemzeit über Webbrowser synchronisieren
  <https://github.com/Tinkerforge/red-brick/tree/master/programs/sync_time>`__:
  Wenn weder NTP noch GPS, noch Real-Time Clock Bricklet zur Synchrionisierung
  der Systemzeit genutzt werden kann, dann kann über dieses Programm die
  Systemzeit vom Webbrowser aus synchronisiert werden.
* `Humidity Callback per SMS erhalten
  <https://github.com/Tinkerforge/red-brick/tree/master/programs/sms_humidity>`__:
  Dieses Beispiel zeigt, wie Bricklet Callback-Werte per SMS weiter geleitet
  werden können, wenn am RED Brick ein GSM Modem angeschlossen ist.
* `GPS Position per SMS abfragen
  <https://github.com/Tinkerforge/red-brick/tree/master/programs/sms_location>`__:
  Dieses Beispiel zeigt, wie die GPS Position per SMS abgefragt werden kann,
  wenn am RED Brick ein GPS Bricklet und ein GSM Modem angeschlossen sind.


.. _red_brick_hardware:

Hardwarebeschreibung
--------------------

.. image:: /Images/Bricks/brick_red_caption_top_fixed_width.jpg
   :scale: 100 %
   :alt: RED Brick Beschreibung Oberseite
   :align: center
   :target: ../../_images/Bricks/brick_red_caption_top_1000.jpg

.. image:: /Images/Bricks/brick_red_caption_bottom_fixed_width.jpg
   :scale: 100 %
   :alt: RED Brick Beschreibung Unterseite
   :align: center
   :target: ../../_images/Bricks/brick_red_caption_bottom_1000.jpg

Power Button
^^^^^^^^^^^^

Der Taster auf dem RED Brick ist ein Power Button. Wenn dieser länger wie 5
Sekunden gedrückt wird, so schaltet sich der RED Brick ab. Wenn der Brick
aus ist, kann dieser über den Button auch wieder eingeschaltet werden. Dazu
muss der Button solange gedrückt werden (ca. 3 Sekunden) bis die blaue LED
an geht. Der Brick bootet anschließend.

.. _red_brick_leds:

LEDs
^^^^

Der RED Brick besitzt drei verschiedene LEDs auf der Oberseite. Eine blaue,
eine rote und eine grüne LED.

* Die blaue LED ist direkt mit der internen Stromversorgung des Prozessors
  verbunden und leuchtet also immer, wenn der Prozessor mit Strom versorgt ist.

* Die rote LED zeigt an wenn ein Fehler vorliegt. Wenn die rote LED während des
  Bootvorgangs dauerhaft leuchtet, so konnte kein Image gefunden werden. Es ist
  entweder keine SD Karte vorhanden oder auf dieser ist kein gültiges Image.

* Die grüne LED zeigt den aktuellen Status. Wenn beim Starten die rote LED
  aus geht und die grüne nicht an, dann konnte Linux nicht korrekt booten.
  Während des Bootvorgangs geht die grüne LED an, nachdem alle Services gestartet
  sind und der Brick bereit ist blinkt diese (Heartbeat).

Ein normaler Bootvorgang verläuft wie folgt:

1. Blaue und rote LED sind an, grüne LED ist aus.
2. Rote LED geht aus (U-Boot geladen).
3. Grüne LED geht an (Linux bootet).
4. Grüne LED blinkt (Heartbeat: Linux erfolgreich gestartet, alle Services laufen).

Die Funktion der grünen und der roten LED kann geändert werden. Diese können zum
Beispiel die Ausnutzung der
:ref:`CPU oder der SD Karte <red_brick_brickv_settings_brickd>` anzeigen,
anstatt des Heartbeats.

.. _red_brick_micro_sd_card_slot:

Micro-SD-Kartenslot
^^^^^^^^^^^^^^^^^^^

Das Linux System und alle Daten sind auf einer Micro-SD-Karte gespeichert.
Der Kartenslot ist auf der Unterseite des Bricks.
Micro-SD (1.0), Micro-SDHC (2.0) und Micro-SDXC (3.0) Karten werden
unterstützt. Wir empfehlen als Minimum eine Class 10 Micro-SD-Karte mit
einer Leserate von mindestens 30MB/s um schnelle Lese- und
Schreibvorgänge zu ermöglichen.

Eine Beschreibung der Images befindet sich im
:ref:`Image Abschnitt <red_brick_images>`.

.. _red_brick_usb_host:

USB 2.0 Host
^^^^^^^^^^^^

Der RED Brick ist mit einer Standard
`USB 2.0 <https://de.wikipedia.org/wiki/USB>`__ (480Mb/s) Typ A Buchse
ausgestattet. Mit ihr können USB Geräte mit bis zu 7,5W (5V/1,5A) betrieben
werden. Ein Kurzschluss-Schutz schützt den RED Brick und das angeschlossene
Gerät. Typische USB Geräte, wie zum Beispiel WLAN oder Ethernet USB Stick,
Webcams, Drucker, Tastaturen, Mäuse und USB Touchscreens werden unterstützt,
sofern die nötigen Treiber auf dem RED Brick vorhanden sind.
Im Wiki findet sich eine wachsende `Liste von USB Geräten
<http://www.tinkerunity.org/wiki/index.php/DE/RED_USB>`__ die von Nutzern
erfolgreich am RED Brick getestet wurden.

Manche Ethernet oder WLAN Sticks können direkt über den Brick Viewer
konfiguriert werden.
`Unterstützte Sticks <https://www.tinkerforge.com/de/shop/accessories/red-brick.html>`__
bieten wir in unserem Shop an. Andere Geräte müssen ggf. direkt
im Linux System konfiguriert werden und können nicht vom Brick Viewer
konfiguriert werden.


.. _red_brick_mini_usb:

Mini-USB
^^^^^^^^

Über den Mini-USB Anschluss wird der RED Brick vom
:ref:`Brick Viewer <red_brick_brickv>` gesteuert und konfiguriert. Der RED
Brick kann auch über diesen mit Strom versorgt werden.


.. _red_brick_hdmi:

Micro-HDMI
^^^^^^^^^^

Mit dem Micro-`HDMI <https://en.wikipedia.org/wiki/HDMI>`__ Anschluss
(auch Typ D genannt), können alle Standard HDMI Monitore und Fernseher mit dem
RED Brick verbunden werden. HDMI Ethernet Channel (HEC) wird nicht unterstützt.


Brick Stapel Stecker
^^^^^^^^^^^^^^^^^^^^

Der RED Brick kann bis zu acht andere Bricks über den Stapelstecker steuern.
Zusätzlich können bis zu zwei Master Extensions genutzt werden. Aktuell
werden nur die :ref:`RS485 Extension <rs485_extension>` und alle Versionen der
:ref:`Ethernet Extension <ethernet_extension>`
unterstützt. Jede Extension kann maximal einmal im Stapel verbaut werden.
Zwei RS485 oder zwei Ethernet Extensions sind also nicht möglich.

Die :ref:`WIFI Extension <wifi_extension>` wird zur Zeit nicht unterstützt.
Wir empfehlen die Nutzung eines WLAN USB Sticks um den RED Brick ins WLAN zu
bringen.

Die Ethernet Extension taucht als normale Ethernet-Schnittstelle des Linux
Systems auf. Über eine :ref:`Step-Down Power Supply <step_down_power_supply>`
kann der RED Brick und die anderen Module des Stapels mit Strom versorgt werden.
Dazu muss dieser nur unter den RED Brick gesteckt werden.


Stromversorgung
^^^^^^^^^^^^^^^

Der RED Brick muss mit 5V versorgt werden. Er kann über den
Mini-USB Anschluss oder eine
:ref:`Step-Down Power Supply <step_down_power_supply>` versorgt werden. Ein
einzelner RED Brick benötigt bis zu 1,1 Watt, so dass ein typisches 5W
(5V/1A) USB Netzteil ausreicht um diesen und zum Beispiel ein Master Brick
mit ein paar Bricklets zu versorgen. Bei größeren Aufbauten sollte der
Strombedarf berechnet werden und eine geeignete Stromversorgung genutzt werden.
Dabei dürfen zusätzlich angeschlossene USB Geräte, die ebenfalls versorgt
werden, nicht außer acht gelassen werden.

.. _red_brick_faq:

FAQ
---

* Q: Ich habe mein RED Brick mit einem Linux PC verbunden. Ich sehe aber
  kein ``/dev/ttyACM0`` Gerät um mich mit der seriellen Konsole zu verbinden.

  A: Der ``cdc_acm`` Treiber muss geladen werden.
* Q: Die rote und blaue LED sind an, aber nichts passiert.

  A: Der RED Brick bootet nicht. Überprüfe die Micro-SD-Karte.


.. _red_brick_known_issues:

Bekannte Probleme
-----------------

**Zweite Master Extension funktioniert nicht immer** (gelöst)

Die Kernel Konfiguration in Image Version 1.0 ist fehlerhaft.
Dadurch kann es bei gleichzeitiger Verwendung zweier Master Extension auf dem
RED Brick dazu kommen, dass die zweite Extension nicht immer richtig
funktioniert.

Seit Image Version 1.1 ist die Kernel Konfiguration korrigiert, so dass dort
dieses Problem nicht mehr auftritt.

**C# Programm stürzt beim Starten ab** (gelöst)

Image Version 1.0 beinhalten C# Bindings, die versehentlich für
CLR Version 4 kompiliert wurde. Mit diesen C# Bindings stürzt Mono ab, wenn
das C# Programm für CLR Version 2 kompiliert wurde::

  Missing method .ctor in assembly /usr/lib/Tinkerforge.dll, type System.Runtime.Versioning.TargetFrameworkAttribute

Um dieses Problem zu beheben, kann entweder das C# Programm für CLR Version 4
kompiliert, oder in der :ref:`C# Konfiguration
<red_brick_program_tab_step3_csharp>` des Programms folgende Zeile::

  --runtime=v4.0

als Mono Option hinzugefügt werden.

Dieses Problem betrifft nur Image Version 1.0. Seit Image Version 1.1
sind C# Bindings wieder für CLR Version 2 kompiliert, so dass dort dieses
Problem nicht mehr auftritt.


**Stapel mit NFC/RFID Bricklet auf RED Brick taucht im Brick Viewer nicht auf** (gelöst)

Problematischer Aufbau: Master Brick mit NFC/RFID Bricklet und irgendeinem
weiteren Bricklet steckt auf einem RED Brick. Dann taucht nur der RED Brick
im Brick Viewer auf, aber sonst kein weitere Brick oder Bricklet aus dem
Stapel.

Das Problem wird durch eine Inkompatibilität im NFC/RFID Bricklet Plugin
Version 2.0.0 verursacht. Diese Inkompatibilität ist in Plugin Version 2.0.1
behoben.

**FPC (Delphi/Lazarus) Library ist nicht Verfügbar auf dem RED Brick** (gelöst)

Leider hat sich durch eine Laste-Minute-Änderung ein Bug in die Delphi/Lazarus
Bindings eingeschlichen. Aufgrund dieses Bugs sind keine FPC Libraries auf
dem RED Brick Image (Version 1.0 und 1.1) vorhanden. Dies wird in Version 1.2
behoben. In der Zwischenzeit kann das Problem über die Konsole gelöst werden::

 sudo su
 # password = tf

 cd /usr/tinkerforge/bindings/delphi/source/
 sed -i -e 's/BrickRED//g' Makefile.fpc
 export FPCDIR=/usr/lib/fpc/`ls /usr/lib/fpc/ | grep -E [0-9].[0-9].[0-9] | head -n1`
 fpcmake
 make
 make install

Jetzt sollte die FPC Library ordnungsgemäß installiert sein und alles
sollte wie erwartet funktionieren!

Dieses Problem tritt nur in Image Version 1.0 und 1.1 auf, es ist seit
Image Version 1.2 beseitigt.

**Keine Namensauflösung** (gelöst)

In Image Version 1.2 steht Standardmäßig keine Namensauflösung (DNS) zur 
Verfügung. Das Problem kann über die Konsole gelöst werden::

 sudo su
 # enter password tf

 echo "nameserver 8.8.8.8" > /etc/resolv.conf

Dieses Problem tritt nur in Image Version 1.2 auf, es ist seit Image Version
1.3 beseitigt.

**Ethernet Extension wird im Extension-Tab angezeigt, aber nicht in den Netzwerkeinstellungen** (gelöst)

In Image Version 1.4 kann der RED Brick Probleme haben den Treiber für die
Ethernet Extension zu finden. Das Problem kann über die Console gelöst werden::

 sudo su
 # enter password tf

 ln -s /lib/modules/3.4.103+/kernel/drivers/net/ethernet/wiznet/w5x00.ko /lib/modules/3.4.90+/kernel/drivers/net/ethernet/wiznet/

Dieses Problem tritt nur in Image Version 1.4 auf.

.. _red_brick_history:

Historie
--------

Die Entwicklung des RED Bricks hat fast ein Jahr gedauert und ist in
verschiedenen Blog Posts dokumentiert:

* `Tinkerforge goes Stand-Alone aka RED Brick <http://www.tinkerforge.com/de/blog/2014/2/21/tinkerforge-goes-stand-alone-aka-red-brick>`__
* `RED Brick Leiterplatten angekommen <http://www.tinkerforge.com/de/blog/2014/4/10/red-brick-leiterplatten-angekommen>`__
* `Neuigkeiten zum RED Brick <http://www.tinkerforge.com/de/blog/2014/5/13/neuigkeiten-zum-red-brick>`__
* `RED Brick: Tut es? Oder tut es nicht? <http://www.tinkerforge.com/de/blog/2014/5/21/red-brick:-tut-es-oder-tut-es-nicht>`__
* `RED Brick Software-Infrastruktur <http://www.tinkerforge.com/de/blog/2014/6/20/red-brick-software-infrastruktur>`__
* `RED Brick im EMV Labor <http://www.tinkerforge.com/de/blog/2014/8/28/red-brick-im-emv-labor>`__
* `RED Brick Zustandsbericht <http://www.tinkerforge.com/de/blog/2014/10/15/neuigkeiten-zum-red-brick>`__
* `RED Brick, der Countdown läuft <http://www.tinkerforge.com/de/blog/2014/11/12/red-brick-der-countdown-laeuft>`__


.. _red_brick_programming_interface:

Programmierschnittstelle
------------------------

Die RED Brick API ist dazu gedacht um für den Brick Viewer die angebotene
Funktionalität zu implementieren (Statusinformationen bekommen, Programme
managen, etc.). Diese API ist ggf. für Power User interessant, normale
Nutzer benötigen diese nicht.

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine
detaillierte Beschreibung.

.. include:: RED_Brick_hlpi.table
