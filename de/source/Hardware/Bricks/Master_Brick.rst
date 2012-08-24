.. _master_brick:

Master Brick
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_master_tilted_front_350.jpg",
	             "Bricks/brick_master_tilted_front_600.jpg",
	             "Master Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_master_tilted_back_100.jpg",
	             "Bricks/brick_master_tilted_back_600.jpg",
	             "Master Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_master_stack_front_big_100.jpg",
	             "Bricks/brick_master_stack_front_big_600.jpg",
                 "Master Brick in Stapel")
	}}
	{{
	    tfdocimg("Bricks/brick_master_stack_back_big_100.jpg",
	             "Bricks/brick_master_stack_back_big_600.jpg",
                 "Master Brick im Stapel")
	}}
	{{
	    tfdocimg("Bricks/brick_master_caption_100.jpg",
	             "Bricks/brick_master_caption_600.jpg",
	             "Master Brick mit Beschriftung")
	}}
	{{
	    tfdocimg("Bricks/brick_master_top_100.jpg",
	             "Bricks/brick_master_top_600.jpg",
	             "Master Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_master_bottom_100.jpg",
	             "Bricks/brick_master_bottom_600.jpg",
	             "Master Brick Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/master_brick_dimensions_100.png",
	             "Dimensions/master_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Ist Grundlage um Stapel zu bauen
* Benutzbar mit kabelgebundenen und kabellosen Master Extensions
* Eine USB und **vier** Bricklet Schnittstellen


Beschreibung
------------

Der Master :ref:`Brick <product_overview_bricks>` ist mit einem 32-Bit ARM
Mikrocontroller ausgestattet und besitzt zwei Aufgaben.
Als erstes besitzt es **vier** :ref:`Bricklet <product_overview_bricklets>`
Anschlüsse und ist daher ideal geeignet für Anwendungen bei denen viele
Bricklets genutzt werden.

Als zweites kann das Master Brick für Kommunikationsaufgaben genutzt werden.
Wird ein Stapel von Bricks aufgebaut so arbeitet der untere Brick als Master
des Stapels und leitet Daten von dem PC an die Platinen des Stapels weiter.
Andere Master Bricks im Stapel erkennen, dass sie nicht als Master eingesetzt
sind und stellen nur ihre angeschlossenen Bricklets zur Verfügung.

Im einfachsten Fall werden Daten von einem PC über die **USB** Verbindung
des Master Bricks geleitet. Diese Schnittstelle kann mit Master Extensions
geändert werde. Es gibt Master Extensions für kabelgebundene Schnittstellen
(**RS485**, **Ethernet**) und kabellose Schnittstellen (**WLAN**).
Diese können auf einen Master Brick gesteckt werden und werden von diesem
als weitere Schnittstelle erkannt.

Da die Firmware Open Source ist, ist es natürlich auch möglich den Brick direkt
zu programmieren (:ref:`On Device Programmierung <pi_odpi>`).
Momentan bieten wir keine On Device API an.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Mikrocontroller                   ATSAM3S4C (256kB Flash, 48kB RAM)
Stromverbrauch                    53mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse               4
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           12g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/master_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/master-brick/zipball/master>`__)


.. _master_brick_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
Master Bricks.

.. image:: /Images/Bricks/brick_master_caption_600.jpg
   :scale: 100 %
   :alt: Master Brick mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_master_caption_800.jpg


.. _master_brick_test:

Test your Master Brick
----------------------

To test the Master Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Brick to the PC over USB. You should see a tab named
"Master Brick" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricks/master_brickv.jpg
   :scale: 100 %
   :alt: Master Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/master_brickv.jpg

You should see that the Master Brick isn't measuring any stack voltages or
currents. This is because you have not attached a
:ref:`Power Supply <product_overview_powersupplies>`. When attaching
such a board you should see the voltage applied to your stack and the current
flowing in.

After this small test you can go on with writing your own application.
See the :ref:`Programming Interface <master_brick_programming_interfaces>` section
for  the API of the Master Brick and examples in different programming languages.


.. _master_brick_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Master_Brick_hlpi.table


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

