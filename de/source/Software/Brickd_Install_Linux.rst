
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="Brickd.html">Brick Daemon (brickd)</a> / Brick Daemon Installation auf Linux

.. _brickd_install_linux:

Brick Daemon Installation auf Linux
===================================

Der :ref:`Brick Daemon <brickd>` kann auf einer Debian basierten Distribution
(Ubuntu, Mint, etc.) aus einer ``.deb`` Datei installiert werden. Auf anderen
Distributionen kann er aus dem Quelltext installiert werden.


Debian Package
--------------

Als erstes muss das Brick Daemon ``.deb`` von
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

Der Brick Daemon kann von der Console mit folgendem Befehl installiert
werden::

 # Use libudev1 instead of libudev0 in Ubuntu 13.04
 sudo apt-get install libusb-1.0-0 libudev0 pm-utils

 # On ARM (e.g. Raspberry Pi)
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

 # On 64bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
 sudo dpkg -i brickd_linux_latest_amd64.deb

 # On 32bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_i386.deb
 sudo dpkg -i brickd_linux_latest_i386.deb

Der Brick Daemon wird nach der Installation und beim Hochfahren des Systems
automatisch gestartet.


Aus Quelltext
-------------

Um den Brick Daemon aus dem Quelltext zu installieren, muss
der `Quellcode von GitHub <https://github.com/Tinkerforge/brickd>`__
geclont/heruntergeladen werden::

 git clone https://github.com/Tinkerforge/brickd

Brick Daemon benutzt die Tinkerforge daemonlib. Deren `Quellcode von GitHub
<https://github.com/Tinkerforge/daemonlib>`__ muss in den ``src/`` Ordner des
brickd Clones geclont/heruntergeladen werden::

 cd src/
 git clone https://github.com/Tinkerforge/daemonlib

Es müssen folgende Abhängigkeiten installiert werden:

* libusb-1.0
* libudev (optional für USB Hotplug)
* pm-utils (optional für Suspend/Resume Behandlung)

Auf Debian basierten Distributionen können die Abhängigkeiten mit apt-get
installiert werden::

 sudo apt-get install build-essential pkg-config libusb-1.0-0-dev libudev-dev pm-utils

Auf Fedora können die Abhängigkeiten mit yum installiert werden::

 sudo yum groupinstall "Development Tools"
 sudo yum install libusb1-devel libudev-devel pm-utils-devel

Auf anderen Distributionen muss nach den äquivalenten Paketen gesucht werden.

Der Brick Daemon kann mit den folgenden Befehlen compiliert und installiert
werden::

 cd src/brickd/
 make
 sudo make install

Die folgenden Befehle registrieren brickd für Autostart auf Debian basierten
Distributionen und starten brickd::

 sudo update-rc.d brickd defaults
 sudo /etc/init.d/brickd start
