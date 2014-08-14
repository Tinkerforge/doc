
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Hall Effect Bricklet
:shoplink: ../../../shop/bricklets/hall-effect-bricklet.html

.. include:: Hall_Effect.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _hall_effect_bricklet:

Hall Effect Bricklet
====================

.. raw:: html

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
	    tfdocimg("Bricklets/bricklet_hall_effect_tilted_back_100.jpg",
	             "Bricklets/bricklet_hall_effect_tilted_back_600.jpg",
	             "Hall Effect Bricklet")
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

* Detektiert Magnetfelder
* Zählt das Auftreten und Verschwinden eines Magnetfelds
* Kann genutzt werden um einen Wasser-/Stromzähler auszulesen


.. _hall_effect_bricklet_description:

Beschreibung
------------

Das Hall Effect :ref:`Bricklet <primer_bricklets>` kann die Präsenz
eines Magnetfelds detektieren. Es zählt das Auftreten und Verschwinden eines
Magnetfelds und kann von :ref:`Bricks <primer_bricks>` genutzt werden, um z.B. 
die Geschwindigkeit eines Rades, an dem ein Magnet befestigt ist, mit bis zu 
13Hz zu messen.

Beispielanwendungen:

* Erkennung ob eine Tür geöffnet oder geschlossen ist
* Auslesen eines Wasser-/Stromzählers

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            AH180N
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Funktionsweise                    Omnipolar (Nord- und Südpol werden detektiert)
Auslösepunkt                      -35/35 Gauss
Freigabepunkt                     -25/25 Gauss
Abtastrate                        8Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* AH180N Datenblatt (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/datasheets/AH180N.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/hardware/hall-effect-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hall_effect_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/zipball/master>`__)


.. _hall_effect_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird ein Magnetfeld erkannt. Zum Testen
kann zum Beispiel ein Magnet verwendet werden, der an dem Bricklet vorbei geführt wird.

.. image:: /Images/Bricklets/bricklet_hall_effect_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_brickv.jpg

|test_pi_ref|


.. _hall_effect_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Hall_Effect_hlpi.table
