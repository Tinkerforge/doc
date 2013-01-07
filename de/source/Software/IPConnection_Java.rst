.. _ipcon_java:

Java - IP Connection
====================

Dies ist die API Beschreibung für die Java Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_java_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.java>`__

.. literalinclude:: Example.java
 :language: java
 :linenos:
 :tab-width: 4


.. _ipcon_java_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. java:function:: class IPConnection()

 Erzeugt ein IP Connection Objekt. Das konstruierte Objekt wird für
 den Konstruktor von Bricks und Bricklets benötigt.


.. java:function:: public void IPConnection::connect(String host, int port)

 Erstellt eine TCP/IP Verbindung zum gegebenen Host und Port.
 Host und Port können zu eine Brick Daemon oder der WIFI/Ethernet Extension
 zeigen.

 Bricks/Bricklets können erst gesteuert werden, wenn die Verbindung
 erfolgreich aufgebaut wurde.

 Blockiert bis die Verbindung aufgebaut wurde und wirf eine Exception
 falls kein Brick Daemon oder WIFI/Ethernet Extension auf dem gegebenen
 Host und Port horchen.


.. java:function:: public void IPConnection::disconnect()

 Trennt die TCP/IP verbindung zum Brick Daemon oder einer WIFI/Ethernet
 Extension.


.. java:function:: public short IPConnection::getConnectionState()

 Kann die folgenden Zustände zurückgeben:

 * CONNECTION_STATE_DISCONNECTED (0): Keine Verbindung aufgebaut.
 * CONNECTION_STATE_CONNECTED (1): Eine Verbindung zum Brick Daemon oder der
   WIFI/Ethernet Extension ist aufgebaut.
 * CONNECTION_STATE_PENDING (2): IP Connection versucht im Moment eine
   Verbindung aufzubauen.


.. java:function:: public void IPConnection::setAutoReconnect(boolean autoReconnect)

 Aktiviert oder deaktiviert die automatische Wiederverbindung. Falls die
 Wiederverbindung aktiviert ist, versucht die IP Connection eine Verbindung
 zum vorher angegebenen Host und Port wieder herzustellen, falls die Verbindung
 verloren geht.

 Standardwert ist *true*.


.. java:function:: public boolean IPConnection::getAutoReconnect()

 Gibt *true* zurück wenn die Wiederverbindung aktiviert ist und *false* sonst.


.. java:function:: public void IPConnection::setTimeout(int timeout)

 Setzt den Timeout (in ms) für Getter und für Setter die "response expected"
 aktiviert haben.

 Standardwert ist 2500ms.


.. java:function:: public int IPConnection::getTimeout()

 Gibt den Timeout zurück, wie er von :java:func:`setTimeout <IPConnection::setTimeout>`
 gesetzt wurde.


.. java:function:: public void IPConnection::enumerate()

 Broadcast einer Enumerierungsanfrage. Alle Bricks/Bricks werden mit
 einem Enumerate Callback antworten.


Konfiguration von Listener
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:function:: public void IPConnection::addListener(Object object)

 Diese Methode registriert die folgenden Listener:

 .. java:function:: public class IPConnection.EnumerateListener()

  .. java:function:: public void enumerate(String uid, String connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)
   :noindex:

   Der Listener empfängt sieben Parameter:

   * *uid*: Die UID des Bricks/Bricklets.
   * *connectedUid*: Die UID wo das Brick/Bricklet mit verbunden ist. Für ein
     Bricklet ist dies die UID des Bricks mit dem es verbunden ist. Für einen
     Brick ist es die UID des untsten Master Brickss in einem Stapel. Der
     unterste Master Brick hat die connected UID "1". Mit diesen Informationen
     sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
   * *position*: Für Bricks: '0' - '8' (Position in Stapel). Für Bricklets:
     'a' - 'd' (Position an Brick).
   * *hardwareVersion*: Major, Minor und Release Nummer der Hardwareversion.
   * *firmwareVersion*: Major, Minor und Release Nummer der Firmwareversion.
   * *deviceIdentifier*: Eine Zahl, welche den Brick/Bricklet repräsentiert.
   * *enumerationType*: Art der Enumerierung.

   Mögliche Enumerierungsarten sind:

   * ENUMERATION_TYPE_AVAILABLE (0): Gerät ist verfügbar (Enumerierung vom
     Benutzer ausgelöst).
   * ENUMERATION_TYPE_CONNECTED (1): Gerät ist neu verfügbar (Automatisch vom
     Brick gesendet nachdem die Kommunikation aufgebaut wurde). Dies kann
     bedeuten, dass das Gerät die vorher eingestellte Konfiguration verloren
     hat und neu konfiguriert werden muss.
   * ENUMERATION_TYPE_DISCONNECTED (2): Gerät wurde getrennt (Nur bei
     USB-Verbindungen möglich). In diesem Fall haben nur *uid* und
     *enumerationType* einen gültigen Wert.

   Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Listener
   zu implementieren (wie es im Brick Viewer geschieht).


 .. java:function:: public class IPConnection.ConnectedListener()

  .. java:function:: public void connected(short connectReason)
   :noindex:

   Dieser Listener wird aufgerufen wenn die IP Connection eine Verbindung
   aufgebaut hat, mögliche Gründe sind:

   * CONNECT_REASON_REQUEST (0): Verbindung aufgebaut nach anfrage vom Benutzer.
   * CONNECT_REASON_AUTO_RECONNECT (1): Verbindung aufgebaut nach einer
     automatischen Wiederverbindung.


 .. java:function:: public class IPConnection.DisconnectedListener()

  .. java:function:: public void disconnected(short disconnectReason)
   :noindex:

   Dieser Listener wird aufgerufen wenn die Verbindung der IP Connection
   getrennt wird, mögliche Gründe sind:

   * DISCONNECT_REASON_REQUEST (0): Trennung wurde vom Benutzer angefragt.
   * DISCONNECT_REASON_ERROR (1): Trennung aufgrund eines unlösbaren Problems.
   * DISCONNECT_REASON_SHUTDOWN (2): Trennung wurde vom Brick Daemon oder
     WIFI/Ethernet Extension eingeleitet.
