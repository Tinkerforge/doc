
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Linear Poti Bricklet
:shoplink: ../../../shop/bricklets/linear-poti-bricklet.html

.. include:: Linear_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _linear_poti_bricklet:

Linear Poti Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_linear_poti_tilted_350.jpg",
	               "Bricklets/bricklet_linear_poti_tilted_600.jpg",
	               "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_front_100.jpg",
	             "Bricklets/bricklet_linear_poti_front_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_vertical_100.jpg",
	             "Bricklets/bricklet_linear_poti_vertical_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_horizontal_100.jpg",
	             "Bricklets/bricklet_linear_poti_horizontal_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_knob_100.jpg",
	             "Bricklets/bricklet_linear_poti_knob_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_master_100.jpg",
	             "Bricklets/bricklet_linear_poti_master_600.jpg",
	             "Linear Poti Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_linear_poti_case_100.jpg",
	             "Cases/bricklet_linear_poti_case_600.jpg",
	             "Linear Poti Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_brickv_100.jpg",
	             "Bricklets/bricklet_linear_poti_brickv.jpg",
	             "Linear Poti Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/linear_poti_bricklet_dimensions_100.png",
	             "Dimensions/linear_poti_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 59mm Linear-Potentiometer
* Ausgabe der Position von 0% bis 100% in 1% Schritten



Beschreibung
------------

Das Linear Poti :ref:`Bricklet <product_overview_bricklets>` ist mit einem
Linear-`Potentiometer <http://de.wikipedia.org/wiki/Potentiometer>`__
("Fader", "Slider") ausgestattet. :ref:`Brick <product_overview_bricks>`
können die Position des Sliders auslesen. Zusätzlich können Events konfiguriert
werden die bei einer definierten Position des Sliders ausgelöst werden.

Dieses Bricklet kann für Steuerungsaufgaben genutzt werden, wie z.B. das
Einstellen der Lautstärke eines Mediaplayers.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Linear-Potentiometer              59mm (2,32") einstellbare Länge
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          0% - 100% (Slider unten - Slider oben) in 1% Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 85 x 20mm (0,98 x 3,35 x 0,78")*
Gewicht                           14g*
================================  ============================================================

\* ohne Knopf


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/raw/master/hardware/linear-poti-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/linear_poti_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/zipball/master>`__)


.. _linear_poti_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_linear_poti_master_600.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_linear_poti_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current12_brickv.jpg

Der Graph ist durch hoch und runter bewegen des Sliders entstanden.

|test_pi_ref|

.. _linear_poti_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Linear Poti Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-linear-poti-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_linear_poti_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Linear Poti Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_linear_poti_case_1000.jpg

.. include:: Linear_Poti.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/linear_poti_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Linear Poti Bricklet
   :align: center
   :target: ../../_images/Exploded/linear_poti_exploded.png

|bricklet_case_hint|

.. _linear_poti_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Linear_Poti_hlpi.table
