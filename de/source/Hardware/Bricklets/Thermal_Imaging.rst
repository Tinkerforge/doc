:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Thermal Imaging Bricklet
:shoplink: ../../../shop/bricklets/thermal-imaging-bricklet.html

.. include:: Thermal_Imaging.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermal_imaging_bricklet:

Thermal Imaging Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermal_imaging_tilted_[?|?].jpg           Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_horizontal_[?|?].jpg       Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_lepton_[?|?].jpg           Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_brickv_[100|].jpg          Thermal Imaging Bricklet im Brick Viewer
	Dimensions/thermal_imaging_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 80x60 Pixel Wärmebildkamera
* Messbereich -10°C bis 450°C
* Nutzt FLIR Lepton **mit Radiometry und Shutter**
* High Contrast Bild mit 8,6Hz und 8 Bit Auflösung (zum darstellen)
* Temperatur Bild mit 4,5Hz und 16 Bit Auflösung (für wissenschaftliche Berechnungen)
* Definierbares Spotmeter mit Min-, Max-, Durchschnitts-Temperaturberechnung
* Automatische Shutter-Steuerung


.. _thermal_imaging_bricklet_description:

Beschreibung
------------

Das Thermal Imaging :ref:`Bricklet <primer_bricklets>` ist mit einer
60x80 Pixel `Wärmebildkamera <https://de.wikipedia.org/wiki/W%C3%A4rmebildkamera>`__
ausgestattet. Das Bricklet kann mit :ref:`Bricks <primer_bricks>` verbunden werden.

Das Bricklet nutzt einen FLIR Lepton Sensor mit Radiometrie und Shutter. Der Sensor
kann Temperaturen zwischen -10°C bis zu 450°C mit einer Auflösung von 80x60 Pixel
messen.

Ein Spotmeter kann definiert werden um Minimum-, Durchschnitts und Maximaltemperatur
für eine definierte Region im Bild zu messen.

Das Bricklet unterstützt zwei Modi: High Contrast Image und Temperature Image.

Im High Contrast Image Modus streamt das Bricklet Bilddaten mit 8,6Hz und 8 Bit
Auflösung. Die Bilddaten sind Grauwerte, der hohe Dynamikbereich des Sensors
ist zusammengefasst um zur Anzeige geeignet zu sein. Dieser Modus wird von
Wärmebildkameras, die auf dem Markt verfügbar sind, genutzt. Üblicherweise werden
die Grauwerte mittels einer Lookuptable auf Falschfarben abgebildet.

Im Termperature Image Modus streamt das Bricklet Daten mit 4,5Hz und 16 Bit
Auflösung. In den Bilddaten stellt jeder 16 Bit Wert eine Temperatur zwischen
-10°C und 450°C mit einer Auflösung von 0,1°C oder einen Wert -10°C und 140°C
mit einer Auflösung von 0,01°C (abhängig von der Auflösungs-Konfiguration).
Dieser Modus kann für wissenschaftliche Berechnungen und der Analyse von
Temperaturänderungen genutzt werden.

Der Shutter wird vom Bricklet automatisch gesteuert.

Das Thermal Imaging Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_thermal_imaging_short_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_thermal_imaging_short_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_thermal_imaging_short_video.webm" type="video/webm">
	</video>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    546mW (109,2mA bei 5V, laufend)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         80x60
Bildrate (Frame Rate)             8,6Hz (High Contrast Image); 4,5Hz (Temperature Image)
Blickfeld (Field of View)         51° Horizontal, 66° Diagonal
Tiefenschärfe                     10cm bis unendlich
Thermale Sensitivität             < 50mK (0,05°C)
Radiometrische Genauigkeit        ±5°C or 5% (typisch)
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
* 3D Modell (`Online ansehen <http://autode.sk/2BUaYhK>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/thermal_imaging/thermal-imaging.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/thermal_imaging/thermal-imaging.FCStd>`__)


.. _thermal_imaging_bricklet_demo_video:

Demo Video
----------

Im folgenden Video ist ein Thermal Imaging Bricklet im Einsatz zu sehen.
Wir filmen eine Küchenspühle mit einer warmen Tasse Kaffee. Dann stellen
wir warmes wasser an und danach auf kalt und wieder zurück.

Man kann sehen das anfangs der die warme Tasse Kaffe das wärmste Objekt
im Bildausschnitt ist. Nach dem wir das warme Wasser aufdrehen wird dieses
langsam wärmer als die Tasse. Wenn wir dann den Wasserhahn wieder auf kalt
stellen wird es wieder kälter etc.

Zusätzlich kann man in der Küchenspühle einen Vortex sehen, der sich
durch das wechseln von warm und kalt im Wasser bildet.

Das Wärmebild im Video wurde aus den :ref:`High Contrast <thermal_imaging_bricklet_high_contrast_vs_temperature>`
Daten des Thermal Imaging Bricklet erstellt.

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/xb44krsgmaM" frameborder="0" allowfullscreen></iframe>

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


.. _thermal_imaging_bricklet_high_contrast_vs_temperature:

High Contrast Image vs Temperature Image
----------------------------------------

Das Thermal Imaging Bricklet unterstützt zwei Bildstream Modis mit verschiedenen
Anwendungsmöglichkeiten.

**High Contrast Image**:

Im High Contrast Image Modus stellt das Bricklet ein 60x80 Pixel Bild mit einer
Bildrate von 8.6Hz. Jedes Pixel ist eine Grauwert-Darstellung und hat eine
Auflösung von 8-Bit.

Dieser Modus wird von FLIR basierten Wärmebildkameras genutzt, die auf dem Markt
verfügbar sind. Die Daten können für Visualisierungen genutzt werden oder direkt
auf ein Display dargestellt werden.

Für den High Contrast Image Modus wird der hohe Dynamikumfang des Sensors 
zusammengefasst mit einer Histogramm-basierten nichtlinearen Abbildungsfunktion.
Diese Filterung ist notwendig für Visualisierungen. Wären die Daten ungefiltert, 
so könnten diese nicht für Visualisierungen genutzt werden. Mit einem 
Temperaturbereich von -10°C bis 450°C wären typische Temperaturänderungen im
Bild von 20°C-30°C nicht sichtbar.

Die 8-Bit Daten jedes Pixels enthält dafür aber keine Temperaturinformationen mehr.
Dafür gibt es aber die Möglichkeit, auch im High Contrast Image Modus, das Spotmeter
zu nutzen.

Für das Spotmeter kann eine Region innerhalb der 60x80 Pixel Matrix definiert werden.
In dieser Region wird die Minimum-, Maximum- und die Durchschnitttemperatur für 
jedes Bild berechnet. Es ist auch möglich die Spotmeter-Region als nur ein Pixel
zu definieren um genau für dieses Pixel die Temperatur zu erhalten.

In diesem Modus können verschiedene Parameter konfiguriert werden:


* **Dampening Factor**: Dieser Parameter stellt die Stärke der zeitlichen Dämpfung dar,
  die auf der HEQ (history equalization) Transformationsfunktion angewendet wird.
  Ein IIR-Filter der Form (N/256) * transformation_zuvor + ((256-N)/256) * transformation_aktuell
  wird dort angewendet. Der HEQ Dämpfungsfaktor stellt dabei den Wert N in der Gleichung dar.
  Der Faktor stellt also ein, wie stark der Einfluss der vorherigen HEQ Transformation
  auf die aktuelle ist. Umso niedriger der Wert von N um so größer ist der Einfluss des
  aktuellen Bildes. Umso größer der Wert von N umso kleiner ist der Einfluss der vorherigen
  Dämpfungs-Transferfunktion.

* **Clip Limit Low**: Dieser Parameter definiert einen künstliche Menge,
  die jeder nicht leeren Histogrammklasse hinzugefügt wird. Wenn *Clip Limit Low* mit L dargestellt
  wird, so erhält jede Klasse mit der aktuellen Menge X die effektive Menge L + X. Jede Klasse, die
  nahe einer gefüllten Klasse ist erhält die Menge L. Der Effekt von höheren Werten ist eine stärkere
  lineare Transferfunktion bereitzustellen. Niedrigere Werte führen zu einer nichtlinearen
  Transferfunktion.

* **Clip Limit High**: Dieser Parameter definiert die maximale Anzahl
  von Pixeln, die sich in jeder Histogrammklasse sammeln dürfen. Jedes weitere Pixel wird verworfen.
  Der Effekt dieses Parameters ist den Einfluss von stark gefüllten Klassen in der HEQ Transformation
  zu beschränken.

* **Empty Counts**: Dieser Parameter spezifiziert die maximale Anzahl von Pixeln in einer Klasse, damit
  die Klasse als leere Klasse interpretiert wird. Jede Histogrammklasse mit dieser Anzahl an Pixeln oder
  weniger wird als leere Klasse behandelt.

Zusätzlich kann eine *Region of Interest* definiert werden. Der Algorithmus, der mit den obigen Parametern
konfiguriert wird, arbeitet dann nur auf dieser Region. Diese Region kann definiert werden um Teile des Bildes
von der Analyse auszuschließen und daher die Daten nicht verzerren kann. Dies ist zum Beispiel interessant,
wenn irgendwo im Bild ein heißer Bereich ausgeschlossen werden soll.

Dieser Modus sollte genutzt werden, wenn Daten visualisiert werden sollen.

**Temperature Image**:

Im Temperature Image Modus stellt das Bricklet ein 60x80 Pixel Bild mit einer Bildrate von 4.5Hz
zur Verfügung. Jeder Pixel in dem Bild ist eine Temperaturmessung mit einer Auflösung von
16-Bit.

Das Thermal Imaging Bricklet hat zwei konfigurierbare Temperaturbereiche für den 
Temperature Image Modus:

* -10°C to 140°C mit einer Auflösung von 0.01°C
* -10°C to 450°C mit einer Auflösung von 0.1°C

Müssen keine Temperaturen über 381°C sollte der erste Messbereich gewählt werden um die
Auflösung zu erhöhen.

Die Daten können für wissenschaftliche Berechnungen oder zur Analyse von 
Temperaturänderungen genutzt werden.

Dieser Modus sollte genutzt werden, wenn mit wirklichen Temperaturdaten gearbeitet
werden soll.


.. _thermal_imaging_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Thermal Imaging Bricklet 
<https://www.tinkerforge.com/de/shop/cases/case-thermal-imaging-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_thermal_imaging_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Thermal Imaging Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_thermal_imaging_case_built_up1_800.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* schraube 12mm Schrauben mit Mutter an Oberteil 
* Baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Oberteil,
* Schraube 10mm Abstandshalter an das Bricklet und,
* schraube Unterteil auf Abstandshalter.

Im Folgenden befindet sich eine Explosionszeichnung des Thermal Imaging Bricklet Gehäuses:

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
