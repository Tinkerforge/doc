.. include:: Stepper_Brick.substitutions


.. _stepper_brick:

Stepper Brick
=============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_stepper_tilted_front_350.jpg",
	               "Bricks/brick_stepper_tilted_front_600.jpg",
	               "Stepper Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_tilted_back_100.jpg",
	             "Bricks/brick_stepper_tilted_back_600.jpg",
	             "Stepper Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_motor_setup_100.jpg",
	             "Bricks/brick_stepper_motor_setup_600.jpg",
	             "Stepper Brick mit Motor")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_caption_100.jpg",
	             "Bricks/brick_stepper_caption_600.jpg",
	             "Stepper Brick mit Beschriftung")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_top_100.jpg",
	             "Bricks/brick_stepper_top_600.jpg",
	             "Stepper Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_bottom_100.jpg",
	             "Bricks/brick_stepper_bottom_600.jpg",
	             "Stepper Brick Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/stepper_brick_dimensions_100.png",
	             "Dimensions/stepper_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Steuert einen bipolaren Schrittmotor mit max. **38V** und **2,5A** pro Phase
* Position, Geschwindigkeit und Beschleunigung sind steuerbar
* Voll-, Halb-, Viertel- und Achtelschritt
* Konfigurierbarer Decay Modus
* Eine USB und zwei Bricklet Schnittstellen


Beschreibung
------------

Der Stepper :ref:`Brick <product_overview_bricks>` ist mit einem 32-Bit ARM
Mikrocontroller ausgestattet und kann einen bipolaren `Schrittmotor
<http://de.wikipedia.org/wiki/Schrittmotor>`__
mit einem maximalen Strom von **2,5A** und einer maximalen Spannung von **38V**
pro Phase steuern.
Der maximale Treiberstrom und der :ref:`Decay Modus <stepper_brick_decay_mode>`
können per Software über die API eingestellt werden.
Schritte, Geschwindigkeit und Beschleunigung des angeschlossenen Schrittmotors
können gesteuert, der Stromverbrauch und die Versorgungsspannung gemessen werden.

Der Brick ist kompatibel zu anderen Tinkerforge
:ref:`Bricks <product_overview_bricks>`
und kann in einem Stapel benutzt werden.
Über zwei Anschlüsse können :ref:`Bricklet <product_overview_bricklets>`
angeschlossen werden.

Der Schrittmotor kann über eine externe Stromversorgung oder durch den
Stapel versorgt werden.
Der Brick schaltet automatisch auf eine externe Stromversorgung um,
sobald eine angeschlossen wird.

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

===================================  ============================================================
Eigenschaft                          Wert
===================================  ============================================================
Mikrocontroller                      ATSAM3S2B (128kB Flash, 32kB RAM)
Stromverbrauch                       60mA
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Maximaler Motorstrom pro Phase       2,5A
Minimale/Maximale Eingangsspannung   8V/38V
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Schrittmodi                          Voll-, Halb-, Viertel- oder Achtelschritte
Decay Modi                           Slow Decay, Fast Decay oder konfigurierbares Mixed Decay
Maximale Geschwindigkeit             0 bis 65535, konfigurierbar als Grenze, in Schritten/s
Maximale Beschleunigung              0 bis 65535, konfigurierbar als Grenze, in Schritten/s²
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse                  2
Abmessungen (B x T x H)              40 x 40 x 17mm (1,57 x 1,57 x 0,67")
Gewicht                              20g
===================================  ============================================================


Ressourcen
----------

* DRV8811 Datenblatt (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/datasheets/drv8811.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/hardware/stepper-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/stepper_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/stepper-brick/zipball/master>`__)


.. _stepper_brick_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
Stepper Bricks.

.. image:: /Images/Bricks/brick_stepper_caption_600.jpg
   :scale: 100 %
   :alt: Stepper Brick mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_stepper_caption_800.jpg


.. _stepper_brick_test:

Teste deinen Stepper Brick
--------------------------

|test_intro|

Connect a stepper motor to the Brick and a suitable power supply
(see :ref:`here <stepper_brick_connectivity>`). Your setup should look
like below.

.. image:: /Images/Bricks/brick_stepper_motor_setup_600.jpg
   :scale: 100 %
   :alt: Stepper Brick mit Motor
   :align: center
   :target: ../../_images/Bricks/brick_stepper_motor_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/stepper_brickv.jpg
   :scale: 100 %
   :alt: Stepper Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/stepper_brickv.jpg

In the left part of the GUI you can enable the driver and control
the velocity, acceleration, deceleration and the decay mode
(see :ref:`stepper_brick_decay_mode`) of the stepper. Below
there are three buttons that control the direction of
the stepper and stop it. For example if you press "Forward",
the stepper will increase its speed to "Max Velocity" with the given
acceleration. If you press "Stop" it will decrease its speed to "0" with
the given deceleration.

Below you can set the stepping mode (full, half, quarter, eighth) stepping mode
and trigger a "Full Brake", which stops the motor immediately.

You can drive to a specific position (measured in steps)
by entering it at "DrivingTo" an press "Go". Also you can drive a
specific number of steps. By using these controls the motor will accelerate
until reaching the maximum velocity and decelerate before reaching the
specified position.

On the right side the current position and remaining steps are shown
as well as the stack and external voltages.
Below is a graphical representation of the velocity of the stepper.
Beneath you can configure the minimum input voltage, which allows for
undervoltage signals if the voltage is too low. In the bottom right the
motor current can be configured according to the connected motor.

To start testing set a motor current suitable for your stepper motor, enable
the driver and play around with the controls.

|test_pi_ref|


Stromversorgung
---------------

Der angeschlossene Motor kann über den schwarzen Stromversorgungsstecker auf
der Platine extern versorgt werden. Alternativ kann eine :ref:`Stromversorgung
<product_overview_power_supplies>` unter den Brick gesteckt werden.
Der Brick schaltet von selbst auf extern Versorgungen um, wenn am schwarzen
Stecker eine Spannung anliegt.


.. _stepper_brick_decay_mode:

Decay Modes
-----------

A good explanation of decay modes can be found
`here <http://robot.avayanex.com/?p=86/>`__.

A good decay mode is unfortunately different for every motor. The best
way to work out a good decay mode for your stepper motor, if you can't
measure the current with an oscilloscope, is to listen at the sound of
the motor. If the value is too low, you often hear a high pitched
sound and if it is too high you can often hear a humming sound.

Generally, fast decay mode (small value) will be noisier but also
allow higher motor speeds.


Error LED Sources
-----------------

The red LED is enabled if the input voltage is below the user
configurable minimum voltage.


.. _stepper_brick_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Stepper_Brick_hlpi.table


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

Stepper makes funny noises
^^^^^^^^^^^^^^^^^^^^^^^^^^

Stepper motors can produce high pitch or humming noises, even if
they are standing still, if the decay mode is not configured correctly
for the connected motor.

Try to play around with the decay mode as described
:ref:`here <stepper_brick_decay_mode>`.
