
:shoplink: ../../../shop/bricklets/outdoor-weather-bricklet.html

.. include:: Outdoor_Weather.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _outdoor_weather_bricklet:

Outdoor Weather Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_outdoor_weather_tilted_[?|?].jpg           Outdoor Weather Bricklet
	Bricklets/bricklet_outdoor_weather_top_[?|?].jpg              Outdoor Weather Bricklet
	Bricklets/bricklet_outdoor_weather_front_[?|?].jpg            Outdoor Weather Bricklet
	Cases/bricklet_outdoor_weather_case_built_up_[?|?].jpg        Outdoor Weather Bricklet im Gehäuse
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

Es unterstützt derzeit die `Außen-Wetterstation WS-6147 <https://www.tinkerforge.com/de/shop/outdoor-weather-station-ws-6147.html>`__,
welche folgende Daten misst und sendet

* Temperatur (C°)
* Luftfeuchtigkeit (%RH)
* Windgeschwindigkeit (m/s)
* Windrichtung (16 unterschiedliche Richtungen)
* Niederschlag (mm)

und der `Temperatur/Luftfeuchte Sensor TH-6148 <https://www.tinkerforge.com/de/shop/temperature-humidity-sensor-th-6148.html>`__ misst

* Temperatur (C°)
* Luftfeuchtigkeit (%RH)

Die Außen-Wetterstation WS-6147 ist dafür ausgelegt im Außenbereich genutzt zu werden (sie
sollte so angebracht sein, dass es den Regen/Wind messen kann). Der TH-6148 Sensor wiederum
kann im Innen- sowie im Außenbereich verwendet werden. Es können die Daten von bis zu 
255 Außen-Wetterstationen und bis zu 255 Sensoren gleichzeitig empfangen werden.

Das Outdoor Weather Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_outdoor_weather_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_outdoor_weather_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_outdoor_weather_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    53mW
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Max. Anzahl von WS-6147           255
Max. Anzahl von TH-6148           255
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 35 x 5mm (1,56 x 1,38 x 0,2")
Gewicht*                          10g
================================  ============================================================

\* ohne Antenne

Ressourcen
----------

* Aufbauanleitung WS-6147 (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/datasheets/WS-6147.pdf>`__)
* 433 MHz Empfänger RFM210LCF (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/datasheets/RFM210LCF.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/hardware/outdoor-weather-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/outdoor_weather_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2E2p4U7>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/outdoor_weather/outdoor-weather.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/outdoor_weather/outdoor-weather.FCStd>`__)


.. _outdoor_weather_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können die zuletzt übermittelten Daten 
der Wetterstation sowie der Sensoren angesehen werden. Bei der ersten
Inbetriebnahme kann es ca. 45 Sekunden dauern bis die ersten Daten übertragen
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

Ein `laser-geschnittenes Gehäuse für das Outdoor Weather Bricklet 
<https://www.tinkerforge.com/de/shop/cases/case-outdoor-weather-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_outdoor_weather_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Outdoor Weather Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_outdoor_weather_case_built_up_1000.jpg

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
