
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Accelerometer Bricklet
:FIXME_shoplink: ../../../shop/bricklets/accelerometer-bricklet.html

.. include:: Accelerometer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _accelerometer_bricklet:

Accelerometer Bricklet
======================

.. note::
  Diese Bricklet ist noch in Entwicklung!


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
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beschleunigung                    0,001g Schritte, 16Bit Auflösung
Stoßfestigkeit                    10000g
Messbereich                       ±2g / ±4g / ±6g / ±8g / ±16g per API einstellbar
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0,98 x 0,79 x 0,19")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* LIS3DSH Datenblatt (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/datasheets/LIS3DSH.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/hardware/accelerometer-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/accelerometer_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/zipball/master>`__)


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


.. _accelerometer_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Accelerometer_hlpi.table
