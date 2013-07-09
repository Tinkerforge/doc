
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricklets">Bricklets</a> / Distance IR Bricklet
:shoplink: ../../../shop/bricklets/distance-ir-bricklet.html

.. include:: Distance_IR.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_ir_bricklet:

Distance IR Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_distance_ir_tilted_350.jpg",
	               "Bricklets/bricklet_distance_ir_tilted_600.jpg",
	               "Distance IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_ir_front_100.jpg",
	             "Bricklets/bricklet_distance_ir_front_600.jpg",
	             "Distance IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_ir_back_100.jpg",
	             "Bricklets/bricklet_distance_ir_back_600.jpg",
	             "Distance IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_ir_master_100.jpg",
	             "Bricklets/bricklet_distance_ir_master_600.jpg",
	             "Distance IR Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_ir_sensors_100.jpg",
	             "Bricklets/bricklet_distance_ir_sensors_600.jpg",
	             "Distance IR Bricklet Sensoren")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_ir_brickv_100.jpg",
	             "Bricklets/bricklet_distance_ir_brickv.jpg",
	             "Distance IR Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dist_ir_bricklet_dimensions_100.png",
	             "Dimensions/dist_ir_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Entfernungen bis zu 150cm mit IR Licht
* Sensor kann ausgetauscht werden
* Ausgabe in 1mm Schritten (12Bit Auflösung)


Beschreibung
------------

Mit dem Distance IR :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` Entfernungen messen.
Dieses Bricklet wird auf der Rückseite von analogen
`Sharp <http://www.sharpsma.com>`__ Infrarot Entfernungssensoren befestigt.
Nachdem der verbundene Sensor konfiguriert wurde, können die gemessenen
Entfernungen direkt in Millimeter ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf veränderte Distanzmessung zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Typischerweise werden diese Sensoren in der Robotik genutzt um Entfernungen
zu messen, zur Lokalisierung oder zur Kartenerstellung. Sie sind aber noch
für viele andere Anwendungen genutzt werden. Zum Beispiel können diese Sensoren
wie eine Lichtschranke benutzt werden um zum Beispiel den Zugang zu einem
Raum zu kontrollieren.


Technische Spezifikation
------------------------

================================  ===========================================================================
Eigenschaft                       Wert
================================  ===========================================================================
Sensor                            GP2Y0A41 oder GP2Y0A21 oder GP2Y0A02
Stromverbrauch                    Siehe Datenblatt des Sensors
--------------------------------  ---------------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------------
Entfernungen                      Abhängig vom angeschlossenen `Sharp <http://www.sharpsma.com>`__ IR Sensor:

                                  * GP2Y0A41:  4cm -  30cm (1,57" - 11,81")
                                  * GP2Y0A21: 10cm -  80cm (3,94" - 31,50")
                                  * GP2Y0A02: 20cm - 150cm (7,87" - 59,06")

                                  in 1mm Schritten, 12Bit Auflösung
--------------------------------  ---------------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------------
Abmessungen (B x T x H)           45 x 13 x 5mm (1,76 x 0,51 x 0,19")*, passt auf Rückseite des Sensors
Gewicht                           2g*
================================  ===========================================================================

\* ohne Kabel und Sensor


Ressourcen
----------

* GP2Y0A41 Datenblatt (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A41.pdf>`__)
* GP2Y0A21 Datenblatt (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A21.pdf>`__)
* GP2Y0A02 Datenblatt (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/datasheets/GP2Y0A02.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/hardware/distir-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dist_ir_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/distance-ir-bricklet/zipball/master>`__)


.. _distance_ir_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_distance_ir_master_600.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet mit IR Sensor verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessen Distanz und die
Ausgangsspannung des Sensors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Distanz wieder.
Das folgende Bild entstand durch langsames auf den Sensor zu und wieder
wegbewegen einer Hand.

.. image:: /Images/Bricklets/bricklet_distance_ir_brickv.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_brickv.jpg

|test_pi_ref|


.. _distance_ir_sensor_configuration:

Infrarot Sensor konfigurieren
-----------------------------

Die unterstützten Infrarot Sensors geben eine Spannung entsprechend der
gemessenen Distanz aus. Diese Spannung wird vom ADC des angeschlossenen Bricks
gemessen. Um aus der Spannung die Distanz zu errechnen wird eine Abbildung von
Spannung auf Distanz benötigt. Diese Abbildung ist spezifisch für den jeweiligen
Sensortyp und wird auf dem Bricklet gespeichert. Um Sensoren verwenden zu können,
die nicht direkt von uns unterstützt werden muss zuerst eine passenden Abbildung
von Spannung auf Distanz definiert werden.


Spannung/Distanz Abbildung speichern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um die Spannung/Distanz Abbildung auf dem Bricklet zu speichern muss es über
einen Brick an einen PC angeschlossen werden auf dem der :ref:`Brick Daemon
<brickd>` und der :ref:`Brick Viewer <brickv>` laufen.

Wähle den "Distance IR Bricklet" Tab aus, klicke auf den "File.." Knopf und
wähle die passende Spannung/Distanz Abbildungsdatei aus. Dann klicke auf den
"Save" Knopf um die Abbildung auf dem Bricklet zu speichern. Dabei wird aus
den Stützwerten der Abbildungsdatei eine Spline interpoliert um äquidistante
Stützwerte für den gesamten Messbereich des Infrarot Sensors zu erhalten.

Damit die neue Abbildung verwendet wird muss der Brick per Reset Knopf oder per
USB ab- und anstecken neu gestartet werden.


Spannung/Distanz Abbildung
^^^^^^^^^^^^^^^^^^^^^^^^^^

Wir haben vorgefertigte Spannung/Distanz Abbildungsdateien für die folgenden
Sensoren:

.. csv-table::
   :header: "Typ", "Bereich", "Abbildungsdatei"
   :widths: 15, 25, 10

   "GP2D120*", "4cm - 30cm (1,57"" - 11,81"")",   "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2D120.txt>`__"
   "GP2Y0A41", "4cm - 30cm (1,57"" - 11,81"")",   "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A41.txt>`__"
   "GP2Y0A21", "10cm - 80cm (3,94"" - 31,50"")",  "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A21.txt>`__"
   "GP2Y0A02", "20cm - 150cm (7,87"" - 59,06"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A02.txt>`__"

\* wird nicht mehr verkauft, durch GP2Y0A41 ersetzt

Es können eigenen Spannung/Distanz Abbildungen erstellen werden um Sensoren zu
verwenden die im Moment noch nicht offiziell unterstützt werden. Es können auch
die bestehenden Abbildungen auf einen einzelnen Sensor genauer angepasst werden,
um die Genauigkeit der Distanzmessung für diesen einen Sensor zu verbessern. Die
vorgefertigte Spannung/Distanz Abbildungsdateien enthalten über mehrere Sensoren
gemittelte Werte.

Eine Spannung/Distanz Abbildungsdatei kann Kommentare beinhalten (Zeilen die
mit ``#`` beginnen) und beinhaltet Zeilen die jeweils ein
``<Distanz in cm>: <Analogwert in mV>`` Paar enthalten. Die bestehenden
Abbildungsdateien diesen als Beispiel für ein besseres Verständnis.


.. _distance_ir_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Distance IR Bricklet <https://www.tinkerforge.com/de/shop/cases/case-distance-ir-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_distance_ir_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Distance IR Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_distance_ir_case_1000.jpg

.. include:: Distance_IR.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/distance_ir_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Distance IR Bricklet
   :align: center
   :target: ../../_images/Exploded/distance_ir_exploded.png

|bricklet_case_hint|

.. _distance_ir_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Distance_IR_hlpi.table


FAQ
---

Die Distanzen passen nicht
^^^^^^^^^^^^^^^^^^^^^^^^^^

Dies kann verschiedenen Ursachen haben. Die Sharp IR Sensoren benötigen 5V
Versorgungsspannung. Wird der verbundene Brick über USB versorgt, so kann es
sein, dass 5V nicht erreicht werden können. Der Grund für diesen Spannungsabfall
um 0,5V sind Schutzdioden auf den Bricks. Der Stapel kann mit einer
zusätzlichen Stromversorgung, wie der :ref:`Step-Down Power Supply
<step_down_power_supply>`, erweitert werden um den Sensor besser mit 5V
zu versorgen und so eine bessere Distanzmessung zu erhalten.

Eine andere mögliche Ursache kann ein Kalibrierungsproblem sein. Als erstes sollte
sichergestellt werden, dass die richtige Spannung/Distanz Abbildungsdatei für
den angeschlossenen Sensor auf dem Bricklet gespeichert ist (siehe
:ref:`hier <distance_ir_sensor_configuration>`). Dann sollte noch die
Kalibrierung des Analog-Digital-Wandlers des verwendeten Bricks überprüft werden
(siehe :ref:`hier <brickv_adc_calibration>`).

Falls die Distanzmessung immer noch nicht genau genug ist, bleibt nur noch
eine speziell auf den einzelnen Sensor angepasste Spannung/Distanz
Abbildungsdatei zu erstellen. Die vorgefertigte Spannung/Distanz
Abbildungsdateien enthalten über mehrere Sensoren gemittelte Werte, damit sie
für alle Sensoren einer Serie funktionieren.
