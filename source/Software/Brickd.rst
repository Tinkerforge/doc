.. _brickd:

Brick Deamon (brickd)
=====================

Is a deamon or service (Windows term) which acts
as a bridge between the 
:ref:`Bricks <product_overview_bricks>`/
:ref:`Bricklets <product_overview_bricklets>`
and the programming language 
:ref:`API bindings <api_bindings>`.

The deamon routes data between the USB connections and one TCP socket.
When using the API bindings a TCP connection to this socket is established.
This concepts allows it to create language bindings for almost every language.

Additionally it is possible to seperate the machine which running the Brick Deamon
and where the Bricks are connected to and the machine running the user code.
You have simply to change the Host from "localhost" to the name or IP of the
PC running the Brick Deamon in your code.


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




