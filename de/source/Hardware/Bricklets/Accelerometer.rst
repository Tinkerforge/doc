
.. include:: Accelerometer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _accelerometer_bricklet:

Accelerometer Bricklet
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_accelerometer_tilted_[?|?].jpg           Accelerometer Bricklet
	Bricklets/bricklet_accelerometer_horizontal_[?|?].jpg       Accelerometer Bricklet
	Cases/bricklet_accelerometer_case_built_up_[?|?].jpg        Accelerometer Bricklet im Gehäuse
	Bricklets/bricklet_accelerometer_brickv_[100|].jpg          Accelerometer Bricklet im Brick Viewer
	Dimensions/accelerometer_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Accelerometer Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`Accelerometer Bricklet 2.0 <accelerometer_v2_bricklet>`
 empfohlen.


Features
--------

* 3-Achsen Accelerometer
* 0,001g Schritte mit 16Bit Auflösung
* Messbereich bis zu ±16g
* Volle 1kHz Datenrate mit Callbacks


.. _accelerometer_bricklet_description:

Beschreibung
------------

Mit dem Accelerometer :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Beschleunigung entlang der X- Y- und Z-Achse
messen. Die gemessene Beschleunigung kann in `g
<https://de.wikipedia.org/wiki/G-Kraft>`__ ausgelesen werden. Mit
konfigurierbaren Events ist es möglich auf Beschleunigungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Auf dem Bricklet befindet sich eine LED die mittels API ein- und ausgeschaltet
werden kann, um z.B. anzuzeigen, dass eine bestimmte Beschleunigung erreicht
wurde.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            LIS3DSH
Stromverbrauch                    5mW (1mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beschleunigung                    0,001g Schritte, 16Bit Auflösung
Stoßfestigkeit                    10000g
Messbereich                       ±2g / ±4g / ±6g / ±8g / ±16g per API einstellbar
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0,98 x 0,79 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* LIS3DSH Datenblatt (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/datasheets/LIS3DSH.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/hardware/accelerometer-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/accelerometer_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2kpdWE3>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/accelerometer/accelerometer.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/accelerometer/accelerometer.FCStd>`__)


.. _accelerometer_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die Beschleunigung in g
angezeigt. Der Graph gibt den zeitlichen Verlauf der Beschleunigung wieder.

Lasse das Bricklet mit allen drei Achsen nacheinander nach unten zeigen. Die
angezeigte Beschleunigung sollte ca. 1g für die nach unten zeigende Achse
betragen. Die Beschleunigung für die anderen Achsen sollte nahe 0g sein.

.. image:: /Images/Bricklets/bricklet_accelerometer_brickv.jpg
   :scale: 100 %
   :alt: Accelerometer Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_accelerometer_brickv.jpg

|test_pi_ref|


.. _accelerometer_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Accelerometer Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-accelerometer-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_accelerometer_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Accelerometer Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_accelerometer_case_built_up_1000.jpg

.. include:: Accelerometer.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/accelerometer_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Accelerometer Bricklet
   :align: center
   :target: ../../_images/Exploded/accelerometer_exploded.png

|bricklet_case_hint|


.. _accelerometer_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Accelerometer_hlpi.table
