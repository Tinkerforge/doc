.. _brickd:

Brick Daemon (brickd)
=====================

The Brick Daemon is a daemon (or service on Windows) that acts as a bridge
between the :ref:`Bricks <product_overview_bricks>`/:ref:`Bricklets
<product_overview_bricklets>` and the :ref:`API bindings <api_bindings>` for
the different programming languages.

The daemon routes data between the USB connections and TCP/IP sockets.
When using the API bindings a TCP/IP connection to the daemon is established.
This concepts allows the creation of bindings for almost every language
without any dependencies. Therefore it is possible to program Bricks and
Bricklets from embedded devices that only support specific languages,
such as smart phones.

Additionally it is possible to separate the machine running the Brick Daemon
from the machine running the user code. This allows e.g. a Brick connected
to a PC to be controlled from a smart phone or over the Internet from
another PC.

.. _brickd_installation:

Installation
------------

Windows
^^^^^^^

To install the Brick Deamon (Service) on a Windows, download the
Brick Deamon .exe form :ref:`here <downloads_tools>`.
Click on the downloaded file, this should open the installer:

.. image:: /Images/Screenshots/brickd_windows_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_1.jpg

You can choose the actions of the installer:

* **Install Brickd Program** will copy the program files
* **Register Brickd Service** will install it as a Windows service

Typically you want the installer to perform both tasks.
Click on "Next" to start the installation process.

.. image:: /Images/Screenshots/brickd_windows_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_2.jpg

Next the installation path will be questioned.
Change it if necessary and click "Install".

At the end of the installation process a window will come
up which informs you, that you may have to install the
Brick drivers manually (see section below). Press "OK"
and reboot your PC.


Driver Installation (Windows XP, Vista, 7)
""""""""""""""""""""""""""""""""""""""""""

Depending on your Windows version it is necessary
to install a Brick driver. This driver needs to be installed for each of your
Bricks independently.

Connect your Brick over USB to your PC. If a driver installation
is necessary you should see an window like below:

.. image:: /Images/Screenshots/brickd_windows_driver_1_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_1.jpg

If you have not installed the driver before,
Windows does not know our drivers and you have to specify the
driver location. You can find the drivers in your Brick Daemon installation
folder. If you have installed the drivers before, you can choose the
"Install the software automatically" option since Windows already knows
the driver location.

.. image:: /Images/Screenshots/brickd_windows_driver_2_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_2.jpg

Choose the driver location manually.

.. image:: /Images/Screenshots/brickd_windows_driver_3_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_3.jpg

You will find them in your Brickd program folder in the "drivers" folder.

.. image:: /Images/Screenshots/brickd_windows_driver_4_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 4
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_4.jpg

After a successful installation the Brick should use a driver called "Brick_Driver".
You can test the Brick by using the :ref:`Brick Viewer<brickv>`.

.. note::
 Under Windows 7 it is possible that Windows tries to install the
 drivers automatically and you don't have the choice to choose them manually.
 This automatic driver installation can fail without
 your notice. If you don't see Bricks in the Brick Viewer, please check in
 the Windows "Device Manager" that the drivers for the connected Bricks are
 installed correctly. If not, please choose the ``drivers`` folder in Brick
 Daemon installation and install the drivers manually.


Driver Installation (Windows 8)
"""""""""""""""""""""""""""""""

On Windows 8 no driver is needed anymore. Windows 8 recognizes
the hardware automatically and correctly.

Linux
^^^^^

Um den Brick Daemon auf einer Debian basierten Distribution 
(Ubuntu, Mint, etc.) zu installieren, muss das Brick Daemon .deb von
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

In Ubuntu kann auch das Ubuntu Software Center benutzt werden. Andere
Desktopumgebungen haben ähnliche Werkzeuge die praktisch genauso
funktionieren.

Der Brick Daemon kann von der Console mit folgemdem Befehl installiert
werden::

 sudo apt-get install python-twisted python-gudev libusb-1.0-0
 sudo dpkg -i brickd_linux_latest.deb

Um den Brick Daemon aus den Sourcen zu installieren, kann der
`Quellcode von github <https://github.com/Tinkerforge/brickd>`__ heruntergeladen werden.
Es gibt folgende Abhängigkeiten:

* libusb-1.0-0-dev >= 1.0.8
* libudev-dev >= 173 (Optional für Hotplug)

Auf Debian basierten Distributionen können die Abhängigkeiten mit apt-get
installiert werden::

 sudo apt-get install libusb-1.0-0-dev libudev-dev

Auf anderen Distributionen muss nach den äquivakten Paketen gesucht werden.

Der Brick Daemon kann mit den folgenden Befehlen aus brickd/src/brickd/ 
compiliert und gestartet werden::

 make
 sudo ./brickd

Error Logs gibt es unter::

 /var/log/brickd.log

Wenn der Brick Daemon aus dem Paket installiert wird, wird er automatisch
bei jedem neustart beim Hochfahren gestartet.

Mac OS X
^^^^^^^^

Um den Brick Daemon auf Mac OS X zu installieren, muss die .dmg
von der :ref:`Download-Seite <downloads_tools>` heruntergeladen werden.
Ein Klick auf die Datei sollte das Paket öffnen:

.. image:: /Images/Screenshots/brickd_macos_1_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickd_macos_1.jpg

Danach muss auf "INSTALL" geklickt werden, es sollte ein
Passwort-Abfrage geöffnet werden. Es werden Root-Rechte
benötigt um den Brick Daemon als Launchd Daemon zu
installieren.

.. image:: /Images/Screenshots/brickd_macos_2_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickd_macos_2.jpg

Danach sollte ein "Installation Finished" Fenster erscheinen.

.. image:: /Images/Screenshots/brickd_macos_3_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 3
   :align: center
   :target: ../_images/Screenshots/brickd_macos_3.jpg

Nach einem Klick auf "OK" ist die Installation beended. Der Brick Daemon
sollte nun bei jedem Neustart beim Hochfahren gestartet werden.

Falls der Brick Daemon nicht laufen sollte oder er abgestürzt ist, kann er
aus der Console mit folgendem Befehl gestartet werden::

 sudo launchctl start com.tinkerforge.brickd

.. note::
 Seit Mac OS X Mountain Lion kann ausschließlich signierte Sofware installiert
 werden. Der Brick Daemon Installer ist im Moment nicht signiert. Daher kann
 es passieren, dass Mac OS X eine Fehlermeldung gibt beim versuch den Installer
 zu starten. Als Ausweg können die Sicherheitseinstellungen abgeschwächt 
 werden, unter:

 * System Settings
 * Security & Privacy
 * Allow applications downloaded from: Anywhere


Installierte Version herausfinden
---------------------------------

Seit Brick Daemon Version 1.0.8 ist es möglich die aktuell installierte
Brick Daemon Version zu erfragen. Dafür unterstützt der Brick Daemon
den Kommandozeilenparameter `--version`:

* Windows:

  .. code-block:: none

    "C:\Program Files\Tinkerforge\Brickd\brickd_windows.exe" --version

* Linux::

   brickd --version

* Mac OS X::

   /usr/libexec/brickd.app/Contents/MacOS/brickd_macosx --version
