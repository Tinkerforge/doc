
.. |ref_api_bindings| replace:: :ref:`Go API bindings <api_bindings_go>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_go_install>`
.. |bindings_name| replace:: Go

.. _ipcon_go:

Go - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_go_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.go) <https://raw.githubusercontent.com/Tinkerforge/generators/master/go/example_enumerate.go>`__

.. literalinclude:: IPConnection_Go_example_enumerate.go
 :language: go
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.go) <https://raw.githubusercontent.com/Tinkerforge/generators/master/go/example_authenticate.go>`__

.. literalinclude:: IPConnection_Go_example_authenticate.go
 :language: go
 :linenos:
 :tab-width: 4


.. _ipcon_go_api:

API
---

Die IP Connection ist im Package ``github.com/Tinkerforge/go-api-bindings/ipconnection`` definiert.

Grundfunktionen
^^^^^^^^^^^^^^^

.. go:function:: func ipconnection.NewIPConnection() (ipcon IPConnection)

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.

.. go:function:: func (*IPConnection) Close()

 Zerstört diese IP Connection und beendet deren interne Go-Routinen.

.. go:function:: func (*IPConnection) Connect(addr string) (err error)

 Erstellt eine TCP/IP Verbindung zur gegebenen ``addr`` in der Form "host:port", wie `hier <https://golang.org/pkg/net/#Dial>`_ beschrieben. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.


.. go:function:: func (*IPConnection) Disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.

.. go:function:: func (*IPConnection) Authenticate(secret string) (err error)

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


.. go:function:: func (*IPConnection) GetConnectionState() (state ConnectionState)

 Kann die folgenden Zustände zurückgeben:

 * ipconnection.\ **ConnectionState**\ Disconnected = 0: Keine Verbindung aufgebaut.
 * ipconnection.\ **ConnectionState**\ Connected = 1: Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * ipconnection.\ **ConnectionState**\ Pending = 2: IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. go:function:: func (*IPConnection) SetAutoReconnect(autoReconnectEnabled bool)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :go:func:`Connect() <(*IPConnection) Connect>`.

 Standardwert ist *true*.


.. go:function:: func (*IPConnection) GetAutoReconnect() (autoReconnect bool)

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. go:function:: func (*IPConnection) SetTimeout(timeout time.Duration)

 Setzt den Timeout für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500ms.


.. go:function:: func (*IPConnection) GetTimeout() (timeout time.Duration)

 Gibt den Timeout zurück, wie er von :go:func:`SetTimeout() <(*IPConnection) SetTimeout>` gesetzt wurde.


.. go:function:: func (*IPConnection) Enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit einem
 Enumerate Callback antworten.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung kann mit ``Register*Callback()`` Funktionen des IPConnection Objekts
durchgeführt werden. Zum Beispiel:

.. code-block:: go

    registrationId := ipcon.RegisterExampleCallback(func(param type) {
        fmt.Println(param)
    });

Die verfügbaren Ereignisse werden unterhalb beschrieben. Es ist möglich mehrere Callbacks
hinzuzufügen und auch mit einem korrespondierenden ``Deregister*Callback()``-Aufruf
wieder zu entfernen. Dieser erwartet eine Registrierungs-ID, die von ``Register*Callback()`` zurückgegeben wurde


.. go:function:: func (*IPConnection) RegisterEnumerateCallback(func(uid string, connectedUid string, position rune, hardwareVersion [3]uint8, firmwareVersion [3]uint8, deviceIdentifier uint16, enumerationType EnumerationType)) (registrationId uint64)

 Dieses Callback empfängt sieben Parameter:

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

 * ipconnection.\ **EnumerationType**\ Available = 0: Gerät ist verfügbar (Enumerierung
   vom Benutzer ausgelöst: :go:func:`Enumerate() <(*IPConnection) Enumerate>`).
   Diese Enumerierungsart kann mehrfach für das selbe Gerät auftreten.
 * ipconnection.\ **EnumerationType**\ Connected = 1: Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * ipconnection.\ **EnumerationType**\ Disconnected = 2: Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``UID`` und
   ``EnumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Listener zu implementieren (wie es im Brick Viewer geschieht).

  Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
  Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
  benannt sind::

  <device-package>.DeviceIdentifier

 Zum Beispiel: :go:const:`master_brick.DeviceIdentifier` oder :go:const:`ambient_light_bricklet.DeviceIdentifier`.


.. go:function:: func (*IPConnection) RegisterConnectCallback(func(reason ConnectReason)) (registrationId uint64)

 Dieses Callback wird aufgerufen wenn die IP Connection eine Verbindung zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat, mögliche Gründe sind:

 * ipconnection.\ **ConnectReason**\ Request = 0: Verbindung aufgebaut nach Anfrage vom Benutzer.
 * ipconnection.\ **ConnectReason**\ AutoReconnect = 1: Verbindung aufgebaut durch Auto-Reconnect.


.. go:function:: func (*IPConnection) RegisterDisconnectCallback(func(reason DisconnectReason)) (registrationId uint64)

 Dieses Callback wird aufgerufen wenn die Verbindung der IP Connection zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde, mögliche Gründe sind:

 * ipconnection.\ **DisconnectReason**\ Request = 0: Trennung wurde vom Benutzer angefragt.
 * ipconnection.\ **DisconnectReason**\ Error = 1: Trennung aufgrund eines unlösbaren Problems.
 * ipconnection.\ **DisconnectReason**\ Shutdown = 2: rennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
