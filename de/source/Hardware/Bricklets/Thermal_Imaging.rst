:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Thermal Imaging Bricklet
:FIXME_shoplink: ../../../shop/bricklets/thermal-imaging-bricklet.html

.. include:: Thermal_Imaging.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermal_imaging_bricklet:

Thermal Imaging Bricklet
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermal_imaging_tilted_[?|?].jpg           Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_horizontal_[?|?].jpg       Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_master_[100|600].jpg       Thermal Imaging Bricklet mit Master Brick
	Cases/bricklet_thermal_imaging_case_[100|600].jpg             Thermal Imaging Bricklet im Gehäuse
	Bricklets/bricklet_thermal_imaging_brickv_[100|].jpg          Thermal Imaging Bricklet im Brick Viewer
	Dimensions/thermal_imaging_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 80x60 Pixel Wärmebildkamera
* Messbereich -273°C bis 6279°C
* Nutzt FLIR Lepton **mit Radometry und Shutter**
* High Contrast Bild mit 8.6Hz und 8 Bit Auflösung (zum darstellen)
* Temperatur Bild mit 4.5Hz und 16 Bit Auflösung (für wissenschaftliche Berechnungen)
* Definierbares Spotmeter mit Min-, Max-, Durchschnitts-Temperaturberechnung
* Automatische Shutter-Steuerung


.. _thermal_imaging_bricklet_description:

Beschreibung
------------

Das Thermal Imaging :ref:`Bricklet <primer_bricklets>` ist mit einer
60x80 Pixel `Wärmebildkamera <https://de.wikipedia.org/wiki/W%C3%A4rmebildkamera>`__
ausgestattet. Das Bricklet kann mit :ref:`Bricks <primer_bricks>` verbunden werden.

Das Bricklet nutzt einen FLIR Lepton Sensor mit Radiometrie und Shutter. Der Sensor
kann Temperaturen zwischen -273°C bis zu 6279°C mit einer Auflösung von 80x60 Pixel
messen.

Ein Spotmeter kann definiert werden um Minimum-, Durchschnitts und Maximaltemperatur
für eine definierte Region im Bild zu messen.

Das Bricklet unterstützt zwei Modi: High Contrast Image und Temperature Image.

Im High Contrast Image Modus streamt das Bricklet Bilddaten mit 8.6Hz und 8 Bit
Auflösung. Die Bilddaten sind Grauwerte, der hohe Dynamikbereich des Sensors
ist zusammengefasst um zur Anzeige geeignet zu sein. Dieser Modus wird von
Wärmebildkameras, die auf dem Markt verfügbar sind, genutzt.

Im Termperature Image Modus streamt das Bricklet Daten mit 4.5Hz und 16 Bit
Auflösung. In den Bilddaten stellt jeder 16 Bit Wert eine Temperatur zwischen
-273°C und 6279°C mit einer Auflösung von 0.1°C oder einen Wert -273°C und 381°C 
mit einer Auflösung von 0.01°C (abhängig von der Auflösungs-Konfiguration). 
Dieser Modus kann für wissenschaftliche Berechnungen und der Analyse von
Temperaturänderungen genutzt werden.

Der Shutter wird vom Bricklet automatisch gesteuert.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         60x80
Bildrate (Frame Rate)             High Contrast Image: 8.6Hz
                                  Temperature Image: 4.5Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 9mm (1.57 x 1.57 x 0.35")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/thermal-imaging-bricklet/raw/master/hardware/thermal-imaging-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/thermal_imaging_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/thermal-imaging-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _thermal_imaging_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte nun ein Wärmebild dargestellt werden.

.. image:: /Images/Bricklets/bricklet_thermal_imaging_brickv.jpg
   :scale: 100 %
   :alt: Thermal Imaging Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_thermal_imaging_brickv.jpg

|test_pi_ref|


.. _thermal_imaging_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Thermal Imaging Bricklet 
	<https://www.tinkerforge.com/de/shop/cases/case-thermal-imaging-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_thermal_imaging_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Thermal Imaging Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_thermal_imaging_case_1000.jpg

	.. include:: Thermal_Imaging.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/thermal_imaging_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Thermal Imaging Bricklet
	   :align: center
	   :target: ../../_images/Exploded/thermal_imaging_exploded.png

	|bricklet_case_hint|


.. _thermal_imaging_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Thermal_Imaging_hlpi.table
