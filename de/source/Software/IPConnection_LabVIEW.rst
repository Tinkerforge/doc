
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-labview">Software</a> / LabVIEW - IP Connection

.. |ref_api_bindings| replace:: :ref:`LabVIEW API Bindings <api_bindings_labview>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_labview_install>`
.. |bindings_name| replace:: LabVIEW

.. _ipcon_labview:

LabVIEW - IP Connection
=======================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_labview_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (Example Enumerate.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Enumerate.vi>`__,
`Download (Example Enumerate - EnumerateCallback Callback.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Enumerate%20-%20EnumerateCallback%20Callback.vi>`__

.. raw:: html

   <div class="horizontal-image-scroll">

.. image:: /Images/Screenshots/LabVIEW/IPConnection_LabVIEW_Example_Enumerate.vi.png
    :scale: 100 %
    :alt: LabVIEW Enumerate Beispiel
    :align: center

.. raw:: html

   </div>


Authenticate
^^^^^^^^^^^^

`Download (Example Authenticate.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Authenticate.vi>`__,
`Download (Example Authenticate - Connected Callback.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Authenticate%20-%20Connected%20Callback.vi>`__
`Download (Example Authenticate - EnumerateCallback Callback.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Authenticate%20-%20EnumerateCallback%20Callback.vi>`__

.. raw:: html

   <div class="horizontal-image-scroll">

.. image:: /Images/Screenshots/LabVIEW/IPConnection_LabVIEW_Example_Authenticate.vi.png
   :scale: 100 %
   :alt: LabVIEW Authenticate Beispiel
   :align: center

.. raw:: html

   </div>


.. _ipcon_labview_api:

API
---

Der Namensraum für IPConnection ist ``Tinkerforge.*``.

Grundfunktionen
^^^^^^^^^^^^^^^

.. labview:function:: IPConnection() -> ipcon

 :output ipcon: .NET Refnum (IPConnection)

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. labview:function:: IPConnection.Connect(host, port)

 :input host: String
 :input port: Int32

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. labview:function:: IPConnection.Disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. labview:function:: IPConnection.Authenticate(secret)

 :input secret: String

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


.. labview:function:: IPConnection.GetConnectionState() -> connectionState

 :output connectionState: Byte

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. labview:function:: IPConnection.SetAutoReconnect(autoReconnect)

 :input autoReconnect: Boolean

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die Verbindung verloren geht.

 Standardwert ist *true*.


.. labview:function:: IPConnection.GetAutoReconnect() -> autoReconnect

 :output autoReconnect: Boolean

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. labview:function:: IPConnection.SetTimeout(timeout)

 :input timeout: Int32

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. labview:function:: IPConnection.GetTimeout() -> timeout

 :output timeout: Int32

 Gibt den Timeout zurück, wie er von :labview:func:`SetTimeout()
 <IPConnection.SetTimeout>` gesetzt wurde.


.. labview:function:: IPConnection.Enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. labview:function:: IPConnection.Wait()

 Hält den aktuellen Thread an bis :labview:func:`Unwait() <IPConnection.Unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


.. labview:function:: IPConnection.Unwait()

 Startet einen Thread der vorher mit :labview:func:`Wait() <IPConnection,Wait>`
 angehalten wurde wieder.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung geschieht durch Anhängen des Callback Handlers an den
passenden Event.
Die verfügbaren Events werden im Folgenden beschrieben.


.. labview:function:: event IPConnection.EnumerateCallback(sender, uid, connectedUid, position, hardwareVersion, firmwareVersion, deviceIdentifier, enumerationType)

 :input sender: .NET Refnum (IPConnection)
 :input uid: String
 :input connectedUid: String
 :input position: Char
 :input hardwareVersion: Byte[3]
 :input firmwareVersion: Byte[3]
 :input deviceIdentifier: Int32
 :input enumerationType: Int16

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
   (Enumerierung vom Benutzer ausgelöst: :labview:func:`Enumerate()
   <IPConnection.Enumerate>`). Diese Enumerierungsart kann mehrfach für das
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

 Zum Beispiel: :labview:sym:`BrickMaster.DEVICE_IDENTIFIER <BrickMaster.DEVICE_IDENTIFIER>`
 oder :labview:sym:`BrickletAmbientLight.DEVICE_IDENTIFIER <BrickletAmbientLight.DEVICE_IDENTIFIER>`.


.. labview:function:: event IPConnection.Connected(sender, connectReason)

 :input sender: .NET Refnum (IPConnection)
 :input connectReason: Int16

 Dieser Event wird ausgelöst wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut durch
   Auto-Reconnect.


.. labview:function:: event IPConnection.Disconnected(sender, disconnectReason)

 :input sender: .NET Refnum (IPConnection)
 :input disconnectReason: Int16

 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
