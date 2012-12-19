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

Erster Test
-----------

|test_intro|

Schließe einen DC Motor und eine passende Stromversorgung an den Brick an.
Der Aufbau sollte dem im folgenden Bild ähnlich sehen.

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

Als erstes muss das Häkchen für "Enable" gesetzt werden um die Treiberstufe
zu aktivieren. Es stehen 3 Regler zur Kontrolle der Geschwindigkeit
(vorwärts und rückwärts), der Beschleunigung und der
`PWM <http://de.wikipedia.org/wiki/Pulsweitenmodulation>`__ Frequenz zur
Verfügung. Letztere wird von der Treiberstufe benutzt um den angeschlossenen
Motor anzusteuern.

Auf der rechten Seite befinden sich Anzeigen für die Spannungen der zwei
möglichen Stromversorgung sowie den Stromverbrauch des Motors.
Darunter befindet sich eine Tachometer zur Darstellung der
Motorgeschwindigkeit. Ganz unten kann die Mindestspannung des Motors eingestellt
werden. Wird diese unterschritten wird der Undervoltage Callback ausgelöst.

Unterhalb der Regler befinden sich Knöpfe für "Full Break" und die verschiedenen
Fahrmodi (siehe :ref:`here <dc_brick_drive_mode>` für weiterführende Information).

|test_pi_ref|


Stromversorgung
---------------

Der angeschlossene Motor kann über den schwarzen Stromversorgungsstecker auf
der Platine extern versorgt werden. Alternativ kann eine :ref:`Stromversorgung
<product_overview_power_supplies>` unter den Brick gesteckt werden.
Der Brick schaltet von selbst auf extern Versorgungen um, wenn am schwarzen
Stecker eine Spannung anliegt.


.. warning::
  Der Brick schaltet automatisch auf Stackversorgung um wenn am externen
  Stecker weniger wie 1V anliegen. Wenn z.B. ein Stack genutzt wird
  und eine zuvor angeschlossene externe Batterie vom Brick abgezogen wird,
  nutzt der Brick den Stack Stromversorgung. Wenn der Motor danach aktiviert 
  wird kann es sein, dass dieser mit der höheren Stackstromversorgung
  betrieben wird.
  

.. _dc_brick_drive_mode:

Fahrmodi
--------

Es gibt zwei Arten den Motor anzusteuern:

* Fahren/Bremsen

  In diesem Modus wird der Motor durchgehend angesteuert, entweder wird er
  gefahren oder gebremst. Es ist kein Freilauf möglich. Dies führt zu einer
  besseren Korrelation zwischen PWM und Geschwindigkeit, als Vorteil diese
  Modus. Dadurch kann eine genauere Beschleunigung erzielt werden. Gewöhnliche
  Motoren können in diesem Modus mit geringeren Geschwindigkeit gefahren
  werden. Ein Nachteil diese Modus ist der höhere Stromverbrauch wodurch sich
  die Treiberstufe schneller aufheizt.

* Fahren/Leerlauf

  In diesem Modus wird der Motor nicht durchgehend angesteuert, entweder wird er
  gefahren oder ist im Leerlauf. Dies verringert den Stromverbrauch und die
  Treiberstufe heizt sich nicht so schnell auf.
  Die Kontrolle über Geschwindigkeit und Beschleunigung ist weniger genau und
  kann "hinterher hinken".


Fehler LED
----------

Die rote LED leuchtet wenn die Versorgungsspannung unter das einstellbaren
Minimum fällt oder die Treiberstufe eine Notfallabschaltung ausgelöst hat.

Eine Notfallabschaltung wird ausgelöst wenn entweder der Stromverbrauch (über 5A)
oder die Temperatur der Treiberstufe zu hoch ist (über 175°C). Beide
Möglichkeiten sind letztendlich gleichbedeutend, da die Temperatur
ihren Schwellwert überschreitet sobald der Motor zu viel Strom verbraucht.

Um die Funktion des Bricks wiederherzustellen muss die Versorgungsspannung erhöht
werden, oder im Falle einer Notfallabschaltung muss die Treiberstufe abkühlen.


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
