
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Ruby - IP Connection

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

`Download <https://github.com/Tinkerforge/doc/raw/master/de/source/Software/example.rb>`__

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

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. rb:function:: IPConnection#connect(host, port) -> nil

 :param host: str
 :param port: int

 Erstellt eine TCP/IP Verbindung zum gegebenen *host* und *port*. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. rb:function:: IPConnection#disconnect() -> nil

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. rb:function:: IPConnection#get_connection_state() -> int

 Kann die folgenden Zustände zurückgeben:

 * IPConnection::CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection::CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection::CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. rb:function:: IPConnection#set_auto_reconnect(auto_reconnect) -> nil

 :param auto_reconnect: bool

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen, falls die Verbindung
 verloren geht.

 Standardwert ist *true*.


.. rb:function:: IPConnection#get_auto_reconnect() -> bool

 :rtype: bool

 Gibt *true* zurück wenn die Wiederverbindung aktiviert ist und *false* sonst.


.. rb:function:: IPConnection#set_timeout(timeout) -> nil

 :param timeout: float

 Setzt den Timeout in Sekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2.5.


.. rb:function:: IPConnection#get_timeout() -> int

 :rtype: int

 Gibt den Timeout zurück, wie er von
 :rb:func:`#set_timeout <IPConnection#set_timeout>` gesetzt wurde.


.. rb:function:: IPConnection#enumerate() -> nil

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. rb:function:: IPConnection#wait() -> nil


 Hält den aktuellen Thread an bis :rb:func:`#unwait <IPConnection#unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``wait`` und ``unwait`` agieren auf die gleiche Weise wie "acquire" und
 "release" einer Semaphore.


.. rb:function:: IPConnection#unwait() -> nil

 Startet einen Thread der vorher mit :rb:func:`#wait <IPConnection#wait>`
 angehalten wurde wieder.

 ``wait`` und ``unwait`` agieren auf die gleiche Weise wie "acquire" und
 "release" einer Semaphore.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rb:function:: IPConnection#register_callback(id) { |param [, ...]| block } -> nil

 :param id: int

 Registriert einen Callback für eine gegebene ID.

 Die verfügbaren IDs mit zugehörenden Callback-Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung kann mit der Funktion :rb:func:`#register_callback
<IPConnection#register_callback>` durchgeführt werden. Der erste Parameter ist
der Callback ID und der zweite Parameter der Block:

.. code-block:: ruby

    ipcon.register_callback IPConnection::CALLBACK_EXAMPLE, do |param|
      puts "#{param}"
    end

Die verfügbaren Konstanten mit der dazugehörigen Parameteranzahl und -typen
werden weiter unten beschrieben.


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
 * *connected_uid*: Die UID wo das Brick/Bricklet mit verbunden ist. Für ein
   Bricklet ist dies die UID des Bricks mit dem es verbunden ist. Für einen
   Brick ist es die UID des untersten Master Bricks in einem Stapel. Der
   unterste Master Brick hat die connected UID "1". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * *position*: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'd' (Position an Brick).
 * *hardware_version*: Major, Minor und Release Nummer der Hardwareversion.
 * *firmware_version*: Major, Minor und Release number der Firmwareversion.
 * *device_identifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * *enumeration_type*: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection::ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst).
 * IPConnection::ENUMERATION_TYPE_CONNECTED (1): Gerät ist neu verfügbar
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection::ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur *uid* und
   *enumeration_type* einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht)

 Die Device Identifiers sind :ref:`hier <device_identifier>` zu finden.


.. rb:attribute:: IPConnection::CALLBACK_CONNECTED

 :param connect_reason: int

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection::CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection::CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach
   einer automatischen Wiederverbindung.


.. rb:attribute:: IPConnection::CALLBACK_DISCONNECTED

 :param disconnect_reason: int

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection::DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection::DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines
   unlösbaren Problems.
 * IPConnection::DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick
   Daemon oder WIFI/Ethernet Extension eingeleitet.
