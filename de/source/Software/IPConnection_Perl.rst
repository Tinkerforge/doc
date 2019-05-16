
.. |ref_api_bindings| replace:: :ref:`Perl API Bindings <api_bindings_perl>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_perl_install>`
.. |bindings_name| replace:: Perl

.. _ipcon_perl:

Perl - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_perl_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.pl) <https://github.com/Tinkerforge/generators/raw/master/perl/example_enumerate.pl>`__

.. literalinclude:: IPConnection_Perl_example_enumerate.pl
 :language: perl
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.pl) <https://github.com/Tinkerforge/generators/raw/master/perl/example_authenticate.pl>`__

.. literalinclude:: IPConnection_Perl_example_authenticate.pl
 :language: perl
 :linenos:
 :tab-width: 4


.. _ipcon_perl_api:

API
---

Allgemein kann jede Subroutine der Perl Bindings Fehler als
``Tinkerforge::Error`` Objekt mittels ``croak()`` melden. Das Objekt hat eine
``get_code()`` und eine ``get_message()`` Subroutine. Es sind verschiedene
Fehlercodes definiert:

* Error->ALREADY_CONNECTED = 11
* Error->NOT_CONNECTED = 12
* Error->CONNECT_FAILED = 13
* Error->INVALID_FUNCTION_ID = 21
* Error->TIMEOUT = 31
* Error->INVALID_PARAMETER = 41
* Error->FUNCTION_NOT_SUPPORTED = 42
* Error->UNKNOWN_ERROR = 43

Alle folgend aufgelisteten Funktionen sind Thread-sicher.

Grundfunktionen
^^^^^^^^^^^^^^^

.. perl:function:: IPConnection->new()

 Erzeugt ein IP Connection Objekt das verwendet werden kann um die verfügbar
 Geräte zu enumerieren. Es wird auch für den Konstruktor von Bricks und
 Bricklets benötigt.


.. perl:function:: IPConnection->connect($host, $port)

 :param $host: string
 :param $port: int
 :rtype: undef

 Erstellt eine TCP/IP Verbindung zum gegebenen ``$host`` und ``$port``. Host und Port
 können auf einen Brick Daemon oder einer WIFI/Ethernet Extension verweisen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung erfolgreich
 aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirft eine Exception, falls
 kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen Host und Port
 horcht.


.. perl:function:: IPConnection->disconnect()

 :rtype: undef

 Trennt die TCP/IP Verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. perl:function:: IPConnection->authenticate($secret)

 :param $host: string
 :rtype: undef

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


.. perl:function:: IPConnection->get_connection_state()

 :rtype: int

 Kann die folgenden Zustände zurückgeben:

 * IPConnection->CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * IPConnection->CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon
   oder der WIFI/Ethernet Extension ist aufgebaut.
 * IPConnection->CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment
   eine Verbindung aufzubauen.


.. perl:function:: IPConnection->set_auto_reconnect($auto_reconnect)

 :param $auto_reconnect: bool
 :rtype: undef

 Aktiviert oder deaktiviert Auto-Reconnect. Falls Auto-Reconnect aktiviert
 ist, versucht die IP Connection eine Verbindung zum vorher angegebenen Host
 und Port wieder herzustellen, falls die aktuell bestehende Verbindung verloren
 geht. Auto-Reconnect greift also erst nach einem erfolgreichen Aufruf von
 :perl:func:`connect() <IPConnection->connect>`.

 Standardwert ist 1.


.. perl:function:: IPConnection->get_auto_reconnect()

 :rtype: bool

 Gibt *True* zurück wenn Auto-Reconnect aktiviert ist und *False* sonst.


.. perl:function:: IPConnection->set_timeout($timeout)

 :param $timeout: float
 :rtype: undef

 Setzt den Timeout in Sekunden für Getter und für Setter die das
 Response-Expected-Flag aktiviert haben.

 Standardwert ist 2,5.


.. perl:function:: IPConnection->get_timeout()

 :rtype: float

 Gibt den Timeout zurück, wie er von :perl:func:`set_timeout()
 <IPConnection->set_timeout>` gesetzt wurde.


.. perl:function:: IPConnection->enumerate()

 :rtype: undef

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit
 einem Enumerate Callback antworten.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. perl:function:: IPConnection->register_callback($callback_id, $function)

 :param $callback_id: int
 :param $function: callable
 :rtype: undef

 Registriert den ``$function`` Namen für die gegebene ``$callback_id``.

 Die verfügbaren Callback IDs mit zugehörenden Funktionssignaturen
 sind unten beschrieben.


Callbacks
^^^^^^^^^

Callbacks können registriert werden um über Ereignisse informiert zu werden.
Die Registrierung kann mit der Funktion :perl:func:`register_callback()
<IPConnection->register_callback>` durchgeführt werden. Der erste Parameter
ist der Callback ID und der zweite die Callback Funktion:

.. code-block:: perl

    sub my_callback
    {
        print "@_[0]";
    }

    $ipcon->register_callback(IPConnection->CALLBACK_EXAMPLE, 'my_callback')

Die Callback Funktion wird dann von einem internen Thread der IP Connection
aufgerufen werden. Im Gegensatz zu vielen anderen Programmiersprachen werden
Variablen nicht automatisch zwischen Threads geteilt. Wenn eine Variable
gleichzeitig in einer Callback Funktion und dem Rest des Programms genutzt
werden soll, dann muss diese als ``:shared`` markiert werden. Siehe dazu auch
die Dokumentation des `threads::shared
<http://perldoc.perl.org/threads/shared.html>`__ Perl Moduls für weitere
Details.

Die verfügbaren IDs mit der dazugehörigen Parameteranzahl und -typen
werden weiter unten beschrieben.


.. perl:attribute:: IPConnection->CALLBACK_ENUMERATE

 :param $uid: string
 :param $connected_uid: string
 :param $position: char
 :param @hardware_version: [int, int, int]
 :param @firmware_version: [int, int, int]
 :param $device_identifier: int
 :param $enumeration_type: int

 Der Callback empfängt sieben Parameter:

 * ``$uid``: Die UID des Bricks/Bricklets.
 * ``$connected_uid``: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``$position``: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
   'a' - 'h' (Position an Brick) oder 'i' (Position des Raspberry Pi (Zero) HAT)
   oder 'z' (Bricklet an :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``@hardware_version``: Major, Minor und Release Nummer der Hardwareversion.
 * ``@firmware_version``: Major, Minor und Release Nummer der Firmwareversion.
 * ``$device_identifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert.
 * ``$enumeration_type``: Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * IPConnection->ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar
   (Enumerierung vom Benutzer ausgelöst: :perl:func:`enumerate()
   <IPConnection->enumerate>`). Diese Enumerierungsart kann mehrfach für das
   selbe Gerät auftreten.
 * IPConnection->ENUMERATION_TYPE_CONNECTED (1): Gerät wurde neu verbunden
   (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde).
   Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration
   verloren hat und neu konfiguriert werden muss.
 * IPConnection->ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei
   USB-Verbindungen möglich). In diesem Fall haben nur ``$uid`` und
   ``$enumeration_type`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback
 zu implementieren (wie es im Brick Viewer geschieht)

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.
 Es gibt auch Konstanten für diese Werte, welche nach dem folgenden Muster
 benannt sind::

  <device-class>->DEVICE_IDENTIFIER

 Zum Beispiel: :perl:attr:`BrickMaster->DEVICE_IDENTIFIER`
 oder :perl:attr:`BrickletAmbientLight->DEVICE_IDENTIFIER`.


.. perl:attribute:: IPConnection->CALLBACK_CONNECTED

 :param $connect_reason: int

 Dieser Callback wird aufgerufen wenn die IP Connection eine Verbindung
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat,
 mögliche Gründe sind:

 * IPConnection->CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach Anfrage
   vom Benutzer.
 * IPConnection->CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut durch
   Auto-Reconnect.


.. perl:attribute:: IPConnection->CALLBACK_DISCONNECTED

 :param $disconnect_reason: int

 Dieser Callback wird aufgerufen wenn die Verbindung der IP Connection
 zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde,
 mögliche Gründe sind:

 * IPConnection->DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer
   angefragt.
 * IPConnection->DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren
   Problems.
 * IPConnection->DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon
   oder WIFI/Ethernet Extension eingeleitet.
