
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Rotary Poti Bricklet
:shoplink: ../../../shop/bricklets/rotary-poti-bricklet.html

.. include:: Rotary_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rotary_poti_bricklet:

Rotary Poti Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_rotary_poti_tilted_350.jpg",
	               "Bricklets/bricklet_rotary_poti_tilted_600.jpg",
	               "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_front_100.jpg",
	             "Bricklets/bricklet_rotary_poti_front_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_vertical_100.jpg",
	             "Bricklets/bricklet_rotary_poti_vertical_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_horizontal_100.jpg",
	             "Bricklets/bricklet_rotary_poti_horizontal_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_knob_100.jpg",
	             "Bricklets/bricklet_rotary_poti_knob_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_master_100.jpg",
	             "Bricklets/bricklet_rotary_poti_master_600.jpg",
	             "Rotary Poti Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_rotary_poti_case_shallow_100.jpg",
	             "Cases/bricklet_rotary_poti_case_shallow_600.jpg",
	             "Rotary Poti Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_brickv_100.jpg",
	             "Bricklets/bricklet_rotary_poti_brickv.jpg",
	             "Rotary Poti Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/rotary_poti_bricklet_dimensions_100.png",
	             "Dimensions/rotary_poti_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 300° Dreh-Potentiometer
* Ausgabe der Position von -150° bis 150° in 1° Schritten


.. _rotary_poti_bricklet_description:

Beschreibung
------------

Das Rotary Poti :ref:`Bricklet <primer_bricklets>` ist mit einem
Dreh-`Potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`__ ausgestattet,
dessen Position über ein :ref:`Brick <primer_bricks>` ausgelesen werden kann. 
Zusätzlich können Events konfiguriert werden die ausgelöst werden wenn eine 
spezifizierte Position erreicht wird.

Dieses Bricklet kann für Steueraufgaben benutzt werden wie z.B. das Steuern
einer Lautstärke.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Dreh-Potentiometer                1 Umdrehung, 300°
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          -150° bis 150° (links nach rechts) in 1° Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 23mm (1,18 x 0,98 x 0,9")*
Gewicht                           5g*
================================  ============================================================

\* ohne Knopf


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/raw/master/hardware/rotary-poti-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rotary_poti_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/zipball/master>`__)


.. _rotary_poti_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_rotary_poti_master_600.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg

Der Graph ist durch Drehen des Knopfes von links nach rechts und zurück
entstanden.

|test_pi_ref|

.. _rotary_poti_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Rotary Poti Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-rotary-poti-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_rotary_poti_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_poti_case_1000.jpg

.. include:: Rotary_Poti.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|


.. _rotary_poti_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Rotary_Poti_hlpi.table
