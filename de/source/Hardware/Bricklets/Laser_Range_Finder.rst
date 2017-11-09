
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Laser Range Finder Bricklet
:shoplink: ../../../shop/bricklets/laser-range-finder-bricklet.html

.. include:: Laser_Range_Finder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_bricklet:

Laser Range Finder Bricklet
===========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_laser_range_finder_tilted1_[?|?].jpg          Laser Range Finder Bricklet
	Bricklets/bricklet_laser_range_finder_tilted2_[?|?].jpg          Laser Range Finder Bricklet
	Bricklets/bricklet_laser_range_finder_bottom_[?|?].jpg           Laser Range Finder Bricklet
	Bricklets/bricklet_laser_range_finder_brickv_[100|].jpg          Laser Range Finder Bricklet im Brick Viewer
	Dimensions/laser_range_finder_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Entfernung und Geschwindigkeit mit Laser-Pulsen
* Entfernungs-Messbereich 0-40m mit 1cm Auflösung
* Messfrequenz bis zu 500Hz.


.. _laser_range_finder_bricklet_description:

Beschreibung
------------

Mit dem Laser Range Finder :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Entfernungen und Geschwindigkeiten messen.
Dies wird mit einer `Laufzeitmessung <https://de.wikipedia.org/wiki/Laufzeitmessung>`__
von Laser-Pulsen bewerkstelligt.


Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Sensor                                LIDAR-Lite (V3)
Stromverbrauch                        | 450mW (90mA bei 5V, Laser aus)
                                      | 520mW (104mA bei 5V, Laser an)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Entfernung (Bereich, Auflösung)       0-40m, 1cm
Abtastrate                            bis zu 500Hz (abhängig von Entfernung)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               49 x 45 x 36mm (1,93 x 1,77 x 1,42")
Gewicht                               39g
====================================  ============================================================


Ressourcen
----------

* LIDAR-Lite Datenblatt (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/raw/master/datasheets/LIDAR-Lite-v1.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/raw/master/hardware/laser-range-finder-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/laser_range_finder_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2hfjrUH>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/laser_range_finder/laser-range-finder.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/laser_range_finder/laser-range-finder.FCStd>`__)


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
