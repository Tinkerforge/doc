
.. _apt_repository:

APT Repository
==============

The software available in the :ref:`download section <downloads>` is also available
for installation as Debian packages in our `APT repository <https://download.tinkerforge.com/apt/>`__.

Currently, these distributions and architectures are supported:

* `Debian <https://www.debian.org>`__: amd64, i386, armhf, arm64
* `Ubuntu <https://ubuntu.com>`__: amd64, i386, armhf, arm64
* `Raspberry Pi OS <https://www.raspberrypi.org/downloads/raspberry-pi-os/>`__ (previously Raspbian): armhf, arm64

.. _apt_repository_setup:

Setup
-----

**Step 1:** Import public GPG key::

 wget https://download.tinkerforge.com/apt/$(. /etc/os-release; echo $ID)/tinkerforge.gpg -q -O - | sudo tee /etc/apt/trusted.gpg.d/tinkerforge.gpg > /dev/null

**Step 2:** Add APT repository::

 echo "deb https://download.tinkerforge.com/apt/$(. /etc/os-release; echo $ID $VERSION_CODENAME) main" | sudo tee /etc/apt/sources.list.d/tinkerforge.list

**Step 3:** Update APT package list::

 sudo apt update

.. _apt_repository_packages:

Packages
--------

Currently, these packages are available:

* Tools

  * :ref:`Brick Daemon <brickd>`: ``brickd``
  * :ref:`Brick Viewer <brickv>`: ``brickv``
  * :ref:`Brick Flash <brick_flash>`: ``brick-flash``

* API Bindings

  * :ref:`Go <api_bindings_go>`: ``golang-tinkerforge-dev``
  * :ref:`Java <api_bindings_java>`: ``libtinkerforge-java`` and ``libtinkerforge-java-doc``
  * :ref:`JavaScript (Node.js) <api_bindings_javascript>`: ``node-tinkerforge``
  * JSON: ``tinkerforge-json``
  * :ref:`MQTT <api_bindings_mqtt>`: ``tinkerforge-mqtt``
  * :ref:`Octave <api_bindings_matlab>`: ``octave-tinkerforge``
  * :ref:`Perl <api_bindings_perl>`: ``libtinkerforge-perl``
  * :ref:`PHP <api_bindings_php>`: ``php-tinkerforge``
  * :ref:`Python <api_bindings_python>`: ``python3-tinkerforge`` (Python 3) and ``python-tinkerforge`` (Python 2, last available version is 2.1.30, no new version will be released anymore, due to Python 2 being end-of-life)
  * :ref:`Ruby <api_bindings_perl>`: ``ruby-tinkerforge``
  * :ref:`Shell <api_bindings_shell>`: ``tinkerforge-shell``
