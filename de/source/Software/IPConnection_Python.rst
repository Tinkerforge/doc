
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Python - IP Connection

.. |ref_api_bindings| replace:: :ref:`Python Bindings <api_bindings_python>`

.. _ipcon_python:

Python - IP Connection
======================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_python_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.py) <https://github.com/Tinkerforge/generators/raw/master/python/example_enumerate.py>`__

.. literalinclude:: IPConnection_Python_example_enumerate.py
 :language: python
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.py) <https://github.com/Tinkerforge/generators/raw/master/python/example_authenticate.py>`__

.. literalinclude:: IPConnection_Python_example_authenticate.py
 :language: python
 :linenos:
 :tab-width: 4


.. _ipcon_python_api:

API
---

Prinzipiell kann jede Funktion der Python Bindings
``tinkerforge.ip_connection.Error`` Exception werfen, welche ein ``value`` und
eine ``description`` Property hat. ``value`` kann verschiende Werte haben:

* Error.TIMEOUT = -1
* Error.ALREADY_CONNECTED = -7
* Error.NOT_CONNECTED = -8
* Error.INVALID_PARAMETER = -9
* Error.NOT_SUPPORTED = -10
* Error.UNKNOWN_ERROR_CODE = -11

Alle folgend aufgelisteten Funktionen sind Thread-sicher.

Grundfunktionen
^^^^^^^^^^^^^^^

.. py:function:: IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. py:function:: IPConnection.connect(host, port)

 :param host: str
 :param port: int
 :rtype: None

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. py:function:: IPConnection.disconnect()

 :rtype: None

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. py:function:: IPConnection.authenticate(secret)

 :param secret: str
 :rtype: None

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


.. py:function:: IPConnection.get_connection_state()

 :rtype: int

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. py:function:: IPConnection.set_auto_reconnect(auto_reconnect)

 :param auto_reconnect: bool
 :rtype: None

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die Verbindung verloren geht.

 Standardwert ist *True*.


.. py:function:: IPConnection.get_auto_reconnect()

 :rtype: bool

 Gibt *True* zurück wenn Auto-Reconnect aktiviert ist und *False* sonst.


.. py:function:: IPConnection.set_timeout(timeout)

 :param timeout: float
 :rtype: None

 Setzt den Timeout in Sekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2,5.


.. py:function:: IPConnection.get_timeout()

 :rtype: float

 Gibt den Timeout zurück, wie er von :py:func:`set_timeout()
 <IPConnection.set_timeout>` gesetzt wurde.


.. py:function:: IPConnection.enumerate()

 :rtype: None

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. py:function:: IPConnection.wait()

 :rtype: None

 Hält den aktuellen Thread an bis :py:func:`unwait() <IPConnection.unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``wait`` und ``unwait`` agieren auf die gleiche Weise wie ``acquire`` und
 ``release`` einer Semaphore.


.. py:function:: IPConnection.unwait()

 :rtype: None

 Startet einen Thread der vorher mit :py:func:`wait() <IPConnection.wait>`
 angehalten wurde wieder.

 ``wait`` und ``unwait`` agieren auf die gleiche Weise wie ``acquire`` und
 ``release`` einer Semaphore.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: IPConnection.register_callback(id, callback)

 :param id: int
 :param callback: callable
 :rtype: None

 Registriert einen Callback für eine gegebene ID.

 Die verfügbaren IDs mit zugehörenden Callback-Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung kann mit der Funktion :py:func:`register_callback()
<IPConnection.register_callback>` durchgeführt werden. Der erste Parameter
ist der Callback ID und der zweite die Callback Funktion:

.. code-block:: python

    def my_callback(param):
        print(param)

    ipcon.register_callback(IPConnection.CALLBACK_EXAMPLE, my_callback)

Die verfügbaren IDs mit der dazugehörigen Parameteranzahl und -typen
werden weiter unten beschrieben.


.. py:attribute:: IPConnection.CALLBACK_ENUMERATE

 :param uid: str
 :param connected_uid: str
 :param position: chr
 :param hardware_version: [int, int, int]
 :param firmware_version: [int, int, int]
 :param device_identifier: int
 :param enumeration_type: int

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
 * ``enumeration_type``: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst).
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei
   USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumeration_type`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht)

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>.DEVICE_IDENTIFIER

 Zum Beispiel: :py:attr:`Master.DEVICE_IDENTIFIER`
 oder :py:attr:`AmbientLight.DEVICE_IDENTIFIER`.


.. py:attribute:: IPConnection.CALLBACK_CONNECTED

 :param connect_reason: int

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut durch
   Auto-Reconnect.


.. py:attribute:: IPConnection.CALLBACK_DISCONNECTED

 :param disconnect_reason: int

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
