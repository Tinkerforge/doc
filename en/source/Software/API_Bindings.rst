
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / API Bindings

.. _api_bindings:

API Bindings
============

The API bindings establish a TCP/IP connection to the
:ref:`Brick Daemon <brickd>`. Each function call creates a TCP/IP packet that
is send over the Brick Daemon to the Brick. Incoming packets from the Brick
are routed back to the caller.

See also our :ref:`tutorial <tutorial_first_steps>` for more information on how
everything works together.

.. _api_bindings_ip_connection:

IP Connection
-------------

The IP Connection creates a TCP/IP connection between the
:ref:`Brick Daemon <brickd>` and the corresponding programming language
API bindings.

It is used by the bindings and implemented for each programming language.
The corresponding documentation can be found here:

.. include:: API_Bindings_bindings.table


Using the Bindings
------------------

The latest versions of the bindings can be found on the
:ref:`download page <downloads_bindings_examples>`.

Installation and usage instructions for each programming languages:

* :ref:`C/C++ <api_bindings_c>`
* :ref:`C/C++ (iOS) <api_bindings_c_ios>`
* :ref:`C# <api_bindings_csharp>`
* :ref:`C# (Windows Phone) <api_bindings_csharp_windows_phone>`
* :ref:`Delphi <api_bindings_delphi>`
* :ref:`Java <api_bindings_java>`
* :ref:`Java (Android) <api_bindings_java_android>`
* :ref:`PHP <api_bindings_php>`
* :ref:`Python <api_bindings_python>`
* :ref:`Ruby <api_bindings_ruby>`
* :ref:`VB.NET <api_bindings_vbnet>`
