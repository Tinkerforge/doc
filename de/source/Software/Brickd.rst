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
die Brick Daemon .exe :ref:`heruntergeladen <downloads_tools>`
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
abgeändert werden wenn gewünscht. Die Installation wird mit
einem Klick auf "Install" gestartet.

Am Ende des Installationsprozess erscheint ein Fenster,
welches darüber informiert dass der Brick Treiber
noch installiert werden muss (siehe unten). Nach der
Installation muss der PC neugestartet werden.


.. _brickd_windows_driver_installation:

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

Der Brick Daemon kann von der Console mit folgendem Befehl installiert
werden:: 

 sudo apt-get install libusb-1.0-0 libudev0

 # On ARM (e.g. Raspberry PI)
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

 # On 64bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
 sudo dpkg -i brickd_linux_latest_amd64.deb

 # On 32bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_i386.deb
 sudo dpkg -i brickd_linux_latest_i386.deb

Um den Brick Daemon aus den Sourcen zu installieren, kann der
`Quellcode von github <https://github.com/Tinkerforge/brickd>`__ heruntergeladen werden.
Es gibt folgende Abhängigkeiten:

* libusb-1.0-0-dev >= 1.0.8
* libudev-dev >= 173 (Optional für Hotplug)

Auf Debian basierten Distributionen können die Abhängigkeiten mit apt-get
installiert werden::

 sudo apt-get install libusb-1.0-0-dev libudev-dev

Auf anderen Distributionen muss nach den äquivalenten Paketen gesucht werden.

Der Brick Daemon kann mit den folgenden Befehlen aus brickd/src/brickd/ 
compiliert und gestartet werden::

 make
 sudo ./brickd

Error Logs gibt es unter::

 /var/log/brickd.log

Wenn der Brick Daemon aus dem Paket installiert wird, wird er automatisch
bei beim Hochfahren des Systems mitgestartet.

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

Nach einem Klick auf "OK" ist die Installation beendet. Der Brick Daemon
sollte nun bei jedem Neustart beim Hochfahren gestartet werden.

Falls der Brick Daemon nicht laufen sollte oder er abgestürzt ist, kann er
aus der Console mit folgendem Befehl gestartet werden::

 sudo launchctl start com.tinkerforge.brickd

.. note::
 Seit Mac OS X Mountain Lion kann ausschließlich signierte Software installiert
 werden. Der Brick Daemon Installer ist im Moment nicht signiert. Daher kann
 es passieren, dass Mac OS X eine Fehlermeldung anzeigt beim Versuch den Installer
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

    "C:\Program Files\Tinkerforge\Brickd\brickd.exe" --version

* Linux::

   brickd --version

* Mac OS X::

   /usr/libexec/brickd.app/Contents/MacOS/brickd --version


Kommandozeilenparameter
-----------------------

Allgemein:

* **--help**: Hilfe anzeigen
* **--version**: Versionsnummer anzeigen
* **--check-config**: Konfigurationsdatei auf Fehler überprüfen
* **--debug**: Alle Log Level auf Debug setzen

Spezifisch für Windows:

* **--install**: Als Service registrieren und starten
* **--uninstall**: Service stoppen und deregistrieren
* **--console**: Start als Konsolenanwendung erzwingen
* **--log-to-file**: Log Nachrichten in Datei schreiben
