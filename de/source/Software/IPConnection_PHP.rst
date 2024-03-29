
.. |ref_api_bindings| replace:: :ref:`PHP API Bindings <api_bindings_php>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_php_install>`
.. |bindings_name| replace:: PHP

.. _ip_connection_php:

PHP - IP Connection
===================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ip_connection_php_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.php) <https://github.com/Tinkerforge/generators/raw/master/php/ExampleEnumerate.php>`__

.. literalinclude:: IPConnection_PHP_ExampleEnumerate.php
 :language: php
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.php) <https://github.com/Tinkerforge/generators/raw/master/php/ExampleAuthenticate.php>`__

.. literalinclude:: IPConnection_PHP_ExampleAuthenticate.php
 :language: php
 :linenos:
 :tab-width: 4


.. _ip_connection_php_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. php:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. php:function:: void IPConnection::connect(string $host, int $port)

 Erstellt eine TCP/IP Verbindung zum gegebenen ``$host`` und ``$port``. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. php:function:: void IPConnection::disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. php:function:: void IPConnection::authenticate(string $secret)

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


.. php:function:: int IPConnection::getConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * IPConnection::\ **CONNECTION_STATE**\ _DISCONNECTED = 0: Keine Verbindung aufgebaut.
 * IPConnection::\ **CONNECTION_STATE**\ _CONNECTED = 1: Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.


.. php:function:: void IPConnection::setTimeout(float $seconds)

 Setzt den Timeout in Sekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2,5.


.. php:function:: int IPConnection::getTimeout()

 Gibt den Timeout zurück, wie er von :php:func:`setTimeout()
 <IPConnection::setTimeout>` gesetzt wurde.


.. php:function:: void IPConnection::enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


.. php:function:: void IPConnection::dispatchCallbacks(float $seconds)

 Liefert eingehende Callbacks für die gegebene Dauer in Sekunden aus (negative
 Werte bedeuten unendlich). Da PHP keine Threads unterstützt muss diese Methode
 periodisch aufgerufen werden, um sicherzustellen, dass eingehende Callbacks
 behandelt werden. Falls keine Callbacks benutzt werden braucht diese Methode
 nicht aufgerufen zu werden.

 Die empfohlene Auslieferungsdauer ist 0. Dadurch werden nur die Callbacks
 ausgeliefert die noch auf Auslieferung warten. Es wird jedoch nicht auf den
 Eingang weitere Callbacks gewartet.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. php:function:: void IPConnection::registerCallback(int $callback_id, callable $function, mixed $user_data = NULL)

 Registriert die ``$function`` für die gegebene ``$callback_id``. Die optionalen
 ``$user_data`` werden der Funktion als letztes Parameter mit übergeben.

 Die verfügbaren Callback IDs mit zugehörenden Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung wird mit der Funktion :php:func:`registerCallback()
<IPConnection::registerCallback>` durchgeführt. Die Parameter bestehen aus der
Callback ID, der Callback Funktion und optionalen Benutzer Daten:

.. code-block:: php

    <?php

    function my_callback($param)
    {
        echo $param . "\n";
    }

    $ipcon->registerCallback(IPConnection::CALLBACK_EXAMPLE, 'my_callback');

    ?>

Die verfügbaren Konstanten mit den zugehörigen Callback Funktionssignaturen
werden im Folgenden beschrieben.


.. php:member:: int IPConnection::CALLBACK_ENUMERATE

 .. code-block:: php

  <?php   void callback(string $uid, string $connectedUid, char $position, array $hardwareVersion, array $firmwareVersion, int $deviceIdentifier, int $enumerationType [, mixed $userData])   ?>

 Der Callback empfängt sieben Parameter:

 * ``$uid``: Die UID des Bricks/Bricklets.
 * ``$connectedUid``: Die UID des Gerätes mit dem der Brick/das Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks oder Bricklets mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Bricks im Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``$position``: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'h' (Position an Brick) oder 'i' (Position des Raspberry Pi (Zero) HAT)
   oder 'z' (Bricklet an :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``$hardwareVersion``: Major, Minor und Release Nummer der Hardwareversion.
 * ``$firmwareVersion``: Major, Minor und Release Nummer der Firmwareversion.
 * ``$deviceIdentifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * ``$enumerationType``: Art der Enumerierung

 Mögliche Enumerierungsarten sind:

 * IPConnection::\ **ENUMERATION_TYPE**\ _AVAILABLE = 0: Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst: :php:func:`enumerate()
   <IPConnection::enumerate>`). Diese Enumerierungsart kann mehrfach für das
   selbe Gerät auftreten.
 * IPConnection::\ **ENUMERATION_TYPE**\ _CONNECTED = 1: Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu Konfiguriert werden muss.
 * IPConnection::\ **ENUMERATION_TYPE**\ _DISCONNECTED = 2: Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur ``$uid`` und
   ``$enumerationType`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht)

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>::DEVICE_IDENTIFIER

 Zum Beispiel: :php:member:`BrickMaster::DEVICE_IDENTIFIER`
 oder :php:member:`BrickletAmbientLight::DEVICE_IDENTIFIER`.


.. php:member:: int IPConnection::CALLBACK_CONNECTED

 .. code-block:: php

  <?php   void callback(int $connectReason [, mixed $userData])   ?>

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection::\ **CONNECT_REASON**\ _REQUEST = 0: Verbindung aufgebaut nach Anfrage
   vom Benutzer.


.. php:member:: int IPConnection::CALLBACK_DISCONNECTED

 .. code-block:: php

  <?php   void callback(int $disconnectReason [, mixed $userData])   ?>

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection::\ **DISCONNECT_REASON**\ _REQUEST = 0: Trennung wurde vom Benutzer
   angefragt.
 * IPConnection::\ **DISCONNECT_REASON**\ _ERROR = 1: Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection::\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
