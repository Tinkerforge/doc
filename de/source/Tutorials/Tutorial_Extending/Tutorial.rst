
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#tutorials-und-faq">Tutorials und FAQ</a> / Erste Schritte - Tutorial

.. _tutorial_first_steps:

Erste Schritte - Tutorial
=========================

Das folgende Tutorial demonstriert wie :ref:`Bricks <primer_bricks>`
und :ref:`Bricklets <primer_bricklets>` mit der
:ref:`Programmierschnittstelle <programming_interface>` verwendet werden können.

Im ersten Teil wird ein :ref:`DC Brick <dc_brick>` verwendet, um einen Motor
zu steuern. Danach wird der Aufbau erweitert um die Geschwindigkeit des Motors
über ein Dreh-`Potentiometer <http://de.wikipedia.org/wiki/Potentiometer>`__
regeln zu können indem wir ein :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`
anschließen. Am Ende geht es um das Stapeln von Bricks um Verkabelung zu sparen
und um die Kommunikation über drahtlose oder kabelgebundene Schnittstellen.


Ein einzelner Brick
-------------------

Der DC Brick dient hier als Beispiel. Die beschriebenen Konzept gelten aber für
alle Bricks. :ref:`Hier <primer_bricks>` ist eine Übersicht über alle
verfügbaren Bricks.


Phase 1: Testen
^^^^^^^^^^^^^^^

Um den DC Brick testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken). Der Brick Viewer muss mit
dem Brick Daemon verbunden sein, klicke dazu auf den "Connect" Knopf des Brick
Viewers.

Der Brick Daemon bildete eine Brücke zwischen Bricks/Bricklets und den
programmiersprachenspezifischen API Bindings. Der Brick Viewer bietet eine
graphische Oberfläche für Testzwecke.

Nach der Installation kann das Basteln losgehen! Schließe als erstes einen
Motor und eine Stromversorgung (z.B. eine Batterie) an, wie auf dem folgenden
Bild zu sehen. Es kann z.B. auch einen Servo Brick und einen Servo anstatt eines
DC Bricks verwendet werden.

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick mit angeschlossenem Motor
   :align: center
   :target: ../../_images/Bricks/brick_dc_motor_setup_1200.jpg

Schließe jetzt den Brick per USB an den PC an. Einen Moment später im Brick
Viewer ein neuer Tab namens "DC Brick" auftauchen. Wähle diesen Tab aus.
Der Brick Viewer sollte nun so aussehen:

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick Tab im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

Auf der rechten Seite wird die externe Eingangsspannung unter "External Voltage",
der Stromverbrauch des angeschlossenen Motors unter "Current Consumption" und
die aktuelle Geschwindigkeit als Tachometer angezeigt. Verschiedene Regler auf
der linken Seite ermöglichen es die Geschwindigkeit, Beschleunigung und
`PWM <http://de.wikipedia.org/wiki/Pulsweitenmodulation>`__ Frequenz für den
Motor einzustellen. Um die Treiberstufe und damit die Ansteuerung des Motors
zu aktivieren muss das "Enable" Häkchen gesetzt werden.


Phase 2: Ein eigenes Programm schreiben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der DC Brick mit Motor und Stromquelle sind nun getestet, es spricht nun nichts
mehr dagegen das erstes eigenes Programm zu schreiben, dass den DC Brick
steuert.

Dies kann mit jeder der :ref:`unterstützten <api_bindings>` Programmiersprachen
geschrieben werden. In diesem Tutorial wird `Python <http://www.python.org>`__
verwendet.

Dieses Tutorial sollte es dir ermöglichen, zusammen mit den Beispielen in den 
API Dokumentationen der verschiedenen Produkte, jeden Brick mit allen 
unterstützen Programmiersprachen zu verwenden.

Im Folgenden wird angenommen, dass die Grundlagen der gewählten
Programmiersprache bekannt und die notwendigen Entwicklungswerkzeuge
bereits installiert sind.

Als erstes müssen API Bindings für die entsprechenden Programmiersprache
installiert werden. Passende Anleitungen dazu gibt es
:ref:`hier <api_bindings_install_and_usage>`.

Erstelle dann einen neuen Ordner für das DC Brick Testprojekt und lade eines
der :ref:`Beispiele <dc_brick_python_examples>` für den DC Brick als
Ausgangspunkt in diesen Ordner herunter.

Nun folgt ein Blick auf ``example_configuration.py``:

.. literalinclude:: /Software/Bricks/DC_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

**Zeile 12** erstellt ein IP Connection Objekt.

**Zeile 13** erzeugt ein DC Brick Objekt über welches der eigentliche DC Brick
gesteuert werden kann. Dabei müssen die eindeutige Identifikationsnummer (UID)
des DC Bricks (in diesem Falle steht sie in **Zeile 6**), sowie das ``ipcon``
Objekt übergeben werden.

.. note::
 Die einfachste Möglichkeit die UID eines Bricks zu ermitteln ist über der
 Brick Viewer. Wenn der Brick über USB an den PC angeschlossen ist zeigt der
 Brick Viewer dessen UID im "Setup" Tab an.

In **Zeile 15** Die IP Connection wird verbunden. Es ist möglich das Programm 
auf einem anderen PC, als dem auf dem der Brick Daemon läuft, auszuführen 
(z.B. kann das Programm für ein Smartphone schreiben, das dann den Brick 
steuert, der am PC angeschlossen ist).

Die **Zeilen 18-23** konfigurieren DC Brick und lassen den Motor mit voller
Geschwindigkeit vorwärts laufen.

**Zeile 25-27** sorgt dafür, dass das Programm weiter läuft bis die Enter Taste
gedrückt wird. Der Motor wird danach abgeschaltet.

Führe diese Python Script aus und verwende es oder eines der anderen Beispiele
als Ausgangspunkt für ein eigenes Projekt.

.. note::
 Eine vollständige Beschreibung der API und weitere Beispiele finden sich auch
 der Beschreibungsseite jedes Produkts. Im Falle des DC Bricks :ref:`hier
 <dc_brick_programming_interface>`.


Bricklets anschließen für weitere Features
------------------------------------------

Bricklets können genutzt werden um die Fähigkeiten von Bricks zu erweitern.
:ref:`Hier <primer_bricklets>` findet sich eine Übersicht über alle
verfügbaren Bricklets.

Um ein Bricklet nutzen zu können muss es an einen Brick über das mitgelieferte
Kabel angeschlossen werden, wobei der Brick dabei nicht mit Strom versorgt sein
darf.

Als Beispiel dient ein :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>` und
der :ref:`DC Brick <dc_brick>` aus dem ersten Teil des Tutorials. Die Konzepte
gelten aber für alle Bricks und Bricklets.


Phase 1: Testen
^^^^^^^^^^^^^^^

Schließe das Rotary Poti Bricklet an den DC Brick an wie im folgenden Bild
gezeigt.

.. image:: /Images/Tutorial/tutorial_1_600.jpg
   :scale: 100 %
   :alt: DC Brick mit angeschlossenen Motor und Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_1_1200.jpg

Wenn der DC Brick über USB angeschlossen wird, dann taucht neben dem "DC Brick"
Tab noch ein "Rotary Poti Bricklet" Tab im Brick Viewer auf. Wähle den "Rotary
Poti Bricklet" Tab und drehe am Knopf des Potentiometers. Im Brick Viewer wird
die Drehung entsprechend dargestellt.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet Tab im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg


Phase 2: Ein eigenes Programm schreiben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um das Rotary Poti Bricklet in das Projekt aufzunehmen wird nun das Programm so
abgeändert, dass die Position des Potentiometers die Geschwindigkeit des
Motors bestimmt. Das abgeänderte Programm sieht wie folgt aus (`Download
<https://raw.githubusercontent.com/Tinkerforge/doc/master/de/source/Tutorials/Tutorial_Extending/tutorial_brick_bricklet_test.py>`__):

.. literalinclude:: tutorial_brick_bricklet_test.py
 :language: python
 :linenos:
 :tab-width: 4

Die **Zeilen 4-7** sind die typische Konfiguration, die UIDs müssen die der
verwendeten Bricks und Bricklets sein.

Die **Zeilen 22-27** erstellen die IP Connection zum Brick Daemon. Die Brick und
Bricklet Objekte werden erzeugt.

Das Rotary Poti Bricklet wird so konfiguriert, das die Funktion ``cb_position``
jedes Mal aufgerufen wird wenn sich die Position des Potentiometers ändert.
**Zeile 29** stellt diesen Callback so ein, dass er mit einer Periode von
50ms ausgelöst wird wenn sich die Position ändert. Wenn sich die Position nicht
ändert werden keine Callbacks ausgelöst. Dieses Vorgehen ist effizient, es wird
nur die unbedingt notwendige USB Bandbreite verwendet.
Die Callback Funktion wird in **Zeile 30** registriert. ``cb_position`` ist in
den **Zeilen 16-19** definiert, es setzt eine neue Geschwindigkeit für den
Motor abhängig von der aktuelle Position des Potentiometers.

Die **Zeilen 32-33** schalten die Motorsteuerung ein und setzen die
Beschleunigung auf Maximum. Dadurch kann die Motorgeschwindigkeit den Änderungen
der Potentiometerposition direkt folgen.

Die **Zeile 35-37** sorgt dafür, dass das Programm weiter läuft bis die Enter
Taste gedrückt wird. Der Motor wird danach abgeschaltet.


.. _tutorial_first_steps_build_stacks:

Stapel bauen
------------

Um Verkabelung und Raum zu sparen können Bricks gestapelt werden.
Ein :ref:`Master Brick <master_brick>` mit USB Verbindung am unteren Ende des
Stapels kümmert sich um das Routen von Nachrichten zwischen PC und allen
Stapelteilnehmern.

Das Stapeln ist transparent, das bedeutet, dass **keine Änderungen am Programm**
notwendig sind zwischen der Verwendung mehrerer Bricks mit jeweils einer eigenen
USB Verbindung und einem Stapel aus den selben Bricks mit nur einer USB
Verbindung zum Master Brick.

Ein Stapel kann auch mehrere Master Bricks enthalten. Dabei agiert aber nur der
unterste Master Brick als Master des Stapels und kümmert sich um das Routen von
Nachrichten. Die anderen Master Bricks im Stapel können z.B. genutzt werden, um
mehr Bricklets an den Stapel anzuschließen.

Der Master des Stapels versorgt alle Teilnehmer des Stapels über seine USB
Verbindung mit maximal 500mA in Summe. Jeder Motortreiber Brick kann über
seinen schwarzen Stromversorgungsstecker auf der Platine extern versorgt werden.
Um nochmal Verkabelung zu sparen und auch den Stapel mit mehr Strom versorgen
zu können kann eine :ref:`Stromversorgung <primer_power_supplies>`
unter den Stapel gesteckt werden (unter den Master des Stapels). Von dort stellt
sie die 5V bereit die von Bricks und Bricklets benötigt werden. Motortreiber
Bricks die nicht über ihren schwarzen Stromversorgungsstecker extern versorgt
werden beziehen den Strom für die Motoren über die 5V Versorgung des Stapels.

Da bei Verwendung einer Stromversorgung im Stapel die USB Verbindung nicht mehr
für die Stromversorgung verwendet wird erlaubt dieser Aufbau die Verwendung von
Bricks mit Embedded Boards die ansonsten nicht in der Lage wären den Stapel mit
ausreichend Strom zu versorgen.

Der Master des Stapels kann die externe Versorgungsspannung der Stromversorgung
messen, sowie den Stromverbrauch des gesamten Stapels.

.. note::
 Jeder Motortreiber Brick schaltet automatisch zwischen externer Versorgung über
 seinen eigenen schwarzen Stromversorgungsstecker und der Versorgung über den
 Stapel um. Das bedeutet, wenn ein Motor zuvor extern versorgt wurde führt ein
 Abstecken oder Abschalten der externen Versorgung dazu, dass der Motor dann
 direkt über den Stapel versorgt wird. Dies sollte unbedingt bedacht werden!

Im Folgenden wird der bisherigen Aufbau aus DC Brick und Rotary Poti
Bricklet um einen Master Brick erweitert.

.. note::
 Die weise Ecke jedes Bricks zeigt an, in welcher Ausrichtung zwei Bricks
 zusammengesteckt werden können.


Phase 1: Testen
^^^^^^^^^^^^^^^

Nun wird ein Stapel (von unten nach oben) aus Step-Down Power Supply mit
angeschlossener Batterie, einem Master Brick mit angeschlossenem Rotary Poti
Bricklet und einem DC Brick mit angeschlossenem Motor benötigt, wie in folgendem
Bild dargestellt.

.. image:: /Images/Tutorial/tutorial_2_600.jpg
   :scale: 100 %
   :alt: DC Brick im Stapel mit Master Brick und Step-Down Power Supply, mit angeschlossenem Motor und Rotary Poti Bricklet
   :align: center
   :target: ../_images/Tutorial/tutorial_2_1200.jpg

Einen Moment nachdem der Master Brick über USB an den PC angeschlossen wurde
sollte der Brick Viewer Tabs für alle drei Teilnehmer des Stapels anzeigen
und auf dem Master Brick sollte eine von Null verschiedenen Strom- und
Spannungsmessung zu sehen sein.


Phase 2: Ein eigenes Programm schreiben
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das Stapeln von Bricks ist für die API transparent, daher kann das Programm
aus dem vorherigen Abschnitt ohne Änderungen weiterverwendet werden!


Stapel querverbinden
--------------------

Die bisher gezeigten Stapel in diesem Tutorial sind nicht besonders spannend,
sie sparen vornehmlich Verkabelung und Platz ein. Aber das Stapelkonzept kann
mehr. Es erlaubt **Master Extensions** auf den Stapel zu stecken um die
Kommunikationsmöglichkeiten des Stapels über USB hinaus zu erweitern. Dazu
gehören :ref:`RS485 <rs485_extension>` und :ref:`WIFI <wifi_extension>`, sowie
die :ref:`Ethernet <ethernet_extension>`.

Um einen RS485 Bus zwischen zwei Stapeln zu bauen werden noch ein Master Brick
und zwei RS485 Extensions zusätzlich zu den bisher verwendeten Teilen
benötigt. Auf jeden Master Brick wird jeweils eine RS485 Extension gesteckt
und die beiden Extensions passend miteinander verkabelt. Jetzt noch das
Rotary Poti Bricklet an den neu zusammengesteckten Stapel anschließen.

Als nächster Schritt muss jetzt jeder Stapel einzeln über USB am PC angeschlossen
und konfiguriert werden. Die Details dazu sind in der :ref:`RS485 Dokumentation
<rs485_configuration>` beschrieben. Wichtig ist dann noch, dass nach der
Konfiguration der RS485 Slave vor dem RS485 Master gestartet wird.

Jetzt sollten im Brick Viewer die zwei Master Bricks, das Rotary Poti Bricklet
und der DC Brick auftauchen. Wenn das der Falls ist kann jetzt das vorherige
Programm ohne Änderung weiterverwendet werden.
