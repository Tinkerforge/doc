
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / Brick Daemon (brickd)

.. _brickd:

Brick Daemon (brickd)
=====================

Der Brick Daemon ist ein Daemon (bzw. Service für Windows) der als eine Brücke
zwischen :ref:`Bricks <product_overview_bricks>`/:ref:`Bricklets
<product_overview_bricklets>` und den :ref:`API Bindings <api_bindings>` für die
verschiedenen Programmiersprachen fungiert.

Der Daemon leitet Daten zwischen der USB Verbindung und den TCP/IP Sockets
hin und her. Bei der Benutzung der API Bindings wird eine TCP/IP Verbindung
zum Brick Daemon hergestellt. Dieses Konzept erlaubt es Bindings für
nahezu jede Programmiersprache ohne Abhängigkeiten zu erstellen. Dadurch ist
es möglich Bricks und Bricklets über eingebettete Geräte wie Smartphones
zu programmieren, die nur spezifische Programmiersprachen unterstützten.

Zusätzlich ist es möglich den PC auf dem der Brick Daemon läuft von dem
PC auf dem der Benutzercode läuft zu trennen. Dadurch ist das Steuern über ein
Smartphone oder auch über das Internet möglich.


.. _brickd_installation:

Installation
------------

* :ref:`Windows <brickd_install_windows>`
* :ref:`Linux <brickd_install_linux>`
* :ref:`Mac OS X <brickd_install_macosx>`


Logging
-------

Standardmäßig loggt Brick Daemon Nachrichten über Informationen, Warnungen und
Fehler.

* Windows: Nachrichten werden im Windows Event Log angezeigt. Das
  ``eventlog.exe`` Tool (Teil der brickd Installation) zeigt die brickd
  Meldungen im Windows Event Log an.
* Linux und Mac OS X: Nachrichten werden nach ``/var/log/brickd.log`` geschrieben.


Installierte Version herausfinden
---------------------------------

Seit Brick Daemon Version 1.0.8 ist es möglich die aktuell installierte
Brick Daemon Version zu erfragen. Dafür unterstützt der Brick Daemon
den Kommandozeilenparameter `--version`:

* Windows:

  .. code-block:: none

    "C:\Program Files\Tinkerforge\Brickd\brickd.exe" --version

* Linux::

   brickd --version

* Mac OS X::

   /usr/libexec/brickd.app/Contents/MacOS/brickd --version


Kommandozeilenparameter
-----------------------

Allgemein:

* ``--help`` zeigt Hilfetext an
* ``--version`` zeigt Versionsnummer an
* ``--check-config`` prüft Konfigurationsdatei auf Fehler
* ``--debug`` setzt alle Log Level auf Debug
* ``--libusb-debug`` setzt libusb Log Level auf Debug

Spezifisch für Windows:

* ``--install`` registriert und starten Brick Daemon als Service
* ``--uninstall`` stoppt und deregistriert  Brick Daemon als Service
* ``--console`` erzwingt den Start als Konsolenanwendung
* ``--log-to-file`` schreibt alle Log Nachrichten in eine Datei
