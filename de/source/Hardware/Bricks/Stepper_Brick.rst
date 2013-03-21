
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricks">Bricks</a> / Stepper Brick

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
	             "Stepper Brick mit Schrittmotor")
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

Erster Test
-----------

|test_intro|

Schließe einen Schrittmotor und eine passende Stromversorgung an den Brick an.
Der Aufbau sollte dem im folgenden Bild ähnlich sehen.

.. image:: /Images/Bricks/brick_stepper_motor_setup_600.jpg
   :scale: 100 %
   :alt: Stepper Brick mit Schrittmotor
   :align: center
   :target: ../../_images/Bricks/brick_stepper_motor_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/stepper_brickv.jpg
   :scale: 100 %
   :alt: Stepper Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/stepper_brickv.jpg

..
  FIXME: update image, to remove decay slider also put the warning about
         sync rect from the api docs here

Auf der linken Seite des Tabs kann die Treiberstufe ein- und ausgeschaltet,
sowie die maximale Geschwindigkeit, Beschleunigung und Verzögerung eingestellt werden.
Darunter sind drei Knöpfe um die Drehrichtung des Schrittmotors zu kontrollieren
sowie diesen zu stoppen. Wenn der "Forward" Kopf geklickt wird, dann wird die
Geschwindigkeit des Schrittmotors bis zur "Max Velocity" mit der eingestellten
Beschleunigung erhöht. Ein Klick auf den "Stop" Knopf verringert die
Geschwindigkeit auf "0" mit der eingestellten Verzögerung.

Weiter unten kann die Schrittmodus (Voll-, Halb-, Viertel- und Achtelschritt)
eingestellt sowie eine Vollbremsung ausgelöst werden, die den Motor sofort
anhält.

Alternative kann der Schrittmotor auch zu einer bestimmten Position (gemessen
in Schritten) gefahren werden. Dazu einfach bei "Drive To" die Position eingeben
und "Go" klicken. Der Schrittmotor kann ebenfalls eine bestimmte Anzahl Schritte
gefahren werden. Bei diesen beiden Fahrweisen werden auch die Einstellungen für
die maximale Geschwindigkeit, Beschleunigung und Verzögerung berücksichtigt.

Auf der rechten Seite werden die aktuelle Position, die noch zu fahrenden
Schritte sowie die Versorgungsspannung des Stapels und die externe
Versorgungsspannung angezeigt. Darunter befindet sich eine Tachometer zur
Darstellung der Motorgeschwindigkeit. Ganz unten kann die Mindestspannung des
Motors eingestellt werden. Wird diese unterschritten wird der Undervoltage
Callback ausgelöst. Zusätzlich kann auch noch der Motorstrom entsprechend des
angeschlossenen Motors eingestellt werden.

|test_pi_ref|


Stromversorgung
---------------

Der angeschlossene Motor kann über den schwarzen Stromversorgungsstecker auf
der Platine extern versorgt werden. Alternativ kann eine :ref:`Stromversorgung
<product_overview_power_supplies>` unter den Brick gesteckt werden.
Der Brick schaltet von selbst auf extern Versorgungen um, wenn am schwarzen
Stecker eine Spannung anliegt.


.. _stepper_brick_decay_mode:

Decay Modi
-----------

Für eine gute Erläuterung der verschiedenen Decay Modi siehe
`diesen <http://ebldc.com/?p=86/>`__ Blogeintrag (Englisch) von Avayan oder
`diesen <http://www.schrittmotor-blog.de/?p=51>`__ Blogeintrag (Deutsch) von
T. Ostermann.

Der richtige Decay Modus ist unglücklicherweise für jeden Schrittmotor anders.
Der beste Weg einen guten Decay Modus für deinen Schrittmotor zu ermitteln ist
die Stromaufnahme des Motors mit einem Oszilloskop zu messen. Der zweitbeste
Weg ist es auf die Geräusche des Motors zu hören. Wenn der Wert zu klein
ist dann ist häufig ein hoher Ton zu hören. Ist dagegen der Wert zu groß dann
ist häufig ein ein Brummgeräusch zu hören.

Im Allgemeinen ist der Fast Decay Modus (kleine Werte) geräuschvoller, erlaubt
aber höhere Motorgeschwindigkeiten.


Fehler LED
----------

Die rote LED leuchtet wenn die Versorgungsspannung unter das einstellbaren
Minimum fällt.


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

Schrittmotor macht komische Geräusche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schrittmotoren können hohe oder Brummtöne erzeugen, selbst im Stillstand,
wenn der Decay Modus nicht passen für den angeschlossenen Motor eingestellt ist.

Der Decay Modus kann, wie :ref:`hier <stepper_brick_decay_mode>`
beschrieben, möglicherweise besser für den verwendeten Schrittmotor eingestellt
werden.
