.. _tutorial_rugged_approach:

Robuster Ansatz
===============

Seit dem neuen Protokoll 2.0 ist es möglich Programme zu schreiben die
stabil bleiben bei Unterbrechungen, kurzen Stromausfällen und ähnliches.

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

Es muss sichergestellt werden, dass die Konfiguration von Bricks/Bricklets
während der Enumerierung stattfindet. Dies stellt sicher, dass die
Konfiguration (z.B. Callbackperiode) immer vorhanden ist, auch wenn
ein Brick oder Bricklet neugestartet wurde und die Konfiguration
verloren hat.

Eine Möglichkeit um dies sicherzustellen ist den Konfigurationscode in
den Enumeration-Callback zu stecken. Es sollte zusätzlich sichergestellt sein,
das eine neue Enumerierung ausgelöst wird wenn eine TCP/IP Verbindung neu
aufgebaut wird, nachdem sie getrennt wurde. Wenn eine Verbindung getrennt wird,
ist nicht ausgeschlossen dass en Brick oder Bricklet in der zwischenzeit
neugestartet wird und deshalb neu Konfiguriert werden muss.

Im folgenden befinden sich Quelltext für ein Pgoramm, dass eine Temperatur
auf einem LCD 20x4 Bricklet anzeigt. Dieses Programm sollte auch bei einem
Neustart des Master Bricks oder eine verlorenen WiFi Verbindung weiter
funktionieren. Es ist sogar möglich das Temperature oder LCD 20x4 Bricklet
auszutauschen, da das Programm die UID aus der Enumerierung benutzt.

C#
--

.. literalinclude:: ExampleRugged.cs
 :language: csharp
 :linenos:
 :tab-width: 4

Python
------

.. literalinclude:: example_rugged.py
 :language: python
 :linenos:
 :tab-width: 4

