.. _servo_brick:

Servo Brick
===========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_servo_tilted_front_350.jpg",
	               "Bricks/brick_servo_tilted_front_600.jpg",
	               "Servo Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_tilted_back_100.jpg",
	             "Bricks/brick_servo_tilted_back_600.jpg",
	             "Servo Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_setup_100.jpg",
	             "Bricks/brick_servo_setup_600.jpg",
	             "Servo Brick mit Servo")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_setup_big_100.jpg",
	             "Bricks/brick_servo_setup_big_600.jpg",
	             "Servo Brick mit Servos")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_caption_100.jpg",
	             "Bricks/brick_servo_caption_600.jpg",
	             "Servo Brick mit Beschriftung")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_top_100.jpg",
	             "Bricks/brick_servo_top_600.jpg",
	             "Servo Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_bottom_100.jpg",
	             "Bricks/brick_servo_bottom_600.jpg",
	             "Servo Brick Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/servo_brick_dimensions_100.png",
	             "Dimensions/servo_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Steuert bis zu **7** RC Servos mit max. **3A**
* Steuert Brushless Motoren (benötigt externe ESC)
* Software einstellbare Servospannung, Periode und Pulsweite
* Position, Geschwindigkeit und Beschleunigung steuerbar
* Eine USB und zwei Bricklet Schnittstellen


Beschreibung
------------

Der Servo :ref:`Brick <product_overview_bricks>` ist mit einem 32-Bit
ARM Mikrocontroller ausgestattet und kann bis zu **7**
`RC Servos <http://de.wikipedia.org/wiki/Servo>`__
mit einem maximalen Strom bis zu **3A** steuern.
Die Ausgangsspannung ist einstellbar bis zu **9V**, der Stromverbrauch jedes
Servos kann einzeln gemessen werden.
Zusätzlich kann die PWM jedes Servos einzeln konfiguriert werden.

Über einen zusätzlichen Modellbau Fahrtenregler (Electronic Speed
Controller - ESC) ist es möglich Brushless Motoren zu steuern.
Es muss nur der richtige ESC abhängig vom Motor gewählt werden, so dass auch
Motoren mit einem Stromverbrauch von 150A und mehr steuerbar sind.

Der Brick ist kompatibel zu anderen Tinkerforge
:ref:`Bricks <product_overview_bricks>`
und kann in einem Stapel benutzt werden.
Über zwei Anschlüsse können :ref:`Bricklet <product_overview_bricklets>`
angeschlossen werden.

Die Versorgung der Servos erfolgt entweder über eine externe Stromversorgung
die direkt an den Brick angeschlossen wird oder über die interne
Stromversorgung des Stapels.
Der Brick schaltet automatisch auf externe Stromversorgung um, sobald eine
angeschlossen wird.

Über eine **USB** Verbindung kann der Brick von einem PC gesteuert werden.
Über einen zusätzlichen Master Brick mit Master Extension ist es möglich diese
USB Verbindung durch kabelgebundene Schnittstellen (**RS485**, **Ethernet**)
oder drahtlose Schnittstellen (**WLAN**) zu ersetzen
(:ref:`High Level Konzept <pi_hlpi>`).

Da die Firmware Open Source ist, ist es natürlich auch möglich den Brick direkt
zu programmieren (:ref:`On Device Programmierung <pi_odpi>`).
Momentan bieten wir keine On Device API an.


Technische Spezifikation
------------------------

===================================== ============================================================
Eigenschaft                           Wert
===================================== ============================================================
Mikrocontroller                       ATSAM3S2B (128kB Flash, 32kB RAM)
Stromverbrauch                        60mA
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Maximaler Motorstrom (Summe)          3A
Minimale/Maximale Eingangsspannung    5V/25V
Ausgangsspannung                      Über Software einstellbar 2V - 9V
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Ausgangsperiode\*                     1µs - 65535µs
Pulsweite\*                           1µs - 65535µs
Geschwindigkeit\*                     0 - 65535 °/100s
Beschleunigung\*                      1 - 65535 °/100s²
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Bricklet Anschlüsse                   2
Abmessungen (B x T x H)               40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                               18g
===================================== ============================================================

\* einstellbar pro Servo


Ressourcen
----------

* MCP3008 Datenblatt (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/datasheets/MCP3008.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/hardware/servo-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/servo_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/servo-brick/zipball/master>`__)


.. _servo_brick_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
Servo Bricks.

.. image:: /Images/Bricks/brick_servo_caption_600.jpg
   :scale: 100 %
   :alt: Servo Brick mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_servo_caption_800.jpg


.. _servo_brick_test:

Teste deinen Servo Brick
------------------------

To test the Servo Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect a RC servo to a port of the Brick and a suitable power supply.
Your setup should look as shown below.

.. image:: /Images/Bricks/brick_servo_setup_600.jpg
   :scale: 100 %
   :alt: Servo Brick mit Servo
   :align: center
   :target: ../../_images/Bricks/brick_servo_setup_1200.jpg

Now connect the Brick to the PC over USB, you should see a tab named
"Servo Brick" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricks/servo_brickv.jpg
   :scale: 100 %
   :alt: Servo Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/servo_brickv.jpg

In the left part of the GUI you can select the servo
to control. You can enable it, configure the
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ and configure
the corresponding position. Additionally you can see the current consumption of
the servo. Below there are four sliders to control
the position, velocity and acceleration of the servo. The fourth slider
can be used to change the period of the PWM
(see :ref:`Configure Servo PWM <servo_brick_configure_servo_pwm>` for more
information).

On the right side you can see the external and stack voltage.
Below are graphical representations for the state of each servo.
Beneath you can configure the minimum input voltage, which allows for
undervoltage signals if the voltage is too low.
Also you can configure the output voltage
(Caution: A too high output voltage may damage your servo!).
At the bottom right there is a "Start Test" button, which starts
a test sequence that performs random movements for each servo.

To start testing enable servo 0 and play around with the controls
or let the Brick Viewer perform a test.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <servo_brick_programming_interfaces>` section for
the API of the Servo Brick and examples in different programming languages.


.. _servo_brick_configure_servo_pwm:

Configure Servo PWM
-------------------

Typically you control a RC servo by a PWM signal with a
period of 20ms and an on-time of 1ms - 2ms depending on the position you want
to achieve. However, some servos do not work properly with these standard
settings. Therefore we provide a fully configurable PWM.

The default value for the period is 19.5ms. This period worked on all servos
we could get our fingers on (20ms did not work with some of the cheaper
chinese servos). If the datasheet of your servo does specify a preferred
period, use it. But it is likely that you don't have to change this value.

More interesting is the minimum and maximum pulse width. The default pulse
width is 1ms - 2ms. Most servos can however rotate further when
minimum/maximum pulse width is decreased/increased. If your servo comes
with a datasheet we recommend to use the values described in there. If you
don't have a datasheet you can try to incrementally extend the pulse width
until the servo starts to rattle. Use the biggest pulse width that does not
produce rattling.

.. warning::

   A wrong PWM configuration for an extended period of time can damage
   your servo.


Servo Power Supply
------------------

The Servo Brick is equipped with an internal power supply.
It offers the possibility to adjust the output voltages for the connected
servos.
The internal power supply can be powered through the on-board power-connector
(black connector) or through a
:ref:`Power Supply <product_overview_powersupplies>` in a stack.
The Servo Brick switches autonomously to the on-board power-connector when
there is a voltage measured. Since we use a step-down switcher for the
internal power supply please consider that the input voltage of the Brick has
to be 1V higher than the configured output voltage to assure stable operation.

.. warning::

   A too high output voltage can damage your servo.


Usage of RC ESC to drive brushless motors
-----------------------------------------

With this Brick you can control up to 7 brushless motors by using external
RC Electronic Speed Controllers (ESC). Simply connect the brushless
motor to the ESC and the ESC to the Servo Brick. With this construction
the maximum brushless motor current only depends on your selected ESC.

.. warning::

   Many ESC's have a build-in BEC which can be used to power RC receivers.
   If you use a ESC with BEC you have to disable it! Otherwise your ESC or
   the Brick can be destroyed. To disable BEC you have to remove the red
   wire from the connector you plug in the Servo Brick
   (`external video tutorial <http://www.youtube.com/watch?v=clNvfjhMQ5w>`__).

   If you use the same power supply for your ESC and the Servo Brick, additionally
   you have to remove the black (GND) wire too. It seems that the most
   ESC's will draw their current not over the power supply cable of the ESC
   but over the GND pin of the Servo Brick. This can lead to a destroyed Servo
   Brick. At the first tests have an eye on the current measurement in
   Brick Viewer.


Error LED Sources
-----------------

The red LED is enabled so long as the input voltage is below the user
configurable minimum voltage.


.. _servo_brick_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Servo_Brick_hlpi.table


On Device Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
 In Kürze!

 Eine API und Dokumentation um direkt auf dem Mikrocontroller zu programmieren
 (vergleichbar mit Arduino) ist geplant.
 Bis es soweit ist kann unsere Firmware als Grundlage für eigene Modifikationen
 verwendet werden (C Kenntnisse vorausgesetzt).

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"


FAQ
---

My servos are shaking, help!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The reason for this is typically a voltage drop, caused by repeated high
current peaks produced by the connected servos. First you should check
the input voltage, it should be at least 1V higher then the configured
output voltage.

Typically this problem occurs when the power supply can't handle the
high current peaks. To test if your power supply is the problem, you can
try batteries. Batteries normally don't have problems with current peaks.

If you are using batteries and the problem is still occurring, check
the voltage of the batteries when the servos are in use. If your batteries
are too weak, the voltage is dropping (in this case use full batteries).

If your servos only start shaking when you reach the maximum/minimum angle,
you have configured a too high/low pulse width. In this case you have to
reduce the pulse width, otherwise your servos might get damaged over time.
