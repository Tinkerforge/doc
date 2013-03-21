
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../Software.html">Software</a> / <a href="Brickv.html">Brick Viewer (brickv)</a> / Brick Viewer Installation auf Linux

.. _brickv_install_linux:

Brick Viewer Installation auf Linux
===================================

Der :ref:`Brick Viewer <brickv>` kann auf einer Debian basierten Distribution
(Ubuntu, Mint, etc.) aus einer ``.deb`` Datei installiert werden. Auf anderen
Distributionon kann er aus dem Quelltext installiert werden.


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

 sudo apt-get install python python-qt4 python-qt4-gl python-qwt5-qt4 python-opengl python-serial
 sudo dpkg -i brickv_linux_latest.deb


Aus Quelltext
-------------

Um den Brick Viewer aus dem Quelltext heraus zu verwenden kann der Quelltext
ebenfalls im :ref:`Downloadbereich <downloads_tools>` heruntergeladen werden.
Auch hier müssen die benötigten Abhängigkeiten installiert werden:

* python
* python-qt4
* python-qt4-gl
* python-qwt5-qt4
* python-opengl
* python-serial

Auf Debian basierte Distributionen können diese Pakete wie zuvor per ``apt-get``
installiert werden. Für andere Distributionen sollte es äquivalente Pakete geben::

 sudo apt-get install python python-qt4 python-qt4-gl python-qwt5-qt4 python-opengl python-serial

Um den Brick Viewer zu starten muss zuerst in den ``src/brickv/`` Ordner
innerhalb des entpackten Quelltext gewechselt und dort folgender Befehl
ausgeführt werden::

 python main.py


python-qwt5-qt4 auf Debian Wheezy
---------------------------------

Unglücklicherweise gibt es bei Debian zum Zeitpunkt des Schreibens dieser
Anleitung ein Problem mit dem ``python-qwt5-qt4`` Paket in Wheezy.
Falls Debian Wheezy verwendet wird und ``python-qwt5-qt4`` ist nicht im
Paket-Repository zu finden, dann kann es aus dem Sid Paket-Repository installiert
werden::

 sudo echo 'APT::Default-Release "testing";' >> /etc/apt/apt.conf

Dann muss ``/etc/apt/sources.list`` bearbeitet und die
nicht-``security testing`` Zeilen kopiert und von ``wheezy`` auf ``sid``
verändert werden. Jetzt kann das Paket wie folgt installiert werden::

 sudo apt-get update
 sudo apt-get -t sid install python-qwt5-qt4
