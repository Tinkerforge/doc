.. _rotary_poti_bricklet:

Rotary Poti Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_rotary_poti_tilted_350.jpg",
	               "Bricklets/bricklet_rotary_poti_tilted_600.jpg",
	               "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_front_100.jpg",
	             "Bricklets/bricklet_rotary_poti_front_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_vertical_100.jpg",
	             "Bricklets/bricklet_rotary_poti_vertical_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_horizontal_100.jpg",
	             "Bricklets/bricklet_rotary_poti_horizontal_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_knob_100.jpg",
	             "Bricklets/bricklet_rotary_poti_knob_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_master_100.jpg",
	             "Bricklets/bricklet_rotary_poti_master_600.jpg",
	             "Rotary Poti Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_brickv_100.jpg",
	             "Bricklets/bricklet_rotary_poti_brickv.jpg",
	             "Rotary Poti Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/rotary_poti_bricklet_dimensions_100.png",
	             "Dimensions/rotary_poti_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 300° Dreh-Potentiometer
* Ausgabe der Position von -150° bis 150° in 1° Schritten


Beschreibung
------------

Das Rotary Poti :ref:`Bricklet <product_overview_bricklets>` ist mit einem
Dreh-`Potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`__ ausgestattet,
dessen Position ausgelesen werden kann. Zusätzlich können Events konfiguriert
werden die ausgelöst werden wenn eine spezifizierte Position erreicht wird.

Dieses Bricklet kann für Steueraufgaben benutzt werden wie z.B. das Steuern
einer Lautstärke.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Dreh-Potentiometer                1 Umdrehung, 300°
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          -150° bis 150° (links nach rechts) in 1° Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 23mm (1,18 x 0,98 x 0,9")*
Gewicht                           5g*
================================  ============================================================

\* ohne Knopf


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/raw/master/hardware/rotary-poti-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rotary_poti_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/zipball/master>`__)


.. _rotary_poti_bricklet_test:

Teste dein Rotary Poti Bricklet
-------------------------------

Um das Rotary Poti Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect the Rotary Potentiometer Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_rotary_poti_master_600.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Rotary Poti Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg

Turn the potentiometer.
You should be able to create a similar graph by turning the potentiometer
from left left to right and back to left.

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <rotary_poti_programming_interfaces>` über das
API des Rotary Poti Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _rotary_poti_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Rotary_Poti_hlpi.table
