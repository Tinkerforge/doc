.. _step-down:

Step-Down Power Supply
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Power_Supplies/powersupply11_tilted_350.jpg",
	               "Power_Supplies/powersupply11_tilted_600.jpg",
	               "Step-Down Power Supply")
	}}
	{{
	    tfdocimg("Power_Supplies/powersupply11_caption_100.jpg",
	             "Power_Supplies/powersupply11_caption_600.jpg",
	             "Step-Down Power Supply mit Beschriftung")
	}}
	{{
	    tfdocimg("Power_Supplies/powersupply11_horizontal_100.jpg",
	             "Power_Supplies/powersupply11_horizontal_600.jpg",
	             "Step-Down Power Supply")
	}}
	{{
	    tfdocimg("Power_Supplies/powersupply11_connector_100.jpg",
	             "Power_Supplies/powersupply11_connector_600.jpg",
	             "Step-Down Power Supply mit Steckern")
	}}
	{{
	    tfdocimg("Dimensions/step_down_powersupply_dimensions_100.png",
	             "Dimensions/step_down_powersupply_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Versorgt einen Stapel von Bricks mit 5V
* Kann Motoren angeschlossen an Bricks, z.B.. DC Brick, versorgen
* Eingangsspannung 6V bis 27V
* Zusätzlich Ausgangsspannung 5V (seit Version 1.1)


Beschreibung
------------

Diese Stromversorgungsplatine kann unter einen Stapel gesteckt werden und
diesen versorgen. Sie ist mit einem effizienten Step-Down Regler ausgestattet.

Es kann eine externe Stromversorgung (6V bis 27V), wie z.B. eine Batterie,
angeschlossen werden und diese Platine erzeugt 5V für alle
:ref:`Bricks <product_overview_bricks>` und
:ref:`Bricklets <product_overview_bricklets>` des Stapels.
Zusätzlich verbindet diese Platine die externe Stromversorgung mit den
Powerleitungen des Stapels, so dass Treiber Bricks (DC, Servo, Stepper) diese
als Stromversorgung für ihre Motoren nutzen kann.

Der :ref:`Master Brick <master_brick>`, welcher als Master des Stacks
eingesetzt ist, kann den Stromverbrauch und die Spannung der externen
Stromversorgung messen. Ströme unter 200mA könne nicht zufriedenstellend
gemessen werden.


Technische Spezifikation
------------------------

===========================================  ============================================================
Eigenschaft                                  Wert
===========================================  ============================================================
Stromverbrauch                               20-30mA (hängt von Eingangsspannung ab)
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Minimale/Maximale Eingangsspannung           6V/27V
Maximaler Ausgangsstrom für 5V Versorgung    3A
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                      40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Gewicht                                      14g
===========================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/step-down-powersupply/raw/master/hardware/step-down-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/step_down_powersupply_dimensions.png>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/step-down-powersupply/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit der
Step-Down Power Supply.

.. image:: /Images/Power_Supplies/powersupply11_caption_600.jpg
   :scale: 100 %
   :alt: Step-Down Power Supply mit Beschriftung
   :align: center
   :target: ../../_images/Power_Supplies/powersupply11_caption_800.jpg
