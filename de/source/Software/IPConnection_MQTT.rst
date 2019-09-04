
.. |ref_api_bindings| replace:: :ref:`MQTT API Bindings <api_bindings_mqtt>`
.. |ref_install_guide| replace:: :ref:`Installationanleitung <api_bindings_mqtt_install>`
.. |bindings_name| replace:: MQTT

.. _ipcon_mqtt:

MQTT - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_mqtt_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.txt) <https://raw.githubusercontent.com/Tinkerforge/generators/master/mqtt/example-enumerate.txt>`__

.. literalinclude:: IPConnection_MQTT_example-enumerate.txt
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.txt) <https://raw.githubusercontent.com/Tinkerforge/generators/master/mqtt/example-authenticate.txt>`__

.. literalinclude:: IPConnection_MQTT_example-authenticate.txt
 :linenos:
 :tab-width: 4


.. _ipcon_mqtt_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. mqtt:function:: request/ip_connection/enumerate

 Broadcast einer Enumerierungsanfrage. Alle Bricks und Bricklets werden mit einem
 Enumerate Callback antworten.

.. mqtt:function:: request/ip_connection/get_connection_state

 :response connection_state: int `(hat Symbole)`

 Kann die folgenden Zustände zurückgeben:
 
 * 0: Keine Verbindung aufgebaut.
 * 1: Eine Verbindung zum Brick Daemon oder der WIFI/Ethernet Extension ist aufgebaut.
 * 2: IP-Connection versucht im Moment eine Verbindung aufzubauen.
 
 Die folgenden Symbole sind für diese Funktion verfügbar:
 
 für connection_state: 
 
 * 0: "disconnected"
 * 1: "connected"
 * 2: "pending"
 
Callbacks
^^^^^^^^^

Callbacks können registriert werden um zeitkritische
oder wiederkehrende Daten vom Gerät zu erhalten. Die Registrierung kann
mit dem entsprechenden `.../register/...`-Topic und einem optionalen Suffix durchgeführt werden.
Mit diesem Suffix kann das Callback später deregistriert werden.

.. note::
 Callbacks für wiederkehrende Ereignisse zu verwenden ist
 *immer* zu bevorzugen gegenüber der Verwendung von Abfragen.
 Es wird weniger USB-Bandbreite benutzt und die Latenz ist
 erheblich geringer, da es keine Paketumlaufzeit gibt.


.. mqtt:function:: register/ip_connection/enumerate

 :register register: bool
 :response uid: string
 :response connected_uid: string
 :response position: string
 :response hardware_version: [int,int,int]
 :response firmware_version: [int,int,int]
 :response device_identifier: int `(hat Symbole)`
 :response enumeration_type: int `(hat Symbole)`
 :response _display_name: string

 Ein Callback für dieses Event kann durch Senden des Payloads "true" an das ``.../register/ip_connection/enumerate[/SUFFIX]``-Topic hinzugefügt werden.
 Ein hinzugefügtes Callback kann durch Senden des Payloads "false" an das selbe Topic wieder entfernt werden.
 Um mehrere (De-)Registrierungen zu unterstützen, z.B. um Nachrichten filtern zu können, kann ein optionaler Suffix verwendet werden.

 Wenn das Callback ausgelöst wird, wird dessen Payload für jeden Suffix auf dem entsprechenden ``.../callback/ip_connection/enumerate[/SUFFIX]``-Topic veröffentlicht.
 
 Dieses Callback empfängt ein JSON-Objekt mit acht Feldern:

 * ``uid``: Die UID des Bricks/Bricklets.
 * ``connected_uid``: Die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``position``: Für Bricks: ``0`` - ``8`` (Position in Stapel). Für Bricklets:
   ``a`` - ``h`` (Position an Brick) oder ``i`` (Position des Raspberry Pi (Zero) HAT)
   oder ``z`` (Bricklet an :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardware_version``: Major, Minor und Release Nummer der Hardwareversion.
 * ``firmware_version``: Major, Minor und Release Nummer der Firmwareversion.
 * ``device_identifier``: Eine Zahl, welche den Brick/Bricklet repräsentiert. Falls die symbolische Ausgabe nicht 
   deaktiviert ist, wird diese auf den entsprechenden Gerätenamen in der Form, wie sie in Topics verwendet wird, 
   gemappt.
 * ``enumeration_type``: Art der Enumerierung.
 * ``_display_name``: Der Anzeigenamen des Gerätes.

 Die folgenden Symbole sind für diese Funktion verfügbar:
 
 für device_identifier: siehe :ref:`hier <device_identifier>`.
 
 für enumeration_type:

 * 0: "available": Gerät ist verfügbar (Enumerierung vom Benutzer ausgelöst: :mqtt:func:`enumerate <register/ip_connection/enumerate>`). Diese Enumerierungsart kann mehrfach für das selbe Gerät auftreten.
 * 1: "connected": Gerät wurde neu verbunden (Automatisch vom Brick gesendet nachdem die Kommunikation aufgebaut wurde). Dies kann bedeuten, dass das Gerät die vorher eingestellte Konfiguration verloren hat und neu konfiguriert werden muss.
 * 2: "disconnected": Gerät wurde getrennt (Nur bei USB-Verbindungen möglich). In diesem Fall haben nur ``uid`` und ``enumeration_type`` einen gültigen Wert.

 Es sollte möglich sein Plug-and-Play-Funktionalität mit diesem Callback zu implementieren (wie es im Brick Viewer geschieht).

.. mqtt:function:: register/ip_connection/connected

 :register register: bool
 :response connect_reason: int `(hat Symbole)`

 Ein Callback für dieses Event kann durch Senden des Payloads "true" an das ``.../register/ip_connection/connected[/SUFFIX]``-Topic hinzugefügt werden.
 Ein hinzugefügtes Callback kann durch Senden des Payloads "false" an das selbe Topic wieder entfernt werden.
 Um mehrere (De-)Registrierungen zu unterstützen, z.B. um Nachrichten filtern zu können, kann ein optionaler Suffix verwendet werden.

 Wenn das Callback ausgelöst wird, wird dessen Payload für jeden Suffix auf dem entsprechenden ``.../callback/ip_connection/connected[/SUFFIX]``-Topic veröffentlicht.
 
 Dieses Callback wird aufgerufen wenn die IP-Connection eine Verbindung zu einem Brick Daemon oder einer WIFI/Ethernet Extension aufgebaut hat.
 
 Die folgenden Symbole sind für diese Funktion verfügbar:
 
 für connect_reason:

 * 0: "request": Verbindung aufgebaut nach Anfrage vom Benutzer.
 * 1: "auto-reconnect": Verbindung aufgebaut durch Auto-Reconnect.


.. mqtt:function:: register/ip_connection/disconnected

 :register register: bool
 :response disconnect_reason: int `(hat Symbole)`

 Ein Callback für dieses Event kann durch Senden des Payloads "true" an das ``.../register/ip_connection/disconnected[/SUFFIX]``-Topic hinzugefügt werden.
 Ein hinzugefügtes Callback kann durch Senden des Payloads "false" an das selbe Topic wieder entfernt werden.
 Um mehrere (De-)Registrierungen zu unterstützen, z.B. um Nachrichten filtern zu können, kann ein optionaler Suffix verwendet werden.

 Wenn das Callback ausgelöst wird, wird dessen Payload für jeden Suffix auf dem entsprechenden ``.../callback/ip_connection/disconnected[/SUFFIX]``-Topic veröffentlicht.
 
 Dieses Callback wird aufgerufen wenn die Verbindung der IP Connection zu einem Brick Daemon oder einer WIFI/Ethernet Extension getrennt wurde, mögliche Gründe sind:

 Die folgenden Symbole sind für diese Funktion verfügbar:
 
 für disconnect_reason:
 
 * 0: "request": Trennung wurde vom Benutzer angefragt.
 * 1: "error": Trennung aufgrund eines unlösbaren Problems.
 * 2: "shutdown": Trennung wurde vom Brick Daemon oder WIFI/Ethernet Extension eingeleitet.
