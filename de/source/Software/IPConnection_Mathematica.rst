
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Mathematica - IP Connection

.. |ref_api_bindings| replace:: :ref:`Mathematica Bindings <api_bindings_mathematica>`

.. _ipcon_mathematica:

Mathematica - IP Connection
===========================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_mathematica_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.nb) <https://github.com/Tinkerforge/generators/raw/master/mathematica/ExampleEnumerate.nb>`__

.. literalinclude:: IPConnection_Mathematica_ExampleEnumerate.nb.txt
 :language: mathematica
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.nb) <https://github.com/Tinkerforge/generators/raw/master/mathematica/ExampleAuthenticate.nb>`__

.. literalinclude:: IPConnection_Mathematica_ExampleAuthenticate.nb.txt
 :language: mathematica
 :linenos:
 :tab-width: 4


.. _ipcon_mathematica_api:

API
---

Der Namensraum für IPConnection ist ``Tinkerforge.*``.

Grundfunktionen
^^^^^^^^^^^^^^^

.. mathematica:function:: IPConnection[] -> ipcon

 :ret ipcon: NETObject[IPConnection]

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.

 .. code-block:: mathematica

    ipcon=NETNew["Tinkerforge.IPConnection"]

 Die .NET Runtime hat eingebauten Garbage Collection welche Objekte wieder
 freigibt, wenn sie vom Programm nicht mehr verwendet werden. Da Mathematica
 aber selbst nicht automatisch feststellen kann, wann ein Mathematica "Programm"
 ein .NET Objekt nicht mehr verwendet, muss sich das Programm selbst darum
 kümmern. Für diesen Zweck wird die `ReleaseNETObject[]
 <http://reference.wolfram.com/mathematica/NETLink/ref/ReleaseNETObject.html>`__
 Funktion in den Beispielen verwendet.

 Weitere Informationen über Objekt-Verwaltung mittels .NET/Link sind in der
 entsprechende Mathematica `.NET/Link Dokumentation
 <http://reference.wolfram.com/mathematica/NETLink/tutorial/CallingNETFromMathematica.html#14400>`__
 zu finden.


.. mathematica:function:: IPConnection@Connect[host, port] -> Null

 :param host: String
 :param port: Integer

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. mathematica:function:: IPConnection@Disconnect[] -> Null

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. mathematica:function:: IPConnection@Authenticate[secret] -> Null

 :param secret: String

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


.. mathematica:function:: IPConnection@GetConnectionState[] -> connectionState

 :ret connectionState: Integer

 Kann die folgenden Zustände zurückgeben:

 * IPConnection`CONNECTIONUSTATEUDISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection`CONNECTIONUSTATEUCONNECTED (1): Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection`CONNECTIONUSTATEUPENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. mathematica:function:: IPConnection@SetAutoReconnect[autoReconnect] -> Null

 :param autoReconnect: True/False

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die Verbindung verloren geht.

 Standardwert ist *True*.


.. mathematica:function:: IPConnection@GetAutoReconnect[] -> autoReconnect

 :ret autoReconnect: True/False

 Gibt *True* zurück wenn Auto-Reconnect aktiviert ist und *False* sonst.


.. mathematica:function:: IPConnection@SetTimeout[timeout] -> Null

 :param timeout: Integer

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. mathematica:function:: IPConnection@GetTimeout[] -> timeout

 :param timeout: Integer

 Gibt den Timeout zurück, wie er von :mathematica:func:`SetTimeout[] <IPConnection@SetTimeout>`
 gesetzt wurde.


.. mathematica:function:: IPConnection@Enumerate[] -> Null

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. mathematica:function:: IPConnection@Wait[] -> Null

 Hält den aktuellen Thread an bis :mathematica:func:`Unwait[] <IPConnection@Unwait>`
 aufgerufen wird.

 Dies ist nützlich falls ausschließlich auf Callbacks reagiert werden soll oder
 wenn auf einen spezifischen Callback gewartet werden soll oder wenn die
 IP Connection in einem Thread gestartet wird.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


.. mathematica:function:: IPConnection@Unwait[] -> Null

 Startet einen Thread der vorher mit :mathematica:func:`Wait[] <IPConnection@Wait>`
 angehalten wurde wieder.

 ``Wait`` und ``Unwait`` agieren auf die gleiche Weise wie ``Acquire`` und
 ``Release`` einer Semaphore.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung geschieht durch Anhängen des Callback Handlers an den
passenden Event:

.. code-block:: mathematica

    Callback[sender_,value_]:=Print["Value: "<>ToString[value]]

    AddEventHandler[ipcon@Example,Callback]

Weitere Informationen über Event-Behandlung mittels .NET/Link sind in der
entsprechende Mathematica `.NET/Link Dokumentation
<http://reference.wolfram.com/mathematica/NETLink/tutorial/CallingNETFromMathematica.html#17034>`__
zu finden.

Die verfügbaren Events werden im Folgenden beschrieben.


.. mathematica:function:: event IPConnection@EnumerateCallback[sender, uid, connectedUid, position, {hardwareVersion1, hardwareVersion2, hardwareVersion3}, {firmwareVersion1, firmwareVersion2, firmwareVersion3}, deviceIdentifier, enumerationType]

 :param sender: NETObject[IPConnection]
 :param uid: String
 :param connectedUid: String
 :param position: Integer
 :param hardwareVersioni: Integer
 :param firmwareVersioni: Integer
 :param deviceIdentifier: Integer
 :param enumerationType: Integer

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

 * IPConnection`ENUMERATIONUTYPEUAVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst).
 * IPConnection`ENUMERATIONUTYPEUCONNECTED (1): Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection`ENUMERATIONUTYPEUDISCONNECTED (2): Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und
   ``enumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Event
 zu implementieren (wie es im Brick Viewer geschieht).

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>`DEVICEUIDENTIFIER

 Zum Beispiel: :mathematica:sym:`BrickMaster`DEVICEUIDENTIFIER <BrickMaster`DEVICEUIDENTIFIER>`
 oder :mathematica:sym:`BrickletAmbientLight`DEVICEUIDENTIFIER <BrickletAmbientLight`DEVICEUIDENTIFIER>`.


.. mathematica:function:: event IPConnection@Connected[sender, connectReason]

 Dieser Event wird ausgelöst wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection`CONNECTUREASONUREQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection`CONNECTUREASONUAUTOURECONNECT (1): Verbindung aufgebaut durch
   Auto-Reconnect.


.. mathematica:function:: event IPConnection@Disconnected[sender, disconnectReason]

 Dieser Event wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection`DISCONNECTUREASONUREQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection`DISCONNECTUREASONUERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection`DISCONNECTUREASONUSHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
