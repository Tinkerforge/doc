
.. include:: Stepper_Brick.substitutions


.. _stepper_brick:

Stepper Brick
=============

.. raw:: html

	{% tfgallery %}

	Bricks/brick_stepper_tilted_front_[?|?].jpg        Stepper Brick
	Bricks/brick_stepper_tilted_back_[?|?].jpg         Stepper Brick
	Bricks/brick_stepper_motor_setup_[?|?].jpg         Stepper Brick mit Schrittmotor
	Bricks/brick_stepper_caption_[?|?].jpg             Stepper Brick mit Beschriftung
	Bricks/brick_stepper_top_[?|?].jpg                 Stepper Brick Oberseite
	Bricks/brick_stepper_bottom_[?|?].jpg              Stepper Brick Unterseite
	Dimensions/stepper_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Der Stepper Brick ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird der :ref:`Silent Stepper Brick <silent_stepper_brick>` empfohlen.
 Zusätzlich befinden sich zwei unterschiedliche Stepper Bricklets gerade in der Entwicklung.

Features
--------

* Steuert einen bipolaren Schrittmotor über USB (max. **38V**, **2,5A** pro Phase)
* API für viele Programmiersprachen verfügbar
* Position, Geschwindigkeit und Beschleunigung sind steuerbar
* Voll-, Halb-, Viertel- und Achtelschritt
* Konfigurierbarer Decay Modus
* Erweiterbar über zwei Bricklet Anschlüsse


.. _stepper_brick_description:

Beschreibung
------------

Mit dem Stepper :ref:`Brick <primer_bricks>` kann einen bipolaren
`Schrittmotor <https://de.wikipedia.org/wiki/Schrittmotor>`__
mit einem maximalen Strom von **2,5A** und einer maximalen Spannung von **38V**
pro Phase über **USB** gesteuert werden. Eine API für
:ref:`viele Programmiersprachen <stepper_brick_programming_interface>` ermöglicht 
das Steuern der Richtung, Geschwindigkeit und Beschleunigung des Motors.

Der maximale Treiberstrom und der :ref:`Decay Modus <stepper_brick_decay_mode>`
können ebenfalls per Software über die API eingestellt werden. Der Stromverbrauch 
und die Versorgungsspannung können über diese auch gemessen werden.

Über zwei Anschlüsse können :ref:`Bricklets <primer_bricklets>` 
angeschlossen werden, die die Fähigkeiten des Bricks erweitern. Der Stepper 
Brick kann mit anderen Bricks in einem :ref:`Stapel <primer_stack>` genutzt 
werden. Zum Beispiel kann ein zusätzlicher  :ref:`Master Brick <master_brick>` 
mit :ref:`Master Extensions <primer_master_extensions>` genutzt werden,
um die USB Verbindung durch andere kabelgebundene Schnittstellen 
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
oder drahtlose Schnittstellen (:ref:`WLAN <wifi_extension>`) zu ersetzen.

Der Schrittmotor kann über eine externe Stromversorgung (schwarze 
Stromversorgungsbuchse) oder durch den Stapel versorgt werden.
Der Brick schaltet automatisch auf die externe Stromversorgung um,
sobald diese angeschlossen wird.


Technische Spezifikation
------------------------

===================================  ============================================================
Eigenschaft                          Wert
===================================  ============================================================
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
Stromverbrauch                       60mA
===================================  ============================================================


Ressourcen
----------

* DRV8811 Datenblatt (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/datasheets/drv8811.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/hardware/stepper-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/stepper_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/stepper-brick/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2BCk72r>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/stepper/stepper.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/stepper/stepper.FCStd>`__)


.. _stepper_brick_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeiten des
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

Alternativ kann der Schrittmotor auch zu einer bestimmten Position (gemessen
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
<primer_power_supplies>` unter den Brick gesteckt werden.
Der Brick schaltet von selbst auf die externe Versorgung um, wenn am schwarzen
Stecker eine Spannung anliegt.


.. _stepper_brick_decay_mode:

Decay Modi
----------

Für eine gute Erläuterung der verschiedenen Decay Modi siehe
`diesen <https://ebldc.com/?p=86/>`__ Blogeintrag (Englisch) von Avayan oder
`diesen <http://www.schrittmotor-blog.de/stromregelung-von-schrittmotoren-auf-das-abschalten-kommt-es-an/>`__
Blogeintrag (Deutsch) von T. Ostermann.

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


.. _stepper_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Stepper_Brick_hlpi.table


FAQ
---

Schrittmotor macht komische Geräusche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schrittmotoren können hohe oder Brummtöne erzeugen, selbst im Stillstand,
wenn der Decay Modus nicht passen für den angeschlossenen Motor eingestellt ist.

Der Decay Modus kann, wie :ref:`hier <stepper_brick_decay_mode>`
beschrieben, möglicherweise besser für den verwendeten Schrittmotor eingestellt
werden.
