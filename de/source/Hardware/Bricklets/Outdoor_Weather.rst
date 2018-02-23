
:DISABLED_shoplink: ../../../shop/bricklets/outdoor-weather-bricklet.html

.. include:: Outdoor_Weather.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _outdoor_weather_bricklet:

Outdoor Weather Bricklet
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_outdoor_weather_tilted_[?|?].jpg           Outdoor Weather Bricklet
	Bricklets/bricklet_outdoor_weather_top_[?|?].jpg              Outdoor Weather Bricklet
	Bricklets/bricklet_outdoor_weather_front_[?|?].jpg            Outdoor Weather Bricklet mit Master Brick
	Bricklets/bricklet_outdoor_weather_brickv_[100|].jpg          Outdoor Weather Bricklet im Brick Viewer
	Dimensions/outdoor_weather_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Empfängt Daten von der Outdoor Wetterstation und Indoor Sensoren
* Misst Temperatur, Luftfeuchtigkeit, Windgeschwindigkeit, Windrichtung und Niederschlag
* Kann von bis zu 255 Wetterstationen gleichzeitig Daten empfangen


.. _outdoor_weather_bricklet_description:

Beschreibung
------------

Das Outdoor Weather :ref:`Bricklet <primer_bricklets>` ist mit einem
433MHz Empfänger ausgestattet und ist damit fähig die Daten von der
Außen-Wetterstation zu empfangen. Das Bricklet kann mit einem
:ref:`Brick <primer_bricks>` verbunden werden.

Es unterstützt derzeit die `Outdoor Weather Station XXX <TBD>`__ welche folgende Daten misst und sendet

* Temperatur (C°)
* Luftfeuchtigkeit (%RH)
* Windgeschwindigkeit (m/s)
* Windrichtung (16 unterschiedliche Richtungen)
* Niederschlag (mm)

und der `Sensor YYY <TBD>`__ misst

* Temperatur (C°)
* Luftfeuchtigkeit (%RH)

Die Wetterstation ist dafür ausgelgt im Außenbereich genutzt zu werden (Es
sollte so angebracht sein, dass es den Regen/Wind messen kann). Der Sensor wiederum
kann im Innen- sowie im Außenbereich verwendet werden. Man besitzt die Möglichkeit 
Daten von bis zu 255 Wetterstationen und zusätzlich von über 255 Sensoren zu empfangen.

Das Outdoor Weather Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
E TBD                             W TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 35 x 5mm (1.56 x 1.38 x 0.2")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* Aufbauanleitung WS-6147 (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/datasheets/WS-6147.pdf>`__)
* 433 MHz Empfänger RFM210LCF (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/datasheets/RFM210LCF.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/hardware/outdoor-weather-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/outdoor_weather_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2E2p4U7>`__ | Download: `STEP <http://download.tinkerforge.com/3d/outdoor-weather/outdoor_weather_bricklet.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/outdoor-weather/outdoor_weather_bricklet.FCStd>`__)


.. _outdoor_weather_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können die zuletzt übermittelten Daten 
der Wetterstation sowie der Sensoren angesehen werden. Bei der ersten
Inbetriebnahme kann es bis zu 45 Sekunden dauern bis die ersten Daten übertragen
und auf dem Monitor zu sehen sind.

.. image:: /Images/Bricklets/bricklet_outdoor_weather_brickv.jpg
   :scale: 100 %
   :alt: Outdoor Weather Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_outdoor_weather_brickv.jpg

|test_pi_ref|


.. _outdoor_weather_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Outdoor Weather Bricklet 
	<https://www.tinkerforge.com/de/shop/cases/case-outdoor-weather-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_outdoor_weather_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Outdoor Weather Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_outdoor_weather_case_1000.jpg

	.. include:: Outdoor_Weather.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/outdoor_weather_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Outdoor Weather Bricklet
	   :align: center
	   :target: ../../_images/Exploded/outdoor_weather_exploded.png

	|bricklet_case_hint|


.. _outdoor_weather_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Outdoor_Weather_hlpi.table
