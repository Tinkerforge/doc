
.. |ref_api_bindings| replace:: :ref:`JavaScript API Bindings <api_bindings_javascript>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_javascript_install>`
.. |bindings_name| replace:: JavaScript

.. _ipcon_javascript:

JavaScript - IP Connection
==========================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_javascript_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate (Node.js)
^^^^^^^^^^^^^^^^^^^

`Download (ExampleEnumerate.js) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleEnumerate.js>`__

.. literalinclude:: IPConnection_JavaScript_ExampleEnumerate.js
 :language: javascript
 :linenos:
 :tab-width: 4

Authenticate (Node.js)
^^^^^^^^^^^^^^^^^^^^^^

`Download (ExampleAuthenticate.js) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleAuthenticate.js>`__

.. literalinclude:: IPConnection_JavaScript_ExampleAuthenticate.js
 :language: javascript
 :linenos:
 :tab-width: 4

Enumerate (HTML)
^^^^^^^^^^^^^^^^

`Download (ExampleEnumerate.html) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleEnumerate.html>`__,
`Test (ExampleEnumerate.html) <https://www.tinkerforge.com/de/doc/Software/Examples/JavaScript/IPConnection_JavaScript_ExampleEnumerate.html>`__

.. literalinclude:: IPConnection_JavaScript_ExampleEnumerate.html
 :language: html
 :linenos:
 :tab-width: 4

Authenticate (HTML)
^^^^^^^^^^^^^^^^^^^

`Download (ExampleAuthenticate.html) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleAuthenticate.html>`__,
`Test (ExampleAuthenticate.html) <https://www.tinkerforge.com/de/doc/Software/Examples/JavaScript/IPConnection_JavaScript_ExampleAuthenticate.html>`__

.. literalinclude:: IPConnection_JavaScript_ExampleAuthenticate.html
 :language: html
 :linenos:
 :tab-width: 4


.. _ipcon_javascript_api:

API
---

Allgemein kann jede Methode der JavaScript Bindings zwei optionale Parameter
haben, ``returnCallback`` und ``errorCallback``. Dies sind benutzerdefinierte
Callback-Funktionen. Der ``returnCallback`` wird aufgerufen mit den
Rückgabewerten der Methode, sofern vorhanden. Der ``errorCallback`` wird im
Fehlerfall mit einem Fehlercode aufgerufen. Der Fehlercode kann einer der
folgenden Werte sein:

* IPConnection.ERROR_ALREADY_CONNECTED = 11
* IPConnection.ERROR_NOT_CONNECTED = 12
* IPConnection.ERROR_CONNECT_FAILED = 13
* IPConnection.ERROR_INVALID_FUNCTION_ID = 21
* IPConnection.ERROR_TIMEOUT = 31
* IPConnection.ERROR_INVALID_PARAMETER = 41
* IPConnection.ERROR_FUNCTION_NOT_SUPPORTED = 42
* IPConnection.ERROR_UNKNOWN_ERROR = 43

Der Namespace der JavaScript Bindings ist ``Tinkerforge.*``.

Grundfunktionen
^^^^^^^^^^^^^^^

.. javascript:function:: new IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. javascript:function:: IPConnection.connect(host, port, [errorCallback])

 :param host: string
 :param port: int

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.


.. javascript:function:: IPConnection.disconnect([errorCallback])

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. javascript:function:: IPConnection.authenticate(secret, [returnCallback], [errorCallback])

 :param secret: string
 :noreturn: undefined

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


.. javascript:function:: IPConnection.getConnectionState()

 :rtype: int

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. javascript:function:: IPConnection.setAutoReconnect(autoReconnect)

 :param auto_reconnect: boolean

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :javascript:func:`connect() <IPConnection.connect>`.

 Standardwert ist *true*.


.. javascript:function:: IPConnection.getAutoReconnect()

 :rtype: boolean

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. javascript:function:: IPConnection.setTimeout(timeout)

 :param timeout: int

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. javascript:function:: IPConnection.getTimeout()

 :rtype: int

 Gibt den Timeout zurück, wie er von :javascript:func:`setTimeout()
 <IPConnection.setTimeout>` gesetzt wurde.


.. javascript:function:: IPConnection.enumerate([errorCallback])

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit einem
 Enumerate Callback antworten.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. javascript:function:: IPConnection.on(callback_id, function)

 :param callback_id: int
 :param function: function

 Registriert die ``function`` für die gegebene ``callback_id``.

 Die verfügbaren Callback IDs mit zugehörenden Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung wird mit der Funktion :javascript:func:`on() <IPConnection.on>`
durchgeführt. Die Parameter bestehen aus dem IP Connection Objekt, der
Callback ID, der Callback Funktion und optionalen Benutzer Daten:

.. code-block:: javascript

    ipcon.on(IPConnection.CALLBACK_EXAMPLE,
        function (param) {
            console.log(param);
        }
    );

Die verfügbaren IDs mit den zugehörigen Callback Funktionssignaturen
werden weiter unten beschrieben.


.. javascript:attribute:: IPConnection.CALLBACK_ENUMERATE

 :param uid: string
 :param connectedUid: string
 :param position: char
 :param hardwareVersion: [int, int, int]
 :param firmwareVersion: [int, int, int]
 :param deviceIdentifier: int
 :param enumerationType: int

 Der Callback empfängt sieben Parameter:

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
   (Enumerierung vom Benutzer ausgelöst: :javascript:func:`enumerate()
   <IPConnection.enumerate>`). Diese Enumerierungsart kann mehrfach für das
   selbe Gerät auftreten.
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>.DEVICE_IDENTIFIER

 Zum Beispiel: :javascript:attr:`Master.DEVICE_IDENTIFIER`
 oder :javascript:attr:`AmbientLight.DEVICE_IDENTIFIER`.


.. javascript:attribute:: IPConnection.CALLBACK_CONNECTED

 :param connectReason: int

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut durch
   Auto-Reconnect.


.. javascript:attribute:: IPConnection.CALLBACK_DISCONNECTED

 :param disconnectReason: int

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
