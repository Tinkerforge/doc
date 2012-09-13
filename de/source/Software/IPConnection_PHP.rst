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

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.php>`__

.. literalinclude:: Example.php
 :language: php
 :linenos:
 :tab-width: 4


.. _ipcon_php_api:

API
---

Grundfunktionen
^^^^^^^^^^^^^^^

.. php:function:: class IPConnection(string $host, int $port)

 Erzeugt eine IP Connection zum Brick Daemon mit dem übergebenen *$host*
 und *$port*. Die IP Connection erlaubt es die bekannten Bricks und Bricklets
 aufzuzählen. Abgesehen davon wird sie benutzt um Bricks und Bricklets zur
 Kommunikation über diese Verbindung hinzuzufügen.

.. php:function:: void IPConnection::addDevice(Device $device)

 Fügt ein Gerät (Brick or Bricklet) der IP Connection hinzu. Jegliches Gerät
 muss zuerst einer IP Connection hinzugefügt werden bevor es benutzt werden
 kann. Beispiele dafür finden sich in der API Dokumentation jedes Bricks und
 Bricklets.

.. php:function:: void IPConnection::dispatchCallbacks(float $seconds)

 Liefert eingehende Callbacks für die gegebene Dauer in Sekunden aus (negative
 Werte bedeuten unendlich). Da PHP keine Threads unterstützt musst du diese
 Methode periodisch aufrufen, um sicherzustellen, dass eingehende Callbacks
 behandelt werden. Falls du keine Callbacks benutzt brauchst du diese Methode
 nicht aufzurufen.

 Die empfohlene Wert für *$seconds* ist 0. Dadurch werden nur die Callbacks
 ausgeliefert die noch auf Auslieferung warten. Es wird jedoch nicht auf den
 Eingang weitere Callbacks gewartet.

.. php:function:: void IPConnection::destroy()

 Zerstört die IP Connection. Die Verbindung zum Brick Daemon wird geschlossen.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. php:function:: void IPConnection::enumerate(callable $callback)

 Diese Methode registriert eine Callback mit folgender Signatur:

 .. code-block:: php

  void callback(string $uid, string $name, int $stackID, bool $isNew)

 der die folgenden vier Parameter übergeben bekommt:

 * *$uid*: Die UID des Gerätes.
 * *$name*: Der Name des Gerätes (beinhaltet "Brick" oder "Bricklet" und eine Versionsnummer).
 * *$stackID*: Die Stapel ID des Gerätes (damit kann die Position innerhalb des Stapels ermittelt werden).
 * *$isNew*: Ist *true* wenn das Gerät hinzugefügt wurde, *false* wenn es entfernt wurde.

 Es gibt drei verschiedenen Situationen in denen der Callback aufgerufen wird.
 Erstens, der Callback wird für alle im Moment angeschlossenen Geräte aufgerufen
 (mit *$isNew* gleich *true*). Dies wird durch den Aufruf von
 :php:func:`enumerate <IPConnection::enumerate>` ausgelöst. Zweitens, der Callback wird auch aufgerufen
 wenn ein Brick an USB angesteckt wird (mit *$isNew* gleich *true*).
 Schlussendlich wird der Callback aufgerufen wenn ein Brick von USB angesteckt
 wurde (mit *$isNew* gleich *false*).

 Dieser Callback erlaubt es "Plug'n'Play" Funktionalität zu implementieren (wie
 es im Brick Viewer getan wurde).

 Du musst :php:func:`dispatchCallbacks <IPConnection::dispatchCallbacks>` aufrufen
 um Callbackaufrufe zu erhalten. Die empfohlene Wert für *$seconds* ist 2.5;
