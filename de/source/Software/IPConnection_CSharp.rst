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

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.cs>`__

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

 Erzeugt ein IP Connection Objekt. Das konstruierte Objekt wird für
 den Konstruktor von Bricks und Bricklets benötigt.

.. csharp:function:: public void IPConnection::Connect(String host, int port)

 Erstellt eine TCP/IP Verbindung zum gegebenen Host und Port.
 Host und Port können zu eine Brick Daemon oder der WIFI/Ethernet Extension 
 zeigen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung
 erfolgreich aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception
 falls kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen
 Host und Port horchen.

.. csharp:function:: public void IPConnection::Disconnect()

 Trennt die TCP/IP verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.

.. csharp:function:: public byte IPConnection::GetConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * CONNECTION_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * CONNECTION_CONNETED (1): Eine Verbindung zum Brick Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * CONNECTION_PENDING (2): IP Connection versucht im Moment eine Verbindung aufzubauen.

.. csharp:function:: public void IPConnection::SetAutoReconnect(boolean autoReconnect)

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen, falls die Verbindung
 verloren geht.

 Standardwert ist *true*.

.. csharp:function:: public boolean IPConnection::GetAutoReconnect()

 Gibt *true* zurück wenn die Wiederverbindung aktiviert ist und *false* sonst.

.. csharp:function:: public void IPConnection::SetTimeout(int timeout)

 Setzt den Timeout (in ms) für Getter und für Setter die "response expected"
 aktiviert haben.

 Standardwert ist 2500ms.

.. csharp:function:: public int IPConnection::GetTimeout()

 Gibt den Timeout zurück, wie er von :csharp:func:`SetTimeout <IPConnection::SetTimeout>`
 gesetzt wurde.

.. csharp:function:: public void IPConnection::Wait()

 Hält den aktuellen Thread an bis :csharp:func:`Unwait <IPConnection::Unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 Wait und unwait agieren auf die gleiche Weise wie "require" und "release" einer 
 Semaphore.
 
.. csharp:function:: public void IPConnection::Unwait()

 Startet einen Thread der vorher mit :csharp:func:`Wait <IPConnection::Wait>`
 angehalten wurde wieder.

 Wait und unwait agieren auf die gleiche Weise wie "require" und "release" einer 
 Semaphore.

.. csharp:function:: public void IPConnection::Enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks/Bricks werden mit
 einem Enumerate Callback antworten.


Callbacks
^^^^^^^^^

*Callbacks* können registriert werden um zeitkritische
oder wiederkehrende Daten vom Gerät zu erhalten. Die Registrierung kann
durch die anhängen des Callback-Handlers zum passenden Event geschehen:

.. code-block:: csharp
    
    void Callback(object sender, int value)
    {
        System.Console.WriteLine("Value: " + value);
    }

    device.ExampleCallback += Callback;

Die verfügbaren Events werden weiter unten beschrieben.


.. csharp:function:: public event IPConnection::EnumerateCallback(object sender, string UID, string connectedUID, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)

 Der Event empfängt sieben Parameter:

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

.. csharp:function:: public event IPConnection::Connected(object sender, int reason)

 Dieser Event wird aufgerufen wenn die IP Connection eine Verbindung aufgebaut hat,
 mögliche Gründe sind:

 * CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach anfrage vom Benutzer.
 * CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach einer automatischen Wiederverbindung.

.. csharp:function:: public event IPConnection::Disconnected(object sender, int reason)
 
 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection getrennt wird,
 mögliche Gründe sind:

 * DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer angefragt.
 * DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren Problems.
 * DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon oder WIFI/Ethernet Extension eingeleitet.
