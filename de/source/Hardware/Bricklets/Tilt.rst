
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Tilt Bricklet
:FIXME_shoplink: ../../../shop/bricklets/tilt-bricklet.html

.. include:: Tilt.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _tilt_bricklet:

Tilt Bricklet
=============

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_tilt_tilted_350.jpg",
	               "Bricklets/bricklet_tilt_tilted_600.jpg",
	               "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_vertical_100.jpg",
	             "Bricklets/bricklet_tilt_vertical_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_horizontal_100.jpg",
	             "Bricklets/bricklet_tilt_horizontal_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_master_100.jpg",
	             "Bricklets/bricklet_tilt_master_600.jpg",
	             "Tilt Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_brickv_100.jpg",
	             "Bricklets/bricklet_tilt_brickv.jpg",
	             "Tilt Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/tilt_bricklet_dimensions_100.png",
	             "Dimensions/tilt_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Erkennt Neigung des Bricklets (Neigungsschalter offen/geschlossen)
* Erkennt ob Bricklet vibriert.

Beschreibung
------------

Das Tilt Bricklet ist mit einem Neigungsschalter ausgestattet. Es kann
erkennen ob das Bricklet aktuell geneigt ist oder ob es vibriert.

Es ist möglich Events zu konfigurieren die automatisch ausgelöst werden 
wenn sich der Status des Tilt Bricklets ändert.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           25 x 15 x 15mm (0,98 x 0,59 x 0,59")
Gewicht                           3g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/tilt-bricklet/raw/master/hardware/tilt-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/tilt_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/tilt-bricklet/zipball/master>`__)


.. _tilt_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_tilt_master_600.jpg
   :scale: 100 %
   :alt: Tilt Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_tilt_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird nun der aktuelle Status
des Tilt Bricklet angezeigt.

.. image:: /Images/Bricklets/bricklet_tilt_brickv.jpg
   :scale: 100 %
   :alt: Tilt Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_tilt_brickv.jpg

|test_pi_ref|

.. _tilt_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Tilt Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-tilt-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_tilt_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Tilt Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_tilt_case_built_up_1000.jpg

.. include:: Tilt.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/tilt_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Tilt Bricklet
   :align: center
   :target: ../../_images/Exploded/tilt_exploded.png

|bricklet_case_hint|


.. _tilt_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Tilt_hlpi.table
