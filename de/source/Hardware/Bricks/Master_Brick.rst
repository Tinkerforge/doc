
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Master Brick
:shoplink: ../../../shop/bricks/master-brick.html

.. include:: Master_Brick.substitutions


.. _master_brick:

Master Brick
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_master21_tilted_front_350.jpg",
	               "Bricks/brick_master21_tilted_front_800.jpg",
	               "Master Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_master_stack_front_big_100.jpg",
	             "Bricks/brick_master_stack_front_big_800.jpg",
                 "Master Brick in Stapel")
	}}
	{{
	    tfdocimg("Bricks/brick_master_stack_back_big_100.jpg",
	             "Bricks/brick_master_stack_back_big_800.jpg",
                 "Master Brick im Stapel")
	}}
	{{
	    tfdocimg("Bricks/brick_master_caption_100.jpg",
	             "Bricks/brick_master_caption_800.jpg",
	             "Master Brick mit Beschriftung")
	}}
	{{
	    tfdocimg("Bricks/brick_master20_top_100.jpg",
	             "Bricks/brick_master20_top_800.jpg",
	             "Master Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_master20_bottom_100.jpg",
	             "Bricks/brick_master20_bottom_800.jpg",
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

* Bis zu **vier** Bricklets per USB steuerbar
* Ist Grundlage um Stapel zu bauen
* Benutzbar mit kabelgebundenen und drahtlosen Master Extensions


.. _master_brick_description:

Beschreibung
------------

Der Master :ref:`Brick <primer_bricks>` besitzt zwei Aufgaben:
Als erstes besitzt er **vier** :ref:`Bricklet <primer_bricklets>`
Anschlüsse und ist daher ideal geeignet für Anwendungen bei denen viele
Bricklets genutzt werden. Diese können dann direkt über die **USB** 
Schnittstelle des Master Bricks gesteuert werden. Somit können USB Sensoren, 
zum Beispiel zur Messung der Luftfeuchtigkeit und Temperatur, aber auch USB 
Aktoren, wie Relais, ganz nach den eigenen Bedürfnissen aufgebaut werden.

Als zweites kann der Master Brick für Kommunikationsaufgaben genutzt werden.
Wird ein :ref:`Stapel <primer_stack>` von Bricks aufgebaut so arbeitet der 
unterste Brick als Master des Stapels und leitet Daten vom steuernden Gerät
an die Platinen des Stapels weiter. Andere Master Bricks im Stapel erkennen, 
dass sie nicht als Master eingesetzt sind und stellen nur ihre angeschlossenen 
Bricklets zur Verfügung. Es ist also nur eine USB Verbindung, die des untersten 
Master Bricks, für einen ganzen Stapel von Bricks notwendig.

Die USB Schnittstelle kann durch Master Extensions ersetzt werden. Es gibt
Master Extensions für kabelgebundene Schnittstellen
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
und drahtlose Schnittstellen (:ref:`WLAN <wifi_extension>`).
Extensions können auf einen Master Brick gesteckt werden und werden von diesem
als weitere Schnittstelle erkannt. Somit können Bricks und Bricklets zum 
Beispiel direkt aus dem eigenen Netzwerk gesteuert werden (WLAN, Ethernet) oder
aber über größere Strecken vernetzt werden (RS485).

Der größtmögliche Stapel besteht aus (von unten nach oben)
1x Step-Down Power Supply, 1x Master Brick, 8x beliebige andere Bricks, 
2x Master Extensions. Wenn alle Bricks im Stapel Master Bricks sind können bis 
zu 9 Master Bricks x je 4 Bricklets = 36 Bricklets an einem Stapel 
angeschlossen werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Bricklet Anschlüsse               4
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           12g
Stromverbrauch                    68mA
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

Erster Test
-----------

|test_intro|

|test_tab|

.. image:: /Images/Bricks/master_brickv.jpg
   :scale: 100 %
   :alt: Master Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/master_brickv.jpg

Die Messung Versorgungsspannung des Stapels und des Stromverbrauchs sollte
jeweils Null anzeigen. Dies liegt daran, dass keine :ref:`Stromversorgung
<primer_power_supplies>` angeschlossen ist. Wenn eine unter den
Stapel gesteckt wurde, dann wird hier die angelegte Spannung und der
Stromverbrauch des Stapels angezeigt.

|test_pi_ref|


.. _master_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Master_Brick_hlpi.table
