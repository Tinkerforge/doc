
.. _embedded_raspberry_pi:

Raspberry Pi
============

Hier wird beschrieben wie Bricks und Bricklets zusammen mit einem
`Raspberry Pi <https://www.raspberrypi.org/>`__ und Debian genutzt werden können.


SD Karte vorbereiten
--------------------

Als erstes musst Debian auf einer SD Karte eingerichtet werden. Es gibt zwei
Wege das zu tun.

Es gibt den empfohlenen `New Out of Box Software (NOOBS)
<https://www.raspberrypi.org/downloads>`__ Weg. Dazu wird einfach die NOOBS ZIP
Datei herunterladen, auf eine SD Karte entpackt und das Raspberry Pi damit
gestartet. Dann den Schritten des graphischen Installers folgen und "Raspbian"
zur Installation auswählen.

Falls NOOBS nicht verwendet werden soll, dann gibt es noch den alten mehr
händischen Weg eines der vorgefertigten Debian Images herunterzuladen. Hier gibt
es zwei verschiedene Varianten für das Raspberry Pi: Einmal "Raspbian" (armhf)
und "Soft-Float Debian" (armel). Raspbian nutzt die Hardware Floating Point
Unit (FPU) des Boards und ist die empfohlene Variante. Dazu muss zuerst
das neuste `Raspbian Image <https://www.raspberrypi.org/downloads>`__
heruntergeladen werden und dann den Schritten dieser `Anleitung
<https://elinux.org/RPi_Easy_SD_Card_Setup>`__ zum manuelle Einrichten einer
SD Karte folgen.

Raspberry Pi starten
--------------------

Schließe eine Tastatur, einen Bildschirm und eine Stromversorgung an das
Raspberry Pi an. Sobald das Raspberry Pi mit Strom versorgt wird bootet es.

Am Ende des Bootvorgangs sollte ein Anmeldeaufforderung zu sehen sein. Der
Benutzername ist ``pi`` und das Password ist ``raspberry``.


Brick Daemon installieren
-------------------------

Wie der Brick Daemon installiert werden kann hängt von der verwendeten Debian
Variante ab.

Raspbian (armhf)
^^^^^^^^^^^^^^^^

Wurde Debian **mit** Hardware Floating Point Unit Unterstützung (Raspbian)
installiert, so kann der :ref:`Brick Daemon <brickd>` einfach mit folgenden
Befehlen installiert werden (falls ``libudev1`` nicht verfügbar ist ``libudev0``
installieren)::

 sudo apt-get install libusb-1.0-0 libudev1 procps
 wget --backups=1 https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

Der Brick Daemon wird nach der Installation und beim Hochfahren des Systems
automatisch gestartet.

Updates können durch Wiederholen der letzten beiden Befehle installiert werden::

 wget --backups=1 https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb


Soft-Float Debian (armel)
^^^^^^^^^^^^^^^^^^^^^^^^^

Wurde Debian **ohne** Hardware Floating Point Unit Unterstützung installiert,
so muss der :ref:`Brick Daemon <brickd>` selbst kompiliert werden.

Als erstes muss der Quelltext von der :ref:`Download Seite <downloads_tools>`
heruntergeladen werden und im ``home`` Verzeichnis platziert werden.

Danach müssen folgende Schritte ausgeführt werden::

 sudo apt-get install build-essential pkg-config libusb-1.0-0-dev libudev-dev procps
 unzip Tinkerforge-brickd-vX.Y.Z-W-***.zip (Dateiname anpassen)
 cd Tinkerforge-brickd-vX.Y.Z-W-*** (Ordnername anpassen)
 cd src/brickd
 make
 sudo make install
 sudo update-rc.d brickd defaults
 sudo /etc/init.d/brickd start


Brick Viewer installieren
-------------------------

Der :ref:`Brick Viewer <brickv>` kann mit folgenden Befehlen installiert werden::

 sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtopengl python3-serial python3-tz python3-tzlocal
 wget --backups=1 https://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb

Es kann vorkommen, dass ``apt-get`` meldet, dass bestimmte Abhängigkeiten nicht
installiert werden. Wenn dies passiert schlägt ``apt-get`` vor
``sudo apt-get -f install`` auszuführen. Dies sollte das Problem beheben und
die benötigten Abhängigkeiten installieren.

Updates können durch Wiederholen der letzten beiden Befehle installiert werden::

 wget --backups=1 https://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb


Zugriff von Außen
-----------------

Das Raspberry Pi kann dazu verwendet werden dort den Brick Daemon laufen zu
lassen und angeschlossene Bricks dann von Außen zu steuern, z.B. über ein
Smartphone.

Um dies zu tun musst der Host zu dem die IP Connection hergestellt wird von
"localhost" auf die IP Adresse des Raspberry Pis geändert werden.


Bekannte Probleme
-----------------

Der USB Anschluss des Raspberry Pis ist möglicherweise nicht in der Lage einen
großen Stapel von Bricks und Bricklets mit Strom zu versorgen. In diesem Fall
sollte eine :ref:`Step-Down Power Supply <step_down_power_supply>`
verwendet werden um den Stapel zu versorgen.
