
.. _embedded_raspberry_pi:

Raspberry Pi
============

Hier wird beschrieben wie Bricks und Bricklets zusammen mit einem
`Raspberry Pi <https://www.raspberrypi.org/>`__ und Debian genutzt werden können.


SD Karte vorbereiten
--------------------

Als erstes musst Raspberry Pi OS auf einer SD Karte eingerichtet werden. Es wird empfohlen dafür
`Raspberry Pi Imager <https://www.raspberrypi.com/software/>`__ zu verwenden.


Raspberry Pi starten
--------------------

Schließe eine Tastatur, einen Bildschirm und eine Stromversorgung an das
Raspberry Pi an. Sobald das Raspberry Pi mit Strom versorgt wird bootet es.

Am Ende des Bootvorgangs sollte ein Anmeldeaufforderung zu sehen sein. Dort
mit dem Benutzernamen und Passwort anmelden, die zuvor in Raspberry Pi Imager
vergeben wurden.


Brick Daemon installieren
-------------------------

Dazu der Brick Daemon :ref:`Installationsanleitung <brickd_install_linux>` folgen.


Brick Viewer installieren
-------------------------

Dazu der Brick Viewer :ref:`Installationsanleitung <brickv_install_linux>` folgen.


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
