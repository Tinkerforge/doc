
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Laser Range Finder Bricklet
:FIXME_shoplink: ../../../shop/bricklets/laser-range-finder-bricklet.html

.. include:: Laser_Range_Finder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_bricklet:

Laser Range Finder Bricklet
===========================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------


.. _laser_range_finder_bricklet_description:

Beschreibung
------------


Technische Spezifikation
------------------------

====================================  ============================================================
Property                              Value
====================================  ============================================================
Stromverbrauch                        TBDmA
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Entfernung (Bereich, Auflösung)       * 0-40m, 1cm

Geschwindigkeit (Bereich, Auflösung)  * 0-12.7 m/s, 0,1m/s
                                      * 0-31,75 m/s, 0,25m/s
                                      * 0-63,5 m/s, 0,5m/s
                                      * 0-127 m/s, 1,0m/s
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               49 x 36 x 48mm (1,93 x 1,42 x 1,89")
Gewicht                               TBDg
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


.. _laser_range_finder_bricklet_case:

Gehäuse
-------


.. _laser_range_finder_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Laser_Range_Finder_hlpi.table
