
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - IP Connection

.. _ipcon_shell:

Shell - IP Connection
=====================

Dies ist die API Beschreibung für die Shell Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden. Im Falle der Shell Bindings passiert dies
alles im Hintergrund, unsichtbar für den Benutzer.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_shell_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/de/source/Software/example.sh>`__

.. literalinclude:: example.sh
 :language: bash
 :linenos:
 :tab-width: 4


.. _ipcon_shell_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. sh:function:: tinkerforge

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. sh:function:: IPConnection.connect(host, port)

 :param host: str
 :param port: int
 :rtype: None

 Erstellt eine TCP/IP Verbindung zum gegebenen *host* und *port*. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. sh:function:: IPConnection.disconnect()

 :rtype: None

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. sh:function:: IPConnection.get_connection_state()

 :rtype: int

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. sh:function:: IPConnection.set_auto_reconnect(auto_reconnect)

 :param auto_reconnect: bool
 :rtype: None

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen, falls die Verbindung
 verloren geht.

 Standardwert ist *True*.


.. sh:function:: IPConnection.get_auto_reconnect()

 :rtype: bool

 Gibt *True* zurück wenn die Wiederverbindung aktiviert ist und *False* sonst.


.. sh:function:: IPConnection.set_timeout(timeout)

 :param timeout: float
 :rtype: None

 Setzt den Timeout in Sekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2,5.


.. sh:function:: IPConnection.get_timeout()

 :rtype: float

 Gibt den Timeout zurück, wie er von :sh:func:`set_timeout()
 <IPConnection.set_timeout>` gesetzt wurde.


.. sh:function:: IPConnection.enumerate()

 :rtype: None

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sh:function:: IPConnection.register_callback(id, callback)

 :param id: int
 :param callback: callable
 :rtype: None

 Registriert einen Callback für eine gegebene ID.

 Die verfügbaren IDs mit zugehörenden Callback-Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung kann mit der Funktion :sh:func:`register_callback()
<IPConnection.register_callback>` durchgeführt werden. Der erste Parameter
ist der Callback ID und der zweite die Callback Funktion:

.. code-block:: python

    def my_callback(param):
        print(param)

    ipcon.register_callback(IPConnection.CALLBACK_EXAMPLE, my_callback)

Die verfügbaren Konstanten mit der dazugehörigen Parameteranzahl und -typen
werden weiter unten beschrieben.


.. sh:attribute:: IPConnection.CALLBACK_ENUMERATE

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
 * *firmware_version*: Major, Minor und Release Nummer der Firmwareversion.
 * *device_identifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * *enumeration_type*: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst).
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Gerät ist neu verfügbar
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei
   USB-Verbindungen möglich). In diesem Fall haben nur *uid* und
   *enumeration_type* einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht)

 Die Device Identifiers sind :ref:`hier <device_identifier>` zu finden.
