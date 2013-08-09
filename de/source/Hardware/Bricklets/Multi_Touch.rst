
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Multi Touch Bricklet
:FIXME_shoplink: ../../../shop/bricklets/multi-touch-bricklet.html

.. include:: Multi_Touch.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _multi_touch_bricklet:

Multi Touch Bricklet
====================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 und die Dokumentation sind in einem halbfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_multi_touch_tilted_350.jpg",
	               "Bricklets/bricklet_multi_touch_tilted_600.jpg",
	               "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_vertical_100.jpg",
	             "Bricklets/bricklet_multi_touch_vertical_600.jpg",
	             "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_horizontal_100.jpg",
	             "Bricklets/bricklet_multi_touch_horizontal_600.jpg",
	             "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_master_100.jpg",
	             "Bricklets/bricklet_multi_touch_master_600.jpg",
	             "Multi Touch Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_brickv_100.jpg",
	             "Bricklets/bricklet_multi_touch_brickv.jpg",
	             "Multi Touch Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/multi_touch_bricklet_dimensions_100.png",
	             "Dimensions/multi_touch_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Work In Progress


Beschreibung
------------


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           ? x ? x ?mm (? x ? x ?")
Gewicht                           ?g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/raw/master/hardware/multi-touch-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/multi_touch_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/zipball/master>`__)


.. _multi_touch_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_multi_touch_master_600.jpg
   :scale: 100 %
   :alt: Multi Touch Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_multi_touch_brickv.jpg
   :scale: 100 %
   :alt: Multi Touch Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_brickv.jpg

|test_pi_ref|

.. _multi_touch_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Multi Touch Bricklet <https://www.tinkerforge.com/de/shop/cases/case-multi-touch-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_multi_touch_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Multi Touch Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_multi_touch_case_built_up_1000.jpg

.. include:: Multi_Touch.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/multi_touch_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Multi Touch Bricklet
   :align: center
   :target: ../../_images/Exploded/multi_touch_exploded.png

|bricklet_case_hint|


.. _multi_touch_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Multi_Touch_hlpi.table
