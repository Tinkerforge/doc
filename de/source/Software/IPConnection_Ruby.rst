.. _ipcon_ruby:

Ruby - IP Connection
====================

Dies ist die API Beschreibung für die Ruby Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_ruby_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.rb>`__

.. literalinclude:: example.rb
 :language: ruby
 :linenos:
 :tab-width: 4


.. _ipcon_ruby_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. rb:function:: IPConnection::new() -> ipcon

 Erzeugt ein IP Connection Objekt. Das konstruierte Objekt wird für
 den Konstruktor von Bricks und Bricklets benötigt.


.. rb:function:: IPConnection#connect(host, port) -> nil

 :param host: str
 :param port: int

 Erstellt eine TCP/IP Verbindung zum gegebenen Host und Port.
 Host und Port können zu eine Brick Daemon oder der WIFI/Ethernet Extension 
 zeigen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung
 erfolgreich aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine IOException
 falls kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen
 Host und Port horchene.


.. rb:function:: IPConnection#disconnect() -> nil

 Trennt die TCP/IP verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. rb:function:: IPConnection#get_connection_state() -> nil

 Kann die folgenden Zustände zurückgeben:

 * IPCON_CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPCON_CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPCON_CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment eine Verbindung aufzubauen.


.. rb:function:: IPConnection#set_auto_reconnect(auto_reconnect) -> nil

 :param auto_reconnect: bool

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen.

 Standardwert ist *true*.


.. rb:function:: IPConnection#get_auto_reconnect() -> bool 

 :rtype: bool

 Gibt *true* zurück wenn die Wiederverbindung aktiviert ist und *false* sonst.


.. rb:function:: IPConnection#set_timeout(timeout) -> nil

 :param timeout: int

 Setzt den Timeout (in ms) für Getter und für Setter die "response expected"
 aktiviert haben.

 Standardwert ist 2500ms.


.. rb:function:: IPConnection#get_timeout() -> int

 :rtype: int


 Gibt den Timeout zurück, wie er von :rb:func:`#set_timeout <IPConnection#set_timeout>`
 gesetzt wurde.

.. rb:function:: IPConnection#wait() -> nil


 Hält den aktuellen Thread an bis :rb:func:`#unwait <IPConnection#unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.


.. rb:function:: IPConnection#unwait() -> nil

 Startet einen Thread der vorher mit :rb:func:`#wait <IPConnection#wait>`
 angehalten wurde wieder.

 Wait und unwait agieren auf die gleiche Weise wie "require" und "release" einer 
 Semaphore.


.. rb:function:: IPConnection#enumerate() -> nil

 Broadcast einer Enumerierungsanfrage. Alle Bricks/Bricks werden mit
 einem Enumerate Callback antworten.


Callbacks
^^^^^^^^^

*Callbacks* können mit *callback IDs* registriert werden um zeitkritische
oder wiederkehrende Daten vom Gerät zu erhalten. Die Registrierung kann
mit der Funktion *register_callbacks* des 
ipcon Objektes durchgeführt werden. Der erste Parameter ist der Callback ID
und der zweite Parameter der Block:

.. code-block:: ruby

    ipcon.register_callback IPConnection::CALLBACK_EXAMPLE, do |param|
      puts "#{param}"
    end

Die verfügbaren Konstanten mit der dazugehörigen Parameteranzahl und -typen werden
weiter unten beschrieben.


.. rb:attribute:: IPConnection::CALLBACK_ENUMERATE

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


.. rb:attribute:: IPConnection::CALLBACK_CONNECTED

 :param reason: int

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung aufgebaut hat,
 mögliche Gründe sind:

 * CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach anfrage vom Benutzer.
 * CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach einer automatischen Wiederverbindung.


.. rb:attribute:: IPConnection::CALLBACK_DISCONNECTED

 :param reason: int

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection getrennt wird,
 mögliche Gründe sind:

 * DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer angefragt.
 * DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren Problems.
 * DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon oder WIFI/Ethernet Extension eingeleitet.
