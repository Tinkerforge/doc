
:shoplink: ../../../shop/bricklets/air-quality-bricklet.html

.. include:: Air_Quality.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _air_quality_bricklet:

Air Quality Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_air_quality_tilted_[?|?].jpg           Air Quality Bricklet
	Bricklets/bricklet_air_quality_top_[?|?].jpg              Air Quality Bricklet
	Cases/bricklet_air_quality_case_[100|600].jpg             Air Quality Bricklet im Gehäuse
	Bricklets/bricklet_air_quality_brickv_[100|].jpg          Air Quality Bricklet im Brick Viewer
	Dimensions/air_quality_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst IAQ (Indoor Air Quality = Innenraumluftqualität) Index, Luftdruck, Luftfeuchte und Temperatur
* IAQ Index und Luftfeuchte sind temperaturkompensiert
* Einstellbare Temperaturkompensation für Anwendungsfälle im Gehäuse


.. _air_quality_bricklet_description:

Beschreibung
------------

Das Air Quality :ref:`Bricklet <primer_bricklets>` kann

* IAQ (Indoor Air Quality = Innenraumluftqualität) Index,
* Luftdruck in hPa,
* Luftfeuchte in %RH und
* Temperatur in °C messen.

Der IAQ Index beschreibt die Luftqualität. Um den IAQ Index zu bestimmen
misst das Bricklet Ethan, Isopren (2-Methylbuta-1,3-dien), Ethanol,
Aceton und Kohlenstoffmonoxid (oft auch VOC genannt, Volatile Organic
Components = flüchtige organische Verbindungen) mittels Adsorption. Diese
Gasmessungen werden mit Messungen des Luftdrucks, der Luftfeuchte und der
Temperatur kombiniert um den IAQ Index zu bestimmen.

Der IAQ Index hat einen Wertebereich von 0-500:

.. image:: /Images/Misc/bricklet_air_quality_iaq_index.png
   :scale: 100 %
   :alt: IAQ Index Skala
   :align: center
   :target: ../../_images/Misc/bricklet_air_quality_iaq_index.png

Typische Anwendungen für dieses Bricklet sind die Überwachung der Luftqualität,
Umweltstatistiken, Hausautomatisierung usw.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_air_quality_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_air_quality_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_air_quality_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  =====================================================================
Eigenschaft                       Wert
================================  =====================================================================
Sensor                            BME680
Stromverbrauch                    100mW (20mA bei 5V)
--------------------------------  ---------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------
IAQ Index-Auflösung               1
Luftdruck-Auflösung               0,0018hPa
Luftfeuchte-Auflösung             0,008%RH
Temperatur-Auflösung              0,01°C
--------------------------------  ---------------------------------------------------------------------
IAQ Index-Genauigkeit             ±15 und ±15% des Wertes
Luftdruck-Genauigkeit             ±0,12hPa (700-900hPa bei 25-40°C), ±0,6hPa (gesamter Messbereich)
Luftfeuchte-Genauigkeit           ±3%RH (20-80%RH bei 25°C)
Temperatur-Genauigkeit            ±0,5°C (at 25°C), ±1,0°C (0-65°C)*
--------------------------------  ---------------------------------------------------------------------
Messfrequenz                      0,3 Messungen pro Sekunde
--------------------------------  ---------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0,98 x 0,79 x 0,19")
Gewicht                           2,1g
================================  =====================================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/air-quality-bricklet/raw/master/hardware/air-quality-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/air_quality_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/air-quality-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2NTYEnR>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/air_quality/air-quality.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/air_quality/air-quality.FCStd>`__)


IAQ-Genauigkeit und automatische Kalibrierung
---------------------------------------------

Das Bricklet baut über längere Zeit eine Datenbank an Messwerten auf, um über
eine automatische Hintergrundkalibrierung einen genaueren IAQ Index bestimmen zu
können. Es dauert ein paar Tage bis der IAQ Index eine hohe Genauigkeit erreicht.

Die IAQ-Genauigkeit (IAQ Accuracy) spiegelt den aktuellen Status der
Hintergrundkalibrierung wieder.

* Accuracy 0: Das Bricklet wurde gerade gestartet und der Sensor stabilisiert sich.
* Accuracy 1: Die Historie der Hintergrundkalibrierung ist zweifelhaft. Dies bedeutet typischerweise dass die Daten die der Sensor gemessen hat über einen längern Zeitraum zu stabil waren. Der Kalibrierungs-Algorithmus kann keine klaren Referenzen bilden.
* Accuracy 2: Das Bricklet hat neue Kalibrierungsdaten gefunden und eine Rekalibrierung läuft.
* Accuracy 3: Das Bricklet ist erfolgreich Kalibriert.

Die effektive Dauer der Kalibrierung hängt von den Stimuli ab die der Sensor
beobachtet. Eine IAQ-Genauigkeit die zwischen 2 und 3 hin- und herwandert ist
erwartet. Das Bricklet ist erfolgreich dabei sich zu rekalibrieren.

Das Bricklet speichert die aktuelle Datenbank an Werten und berechneten
Koeffizienten alle 12 Stunden in seinem internen Flash-Speicher. Dadurch dauert
es nach einem Neustart des Bricklet nicht lange bis wieder verlässliche Daten
zur Verfügung stehen.

Seit Firmware-Version 2.0.3 nutzt die automatische Hintergrundkalibrierung Daten 
der letzten 28 Tage. Wir empfehlen daher das Bricklet für 28 vollte Tage laufen zu 
lassen bevor die Werte als vollständig zuverlässig angesehen werden können. Mit der
API kann das Kalibrierungs-Fenster auf 4 Tage verkürzt werden.

.. _air_quality_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird der IAQ Index, der Luftdruck, die
Luftfeuchte und die Temperatur angezeigt. Die Graphen geben den zeitlichen
Verlauf dieser Werte wieder.

.. image:: /Images/Bricklets/bricklet_air_quality_brickv.jpg
   :scale: 100 %
   :alt: Air Quality Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_air_quality_brickv.jpg

|test_pi_ref|


.. _air_quality_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Air Quality Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-air-quality-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_air_quality_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Air Quality Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_air_quality_case_1000.jpg

.. include:: Air_Quality.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/air_quality_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Air Quality Bricklet
   :align: center
   :target: ../../_images/Exploded/air_quality_exploded.png

|bricklet_case_hint|


.. _air_quality_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Air_Quality_hlpi.table
