
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Step-Down Power Supply
:shoplink: ../../../shop/power-supplies/step-down-power-supply.html

.. _step_down_power_supply:

Step-Down Power Supply
======================

.. raw:: html

	{% tfgallery %}

	Power_Supplies/powersupply11_tilted_[?|?].jpg              Step-Down Power Supply
	Power_Supplies/powersupply11_caption_[?|?].jpg             Step-Down Power Supply mit Beschriftung
	Power_Supplies/powersupply11_horizontal_[?|?].jpg          Step-Down Power Supply
	Power_Supplies/powersupply11_connector_[100|600].jpg       Step-Down Power Supply mit Steckern
	Dimensions/step_down_powersupply_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Versorgt einen Stapel von Bricks mit 5V
* Kann an Bricks angeschlossen Motoren versorgen (z.B. DC Brick)
* Eingangsspannung 6V bis 27V DC
* Zusätzlich Ausgangsspannung 5V (seit Hardwareversion 1.1)


Beschreibung
------------


Die Step-Down Power Supply kann verwendet werden um einen 
:ref:`Stapel <primer_stack>` von :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` mit Strom zu versorgen.
Sie ist mit einem effizienten Step-Down Regler ausgestattet und wird unter
einen Stapel gesteckt. Von dort stellt sie die 5V bereit die von Bricks und
Bricklets benötigt werden. Zusätzlich speist sie die externe Versorgungsspannung
in die Stapelstromversorgung ein. Sie ist nicht zwingend notwendig um einzelne
Bricks zu betreiben, sondern ist für die Verwendung in Stapeln vorgesehen.

Es gibt verschiedene Anwendungsfälle. Die Step-Down Power Supply ermöglicht
Stapel über Batterien zu versorgen. Solche Stapel können dann über
kabelgebundene oder drahtlose Master Extensions kommunizieren. Die Step-Down
Power Supply ermöglicht kann auch genutzt werden um über den Stapel DC Motoren,
Servos oder Schrittmotoren zu versorgen (über die Stapelstromversorgung mit bis
zu 27V DC) ohne eine weitere externe Spannungsquelle an den entsprechenden
Motortreiber Brick anschließen zu müssen.
Falls der Stromverbrauch großer Stapel die 500mA überschreitet die ein normaler
USB Anschluss liefern kann, so kann hier die Step-Down Power Supply einspringen
und die Stromversorgung des Stapels übernehmen.

Der erlaubt Eingangsspannungsbereich betragt 6V bis 27V DC.
Ein :ref:`Master Brick <master_brick>` kann den Stromverbrauch und die Spannung
der externen Stromversorgung messen. Ströme unter 200mA könne nicht
zufriedenstellend gemessen werden.


Technische Spezifikation
------------------------

===========================================  ============================================================
Eigenschaft                                  Wert
===========================================  ============================================================
Stromverbrauch                               20-30mA, abhängig von der Eingangsspannung
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Minimale/Maximale Eingangsspannung           6V/27V DC
Maximaler Ausgangsstrom                      | 5V Versorgung: 3A
                                             | Durchleitung für Motortreiber Bricks: 5A
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
* 3D Modell (`Online ansehen <http://a360.co/2s95Th9>`__ | Download: `STEP <http://download.tinkerforge.com/3d/power_supplies/step_down/step-down.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/power_supplies/step_down/step-down.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit der
Step-Down Power Supply.

.. image:: /Images/Power_Supplies/powersupply11_caption_600.jpg
   :scale: 100 %
   :alt: Step-Down Power Supply mit Beschriftung
   :align: center
   :target: ../../_images/Power_Supplies/powersupply11_caption_800.jpg
