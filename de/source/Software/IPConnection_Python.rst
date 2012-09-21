.. _ipcon_python:

Python - IP Connection
======================

Dies ist die API Beschreibung für die Python Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_python_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.py>`__

.. literalinclude:: example.py
 :language: python
 :linenos:
 :tab-width: 4


.. _ipcon_python_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. py:function:: IPConnection(host, port)

 :param host: str
 :param port: int

 Erzeugt eine IP Connection zum Brick Daemon mit dem übergebenen *host*
 und *port*. Die IP Connection erlaubt es die bekannten Bricks und Bricklets
 aufzuzählen. Abgesehen davon wird sie benutzt um Bricks und Bricklets zur
 Kommunikation über diese Verbindung hinzuzufügen.

.. py:function:: IPConnection.add_device(device)

 :param device: Device
 :rtype: None

 Fügt ein Gerät (Brick or Bricklet) der IP Connection hinzu. Jegliches Gerät
 muss zuerst einer IP Connection hinzugefügt werden bevor es benutzt werden
 kann. Beispiele dafür finden sich in der API Dokumentation jedes Bricks und
 Bricklets.

.. py:function:: IPConnection.join_thread()

 :rtype: None

 Wartet auf die Beendigung der Threads der IP Connection. Der Aufruf blockiert
 bis die IP Connection :py:func:`zerstört <IPConnection.destroy>` wird.

 Dies ist dann sinnvoll, wenn ein Programm vollständig auf Callbacks basiert
 oder die IP Connection in einem anderem Thread erzeugt wurde.

.. py:function:: IPConnection.destroy()

 :rtype: None

 Zerstört die IP Connection. Die Verbindung zum Brick Daemon wird geschlossen
 und die Threads der IP Connection werden beendet.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: IPConnection.enumerate(callback)

 :param callback: callable(uid, name, stack_id, is_new)
 :rtype: None

 Diese Methode registriert einen Callback der vier Parameter übergeben bekommt:

 * *uid*: Die UID des Gerätes.
 * *name*: Der Name des Gerätes (beinhaltet "Brick" oder "Bricklet" und eine Versionsnummer).
 * *stack_id*: Die Stapel ID des Gerätes (damit kann die Position innerhalb des Stapels ermittelt werden).
 * *is_new*: Ist *True* wenn das Gerät hinzugefügt wurde, *False* wenn es entfernt wurde.

 Es gibt drei verschiedenen Situationen in denen der Callback aufgerufen wird.
 Erstens, der Callback wird für alle im Moment angeschlossenen Geräte aufgerufen
 (mit *is_new* gleich *True*). Dies wird durch den Aufruf von
 :py:func:`enumerate <IPConnection.enumerate>` ausgelöst. Zweitens, der Callback wird auch aufgerufen
 wenn ein Brick an USB angesteckt wird (mit *is_new* gleich *True*).
 Schlussendlich wird der Callback aufgerufen wenn ein Brick von USB angesteckt
 wurde (mit *is_new* gleich *False*).

 Dieser Callback erlaubt es "Plug'n'Play" Funktionalität zu implementieren (wie
 es im Brick Viewer getan wurde).
