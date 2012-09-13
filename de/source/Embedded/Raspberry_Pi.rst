.. _embedded_raspberry_pi:

Raspberry Pi
============

Hier wird beschrieben wie Bricks und Bricklets zusammen mit einem
`Raspberry Pi <http://www.raspberrypi.org/>`__ und Debian genutzt werden können.


SD Karte vorbereiten
--------------------

Als erstes musst du Debian auf eine SD Karte bringen. Dazu lädst du das neuste
Debian Image von `hier <http://www.raspberrypi.org/downloads>`__ herunter und
folgst den Schritten `dieser <http://elinux.org/RPi_Easy_SD_Card_Setup>`__
Anleitung.


Raspberry Pi starten
--------------------

Schließe eine Tastertur, einen Bildschirm und eine Stromversorgung an dein
Raspberry Pi an. Sobald das Raspberry Pi mit Strom versorgt wird bootet es.

Am Ende des Bootvorgangs solltest du ein Anmeldeaufforderung sehen. Gib als
Benutzername "pi" und als Password "raspberry" ein. Jetzt solltest du angemeldet
sein.


Brick Daemon und Brick Viewer installieren
------------------------------------------

Um den :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer <brickv>` zu
installieren msst du folgende Befehle ausführen::

 cd /home/pi
 sudo apt-get install python-twisted python-gudev libusb-1.0-0
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest.deb
 sudo dpkg -i brickd_linux_latest.deb

 cd /home/pi
 sudo apt-get install python python-qt4 python-qt4-gl python-qwt5-qt4 python-opengl
 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb


Zugriff von Außen
-----------------

Du kannst ein Raspberry Pi dazu verwenden dort den Brick Daemon laufen zu lassen
und angeschlossene Bricks dann von Außen zu steuern, z.B. über dein Smartphone.

Um dies zu tun musst du den Host zu dem du die IP Connection herstellt von
"localhost" auf die IP Adresse des Raspberry Pis ändern.


Bekannte Probleme
-----------------

Der USB Anschluss des Raspberry Pis ist möglicherweise nicht in der Lage einen
großen Stapel von Bricks und Bricklets mit Strom zu versorgen. In diesem Fall
solltest du deine :ref:`Step-Down Power Supply <step_down_power_supply>`
verwenden um den Stapel zu versorgen.
