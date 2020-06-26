
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

* Tools

  * :ref:`Brick Daemon <brickd>`: ``brickd``
  * :ref:`Brick Viewer <brickv>`: ``brickv``

* API Bindings

  * :ref:`Go <api_bindings_go>`: ``golang-tinkerforge-dev``
  * :ref:`Java <api_bindings_java>`: ``libtinkerforge-java`` und ``libtinkerforge-java-doc``
  * :ref:`JavaScript (Node.js) <api_bindings_javascript>`: ``node-tinkerforge``
  * JSON: ``tinkerforge-json``
  * :ref:`Octave <api_bindings_matlab>`: ``octave-tinkerforge``
  * :ref:`Perl <api_bindings_perl>`: ``libtinkerforge-perl``
  * :ref:`PHP <api_bindings_php>`: ``php-tinkerforge``
  * :ref:`Python <api_bindings_python>`: ``python3-tinkerforge`` (Python 3) und ``python-tinkerforge`` (Python 2)
  * :ref:`Ruby <api_bindings_perl>`: ``ruby-tinkerforge``
  * :ref:`Shell <api_bindings_shell>`: ``tinkerforge-shell``
