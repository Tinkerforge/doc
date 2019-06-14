
.. _tutorial_rugged_approach:

Tutorial - Robuster Ansatz
==========================

Mit dem neuen Protokoll 2.0 ist es möglich Programme zu schreiben, die
robust gegenüber Unterbrechungen, kurzen Stromausfällen und ähnlichem sind.

Der generelle Ansatz für ein solches Programm sieht aus wie folgt
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

     while (true) {
         if (brick_is_configured) {
             do_something_with_brick();
         }

         if (bricklet_is_configured) {
             do_something_with_bricklet();
         }
     }
 }

Es muss sichergestellt werden, dass die Konfiguration von Bricks und Bricklets
während der Enumerierung stattfindet. Dies führt dazu, dass die
Konfiguration (z.B. Callback-Periode) immer gesetzt wird, auch wenn
ein Brick oder Bricklet neu gestartet wurde und dadurch seine Konfiguration
verloren hat.

Eine Möglichkeit um dies zu realisieren ist, den Konfigurationscode in
das Enumeration-Callback zu schreiben. Es sollte zusätzlich sichergestellt sein,
dass eine neue Enumerierung ausgelöst wird, wenn eine TCP/IP-Verbindung neu
aufgebaut wird, nachdem sie getrennt wurde. Wenn eine Verbindung getrennt und wiederhergestellt wird,
ist nicht ausgeschlossen, dass ein Brick oder Bricklet in der Zwischenzeit
neu gestartet wurde. Deshalb muss es auch dann neu konfiguriert werden.

Im Folgenden finden sich C#- und Python-Quelltexte für ein Programm, dass eine Temperatur
auf einem LCD 20x4 Bricklet anzeigt. Dieses Programm sollte auch bei einem
Neustart des Master Bricks oder einer verlorenen WLAN-Verbindung weiter
funktionieren. Es ist sogar möglich, das Temperature oder LCD 20x4 Bricklet
auszutauschen, da das Programm die UID aus der Enumerierung benutzt.

C#
--

`Download (ExampleRugged.cs) <https://raw.githubusercontent.com/Tinkerforge/doc/master/de/source/Tutorials/Tutorial_Rugged/ExampleRugged.cs>`__

.. literalinclude:: ExampleRugged.cs
 :language: csharp
 :linenos:
 :tab-width: 4

Python
------

`Download (example_rugged.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/de/source/Tutorials/Tutorial_Rugged/example_rugged.py>`__

.. literalinclude:: example_rugged.py
 :language: python
 :linenos:
 :tab-width: 4
