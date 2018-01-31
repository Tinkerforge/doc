
.. |ref_api_bindings| replace:: :ref:`C# API Bindings <api_bindings_csharp>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_csharp_install>`
.. |bindings_name| replace:: C#

.. _ipcon_csharp:

C# - IP Connection
==================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_csharp_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.cs) <https://github.com/Tinkerforge/generators/raw/master/csharp/ExampleEnumerate.cs>`__

.. literalinclude:: IPConnection_CSharp_ExampleEnumerate.cs
 :language: csharp
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.cs) <https://github.com/Tinkerforge/generators/raw/master/csharp/ExampleAuthenticate.cs>`__

.. literalinclude:: IPConnection_CSharp_ExampleAuthenticate.cs
 :language: csharp
 :linenos:
 :tab-width: 4


.. _ipcon_csharp_api:

API
---

Der Namensraum für IPConnection ist ``Tinkerforge.*``.

Grundfunktionen
^^^^^^^^^^^^^^^

.. csharp:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. csharp:function:: public void IPConnection::Connect(String host, int port)

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. csharp:function:: public void IPConnection::Disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. csharp:function:: public void IPConnection::Authenticate(string secret)

 Führt einen Authentifizierungs-Handshake mit dem verbundenen Brick Daemon
 oder WIFI/Ethernet Extension durch.
 Ist der Handshake erfolgreich dann wechselt die Verbindung vom
 nicht-authentifizierten in den authentifizierten Zustand und die Kommunikation
 kann normal weitergeführt werden. Schlägt der Handshake fehl wird die
 Verbindung durch die Gegenseite geschlossen. Die Authentifizierung kann
 fehlschlagen wenn das Authentifizierungsgeheimnis nicht übereinstimmt oder
 Authentifizierung für den Brick Daemon oder die WIFI/Ethernet Extension nicht
 aktiviert ist.

 Für mehr Informationen zur Authentifizierung siehe das dazugehörige
 :ref:`Tutorial <tutorial_authentication>`.

 .. versionadded:: 2.1.0


.. csharp:function:: public short IPConnection::GetConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. csharp:function:: public void IPConnection::SetAutoReconnect(bool autoReconnect)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :csharp:func:`Connect() <IPConnection::Connect>`.

 Standardwert ist *true*.


.. csharp:function:: public bool IPConnection::GetAutoReconnect()

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


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

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


.. csharp:function:: public void IPConnection::Unwait()

 Startet einen Thread der vorher mit :csharp:func:`Wait() <IPConnection::Wait>`
 angehalten wurde wieder.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung geschieht durch Anhängen des Callback Handlers an den
passenden Event:

.. code-block:: csharp

    void MyCallback(IPConnection sender, int value)
    {
        System.Console.WriteLine("Value: " + value);
    }

    ipcon.ExampleCallback += MyCallback;

Die verfügbaren Events werden im Folgenden beschrieben.


.. csharp:function:: public event IPConnection::EnumerateCallback(IPConnection sender, string uid, string connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)

 Der Event empfängt sieben Parameter:

 * ``uid``: Die UID des Bricks/Bricklets.
 * ``connectedUid``: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``position``: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'd' (Position an Brick).
 * ``hardwareVersion``: Major, Minor und Release Nummer der Hardwareversion.
 * ``firmwareVersion``: Major, Minor und Release Nummer der Firmwareversion.
 * ``deviceIdentifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * ``enumerationType``: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst: :csharp:func:`Enumerate()
   <IPConnection::Enumerate>`). Diese Enumerierungsart kann mehrfach für das
   selbe Gerät auftreten.
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Event
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>.DEVICE_IDENTIFIER

 Zum Beispiel: :csharp:member:`BrickMaster.DEVICE_IDENTIFIER <BrickMaster::DEVICE_IDENTIFIER>`
 oder :csharp:member:`BrickletAmbientLight.DEVICE_IDENTIFIER <BrickletAmbientLight::DEVICE_IDENTIFIER>`.


.. csharp:function:: public event IPConnection::ConnectedCallback(IPConnection sender, short connectReason)

 Dieser Event wird ausgelöst wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut durch
   Auto-Reconnect.


.. csharp:function:: public event IPConnection::DisconnectedCallback(IPConnection sender, short disconnectReason)

 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
