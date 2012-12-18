.. include:: GPS.substitutions


.. _gps_bricklet:

GPS Bricklet
============


Features
--------

* Empfängt Positions- und Zeitdaten
* Interne Antenne, externe Antenne optional
* 66 Kanäle, 10 Hz Update-Rate
* Hohe Empfindlichkeit und Genauigkeit, Störunterdrückung


Beschreibung
------------
Mit dem GPS :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` ihre Position bestimmen.
Das Bricklet kann aber auch dazu genutzt werden um hochgenaue Zeitinformationen 
zu empfangen.

Todo:
* Ausgabe Formate

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
GPS Modul Chipsatz                MTK MT3339 (PA6H Modul)
Empfindlichkeit                   -148dBm (Acquisition)*, -165dBm (Tracking)*
Positionsgenauigkeit              3.0m (50% CEP)*
Zeit bis erster Fix               <35s (ohne Batterie)*, <1s (mit Batterie)*
Update-Rate                       10Hz
================================  ============================================================
* Datenblattangaben


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/hardware/gps-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/gps_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/gps-bricklet/zipball/master>`__)
* PA6H Datasheet (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/datasheets/FGPMMOPA6H.pdf>`__)


.. _gps_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

..
  .. image:: /Images/Bricklets/bricklet_gps_master_600.jpg
     :scale: 100 %
     :alt: GPS Bricklet verbunden mit Master Brick
     :align: center
     :target: ../../_images/Bricklets/bricklet_gps_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

..
  .. image:: /Images/Bricklets/bricklet_gps_brickv.jpg
     :scale: 100 %
     :alt: GPS Bricklet im Brick Viewer
     :align: center
     :target: ../../_images/Bricklets/bricklet_gps_brickv.jpg

|test_pi_ref|


.. _gps_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: GPS_hlpi.table
