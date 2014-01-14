
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / API Bindings

.. _api_bindings:

API Bindings
============

Die API Bindings stellen eine TCP/IP Verbindung zum
:ref:`Brick Daemon <brickd>` her. Jeder Funktionsaufruf erzeugt ein TCP/IP Paket,
das über den Brick Daemon zum Brick geschickt wird. Beim Brick Daemon vom Brick
eingehende Pakete werden an den Aufrufer zurückgeroutet.

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
* :ref:`Delphi <api_bindings_delphi>`
* :ref:`Java <api_bindings_java>`
* :ref:`Java (Android) <api_bindings_java_android>`
* :ref:`Perl <api_bindings_perl>`
* :ref:`PHP <api_bindings_php>`
* :ref:`Python <api_bindings_python>`
* :ref:`Ruby <api_bindings_ruby>`
* :ref:`Shell <api_bindings_shell>`
* :ref:`VB.NET <api_bindings_vbnet>`


.. _api_bindings_ip_connection:

IP Connection
-------------

Die IP Connection erstellt eine TCP/IP Verbindung zwischen dem
:ref:`Brick Daemon <brickd>` und den entsprechenden API Bindings für die
verschiedenen Programmiersprachen.

Diese wird in den Bindings benutzt und ist für jede unterstütze
Programmiersprache implementiert. Die dazugehörige Dokumentation ist hier zu
finden:

.. include:: API_Bindings_bindings.table
