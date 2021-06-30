
.. _brickd_install_windows:

Brick Daemon Installation auf Windows
=====================================

**Voraussetzungen**: Windows XP oder neuer

Der :ref:`Brick Daemon <brickd>` kann mittels einer Setup ``.exe`` Datei
installiert werden.


Installer
---------

Als erstes muss die Brick Daemon Installer ``.exe`` :ref:`heruntergeladen
<downloads_tools>` werden. Ein Doppelklick auf die heruntergeladene Datei
sollte einen Installer starten:

.. image:: /Images/Screenshots/brickd_windows_1.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_1.jpg

Verschiedene Aktionen können ausgewählt werden:

* **Install Brick Daemon** kopiert die Programmdateien.
* **Register Brick Daemon as Service** installiert den Daemon als automatisch
  startenden Windows Service. Ohne dies muss der Brick Daemon manuell gestartet
  werden. Manueller Start ist nur für fortgeschrittene Debugging-Zwecke
  sinnvoll.
* **Install/Update Brick Driver** installiert/aktualisiert den USB Treiber für
  Bricks (nur Windows XP, Vista, 7). Dieser Treiber ist notwendig, um über
  USB angeschlossene Bricks nutzen zu können.
* **Install/Update RED Brick Driver** installiert/aktualisiert den USB Treiber
  für RED Bricks (nur Windows XP, Vista, 7). Dieser Treiber ist notwendig, um
  über USB angeschlossene RED Bricks nutzen zu können.
* **Install/Update RED Brick Serial Console Driver** installiert/aktualisiert
  den Treiber für die serielle Konsole von RED Bricks. Dieser Treiber ist
  notwendig, um die serielle Konsole von über USB angeschlossenen RED Bricks
  nutzen zu können.

Typischerweise sollen alle Schritte ausgeführt werden. Ein Klick auf
"Next" startet den Installationsprozess.

.. image:: /Images/Screenshots/brickd_windows_2.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_2.jpg

Als nächstes wird der Installationspfad abgefragt. Dieser kann
abgeändert werden wenn gewünscht. Die Installation wird mit
einem Klick auf "Install" gestartet.


.. _brickd_install_windows_driver:

Manuelle Treiber Installation
-----------------------------

Der Brick Daemon Installer installiert alle nötigen Treiber automatisch, außer
die entsprechenden Schritte wurden manuell abgewählt. Es kann in seltenen
Fällen auch vorkommen, dass die automatische Treiberinstallation durch den
Installer fehlschlägt. In allen diesen Fällen kann es nötig sein den
entsprechenden Treiber manuelle zu installieren.

Windows XP, Vista, 7
^^^^^^^^^^^^^^^^^^^^

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

Sie befinden sich beim Brickd im Verzeichnis ``drivers\brick``.

.. image:: /Images/Screenshots/brickd_windows_driver_4_small.jpg
   :scale: 100 %
   :alt: Brickd Treiber Installation Schritt 4
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_4.jpg

Nach einer erfolgreichen Installation sollte der Brick den Treiber
"Tinkerforge Brick" nutzen. Dies kann mit dem :ref:`Brick Viewer <brickv>`
getestet werden.

.. note::
 Unter Windows 7 ist es möglich, dass Windows versucht den Treiber automatisch
 zu installieren und eine Auswahl zur manuellen Installation gar nicht
 erscheint. Das automatische Installieren des Treibers kann ohne Meldung
 fehlschlagen. Falls im Brick Viewer kein Brick angezeigt wird, kann im
 Gerätemanager nachgeschaut werden ob der korrekte Treiber installiert ist.
 Falls dies nicht der Fall ist, kann dort der falsche Treiber mit dem
 richtigen aus dem ``drivers\brick\win7`` Verzeichnis vom Brickd manuell
 überschrieben werden.


Windows 8, 8.1 und 10
^^^^^^^^^^^^^^^^^^^^^

Ab Windows 8 wird kein Treiber für Bricks mehr benötigt, Windows 8 und neuer
erkennt Bricks automatisch. **Brick Daemon selbst muss dennoch installiert werden.**
