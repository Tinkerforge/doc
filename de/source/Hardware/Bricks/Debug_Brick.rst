.. _debug_brick:

Debug Brick
===========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_debug_tilted_front_350.jpg",
	             "Bricks/brick_debug_tilted_front_600.jpg",
	             "Debug Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_debug_tilted_back_100.jpg",
	             "Bricks/brick_debug_tilted_back_600.jpg",
	             "Debug Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_debug_top_100.jpg",
	             "Bricks/brick_debug_top_600.jpg",
	             "Debug Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_debug_bottom_100.jpg",
	             "Bricks/brick_debug_bottom_600.jpg",
	             "Debug Brick Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/debug_brick_dimensions_100.png",
	             "Dimensions/debug_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Für Firmware Entwickler
* JTAG und serielle Konsole


Beschreibung
------------

Der Debug Brick kann benutzt werden um Debug-Möglichkeiten wie JTAG und eine
serielle Konsole zu :ref:`Bricks <product_overview_bricks>`,
:ref:`Bricklets <product_overview_bricklets>` und Stapeln hinzuzufügen.

.. note::
 Ein Debug Brick kann zum Debuggen der Low Level C Firmware von Bricks und
 Bricklets benutzt werden. Es ist nicht dafür gedacht für PC basierte
 Programmierung genutzt zu werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           40 x 40 x 8mm (1.57 x 1.57 x 0.31")*
Gewicht                           18g
================================  ============================================================

\* ohne Stecker


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/debug-brick/raw/master/hardware/debug-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/debug_brick_dimensions.png>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/debug-brick/zipball/master>`__)
