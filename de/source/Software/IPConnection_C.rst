
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-c">Software</a> / C/C++ - IP Connection

.. |ref_api_bindings| replace:: :ref:`C/C++ Bindings <api_bindings_c>`

.. _ipcon_c:

C/C++ - IP Connection
=====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_c_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.c) <https://github.com/Tinkerforge/generators/raw/master/c/example_enumerate.c>`__

.. literalinclude:: IPConnection_C_example_enumerate.c
 :language: c
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.c) <https://github.com/Tinkerforge/generators/raw/master/c/example_authenticate.c>`__

.. literalinclude:: IPConnection_C_example_authenticate.c
 :language: c
 :linenos:
 :tab-width: 4


.. _ipcon_c_api:

API
---

Jede Funktion der C/C++ Bindings gibt einen Integer zurück, welcher einen
Fehlercode beschreibt.

Mögliche Fehlercodes sind:

* E_OK = 0
* E_TIMEOUT = -1
* E_NO_STREAM_SOCKET = -2
* E_HOSTNAME_INVALID = -3
* E_NO_CONNECT = -4
* E_NO_THREAD = -5
* E_NOT_ADDED = -6 (seit Bindings Version 2.0.0 nicht mehr verwendet)
* E_ALREADY_CONNECTED = -7
* E_NOT_CONNECTED = -8
* E_INVALID_PARAMETER = -9
* E_NOT_SUPPORTED = -10
* E_UNKNOWN_ERROR_CODE = -11

wie in :file:`ip_connection.h` definiert.


Grundfunktionen
^^^^^^^^^^^^^^^

.. c:function:: void ipcon_create(IPConnection *ipcon)

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. c:function:: void ipcon_destroy(IPConnection *ipcon)

 Zerstört die IP Connection. Ruft intern :c:func:`ipcon_disconnect` auf. Der
 Socket zum Brick Daemon wird geschlossen und alle Threads der IP Connection
 werden beendet.


.. c:function:: int ipcon_connect(IPConnection *ipcon, const char *host, uint16_t port)

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und gibt einen Fehlercode zurück
 falls kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen
 Host und Port horcht.


.. c:function:: int ipcon_disconnect(IPConnection *ipcon)

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. c:function:: int ipcon_authenticate(IPConnection *ipcon, const char *secret)

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


.. c:function:: int ipcon_get_connection_state(IPConnection *ipcon)

 Kann die folgenden Zustände zurückgeben:

 * IPCON_CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPCON_CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon oder
   der WIFI/Ethernet Extension ist aufgebaut.
 * IPCON_CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment eine
   Verbindung aufzubauen.


.. c:function:: void ipcon_set_auto_reconnect(IPConnection *ipcon, bool auto_reconnect)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die Verbindung verloren geht.

 Standardwert ist *true*.


.. c:function:: bool ipcon_get_auto_reconnect(IPConnection *ipcon)

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. c:function:: void ipcon_set_timeout(IPConnection *ipcon, uint32_t timeout)

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. c:function:: uint32_t ipcon_get_timeout(IPConnection *ipcon)

 Gibt den Timeout zurück, wie er von :c:func:`ipcon_set_timeout` gesetzt wurde.


.. c:function:: int ipcon_enumerate(IPConnection *ipcon)

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. c:function:: void ipcon_wait(IPConnection *ipcon)

 Hält den aktuellen Thread an bis :c:func:`ipcon_unwait`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``wait`` und ``unwait`` agieren auf die gleiche Weise wie ``acquire`` und
 ``release`` einer Semaphore.


.. c:function:: void ipcon_unwait(IPConnection *ipcon)

 Startet einen Thread der vorher mit :c:func:`ipcon_wait`
 angehalten wurde wieder.

 ``wait`` und ``unwait`` agieren auf die gleiche Weise wie ``acquire`` und
 ``release`` einer Semaphore.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. c:function:: void ipcon_register_callback(IPConnection *ipcon, uint8_t id, void *callback, void *user_data)

 Registriert einen Callback für eine gegebene ID.

 Die verfügbaren IDs mit zugehörenden Callback Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung wird mit der Funktion :c:func:`ipcon_register_callback`
durchgeführt. Die Parameter bestehen aus dem IP Connection Objekt, der
Callback ID, der Callback Funktion und optionalen Benutzer Daten:

.. code-block:: c

    void my_callback(int p, void *user_data) {
        printf("parameter: %d\n", p);
    }

    ipcon_register_callback(&ipcon, IPCON_CALLBACK_EXAMPLE, (void*)my_callback, NULL);

Die verfügbaren IDs mit den zugehörigen Callback Funktionssignaturen
werden weiter unten beschrieben.


.. c:var:: IPCON_CALLBACK_ENUMERATE

 .. code-block:: c

  void callback(const char *uid, const char *connected_uid, char position, uint8_t hardware_version[3], uint8_t firmware_version[3], uint16_t device_identifier, uint8_t enumeration_type, void *user_data)

 Der Callback empfängt sieben Parameter:

 * ``uid``: Die UID des Bricks/Bricklets.
 * ``connected_uid``: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``position``: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'd' (Position an Brick).
 * ``hardware_version``: Major, Minor und Release Nummer der Hardwareversion.
 * ``firmware_version``: Major, Minor und Release Nummer der Firmwareversion.
 * ``device_identifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * ``enumeration_type``: Art der Enumerierung

 Mögliche Enumerierungsarten sind:

 * IPCON_ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar (Enumerierung vom
   Benutzer ausgelöst).
 * IPCON_ENUMERATION_TYPE_CONNECTED (1): Gerät wurde neu verbunden (Automatisch
   vom Brick gesendet nachdem die Kommunikation aufgebaut wurde). Dies kann
   bedeuten, dass das Gerät die vorher eingestellte Konfiguration verloren hat
   und neu konfiguriert werden muss.
 * IPCON_ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei
   USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumeration_type`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-type>_DEVICE_IDENTIFIER

 Zum Beispiel: :c:data:`MASTER_DEVICE_IDENTIFIER`
 oder :c:data:`AMBIENT_LIGHT_DEVICE_IDENTIFIER`.


.. c:var:: IPCON_CALLBACK_CONNECTED

 .. code-block:: c

  void callback(uint8_t connect_reason, void *user_data)

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPCON_CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage vom Benutzer.
 * IPCON_CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach durch
   Auto-Reconnect.


.. c:var:: IPCON_CALLBACK_DISCONNECTED

 .. code-block:: c

  void callback(uint8_t disconnect_reason, void *user_data)

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPCON_DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer angefragt.
 * IPCON_DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren Problems.
 * IPCON_DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon oder
   WIFI/Ethernet Extension eingeleitet.
