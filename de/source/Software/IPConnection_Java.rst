
.. |ref_api_bindings| replace:: :ref:`Java API Bindings <api_bindings_java>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_java_install>`
.. |bindings_name| replace:: Java

.. _ipcon_java:

Java - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_java_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.java) <https://github.com/Tinkerforge/generators/raw/master/java/ExampleEnumerate.java>`__

.. literalinclude:: IPConnection_Java_ExampleEnumerate.java
 :language: java
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.java) <https://github.com/Tinkerforge/generators/raw/master/java/ExampleAuthenticate.java>`__

.. literalinclude:: IPConnection_Java_ExampleAuthenticate.java
 :language: java
 :linenos:
 :tab-width: 4


.. _ipcon_java_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. java:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. java:function:: void IPConnection::connect(String host, int port)

 Erstellt eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. java:function:: void IPConnection::disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. java:function:: void IPConnection::authenticate(String secret)

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


.. java:function:: short IPConnection::getConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * IPConnection.\ **CONNECTION_STATE**\ _DISCONNECTED = 0: Keine Verbindung aufgebaut.
 * IPConnection.\ **CONNECTION_STATE**\ _CONNECTED = 1: Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection.\ **CONNECTION_STATE**\ _PENDING = 2: IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. java:function:: void IPConnection::setAutoReconnect(boolean autoReconnect)

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :java:func:`connect() <IPConnection::connect>`.

 Standardwert ist *true*.


.. java:function:: boolean IPConnection::getAutoReconnect()

 Gibt *true* zurück wenn Auto-Reconnect aktiviert ist und *false* sonst.


.. java:function:: void IPConnection::setTimeout(int timeout)

 Setzt den Timeout in Millisekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2500.


.. java:function:: int IPConnection::getTimeout()

 Gibt den Timeout zurück, wie er von :java:func:`setTimeout() <IPConnection::setTimeout>`
 gesetzt wurde.


.. java:function:: void IPConnection::enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit einem
 Enumerate Callback antworten.


Listener
^^^^^^^^

Listeners können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung kann mit "addListener" Funktionen des IPConnection Objekts
durchgeführt werden.

Der Parameter ist ein Listener Klassen Objekt, z.B.:

.. code-block:: java

    ipcon.addExampleListener(new IPConnection.ExampleListener() {
        public void property(int value) {
            System.out.println("Value: " + value);
        }
    });

Die verfügbaren Listener Klassen mit den Methoden welche überschrieben
werden können werden unterhalb beschrieben. Es ist möglich mehrere Listener
hinzuzufügen und auch mit einem korrespondierenden "removeListener"
wieder zu entfernen.


.. java:function:: class IPConnection::EnumerateListener()

 Dieser Listener kann mit der Funktion ``addEnumerateListener()`` hinzugefügt werde.
 Ein hinzugefügter Listener kann mit der Funktion ``removeEnumerateListener()`` wieder
 entfernt werden.

 .. java:function:: void enumerate(String uid, String connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)
  :noindex:

  Der Listener empfängt sieben Parameter:

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
    (Enumerierung vom Benutzer ausgelöst: :java:func:`enumerate()
    <IPConnection::enumerate>`). Diese Enumerierungsart kann mehrfach für
    das selbe Gerät auftreten.
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

  Zum Beispiel: :java:member:`BrickMaster.DEVICE_IDENTIFIER <BrickMaster::DEVICE_IDENTIFIER>`
  oder :java:member:`BrickletAmbientLight.DEVICE_IDENTIFIER <BrickletAmbientLight::DEVICE_IDENTIFIER>`.


.. java:function:: class IPConnection::ConnectedListener()

 Dieser Listener kann mit der Funktion ``addConnectedListener()`` hinzugefügt werde.
 Ein hinzugefügter Listener kann mit der Funktion ``removeConnectedListener()`` wieder
 entfernt werden.

 .. java:function:: void connected(short connectReason)
  :noindex:

  Dieser Listener wird aufgerufen wenn die IP Connection eine Verbindung
  zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
  mögliche Gründe sind:

  * IPConnection.\ **CONNECT_REASON**\ _REQUEST = 0: Verbindung aufgebaut nach Anfrage
    vom Benutzer.
  * IPConnection.\ **CONNECT_REASON**\ _AUTO_RECONNECT = 1: Verbindung aufgebaut durch
    Auto-Reconnect.


.. java:function:: class IPConnection::DisconnectedListener()

 Dieser Listener kann mit der Funktion ``addDisconnectedListener()`` hinzugefügt werde.
 Ein hinzugefügter Listener kann mit der Funktion ``removeDisconnectedListener()`` wieder
 entfernt werden.

 .. java:function:: void disconnected(short disconnectReason)
  :noindex:

  Dieser Listener wird aufgerufen wenn die Verbindung der IP Connection
  zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
  mögliche Gründe sind:

  * IPConnection.\ **DISCONNECT_REASON**\ _REQUEST = 0: Trennung wurde vom Benutzer
    angefragt.
  * IPConnection.\ **DISCONNECT_REASON**\ _ERROR = 1: Trennung aufgrund eines unlösbaren
    Problems.
  * IPConnection.\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Trennung wurde vom Brick Daemon
    oder WIFI/Ethernet Extension eingeleitet.
