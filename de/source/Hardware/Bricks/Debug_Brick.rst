
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Debug Brick
:shoplink: ../../../shop/bricks/debug-brick.html

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


.. _debug_brick_description:

Beschreibung
------------

Der Debug Brick kann benutzt werden um Debug-Möglichkeiten wie JTAG und eine
serielle Konsole zu :ref:`Bricks <primer_bricks>`,
:ref:`Bricklets <primer_bricklets>` und :ref:`Stapeln <primer_stack>` 
hinzuzufügen.

.. note::
 Ein Debug Brick kann zum Debuggen der Low Level C Firmware von Bricks und
 Bricklets benutzt werden. Es ist nicht dafür gedacht für PC basierte
 Programmierung genutzt zu werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           40 x 40 x 8mm (1,57 x 1,57 x 0,31")*
Gewicht                           18g
================================  ============================================================

\* ohne Stecker


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/debug-brick/raw/master/hardware/debug-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/debug_brick_dimensions.png>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/debug-brick/zipball/master>`__)

Bekannte Fehler/Probleme
------------------------

Bei dem Debug Brick Hardware Version 1.1 sind die GND Pins des JTAG Steckers
nicht verbunden. Dies kann zu Problemen mit der JTAG Verbindung führen. Die 
serielle Konsole ist davon nicht betroffen. Das JTAG Problem kann über das 
Anlöten eines  Drähtchens zwischen einem GND Pin des JTAG Steckers und GND auf 
der Platine behoben werden. Der Fehler wird in der nächsten Hardwareversion 
behoben.

.. image:: /Images/Bricks/brick_debug_wire_fix_350.jpg
   :scale: 100 %
   :alt: Debug Brick mit Draht
   :align: center
   :target: ../../_images/Bricks/brick_debug_wire_fix_1000.jpg


