
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / Brick Daemon (brickd)

.. _brickd:

Brick Daemon (brickd)
=====================

Der Brick Daemon ist ein Daemon (bzw. Service für Windows) der als eine Brücke
zwischen :ref:`Bricks <primer_bricks>`/:ref:`Bricklets
<primer_bricklets>` und den :ref:`API Bindings <api_bindings>` für die
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


Voraussetzungen
---------------

* Windows XP oder neuer
* Linux mit libusb 1.0 oder neuer
* Mac OS X 10.8 oder neuer


.. _brickd_installation:

Installation
------------

* :ref:`Windows <brickd_install_windows>`
* :ref:`Linux <brickd_install_linux>`
* :ref:`Mac OS X <brickd_install_macosx>`

.. toctree::
   :hidden:

   Windows <Brickd_Install_Windows>
   Linux <Brickd_Install_Linux>
   Mac OS X <Brickd_Install_MacOSX>


Logging
-------

Standardmäßig loggt Brick Daemon Nachrichten über Informationen, Warnungen und
Fehler. Diese beinhalten auch Informationen über USB hotplug und TCP/IP
Verbindungen.

* Windows: Nachrichten werden im Windows Event Log angezeigt. Das
  ``logviewer.exe`` Tool (Teil der brickd Installation) zeigt die brickd
  Meldungen im Windows Event Log an.
* Linux und Mac OS X: Nachrichten werden nach ``/var/log/brickd.log`` geschrieben.

Falls der Standard Logging Einstellung nicht genug Details ausgibt, um ein
Problem debuggen zu können, dann kann das Debug Log Level aktiviert werden.
Dies ist standardmäßig nicht aktiviert, da es die Menge der ausgegebenen
Lognachrichten stark erhöht, so dass es einen Einfluss auf den
Nachrichtendurchsatz von brickd haben kann.

* Windows: Das ``logviewer.exe`` Tool stellt ebenfalls Live Debug Log Ansicht
  bereit, die das vollständige Debug Log eines laufenden brickd anzeigt.


Konfiguration
-------------

Brick Daemon verwendet eine Konfigurationsdatei mit Schlüssel-Wert Format:

* Windows: Die Konfigurationsdatei heißt ``brickd.ini`` und ist im Brick Daemon
  Installationsverzeichnis gespeichert::

   C:\Program Files\Tinkerforge\Brickd\brickd.ini

* Linux und Mac OS X: Die Konfigurationsdatei heißt ``brickd.conf`` und ist hier
  gespeichert::

   /etc/brickd.conf

Nach Änderungen an der Konfigurationsdatei muss Brick Daemon neugestartet
werden um die Änderungen zu übernehmen:

* Windows:

  Die "Computerverwaltung" öffnen, zum Abschnitt für "Dienste" wechseln
  und den Brick Daemon Dienst neustarten.
* Linux::

   sudo /etc/init.d/brickd restart

* Mac OS X::

   sudo launchctl stop com.tinkerforge.brickd
   sudo launchctl start com.tinkerforge.brickd

Wenn die Konfigurationsdatei fehlerhaft ist meldet Brick Daemon dies im Log.


.. _brickd_websockets:

WebSockets
^^^^^^^^^^

Brick Daemon unterstützt seit Version 2.1.0 `WebSockets
<https://de.wikipedia.org/wiki/WebSocket>`__. Diese sind
standardmäßig deaktiviert. Um WebSockets zu aktivieren muss ein
WebSockets-Port in der Brick Daemon Konfigurationsdatei eingetragen werden.

Die WebSockets-Port Option hat den Schlüssel ``listen.websocket_port``. Ein
Wert von 0 oder das Fehlen des ``listen.websocket_port`` Schlüssels führt zur
deaktiviert der WebSocket-Unterstützung. Hier der Authentifizierungsabschnitt
einer Beispiel-Konfiguration, das dem empfohlenen Wert 4280 als
WebSockets-Port verwendet:

  .. code-block:: none

    listen.websocket_port = 4280

Danach muss Brick Daemon neugestartet werden, um die Änderungen an der
Konfigurationsdatei zu übernehmen. Ab jetzt kann die Browser-Version der
:ref:`JavaScript Bindings <api_bindings_javascript>` sich zum Brick Daemon
verbinden und Bricks und Brickets steuern.

.. note::

 Da WebSockets es grundsätzlich ermöglichen, dass jede Webseite in ihrem
 Browser sich mit ihren Bricks und Bricklets verbinden kann, empfehlen
 wir :ref:`Authentifizierung <tutorial_authentication>` in Kombination mit
 WebSockets zu verwenden.


.. _brickd_authentication:

Authentifizierung
^^^^^^^^^^^^^^^^^

Brick Daemon unterstützt seit Version 2.1.0 Authentifizierung. Diese ist
standardmäßig deaktiviert. Um Authentifizierung zu aktivieren muss ein
Authentifizierungsgeheimnis in der Brick Daemon Konfigurationsdatei eingetragen
werden.

Das Authentifizierungsgeheimnis kann maximal 64 ASCII Zeichen lang sein und hat
den Schlüssel ``authentication.secret``. Ein leerer Wert oder das Fehlen des
``authentication.secret`` Schlüssels führt zur deaktiviert der Authentifizierung.
Hier der Authentifizierungsabschnitt einer Beispiel-Konfiguration die
``My Authentication Secret!`` als Authentifizierungsgeheimnis verwendet::

  authentication.secret = My Authentication Secret!

Danach muss Brick Daemon neugestartet werden, um die Änderungen an der
Konfigurationsdatei zu übernehmen. Ab jetzt muss jede TCP/IP Verbindung zum
Brick Daemon zuerst nachweisen, dass sie das Authentifizierungsgeheimnis kennt,
bevor normale Kommunikation stattfinden kann. Für mehr Informationen zur
Authentifizierung siehe das dazugehörige :ref:`Tutorial
<tutorial_authentication>`.


Installierte Version bestimmen
------------------------------

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

Spezifisch für Windows:

* ``--install`` registriert und starten Brick Daemon als Service
* ``--uninstall`` stoppt und deregistriert  Brick Daemon als Service
* ``--console`` erzwingt den Start als Konsolenanwendung
* ``--log-to-file`` schreibt alle Log Nachrichten in eine Datei
