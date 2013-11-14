
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / LED Strip Bricklet
:FIXME_shoplink: ../../../shop/bricklets/led-strip-bricklet.html

.. include:: LED_Strip.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _led_strip_bricklet:

LED Strip Bricklet
==================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

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
	    tfdocimg("Bricklets/bricklet_led_strip_master_100.jpg",
	             "Bricklets/bricklet_led_strip_master_600.jpg",
	             "LED Strip Bricklet mit Master Brick")
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

Das LED Strip Bricklet kann genutzt werden um LED Strips zu steuern
die mit einem WS2801 LED-Treiber ausgestattet sind. Es ist möglich
320 RGB LEDs (960 verschiedene LEDs) unabhängig voneinander zu steuern.

Mit Hilfe der API können alle LEDs gleichzeitig mit einer festen
Aktualisierungsrate von bis zu 100Hz gesteuert werden.

TODO: Video

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Unterstützer LED-Treiber          WS2801
Auflösung                         8 Bit pro LED
Anzahl kontrollierbarer LEDs      Maximal 960 (320 RGB LEDs)*
Aktualisierungsrate               Maximal 100 Aktualisierungen pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 12mm (1,18 x 1,18 x 0,47")
Gewicht                           10g
================================  ============================================================

\* Mit einem Master Brick, 480 mit anderen Bricks

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/led-strip-bricklet/raw/master/hardware/led-strip-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/led_strip_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/led-strip-bricklet/zipball/master>`__)

.. _led_strip_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_led_strip_master_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert, kann nun ein LED Strip gesteuert werden.

.. image:: /Images/Bricklets/bricklet_led_strip_brickv.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_brickv.jpg

|test_pi_ref|


.. _led_strip_bricklet_ws2801:

WS2801
------

Momentan werden LED Strips und Pixels unterstützt die mit WS2801 Controllern
ausgestattet sind (weitere Controller-Typen werden folgen).

Das WS2801 IC kann bis zu drei LEDs unabhängig voneinander steuern.
Typischerweise werden RGB LEDs, die in einem Gehäuse zusammen untergebracht 
sind, gesteuert. Der WS2801 wird über einen 3-Leiter Datenbus, bestehend aus 
einer Datenleitung, Taktleitung und Masse als Referenz, gesteuert. Jeder
IC verfügt dazu über einen Bus-Eingang und einen Bus-Ausgang, so dass die ICs
in Serie hintereinander geschaltet werden 
(`Daisy Chain <http://de.wikipedia.org/wiki/Daisy_chain>`__).
Jeder Bus-Eingang der WS2801 ICs ist entweder mit einem steuernden Gerät (wie 
z.B. das LED Strip Bricklet) oder mit einem Bus-Ausgang von einem WS2801 
Vorgänger verbunden. Da die WS2801 in Serie geschaltet werden müssen, darf jeder
Bus-Ausgang höchstens mit einem Bus-Eingang verbunden werden. Der Bus wird
beginnend beim ersten WS2801 indiziert.

.. image:: /Images/Bricklets/bricklet_led_strip_strip_example_600.jpg
   :scale: 100 %
   :alt: LED Strip with WS2801
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_strip_example_800.jpg

Das obige Foto zeigt einen typischen WS2801 LED Strip. Jedes Modul des Strips
ist mit einem WS2801 IC und einer davon angesteuerten RGB LED ausgestattet.
Die Signale sind jeweils auf der
Eingangsseite ("IN") und auf der Ausgangsseite ("OUT") gekennzeichnet:
5V, CK (Clock), SD (Serial Data) und GND.


.. _led_strip_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das nachfolgende Bild stellt die Schnittstellen des LED Strip Bricklets dar.

.. FIXME image:: /Images/Bricklets/bricklet_led_strip_connection_600.jpg
   :scale: 100 %
   :alt: LED Strip Bricklet Interface Description
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_connection_800.jpg

Wie in dem :ref:`WS2801 Abschnitt <led_strip_bricklet_ws2801>` beschrieben
unterstütz das Bricklet Strips und Pixels ausgestattet mit dem WS2801
controller. Die mit "Output" beschrifteten Klemmen müssen mit dem Eingang
des ersten WS2801 Controllers verbunden werden.

Die Klemme ist mit folgenden Signalen belegt:

* "DAT" ist die Datenleitung zum WS2801 Chip. Sie muss mit dem Dateneingang des
  ersten WS2801 verbunden werden. Leider gibt es keine allgemeingültige 
  Beschriftung für Strips und Pixels. Manchmal ist das Signal mit SD 
  (Serial Data) oder DI (Data Input) beschriftet. Es ist ebenfalls möglich das 
  nur der Ausgang beschriftet ist (z.B. DO, Data Output). Bei der anderen Seite
  muss es sich also folglich um den Eingang handeln.

* "CLK" ist die Taktleitung zum WS2801 Chip. Sie muss mit dem Takteingang des 
  ersten WS2801 verbunden werden. Dieser Eingang ist typischerweise mit
  CLK, CK oder CI (Clock Input) beschriftet. Falls nur der Ausgang beschriftet
  ist findet man Beschriftungen wie CO (Clock Output).

* "-" ist die Masseleitung. Masse ist notwendig um eine Referenz zu den
  DAT und CLK Signalen zu besitzen.

* "+" ist die Versorgungsspannungs-Ausgang. Es ist mit dem "+" Signal der "Input"
  Klemme verbunden und sollte nicht benutzt werden um LED Strips oder Pixel zu
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
zu speichern. Normalerweise könnte das LED Strip Bricklet nur bis zu 80 RGB LEDs
steuern auf Grund des begrenzten RAMs pro Bricklet.

Um diese Beschränkung zu umgehen kann das LED Strip Bricklet den ungenutzten RAM
von nicht genutzten Bricklet Ports nutzen. Dies erlaubt es bis zu 
320 RGB LEDs mit einem Master Brick und einem LED Strip Bricklet zu steuern.

Die maximale Anzahl von LEDs ergibt sich wie folgt:

================================  ============================================================
Freie Bricklet Ports              Maximale Anzahl von RGB LEDs
================================  ============================================================
0                                 80
1                                 160
2                                 240
3                                 320
================================  ============================================================


.. _led_strip_bricklet_led_strips:

LED Strips
----------

TODO:

* How to use them?
* Where to inject power?


.. _led_strip_bricklet_led_pixels:

LED Pixels
----------

TODO:

* How to use them?
* Where to inject power?


.. _led_strip_bricklet_fixed_frame_rate:

Feste Aktualisierungsrate
-------------------------

Um eine flüssige Animation zu erreichen wird eine feste Aktualisierungsrate
benötigt. Eine feste Aktualisierungsrate kann einfach mit einer
korrekt konfigurierten Framelänge und dem FrameRendered Callback erreicht
werden. Die Framelänge stellt die Zeit in ms dar, die zwischen zwei
Frames verstreicht. Der FrameRendered Callback wird ausgelöst nachdem
ein neues Frame auf die LEDs übertragen wurde.

Wenn als Beispiel eine Aktualisierungsrate von 20 Frames pro Sekunde
erreicht werden soll, sollte die Framelänge auf 50ms gesetzt werden.
Nachdem die Framelänge gesetzt ist, muss das erste Frame übertragen werden
(d.h. es müssen alle RGB Werte gesetzt werden). Danach muss auf den
FrameRendered Callback gewartet werden woraufhin das nächste Frame
übertragen werden muss usw.

.. image:: /Images/Bricklets/bricklet_led_strip_fixed_frame_rate.png
   :scale: 100 %
   :alt: LEDs mit fester Aktualisierungsrate steuern
   :align: center
   :target: ../../_images/Bricklets/bricklet_led_strip_fixed_frame_rate.png

Wenn ein FrameRendered Callback empfangen wird bevor alle LEDs eines Frames
gesetzt wurden, ist die Aktualisierungsrate zu hoch.


.. _led_strip_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das LED Strip Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-led-strip-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_led_strip_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für LED Strip Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_led_strip_case_built_up_1000.jpg

.. include:: LED_Strip.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/led_strip_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für LED Strip Bricklet
   :align: center
   :target: ../../_images/Exploded/led_strip_exploded.png

|bricklet_case_hint|


.. _led_strip_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: LED_Strip_hlpi.table
