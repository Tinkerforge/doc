.. include:: Joystick.substitutions


.. _joystick_bricklet:

Joystick Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_joystick_tilted_350.jpg",
	               "Bricklets/bricklet_joystick_tilted_600.jpg",
	               "Joystick Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_joystick_front_100.jpg",
	             "Bricklets/bricklet_joystick_front_600.jpg",
	             "Joystick Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_joystick_horizontal_100.jpg",
	             "Bricklets/bricklet_joystick_horizontal_600.jpg",
	             "Joystick Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_joystick_master_100.jpg",
	             "Bricklets/bricklet_joystick_master_600.jpg",
	             "Joystick Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_joystick_brickv_100.jpg",
	             "Bricklets/bricklet_joystick_brickv.jpg",
	             "Joystick Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/joystick_bricklet_dimensions_100.png",
	             "Dimensions/joystick_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 2-Achsen Joystick mit Taster


Beschreibung
------------

Das Joystick :ref:`Bricklet <product_overview_bricklets>` kann an jedes
:ref:`Bricks <product_overview_bricks>` angeschlossen werden.

Der Joystick is in zwei Richtungen beweglich und mit einem Taster ausgestattet.
Die Position des Joysticks (X/Y Koordinaten) und der Status des Tasters kann
ausgelesen werden. Zusätzlich können Events konfiguriert werden die ausgelöst
werden wenn der Stick eine bestimmte Position erreicht oder der Taster gedrückt
wird.

Der Joystick kann benutzt werden um z.B. Roboter oder Spiele zu steuern.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Joystick                          2-Achsen mit Taster
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
X/Y Position                      -100/100, 0=Mittelposition
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 45 x 23mm (0,98 x 1,77 x 0,9")*
Gewicht                           12g*
================================  ============================================================

\* ohne Knopf


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/joystick-bricklet/raw/master/hardware/joystick-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/joystick_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/joystick-bricklet/zipball/master>`__)


.. _joystick_bricklet_test:

Teste dein Joystick Bricklet
----------------------------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_joystick_master_600.jpg
   :scale: 100 %
   :alt: Joystick Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_master_1200.jpg

|test_tab|

.. image:: /Images/Bricklets/bricklet_joystick_brickv.jpg
   :scale: 100 %
   :alt: Joystick Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_brickv.jpg

The tab consists of a coordinate system that shows the current position of
the joystick and if the button is pressed.
Below this coordinate system you can find a graph that visualizes the
movements over time.
You should be able to  reproduce the depicted graph when you move the
joystick first up, then down, then right and then end left.

If the Brick Viewer does not show Position (0,0) when the joystick is
in resting position, press the "Calibrate (0,0)" button.

|test_pi_ref|


.. _joystick_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Joystick_hlpi.table
