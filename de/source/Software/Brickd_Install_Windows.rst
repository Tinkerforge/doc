
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="Brickd.html">Brick Daemon (brickd)</a> / Brick Daemon Installation auf Windows

.. _brickd_install_windows:

Brick Daemon Installation auf Windows
=====================================

Der :ref:`Brick Daemon <brickd>` kann mittels einer Setup ``.exe`` Datei
installiert werden.


Installer
---------

Als erstes muss die Brick Daemon ``.exe`` :ref:`heruntergeladen <downloads_tools>`
werden. Ein Doppelklick auf die heruntergeladene Datei sollte einen Installer
starten:

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
Installation muss der PC neu gestartet werden.


.. _brickd_install_windows_driver:

Treiber Installation (Windows XP, Vista, 7)
-------------------------------------------

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
"Brick_Driver" nutzen. Dies kann mit dem :ref:`Brick Viewer <brickv>` getestet
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
--------------------------------

Unter Windows 8 wird kein Treiber mehr benötigt, Windows 8 erkennt die
Hardware automatisch und korrekt.
