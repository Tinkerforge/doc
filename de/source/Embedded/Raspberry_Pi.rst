.. _embedded_raspberry_pi:

Raspberry Pi
============

Hier wird beschrieben wie Bricks und Bricklets zusammen mit einem
`Raspberry Pi <http://www.raspberrypi.org/>`__ und Debian genutzt werden können.


SD Karte vorbereiten
--------------------

Als erstes musst Debian auf einer SD Karte eingerichtet werden. Hier gibt es 
zwei verschiedene Versionen für das Raspberry Pi: Einmal "Raspbian" (armhf)
und "Soft-Float Debian" (armel). Raspbian nutzt die Hardware Floating Point
Unit von dem Board und wird empfohlen zu benutzen.

Dazu muss zuerst
das neuste Raspbian Image von `hier <http://www.raspberrypi.org/downloads>`__
heruntergeladen werden. Diese `Anleitung <http://elinux.org/RPi_Easy_SD_Card_Setup>`__
erklärt dann alles weitere.


Raspberry Pi starten
--------------------

Schließe eine Tastatur, einen Bildschirm und eine Stromversorgung an das
Raspberry Pi an. Sobald das Raspberry Pi mit Strom versorgt wird bootet es.

Am Ende des Bootvorgangs sollte ein Anmeldeaufforderung zu sehen sein. Der
Benutzername ist "pi" und das Password ist "raspberry".


Brick Daemon und Brick Viewer installieren
------------------------------------------

Der :ref:`Brick Viewer <brickv>` kann mit
folgenden Befehlen installiert werden::

 cd /home/pi
 sudo apt-get install python python-qt4 python-qt4-gl python-qwt5-qt4 python-opengl
 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb


Option 1: Wurde Debian **mit** Hardware Floating Point Unit Unterstützung (Raspbian) installiert,
so kann der :ref:`Brick Daemon <brickd>` einfach mit folgenden Befehlen installiert werden::

 cd /home/pi
 sudo apt-get install python-twisted python-gudev libusb-1.0-0
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

Option 2: Wurde Debian **ohne** Hardware Floating Point Unit Unterstützung installiert,
so muss der :ref:`Brick Daemon <brickd>` selbst kompiliert werden.

Als erstes muss der Quelltext von der 
`Download Seite <http://www.tinkerforge.com/en/doc/Downloads.html#tools>`__
heruntergeladen werden und im home Verzeichnis platziert werden.

Danach müssen folgende Schritte ausgeführt werden::

 sudo apt-get install build-essential libusb-1.0-0-dev libudev-dev
 cd /home/pi
 unzip Tinkerforge-brickd-vX.X.X-X-***.zip (Dateiname anpassen)
 cd Tinkerforge-brickd-vX.X.X-X-*** (Ordnername anpassen)
 cd src/brickd
 make
 sudo make install

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
