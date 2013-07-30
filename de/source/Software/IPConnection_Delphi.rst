
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Delphi - IP Connection

.. _ipcon_delphi:

Delphi - IP Connection
======================

Dies ist die API Beschreibung für die Delphi Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_delphi_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/de/source/Software/Example.pas>`__

.. literalinclude:: Example.pas
 :language: delphi
 :linenos:
 :tab-width: 4


.. _ipcon_delphi_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. delphi:function:: constructor TIPConnection.Create()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. delphi:function:: destructor TIPConnection.Destroy()

 Zerstört die IP Connection. Ruft intern :delphi:func:`Disconnect
 <TIPConnection.Disconnect>` auf. Der Socket zum Brick Daemon wird geschlossen
 und alle Threads der IP Connection werden beendet.


.. delphi:function:: procedure TIPConnection.Connect(const host: string; const port: word)

 Erstellt eine TCP/IP Verbindung zum gegebenen *host* und *port*. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. delphi:function:: procedure TIPConnection.Disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. delphi:function:: function TIPConnection.GetConnectionState(): byte

 Kann die folgenden Zustände zurückgeben:

 * IPCON_CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPCON_CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon oder
   der WIFI/Ethernet Extension ist aufgebaut.
 * IPCON_CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment eine
   Verbindung aufzubauen.


.. delphi:function:: procedure TIPConnection.SetAutoReconnect(const autoReconnect: boolean)

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen, falls die Verbindung
 verloren geht.

 Standardwert ist *true*.


.. delphi:function:: function TIPConnection.GetAutoReconnect(): boolean

 Gibt *true* zurück wenn die Wiederverbindung aktiviert ist und *False* sonst.


.. delphi:function:: procedure TIPConnection.SetTimeout(const timeout: longword)

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. delphi:function:: function TIPConnection.GetTimeout(): longword

 Gibt den Timeout zurück, wie er von :delphi:func:`TIPConnection.SetTimeout`
 gesetzt wurde.


.. delphi:function:: procedure TIPConnection.Enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. delphi:function:: procedure TIPConnection.Wait()

 Hält den aktuellen Thread an bis :delphi:func:`TIPConnection.Unwait`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie "acquire" und
 "release" einer Semaphore.


.. delphi:function:: procedure TIPConnection.Unwait()

 Startet einen Thread der vorher mit :delphi:func:`TIPConnection.Wait`
 angehalten wurde wieder.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie "acquire" und
 "release" einer Semaphore.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung erfolgt indem eine Prozedur einem Callback Property des
TIPConnection Objektes zugewiesen wird:

.. code-block:: delphi

    procedure TExample.MyCallback(sender: TIPConnection; const param: word);
    begin
      WriteLn(param);
    end;

    ipcon.OnExample := {$ifdef FPC}@{$endif}example.MyCallback;

Die verfügbaren Callback Properties und ihre Parametertypen werden im Folgenden
beschrieben.


.. delphi:function:: property TIPConnection.OnEnumerate

 .. code-block:: delphi

  procedure(sender: TIPConnection; const uid: string; const connectedUid: string; const position: char; const hardwareVersion: TVersionNumber; const firmwareVersion: TVersionNumber; const deviceIdentifier: word; const enumerationType: byte) of object;

 Der Callback empfängt sieben Parameter:

 * *uid*: Die UID des Bricks/Bricklets.
 * *connectedUid*: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * *position*: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'd' (Position an Brick).
 * *hardwareVersion*: Major, Minor und Release Nummer der Hardwareversion.
 * *firmwareVersion*: Major, Minor und Release Nummer der Firmwareversion.
 * *deviceIdentifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * *enumerationType*: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPCON_ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar (Enumerierung vom
   Benutzer ausgelöst).
 * IPCON_ENUMERATION_TYPE_CONNECTED (1): Gerät wurde neu verbunden (automatisch
   vom Brick gesendet nachdem die Kommunikation aufgebaut wurde). Dies kann
   bedeuten, dass das Gerät die vorher eingestellte Konfiguration verloren hat
   und neu konfiguriert werden muss.
 * IPCON_ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei
   USB-Verbindungen möglich). In diesem Fall haben nur *uid* und
   *enumerationType* einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifiers sind :ref:`hier <device_identifier>` zu finden.


.. delphi:function:: property TIPConnection.OnConnected

 .. code-block:: delphi

  procedure(sender: TIPConnection; const connectReason: byte) of object;

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPCON_CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage vom Benutzer.
 * IPCON_CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach einer
   automatischen Wiederverbindung.


.. delphi:function:: property TIPConnection.OnDisconnected

 .. code-block:: delphi

  procedure(sender: TIPConnection; const disconnectReason: byte) of object;

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPCON_DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer angefragt.
 * IPCON_DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren Problems.
 * IPCON_DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon oder
   WIFI/Ethernet Extension eingeleitet.
