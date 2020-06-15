
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

* Linux mit libusb 1.0.6 oder neuer
* Windows XP oder neuer
* macOS 10.8 (Mountain Lion) oder neuer


.. _brickd_installation:

Installation
------------

* :ref:`Linux <brickd_install_linux>`
* :ref:`Windows <brickd_install_windows>`
* :ref:`macOS <brickd_install_macos>`

.. toctree::
   :hidden:

   Linux <Brickd_Install_Linux>
   Windows <Brickd_Install_Windows>
   macOS <Brickd_Install_MacOSX>


Logging
-------

Standardmäßig loggt Brick Daemon Nachrichten über Informationen, Warnungen und
Fehler. Diese beinhalten auch Informationen über USB Hotplug und TCP/IP
Verbindungen.

* Linux und macOS: Nachrichten werden in diesem Log-Datei geschrieben::

   /var/log/brickd.log

* Windows: Nachrichten werden einer Log-Datei namens ``brickd.log`` im Brick
  Daemon Data-Verzeichnis gespeichert:

  * Windows XP::

     C:\Dokumente und Einstellungen\All Users\Application Data\Tinkerforge\Brickd\brickd.log

  * Windows Vista oder neuer::

     C:\ProgramData\Tinkerforge\Brickd\brickd.log

  Das ``logviewer.exe`` Tool (Teil der brickd Installation) kann diese Log-Datei
  anzeigen und beinhaltet auch eine Live Log Ansicht.

Falls der Standard Logging Einstellung nicht genug Details ausgibt, um ein
Problem debuggen zu können, dann kann das Debug Log Level aktiviert werden.
Dies ist standardmäßig nicht aktiviert, da es die Menge der ausgegebenen
Log-Nachrichten stark erhöht, so dass es einen Einfluss auf den
Nachrichtendurchsatz von brickd haben kann.

* Windows: Das ``logviewer.exe`` Tool stellt ebenfalls Live Log Ansicht
  bereit, die auf Debug Level gestellt werden kann.


Konfiguration
-------------

Brick Daemon verwendet eine Konfigurationsdatei mit Schlüssel-Wert Format:

* Linux und macOS: Die Konfigurationsdatei heißt ``brickd.conf`` und ist hier
  gespeichert::

   /etc/brickd.conf

* Windows: Die Konfigurationsdatei heißt ``brickd.ini`` und ist im Brick Daemon
  Data-Verzeichnis gespeichert:

  * Windows XP::

     C:\Dokumente und Einstellungen\All Users\Application Data\Tinkerforge\Brickd\brickd.ini

  * Windows Vista oder neuer::

     C:\ProgramData\Tinkerforge\Brickd\brickd.ini

  Das ``logviewer.exe`` Tool (Teil der brickd Installation) kann diese
  Konfigurationsdatei bearbeiten.

Nach Änderungen an der Konfigurationsdatei muss Brick Daemon neugestartet
werden um die Änderungen zu übernehmen:

* Linux (systemd)::

   sudo systemctl restart brickd

* Linux (SysVinit)::

   sudo /etc/init.d/brickd restart

* Windows: Mit dem ``logviewer.exe`` Tool (Teil der brickd Installation) kann
  der Brick Daemon Dienst neustarten werden.
* macOS::

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

* Linux::

   brickd --version

* Windows XP:

  .. code-block:: none

    "C:\Programme\Tinkerforge\Brickd\brickd.exe" --version

* Windows Vista oder neuer:

  .. code-block:: none

    "C:\Programme (x86)\Tinkerforge\Brickd\brickd.exe" --version

* macOS (bis Brick Daemon 2.2.1)::

   /usr/libexec/brickd.app/Contents/MacOS/brickd --version

* macOS (seit Brick Daemon 2.2.2)::

   /usr/local/libexec/brickd.app/Contents/MacOS/brickd --version
