
.. _brickd_install_linux:

Brick Daemon Installation auf Linux
===================================

**Voraussetzungen**: libusb 1.0.6 oder neuer

Der :ref:`Brick Daemon <brickd>` kann auf einer Debian basierten Distribution
(Ubuntu, Mint, etc.) aus einer ``.deb`` Datei installiert werden. Für Arch Linux
steht im AUR das Paket `brickd <https://aur.archlinux.org/packages/brickd/>`_ zur Verfügung.
Auf anderen Distributionen kann der Brick Daemon aus dem Quelltext installiert werden.

Debian Paket
------------

Das Brick Daemon Debian Paket steht in unserem `APT Repository
<https://download.tinkerforge.com/apt/>`__ bereit, kann aber auch händisch
installiert werden.

APT Repository
^^^^^^^^^^^^^^

Zuerst entsprechend der :ref:`Anleitung <apt_repository>` das APT Repository
hinzufügen. Dann das Brick Daemon Paket installieren::

 sudo apt install brickd

Der Brick Daemon wird nach der Installation und beim Hochfahren des Systems
automatisch gestartet.


Händische Installation
^^^^^^^^^^^^^^^^^^^^^^

Als erstes muss das passende Brick Daemon ``.deb`` von
der :ref:`Download-Seite <downloads_tools>` heruntergeladen werden.
Nach einem Rechtsklick auf die Datei kann "Open with GDebi Package Installer"
ausgewählt werden:

.. image:: /Images/Screenshots/brickd_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_linux_1.jpg

Klick auf "Install Package":

.. image:: /Images/Screenshots/brickd_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_linux_2.jpg

Fertig:

.. image:: /Images/Screenshots/brickd_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_linux_3.jpg

Auf Ubuntu kann auch das Ubuntu Software Center benutzt werden. Andere
Desktopumgebungen haben ähnliche Werkzeuge die praktisch genauso
funktionieren.

Der Brick Daemon kann von der Konsole mit folgendem Befehl installiert
werden::

 # Use libudev1 instead of libudev0 in Ubuntu 13.04
 sudo apt-get install libusb-1.0-0 libudev0 pm-utils

 # On ARM (e.g. Raspberry Pi)
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

 # On 64bit x86
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
 sudo dpkg -i brickd_linux_latest_amd64.deb

 # On 32bit x86
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_i386.deb
 sudo dpkg -i brickd_linux_latest_i386.deb

 # On RED Brick
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest+redbrick_armhf.deb
 sudo dpkg -i brickd_linux_latest+redbrick_armhf.deb

Der Brick Daemon wird nach der Installation und beim Hochfahren des Systems
automatisch gestartet.


Aus Quelltext
-------------

In dieser `README <https://github.com/Tinkerforge/brickd/blob/master/README.rst>`__
sind die nötigen Schritte beschrieben, um den Brick Daemon aus dem Quelltext zu
installieren.
