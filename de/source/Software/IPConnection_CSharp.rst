
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#ip-connection">IP Connection</a> / C# - IP Connection

.. _ipcon_csharp:

C# - IP Connection
==================

Dies ist die API Beschreibung für die C# Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_csharp_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/de/source/Software/Example.cs>`__

.. literalinclude:: Example.cs
 :language: csharp
 :linenos:
 :tab-width: 4


.. _ipcon_csharp_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. csharp:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. csharp:function:: public void IPConnection::Connect(String host, int port)

 Erstellt eine TCP/IP Verbindung zum gegebenen *host* und *port*. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. csharp:function:: public void IPConnection::Disconnect()

 Trennt die TCP/IP verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. csharp:function:: public short IPConnection::GetConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. csharp:function:: public void IPConnection::SetAutoReconnect(boolean autoReconnect)

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen, falls die Verbindung
 verloren geht.

 Standardwert ist *true*.


.. csharp:function:: public boolean IPConnection::GetAutoReconnect()

 Gibt *true* zurück wenn die Wiederverbindung aktiviert ist und *false* sonst.


.. csharp:function:: public void IPConnection::SetTimeout(int timeout)

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. csharp:function:: public int IPConnection::GetTimeout()

 Gibt den Timeout zurück, wie er von :csharp:func:`SetTimeout() <IPConnection::SetTimeout>`
 gesetzt wurde.


.. csharp:function:: public void IPConnection::Enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. csharp:function:: public void IPConnection::Wait()

 Hält den aktuellen Thread an bis :csharp:func:`Unwait() <IPConnection::Unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 Wait und unwait agieren auf die gleiche Weise wie "acquire" und "release" einer
 Semaphore.


.. csharp:function:: public void IPConnection::Unwait()

 Startet einen Thread der vorher mit :csharp:func:`Wait() <IPConnection::Wait>`
 angehalten wurde wieder.

 Wait und unwait agieren auf die gleiche Weise wie "acquire" und "release" einer
 Semaphore.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung geschieht durch Anhängen des Callback Handlers an den
passenden Event:

.. code-block:: csharp

    void Callback(IPConnection sender, int value)
    {
        System.Console.WriteLine("Value: " + value);
    }

    ipcon.ExampleCallback += Callback;

Die verfügbaren Events werden im Folgenden beschrieben.


.. csharp:function:: public event IPConnection::EnumerateCallback(IPConnection sender, string uid, string connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)

 Der Event empfängt sieben Parameter:

 * *uid*: Die UID des Bricks/Bricklets.
 * *connectedUid*: Die UID wo das Brick/Bricklet mit verbunden ist. Für ein
   Bricklet ist dies die UID des Bricks mit dem es verbunden ist. Für einen
   Brick ist es die UID des untersten Master Bricks in einem Stapel. Der
   unterste Master Brick hat die connected UID "1". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * *position*: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'd' (Position an Brick).
 * *hardwareVersion*: Major, Minor und Release Nummer der Hardwareversion.
 * *firmwareVersion*: Major, Minor und Release Nummer der Firmwareversion.
 * *deviceIdentifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * *enumerationType*: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst).
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Gerät ist neu verfügbar
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur *uid* und
   *enumerationType* einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Event
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifiers sind :ref:`hier <device_identifier>` zu finden.


.. csharp:function:: public event IPConnection::Connected(IPConnection sender, short connectReason)

 Dieser Event wird ausgelöst wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach
   einer automatischen Wiederverbindung.


.. csharp:function:: public event IPConnection::Disconnected(IPConnection sender, short disconnectReason)

 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
