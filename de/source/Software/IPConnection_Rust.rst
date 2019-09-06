
.. |ref_api_bindings| replace:: :ref:`Rust API Bindings <api_bindings_rust>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_rust_install>`
.. |bindings_name| replace:: Rust

.. _ipcon_rust:

Rust - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_rust_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.rs) <https://raw.githubusercontent.com/Tinkerforge/generators/master/rust/example_enumerate.rs>`__

.. literalinclude:: IPConnection_Rust_example_enumerate.rs
 :language: rust
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.rs) <https://raw.githubusercontent.com/Tinkerforge/generators/master/rust/example_authenticate.rs>`__

.. literalinclude:: IPConnection_Rust_example_authenticate.rs
 :language: rust
 :linenos:
 :tab-width: 4


.. _ipcon_rust_api:

API
---

Die IPConnection ist im Modul ``tinkerforge::ip_connection`` definiert.

Grundfunktionen
^^^^^^^^^^^^^^^

.. rust:function:: IpConnection::new() -> IpConnection

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.

.. rust:function:: IpConnection::get_request_sender(&self) -> IpConnectionRequestSender

 Die IP-Connection kann nicht mit anderen Threads geteilt werden. Um in solchen dennoch die
 Funktionalität der IP-Connection nutzen zu können, kann mit dieser Methode ein IP-Connection-Request-Sender
 erstellt werden, der die selben Methoden zur Verfügung stellt. Besitzer der Verbindung bleibt die IP-Connection, sodass die Request-Sender-Objekte beliebig erzeugt, geklont, an andere Threads übergeben und zerstört werden können.

.. rust:function:: IpConnection::connect<T: ToSocketAddrs>(&self, addr: T) -> Receiver<Result<(), ConnectError>>

 Erstellt eine TCP/IP Verbindung zur gegebenen ``addr``, die `ToSocketAddrs <https://doc.rust-lang.org/std/net/trait.ToSocketAddrs.html>`_ implementiert. Zum Beispiel kann ein Tupel ``(host, port)``, bei dem ``host`` ein String (eine IP-Addresse oder ein Hostname) und ``port`` ein ``u16`` sind, verwendet werden. Host und Port können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Gibt einen Receiver zurück, der entweder ``()`` oder, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht, einen ``ConnectError`` empfängt.


.. rust:function:: IpConnection::disconnect(&self) -> Receiver<Result<(), DisconnectErrorNotConnected>>

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension. Gibt einen Receiver zurück, der entweder ``()`` oder, falls keine Verbindung bestand, einen Fehler empfängt.


.. rust:function:: IpConnection::authenticate(&self, secret: &str) -> Result<ConvertingReceiver<()>, AuthenticateError>

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


.. rust:function:: IpConnection::get_connection_state(&self) -> ConnectionState

 Kann die folgenden Zustände zurückgeben:

 * **ConnectionState**\ ::Disconnected = 0: Keine Verbindung aufgebaut.
 * **ConnectionState**\ ::Connected = 1: Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * **ConnectionState**\ ::Pending = 2: IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. rust:function:: IpConnection::set_auto_reconnect(&mut self, auto_reconnect_enabled: bool)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :rust:func:`connect() <IpConnection::connect>`.

 Standardwert ist *true*.


.. rust:function:: IpConnection::get_auto_reconnect(&self) -> bool

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. rust:function:: IpConnection::set_timeout(&mut self, timeout: std::time::Duration)

 Setzt den Timeout für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500 ms.


.. rust:function:: IpConnection::get_timeout(&self) -> std::time::Duration

 Gibt den Timeout zurück, wie er von :rust:func:`set_timeout() <IpConnection::set_timeout>`
 gesetzt wurde.


.. rust:function:: IpConnection::enumerate(&self)

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung geschieht durch das Erstellen eines Receivers für die Nachrichten des Callbacks.
Empfangene Nachrichten können in einem neuen Thread asynchron verarbeitet werden:

.. code-block:: rust

    let receiver = ipcon.get_example_callback_receiver();
    // No join is needed here, as the iteration over the receiver ends when the ipcon is dropped.
    thread::spawn(move || {
        for value in receiver {
            println!("Value: {:?}", value);
        }
    };

Die verfügbaren Events werden im Folgenden beschrieben.


.. rust:function:: IpConnection::get_enumerate_callback_receiver(&self) -> ConvertingCallbackReceiver<EnumerateResponse>

 Der Event empfängt eine Struktur mit sieben Feldern:

 * ``uid``: Die UID des Bricks/Bricklets.
 * ``connected_uid``: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``position``: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'h' (Position an Brick) oder 'i' (Position des Raspberry Pi (Zero) HAT)
   oder 'z' (Bricklet an :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardware_version``: Major, Minor und Release Nummer der Hardwareversion.
 * ``firmware_version``: Major, Minor und Release Nummer der Firmwareversion.
 * ``device_identifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * ``enumeration_type``: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * **EnumerationType**\ ::Available = 0: Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst: :rust:func:`enumerate()
   <IpConnection::enumerate>`). Diese Enumerierungsart kann mehrfach für das
   selbe Gerät auftreten.
 * **EnumerationType**\ ::Connected = 1: Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * **EnumerationType**\ ::Disconnected = 2: Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Event
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>::DEVICE_IDENTIFIER

 Zum Beispiel: ::rust:const:`MasterBrick::DEVICE_IDENTIFIER`
 oder :rust:const:`AmbientLightBricklet::DEVICE_IDENTIFIER`.

.. rust:function:: IpConnection::get_connect_callback_receiver(&self) -> Receiver<ConnectReason>

 Dieser Event wird ausgelöst wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * **ConnectReason**\ ::Request = 0: Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * **ConnectReason**\ ::AutoReconnect = 1: Verbindung aufgebaut durch
   Auto-Reconnect.


.. rust:function:: IpConnection::get_disconnect_callback_receiver(&self) -> Receiver<DisconnectReason>

 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * **DisconnectReason**\ ::Request = 0: Trennung wurde vom Benutzer
   angefragt.
 * **DisconnectReason**\ ::Error = 1: Trennung aufgrund eines unlösbaren
   Problems.
 * **DisconnectReason**\ ::Shutdown = 2: Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
