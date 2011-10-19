.. _api_bindings:

API Bindings
============

API bindings establish a TCP connection to the 
:ref:`Brick Daemon <brickd>`. Each method call creates a TCP package which
is send over the Brick Daemon to the Brick. Incoming TCP packages
are routed back to the calling method.

See also our :ref:`tutorial` for more information how everything works 
together.


IP Connection
-------------

The IPConnection creates a connection between the
:ref:`Brick Daemon <brickd>` and the corresponding programming language 
:ref:`API bindings<api_bindings>`. 

It is used by the bindings and implemented for each programming language:

* :ref:`Python <ipcon_brick_python>`
* :ref:`C/C++ <ipcon_brick_c>`
* :ref:`C# <ipcon_brick_csharp>`
* :ref:`Java <ipcon_brick_java>`

Using the Bindings
------------------


.. _api_bindings_c:
C/C++
^^^^^

MinGW (Windows)
"""""""""""""""

Visual Studio (Windows)
"""""""""""""""""""""""

GCC/G++ (Linux/ MacOS)
""""""""""""""""""""""

.. _api_bindings_csharp:
C#
^^


.. _api_bindings_java:
Java
^^^^


.. _api_bindings_python:
Python
^^^^^^



