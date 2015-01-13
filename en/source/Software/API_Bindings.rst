
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / API Bindings

.. _api_bindings:

API Bindings
============

The API bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your programs.
They do this by establishing a TCP/IP connection to the
:ref:`Brick Daemon <brickd>` or a :ref:`WIFI <wifi_extension>`/:ref:`Ethernet
<ethernet_extension>` Extension. Each function call creates a TCP/IP packet that
is send over the Brick Daemon or directly to the Brick. Incoming packets from
the Brick are routed back to the caller.

See also our :ref:`tutorial <tutorial_first_steps>` for more information on how
everything works together.

.. _api_bindings_install_and_usage:

Installation and Usage
----------------------

Installation and usage instructions for each supported programming language:

* :ref:`C/C++ <api_bindings_c>`
* :ref:`C/C++ (iOS) <api_bindings_c_ios>`
* :ref:`C# <api_bindings_csharp>`
* :ref:`C# (Windows Phone) <api_bindings_csharp_windows_phone>`
* :ref:`Delphi/Lazarus <api_bindings_delphi>`
* :ref:`Java <api_bindings_java>`
* :ref:`Java (Android) <api_bindings_java_android>`
* :ref:`JavaScript <api_bindings_javascript>`
* :ref:`LabVIEW <api_bindings_labview>`
* :ref:`Mathematica <api_bindings_mathematica>`
* :ref:`MATLAB/Octave <api_bindings_matlab>`
* :ref:`Perl <api_bindings_perl>`
* :ref:`PHP <api_bindings_php>`
* :ref:`Python <api_bindings_python>`
* :ref:`Ruby <api_bindings_ruby>`
* :ref:`Shell <api_bindings_shell>`
* :ref:`Visual Basic .NET <api_bindings_vbnet>`

The latest versions of the bindings can be found in the
:ref:`download section <downloads_bindings_examples>`.


.. _api_bindings_ip_connection:

IP Connection
-------------

The IP Connection manages the TCP/IP communication between the API bindings and
the :ref:`Brick Daemon <brickd>` or a :ref:`WIFI <wifi_extension>`/:ref:`Ethernet
<ethernet_extension>` Extension.

It is used by the bindings and implemented for each programming language.
The corresponding documentation can be found here:

.. include:: API_Bindings_bindings.table
