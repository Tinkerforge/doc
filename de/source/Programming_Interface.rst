
.. _programming_interface:

Programmierschnittstelle
========================

Die Programmierschnittstelle verwendet vorprogrammierte Geräte
(:ref:`Bricks <primer_bricks>` und 
:ref:`Bricklets <primer_bricklets>`) die von einem (Embedded-) PC, 
Tablet oder Smartphone aus gesteuert werden können. Jedes Gerät
hat seine eigene eindeutige Identifikationsnummer (UID).

Der Benutzer ruft eine Funktion, implementiert in den
:ref:`API Bindings <api_bindings>`, für ein Gerät das mit seiner UID 
spezifiziert wird, auf. Diese Funktion erzeugt dann wiederum ein TCP/IP
Datenpaket, welches dann zu dem :ref:`Brick <primer_bricks>` mit 
der entsprechenden UID geschickt wird.

Ist das Brick per USB mit einem Computer verbunden, so muss noch ein 
Programm :ref:`Brick Daemon <brickd>` genannt installiert werden. Es dient als
Übersetzer zwischen TCP/IP und USB.
Manche :ref:`Master Extensions <primer_master_extensions>` können 
genutzt werden um auf diesen Computer zu verzichten. Sie können direkt TCP/IP
Pakete annehmen. Ein Beispiel hierfür ist die 
:ref:`WIFI Extension <wifi_extension>`.

Nachdem von einem Brick ein Paket empfangen wurde, führt dieser die im 
Datenpaket definierte Funktion aus. Zum Beispiel beim Aufruf von 
``getTemperature()`` liest der Brick die Temperatur des Temperatursensors aus und
schickt diese in einem Datenpaket zurück. Der Funktionsaufruf des Benutzers 
blockiert bis die Antwort vom Brick eingetroffen ist und gibt dann die 
gemessene Temperatur zurück.

Falls eine :ref:`Bricklet <primer_bricklets>` Funktion aufgerufen
wird, wird das Datenpaket an den Brick geschickt an dem das Bricklet
angeschlossen ist. Dieser Brick führt dann die entsprechende Funktion aus.

Die Bricklet Funktion ist anfangs im 
`EEPROM <https://de.wikipedia.org/wiki/Electrically_Erasable_Programmable_Read-Only_Memory>`__
des Bricklets, zusammen mit anderen Daten wie die UID (zusammen genannt Plugin), 
gespeichert. Beim Booten wird diese Funktion, zusammen mit anderen, in den Flash 
des angeschlossenen Bricks geladen 
(`positionsunabhängiger Code <https://de.wikipedia.org/wiki/Position-Independent_Code>`__).
Beim Aufruf kann diese Funktion nun, genauso wie jede andere Brick Funktion,
aus dem Flash ausgeführt werden. Dieser Ansatz ermöglicht es eine 
Kompatibilität zwischen allen Bricks und Bricklets herzustellen.

Diese Programmierschnittstelle ist für Windows, Linux und Mac OS X sowie mobile
Betriebssystem wie Android, iOS und Windows Phone verfügbar.

.. note::
 Dieses :ref:`Tutorial <tutorial_first_steps>` vermittelt weitere Informationen
 wie diese Konzept verwendet werden kann.
