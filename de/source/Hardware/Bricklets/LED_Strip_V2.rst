
:DISABLED_shoplink: ../../../shop/bricklets/led-strip-v2-bricklet.html


.. role:: led-strip-red

.. role:: led-strip-green

.. role:: led-strip-blue

.. role:: led-strip-black

.. role:: led-strip-white

.. role:: led-pixel-red

.. role:: led-pixel-green

.. role:: led-pixel-blue

.. role:: led-pixel-white


.. include:: LED_Strip_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _led_strip_v2_bricklet:

LED Strip Bricklet 2.0
======================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_led_strip_v2_tilted_[?|?].jpg           LED Strip Bricklet 2.0
	Bricklets/bricklet_led_strip_v2_tilted2_[?|?].jpg          LED Strip Bricklet 2.0
	Bricklets/bricklet_led_strip_v2_top_[?|?].jpg              LED Strip Bricklet 2.0
	Bricklets/bricklet_led_strip_v2_brickv_[100|].jpg          LED Strip Bricklet 2.0 im Brick Viewer
	Dimensions/led_strip_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Steuert bis zu 2048 RGB oder 1536 RGBW LEDs
* Alle LEDs können unabhängig voneinander geschaltet werden
* Aktualisierungsrate von bis zu 100Hz für jede LED möglich


.. _led_strip_v2_bricklet_description:

Beschreibung
------------

Das LED Strip :ref:`Bricklet <primer_bricklets>` 2.0 kann genutzt werden um LED
Streifen und LED Pixel zu steuern, die mit einem WS2801, WS2811,
WS2812/SK6812 (NeoPixel RGB), SK6812RGBW (NeoPixel RGBW), LPD8806 oder
APA102 (DotStar) LED-Treiber ausgestattet sind. Es ist möglich 2048 RGB oder
1536 RGBW LEDs (6144 einzelne LEDs) unabhängig voneinander über ein
:ref:`Brick <primer_bricks>` zu steuern.

Mit Hilfe der API können alle LEDs gleichzeitig mit einer festen
Aktualisierungsrate von bis zu 100Hz gesteuert werden.  Ein Anwendungsbeispiel
findet man im :ref:`Starter Kit: Blinken Lights <starter_kit_blinkenlights>`:
`Video <https://www.youtube.com/watch?v=mmNRa-lLaXM>`__

Das LED Strip Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Unterstütze LED-Treiber           | WS2801, WS2811, WS2812/SK6812 (NeoPixel RGB),
                                  | SK6812RGBW (NeoPixel RGBW), LPD8806 und APA102 (DotStar)
Stromverbrauch                    64mW (12,8mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         8Bit pro LED
Maximale Anzahl LEDs              6144 (2048 RGB oder 1536 RGBW LEDs)
Maximale Aktualisierungsrate      100 Aktualisierungen pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 12mm (1,18 x 1,18 x 0,47")
Gewicht                           8.1g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/led-strip-v2-bricklet/raw/master/hardware/led-strip-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/led_strip_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/led-strip-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rAcbZ9>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/led_strip_v2/led-strip-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/led_strip_v2/led-strip-v2.FCStd>`__)


.. _led_strip_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|. Anschließend kann ein LED Streifen oder LED Pixel an das
Bricklet, wie weiter unten beschrieben, angeschlossen werden.

|test_tab|
Wenn alles wie erwartet funktioniert, kann nun ein LED Steifen gesteuert werden.

.. image:: /Images/Bricklets/bricklet_led_strip_v2_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_v2_brickv.jpg

|test_pi_ref|


.. _led_strip_v2_bricklet_ws28xy:

Unterstützte LEDs
-----------------


Es werden LED Streifen und Pixel unterstützt, die mit dem WS2801, WS2811, WS2812 
SK6812 (NeoPixel RGB), SK6812RGBW (NeoPixel RGBW), LPD8806 oder APA102 (DotStar) 

Treiber ausgestattet sind. Im Weiteren bezieht sich *LED Treiber* auf alle
diese Treiber.

Der verwendete Treiber muss über Brick Viewer oder die ``set_chip_type()``
Funktion des LED Strip Bricklets 2.0 eingestellt werden.

Der LED Treiber kann bis zu vier LEDs unabhängig voneinander steuern.
Typischerweise werden RGB(W) LEDs, die in einem Gehäuse zusammen untergebracht 
sind, gesteuert. Der LED Treiber wird über einen 3- oder 2-Leiter Datenbus,
bestehend aus einer Datenleitung, einer Taktleitung und Masse als
Referenz, gesteuert. Jeder Treiber verfügt dazu über einen Bus-Eingang und
einen Bus-Ausgang, so dass die Treiber in Serie hintereinander geschaltet
werden (`Daisy Chain <https://de.wikipedia.org/wiki/Daisy_chain>`__).
Jeder Bus-Eingang der LED Treiber ist entweder mit einem steuernden Gerät (wie
z.B. das LED Strip Bricklet 2.0) oder mit einem Bus-Ausgang von einem vorherigen 
LED Treiber verbunden. Da die LED Treiber in Serie geschaltet werden müssen,
darf jeder Bus-Ausgang höchstens mit einem Bus-Eingang verbunden werden. Der
Bus wird beginnend beim ersten LED Treiber indiziert (API Index 0).

.. image:: /Images/Bricklets/bricklet_led_strip_strip_example_600.jpg
   :scale: 100 %
   :alt: LED Strip with WS2801
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_example_800.jpg

Das obige Foto zeigt einen typischen WS2801 LED Steifen. Jedes Modul des Streifens
ist mit einem WS2801 Treiber und einer davon angesteuerten RGB LED ausgestattet.
Die Signale sind jeweils auf der Eingangsseite (IN) und auf der Ausgangsseite
(OUT) gekennzeichnet: 5V, CK (Clock), SD (Serial Data) und GND.
Im Gegensatz zum WS2801 haben die WS2811 und WS2812 Treiber keine Taktleitung.


.. _led_strip_v2_bricklet_connectivity:

Anschlussmöglichkeit
--------------------


Das nachfolgende Bild stellt die Schnittstellen des LED Strip Bricklet 2.0 dar:

.. image:: /Images/Bricklets/bricklet_led_strip_v2_connectivity_350.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 Anschlussbeschreibung
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_v2_connectivity_800.jpg

Wie im :ref:`Unterstützte LEDs Abschnitt <led_strip_v2_bricklet_ws28xy>` beschrieben,
unterstützt das Bricklet LED Steifen und Pixel, die mit WS2801, WS2811,
WS2812, SK6812 (NeoPixel RGB), SK6812RGBW (NeoPixel RGBW), LPD8806 oder APA102 (DotStar)
Treiber-ICs ausgestattet sind. Die mit "Output" beschrifteten Klemmen müssen mit dem Eingang
des ersten LED Treiber-ICs verbunden werden.

Die Klemme ist mit folgenden Signalen belegt:

* "DAT" ist die Datenleitung zum LED Treiber Chip. Sie muss mit dem Dateneingang des
  ersten LED Treiber Chips verbunden werden. Leider gibt es keine allgemeingültige
  Beschriftung für LED Steifen und Pixel. Manchmal ist das Signal mit SD
  (Serial Data) oder DI (Data Input) beschriftet. Es ist ebenfalls möglich, dass
  nur der Ausgang beschriftet ist (z.B. DO, Data Output). Bei der anderen Seite
  muss es sich also folglich um den Eingang handeln.

* "CLK" ist die Taktleitung zum LED Treiber Chip. Sie muss mit dem Takteingang des 
  ersten LED Treiber Chips verbunden werden. Dieser Eingang ist typischerweise mit
  CLK, CK oder CI (Clock Input) beschriftet. Falls nur der Ausgang beschriftet
  ist findet man Beschriftungen wie CO (Clock Output).

  Die WS2811, WS2812 und SK6812 Treiber-ICs haben keine Taktleitung, für diese muss die
  "CLK" Klemme offen gelassen werden.

* "-" ist die Masseleitung. Masse ist notwendig um eine Spannungsreferenz zu 
  den DAT und CLK Signalen zu besitzen.

* "+" ist der Versorgungsspannungs-Ausgang. Es ist mit dem "+" Signal der "Input"
  Klemme verbunden und sollte nicht benutzt werden um LED Steifen oder Pixel zu
  versorgen. Die Streifen oder Pixel sollten direkt von der Stromquelle aus
  versorgt und dieses Signal nicht angeschlossen werden.

Die Eingangsklemme verfügt über zwei Signale:

* "+" ist der Spannungsversorgungs-Eingang. Dieser kann mit der Stromversorgung
  für die LEDs verbunden werden um die Versorgungsspannung zu messen. Wird dies
  nicht benötigt, so kann die Klemme offen bleiben.

* "-" ist die Masseleitung. Sie ist intern mit der Masse von der "Output" 
  Klemme verbunden.


.. _led_strip_v2_bricklet_ws2812b_led_strips:

LED Streifen mit Taktleitung (z.B. WS2812B)
-------------------------------------------

Es existiert keine allgemeine farbliche Kennzeichnung für LED Streifen.
Insbesondere verstoßen die Farben oftmals gegen Konventionen. In diesem WS2812B
LED Streifen Beispiel ist der rote Draht :led-strip-red:`5V`, grün die
:led-strip-green:`Datenleitungleitung` und der weiße Draht ist 
:led-strip-white:`Masse`.

Als erstes wird die Datenleitung des ersten
LED Streifens und Masse der Spannungsversorgung mit dem LED Strip Bricklet 2.0
verbunden. Dabei muss darauf geachtet werden, dass der 
Daten\ **eingang** des ersten Streifen mit 
Daten\ **ausgang** des LED Strip Bricklets 2.0 verbunden wird.

Falls die Spannung der Versorgung gemessen werden soll, müssen die 5V der
Stromversorgung mit dem LED Strip Bricklet 2.0 verbunden werden. Es können weitere
LED Streifen in Reihe (hintereinander) an den ersten LED Streifen angeschlossen 
werden.

Es ist nicht ausreichend die LED Streifen nur an deren Anfang zu versorgen.
Wir empfehlen mindestens alle 2 Meter neu einzuspeisen. Dazu kann zum Beispiel
pro Einspeisepunkt ein eigenes Kabel zur Stromversorgung geführt werden. 
Somit wird der elektrische Widerstand reduziert und Leitungsverluste minimiert.
Das nachfolgende Bild zeigt ein Beispiel.

.. image:: /Images/Bricklets/bricklet_led_strip_ws2812b_wiring_600.png
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 Verkabelung für WS2812B LED Streifen
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_ws2812b_wiring_1500.png


.. _led_strip_v2_bricklet_ws2801_led_strips:

LED Steifen ohne Taktleitung (z.B. WS2801)
------------------------------------------

Es existiert keine allgemeine farbliche Kennzeichnung für LED Streifen.
Insbesondere verstoßen die Farben oftmals gegen Konventionen. In diesem WS2801 
LED Streifen Beispiel ist der schwarze Draht :led-strip-black:`5V`, grün die
:led-strip-green:`Taktleitung`, rot die :led-strip-red:`Datenleitung` und der
blaue Draht ist :led-strip-blue:`Masse`.

Als erstes werden die Takt- und Datenleitung des ersten
LED Streifens und Masse der Spannungsversorgung mit dem LED Strip Bricklet 2.0
verbunden. Dabei muss darauf geachtet werden, dass der Takt- und
Daten\ **eingang** des ersten Streifen mit dem Takt- und
Daten\ **ausgang** des LED Strip Bricklet 2.0 verbunden wird.

Falls die Spannung der Versorgung gemessen werden soll, müssen die 5V der
Stromversorgung mit dem LED Strip Bricklet 2.0 verbunden werden. Es können weitere
LED Streifen in Reihe (hintereinander) an den ersten LED Streifen angeschlossen 
werden.

Es ist nicht ausreichend die LED Streifen nur an deren Anfang zu versorgen.
Wir empfehlen mindestens alle 2 Meter neu einzuspeisen. Dazu kann zum Beispiel
pro Einspeisepunkt ein eigenes Kabel zur Stromversorgung geführt werden. 
Somit wird der elektrische Widerstand reduziert und Leitungsverluste minimiert.
Das nachfolgende Bild zeigt ein Beispiel.

.. image:: /Images/Bricklets/bricklet_led_strip_strip_wiring_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 Verkabelung für WS2801 LED Streifen
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_wiring_1500.jpg

.. _led_strip_v2_bricklet_led_pixels:

LED Pixel
---------

Die Verbindung zu LED Pixeln ist sehr ähnlich zur Verbindung zu LED Streifen.
Es existiert ebenfalls keine allgemeine farbliche Kennzeichnung. Im 
nachfolgenden Beispiel ist der rote Draht :led-pixel-red:`5V`,
blau ist :led-pixel-blue:`Masse`, die :led-pixel-green:`Taktleitung`
(nur WS2801) ist grün und die :led-pixel-white:`Datenleitung` ist weiß.

Die Takt- und Datenleitung vom ersten LED Pixel Bündel, sowie Masse von der 
Stromversorgung werden mit dem LED Strip Bricklet 2.0 verbunden. Dabei muss darauf 
geachtet werden, dass der Takt- (nur WS2801) und Daten\ **eingang** des ersten
Pixels mit dem Takt- (nur WS2801) und Daten\ **ausgang** des LED Strip Bricklet 2.0
verbunden wird. Soll die
Versorgungsspannung gemessen werden, muss auch 5V von der Stromversorgung an das
Bricklet angeschlossen werden. Sollen mehrere Bündel verwendet werden, so können
diese in Reihe (hintereinander) an das erste Bündel angeschlossen werden.

Typischerweise besitzt jedes Pixel Bündel Drähte zur Stromversorgung am Anfang
und Ende des Bündels. Diese sollten über zusätzliche Kabel mit der 
Stromversorgung verbunden werden. Benachbarte Drähte können auch zusammengefasst
werden. Diese Maßnahme reduziert den elektrischen Widerstand und minimiert
die Leitungsverluste der Stromversorgung.

.. image:: /Images/Bricklets/bricklet_led_strip_pixel_wiring_800.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet 2.0 Verkabelung für Pixel
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_pixel_wiring_1500.jpg



.. _led_strip_v2_bricklet_fixed_frame_rate:

Feste Aktualisierungsrate
-------------------------

Um eine flüssige Animation zu erreichen wird eine feste Aktualisierungsrate
benötigt. Eine feste Aktualisierungsrate kann einfach mit einer
korrekt konfigurierten Framelänge und dem ``FrameStarted`` Callback erreicht
werden. Die Framelänge stellt die Zeit in ms dar, die zwischen zwei
Frames verstreicht. Der ``FrameStarted`` Callback wird ausgelöst sobald eine
Übertragung des Frames auf die LEDs started (Die Frames sind Double-Buffered).

Wenn als Beispiel eine Aktualisierungsrate von 20 Frames pro Sekunde
erreicht werden soll, sollte die Framelänge auf 50ms gesetzt werden.
Nachdem die Framelänge gesetzt ist, muss das erste Frame übertragen werden
(d.h. es müssen alle RGB Werte gesetzt werden). Danach muss auf den
``FrameStarted`` Callback gewartet werden woraufhin das nächste Frame
übertragen werden muss usw.

.. image:: /Images/Bricklets/bricklet_led_strip_v2_fixed_frame_rate.png
   :scale: 100 %
   :alt: LEDs mit fester Aktualisierungsrate steuern
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_v2_fixed_frame_rate.png

Wenn ein ``FrameStarted`` Callback empfangen wird bevor alle LEDs eines Frames
gesetzt wurden, ist die Aktualisierungsrate zu hoch.


.. _led_strip_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das LED Strip Bricklet 2.0
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


.. _led_strip_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: LED_Strip_V2_hlpi.table
