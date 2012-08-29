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
`Sharp <http://www.sharpsma.com>`__ Infrarot Entfernungs-Sensoren befestigt.
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

Teste dein Distance IR Bricklet
-------------------------------

Um das Distance IR Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect an infrared distance sensor to the Bricklet and connect it
to a :ref:`Brick <product_overview_bricks>`.
You should have received a suitable cable with the Bricklet.

.. image:: /Images/Bricklets/bricklet_distance_ir_master_600.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet mit IR Sensor verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Distance IR Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected you can now see the measured distance
of the sensor, the output voltage of the IR distance sensor
and a graph that shows the distance over time.

Click on the Distance IR tab and see if the measured values change
corresponding to the real distance. In the image below we slowly moved a hand
away from the sensor and to the sensor again.

.. image:: /Images/Bricklets/bricklet_distance_ir_brickv.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_brickv.jpg

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <distance_ir_programming_interfaces>` über das
API des Distance IR Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _distance_ir_sensor_configuration:

Configure Infrared Sensor
-------------------------

The supported infrared sensors simply produce an output voltage
based on the measured distance. This voltage is measured by the ADC
of the connected Brick. To compute the corresponding distance to this voltage
a voltage/distance mapping is needed. This mapping is stored on the
Distance IR Bricklet. If you want to use an IR distance sensor not directly
supported by us, you have to calibrate this voltage/distance mapping
yourself.


Store Voltage/Distance Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To write the voltage/distance mapping you have to connect the Bricklet
with a Brick to your PC. Start the :ref:`Brick Daemon <brickd>` and the
:ref:`Brick Viewer <brickv>`.

Press "connect" in the Brick Viewer and you should see the Distance IR tab.
Click on it.

Press the "File.." Button and choose an voltage/distance mapping file.
After this press the "Save" Button to write the data onto the Bricklet,
you will get an graphical representation spline interpolation
that is written.

After this press the reset button on the Brick or power cycle to
load the newly stored voltage/distance mapping.


Voltage/Distance Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^

We provide the voltage/distance mappings for the following sensors:

.. csv-table::
   :header: "Type", "Range", "Mapping File"
   :widths: 15, 25, 10

   "GP2Y0A41 und GP2D120", "4cm - 30cm (1,57"" - 11,81"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2D120.txt>`__"
   "GP2Y0A21", "10cm - 80cm (3,94"" - 31,50"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A21.txt>`__"
   "GP2Y0A02", "20cm - 150cm (7,87"" - 59,06"")", "`Download <https://github.com/Tinkerforge/distance-ir-bricklet/raw/master/software/calibration/2Y0A02.txt>`__"

You can write your own voltage/distance mapping for a sensor we
currently do not offer. Or you can modify an existing mapping file to achieve
a better quality of your sensor.

A voltage/distance mapping file consists of comments (lines beginning with '#')
and lines containing one "cm: analog value" tuple each. Look in the provided
files above to get an idea.


.. _distance_ir_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Distance_IR_hlpi.table


FAQ
---

The distances are wrong
^^^^^^^^^^^^^^^^^^^^^^^

This is likely some kind of calibration problem. First of all you should
check if the calibration for the correct infrared sensor is installed
(see :ref:`here <distance_ir_programming_interfaces>`) and calibrate the ADC of your
Brick (see :ref:`here <brickv_adc_calibration>`).

If the distance measurements are still not precise enough, you have to write
a voltage/distance mapping that is specific for your device. The
voltage/distance mapping files provided by us are averaged over several
sensors.
