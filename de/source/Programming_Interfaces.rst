.. _pi:

Programmierschnittstellen
=========================


.. _pi_hlpi:

High Level Programmierschnittstelle (HLPI)
------------------------------------------

Die High Level Programmierschnittstelle verwendet vorprogrammiert Geräte
(Bricks und Bricklets) die von einem PC aus gesteuert werden. Jedes Geräte
hat seine eigene eindeutige Identifikationsnummer (UID).

Der Benutzer ruft Funktionen auf den Geräten auf. Die Anbindung dieser
Funktionen ist in den :ref:`API Bindings <api_bindings>` implementiert und das
Gerät wird über seine UID spezifiziert.

Beim Aufruf einer Funktion wird durch die API Bindings ein Datenpaket erzeugt,
das dann zum :ref:`Brick <product_overview_bricks>` mit der entsprechenden UID
geschickt wird. Der Brick führt die im Datenpaket definierte Funktion aus.
Zum Beispiel, beim Aufrufe von "getTemperature()" liest der Brick die Temperatur
des Temperatursensors aus und schickt diese in einem Datenpaket zurück. Der
Funktionsaufruf des Benutzers blockiert bis die Antwort vom Brick eingetroffen
ist und gibt dann die gemessene Temperatur zurück.

Falls eine :ref:`Bricklet <product_overview_bricklets>` Funktion aufgerufen
wird, Dann wird das Datenpaket an den Brick geschickt an dem das Bricklet
angeschlossen ist. Dieser Brick führt dann die entsprechende Funktion aus, die
im `EEPROM <http://de.wikipedia.org/wiki/Electrically_Erasable_Programmable_Read-Only_Memory>`__
des Bricklets gespeichert ist.

Diese Programmierschnittstelle ist für Windows, Linux und Mac OS sowie mobile
Betriebssystem wie Android, iOS und Windows Mobile verfügbar.

.. note::
 Das :ref:`tutorial` vermittelt weitere Informationen wie diese Konzept
 verwendet werden kann.


.. _pi_odpi:

On Device Programmierschnittstelle (ODPI)
-----------------------------------------

Die On Device Programmierschnittstelle (ODPI) ist eine API, die es erlaubt
eigene Firmwares für Bricks zu entwickeln.

.. warning::
 Im Moment sind nur die Quelltexte der Bricks `online
 <https://github.com/organizations/Tinkerforge>`__ verfügbar. Falls du in der
 Lage bist die passende Entwicklungsumgebung aufzusetzen und C programmieren
 kannst, dann kannst du jetzt schon den Quelltext für deine Zwecke abändern.

 Eine einfache API (vergleichbar der Arduino API) für einfache
 Firmwareentwicklung ist in Arbeit.
