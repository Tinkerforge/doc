
.. |ref_api_bindings| replace:: :ref:`MATLAB/Octave API Bindings <api_bindings_matlab>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_matlab_install>`
.. |bindings_name| replace:: MATLAB/Octave

.. _ip_connection_matlab:

MATLAB/Octave - IP Connection
=============================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ip_connection_matlab_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate (MATLAB)
^^^^^^^^^^^^^^^^^^

`Download (matlab_example_enumerate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/matlab_example_enumerate.m>`__

.. literalinclude:: IPConnection_MATLAB_matlab_example_enumerate.m
 :language: matlab
 :linenos:
 :tab-width: 4

Authenticate (MATLAB)
^^^^^^^^^^^^^^^^^^^^^

`Download (matlab_example_authenticate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/matlab_example_authenticate.m>`__

.. literalinclude:: IPConnection_MATLAB_matlab_example_authenticate.m
 :language: matlab
 :linenos:
 :tab-width: 4

Enumerate (Octave)
^^^^^^^^^^^^^^^^^^

`Download (octave_example_enumerate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/octave_example_enumerate.m>`__

.. literalinclude:: IPConnection_MATLAB_octave_example_enumerate.m
 :language: octave_fixed
 :linenos:
 :tab-width: 4

Authenticate (Octave)
^^^^^^^^^^^^^^^^^^^^^

`Download (octave_example_authenticate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/octave_example_authenticate.m>`__

.. literalinclude:: IPConnection_MATLAB_octave_example_authenticate.m
 :language: octave_fixed
 :linenos:
 :tab-width: 4


.. _ip_connection_matlab_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. matlab:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.

 In MATLAB:

 .. code-block:: matlab

  import com.tinkerforge.IPConnection;

  ipcon = IPConnection();

 In Octave:

 .. code-block:: octave

  ipcon = java_new("com.tinkerforge.IPConnection");


.. matlab:function:: void IPConnection::connect(String host, int port)

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und gibt einen Fehlercode zurück
 falls kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen
 Host und Port horcht.


.. matlab:function:: void IPConnection::disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. matlab:function:: void IPConnection::authenticate(String secret)

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


.. matlab:function:: byte IPConnection::getConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.\ **CONNECTION_STATE**\ _DISCONNECTED = 0: Keine Verbindung aufgebaut.
 * IPConnection.\ **CONNECTION_STATE**\ _CONNECTED = 1: Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.\ **CONNECTION_STATE**\ _PENDING = 2: IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. matlab:function:: void IPConnection::setAutoReconnect(boolean autoReconnect)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :matlab:func:`connect() <IPConnection::connect>`.

 Standardwert ist *true*.


.. matlab:function:: boolean IPConnection::getAutoReconnect()

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. matlab:function:: void IPConnection::setTimeout(int timeout)

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. matlab:function:: int IPConnection::getTimeout()

 Gibt den Timeout zurück, wie er von :matlab:func:`setTimeout()
 <IPConnection::setTimeout>` gesetzt wurde.


.. matlab:function:: void IPConnection::enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit einem
 Enumerate Callback antworten.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um zeitkritische oder wiederkehrende
Daten vom Gerät zu erhalten. Die Registrierung wird mit MATLABs "set"
Funktion durchgeführt. Die Parameter sind ein IP Connection Objekt, der
Callback-Name und die Callback-Funktion. Hier ein Beispiel in MATLAB:

.. code-block:: matlab

    function my_callback(e)
        fprintf('Parameter: %s\\n', e.param);
    end

    set(ipcon, 'ExampleCallback', @(h, e) my_callback(e));

Die Octave Java Unterstützung unterscheidet sich hier von MATLAB, die "set"
Funktion kann hier nicht verwendet werden. Die Registrierung wird in Octave
mit  "add*Callback" Funktionen des IP Connection Objekts durchgeführt. Hier
ein Beispiel in Octave:

.. code-block:: octave

    function my_callback(e)
        fprintf("Parameter: %s\\n", e.param);
    end

    ipcon.addExampleCallback(@my_callback);
    
Es ist möglich mehrere Callback-Funktion hinzuzufügen und auch mit einem
korrespondierenden "remove*Callback" wieder zu entfernen.

Die Parameter des Callbacks werden der Callback-Funktion als Felder der
Struktur ``e`` übergeben. Diese ist von der ``java.util.EventObject`` Klasse
abgeleitete. Die verfügbaren Callback-Namen mit den entsprechenden
Strukturfeldern werden unterhalb beschrieben.


.. matlab:member:: callback IPConnection::EnumerateCallback

 :param uid: String
 :param connectedUid: String
 :param position: char
 :param hardwareVersion: short[]
 :param firmwareVersion: short[]
 :param deviceIdentifier: int
 :param enumerationType: short

 Der Callback empfängt sieben Parameter als Felder er Struktur ``e``:

 * ``uid``: Die UID des Bricks/Bricklets.
 * ``connectedUid``: Die UID des Gerätes mit dem der Brick/das Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks oder Bricklets mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Bricks im Stapel.
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
   (Enumerierung vom Benutzer ausgelöst: :matlab:func:`enumerate()
   <IPConnection::enumerate>`). Diese Enumerierungsart kann mehrfach für das
   selbe Gerät auftreten.
 * IPConnection.\ **ENUMERATION_TYPE**\ _CONNECTED = 1: Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection.\ **ENUMERATION_TYPE**\ _DISCONNECTED = 2: Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Listener
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>.DEVICE_IDENTIFIER

 Zum Beispiel: :matlab:member:`BrickMaster.DEVICE_IDENTIFIER <BrickMaster::DEVICE_IDENTIFIER>`
 oder :matlab:member:`BrickletAmbientLight.DEVICE_IDENTIFIER <BrickletAmbientLight::DEVICE_IDENTIFIER>`.

 In MATLAB kann die ``set()`` Function verwendet werden um diesem Callback eine
 Callback-Function zuzuweisen.

 In Octave kann diesem Callback mit ``addEnumerateCallback()`` eine
 Callback-Function hinzugefügt werde. Eine hinzugefügter Callback-Function
 kann mit ``removeEnumerateCallback()`` wieder entfernt werden.


.. matlab:member:: callback IPConnection::ConnectedCallback

 :param connectReason: short

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection.\ **CONNECT_REASON**\ _REQUEST = 0: Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection.\ **CONNECT_REASON**\ _AUTO_RECONNECT = 1: Verbindung aufgebaut durch
   Auto-Reconnect.

 In MATLAB kann die ``set()`` Function verwendet werden um diesem Callback eine
 Callback-Function zuzuweisen.

 In Octave kann diesem Callback mit ``addConnectedCallback()`` eine
 Callback-Function hinzugefügt werde. Eine hinzugefügter Callback-Function
 kann mit ``removeConnectedCallback()`` wieder entfernt werden.


.. matlab:member:: callback IPConnection::DisconnectedCallback

 :param disconnectReason: short

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection.\ **DISCONNECT_REASON**\ _REQUEST = 0: Trennung wurde vom Benutzer
   angefragt.
 * IPConnection.\ **DISCONNECT_REASON**\ _ERROR = 1: Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection.\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.

 In MATLAB kann die ``set()`` Function verwendet werden um diesem Callback eine
 Callback-Function zuzuweisen.

 In Octave kann diesem Callback mit ``addDisconnectedCallback()`` eine
 Callback-Function hinzugefügt werde. Eine hinzugefügter Callback-Function
 kann mit ``removeDisconnectedCallback()`` wieder entfernt werden.
