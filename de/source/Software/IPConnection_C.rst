.. _ipcon_c:

C/C++ - IP Connection
=====================

Dies ist die API Beschreibung für die C/C++ Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_c_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.c>`__

.. literalinclude:: example.c
 :language: c
 :linenos:
 :tab-width: 4


.. _ipcon_c_api:

API
---

Jede Funktion der C/C++ Bindings gibt einen Integer zurück, welcher einen
Fehlercode beschreibt.

Mögliche Fehlercodes sind:

* E_OK = 0
* E_TIMEOUT = -1
* E_NO_STREAM_SOCKET = -2
* E_HOSTNAME_INVALID = -3
* E_NO_CONNECT = -4
* E_NO_THREAD = -5
* E_NOT_ADDED = -6

wie in :file:`ip_connection.h` definiert.


Grundfunktionen
^^^^^^^^^^^^^^^

.. c:function:: int ipcon_create(IPConnection *ipcon, const char* host, const int port)

 Erzeugt eine IP Connection zum Brick Daemon mit dem übergebenen *host*
 und *port*. Die IP Connection erlaubt es die bekannten Bricks und Bricklets
 aufzuzählen. Abgesehen davon wird sie benutzt um Bricks und Bricklets zur
 Kommunikation über diese Verbindung hinzuzufügen.

.. c:function:: int ipcon_add_device(IPConnection *ipcon, Device *device)

 Fügt ein Gerät (Brick or Bricklet) der IP Connection hinzu. Jegliches Gerät
 muss zuerst einer IP Connection hinzugefügt werden bevor es benutzt werden
 kann. Beispiele dafür finden sich in der API Dokumentation jedes Bricks und
 Bricklets.

.. c:function:: void ipcon_join_thread(IPConnection *ipcon)

 Wartet auf die Beendigung der Threads der IP Connection. Der Aufruf blockiert
 bis die IP Connection :c:func:`zerstört <ipcon_destroy>` wird.

 Dies ist dann sinnvoll, wenn dein Programm vollständig auf Callbacks basiert
 oder du die IP Connection in einem anderem Thread erzeugt hast.

.. c:function:: void ipcon_destroy(IPConnection *ipcon)

 Zerstört die IP Connection. Die Verbindung zum Brick Daemon wird geschlossen
 und die Threads der IP Connection werden beendet.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. c:function:: void ipcon_enumerate(IPConnection *ipcon, enumerate_callback_func_t cb)

 Diese Funktion registriert eine Callback mit folgender Signatur:

 .. code-block:: c

  void callback(char *uid, char *name, uint8_t stack_id, bool is_new)

 der die folgenden vier Parameter übergeben bekommt:

 * *uid*: Die UID des Gerätes.
 * *name*: Der Name des Gerätes (beinhaltet "Brick" oder "Bricklet" und eine Versionsnummer).
 * *stack_id*: Die Stapel ID des Gerätes (damit kann die Position innerhalb des Stapels ermittelt werden).
 * *is_new*: Ist *true* wenn das Gerät hinzugefügt wurde, *false* wenn es entfernt wurde.

 Es gibt drei verschiedenen Situationen in denen der Callback aufgerufen wird.
 Erstens, der Callback wird für alle im Moment angeschlossenen Geräte aufgerufen
 (mit *is_new* gleich *true*). Dies wird durch den Aufruf von
 :c:func:`ipcon_enumerate <ipcon_enumerate>` ausgelöst. Zweitens, der Callback wird auch aufgerufen
 wenn ein Brick an USB angesteckt wird (mit *is_new* gleich *true*).
 Schlussendlich wird der Callback aufgerufen wenn ein Brick von USB angesteckt
 wurde (mit *is_new* gleich *false*).

 Dieser Callback erlaubt es "Plug'n'Play" Funktionalität zu implementieren (wie
 es im Brick Viewer getan wurde).
