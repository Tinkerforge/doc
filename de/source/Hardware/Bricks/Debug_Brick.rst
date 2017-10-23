
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Debug Brick
:shoplink: ../../../shop/bricks/debug-brick.html

.. _debug_brick:

Debug Brick
===========

.. raw:: html

	{% tfgallery %}

	Bricks/brick_debug12_tilted_[?|?].jpg         Debug Brick
	Bricks/brick_debug12_w_headers_[100|800].jpg  Debug Brick mit eingelöteten Stiftleisten
	Bricks/brick_debug12_top_[?|?].jpg            Debug Brick Oberseite
	Bricks/brick_debug12_bottom_[?|?].jpg         Debug Brick Unterseite
	Bricks/brick_debug12_stack_[?|?].jpg          Debug Brick auf Stapel

	{% tfgalleryend %}

.. FIXME: veraltet
	{{
	    tfdocimg("Dimensions/debug_brick_dimensions_100.png",
	             "Dimensions/debug_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}

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

Ein Debug Brick kann zum Debuggen der Low Level C Firmware von Bricks und
Bricklets benutzt werden. Es ist nicht dafür gedacht für PC basierte
Programmierung genutzt zu werden.

In Hardware Version 1.2 wurde der D-Sub 9 Anschluss durch einen Mini-USB Anschluss
und einen Silicon Labs CP2104 USB-nach-Seriell Wandler ersetzt. Dieser Wandler
benötigt einen extra Treiber der von der `Silicon Labs
<https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>`__
Webseite heruntergeladen werden kann.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           40 x 40 x 8mm (1,57 x 1,57 x 0,31")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/debug-brick/raw/master/hardware/debug-schematic.pdf>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/debug-brick/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2gDeatv>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricks/debug/debug.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricks/debug/debug.FCStd>`__)

.. FIXME: veraltet. gehört ursprünglich zwischen Schaltplan und Platinenlayout
	* Umriss und Bohrplan (`Download <../../_images/Dimensions/debug_brick_dimensions.png>`__)

Bekannte Fehler/Probleme
------------------------

Bei dem (nicht mehr verkauften) Debug Brick mit Hardware Version 1.1 sind die 
GND Pins des JTAG Steckers nicht verbunden. Dies kann zu Problemen mit der JTAG 
Verbindung führen. Die serielle Konsole ist davon nicht betroffen.
Das JTAG Problem kann über das 
Anlöten eines  Drähtchens zwischen einem GND Pin des JTAG Steckers und GND auf 
der Platine behoben werden. Der Fehler wird in der nächsten Hardwareversion 
behoben.

.. image:: /Images/Bricks/brick_debug_wire_fix_350.jpg
   :scale: 100 %
   :alt: Debug Brick mit Draht
   :align: center
   :target: ../../_images/Bricks/brick_debug_wire_fix_1000.jpg


