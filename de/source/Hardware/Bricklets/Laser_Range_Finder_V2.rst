
:DISABLED_shoplink: ../../../shop/bricklets/laser-range-finder-v2-bricklet.html

.. include:: Laser_Range_Finder_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_v2_bricklet:

Laser Range Finder Bricklet 2.0
===============================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_laser_range_finder_v2_tilted_[?|?].jpg           Laser Range Finder Bricklet 2.0
	Bricklets/bricklet_laser_range_finder_v2_horizontal_[?|?].jpg       Laser Range Finder Bricklet 2.0
	Bricklets/bricklet_laser_range_finder_v2_master_[100|600].jpg       Laser Range Finder Bricklet 2.0 mit Master Brick
	Cases/bricklet_laser_range_finder_v2_case_[100|600].jpg             Laser Range Finder Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_laser_range_finder_v2_brickv_[100|].jpg          Laser Range Finder Bricklet 2.0 im Brick Viewer
	Dimensions/laser_range_finder_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Entfernung und Geschwindigkeit mit Laser-Pulsen
* Entfernungs-Messbereich 0-40m mit 1cm Auflösung
* Messfrequenz bis zu 500Hz.


.. _laser_range_finder_v2_bricklet_description:

Beschreibung
------------

Mit dem Laser Range Finder :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` Entfernungen und Geschwindigkeiten messen.
Dies wird mit einer `Laufzeitmessung <https://de.wikipedia.org/wiki/Laufzeitmessung>`__
von Laser-Pulsen bewerkstelligt.

Das Laser Range Finder Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Sensor                                LIDAR-Lite (V3)
Stromverbrauch                        | 230mW (46mA bei 5V, Laser aus)
                                      | 455mW (91mA bei 5V, Laser an)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Entfernung (Bereich, Auflösung)       0-40m, 1cm
Abtastrate                            bis zu 500Hz (abhängig von Entfernung)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               49 x 45 x 36mm (1,93 x 1,77 x 1,42")
Gewicht                               30g
====================================  ============================================================


Ressourcen
----------

* LIDAR-Lite V3 Datenblatt (`Download <https://github.com/Tinkerforge/laser-range-finder-v2-bricklet/raw/master/datasheets/lidar-lite-v3.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/laser-range-finder-v2-bricklet/raw/master/hardware/laser-range-finder-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/laser_range_finder_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/laser-range-finder-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2Hx8J8y>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/laser_range_finder_v2/laser-range-finder-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/laser_range_finder_v2/laser-range-finder-v2.FCStd>`__)


.. _laser_range_finder_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Klicke auf die "Enable Laser" Checkbox, um den Laser zu aktivieren.
Wenn alles wie erwartet funktioniert wird die gemessene Distanz des Sensors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Distanz wieder.
Das folgende Bild entstand durch langsames auf den Sensor zu und wieder
wegbewegen einer Hand.

.. image:: /Images/Bricklets/bricklet_laser_range_finder_v2_brickv.jpg
   :scale: 100 %
   :alt: Laser Range Finder Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_laser_range_finder_v2_brickv.jpg

|test_pi_ref|


.. _laser_range_finder_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Laser_Range_Finder_V2_hlpi.table
