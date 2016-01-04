
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / CO2 Bricklet
:FIXME_shoplink: ../../../shop/bricklets/co2-bricklet.html

.. include:: CO2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _co2_bricklet:

CO2 Bricklet
============

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Misst CO2 Konzentration von 0 bis 10000 ppm (Teile pro Million)


.. _co2_bricklet_description:

Beschreibung
------------

Mit dem CO2 :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die `CO2 Konzentration
<https://de.wikipedia.org/wiki/Kohlenstoffdioxid>`__ der Luft messen.
Die gemessene CO2 Konzentration kann in `ppm
<https://de.wikipedia.org/wiki/Parts_per_million>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
CO2 Konzentrationsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Bricklet kann genutzt werden TBD.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            SenseAir K30
Stromverbrauch                    TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0ppm - 10000ppm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             TBD x TBD x TBDmm (TBD x TBD x TBD")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* SenseAir K30 Datenblatt (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/datasheets/K30_Datasheet.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/hardware/co2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/co2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/co2-bricklet/zipball/master>`__)


.. _co2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_co2_brickv.jpg
   :scale: 100 %
   :alt: CO2 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_co2_brickv.jpg

|test_pi_ref|


.. _co2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: CO2_hlpi.table
