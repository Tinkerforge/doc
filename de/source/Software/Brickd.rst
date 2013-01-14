.. _brickd:

Brick Daemon (brickd)
=====================

Der Brick Daemon ist ein Daemon (bzw. Service für Windows) der als eine Brücke
zwischen :ref:`Bricks <product_overview_bricks>`/:ref:`Bricklets
<product_overview_bricklets>` und den :ref:`API Bindings <api_bindings>` für die
verschiedenen Programmiersprachen fungiert.

Der Daemon leitet Daten zwischen der USB Verbindung und den TCP/IP Sockets
hin und her. Bei der Benutzung der API Bindings wird eine TCP/IP Verbindung
zum Brick Daemon hergestellt. Dieses Konzept erlaubt es Bindings für
nahezu jede Programmiersprache ohne Abhängigkeiten zu erstellen. Dadurch ist
es möglich Bricks und Bricklets über eingebettete Geräte wie Smartphones
zu programmieren, die nur spezifische Programmiersprachen unterstützten.

Zusätzlich ist es möglich den PC auf dem der Brick Daemon läuft von dem
PC auf dem der Benutzercode läuft zu trennen. Dadurch ist das Steuern über ein
Smartphone oder auch über das Internet möglich.


.. _brickd_installation:

Installation
------------

Windows
^^^^^^^

Um den Brick Daemon (Service) auf Windows zu installieren, muss
die Brick Daemon .exe  ref:`heruntergeladen <downloads_tools>`
werden. Ein Doppelklick auf die Heruntergeladene Datei
sollte einen Installer starten:

.. image:: /Images/Screenshots/brickd_windows_1_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_1.jpg

Zwei Aktionen können ausgewählt werden:

* **Install Brickd Program** kopiert die Programm-Dateien
* **Register Brickd Service** installiert den Daemon als Windows Service

Typischerweise soll beides ausgeführt werden. Ein Klick auf
"Next" startet den Installationsprozess.

.. image:: /Images/Screenshots/brickd_windows_2_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_2.jpg

Als nächstes wird der Installationspfad abgefragt. Dieser kann
abgeändert werden wenn gewünscht. Die Installtion wird mit
einem Klick auf "Install" gestartet.

Am Ende des Installationsprozess erscheint ein Fenster,
welches darüber informiert dass der Brick Treiber
noch installiert werden muss (siehe unten). Nach der
Installation muss der PC neugestartet werden.


Treiber Installation (Windows XP, Vista, 7)
"""""""""""""""""""""""""""""""""""""""""""

Abhängig von der Windows Version ist es nötig einen Brick Treiber zu 
installieren. Dieser Treiber muss für jedes Brick einmal installiert
werden.

Wenn eine Treiberinstallation notwendig ist, sollte folgendes
Fenster erscheinen nachdem der Brick über USB mit dem PC verbunden
wird:

.. image:: /Images/Screenshots/brickd_windows_driver_1_small.jpg
   :scale: 100 %
   :alt: Brickd Treiber Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_1.jpg


Falls der Treiber zuvor noch nie installiert wurde kennt Windows
diesen noch nicht. In diesem Fall muss die Treiberadresse
angegeben werden. Der Treiber befindet sich im Installationsverzeichnis
des Brick Daemon. Wenn der Treiber zuvor schon einmal installiert
wurde, kann "Install the software automatically" ausgewählt werden.

.. image:: /Images/Screenshots/brickd_windows_driver_2_small.jpg
   :scale: 100 %
   :alt: Brickd Treiber Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_2.jpg

Treiberadresse Manuell auswählen.

.. image:: /Images/Screenshots/brickd_windows_driver_3_small.jpg
   :scale: 100 %
   :alt: Brickd Treiber Installation Schritt 3
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_3.jpg

Sie befinden sich beim Brickd im Verzeichnis "drivers".

.. image:: /Images/Screenshots/brickd_windows_driver_4_small.jpg
   :scale: 100 %
   :alt: Brickd Treiber Installation Schritt 4
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_4.jpg

Nach einer erfolgreichen Installation sollte der Brick en Treiber
"Brick_Driver" nutzen. Dies kann mit dem :ref:`Brick Viewer<brickv>` getestet
werden.

.. note::
 Unter Windows 7 ist es möglich, dass Windows versucht den Treiber automatisch
 zu installieren und eine Auswahl zur manuellen Installation gar nicht
 erscheint. Das automatische Installieren des Treibers kann ohne Meldung
 fehlschlagen. Falls im Brick Viewer kein Brick angezeigt wird, kann im
 Gerätemanager nachgeschaut werden ob der korrekte Treiber installiert ist.
 Falls dies nicht der Fall ist, kann dort der falsche Treiber mit dem
 richtigen aus dem ``drivers`` Verzeichnis vom Brickd manuell überschrieben
 werden.


Treiber Installation (Windows 8)
""""""""""""""""""""""""""""""""

Unter Windows 8 wird kein Treiber mehr benötigt, Windows 8 erkennt die
Hardware automatisch und korrekt.


Linux
^^^^^

To install the Brick Daemon on a Debian based distribution
(Ubuntu, Mint, etc.), download the Brick Daemon .deb from
:ref:`here <downloads_tools>`. Right-click on the file and choose
"Open with GDebi Package Installer":

.. image:: /Images/Screenshots/brickd_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_linux_1.jpg

Then click "Install Package":

.. image:: /Images/Screenshots/brickd_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_linux_2.jpg

Ready:

.. image:: /Images/Screenshots/brickd_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_linux_3.jpg

In Ubuntu you can also use the Ubuntu Software Center, other Desktop
environments have very similar tools that practically work the same way.

To install Brick Daemon from the console use the following::

 sudo apt-get install python-twisted python-gudev libusb-1.0-0
 sudo dpkg -i brickd_linux_latest.deb

To install Brick Daemon from source, download the source from `here
<https://github.com/Tinkerforge/brickd>`__ and install the dependencies:

* libusb-1.0-0-dev >= 1.0.8
* libudev-dev >= 173 (Optional für Hotplug)

On Debian based distributions you can install the dependencies with apt-get::

 sudo apt-get install libusb-1.0-0-dev libudev-dev
 
On other distribution you have to search for and install the equivalent packages.

To compile and brickd from source, change to the folder
brickd/src/brickd/ and do::

 make
 sudo ./brickd

Error logs can be found in::

 /var/log/brickd.log

If you install the Debian package, brickd will be started after the
installation and at startup automatically.


Mac OS X
^^^^^^^^

To install the Brick Daemon on Mac OS X download the .dmg
from :ref:`here <downloads_tools>`. Click on the downloaded file, this
should open the package:

.. image:: /Images/Screenshots/brickd_macos_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_macos_1.jpg

Then click "INSTALL", this should open a password prompt.
Root access is needed to add the Brick Daemon
to your Launchd Daemons.

.. image:: /Images/Screenshots/brickd_macos_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_macos_2.jpg

After this an "Installation Finished" window should come up.
Click "OK".

.. image:: /Images/Screenshots/brickd_macos_3_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_macos_3.jpg

You have finished the installation. The Brick Daemon should be started upon
installation and it should be started automatically after restarts.

If for some reason brickd doesn't run or it has crashed, you can start it
from the terminal with::

 sudo launchctl start com.tinkerforge.brickd

.. note::
 Since Mac OS X Mountain Lion only signed software can be installed by default.
 Currently the Brick Daemon and its installer is not signed. This makes Mac OS X
 show you an error message saying that the installer is broken when you try to
 install it. For now you need to lower your system security settings to allow
 installing unsigned software by clicking:

 * System Settings
 * Security & Privacy
 * Allow applications downloaded from: Anywhere


Checking installed version
--------------------------

Since Brick Daemon version 1.0.8 you can check which Brick Daemon is currently
installed with the `--version` commandline argument:

* Windows:

  .. code-block:: none

    "C:\Program Files\Tinkerforge\Brickd\brickd_windows.exe" --version

* Linux::

   brickd --version

* Mac OS X::

   /usr/libexec/brickd.app/Contents/MacOS/brickd_macosx --version
