
.. include:: CO2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _co2_bricklet:

CO2 Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_co2_tilted1_[?|?].jpg          CO2 Bricklet
	Bricklets/bricklet_co2_tilted2_[?|?].jpg          CO2 Bricklet
	Bricklets/bricklet_co2_horizontal_[?|?].jpg       CO2 Bricklet
	Bricklets/bricklet_co2_brickv_[100|].jpg          CO2 Bricklet im Brick Viewer
	Dimensions/co2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das CO2 Bricklet Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`CO2 Bricklet 2.0 <co2_v2_bricklet>`
 empfohlen.


Features
--------

* Misst CO2 Konzentration von 0 bis 10000ppm (Teile pro Million)
* Hohe Genauigkeit von ±30ppm (gesamter Messbereich) und ±3% (Messwert)


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

Dieses Bricklet kann z.B. für automatische Lüftungssteuerung und
Umweltdatenmessung genutzt werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            SenseAir K30
Stromverbrauch                    | 200mW (40mA bei 5V, Idle)
                                  | 1750mW (350mA bei 5V, Messend)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0ppm bis 10000ppm
Genauigkeit                       ±30ppm (gesamter Messbereich), ±3% (Messwert)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (W x D x H)           60 x 65 x 15mm (2,36 x 2,56 x 0,59")
Gewicht                           29g
================================  ============================================================


Ressourcen
----------

* SenseAir K30 Datenblatt (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/datasheets/K30_Datasheet.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/hardware/co2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/co2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/co2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2E2cT4z>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/co2/co2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/co2/co2.FCStd>`__)


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
