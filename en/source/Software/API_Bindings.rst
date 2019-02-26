
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

Installation and usage instructions for each supported programming language:

* :ref:`C/C++ <api_bindings_c>`
* :ref:`C/C++ (iOS) <api_bindings_c_ios>`
* :ref:`C# <api_bindings_csharp>`
* :ref:`C# (Windows Phone) <api_bindings_csharp_windows_phone>`
* :ref:`Delphi/Lazarus <api_bindings_delphi>`
* :ref:`Go <api_bindings_go>`
* :ref:`Java <api_bindings_java>`
* :ref:`Java (Android) <api_bindings_java_android>`
* :ref:`JavaScript <api_bindings_javascript>`
* :ref:`LabVIEW <api_bindings_labview>`
* :ref:`Mathematica <api_bindings_mathematica>`
* :ref:`MATLAB/Octave <api_bindings_matlab>`
* :ref:`MQTT <api_bindings_mqtt>`
* :ref:`Perl <api_bindings_perl>`
* :ref:`PHP <api_bindings_php>`
* :ref:`Python <api_bindings_python>`
* :ref:`Ruby <api_bindings_ruby>`
* :ref:`Rust <api_bindings_rust>`
* :ref:`Shell <api_bindings_shell>`
* :ref:`Visual Basic .NET <api_bindings_vbnet>`

.. toctree::
   :hidden:

   C/C++ <API_Bindings_C>
   C/C++ (iOS) <API_Bindings_C_iOS>
   C# <API_Bindings_CSharp>
   C# (Windows Phone) <API_Bindings_CSharp_Windows_Phone>
   Delphi/Lazarus <API_Bindings_Delphi>
   Go <API_Bindings_Go>
   Java <API_Bindings_Java>
   Java (Android) <API_Bindings_Java_Android>
   JavaScript <API_Bindings_JavaScript>
   LabVIEW <API_Bindings_LabVIEW>
   Mathematica <API_Bindings_Mathematica>
   MATLAB/Octave <API_Bindings_MATLAB>
   MQTT <API_Bindings_MQTT>
   Perl <API_Bindings_Perl>
   PHP <API_Bindings_PHP>
   Python <API_Bindings_Python>
   Ruby <API_Bindings_Ruby>
   Rust <API_Bindings_Rust>
   Shell <API_Bindings_Shell>
   Visual Basic .NET <API_Bindings_VBNET>

The latest versions of the bindings can be found in the
:ref:`download section <downloads_bindings_examples>`.
