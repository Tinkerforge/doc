
.. _saleae_high_level_analyzer:

Saleae Logic High Level Analyzer
================================

Der Tinkerforge Saleae Logic High Level Analyzer ist eine
Erweiterung für `Saleae Logic 2 <https://www.saleae.com/downloads/>`__.
Er vereinfacht die Analyse der Kommunikation mit Co-MCU Bricklets deutlich.

Der Analyzer kann mitgelesene SPI-Kommunikation in SPITFP- und TFP-Pakete
parsen. Er enthält eine Datenbank aller Funktionen von Bricks und Bricklets.

Der Analyzer kann beim Debugging von Problemen helfen, die bei der Entwicklung
neuer Bricklets mit dem :ref:`XMC1400 Breakout Bricklet <xmc1400_breakout_bricklet>`
entstehen.

..
 oder wenn neue Hardware-Abstraction-Layer für die Low-Level C Bindings entwickelt werden.
 
.. image:: /Images/Screenshots/saleae_hla.png
   :scale: 100 %
   :alt: Saleae High Level Analyzer
   :align: center
   :target: ../_images/Screenshots/saleae_hla.png

Hardware
--------

Um SPI-Kommunikation mitzulesen, muss ein Adapter gebaut werden. Hierfür
können zum Beispiel zwei :ref:`Breakout Bricklets <breakout_bricklet>` mit einem
Pin Header zusammengelötet werden.

Wenn das :ref:`XMC1400 Breakout Bricklet <xmc1400_breakout_bricklet>` verwendet wird,
kann die SPI-Kommunikation an den Pins, die mit CS, CLK, MOSI und MISO markiert sind,
mitgelesen werden

Installation
------------

Der Analyzer benötigt eine aktuelle Version der Saleae Logic 2 Alpha.
Er wurde mit Version 2.2.15 getestet, sollte aber mit Versionen ab 2.2.9
funktionieren.

Der Analyzer kann `hier heruntergeladen <https://download.tinkerforge.com/bindings/saleae/>`__ werden. Danach
muss die ZIP-Datei entpackt werden.

In Logic 2 kann der Analyzer als Extension hinzugefügt werden. Dann sollte
es möglich sein, den SPITFP Analyzer hinzuzufügen.

Konfiguration
-------------

Die folgenden Optionen können konfiguriert werden:

* Input Analyzer: Das unterliegende Protokol. Sollte immer SPI sein.
* Output Format: Pakete mit großen Payloads erzeugen möglicherweise einen großen Graph Overlay Text. Falls nötig kann hier die Menge des Texts auf nur die Protokoll-Header oder den Payload reduziert werden.
* Direction: Wählt das SPI-Signal aus, das analysiert wird. MOSI entspricht den Nachrichten, die zum Bricklet geschickt werden. MISO entspricht den Nachrichten, die vom Bricklet erstellt wurden.
* Device: Hier kann der Typ des angeschlossenen Geräts ausgewählt werden. Das ist notwendig, damit der Analyzer Funktions-IDs und Payload parsen kann.

Es ist möglich, mehrere Instanzen des Analyzers anzulegen. Damit können
beide Kommunikationsrichtungen (zum/vom Bricklet) gleichzeitig analysiert werden.
Es ist außerdem möglich, mehrere Ausgabe-Zeilen für große Pakete zu erzeugen, indem eine Instanz
mit dem "Headers" und einem mit dem "Payload"-Ausgabeformat angelegt wird. Die Ausgabe erscheint dann
wie im obigen Screenshot.
