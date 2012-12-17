.. _ipcon_python:

Python - IP Connection
======================

Dies ist die API Beschreibung für die Python Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_python_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.py>`__

.. literalinclude:: example.py
 :language: python
 :linenos:
 :tab-width: 4


.. _ipcon_python_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. py:function:: IPConnection()

 Erzeugt ein IP Connection Objekt. Das konstruierte Objekt wird für
 den Konstruktor von Bricks und Bricklets benötigt.

.. py:function:: IPConnection.connect(host, port)

 :param host: str
 :param port: int
 :rtype: None

 Erstellt eine TCP/IP Verbindung zum gegebenen Host und Port.
 Host und Port können zu eine Brick Daemon oder der WIFI/Ethernet Extension 
 zeigen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung
 erfolgreich aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine IOException
 falls kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen
 Host und Port horchene.

.. py:function:: IPConnection.disconnect()

 :rtype: None

 Trennt die TCP/IP verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.

.. py:function:: IPConnection.get_connection_state()

 :rtype: None

 Kann die folgenden Zustände zurückgeben:

 * IPCON_CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPCON_CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPCON_CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment eine Verbindung aufzubauen.

.. py:function:: IPConnection.set_auto_reconnect(auto_reconnect)

 :param auto_reconnect: bool
 :rtype: None

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen.

 Standardwert ist *True*.

.. py:function:: IPConnection.get_auto_reconnect()

 Gibt *True* zurück wenn die Wiederverbindung aktiviert ist und *False* sonst.

.. py:function:: IPConnection.set_timeout(timeout)

 :param auto_reconnect: float
 :rtype: None

 Setzt den Timeout (in ms) für Getter und für Setter die "response expected"
 aktiviert haben.

 Standardwert ist 2500ms.

.. py:function:: IPConnection.get_timeout()

 :rtype: float

 Gibt den Timeout zurück, wie er von :py:func:`IPConnection.set_timeout` gesetzt wurde.

.. py:function:: IPConnection.wait()

 :rtype: None

 Hält den aktuellen Thread an bis :py:func:`IPConnection.unwait`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

.. py:function:: IPConnection.unwait()

 :rtype: None

 Startet einen Thread der vorher mit :py:func:`IPConnection.wait`
 angehalten wurde wieder.

 Wait und unwait agieren auf die gleiche Weise wie "require" und "release" einer 
 Semaphore.

.. py:function:: IPConnection.enumerate()

 :rtype: None

 Broadcast einer Enumerierungsanfrage. Alle Bricks/Bricks werden mit
 einem Enumerate Callback antworten.

Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: IPConnection.register_callback(id, callback)

 Registriert einen Callback für eine gegebene ID.

 Die verfügbaren IDs mit zugehörenden Callback-Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

.. py:attribute:: IPConnection.CALLBACK_ENUMERATE

 :param uid: str
 :param connected_uid: str
 :param position: chr
 :param hardware_version: [int, int, int]
 :param firmware_version: [int, int, int]
 :param device_identifier: int
 :param enumeration_type: int

 Der Callback empfängt sieben Parameter:

 * *uid*: Die UID des Bricks/Bricklets.
 * *connectedUID*: Die UID wo das Brick/Bricklet mit verbunden ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist. Für einen Brick ist es die UID des untsten Master Brickss in einem Stapel. Der unterste Master Brick hat die connectedUID "1". Mit diesen Informationen sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * *position*: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets: 'a' - 'd' (Position an Brick).
 * *hardwareVersion*: Major, Minor and Release Nummer der Hardwareversion.
 * *firmwareVersion*: Major, Minor and Release number der Firmwareversion.
 * *deviceIdentifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * *enumerationType*: Art der Enumerierung

 Mögliche Enumerierungsarten sind:

 * ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar (Enumerierung vom benutzer ausgelöst).
 * ENUMERATION_TYPE_CONNECTED (1): Gerät ist neu verfügbar (automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde). Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration verloren hat und neu Konfiguriert werden muss.
 * ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei USB-Verbindungen möglich).

 Es sollte möglich sein eine "plug 'n play"-Funktionalität mit dem Enumerate Listener
 zu implementieren (wie es im Brick Viewer geschieht)

.. py:attribute:: IPConnection.CALLBACK_CONNECTED

 :param reason: int

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung aufgebaut hat,
 mögliche Gründe sind:

 * CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach anfrage vom Benutzer.
 * CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach einer automatischen Wiederverbindung.

.. py:attribute:: IPConnection.CALLBACK_DISCONNECTED

 :param reason: int

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection getrennt wird,
 mögliche Gründe sind:

 * DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer angefragt.
 * DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren Problems.
 * DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon oder WIFI/Ethernet Extension eingeleitet.
