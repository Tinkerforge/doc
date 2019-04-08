
.. _brickv_install_windows:

Brick Viewer Installation auf Windows
=====================================

**Voraussetzungen**: Windows 7 oder neuer

Der :ref:`Brick Viewer <brickv>` kann mittels einer Setup ``.exe`` Datei
installiert werden.


Installer
---------

Als erstes muss die Brick Viewer Installer ``.exe`` :ref:`heruntergeladen
<downloads_tools>` werden. Ein Doppelklick auf die heruntergeladene Datei
sollte einen Installer starten:

.. image:: /Images/Screenshots/brickv_windows_1.jpg
   :scale: 100 %
   :alt: Brickv Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickv_windows_1.jpg

Verschiedene Aktionen können ausgewählt werden:

* **Install Brick Daemon** kopiert die Programmdateien.
* **Install/Update Brick Bootloader Driver** installiert/aktualisiert den USB
  Treiber für Bricks im Bootloader Modus. Dieser Treiber ist notwendig um
  Brick Firmware Updates in Brick Viewer durchführen zu können.

Typischerweise sollen alle Schritte ausgeführt werden. Ein Klick auf
"Next" startet den Installationsprozess.

.. image:: /Images/Screenshots/brickv_windows_2.jpg
   :scale: 100 %
   :alt: Brickv Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickv_windows_2.jpg

Als nächstes wird der Installationspfad abgefragt. Dieser kann
abgeändert werden wenn gewünscht.
Dabei dürfen allerdings nur ASCII Zeichen verwendet werden, insbesondere können
keine Umlaute verwendet werden.
Brick Viewer kann, bedingt durch einen Bug im Python ``pywintypes`` Modul,
nicht gestartet werden, wenn er in einem Pfad mit nicht-ASCII Zeichen
installiert wurde.

Die Installation wird mit einem Klick auf "Install" gestartet.
