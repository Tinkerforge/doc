
.. _apt_repository:

APT Repository
==============

The software available in the :ref:`download section <downloads>` is also available
for installation as Debian packages in our `APT repository <https://download.tinkerforge.com/apt/>`__.

Currently, these distributions and architectures are supported:

* `Debian <https://www.debian.org>`__: amd64, i386, armhf
* `Ubuntu <https://ubuntu.com>`__: amd64, i386, armhf
* `Raspberry Pi OS <https://www.raspberrypi.org/downloads/raspberry-pi-os/>`__ (previously Raspbian): armhf

Setup
-----

**Step 1:** Import public GPG key::

 curl -s https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z])/archive.key | sudo apt-key add -

**Step 2:** Add APT repository::

 sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z]) $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"

**Step 3:** Update APT package list::

 sudo apt update

Packages
--------

Currently, these packages are available:

* :ref:`Brick Daemon <brickd>`: ``brickd``
* :ref:`Brick Viewer <brickv>`: ``brickv``
