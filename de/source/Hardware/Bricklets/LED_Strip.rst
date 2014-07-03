
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / LED Strip Bricklet
:shoplink: ../../../shop/bricklets/led-strip-bricklet.html


.. role:: led-strip-red

.. role:: led-strip-green

.. role:: led-strip-blue

.. role:: led-strip-black

.. role:: led-pixel-red

.. role:: led-pixel-green

.. role:: led-pixel-blue

.. role:: led-pixel-white


.. include:: LED_Strip.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _led_strip_bricklet:

LED Strip Bricklet
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_led_strip_tilted_350.jpg",
	               "Bricklets/bricklet_led_strip_tilted_600.jpg",
	               "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_vertical_100.jpg",
	             "Bricklets/bricklet_led_strip_vertical_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_horizontal_100.jpg",
	             "Bricklets/bricklet_led_strip_horizontal_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_tilted_back_100.jpg",
	             "Bricklets/bricklet_led_strip_tilted_back_600.jpg",
	             "LED Strip Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_led_strip_case_tilted_100.jpg",
	             "Cases/bricklet_led_strip_case_tilted_600.jpg",
	             "LED Strip Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_50_pixel_100.jpg",
	             "Bricklets/bricklet_led_strip_50_pixel_600.jpg",
	             "LED Strip Bricklet mit 50 RGB LED Pixel")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_w_reel_100.jpg",
	             "Bricklets/bricklet_led_strip_w_reel_600.jpg",
	             "LED Strip Bricklet mit RGB LED Streifen")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_led_strip_brickv_100.jpg",
	             "Bricklets/bricklet_led_strip_brickv.jpg",
	             "LED Strip Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/led_strip_bricklet_dimensions_100.png",
	             "Dimensions/led_strip_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Steuert bis zu 320 RGB LEDs
* Alle LEDs können unabhängig voneinander geschaltet werden
* Aktualisierungsrate von bis zu 100Hz für jede LED möglich

Beschreibung
------------

Das LED Strip :ref:`Bricklet <primer_bricklets>` kann genutzt werden um LED
Streifen und LED Pixel zu steuern, die mit einem WS2801, WS2811 oder WS2812
LED-Treiber ausgestattet sind. Es ist möglich 320 RGB LEDs (960 einzelne LEDs)
unabhängig voneinander über ein :ref:`Brick <primer_bricks>` zu steuern.

Mit Hilfe der API können alle LEDs gleichzeitig mit einer festen
Aktualisierungsrate von bis zu 100Hz gesteuert werden.  Ein Anwendungsbeispiel
findet man im :ref:`Starter Kit: Blinken Lights <starter_kit_blinkenlights>`:
`Video <http://www.youtube.com/watch?v=mmNRa-lLaXM>`__

Brick Daemon 2.0.10 oder neuer wird für diese Bricklet empfohlen.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Unterstützer LED-Treiber          WS2801, WS2811 und WS2812
Stromverbrauch                    1mA (inaktiv), 4mA (aktiv)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         8Bit pro LED
Maximale Anzahl LEDs              960 (320 RGB LEDs)*
Maximale Aktualisierungsrate      100 Aktualisierungen pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 12mm (1,18 x 1,18 x 0,47")
Gewicht                           10g
================================  ============================================================

\* mit einem Master Brick, 480 mit anderen Bricks

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/led-strip-bricklet/raw/master/hardware/led-strip-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/led_strip_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/led-strip-bricklet/zipball/master>`__)

.. _led_strip_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|. Anschließend kann ein LED Streifen oder LED Pixel an das
Bricklet, wie weiter unten beschrieben, angeschlossen werden.

|test_tab|
Wenn alles wie erwartet funktioniert, kann nun ein LED Steifen gesteuert werden.

.. image:: /Images/Bricklets/bricklet_led_strip_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_brickv.jpg

|test_pi_ref|


.. _led_strip_bricklet_ws28xy:

WS2801, WS2811 und WS2812
-------------------------

Es werden LED Streifen und Pixel unterstützt, die mit dem WS2801, WS2811 oder
WS2812 Treiber ausgestattet sind. Im Weiteren bezieht sich WS28xy auf alle
diese drei Treiber.

Der verwendete Treiber muss über Brick Viewer oder die ``set_chip_type()``
Funktion des LED Strip Bricklets eingestellt werden. Für WS2811 und WS2812
wird LED Bricklet Plugin Version 2.0.2 oder neuer benötigt.

Der WS28xy Treiber kann bis zu drei LEDs unabhängig voneinander steuern.
Typischerweise werden RGB LEDs, die in einem Gehäuse zusammen untergebracht 
sind, gesteuert. Der WS28xy Treiber wird über einen 3- oder 2-Leiter Datenbus,
bestehend aus einer Datenleitung, einer Taktleitung (nur WS2801) und Masse als
Referenz, gesteuert. Jeder Treiber verfügt dazu über einen Bus-Eingang und
einen Bus-Ausgang, so dass die Treiber in Serie hintereinander geschaltet
werden (`Daisy Chain <http://de.wikipedia.org/wiki/Daisy_chain>`__).
Jeder Bus-Eingang der WS28xy Treiber ist entweder mit einem steuernden Gerät (wie
z.B. das LED Strip Bricklet) oder mit einem Bus-Ausgang von einem vorherigen 
WS28xy Treiber verbunden. Da die WS28xy Treiber in Serie geschaltet werden müssen,
darf jeder Bus-Ausgang höchstens mit einem Bus-Eingang verbunden werden. Der
Bus wird beginnend beim ersten WS28xy Treiber indiziert (API Index 0).

.. image:: /Images/Bricklets/bricklet_led_strip_strip_example_600.jpg
   :scale: 100 %
   :alt: LED Strip with WS2801
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_example_800.jpg

Das obige Foto zeigt einen typischen WS2801 LED Steifen. Jedes Modul des Streifens
ist mit einem WS2801 Treiber und einer davon angesteuerten RGB LED ausgestattet.
Die Signale sind jeweils auf der Eingangsseite (IN) und auf der Ausgangsseite
(OUT) gekennzeichnet: 5V, CK (Clock), SD (Serial Data) und GND.
Im Gegensatz zum WS2801 haben die WS2811 und WS2812 Treiber kene Taktleitung.


.. _led_strip_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das nachfolgende Bild stellt die Schnittstellen des LED Strip Bricklets dar:

.. image:: /Images/Bricklets/bricklet_led_strip_connection_350.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Interface Description
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_connection_800.jpg

Wie im :ref:`WS28xy Abschnitt <led_strip_bricklet_ws28xy>` beschrieben,
unterstützt das Bricklet LED Steifen und Pixel, die mit WS2801, WS2811 oder
WS2812 Treiber-ICs ausgestattet sind.
Die mit "Output" beschrifteten Klemmen müssen mit dem Eingang
des ersten WS28xy Treiber-ICs verbunden werden.

Die Klemme ist mit folgenden Signalen belegt:

* "DAT" ist die Datenleitung zum WS28xy Chip. Sie muss mit dem Dateneingang des
  ersten WS28xy Chips verbunden werden. Leider gibt es keine allgemeingültige
  Beschriftung für LED Steifen und Pixel. Manchmal ist das Signal mit SD
  (Serial Data) oder DI (Data Input) beschriftet. Es ist ebenfalls möglich, dass
  nur der Ausgang beschriftet ist (z.B. DO, Data Output). Bei der anderen Seite
  muss es sich also folglich um den Eingang handeln.

* "CLK" ist die Taktleitung zum WS2801 Chip. Sie muss mit dem Takteingang des 
  ersten WS2801 Chips verbunden werden. Dieser Eingang ist typischerweise mit
  CLK, CK oder CI (Clock Input) beschriftet. Falls nur der Ausgang beschriftet
  ist findet man Beschriftungen wie CO (Clock Output).

  Die WS2811 und WS2812 Treiber-ICs haben keine Taktleitung, für diese muss die
  "CLK" Klemme offen gelassen werden.

* "-" ist die Masseleitung. Masse ist notwendig um eine Spannungsreferenz zu 
  den DAT und CLK Signalen zu besitzen.

* "+" ist der Versorgungsspannungs-Ausgang. Es ist mit dem "+" Signal der "Input"
  Klemme verbunden und sollte nicht benutzt werden um LED Steifen oder Pixel zu
  versorgen. Daher sollte dieses Signal nicht angeschlossen werden.

Die Eingangsklemme verfügt über zwei Signale:

* "+" ist der Spannungsversorgungs-Eingang. Dieser kann mit der Stromversorgung
  für die LEDs verbunden werden um die Versorgungsspannung zu messen. Wird dies
  nicht benötigt, so kann die Klemme offen bleiben.

* "-" ist die Masseleitung. Sie ist intern mit der Masse von der "Output" 
  Klemme verbunden.

.. _led_strip_bricklet_ram_constraints:

RAM Beschränkungen
------------------

Das LED Strip Bricklet benötigt viel RAM um die Farbinformationen für die LEDs
zu speichern. Normalerweise könnte das LED Strip Bricklet,
auf Grund des begrenzten RAMs pro Bricklet, nur bis zu 80 RGB LEDs steuern.

Um diese Beschränkung zu umgehen kann das LED Strip Bricklet den ungenutzten RAM
von nicht genutzten Bricklet Ports verwenden. Dies erlaubt es bis zu
320 RGB LEDs mit einem Master Brick und einem LED Strip Bricklet zu steuern.
Wie beschrieben können diese Bricklet Ports dann aber nicht von anderen Bricklets
verwendet werden.

Die maximale Anzahl von LEDs ergibt sich wie folgt:

================================  ==================================
Freie Bricklet Ports              Maximale Anzahl an RGB LEDs
================================  ==================================
0                                 80
1                                 160
2                                 240
3                                 320
================================  ==================================


.. _led_strip_bricklet_led_strips:

LED Steifen
-----------

Es existiert keine allgemeine farbliche Kennzeichnung für LED Streifen.
Insbesondere verstoßen die Farben oftmals gegen Konventionen. In diesem Beispiel
ist der schwarze Draht :led-strip-black:`5V`, grün die
:led-strip-green:`Taktleitung` (nur WS2801),
rot die :led-strip-red:`Datenleitung` und der
blaue Draht ist :led-strip-blue:`Masse`.

Als erstes werden die Takt- (nur WS2801) und Datenleitung des ersten
LED Streifens und Masse der Spannungsversorgung mit dem LED Strip Bricklet
verbunden. Dabei muss darauf geachtet werden, dass der Takt- und
Daten\ **eingang** des ersten Streifen mit dem Takt- und
Daten\ **ausgang** des LED Strip Bricklets verbunden wird.

Falls die Spannung der Versorgung gemessen werden soll, müssen die 5V der
Stromversorgung mit dem LED Strip Bricklet verbunden werden. Es können weitere
LED Streifen in Reihe (hintereinander) an den ersten LED Streifen angeschlossen 
werden (dabei müssen die
:ref:`RAM Beschränkungen <led_strip_bricklet_ram_constraints>` beachtet werden).

Es ist nicht ausreichend die LED Streifen nur an deren Anfang zu versorgen.
Wir empfehlen mindestens alle 2 Meter neu einzuspeisen. Dazu kann zum Beispiel
pro Einspeisepunkt ein eigenes Kabel zur Stromversorgung geführt werden. 
Somit wird der elektrische Widerstand reduziert und Leitungsverluste minimiert.
Das nachfolgende Bild zeigt ein Beispiel.

.. image:: /Images/Bricklets/bricklet_led_strip_strip_wiring_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Verkabelung für LED Streifen
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_wiring_1500.jpg

.. _led_strip_bricklet_led_pixels:

LED Pixel
---------

Die Verbindung zu LED Pixeln ist sehr ähnlich zur Verbindung zu LED Streifen.
Es existiert ebenfalls keine allgemeine farbliche Kennzeichnung. Im 
nachfolgenden Beispiel ist der rote Draht :led-pixel-red:`5V`,
blau ist :led-pixel-blue:`Masse`, die :led-pixel-green:`Taktleitung`
(nur WS2801) ist grün und die :led-pixel-white:`Datenleitung` ist weiß.

Die Takt- und Datenleitung vom ersten LED Pixel Bündel, sowie Masse von der 
Stromversorgung werden mit dem LED Strip Bricklet verbunden. Dabei muss darauf 
geachtet werden, dass der Takt- (nur WS2801) und Daten\ **eingang** des ersten
Pixels mit dem Takt- (nur WS2801) und Daten\ **ausgang** des LED Strip Bricklets
verbunden wird. Soll die
Versorgungsspannung gemessen werden, muss auch 5V von der Stromversorgung an das
Bricklet angeschlossen werden. Sollen mehrere Bündel verwendet werden, so können
diese in Reihe (hintereinander) an das erste Bündel angeschlossen werden
(dabei müssen die
:ref:`RAM Beschränkungen <led_strip_bricklet_ram_constraints>` beachtet werden).

Typischerweise besitzt jedes Pixel Bündel Drähte zur Stromversorgung am Anfang
und Ende des Bündels. Diese sollten über zusätzliche Kabel mit der 
Stromversorgung verbunden werden. Benachbarte Drähte können auch zusammengefasst
werden. Diese Maßnahme reduziert den elektrischen Widerstand und minimiert
die Leitungsverluste der Stromversorgung.

.. image:: /Images/Bricklets/bricklet_led_strip_pixel_wiring_800.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Verkabelung für Pixel
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_pixel_wiring_1500.jpg



.. _led_strip_bricklet_fixed_frame_rate:

Feste Aktualisierungsrate
-------------------------

Um eine flüssige Animation zu erreichen wird eine feste Aktualisierungsrate
benötigt. Eine feste Aktualisierungsrate kann einfach mit einer
korrekt konfigurierten Framelänge und dem ``FrameRendered`` Callback erreicht
werden. Die Framelänge stellt die Zeit in ms dar, die zwischen zwei
Frames verstreicht. Der ``FrameRendered`` Callback wird ausgelöst nachdem
ein neues Frame auf die LEDs übertragen wurde.

Wenn als Beispiel eine Aktualisierungsrate von 20 Frames pro Sekunde
erreicht werden soll, sollte die Framelänge auf 50ms gesetzt werden.
Nachdem die Framelänge gesetzt ist, muss das erste Frame übertragen werden
(d.h. es müssen alle RGB Werte gesetzt werden). Danach muss auf den
``FrameRendered`` Callback gewartet werden woraufhin das nächste Frame
übertragen werden muss usw.

.. image:: /Images/Bricklets/bricklet_led_strip_fixed_frame_rate_230.png
   :scale: 100 %
   :alt: LEDs mit fester Aktualisierungsrate steuern
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_fixed_frame_rate.png

Wenn ein ``FrameRendered`` Callback empfangen wird bevor alle LEDs eines Frames
gesetzt wurden, ist die Aktualisierungsrate zu hoch.


.. _led_strip_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das LED Strip Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-led-strip-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_led_strip_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für LED Strip Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_led_strip_case_tilted_1000.jpg

.. include:: LED_Strip.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/led_strip_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für LED Strip Bricklet
   :align: center
   :target: ../../_images/Exploded/led_strip_exploded.png

|bricklet_case_hint|


.. _led_strip_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: LED_Strip_hlpi.table
