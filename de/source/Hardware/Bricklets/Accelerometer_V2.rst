
:shoplink: ../../../shop/bricklets/accelerometer-v2-bricklet.html

.. include:: Accelerometer_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _accelerometer_v2_bricklet:

Accelerometer Bricklet 2.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_accelerometer_v2_tilted_[?|?].jpg           Accelerometer Bricklet 2.0
	Bricklets/bricklet_accelerometer_v2_top_[?|?].jpg              Accelerometer Bricklet 2.0
	Bricklets/bricklet_accelerometer_v2_brickv_[100|].jpg          Accelerometer Bricklet 2.0 im Brick Viewer
	Dimensions/accelerometer_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 3-Achsen Accelerometer
* 0,0001g Schritte mit 16Bit Auflösung
* Messbereich bis zu ±8g
* Datenrate bis zu 25,6kHz

.. _accelerometer_v2_bricklet_description:

Beschreibung
------------

Mit dem Accelerometer :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Beschleunigung entlang der X- Y- und Z-Achse
messen. Die gemessene Beschleunigung kann in `g
<https://de.wikipedia.org/wiki/G-Kraft>`__ ausgelesen werden. Mit
konfigurierbaren Events ist es möglich auf Beschleunigungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Ein ``Continuous Acceleration Callback`` kann genutzt werden um hohe Datenraten
bis zu 25,6kHz zu übertragen. Das Bricklet ist damit gut für Anwendungen im
Bereich Predictive Maintenance geeignet.

Auf dem Bricklet befindet sich eine LED die mittels API ein- und ausgeschaltet
werden kann, um z.B. anzuzeigen, dass eine bestimmte Beschleunigung erreicht
wurde.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            KX122
Stromverbrauch                    30mW (6mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         0,0001g Schritte, 16Bit Auflösung
Stoßfestigkeit                    5000g für 0,5ms / 10000g für 0,2ms
Messbereich                       ±2g / ±4g / ±8g (per API einstellbar)
Datenrate                         0,781Hz - 25,6kHz (per API einstellbar)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0,98 x 0,79 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* KX122 datasheet (`Download <https://github.com/Tinkerforge/accelerometer-v2-bricklet/raw/master/datasheets/KX122.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/accelerometer-v2-bricklet/raw/master/hardware/accelerometer-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/accelerometer_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/accelerometer-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2GdSuyv>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/accelerometer_v2/accelerometer-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/accelerometer_v2/accelerometer-v2.FCStd>`__)


.. _accelerometer_v2_bricklet_test:

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

.. image:: /Images/Bricklets/bricklet_accelerometer_v2_brickv.jpg
   :scale: 100 %
   :alt: Accelerometer Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_accelerometer_v2_brickv.jpg

|test_pi_ref|


.. _accelerometer_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Accelerometer Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-accelerometer-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_accelerometer_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Accelerometer Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_accelerometer_case_built_up_1000.jpg

.. include:: Accelerometer.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/accelerometer_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Accelerometer Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/accelerometer_exploded.png

|bricklet_case_hint|


.. _accelerometer_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Accelerometer_V2_hlpi.table
