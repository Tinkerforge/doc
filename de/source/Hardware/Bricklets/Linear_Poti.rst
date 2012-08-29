.. _linear_poti_bricklet:

Linear Poti Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_linear_poti_tilted_350.jpg",
	               "Bricklets/bricklet_linear_poti_tilted_600.jpg",
	               "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_front_100.jpg",
	             "Bricklets/bricklet_linear_poti_front_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_vertical_100.jpg",
	             "Bricklets/bricklet_linear_poti_vertical_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_horizontal_100.jpg",
	             "Bricklets/bricklet_linear_poti_horizontal_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_knob_100.jpg",
	             "Bricklets/bricklet_linear_poti_knob_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_master_100.jpg",
	             "Bricklets/bricklet_linear_poti_master_600.jpg",
	             "Linear Poti Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_brickv_100.jpg",
	             "Bricklets/bricklet_linear_poti_brickv.jpg",
	             "Linear Poti Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/linear_poti_bricklet_dimensions_100.png",
	             "Dimensions/linear_poti_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 59mm Linear-Potentiometer
* Ausgabe der Position von 0% bis 100% in 1% Schritten



Beschreibung
------------

Das Linear Poti :ref:`Bricklet <product_overview_bricklets>` ist mit einem
Linear-`Potentiometer <http://de.wikipedia.org/wiki/Potentiometer>`__
("Fader", "Slider") ausgestattet. :ref:`Brick <product_overview_bricks>`
können die Position des Sliders auslesen. Zusätzlich können Events konfiguriert
werden die bei einer definierten Position des Sliders ausgelöst werden.

Dieses Bricklet kann für Steuerungsaufgaben genutzt werden, wie z.B. das
Einstellen der Lautstärke eines Mediaplayers.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Linear-Potentiometer              59mm (2,32") einstellbare Länge
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          0% - 100% (Slider unten - Slider oben) in 1% Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 85 x 20mm (0,98 x 3,35 x 0,78")*
Gewicht                           14g*
================================  ============================================================

\* ohne Knopf


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/raw/master/hardware/linear-poti-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/linear_poti_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/zipball/master>`__)


.. _linear_poti_bricklet_test:

Teste dein Linear Poti Bricklet
-------------------------------

To test the Linear Poti Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Linear Poti Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_linear_poti_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Linear Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_linear_poti_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named
"Linear Poti Bricklet" in the Brick Viewer after you pressed "connect".
Select it.
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current12_brickv.jpg

Move the potentiometer.
You should be able to create a similar graph
by moving the potentiometer from bottom to top and back to bottom.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <linear_poti_programming_interfaces>`
section for the API of the Linear Poti Bricklet and examples in your
programming language.


.. _linear_poti_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Linear_Poti_hlpi.table
