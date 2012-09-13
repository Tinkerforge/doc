.. _ipcon_delphi:

Delphi - IP Connection
======================

Dies ist die API Beschreibung für die Delphi Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_delphi_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.rb>`__

.. literalinclude:: Example.pas
 :language: delphi
 :linenos:
 :tab-width: 4


.. _ipcon_delphi_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. delphi:function:: constructor TIPConnection.Create(const host: string; const port: word)

 Erzeugt eine IP Connection zum Brick Daemon mit dem übergebenen *host*
 und *port*. Die IP Connection erlaubt es die bekannten Bricks und Bricklets
 aufzuzählen. Abgesehen davon wird sie benutzt um Bricks und Bricklets zur
 Kommunikation über diese Verbindung hinzuzufügen.

.. delphi:function:: procedure TIPConnection.AddDevice(const device: TDevice)

 Fügt ein Gerät (Brick or Bricklet) der IP Connection hinzu. Jegliches Gerät
 muss zuerst einer IP Connection hinzugefügt werden bevor es benutzt werden
 kann. Beispiele dafür finden sich in der API Dokumentation jedes Bricks und
 Bricklets.

.. delphi:function:: procedure TIPConnection.JoinThread

 Wartet auf die Beendigung der Threads der IP Connection. Der Aufruf blockiert
 bis die IP Connection :delphi:func:`zerstört <TIPConnection.Destroy>` wird.

 Dies ist dann sinnvoll, wenn dein Programm vollständig auf Callbacks basiert
 oder du die IP Connection in einem anderem Thread erzeugt hast.

.. delphi:function:: destructor TIPConnection.Destroy

 Zerstört die IP Connection. Die Verbindung zum Brick Daemon wird geschlossen
 und die Threads der IP Connection werden beendet.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. delphi:function:: procedure TIPConnection.Enumerate(const enumerateCallback: TIPConnectionNotifyEnumerate)

 Diese Prozedur registriert eine Callback mit folgender Signatur:

 .. code-block:: delphi

  procedure(const uid: string; const name: string; const stackID: byte; const isNew: boolean) of object;

 der die folgenden vier Parameter übergeben bekommt:

 * *uid*: Die UID des Gerätes.
 * *name*: Der Name des Gerätes (beinhaltet "Brick" oder "Bricklet" und eine Versionsnummer).
 * *stackID*: Die Stapel ID des Gerätes (damit kann die Position innerhalb des Stapels ermittelt werden).
 * *isNew*: Ist *true* wenn das Gerät hinzugefügt wurde, *false* wenn es entfernt wurde.

 Es gibt drei verschiedenen Situationen in denen der Callback aufgerufen wird.
 Erstens, der Callback wird für alle im Moment angeschlossenen Geräte aufgerufen
 (mit *isNew* gleich *true*). Dies wird durch den Aufruf von
 :delphi:func:`Enumerate <TIPConnection.Enumerate>` ausgelöst. Zweitens, der Callback wird auch aufgerufen
 wenn ein Brick an USB angesteckt wird (mit *isNew* gleich *true*).
 Schlussendlich wird der Callback aufgerufen wenn ein Brick von USB angesteckt
 wurde (mit *isNew* gleich *false*).

 Dieser Callback erlaubt es "Plug'n'Play" Funktionalität zu implementieren (wie
 es im Brick Viewer getan wurde).
