
:DISABLED_shoplink: ../../../shop/bricklets/temperature-v2-bricklet.html

.. include:: Temperature_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _temperature_v2_bricklet:

Temperature Bricklet 2.0
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_temperature_v2_tilted_[?|?].jpg           Temperature Bricklet 2.0
	Bricklets/bricklet_temperature_v2_horizontal_[?|?].jpg       Temperature Bricklet 2.0
	Bricklets/bricklet_temperature_v2_master_[100|600].jpg       Temperature Bricklet 2.0 mit Master Brick
	Cases/bricklet_temperature_v2_case_[100|600].jpg             Temperature Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_temperature_v2_brickv_[100|].jpg          Temperature Bricklet 2.0 im Brick Viewer
	Dimensions/temperature_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Umgebungstemperatur mit **0,2°C** Genauigkeit
* Temperaturbereich von -40°C bis 125°C
* Ausgabe in 0,01°C Schritten


.. _temperature_v2_bricklet_description:

Beschreibung
------------

Mit dem Temperature :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Temperaturen messen. Die gemessene
Temperatur kann in `°C
<https://de.wikipedia.org/wiki/Grad_Celsius>`__ ausgelesen werden. Zusätzlich
können Events konfiguriert werden die ausgelöst werden wenn eine bestimmte
Temperatur über- oder unterschritten wird.

Das Temperature Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            STS3x
Stromverbrauch                    28mW (5.6mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Umgebungstemperatur               -40°C bis 125°C in 0,01°C Schritten
Genauigkeit                       typisch 0,2°C in Bereich von 0°C bis 65°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5 mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* STS3x Datenblatt (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/datasheets/STS3x.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/temperature-v2-bricklet/raw/master/hardware/temperature-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/temperature_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/temperature-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2v9CCqr>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/temperature_v2/temperature-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/temperature_v2/temperature-v2.FCStd>`__)


.. _temperature_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_temperature_v2_brickv.jpg
   :scale: 100 %
   :alt: Temperature Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_v2_brickv.jpg

Als einfacher Test kann eine Wärmequelle wie z.B. ein Finger auf den Sensor
gelegt werden, die angezeigte Temperatur sollte steigen (oder fallen wenn es
im Raum sehr warm ist).

|test_pi_ref|


.. _temperature_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Temperature Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Temperature Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Temperature_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Temperature Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _temperature_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Temperature_V2_hlpi.table
