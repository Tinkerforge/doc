
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / API Bindings

.. _api_bindings:

API Bindings
============

Die API Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Programmen heraus zu
steuern. Dafür wird eine TCP/IP Verbindung zum :ref:`Brick Daemon <brickd>`
oder einer :ref:`WIFI <wifi_extension>`/:ref:`Ethernet <ethernet_extension>`
Extension erstellt. Jeder Funktionsaufruf erzeugt ein TCP/IP Paket, das über
den Brick Daemon oder direkt zum Brick geschickt wird. Vom Brick eingehende
Pakete werden an den Aufrufer zurückgeleitet.

Diese :ref:`Tutorial <tutorial_first_steps>` beschreibt wie alles zusammengehört
und funktioniert.

Verwendung der Bindings
-----------------------

Die neusten Versionen der Bindings sind im :ref:`Downloadbereich
<downloads_bindings_examples>` zu finden.

Anleitungen zur Installation und Verwendung der Bindings für jede unterstütze
Programmiersprache:

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


.. _api_bindings_ip_connection:

IP Connection
-------------

Die IP Connection kümmert sich um die Kommunikation zwischen einem
:ref:`Brick Daemon <brickd>` oder einer
:ref:`WIFI <wifi_extension>`/:ref:`Ethernet <ethernet_extension>` Extension.

Diese wird in den Bindings benutzt und ist für jede unterstütze
Programmiersprache implementiert. Die dazugehörige Dokumentation ist hier zu
finden:

.. include:: API_Bindings_bindings.table
