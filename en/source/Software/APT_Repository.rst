
.. _apt_repository:

APT Repository
==============

The software available in the :ref:`download section <downloads>` is also available
for installation as Debian packages in our `APT repository <https://download.tinkerforge.com/apt/>`__.

Currently, theses distributions and architectures are supported:

* Debian: amd64, i386, armhf
* Ubuntu: amd64, i386, armhf
* Raspberry Pi OS (previously called Raspbian): armhf

Setup
-----

Before executing the command lines below, make sure to replace the placeholder
``DISTRIBUTION`` in the command line with either ``debian``, ``ubuntu`` or ``raspios``
according to the distribution in use.

**Step 1:** Import public GPG key::

 curl -s https://download.tinkerforge.com/apt/DISTRIBUTION/archive.key | sudo apt-key add -

**Step 2:** Add APT repository::

 sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/DISTRIBUTION $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"

**Step 3:** Update APT package list::

 sudo apt update

The setup is complete.
