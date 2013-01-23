.. _tutorial_rugged_approach:

Robuster Ansatz
===============

Seit dem neuen Protokoll 2.0 ist es möglich Programme zu schreiben die
stabil bleiben bei Unterbrechungen, kurzen Stromausfällen und ähnlichem.

Der generelle Ansatz für ein solches Programm sieht wie folgt aus 
(Pseudocode)::

 func enumerate_callback(...) {
     configure_brick();
     configure_bricklet();
 }

 func connected_callback(...) {
     ipcon.enumerate();
 }

 func main() {
     ipcon.enumerate();
     while(true) {
         if(brick_is_configured) {
             do_something_with_brick();
         }
         if(bricklet_is_configured) {
             do_something_with_bricklet();
         }
     }
 }

Es muss sichergestellt werden, dass die Konfiguration von Bricks und Bricklets
während der Enumerierung stattfindet. Dies führt dazu, dass die
Konfiguration (z.B. Callback-Periode) immer vorhanden ist, auch wenn
ein Brick oder Bricklet neugestartet wurde und dadurch seine Konfiguration
verloren hat.

Eine Möglichkeit um dies zu realisieren ist den Konfigurationscode in
den Enumeration-Callback zu schreiben. Es sollte zusätzlich sichergestellt sein,
dass eine neue Enumerierung ausgelöst wird wenn eine TCP/IP Verbindung neu
aufgebaut wird, nachdem sie getrennt wurde. Wenn eine Verbindung getrennt wird,
ist nicht ausgeschlossen dass ein Brick oder Bricklet in der Zwischenzeit
neugestartet wird und deshalb neu konfiguriert werden muss.

Im Folgenden befinden sich Quelltexte für ein Programm, dass eine Temperatur
auf einem LCD 20x4 Bricklet anzeigt. Dieses Programm sollte auch bei einem
Neustart des Master Bricks oder eine verlorenen WiFi Verbindung weiter
funktionieren. Es ist sogar möglich das Temperature oder LCD 20x4 Bricklet
auszutauschen, da das Programm die UID aus der Enumerierung benutzt.

C#
--

`Download <https://raw.github.com/Tinkerforge/doc/master/de/source/Tutorials/Tutorial_Rugged/ExampleRugged.cs>`__

.. literalinclude:: ExampleRugged.cs
 :language: csharp
 :linenos:
 :tab-width: 4

Python
------

`Download <https://raw.github.com/Tinkerforge/doc/master/de/source/Tutorials/Tutorial_Rugged/example_rugged.py>`__

.. literalinclude:: example_rugged.py
 :language: python
 :linenos:
 :tab-width: 4

