
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / PHP - IP Connection

.. _ipcon_php:

PHP - IP Connection
===================

Dies ist die API Beschreibung für die PHP Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_php_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/de/source/Software/Example.php>`__

.. literalinclude:: Example.php
 :language: php
 :linenos:
 :tab-width: 4


.. _ipcon_php_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. php:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. php:function:: void IPConnection::connect(string $host, int $port)

 Erstellt eine TCP/IP Verbindung zum gegebenen *$host* und *$port*. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. php:function:: void IPConnection::disconnect()

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. php:function:: int IPConnection::getConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * IPConnection::CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection::CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick
   Daemon oder der WIFI/Ethernet Extension ist aufgebaut.


.. php:function:: void IPConnection::setTimeout(float $seconds)

 Setzt den Timeout in Sekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2,5.


.. php:function:: int IPConnection::getTimeout()

 Gibt den Timeout zurück, wie er von
 :php:func:`setTimeout() <IPConnection::setTimeout>` gesetzt wurde.


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

.. php:function:: void IPConnection::registerCallback(int $id, callable $callback, mixed $userData = NULL)

 Registriert einen Callback für eine gegebene ID.

 Die verfügbaren IDs mit zugehörenden Callback-Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung wird mit der Funktion :php:func:`registerCallback()
<IPConnection::registerCallback>` durchgeführt. Die Parameter bestehen aus der
Callback ID, der Callback Funktion und optionalen Benutzer Daten:

.. code-block:: php

    function my_callback($param)
    {
        echo $param . "\n";
    }

    $ipcon->registerCallback(IPConnection::CALLBACK_EXAMPLE, 'my_callback');

Die verfügbaren Konstanten mit den zugehörigen Callback Funktionssignaturen
werden im Folgenden beschrieben.


.. php:member:: int IPConnection::CALLBACK_ENUMERATE

 .. code-block:: php

  void callback(string $uid, string $connectedUid, char $position, array $hardwareVersion, array $firmwareVersion, int $deviceIdentifier, int $enumerationType [, mixed $userData])

 Der Callback empfängt sieben Parameter:

 * *$uid*: Die UID des Bricks/Bricklets.
 * *$connectedUid*: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * *$position*: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'd' (Position an Brick).
 * *$hardwareVersion*: Major, Minor und Release Nummer der Hardwareversion.
 * *$firmwareVersion*: Major, Minor und Release Nummer der Firmwareversion.
 * *$deviceIdentifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * *$enumerationType*: Art der Enumerierung

 Mögliche Enumerierungsarten sind:

 * IPConnection::ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst).
 * IPConnection::ENUMERATION_TYPE_CONNECTED (1): Gerät ist neu verfügbar
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu Konfiguriert werden muss.
 * IPConnection::ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur
   bei USB-Verbindungen möglich). In diesem Fall haben nur *$uid* und
   *$enumerationType* einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht)

 Die Device Identifiers sind :ref:`hier <device_identifier>` zu finden.


.. php:member:: int IPConnection::CALLBACK_CONNECTED

 .. code-block:: php

  void callback(int $connectReason [, mixed $userData])

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection::CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection::CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach
   einer automatischen Wiederverbindung.


.. php:member:: int IPConnection::CALLBACK_DISCONNECTED

 .. code-block:: php

  void callback(int $disconnectReason [, mixed $userData])

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection::DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection::DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection::DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
