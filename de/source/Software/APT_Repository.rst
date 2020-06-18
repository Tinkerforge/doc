
.. _apt_repository:

APT Repository
==============

Die auf der :ref:`Download Seite <downloads>` verfügbare Software steht auch
als Debian Pakete in unserem `APT Repository <https://download.tinkerforge.com/apt/>`__
zur Installation bereit.

Aktuell werden folgende Distributionen und Architekturen unterstützt:

* `Debian <https://www.debian.org>`__: amd64, i386, armhf
* `Ubuntu <https://ubuntu.com>`__: amd64, i386, armhf
* `Raspberry Pi OS <https://www.raspberrypi.org/downloads/raspberry-pi-os/>`__ (ehemals Raspbian): armhf

.. _apt_repository_setup:

Einrichtung
-----------

**Schritt 1:** Öffentlichen GPG Schlüssel importieren::

 curl -s https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z])/archive.key | sudo apt-key add -

**Schritt 2:** APT Repository hinzufügen::

 sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z]) $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"

**Schritt 3:** APT Paketliste aktualisieren::

 sudo apt update

.. _apt_repository_packages:

Pakete
------

Aktuell sind folgende Pakete verfügbar:

* :ref:`Brick Daemon <brickd>`: ``brickd``
* :ref:`Brick Viewer <brickv>`: ``brickv``
* :ref:`Perl API Bindings <api_bindings_perl>`: ``libtinkerforge-perl``
* :ref:`Python API Bindings <api_bindings_python>`: ``python3-tinkerforge`` (Python 3) und ``python-tinkerforge`` (Python 2)
* :ref:`Ruby API Bindings <api_bindings_perl>`: ``ruby-tinkerforge``
