.. _brickd:

Brick Daemon (brickd)
=====================

The Brick Daemon is a daemon (or service on Windows) that acts as a bridge 
between the :ref:`Bricks <product_overview_bricks>`/
:ref:`Bricklets <product_overview_bricklets>`
and the programming language 
:ref:`API bindings <api_bindings>`.

The daemon routes data between the USB connections and TCP sockets.
When using the API bindings a TCP connection to the daemon is established.
This concepts allows the creation of bindings for almost every language
wihtout any dependencies. Therefore it is possible to program Bricks and
Bricklets from embedded devices that only support specific languages,
such as smart phones.

Additionally it is possible to seperate the machine running the Brick Daemon
from the machine running the user code. This allows e.g. a Brick connected
to a PC to be controlled from a smart phone or over the internet from
another PC.

.. _brickd_installation:

Installation
------------

Windows
^^^^^^^

Linux
^^^^^

Mac OS
^^^^^^


Usage
-----




