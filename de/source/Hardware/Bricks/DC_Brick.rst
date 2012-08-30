.. include:: DC_Brick.substitutions


.. _dc_brick:

DC Brick
========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_dc_tilted_front_350.jpg",
	               "Bricks/brick_dc_tilted_front_600.jpg",
	               "DC Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_tilted_back_100.jpg",
	             "Bricks/brick_dc_tilted_back_600.jpg",
	             "DC Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_motor_setup_100.jpg",
	             "Bricks/brick_dc_motor_setup_600.jpg",
	             "DC Brick mit Motor")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_caption_100.jpg",
	             "Bricks/brick_dc_caption_600.jpg",
	             "DC Brick mit Beschriftung")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_top_100.jpg",
	             "Bricks/brick_dc_top_600.jpg",
	             "DC Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_bottom_100.jpg",
	             "Bricks/brick_dc_bottom_600.jpg",
	             "DC Brick Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/dc_brick_dimensions_100.png",
	             "Dimensions/dc_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}

Features
--------

* Steuert einen DC Motor mit max. **28V** und **5A**
* Richtung, Geschwindigkeit und Beschleunigung können kontrolliert werden
* Übertemperatur- und Überstromevents
* Drive/Brake und Drive/Coast Modus konfigurierbar
* Ein USB und zwei Bricklet Anschlüsse


Beschreibung
------------

Der DC :ref:`Brick <product_overview_bricks>` ist mit einem 32-Bit ARM
Mikrocontroller ausgestattet und kann einen
`DC Motor <http://de.wikipedia.org/wiki/Gleichstrommaschine>`__
bidirektional mit max. **28V** und **5A** steuern. Der Stromverbrauch und
die Versorgungsspannung kann gemessen,
die Geschwindigkeit und Beschleunigung des Motors können gesteuert werden.
Im Falle einer Überhitzung oder Überspannung werden Callbacks ausgelöst.
Ein "Undervoltage" Callback kann genutzt werden um Batterien oder Akkus
vor Tiefenentladung zu schützen.
Zusätzlich kann der Fahrmodus zwischen Drive/Brake und Drive/Coast umgeschaltet
werden (siehe :ref:`Fahrmodus <dc_brick_drive_mode>`).

Der Brick ist kompatibel zu anderen Tinkerforge
:ref:`Bricks <product_overview_bricks>`
und kann in einem Stapel benutzt werden.
Über zwei Anschlüsse können :ref:`Bricklet <product_overview_bricklets>`
angeschlossen werden.

Der DC Motor kann über eine externe Stromversorgung oder durch einen
Stapel versorgt werden. Der Brick schaltet automatisch auf eine externe
Stromversorgung um, sobald eine angeschlossen wird.

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

===================================  ====================================================================
Eigenschaft                          Wert
===================================  ====================================================================
Mikrocontroller                      ATSAM3S2B (128kB Flash, 32kB RAM)
Stromverbrauch                       53mA
-----------------------------------  --------------------------------------------------------------------
-----------------------------------  --------------------------------------------------------------------
Maximaler Motorstrom                 | Kurzzeitig: 5A (Peak)
                                     | Dauerhaft: > 3A (Abhängig von der Kühlung)
Minimale/Maximale Eingangsspannung   6V/28V
-----------------------------------  --------------------------------------------------------------------
-----------------------------------  --------------------------------------------------------------------
PWM Frequenz                         Einstellbar, 1-20kHz, Standard 15kHz
Geschwindigkeit                      -32767 bis 32767, Rückwärts nach Vorwärts, 0=Stop
Beschleunigung                       0 bis 65535, Geschwindigkeit/s, Inkrement für Geschwindigkeit/s
-----------------------------------  --------------------------------------------------------------------
-----------------------------------  --------------------------------------------------------------------
Bricklet Anschlüsse                  2
Abmessungen (B x T x H)              40 x 40 x 17mm (1,57 x 1,57 x 0,67")
Gewicht                              18g
===================================  ====================================================================


Ressourcen
----------

* MC33926 Datenblatt (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/datasheets/MC33926.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/hardware/dc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dc_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dc-brick/zipball/master>`__)


.. _dc_brick_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
DC Bricks.

.. image:: /Images/Bricks/brick_dc_caption_600.jpg
   :scale: 100 %
   :alt: DC Brick mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_dc_caption_800.jpg


.. _dc_brick_test:

Teste deinen DC Brick
---------------------

|test_intro|

Connect a DC brushed Motor to the Brick and a suitable power supply.
Your setup should look as shown below.

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick mit Motor
   :align: center
   :target: ../../_images/Bricks/brick_dc_motor_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

In this tab you can test your driver if you enable it.
You have three sliders to control
the velocity (forward and backward), the acceleration and the
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency which
is used by the driver to control the connected motor. On the right you see
the voltages of the two power sources and the current consumption.
Below you find a graphical representation of the velocity of the motor.
At the bottom you can configure the minimum motor voltage, which allows for
undervoltage signals if the voltage is too low.

Below the sliders you can test the "Full Brake" and change the driving modes
(see :ref:`here <dc_brick_drive_mode>` for more information).
To start testing enable the driver and play around with the controls.

|test_pi_ref|


Motor Power Supply
------------------

The connected motor can be powered through the on-board power-connector
(black connector)
or through a :ref:`Power Supply <product_overview_powersupplies>` in a
stack.
The Brick switches autonomously to the on-board power-connector when there
is a voltage measured.


.. _dc_brick_drive_mode:

Fahrmodi
--------

There are two possible modes of motor controls:

* Drive/Brake

  In this mode the motor is always either driving or braking, there is no
  freewheeling possible. A more linear correlation between PWM and velocity
  is an advantage of this mode.
  Therefore it is possible to accelerate more precise.
  Typically motors can be driven with slower velocities in this mode.
  Disadvantageous is a higher current consumption and a resulting faster
  heat-up of the driver.

* Drive/Coast

  In this mode the motor is either driving or freewheeling.
  Advantageous is a lower current consumption and a resulting slower heat-up.
  The control of the velocity and acceleration is less precise, it can
  "lag behind".


Error LED Sources
-----------------

The red LED is enabled if the voltage is below the minimum voltage
(configurable) or the driver is in emergency shutdown state
caused by over temperature or over current. To get the Brick operational
again you have to increase the voltage or in the latter case you have to
let the driver cool down and enable it again.


.. _dc_brick_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: DC_Brick_hlpi.table


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

..
	FAQ
	---

	Motor is not running correctly
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	**Reasons:**
	 * Voltage drop, caused by the connected motor.
	 * Low input voltage for the DC Brick.
	 * Not correctly connected.
	 * Defective motor.

	**Solutions:**
	 * Check input voltage. If too low, increase voltage.
	 * More powerful power supply. Typically batteries are better suited than wall power adapters.
	 * In case of you are using batteries to power the device, check the voltage of
	   the batteries and keep in mind that this voltage can break-in while delivering
	   high currents.
	 * Reduce the load of the motor.
	 * Check connection between Brick and motor.
	 * Change Motor when defect.
