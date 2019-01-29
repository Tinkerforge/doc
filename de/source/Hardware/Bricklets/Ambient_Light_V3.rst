
:DISABLED_shoplink: ../../../shop/bricklets/ambient-light-v3-bricklet.html

.. include:: Ambient_Light_V3.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ambient_light_v3_bricklet:

Ambient Light Bricklet 3.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ambient_light_v3_tilted_[?|?].jpg           Ambient Light Bricklet 3.0
	Bricklets/bricklet_ambient_light_v3_top_[?|?].jpg              Ambient Light Bricklet 3.0
	Bricklets/bricklet_ambient_light_v3_brickv_[100|].jpg          Ambient Light Bricklet 3.0 im Brick Viewer
	Dimensions/ambient_light_v3_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Umgebungslicht bis zu 64000Lux
* Voller Dynamikumfang von 0,01Lux bis 64000Lux
* Ausgabe in 0,01Lux Schritten (16Bit effektive Auflösung)


.. _ambient_light_v3_bricklet_description:

Beschreibung
------------

Mit dem Ambient Light :ref:`Bricklet <primer_bricklets>` 3.0 können
:ref:`Bricks <primer_bricks>` die Umgebungshelligkeit messen.
Es ist der Nachfolger des :ref:`ambient_light_bricklet` mit einem etwa 70x
größeren Messbereich.
Die gemessene Helligkeit kann in `Lux <https://de.wikipedia.org/wiki/Lux_(Einheit)>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
Helligkeitsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Bricklet kann genutzt werden um z.B. helligkeitsabhängig Beleuchtungen
oder Motoren zu steuern.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            LTR329ALS
Stromverbrauch                    10mW (2mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beleuchtungsstärke                0Lux - 64000Lux in 0,01Lux Schritten, 16Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* LTR329ALS Datenblatt (`Download <https://github.com/Tinkerforge/ambient-light-v3-bricklet/raw/master/datasheets/LTR329ALS.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ambient-light-v3-bricklet/raw/master/hardware/ambient-light-v3-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ambient_light_v3_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ambient-light-v3-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _ambient_light_v3_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die Beleuchtungsstärke in Lux
angezeigt. Der Graph gibt den zeitlichen Verlauf der Beleuchtungsstärke wieder.

Ein guter Test für den Sensor ist es den Raum abzudunkeln und eine Taschenlampe
langsam über den Sensor hinweg zu bewegen. Der resultierende Graph sollte
ungefähr so aussehen wie auf dem folgenden Screenshot.

.. image:: /Images/Bricklets/bricklet_ambient_light_v3_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet 3.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_v3_brickv.jpg

|test_pi_ref|


.. _ambient_light_v3_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Ambient Light Bricklet 3.0
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Ambient Light Bricklet 3.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Ambient_Light_V3.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Ambient Light Bricklet 3.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _ambient_light_v3_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Ambient_Light_V3_hlpi.table
