
.. _brickv_install_linux:

Brick Viewer Installation auf Linux
===================================

Der :ref:`Brick Viewer <brickv>` kann auf einer Debian basierten Distribution
(Ubuntu, Mint, etc.) aus einer ``.deb`` Datei installiert werden. Auf anderen
Distributionen kann er aus dem Quelltext installiert werden.


Debian Package
--------------

Als erstes muss das Brick Viewer ``.deb`` von
der :ref:`Download-Seite <downloads_tools>` heruntergeladen werden.
Durch einen Rechtsklick auf
die Datei und auswählen von "Mit GDebi-Paket-Installationsprogramm öffnen" wird
das Installationsprogramm gestartet:

.. image:: /Images/Screenshots/brickv_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickv Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickv_linux_1.jpg

Ein Klick auf "Paket Installieren" startet dann die eigentliche Installation:

.. image:: /Images/Screenshots/brickv_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickv Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickv_linux_2.jpg

Der Installationsprozess ist nun abgeschlossen:

.. image:: /Images/Screenshots/brickv_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickv Installation Schritt 3
   :align: center
   :target: ../_images/Screenshots/brickv_linux_3.jpg

Auf Ubuntu kann auch das Ubuntu Software Center verwendet werden, andere Debian
basierte Distributionen bieten ähnliche Werkzeuge zur Paketverwaltung.
Der Brick Viewer kann jetzt über das Anwendungsmenü aus der Unterkategorie
Sonstiges gestartet werden, oder aus einem Terminal heraus mit::

 brickv

Statt mittels eines graphischen Installationsprogramms kann der Brick Viewer
auch über einen Terminal mittels folgender Befehle installiert werden::

 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo apt-get install python python-qt4 python-qt4-gl python-opengl python-serial
 sudo dpkg -i brickv_linux_latest.deb


Aus Quelltext
-------------

Um den Brick Viewer aus dem Quelltext heraus zu verwenden kann der Quelltext
ebenfalls im :ref:`Downloadbereich <downloads_tools>` heruntergeladen werden.
Auch hier müssen die benötigten Abhängigkeiten installiert werden:

* python
* python-qt4
* python-qt4-gl
* python-opengl
* python-serial
* pyqt4-dev-tools

Auf Debian basierte Distributionen können diese Pakete wie zuvor per ``apt-get``
installiert werden. Für andere Distributionen sollte es äquivalente Pakete geben::

 sudo apt-get install python python-qt4 python-qt4-gl python-opengl python-serial pyqt4-dev-tools

Als erstes müssen die Qt ``.ui`` Dateien übersetzt werden (dafür wird
``pyuic4`` benötigt). Dazu in den ``src/`` Ordner innerhalb des entpackten
Quelltexts wechseln und dort folgenden Befehl ausführen::

 python build_all_ui.py

Um den Brick Viewer zu starten muss in den ``src/brickv/`` Ordner
gewechselt und dort folgender Befehl ausgeführt werden::

 python main.py
