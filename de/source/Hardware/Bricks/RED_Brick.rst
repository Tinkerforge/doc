
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. note::
  Dieses Brick befindet sich noch in Entwicklung und ist noch nicht erhältlich

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_red_prototype_350.jpg",
	               "Bricks/brick_red_prototype_600.jpg",
	               "RED Brick Prototyp")
	}}
	{{ tfdocend() }}


Features
--------

* Steuert andere Bricks und Bricklets
* Führt direkt dein geschriebenes Programm aus
* Unterstützt nahezu alle Programmiersprachen

.. _red_brick_description:

Beschreibung
------------

.. note::
  Dieses Brick befindet sich noch in Entwicklung und ist noch nicht erhältlich. Geplanter Verkaufsstart: Dez 2014. 

  Aktuelle Informationen lassen sich in unserem `Blog <http://www.tinkerforge.com/de/blog/>`__ finden. Bisherige Blogposts:

  * `Tinkerforge goes Stand-Alone aka RED Brick <http://www.tinkerforge.com/de/blog/2014/2/21/tinkerforge-goes-stand-alone-aka-red-brick>`__
  * `RED Brick Leiterplatten angekommen <http://www.tinkerforge.com/de/blog/2014/4/10/red-brick-leiterplatten-angekommen>`__
  * `Neuigkeiten zum RED Brick <http://www.tinkerforge.com/de/blog/2014/5/13/neuigkeiten-zum-red-brick>`__
  * `RED Brick: Tut es? Oder tut es nicht? <http://www.tinkerforge.com/de/blog/2014/5/21/red-brick:-tut-es-oder-tut-es-nicht>`__
  * `RED Brick Software-Infrastruktur <http://www.tinkerforge.com/de/blog/2014/6/20/red-brick-software-infrastruktur>`__
  * `RED Brick im EMV Labor <http://www.tinkerforge.com/de/blog/2014/8/28/red-brick-im-emv-labor>`__
  * `RED Brick Zustandsbericht <http://www.tinkerforge.com/de/blog/2014/10/15/neuigkeiten-zum-red-brick>`__
  * `RED Brick, der Countdown läuft <http://www.tinkerforge.com/de/blog/2014/11/12/red-brick-der-countdown-laeuft>`__



Der Rapid Embedded Development :ref:`Brick <primer_bricks>` (RED Brick) kann 
andere :ref:`Bricks <primer_bricks>` und :ref:`Bricklets <primer_bricklets>` 
steuern. Die aktuell unterstützten Sprachen: C/C++, C#, Delphi/Lazerus, Java, 
JavaScript, MATLAB/Octave, Perl, PHP, Python, Ruby, Shell und Visual Basic .NET, 
können direkt auf dem Brick ausgeführt werden.

Ein Programm, das Bricks und Bricklets steuert, kann auf einem normalen 
PC/Mac geschrieben und getestet werden. Anschließend kann es per Knopfdruck auf 
den RED Brick übertragen und ohne Änderungen auf diesen ausgeführt werden. 
Es können mehrere Programme gleichzeitig ausgeführt werden und deren Ausführung 
konfiguriert (nach dem Booten, jede Stunde, etc.) sowie überwacht werden.

Eigene Projekte können somit sehr schnell und einfach realisiert werden. 
Unseres Wissens nach ist keine auch nur im Ansatz vergleichbare Lösung 
erhältlich. 

Für jede unterstützte Programmiersprache sind die 
:ref:`Tinkerforge API <api_bindings>` und häufig genutzte Bibliotheken 
vorinstalliert. Weitere Bibliotheken können nachinstalliert werden.

Der Brick ist mit einem `Micro-HDMI <http://de.wikipedia.org/wiki/HDMI>`__
Anschluss ausgestattet, so dass auch 
Programme mit grafischer Benutzeroberfläche ausgeführt werden können. Eine 
`USB 2.0 <http://de.wikipedia.org/wiki/USB>`__ Host Schnittstelle kann genutzt 
werden um Eingabe- und Zeigegeräte, wie Tastaturen, Mäuse oder Touchscreens, 
zu nutzen.

Mit der :ref:`Ethernet Master Extension <ethernet_extension>` kann der RED Brick 
um eine Ethernetschnittstelle erweitert werden. Die 
:ref:`RS485 Master Extension <rs485_extension>` wird ebenfalls unterstützt, so 
dass auch entfernte Stapel von Bricks und Bricklets vom RED Brick gesteuert 
werden können.

Fortgeschrittene Nutzer können den Brick mit vollem Zugriff auf dem 
zugrundeliegenden `Debian <http://www.debian.org>`__ System nutzen. Ein GPIO FPC 
Steckverbinder ermöglicht den Zugriff auf ausgewählte Prozessorsignale und kann 
genutzt werden um eigene Entwicklungen anzubinden.

Technische Spezifikation
------------------------

================================  ==================================================================================
Eigenschaft                       Wert
================================  ==================================================================================
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           14g
Stromverbrauch                    0,75W or 5V/150mA (Leerlauf), 1,1W or 5V/220mA (100% Last)
--------------------------------  ----------------------------------------------------------------------------------

--------------------------------  ----------------------------------------------------------------------------------
Processor                         Allwinner A10s, Cortex A8 1GHz, 3D Mali400 GPU, NEON
Memory                            512MB DDR3 SDRAM, Micro SD Karte als Flash Speicher
Connectors                        USB 2.0, micro HDMI (type D), micro USB, Stapel Verbinder, GPIO FPC Steckverbinder
================================  ==================================================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/red_brick_dimensions.png>`__)
* Linux Image und Platinenlayout (`Download <https://github.com/Tinkerforge/red-brick/zipball/master>`__)

.. _red_brick_test:

Erste Schritte / Teste den RED Brick
------------------------------------

Mit den folgenden Schritten kann der RED Brick getestet werden.

Ein Schritt für Schritt Tutorial zu dem RED Brick kann hier gefunden werden:
:ref:`RED Brick Tutorial <tutorial_red_brick>`.

Als erstes müssen :ref:`Brick Daemon <brickd>` und :ref:`Brick Viewer <brickv>`
Software auf einem PC oder Mac installiert werden. Anschließend sollte die Micro
SD Karte in den :ref:`Micro SD Karten Slot <red_brick_micro_sd_card_slot>` des
RED Bricks gesteckt werden. Die Position von diesem und eine Übersicht über
alle Schnittstellen des Bricks lässt sich in dem 
:ref:`Hardware Abschnitt <red_brick_hardware>` finden. Es können SD Karten mit 
vorinstalliertem Image in unserem Shop bestellt werden (TODO Link?). Ansonsten
muss ein :ref:`Image auf eine SD Karte kopiert werden <red_brick_copy_image>`.

Danach ist der RED Brick einsatzbereit und kann mit dem PC oder Mac mit einem 
Mini USB Kabel verbunden werden.

TODO: Image RED Brick with micro USB cable connected

Nachdem die Brick Viewer Software gestartet wurde muss auf "connect" geklickt 
werden. Ein Tab (Reiter), beschriftet mit "RED Brick", sollte auftauchen. Dieser 
Tab sollte angelickt werden.

TODO: Image RED Brick Tab.

Auf der linken Seite des Tabs sind weitere Tabs vorhanden. Der "Overview" Tab 
gibt eine Übersicht über die CPU Last, Speicherbelegung und anderen 
Statusinformationen. Normale Anzeigen bedeuten, dass der RED Brick wie erwartet
funktioniert und Programme hochgeladen werden können. Im 
:ref:`Brick Viewer Abschnitt <red_brick_brickv>` wird beschrieben, wie der
RED Brick konfiguriert werden kann und wie Programme hochgeladen werden.

Nutzer des :ref:`Full Image <red_brick_images>` können zusätzlich die grafische
Nutzerschnittstelle (HDMI) testen. Dazu muss ein Monitor an den 
:ref:`HDMI Anschluss <red_brick_hdmi>` und ein USB Hub mit Tastatur und Maus an
dem :ref:`USB Anschluss <red_brick_usb_host>` des RED Bricks angeschlossen 
werden. Während des Bootvorgangs kann das LXDE Desktop Environment gesehen 
werden, dass anschließend wie ein ganz normaler Desktop PC verwendet werden kann.

.. _red_brick_brickv:

Brick Viewer
------------
Dieser Abschnitt beschreibt die Konfiguration des RED Bricks mit der
:ref:`Brick Viewer <brickv>` Software. Das RED Brick kann ebenfalls über die
:ref:`RED Brick API <red_brick_programming_interface>` konfiguriert werden (nur 
für Poweruser gedacht).


.. image:: /Images/Screenshots/brickv_red_tab_and_labels.jpg
   :scale: 60 %
   :alt: Screenshot der Tabauswahl und Labeln.
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

Die Liste kann folgende Netzwerkschnittstellen enthalten:

* ``lo``: Dies ist die sogenannte Loopback Schnittstelle. Sie ist rein lokal und
  dient der Kommunikation zwischen Anwenderprogrammen und dem lokalen Brick 
  Daemon.
* ``wlan0``: Dies ist die WLAN-Schnittstelle. Sie wird erzeugt wenn ein WLAN 
  Stick an die :ref:`USB Host Buchse <red_brick_usb_host>` angeschlossen wird.
* ``eth0``: Dies ist eine Ethernet-Schnittstelle. Sie wird erzeugt wenn ein 
  Ethernet Stick Stick an die :ref:`USB Host Buchse <red_brick_usb_host>` 
  angeschlossen wird.
* ``tf0``: Ist die Ethernet-Schnittstelle, die erzeugt wird, wenn eine
  :ref:`Ethernet Extension <ethernet_extension>` auf den RED Brick gesteckt
  wird.

Die Statusanzeigen werden alle 3 Sekunden aktualisiert.

.. _red_brick_brick_settings:

Settings Tab (Netzwerk, Brick Daemon, Datum/Uhrzeit)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _red_brick_brick_settings_network:

TODO: Selektion über den General Tab implementiert?

In dem **Network** Abschnitt dieses Tabs können alle Einstellungen zu Netzwerken
vorgenommen werden.

TODO Image General subsection

In dem *General* Unterabschnitt kann der Hostname des RED Brick gesetzt werden.
Der aktuelle Netzwerkstatus und das aktuell benutzte Netzwerkgerät werden 
angezeigt.

TODO Image Wireless subsection

Der *Wireless* Unterabschnitt ist nur aktiv, wenn ein unterstützter USB WLAN 
Stick angeschlossen wurde. Unterstützte WLAN Sticks gibt es in unserem Shop 
(TODO Link). Die aktuell genutze WLAN Schnittstelle und deren Status werden 
angezeigt und können modifiziert werden. Hier wird auch eingestellt zu welchem 
Access Point sich verbuinden werden soll, welche Verschlüsselung eingesetzt wird 
und ob eine statische oder dynamische IP (DHCP) genutzt werden sollen.

TODO Image Wired subsection

Der *Wired* Unterabschnitt ist nur aktiv, wenn ein unterstützter USB Ethernet 
Stick oder eine Ethernet Extension angeschlossen werden. Der USB Stick wird
als ``eth0``, die Ethernet Extension als ``tf0`` erkannt. Um die Schnittstelle
zu nutzen muss sie ausgewählt und die Nutzung einer statischen IP oder
von DHCP konfiguriert werden. Anschließend muss *Save* geklickt werden.

Es kann einige Sekunden dauern bis eine IP mittels DHCP zugewiesen wird oder
sich ein WLAN Stick zu einem Netzwerk verbindet. Wenn die neue Konfiguration 
nicht sofort in dem *General* Unterabschnitt angezeigt wird, muss ggf. etwas
gewartet werden und der *Refresh* Knopf geklickt werden.

.. _red_brick_brick_settings_brickd:

In dem **Brick Daemon Abschnitt** des Tabs können Einstellungen zum lokalen 
Brick Daemon vorgenommen werden.


.. image:: /Images/Screenshots/brickv_red_tab_settings_brickd.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Brickd Konfiguration.
   :align: center

Zu den Konfigurationsmöglichkeiten gehören die Adresse auf dem der Brick Daemon
lauscht, der dazugehörige Port, der Port für die Nutzung von Websockets und 
das Authentifizierungsgeheimnis. WebSockets werden von der Browser-Version der 
:ref:`JavaScript Bindings <api-bindings-javascript>` verwendet um Bricks und 
Bricklets zu steuern. Weitere Einstellungen können in dem *Advanced* Abschnitt
gefunden werden. Die Nutzung der roten und grünen LED kann auch hier 
konfiguriert werden.

.. _red_brick_brick_settings_date:

In dem **Date/Time Abschnitt** kann die Uhr des RED Bricks mit der Uhr des
angeschlossenen PCs synchronisiert werden. Es gibt keine Batterie auf dem RED 
Brick, so dass die Uhr nicht weiterläuft wenn der RED Brick nicht läuft.

.. image:: /Images/Screenshots/brickv_red_tab_settings_date.jpg
   :scale: 60 %
   :alt: Screenshot des Settings Tabs: Datum/Uhrzeit Konfiguration.
   :align: center

Wenn eine Verbindung zum Internet besteht (Ethernet Extension oder USB WLAN 
Stick), werden Datum und Uhrzeit automatisch mittels NTP gesetzt. Dazu muss nur
die Zeitzone gesetzt werden. Diese wird gespeichert und wieder hergestellt, 
wenn der RED Brick das nächste mal hochfährt.

Falls die Zeit nach dem booten immer vorhanden sein muss, ein Verbindung zum
Internet aber nicht garantiert werden kann, dann kann auch das 
:ref:`GPS Bricklet <gps_bricklet>` benutzt werden. Dazu muss nur ein kleines
`Programm von Github <https://github.com/Tinkerforge/red-brick/tree/master/programs/gps_time>`__
heruntergeladen und auf den RED Brick geladen werden, um die Uhrzeit 
mittels GPS Uhrzeit zu synchronisieren.

.. _red_brick_brickv_program:

Program Tab (Programme hochladen und ausführen)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

.. _red_brick_brickv_console:

Console Tab (Konsole, Fernsteuerung)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn der RED Brick mittels `Mini USB Anschluss <red_brick_mini_usb>`__ mit einem
PC verbunden ist registriert es eine serielle Schnittstelle. Diese Schnittstelle
kann dazu genutzt werden um auf die Linux Shell des RED Bricks zuzugreifen. Dazu
muss nur die entsprechende Schnittstelle gewählt werden und *Connect* geklickt 
werden. Die Schnittstelle ist typischerweise unter Linux ``/dev/ttyACM0``, unter
Windows ``TODO`` und unter OS X ``TODO``. Mit dem Nutzer **tf** und Passwort
**tf** kann man sich einloggen. Falls unbekannt ist welche Schnittstelle die 
richtig ist, kann diese durch Ausprobieren bestimmt werden. Es kann notwendig 
sein die ENTER Taste zu drücken um die Kommandozeile zu sehen.

Nachfolgend ein Screenshot, das die Konsole mit dem Befehl ``htop`` zeigt.


.. image:: /Images/Screenshots/brickv_red_tab_console.jpg
   :scale: 60 %
   :alt: Screenshot des Console Tab.
   :align: center

Ein gutes Shell Tutorial kann unter 
`linuxcommand.org <http://linuxcommand.org/lc3_learning_the_shell.php>`__ 
gefunden werden.

Versions Tab (Daemon, Bindings und Bibliotheken)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der Version Tab gibt Informationen über den installierten Brick Daemon, RED 
Brick API Daemon sowie die installierten Bindings und deren Bibliotheken.

.. image:: /Images/Screenshots/brickv_red_tab_versions.jpg
   :scale: 60 %
   :alt: Screenshot des Versions Tab.
   :align: center

Wenn andere Bibliotheken, wie die installierten genutzt werden sollen, dann 
können diese entweder mit dem eigenen Programm 
:ref:`hochgeladen werden <red_brick_brickv_program>` oder aber mittels
``apt-get``, ``pip``, ``pear``, ``npm`` oder aber eines ähnlichen Paketmanagers
installiert werden. Die genannten Paketmanager sind in allen RED Brick Images 
vorinstalliert.

Extensions Tab (Konfiguration, Verwaltung)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zwei :ref:`Master Extensions <primer_master_extensions>` werden vom RED Brick 
unterstützt: :ref:`Ethernet Extension <ethernet_extension>` und 
:ref:`RS485 Extension <rs485_extension>`.

**Ethernet Extension**

.. image:: /Images/Screenshots/brickv_red_tab_extension_ethernet.jpg
   :scale: 60 %
   :alt: Screenshot des Extension Tabs: Ethernet Extension Konfiguration.
   :align: center

Nur die MAC Adresse der Ethernet Extension kann hier geändert werden. Da diese
als normale Netzwerkschnittstelle auftaucht, können die Netzwerkeinstellungen im 
:ref:`Settings Tab <red_brick_brick_settings>` verändert werden.

**RS485 Extension**

.. image:: /Images/Screenshots/brickv_red_tab_extension_rs485.jpg
   :scale: 60 %
   :alt: Screenshot des Extension Tabs: RS485 Extension Konfiguration.
   :align: center

Die Konfiguration der RS485 Extension ist identisch zu der mittels einem Master 
Brick. Siehe :ref:`RS485 Extension Dokumentation <rs485_configuration>`

Wir empfehlen Baudraten von 500000, 250000, 166666, 125000, 100000, 83333, 
71428, 62500, 55555, 50000, 45454 oder 41666 Baud bei Benutzung eines RED 
Bricks.

Eine Änderung der Einstellungen zu einer Extension führen zu einem Neustart des
Brick Daemons, d.h. der RED Brick Tab verschwindet kurz aus dem Brick Viewer
und taucht kurze Zeit später wieder auf.

.. _red_brick_web_interface:

RED Brick Web Interface
-----------------------

Wenn der RED Brick mit einem USB WLAN Stick, Ethernet Extension oder eine andere
Netzwerkverbindung ausgestattet ist, kann auf das Web Interface zugegriffen 
werden. Das Web Interface is unter der IP Adresse des RED Bricks oder unter
dessen Hostnamen (Voreinstellung: ``red-brick``) erreichbar.

Das RED Brick Web Interface zeigt die installierten Programme. Deren Logs und
Konfiguration als auch die hochgeladenen Dateien werden angezeigt.

.. image:: /Images/Screenshots/red_brick_web_interface.jpg
   :scale: 40 %
   :alt: Screenshot des RED Brick Web Interfaces.
   :align: center

Neben dem vorinstallierten Web Interface können auch eigene installiert werden.
Es werden Webanwendungen, die in HTML/Javascript, Python oder PHP geschrieben
sind, unterstützt. Wenn eine ``index.py``, ``index.php`` oder ``index.html`` 
hochgeladen wird, so wird diese als Index Datei des binary Ordners genutzt.

**Beispiel zur Erklärung:** Es soll eine PHP Webseite entwickelt werden, die 
Bricks/Bricklets steuert. Dazu wird das PHP Programm ``EXAMPLE`` mit der ID 
``EXAMPLEID`` hochgeladen, das eine index.php als Startpunkt enthält. Wird 
anschließend der RED Brick Web Interface aufgerufen und der "Bin" Button der 
``EXAMPLE`` Anwendung geklickt, so wird der Link zu ``/programs/EXAMPLEID/bin`` 
geöffnet. Dieser Link führt direkt die index.php aus.

Webseiten, die Umwelt-Messungen von einem Temperature/Barometer/Humidity 
Bricklets anzeigt können somit sehr einfach erstellt werden. Es können aber auch
Aktoren, zum Beispiel ein Relay Bricklet, über Buttons gesteuert werden.

Mit dem RED Brick ist es also sehr einfach, Web-Anwendungen zu entwickeln, die
Hardware steuern.

HTML/Javascript
^^^^^^^^^^^^^^^

Wenn eine HTML datei mit eingebetteten JavaScript hochgeladen wird, können die 
JavaScript Bindings genutzt werden. Diese sind direkt im Root Verzeichnis 
verfügbar.

 <script src="/Tinkerforge.js" type='text/javascript'></script>

Das JavaScript wird im Browser des Benutzers ausgeführt und nicht auf dem RED 
Brick. Aus diesem Grund muss sich mit der IP des RED Bricks verbunden werden
und nicht mit localhost.

Python
^^^^^^
Auf dem Webserver (Apache) des RED Bricks wird WSGI 
(`mod_wsgi <https://code.google.com/p/modwsgi/>`) von Python genutzt um 
Webseiten darzustellen. Dieser ist konfiguriert um eine ``index.py`` als
Startpunkt für ein WSGI Skript zu nutzen. Alle verbreiteten Python Web 
Frameworks unterstützen WSGI. Das `Flask framework <http://flask.pocoo.org/>`__ 
ist auf dem RED Brick vor installiert (beinhaltet
`Werkzeug <http://werkzeug.pocoo.org/>`__ und 
`Jinja <http://jinja.pocoo.org/>`__).

Ein minimales Flask Web Interface das auf den RED Brick hochgeladen werden kann,
ist eine ``index.py`` mit folgenden Inhalt::

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
Python/Flask. Es kann auf
`Github <https://github.com/Tinkerforge/red-brick/blob/master/image/patches/root-fs/common/tmp/index.py>`__
gefunden werden.

Es können natürlich auch templates, statische Dateien und so weiter benutzt 
werden. Diese können genauso benutzt werden wie in den meisten Flask Tutorials
gezeigt. Ein `etawas komplexeres Flask Beispiel <TODO>`__, dass mehr
Features nutzt liegt ebenfalls auf Github.

PHP
^^^

Der Webserver auf dem RED Brick ist dazu eingerichtet eine ``index.php`` zu 
erkennen.

Eine minimale Hallo Welt index.php könnte wie folgt aussehen::

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

RED Brick Software Images
-------------------------

Das RED Brick Software Image ist auf einer Micro SD Karte gespeichert. Es ist 
ein modifiziertes `Debian <http://debian.org/>`__ Image und in zwei 
verschiedenen Versionen erhältlich: Das ''full'' und das ''fast'' Image. Beide
Images unterstützen die Ausführung von eigenen Programmen und verfügen über alle
notwendigen Tinkerforge Bibliotheken.

Das **Full Image** verfügt über GPU Treiber und besitzt alle notwendigen
Bibliotheken für die Nutzung von grafischen Nutzerschnittstellen (GUIs). Ein
X Server startet während des Bootvorgangs und das 
`LXDE Desktop Environment <http://www.lxde.org>`__ wird mit Autologin gestartet.
Wenn das eigene Programm eine grafische Nutzerschnittstelle nutzt, so wird 
diese auf dem Desktop angezeigt. Die Bildschirmauflösung passt sich der 
Voreinstellung des angeschlossenen HDMI Monitors an. Über LXDE kann diese aber
auch konfiguriert werden. Die HDMI Schnittstelle muss aber nicht benutzt werden
und es können auch Programme ohne grafische Nutzerschnittstelle ausgeführt
werden.

Das **Fast Image** besitzt keine GPU Treiber und es sind keine Bibliotheken für
grafische Nutzerschnittstellen, ein X Server und LXDE installiert. Da diverse
Treiber und die grafische Nutzerschnittstelle nicht geladen werden müssen
erfolgt der Bootvorgang mit einer Dauer von 10s (TODO korrekt?) deutlich 
schneller.

Neue Software kann in beiden Images installiert werden. Siehe
`installing section <TODO>`__ wie neue Software installiert wird.

Eine Liste mit den vorinstallierten Bibliotheken kann hier gefunden werden:

* `Full Image Installed Programs List <TODO_Link_to_download_page>`__.
* `Fast Image Installed Programs List <TODO_Link_to_download_page>`__.

Der Nutzer **tf** ist der Standardnutzer auf den Images. Beim Einloggen über die
Konsole oder in LXDE kann dieser Nutzer mit dem Standardpasswort **tf** benutzt
werden. Der Nutzer ist ein sudoer, so dass Root-Zugriff mittels::

 sudo su

erhalten werden kann. Die Images können von der
`Download Seite <TODO_LINK_TO_DOWNLOAD>`__ herunter geladen werden.

.. _red_brick_build_image:

Baue dein eigenes Image
^^^^^^^^^^^^^^^^^^^^^^^
Bei dieser Anleitung nehmen wir an, dass ein 
`Debian Linux <https://www.debian.org/>`__ als Host Plattform genutzt wird.

1. RED Brick Git auschecken::

    git clone https://github.com/Tinkerforge/red-brick

2. In den Ordner *image* gehen, die Datei README.rst und die dokumentierten 
   Schritte durchführen.

Das Bauen eines Images kann 4-6 Stunden dauern, abhängig von der 
Leistungsfähigkeit des genutzten Rechners kann es auch deutlich
länger dauern.

.. _red_brick_copy_image:

Image auf SD Karte kopieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Das
   :ref:`Full Image oder Fast Image <red_brick_images>` von der RED Brick:
   `Download-Seite  <TODO_Link_to_download_page>`__ herunterladen.

2. Eine geeignete micro SD Karte suchen. Wir empfehlen eine schnelle Karte
   (z.B. Class 10, >30MB/sek. Lesen) mit genügend Speicherplatz. Die Größe 
   des Images steht ebenfall auf der Downloadseite.
3. Das Image auf die SD Karte kopieren:

    * Für Windows nutze ein Tool wie Win32DiskImager um das Image auf die Karte zu kopieren.

        * `Download Link <https://sourceforge.net/projects/win32diskimager/files/latest/download>`__ 
        * `Dokumentation <http://sourceforge.net/p/win32diskimager/wiki/Home/>`__

    * Auf OS X und Linux

        * Verbinde die SD Karte mit dem PC 
        * Identifiziere den Pfad zu der SD Karte (z.B. dmesg)
        * sudo dd if=path_of_your_image.img of=path_to_sdcard bs=1M

            * Beispiel: ``dd if=/tmp/red_full_image.img of=/dev/sdb bs=1M``

.. _red_brick_hardware:


Hardwarebeschreibung
--------------------


TODO: Overview Image with Top and Bottom Side


Power Button
^^^^^^^^^^^^
TODO: Image of Power Button

Der Taster auf dem RED Brick ist ein Power Button. Wenn dieser länger wie 5 
Sekunden gedrückt wird, so schaltet sich der RED Brick ab. Wenn der Brick
aus ist, kann dieser über den Button auch wieder eingeschalten werden. Dazu
muss der Button solange gedrückt werden (ca. 3 Sekunden) bis die blaue LED
an geht. Der Brick bootet anschließend.

.. _red_brick_leds:

LEDs
^^^^

TODO: Image of RED Brick with arrows to LEDs

Der RED Brick besitzt drei verschiedene LEDs auf der Oberseite. Eine blaue, 
eine rote und eine grüne LED.

Die blaue LED ist direkt mit der internen Stromversorgung des Prozessors 
verbunden und leuchtet damit immer wenn der Brick mit Strom versorgt ist.

Die rote LED zeigt an wenn ein Fehler vorliegt. Wenn die rote LED während des 
Bootvorgangs dauerhaft leuchtet, so konnte kein Image gefunden werden. Es ist
entweder keine SD Karte vorhanden oder auf dieser ist kein gültiges Image.

Die grüne LED zeigt den aktuellen Status. Wenn beim Starten die rote LED
aus geht und die grüne nicht an, dann konnte Linux nicht korrekt booten.
Während des Bootvorgangs geht die grüne LED an, nachdem alle Services gestartet
sind und der Brick bereit ist blinkt diese (Heartbeat).

Ein normaler Bootvorgang verläuft wie folgt:

1. Blaue und rote LED sind an, Grüne LED ist aus.
2. Rote LED geht aus (U-Boot geladen).
3. Grüne LED geht an (Linux bootet).
4. Grüne LED blinkt (heartbeat) (Linux erfolgreich gestartet, alle Services laufen).

Die Funktion der grünen und der roten LED kann geändert werden. Diese können zum 
Beispiel die Ausnutzung der 
:ref:`CPU oder der SD Karte <red_brick_brick_settings_brickd>` anstatt des 
Heartbeats.

.. _red_brick_micro_sd_card_slot:

Micro SD Karten Slot
^^^^^^^^^^^^^^^^^^^^

TODO: Image of SD Card Slot

Das Linux System und alle Daten sind auf einer Micro SD Karte gespeichert.
Der Kartenslot ist auf der Unterseite des Bricks.
Micro SD (1.0), Micro SDHC (2.0) und Micro SDXC (3.0) Karten werden 
unterstützt. Wir empfehlen als Minimum eine Class 10 Micro SD Karte mit
einer Leserate von mindestens 30MB/sek um schnelle Lese- und 
Schreibvorgänge zu ermöglichen.

Eine Beschreibung der Images kann in dem
:ref:`Image Abschnitt <red_brick_images>` gefunden werden.

.. _red_brick_usb_host:

USB 2.0 Host
^^^^^^^^^^^^

TODO: Image of USB Port


Der RED Brick ist mit einer Standard 
`USB 2.0 <http://de.wikipedia.org/wiki/USB>`__ (480Mbps) Typ A Buchse 
ausgestattet. Mit ihr können USB Geräte mit bis zu 7.5W (5V/1.5) betrieben 
werden. Ein Kurzschluss-Schutz schützt den RED Brick und das angeschlossene
Gerät. Sowohl das Full als auch das Fast Image basieren auf Debian Linux und
unterstützen typische USB Geräte, wie zum Beispiel WLAN oder Ethernet Sticks,
Webcams, Drucker, Tastaturen, Mäuse und USB Touchscreens.

Manche Ethernet oder WLAN Sticks können direkt über den Brick Viewer 
konfiguriert werden. Unterstützte Sticks bieten wir in unserem Shop an 
(TODO Link). Andere Geräte müssen ggf. direkt im Linux System konfiguriert
werden und können nicht vom Brick Viewer konfiguriert werden.

Das :ref:`Full Image <red_brick_images>` unterstützt grafische 
Nutzerschnittstellen die per standard USB Tastatur, Mäusen oder
Touchscreens gesteuert werden können.


.. _red_brick_mini_usb:

Mini USB
^^^^^^^^
Über den Mini USB Anschluss wird der RED Brick mittels
:ref:`Brick Viewer <red_brick_brickv>` gesteuert und konfiguriert. Der RED 
Brick kann auch über diesen mit Strom versorgt werden.


.. _red_brick_hdmi:

Micro HDMI
^^^^^^^^^^

TODO: Image HDMI connector

Mit dem Micro `HDMI <http://en.wikipedia.org/wiki/HDMI>`__ Anschluss 
(auch Typ D genannt), können alle standard HDMI Monitore und Fernseher mit dem 
RED Brick verbunden werden. Der Anschluss ist nur aktiv, wenn das
:ref:`Full Image <red_brick_images>` genutzt wird. HDMI Ethernet Channel (HEC) 
wird nicht unterstützt.


Brick Stapel Stecker
^^^^^^^^^^^^^^^^^^^^

TODO: Image Stack connector

Der RED Brick kann bis zu acht andere Bricks über den Stapel Stecker steuern.
Zusätzlich können bis zu zwei Master Extensions genutzt werden. Aktuell
wird nur die :ref:`RS485 Extension <rs485_extension>` und alle Versionen der 
:ref:`Ethernet Extension <ethernet_extension>`
unterstützt. Jede Extension kann maximal einmal im Stapel verbaut werden.
Zwei RS485 oder zwei Ethernet Extensions sind also nicht möglich.

Die :ref:`WIFI Extension <wifi_extension>` wird zur Zeit nicht unterstützt. 
Wir empfehlen die Nutzung eines WLAN Sticks um den RED Brick ins WLAN zu bringen.

Die Ethernet Extension taucht als normale Ethernet Schnittstelle des Linux 
Systems auf. Über eine :ref:`Step-Down Power Supply <step_down_power_supply>` 
kann der RED Brick und die anderen Module des Stapels mit Strom versorgt werden. 
Dazu muss dieser nur unter den RED Brick gesteckt werden.

GPIO Anschluss
^^^^^^^^^^^^^^

.. note:: 

	Dieser Anschluss ist für fortgeschrittene Nutzer gedacht um eigene Hardware 
	anzuschließen. Aktuell bieten wir keine Softwareunterstützung zur Nutzung 
	dieses Anschlusses.

TODO Image Header

Der Red Brick ist mit einem 21 Pin, 0.25mm Pitch, FPC GPIO Anschluss
ausgestattet (Molex 502078-2110).

Alle Signale des A10s Prozessors auf Port E sind mit diesem GPIO Anschluss
verbunden. Diese können für verschiedene Funktionen konfiguriert werden:

General Purpose Input/Output, Transport Stream Controller (TS), Camera Sensor
Interface (CSI), Serial Peripheral Interface (SPI), Secure Digital Memory 3.0 
Card Controller (SDC), Universal Asynchronous Receiver Transmitter (UART), 
Interrupt. Zusätzlich befindet sich ein I2C (TWI) Interface auf diesen
Anschluss.

==== ======== =========================================================
Pin  Signal   Beschreibung
==== ======== =========================================================
1    5V       5V Stromversorgung
2    3V3      3.3V Stromversorgung
3    PE0      TS Clock, CSI Pixel Clock, SPI Chip Select 0, INT14, GPIO
4    GND      Masse (Ground)
5    PE1      TS Error, CSI Sensor Clock, SPI Clock, INT15, GPIO
6    GND      Masse (Ground)
7    PE2      TS Sync, CSI Horizontal Sync, SPI MOSI, GPIO
8    GND      Masse (Ground)
9    PE3      TS Data Valid, CSI Vertical Sync, SPI MISO, GPIO
10   GND      Masse (Ground)
11   PE4      TS Data 0, CSI Data 0, SD Controller Data 0, GPIO
12   PE5      TS Data 1, CSI Data 1, SD Controller Data 1, GPIO
13   PE6      TS Data 2, CSI Data 2, SD Controller Data 2, GPIO
14   PE7      TS Data 3, CSI Data 3, SD Controller Data 3, GPIO
15   PE8      TS Data 4, CSI Data 4, SD Controller Command, GPIO
16   PE9      TS Data 5, CSI Data 5, SD Controller Clock, GPIO
17   PE10     TS Data 6, CSI Data 6, UART TX, GPIO
18   PE11     TS Data 7, CSI Data 7, UART RX, GPIO
19   GND      Masse (Ground)
20   PB15     I2C Takt (mit 2k2 Pullup), GPIO
21   PB16     I2C Daten (mit 2k2 Pullup), GPIO
==== ======== =========================================================


Stromversorgung
^^^^^^^^^^^^^^^

Der RED Brick muss mit 5V versorgt werden. Er kann über den 
Mini USB connector oder eine 
:ref:`Step-Down Power Supply <step_down_power_supply>` versorgt werden. Ein 
einzelner RED Brick benötigt bis zu 1.1 Watt, so dass ein typisches 5W 
(5V/1A) USB Netzteil ausreicht um diesen und zum Beispiel ein Master Brick
mit ein paar Bricklets zu versorgen. Bei größeren Aufbauten sollte der
Strombedarf berechnet werden und eine geeignete Stromversorgung genutzt werden.
Dabei dürfen zusätzlich angeschlossene USB Geräte, die ebenfalls versorgt 
werden, nicht außer acht gelassen werden.

.. _red_brick_faq:


FAQ
---

* F: Ich habe mein RED Brick mit einem Linux PC verbunden. Ich sehe aber kein ``/dev/ttyACM0``
  Gerät um mich mit der seriellen Konsole zu verbinden.
* A: Der ``cdc_acm`` Treiber muss geladen werden


* F: Die rote und blaue LED sind an, aber nichts passiert.
* A: Der RED Brick bootet nicht. Überprüfe die micro SD Karte.


.. _red_brick_programming_interface:

Programmierschnittstelle
------------------------

Die RED Brick API ist dazu gedacht um für den Brick Viewer die angebotene 
Funktionalität zu implementieren (Statusinformationen bekommen, Programme 
managen, etc.). Diese API ist vielleicht für Power users interessant, normale
Nutzer benötigen diese nicht.

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte 
Beschreibung.

.. include:: RED_Brick_hlpi.table

