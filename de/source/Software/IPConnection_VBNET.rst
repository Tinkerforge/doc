
.. |ref_api_bindings| replace:: :ref:`Visual Basic .NET API Bindings <api_bindings_vbnet>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_vbnet_install>`
.. |bindings_name| replace:: Visual Basic .NET

.. _ipcon_vbnet:

Visual Basic .NET - IP Connection
=================================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_vbnet_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.vb) <https://github.com/Tinkerforge/generators/raw/master/vbnet/ExampleEnumerate.vb>`__

.. literalinclude:: IPConnection_VBNET_ExampleEnumerate.vb
 :language: vbnet
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.vb) <https://github.com/Tinkerforge/generators/raw/master/vbnet/ExampleAuthenticate.vb>`__

.. literalinclude:: IPConnection_VBNET_ExampleAuthenticate.vb
 :language: vbnet
 :linenos:
 :tab-width: 4


.. _ipcon_vbnet_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. vbnet:function:: Class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. vbnet:function:: Sub IPConnection.Connect(ByVal host As String, ByVal port As Integer)

 Erstellt eine TCP/IP Verbindung zum gegebenen *host* und *port*. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. vbnet:function:: Sub IPConnection.Disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. vbnet:function:: Sub IPConnection.Authenticate(ByVal secret As String)

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


.. vbnet:function:: Function IPConnection.GetConnectionState() As Short

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.\ **CONNECTION_STATE**\ _DISCONNECTED = 0: Keine Verbindung aufgebaut.
 * IPConnection.\ **CONNECTION_STATE**\ _CONNECTED = 1: Eine Verbindung zum Brick Daemon oder
   der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.\ **CONNECTION_STATE**\ _PENDING = 2: IP Connection versucht im Moment eine
   Verbindung aufzubauen.


.. vbnet:function:: Sub IPConnection.SetAutoReconnect(ByVal autoReconnect As Boolean)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :vbnet:func:`Connect() <IPConnection.Connect>`.

 Standardwert ist *true*.


.. vbnet:function:: Function IPConnection.GetAutoReconnect() As Boolean

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *False* sonst.


.. vbnet:function:: Sub IPConnection.SetTimeout(ByVal timeout As Integer)

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. vbnet:function:: Function IPConnection.GetTimeout() As Integer

 Gibt den Timeout zurück, wie er von :vbnet:func:`IPConnection.SetTimeout`
 gesetzt wurde.


.. vbnet:function:: Sub IPConnection.Enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. vbnet:function:: Sub IPConnection.Wait()

 Hält den aktuellen Thread an bis :vbnet:func:`IPConnection.Unwait`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


.. vbnet:function:: Sub IPConnection.Unwait()

 Startet einen Thread der vorher mit :vbnet:func:`IPConnection.Wait`
 angehalten wurde wieder.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung geschieht durch Anhängen des Callback Handlers an den
passenden Event:

.. code-block:: vbnet

    Sub MyCallback(ByVal sender As IPConnection, ByVal value As Short)
        Console.WriteLine("Value: {0}", value)
    End Sub

    AddHandler ipcon.ExampleCallback, AddressOf MyCallback

Die verfügbaren Events werden im Folgenden beschrieben.


.. vbnet:function:: Event IPConnection.EnumerateCallback(ByVal sender As IPConnection, ByVal uid As String, ByVal connectedUid As String, ByVal position As Char, ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)

 Der Event empfängt sieben Parameter:

 * ``uid``: Die UID des Bricks/Bricklets.
 * ``connectedUid``: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``position``: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'h' (Position an Brick) oder 'i' (Position des Raspberry Pi (Zero) HAT)
   oder 'z' (Bricklet an :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardwareVersion``: Major, Minor und Release Nummer der Hardwareversion.
 * ``firmwareVersion``: Major, Minor und Release Nummer der Firmwareversion.
 * ``deviceIdentifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * ``enumerationType``: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection.\ **ENUMERATION_TYPE**\ _AVAILABLE = 0: Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst: :vbnet:func:`IPConnection.Enumerate`).
   Diese Enumerierungsart kann mehrfach für das selbe Gerät auftreten.
 * IPConnection.\ **ENUMERATION_TYPE**\ _CONNECTED = 1: Gerät ist wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.\ **ENUMERATION_TYPE**\ _DISCONNECTED = 2: Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur *uid* und
   *enumerationType* einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Event
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>.DEVICE_IDENTIFIER

 Zum Beispiel: :vbnet:attr:`BrickMaster.DEVICE_IDENTIFIER`
 oder :vbnet:attr:`BrickletAmbientLight.DEVICE_IDENTIFIER`.


.. vbnet:function:: Event IPConnection.ConnectedCallback(ByVal sender As IPConnection, ByVal connectReason As Short)

 Dieser Event wird ausgelöst wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.\ **CONNECT_REASON**\ _REQUEST = 0: Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.\ **CONNECT_REASON**\ _AUTO_RECONNECT = 1: Verbindung aufgebaut durch
   Auto-Reconnect.


.. vbnet:function:: Event IPConnection.DisconnectedCallback(ByVal sender As IPConnection, ByVal disconnectReason As Short)

 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.\ **DISCONNECT_REASON**\ _REQUEST = 0: Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.\ **DISCONNECT_REASON**\ _ERROR = 1: Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
