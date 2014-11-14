
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
vorinstalliert. Weitere notwendige Bibliotheken können nachinstalliert werden.

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

Erste Schritte / Teste das RED Brick
---------------------------------

Mit den folgenden Schritten kann der RED Brick getestet werden.

Ein Schritt für Schritt Tutorial zu dem RED Brick kann hier gefunden werden:
:ref:`RED Brick Tutorial <tutorial_red_brick>`.

Als erstes müssen :ref:`Brick Daemon <brickd>` und :ref:`Brick Viewer <brickv>`
Software auf einem PC oder Mac installiert werden. Anschließend sollte die Micro
SD Karte in den :ref:`Micro SD Card Slot <red_brick_micro_sd_card_slot>` des
RED Bricks gesteckt werden. Die Position von diesem und eine Übersicht über
alle Schnittstellen des Bricks lässt sich in dem 
:ref:`Hardware Abschnitt <red_brick_hardware>` finden. Es können SD Karten mit 
vorinstalliertem Image in unserem Shop bestellt werden (TODO Link?). Ansonsten
muss ein :ref:`Image of eine SD Karte kopiert werden <red_brick_copy_image>`.

Danach ist der RED Brick einsatzbereit und kann mit dem PC oder Mac mit einem 
Mini USB Kabel verbunden werden.

TODO: Image RED Brick with micro USB cable connected

Nachdem die Brick Viewer software gestartet wurde muss auf "connect" geklickt 
werden. Ein Tab (Reiter), beschriftet mit "RED Brick", sollte auftauchen. Dieser 
Tab sollte angelickt werden.

TODO: Image RED Brick Tab.

Auf der linken Seite des Tabs sind weitere Tabs vorhanden. Der "Overview" Tab 
gibt eine Übersicht über die CPU Last, Speicherbelegung und anderen 
Statusinformationen. Diese Ansicht bedeutet, dass der RED Brick wie erwartet
funktioniert und Programme hochgeladen werden können. Im 
:ref:`Brick Viewer Abschnitt <red_brick_brickv>` wird beschrieben wie der
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
Brick neugestartet werden, oder aber das RED Brick selber neugestartet oder 
herunter gefahren werden.

Overview Tab (Statusinformation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dieser Tab ist standardmäßig selektiert. Er zeigt die Zeit, die das RED Brick
bereits läuft (Uptime) sowie die CPU- und Speicher- Nutzung an. Weiter unten
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
* ``tf0```: Ist die Ethernet-Schnittstelle, die erzeugt wird, wenn eine
  :ref:`Ethernet Extension <ethernet_extension>` auf den RED Brick gesteckt
  wird.

Die Statusanzeigen werden alle 3 Sekunden aktualisiert.

.. _red_brick_brick_settings:

Settings Tab (Netzwerk, Brick Daemon, Datum/Uhrzeit)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _red_brick_brick_settings_network:

In dem **Network Abschnitt** dieses Tabs können alle Einstellungen zu Netzwerken
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

Zu den Konfigurationsmöglichkeiten gehören die Address auf dem der Brick Daemon
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
:ref:`GPS Bricklet <bricklet_gps>` benutzt werden. Dazu muss nur ein kleines
`Programm von Github <https://github.com/Tinkerforge/red-brick/tree/master/programs/gps_time>`__
heruntergeladen werden und auf den RED Brick geladen werden um die Uhrzeit 
mittels GPS Uhrzeit zu synchronisieren.

.. _red_brick_brickv_program:

Program Tab (Programme hochladen und ausführen)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

.. _red_brick_brickv_console:

Console Tab (Konsole, Fernsteuerung)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn das RED Brick mittels `Mini USB Anschluss <red_brick_mini_usb>`__ mit einem
PC verbunden ist regestriert es eine serielle Schnittstelle. Diese Schnittstelle
kann dazu genutzt werden um auf die Linux Shell des RED Bricks zuzugreifen. Dazu
muss nur die entsprechende Schnittstelle gewählt werden und *Connect* gedrückt 
werden. Die Schnittstelle ist typischerweise unter Linux ``/dev/ttyACM0``, unter
Windows ``TODO`` und unter OS X ``TODO``. Mit dem Nutzer **tf** und Passwort
**tf** kann man sich einloggen. Falls unbekannt ist welche Schnittstelle die 
richtig ist, kann diese durch Ausprobieren bestimmt werden. Es kann notwendig 
sein die ENTER Taste zu drücken um die Kommandozeile zu sehen.

Nachfolgend ein Screenshot, das die Konsole mit dem Befehl ``htop`` zeigt.


.. image:: /Images/Screenshots/brickv_red_tab_console.jpg
   :scale: 60 %
   :alt: Screenshot des Console Tab zeigt htop.
   :align: center

Ein gutes Shell Tutorial kann unter 
`linuxcommand.org <http://linuxcommand.org/lc3_learning_the_shell.php>`__ 
gefunden werden.

Versions Tab (Daemon, Bindings und Bibliotheken)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. _red_brick_hardware:

Hardwarebeschreibung
--------------------

Das RED Brick ist mit einem 1Ghz Cortex A8 mit 512MB DDR3 SDRAM ausgestattet.
Dazu kommen noch diverse Schnittstellen

Power Button
^^^^^^^^^^^^

LEDs
^^^^


Linux Images
------------

Im Hintergrund läuft ein von uns angepasstes Debian Image. Dieses ist in zwei 
Versionen verfügbar. Das Full Image TODO. Das TODO Image.

Full Image
^^^^^^^^^^

X Image
^^^^^^^

.. _red_brick_test:

Erster Test
-----------

.. _red_brick_usage:

Nutzung des RED Bricks
----------------------

Programme ausführen
^^^^^^^^^^^^^^^^^^^
TODO Link auf RED Brick Tutorial

Ethernet konfigurieren
^^^^^^^^^^^^^^^^^^^^^^




.. _red_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RED_Brick_hlpi.table
