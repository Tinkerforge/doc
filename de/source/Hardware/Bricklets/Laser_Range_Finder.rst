
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Laser Range Finder Bricklet
:shoplink: ../../../shop/bricklets/laser-range-finder-bricklet.html

.. include:: Laser_Range_Finder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_bricklet:

Laser Range Finder Bricklet
===========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_laser_range_finder_tilted1_350.jpg",
	               "Bricklets/bricklet_laser_range_finder_tilted1_600.jpg",
	               "Laser Range Finder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_laser_range_finder_tilted2_350.jpg",
	             "Bricklets/bricklet_laser_range_finder_tilted2_600.jpg",
	             "Laser Range Finder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_laser_range_finder_bottom_100.jpg",
	             "Bricklets/bricklet_laser_range_finder_bottom_600.jpg",
	             "Laser Range Finder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_laser_range_finder_brickv_100.jpg",
	             "Bricklets/bricklet_laser_range_finder_brickv.jpg",
	             "Laser Range Finder Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/laser_range_finder_bricklet_dimensions_100.png",
	             "Dimensions/laser_range_finder_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Entfernung unf Geschwindigkeit mit Laser-Pulsen
* Entfernungs-Messbereich 0-40m mit 1cm Auflösung
* Geschwindigkeits-Messbereich bis zu 0-127m/s mit bis 0,1m/s Auflösung


.. _laser_range_finder_bricklet_description:

Beschreibung
------------

Mit dem Laser Range Finder :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Entfernungen und Geschwindingkeiten messen.
Dies wird der `Laufzeitmessung <https://de.wikipedia.org/wiki/Laufzeitmessung>`__
von Laser-Pulsen bewerkstelligt.


Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Sensor                                LIDAR-Lite
Stromverbrauch                        | 450mW (90mA bei 5V, Laser aus)
                                      | 520mW (104mA bei 5V, Laser an)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Entfernung (Bereich, Auflösung)       * 0-40m, 1cm

Geschwindigkeit (Bereich, Auflösung)  * 0-12,7m/s, 0,1m/s
                                      * 0-31,75m/s, 0,25m/s
                                      * 0-63,5m/s, 0,5m/s
                                      * 0-127m/s, 1,0m/s

Abtastrate                            * bis zu 100Hz (abhängig von Entfernung)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               49 x 45 x 36mm (1,93 x 1,77 x 1,42")
Gewicht                               39g
====================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/raw/master/hardware/laser-range-finder-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/laser_range_finder_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/zipball/master>`__)


.. _laser_range_finder_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Klicke auf die "Enable Laser" Checkbox, um den Laser zu aktivieren.
Wenn alles wie erwartet funktioniert wird die gemessen Distanz und die
Ausgangsspannung des Sensors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Distanz wieder.
Das folgende Bild entstand durch langsames auf den Sensor zu und wieder
wegbewegen einer Hand.

.. image:: /Images/Bricklets/bricklet_laser_range_finder_brickv.jpg
   :scale: 100 %
   :alt: Laser Range Finder Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_laser_range_finder_brickv.jpg

|test_pi_ref|


.. _laser_range_finder_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Laser_Range_Finder_hlpi.table
