
.. _tutorial_first_steps:

Tutorial - Erste Schritte
=========================

Das folgende Tutorial demonstriert wie :ref:`Bricks <primer_bricks>`
und :ref:`Bricklets <primer_bricklets>` mit der
:ref:`Programmierschnittstelle <programming_interface>` verwendet werden können.

Im ersten Teil wird ein :ref:`DC Brick <dc_brick>` verwendet, um einen Motor
zu steuern. Danach wird der Aufbau erweitert, um die Geschwindigkeit des Motors
über ein Dreh-`Potentiometer <https://de.wikipedia.org/wiki/Potentiometer>`__
regeln zu können, indem ein :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`
angeschlossen wird. Schlussendlich wird gezeigt, wie durch das Stapeln von Bricks
die Verkabelung minimiert wird und wie die Kommunikation über drahtlose oder
kabelgebundene Schnittstellen abläuft.


Ein einzelner Brick
-------------------

Der DC Brick dient hier als Beispiel. Die beschriebenen Konzept gelten aber für
alle Bricks. :ref:`Hier <primer_bricks>` ist eine Übersicht über alle
verfügbaren Bricks.


Phase 1: Testen
^^^^^^^^^^^^^^^

Um den DC Brick testen zu können, müssen
:ref:`Brick Daemon <brickd>` und :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
bzw. :ref:`hier <brickv_installation>` klicken). Der Brick Viewer muss mit
dem Brick Daemon durch Klicken des "Connect"-Knopf des Brick
Viewers verbunden sein.

Der Brick Daemon bildet eine Brücke zwischen Bricks/Bricklets und den
programmiersprachenspezifischen API Bindings. Der Brick Viewer bietet eine
graphische Oberfläche zu Testzwecken.

Nach der Installation kann das Basteln losgehen! Zuerst müssen ein
Motor und eine Stromversorgung (z.B. eine Batterie), wie auf dem folgenden
Bild gezeigt, angeschlossen werden. Es kann z.B. auch ein Servo Brick mit einem Servomotor anstatt eines
DC Bricks mit Gleichstrommotor verwendet werden.

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick mit angeschlossenem Motor
   :align: center
   :target: ../../_images/Bricks/brick_dc_motor_setup_1200.jpg

Jetzt muss der Brick per USB an den PC angeschlossen werden. Einen Moment später sollte
im Brick Viewer ein neuer Tab namens "DC Brick" auftauchen. Nach Auswahl dieses Tabs
sollte der Brick Viewer so aussehen:

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick Tab im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

Auf der rechten Seite wird die externe Eingangsspannung unter "External Voltage",
der Stromverbrauch des angeschlossenen Motors unter "Current Consumption" und
die aktuelle Geschwindigkeit als Tachometer angezeigt. Die Regler auf
der linken Seite ermöglichen es die Geschwindigkeit, Beschleunigung und
`PWM <https://de.wikipedia.org/wiki/Pulsweitenmodulation>`__-Frequenz für den
Motor einzustellen. Um die Treiberstufe und damit die Ansteuerung des Motors
zu aktivieren, muss das "Enable DC Motor"-Häkchen gesetzt werden.


Phase 2: Ein eigenes Programm schreiben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der DC Brick mit Motor und Stromquelle ist getestet, es kann nun ein erstes eigenes Programm,
dass den DC Brick steuert, geschrieben werden.

Das eigene Programm kann mit jeder der :ref:`unterstützten Programmiersprachen <api_bindings>`
geschrieben werden. In diesem Tutorial wird `Python <https://www.python.org>`__
verwendet.

Dieses Tutorial sollte es ermöglichen, zusammen mit den Beispielen in den 
API Dokumentationen der verschiedenen Produkte, jeden Brick mit allen 
unterstützen Programmiersprachen zu verwenden.

Im Folgenden wird angenommen, dass die Grundlagen der gewählten
Programmiersprache bekannt und die notwendigen Entwicklungswerkzeuge
bereits installiert sind.

Als erstes müssen API Bindings für die entsprechenden Programmiersprache
installiert werden. Passende Anleitungen dazu gibt es
:ref:`hier <api_bindings>`.

Dann muss ein neuer Ordner für das DC Brick-Testprojekt erstellt und eines
der :ref:`Beispiele <dc_brick_python_examples>` für den DC Brick als
Ausgangspunkt in diesen Ordner heruntergeladen werden.

Nun folgt ein Blick auf ``example_configuration.py``:

.. literalinclude:: /Software/Bricks/DC_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

**Zeile 12** erstellt ein IP-Connection-Objekt.

**Zeile 13** erzeugt ein DC Brick Objekt, über welches der eigentliche DC Brick
gesteuert werden kann. Dabei müssen die eindeutige Identifikationsnummer (UID)
des DC Bricks (in diesem Falle steht sie in **Zeile 6**), sowie das ``ipcon``
Objekt übergeben werden.

.. note::
 Die einfachste Möglichkeit, die UID eines Bricks zu ermitteln, ist über der
 Brick Viewer. Wenn der Brick über USB an den PC angeschlossen ist, zeigt der
 Brick Viewer dessen UID im "Setup"-Tab an.

In **Zeile 15** wird die IP-Connection verbunden. Es ist möglich, das Programm 
auf einem anderen PC, als dem, auf dem der Brick Daemon läuft, auszuführen.
Zum Beispiel kann das Programm für ein Smartphone geschrieben werden, das den Brick 
steuert, der am PC angeschlossen ist.

Die **Zeilen 18-23** konfigurieren den DC Brick und lassen den Motor mit voller
Geschwindigkeit vorwärts laufen.

Die **Zeilen 25-27** sorgen dafür, dass das Programm weiter läuft, bis die Enter-Taste
gedrückt wird. Danach wird der Motor abgeschaltet.

Dieses Python-Skript oder eines der anderen Beispiele kann nun ausgeführt, oder als
Ausgangspunkt für ein eigenes Projekt verwendet werden.

.. note::
 Eine vollständige Beschreibung der API und weitere Beispiele finden sich auch
 der Beschreibungsseite jedes Produkts. Im Falle des DC Bricks :ref:`hier
 <dc_brick_programming_interface>`.


Bricklets anschließen für weitere Features
------------------------------------------

Bricklets können genutzt werden, um die Fähigkeiten von Bricks zu erweitern.
:ref:`Hier <primer_bricklets>` findet sich eine Übersicht über alle
verfügbaren Bricklets.

Um ein Bricklet nutzen zu können, muss es über das mitgelieferte
Kabel an einen Brick angeschlossen werden, wobei der Brick währenddessen
nicht mit Strom versorgt werden darf.

Als Beispiel dient ein :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>` und
der :ref:`DC Brick <dc_brick>` aus dem ersten Teil des Tutorials. Die Konzepte
gelten aber für alle Bricks und Bricklets.


Phase 1: Testen
^^^^^^^^^^^^^^^

Zuerst muss das Rotary Poti Bricklet an den DC Brick, wie im folgenden Bild
gezeigt, angeschlossen werden.

.. image:: /Images/Tutorial/tutorial_1_600.jpg
   :scale: 100 %
   :alt: DC Brick mit angeschlossenen Motor und Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_1_1200.jpg

Wenn jetzt der DC Brick über USB angeschlossen wird, taucht neben dem "DC Brick"-Tab
ein "Rotary Poti Bricklet"-Tab im Brick Viewer auf. Im Tab wird die aktuelle Position
des Potentiometers dargestellt, die sich abhängig von der Drehung ändert.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet Tab im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg


Phase 2: Ein eigenes Programm schreiben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um das Rotary Poti Bricklet in das Projekt aufzunehmen kann nun das Programm so
abgeändert werden, dass die Position des Potentiometers die Geschwindigkeit des
Motors bestimmt. Das abgeänderte Programm sieht wie folgt aus (`Download
<https://raw.githubusercontent.com/Tinkerforge/doc/master/de/source/Tutorials/Tutorial_Extending/tutorial_brick_bricklet_test.py>`__):

.. literalinclude:: tutorial_brick_bricklet_test.py
 :language: python
 :linenos:
 :tab-width: 4

Die **Zeilen 4-7** sind die typische Konfiguration. Die UIDs müssen die der
verwendeten Bricks und Bricklets sein.

Die **Zeilen 22-27** erstellen die IP-Connection zum Brick Daemon. Die Brick- und
Bricklet-Objekte werden erzeugt.

Das Rotary Poti Bricklet wird so konfiguriert, das die Funktion ``cb_position``
jedes Mal aufgerufen wird, wenn sich die Position des Potentiometers ändert.
**Zeile 29** stellt diesen Callback so ein, dass er mit einer Periode von
50 ms ausgelöst wird, wenn sich die Position ändert. Wenn sich die Position nicht
ändert werden keine Callbacks ausgelöst. Dieses Vorgehen ist effizient, es wird
nur die unbedingt notwendige USB-Bandbreite verwendet.
Die Callback-Funktion wird in **Zeile 30** registriert. ``cb_position``
(definiert in den **Zeilen 16-19**) setzt abhängig von der aktuelle Position des
Potentiometers eine neue Geschwindigkeit für den Motor.

Die **Zeilen 32-33** schalten die Motorsteuerung ein und setzen die
Beschleunigung auf Maximum. Dadurch kann die Motorgeschwindigkeit den Änderungen
der Potentiometerposition direkt folgen.

Die **Zeilen 35-37** sorgt dafür, dass das Programm weiter läuft, bis die 
Enter-Taste gedrückt wird. Der Motor wird danach abgeschaltet.


.. _tutorial_first_steps_build_stacks:

Stapel bauen
------------

Um Verkabelung und Raum zu sparen, können Bricks gestapelt werden.
Der unterste Brick eines Stapels muss ein :ref:`Master Brick <master_brick>` sein.
Dieser kümmert sich um das Routen von Nachrichten zwischen PC und allen
Stapelteilnehmern. Nachrichten vom PC werden per USB, oder über eine
::ref:`Master Extension <primer_master_extensions>` an den Stapel übertragen.

Das Stapeln ist transparent, das bedeutet, dass **keine Änderungen am Programm**
notwendig sind, um zwischen mehreren einzelner Bricks und einem Stapel
aus den selben Bricks mit nur einer USB-Verbindung zu wechseln. Die USB-Verbindung muss
zum untersten Master Brick bestehen.

Ein Stapel kann mehrere Master Bricks enthalten. Dabei agiert aber nur der
unterste Master Brick als Master des Stapels und kümmert sich um das Routen von
Nachrichten. Die anderen Master Bricks im Stapel können genutzt werden, um
mehr Bricklets an den Stapel anzuschließen.

Der Master des Stapels versorgt alle Teilnehmer des Stapels über seine USB-Verbindung
mit in Summe maximal 500mA. Die Motorspannung kann bei jedem Motortreiber-Brick über
seinen schwarzen Stromversorgungsstecker auf der Platine eingespeist werden.
Um nochmal Verkabelung zu sparen und den Stapel mit mehr Strom versorgen
zu können, kann eine :ref:`Stromversorgung <primer_power_supplies>`
unter den Stapel gesteckt werden (unter den Master des Stapels). Von dort stellt
sie die 5V bereit, die von Bricks und Bricklets benötigt werden. Motortreiber-Bricks,
deren Motorspannung nicht über ihren eigenen schwarzen Stromversorgungsstecker eingespeist
wird, beziehen die Motorspannung direkt von der Versorgung der Stromversorgungsplatine.
Wenn also die Stromversorgungsplatine mit 20V gespeist wird, dann stehen diese
20V den Motortreiber-Brick auch als Motorspannung zur Verfügung.

Da bei Verwendung einer Stromversorgung im Stapel die USB-Verbindung nicht mehr
für die Stromversorgung verwendet wird, erlaubt dieser Aufbau die Verwendung von
Bricks an Embedded Boards, die ansonsten nicht in der Lage wären, den Stapel mit
ausreichend Strom zu versorgen.

Der Master des Stapels kann die externe Versorgungsspannung der Stromversorgung,
sowie den Stromverbrauch des gesamten Stapels, messen.

.. note::
 Jeder Motortreiber-Brick schaltet automatisch zwischen externer Versorgung über
 seinen eigenen schwarzen Stromversorgungsstecker und Versorgung über den
 Stapel um. Das bedeutet, dass, wenn ein Motor zuvor extern versorgt wurde, ein
 Abstecken oder Abschalten der externen Versorgung dazu führt, dass der Motor dann
 direkt über den Stapel versorgt wird. Dies sollte unbedingt bedacht werden!

Im Folgenden wird der bisherigen Aufbau aus DC Brick und Rotary Poti
Bricklet um einen Master Brick und eine Step-Down Power Supply erweitert.

.. note::
 Die weiße Ecke jedes Bricks zeigt an, in welcher Ausrichtung zwei Bricks
 zusammengesteckt werden können.


Phase 1: Testen
^^^^^^^^^^^^^^^

Der bisherige Stapel muss nun, wie in folgendem Bild dargestellt, (von unten nach oben) aus Step-Down Power Supply mit
angeschlossener Batterie, einem Master Brick mit angeschlossenem Rotary Poti
Bricklet und einem DC Brick mit angeschlossenem Motor aufgebaut werden.

.. image:: /Images/Tutorial/tutorial_2_600.jpg
   :scale: 100 %
   :alt: DC Brick im Stapel mit Master Brick und Step-Down Power Supply, mit angeschlossenem Motor und Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_2_1200.jpg

Einen Moment nachdem der Master Brick über USB an den PC angeschlossen wurde,
sollte der Brick Viewer Tabs für den Master Brick, den DC Brick und das Rotary Poti Bricklet anzeigen.
Auf dem Master Brick sollte eine von Null verschiedene Strom- und
Spannungsmessung zu sehen sein.


Phase 2: Ein eigenes Programm schreiben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das Stapeln von Bricks ist für die API transparent, daher kann das Programm
aus dem vorherigen Abschnitt ohne Änderungen weiterverwendet werden!


Stapel querverbinden
--------------------

Die bisher gezeigten Stapel in diesem Tutorial sind nicht besonders spannend,
sie sparen vornehmlich Verkabelung und Platz ein. Aber das Stapelkonzept kann
mehr. Es erlaubt **Master Extensions** auf den Stapel zu stecken, um die
Kommunikationsmöglichkeiten des Stapels über USB hinaus zu erweitern, zum Beispiel
durch :ref:`RS485 <rs485_extension>`, :ref:`Wi-Fi <wifi_extension>` oder :ref:`Ethernet <ethernet_extension>`.

Um einen RS485-Bus zwischen zwei Stapeln zu bauen, werden noch ein Master Brick
und zwei RS485 Extensions zusätzlich zu den bisher verwendeten Teilen
benötigt. Auf jeden Master Brick wird jeweils eine RS485 Extension gesteckt
und die beiden Extensions passend miteinander verkabelt. Jetzt muss noch das
Rotary Poti Bricklet an den neu zusammengesteckten Stapel angeschlossen werden.

Als nächster Schritt muss jetzt jeder Stapel einzeln über USB am PC angeschlossen
und konfiguriert werden. Die Details dazu sind in der :ref:`RS485 Dokumentation
<rs485_extension_configuration>` beschrieben. Wichtig ist, dass nach der
Konfiguration der RS485 Slave vor dem RS485 Master gestartet wird.

Jetzt sollten im Brick Viewer die zwei Master Bricks, das Rotary Poti Bricklet
und der DC Brick auftauchen. Wenn das der Fall ist, kann jetzt das vorherige
Programm ohne Änderung weiterverwendet werden.
