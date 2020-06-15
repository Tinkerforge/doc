
.. _apt_repository:

APT Repository
==============

Die auf der :ref:`Download Seite <downloads>` verfügbare Software steht auch
als Debian Pakete in unserem `APT Repository <https://download.tinkerforge.com/apt/>`__
zur Installation bereit.

Aktuell werden folgende Distributionen und Architekturen unterstützt:

* Debian: amd64, i386, armhf
* Ubuntu: amd64, i386, armhf
* Raspberry Pi OS (ehemals Raspbian): armhf

Einrichtung
-----------

Bevor die unten aufgeführten Befehle ausgeführt werden, muss der Platzhalter
`DISTRIBUTION` jeweils durch `debian`, `ubuntu` oder `raspios` ersetzen werden,
entsprechend der verwendeten Distribution.

**Schritt 1:** Öffentlichen Schlüssel importieren::

 curl -s https://download.tinkerforge.com/apt/DISTRIBUTION/archive.key | sudo apt-key add -

**Schritt 2:** APT Repository hinzufügen::

 sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/DISTRIBUTION $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"

**Schritt 3:** APT Paketliste aktualisieren::

 sudo apt update

Die Einrichtung ist abgeschlossen.
