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

.. java:function:: class IPConnection(String host, int port)

 Erzeugt eine IP Connection zum Brick Daemon mit dem übergebenen *host*
 und *port*. Die IP Connection erlaubt es die bekannten Bricks und Bricklets
 aufzuzählen. Abgesehen davon wird sie benutzt um Bricks und Bricklets zur
 Kommunikation über diese Verbindung hinzuzufügen.

 Der Konstruktor löst eine ``IOException`` aus falls  kein Brick Daemon unter
 dem angegebenen *host* und *port* zu erreichen ist.

.. java:function:: public void IPConnection::addDevice(Device device)

 Fügt ein Gerät (Brick or Bricklet) der IP Connection hinzu. Jegliches Gerät
 muss zuerst einer IP Connection hinzugefügt werden bevor es benutzt werden
 kann. Beispiele dafür finden sich in der API Dokumentation jedes Bricks und
 Bricklets.

.. java:function:: public void IPConnection::joinThread()

 Wartet auf die Beendigung der Threads der IP Connection. Der Aufruf blockiert
 bis die IP Connection :java:func:`zerstört <IPConnection::destroy>` wird.

 Dies ist dann sinnvoll, wenn ein Programm vollständig auf Callbacks basiert
 oder die IP Connection in einem anderem Thread erzeugt wurde.

.. java:function:: public void IPConnection::destroy()

 Zerstört die IP Connection. Die Verbindung zum Brick Daemon wird geschlossen
 und die Threads der IP Connection werden beendet.


Konfigurationsfunktionen für Callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:function:: public void IPConnection::enumerate(EnumerateListener enumerateListener)

 Diese Methode registriert eine Listener mit folgender Signatur:

 .. java:function:: public class IPConnection.EnumerateListener()

  .. java:function:: public void enumerate(String uid, String name, short stackID, boolean isNew)
   :noindex:

   Der Listener bekommt vier Parameter übergeben:

   * *uid*: Die UID des Gerätes.
   * *name*: Der Name des Gerätes (beinhaltet "Brick" oder "Bricklet" und eine Versionsnummer).
   * *stackID*: Die Stapel ID des Gerätes (damit kann die Position innerhalb des Stapels ermittelt werden).
   * *isNew*: Ist *true* wenn das Gerät hinzugefügt wurde, *false* wenn es entfernt wurde.

   Es gibt drei verschiedenen Situationen in denen der Callback aufgerufen wird.
   Erstens, der Callback wird für alle im Moment angeschlossenen Geräte aufgerufen
   (mit *isNew* gleich *true*). Dies wird durch den Aufruf von
   :java:func:`enumerate <IPConnection::enumerate>` ausgelöst. Zweitens, der Callback wird auch aufgerufen
   wenn ein Brick an USB angesteckt wird (mit *isNew* gleich *true*).
   Schlussendlich wird der Callback aufgerufen wenn ein Brick von USB angesteckt
   wurde (mit *isNew* gleich *false*).

   Dieser Callback erlaubt es "Plug'n'Play" Funktionalität zu implementieren (wie
   es im Brick Viewer getan wurde).
