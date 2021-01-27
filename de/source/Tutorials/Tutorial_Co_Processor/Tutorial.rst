
.. _tutorial_eeprom_vs_co_processor:

Tutorial - Bricklets mit EEPROM vs Co-Prozessor 
===============================================

Anfang 2017 haben wir angefangen alle existierenden Bricklets durch neue
Versionen zu ersetzen. Diese neuen Versionen haben einen Co-Prozessor 
anstelle eines EEPROMs sowie einen anderen Stecker.

Das Neuentwickeln und Ersetzen von ca. 50 Bricklets war natürlich
eine Mammutaufgabe. Warum haben wir das gemacht?


Alte Bricklets mit EEPROM
-------------------------

Bei den alten Bricklets mit EEPROM war es so, dass auf den Bricklets je 
nach Funktion Sensoren, Analog-Digital-Wandler, LEDs, 
Schnittstellenerweiterungen usw. verbaut waren, die direkt vom Prozessor 
des angeschlossenen Bricks gesteuert wurden. Dieses Konzept hat den Vorteil, 
das für einfache Bricklets kein großer Bauteilaufwand notwendig ist. 
Technisch hatte jedes Bricklet ein EEPROM welches Code für den jeweiligen 
Brick beinhaltet. Dieser Code wurde von den Bricks in den eigenen Flash
geschrieben und periodisch ausgeführt. Dadurch musste ein Brick nicht 
jedes einzelne Bricklet kennen und die große Vielfalt des Baukastensystems 
wurde somit ermöglicht.

Nachteilig war, dass der Prozessor auf dem Brick alle angeschlossenen
Bricklets und seine eigene Brick-Funktionalität verarbeiten musste. 
Anwendungen, wie zum Beispiel Frequenzzähler o.ä., bei denen permanent auf 
ein Signal reagiert werden muss, waren daher nicht zu realisieren. Ein
weiterer Nachteil war, dass der Code auf den Bricklets nur zu den 
SAM3 und SAM4 Prozessoren von Atmel kompatibel war. Früher konnten wir 
von einer langen Verfügbarkeit dieser Prozessoren ausgehen. Nach der 
Übernahme von Atmel durch Microchip war dies leider nicht mehr sichergestellt.

Auf Grund dieser Probleme hatten wir uns entschieden alle alten Bricklets
durch neue mit Co-Prozessor zu ersetzen.


Neue Bricklet mit Co-Prozessor
------------------------------

Die neuen Bricklets haben einen eigenen Co-Prozessor, dieser hat nur
zwei Aufgaben:

* Die Bricklet-Funktionalität zu implementieren und
* mit dem Brick zu kommunizieren.

Verglichen mit den alten Bricklets mit EEPROM, haben die neuen Bricklets
mit Co-Prozessor ein festes Protokoll, welches auf jedem Prozessor
implementiert werden kann. Daher benötigen die Bricks keinen speziellen
Prozessor mehr.

Zusätzlich können wir jetzt Bricklets haben die

* große Datenmengen verarbeiten (z.B. `Thermal Imaging Bricklet <https://www.tinkerforge.com/de/doc/Hardware/Bricklets/Thermal_Imaging.html>`__),
* in real-time auf Flankenwechsel reagieren (z.B. `Industrial Counter Bricklet <https://www.tinkerforge.com/de/doc/Hardware/Bricklets/Industrial_Counter.html>`__) oder
* komplizierte Berechnungen durchführen (z.B. `Sound Pressure Level Bricklet <https://www.tinkerforge.com/de/doc/Hardware/Bricklets/Sound_Pressure_Level.html>`__).

Während man die alten Bricklets mit EEPROM nur mit Bricks verbinden konnte,
können die neuen Bricklets in Theorie von jedem Gerät ausgelesen werden
welches SPI spricht.

Das ermöglichte es uns das Isolator Bricklet sowie den HAT Brick und den
HAT Zero Brick zu implementieren.

Es gibt viele weitere kleine technische Vorteile welche die Performance
sowie Robustheit der neuen Bricklets erhöhen.

Zu guter Letzt konnten wir die alten 10-Pol Stecker durch neue robusterere
und benutzerfreundlichere 7-Pol Stekcer ersetzten. Eine detaillierte
Beschreibung des Steckerwechsels kann :ref:`hier <tutorial_bricklet_cables>` 
gefunden werden

Es hat 2,5 Jahre sowie viele viele Personenstunden gedauert die neuen Bricklets
zu entwickeln und die alten zu ersetzen. Nichtsdestotrotz sind wir im
Nachhinein sehr glücklich über das Resultat und sind uns auch sicher
dass sich der Aufwand gelohnt hat.
