
.. _apt_repository:

APT Repository
==============

Die auf der :ref:`Download Seite <downloads>` verfügbare Software steht auch
als Debian Pakete in unserem `APT Repository <https://download.tinkerforge.com/apt/>`__
zur Installation bereit.

Aktuell werden folgende Distributionen und Architekturen unterstützt:

* `Debian <https://www.debian.org>`__: amd64, i386, armhf, arm64
* `Ubuntu <https://ubuntu.com>`__: amd64, i386, armhf, arm64
* `Raspberry Pi OS <https://www.raspberrypi.org/downloads/raspberry-pi-os/>`__ (ehemals Raspbian): armhf, arm64

.. _apt_repository_setup:

Einrichtung
-----------

**Schritt 1:** Öffentlichen GPG Schlüssel importieren::

 wget https://download.tinkerforge.com/apt/$(. /etc/os-release; echo $ID)/tinkerforge.asc -q -O - | sudo tee /etc/apt/trusted.gpg.d/tinkerforge.asc > /dev/null

**Schritt 2:** APT Repository hinzufügen::

 echo "deb https://download.tinkerforge.com/apt/$(. /etc/os-release; echo $ID $VERSION_CODENAME) main" | sudo tee /etc/apt/sources.list.d/tinkerforge.list

**Schritt 3:** APT Paketliste aktualisieren::

 sudo apt update

.. _apt_repository_packages:

Pakete
------

Aktuell sind folgende Pakete verfügbar:

* Tools

  * :ref:`Brick Daemon <brickd>`: ``brickd``
  * :ref:`Brick Viewer <brickv>`: ``brickv``
  * :ref:`Brick Flash <brick_flash>`: ``brick-flash``

* API Bindings

  * :ref:`Go <api_bindings_go>`: ``golang-tinkerforge-dev``
  * :ref:`Java <api_bindings_java>`: ``libtinkerforge-java`` und ``libtinkerforge-java-doc``
  * :ref:`JavaScript (Node.js) <api_bindings_javascript>`: ``node-tinkerforge``
  * JSON: ``tinkerforge-json``
  * :ref:`MQTT <api_bindings_mqtt>`: ``tinkerforge-mqtt``
  * :ref:`Octave <api_bindings_matlab>`: ``octave-tinkerforge``
  * :ref:`Perl <api_bindings_perl>`: ``libtinkerforge-perl``
  * :ref:`PHP <api_bindings_php>`: ``php-tinkerforge``
  * :ref:`Python <api_bindings_python>`: ``python3-tinkerforge`` (Python 3) und ``python-tinkerforge`` (Python 2, letzte verfügbare Version ist 2.1.30, es wird keine neuere Version mehr veröffentlicht, da Python 2 End-of-Life ist)
  * :ref:`Ruby <api_bindings_perl>`: ``ruby-tinkerforge``
  * :ref:`Shell <api_bindings_shell>`: ``tinkerforge-shell``
