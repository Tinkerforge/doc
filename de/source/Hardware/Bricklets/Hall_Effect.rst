
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Hall Effect Bricklet
:FIXME_shoplink: ../../../shop/bricklets/hall-effect-bricklet.html

.. include:: Hall_Effect.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _hall_effect_bricklet:

Hall Effect Bricklet
====================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_hall_effect_tilted_350.jpg",
	               "Bricklets/bricklet_hall_effect_tilted_600.jpg",
	               "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_vertical_100.jpg",
	             "Bricklets/bricklet_hall_effect_vertical_600.jpg",
	             "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_horizontal_100.jpg",
	             "Bricklets/bricklet_hall_effect_horizontal_600.jpg",
	             "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_master_100.jpg",
	             "Bricklets/bricklet_hall_effect_master_600.jpg",
	             "Hall Effect Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_brickv_100.jpg",
	             "Bricklets/bricklet_hall_effect_brickv.jpg",
	             "Hall Effect Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/hall_effect_bricklet_dimensions_100.png",
	             "Dimensions/hall_effect_bricklet_dimensions_600.png",
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

* Schaltplan (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/hardware/hall-effect-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hall_effect_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/zipball/master>`__)


.. _hall_effect_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_hall_effect_master_600.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_hall_effect_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_brickv.jpg

|test_pi_ref|

.. _hall_effect_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Hall Effect Bricklet <https://www.tinkerforge.com/de/shop/cases/case-hall-effect-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_hall_effect_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Hall Effect Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_hall_effect_case_built_up_1000.jpg

.. include:: Hall_Effect.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/hall_effect_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Hall Effect Bricklet
   :align: center
   :target: ../../_images/Exploded/hall_effect_exploded.png

|bricklet_case_hint|


.. _hall_effect_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Hall_Effect_hlpi.table
