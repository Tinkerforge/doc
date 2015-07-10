
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / IMU Brick
:shoplink: ../../../shop/bricks/imu-brick.html

.. include:: IMU_Brick.substitutions


.. _imu_brick:

IMU Brick
=========

.. raw:: html

    {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
    {{
        tfdocstart("Bricks/brick_imu_tilted_front_350.jpg",
                   "Bricks/brick_imu_tilted_front_600.jpg",
                   "IMU Brick")
    }}
    {{
        tfdocimg("Bricks/brick_imu_tilted_back_100.jpg",
                 "Bricks/brick_imu_tilted_back_600.jpg",
                 "IMU Brick")
    }}
    {{
        tfdocimg("Bricks/brick_imu_caption_100.jpg",
                 "Bricks/brick_imu_caption_600.jpg",
                 "IMU Brick mit Beschriftung")
    }}
    {{
        tfdocimg("Bricks/brick_imu_top_100.jpg",
                 "Bricks/brick_imu_top_600.jpg",
                 "IMU Brick Oberseite")
    }}
    {{
        tfdocimg("Bricks/brick_imu_bottom_100.jpg",
                 "Bricks/brick_imu_bottom_600.jpg",
                 "IMU Brick Unterseite")
    }}
    {{
        tfdocimg("Dimensions/imu_brick_dimensions_100.png",
                 "Dimensions/imu_brick_dimensions_600.png",
                 "Umriss und Bohrplan")
    }}
    {{ tfdocend() }}


Features
--------

* Voll ausgestattete IMU/AHRS mit 9 Freiheitsgraden (je 3-Achsen
  Beschleunigungssensor, Kompass, Gyroskop)
* Keine akkumulierenden Fehler, kein Gimbal Lock!
* Werkskalibriert, einfach anwendungsspezifisch zu kalibrieren
* Berechnet Quaternionen sowie Roll-, Nick- (Pitch) und Gier- (Yaw) Winkel
* Direkt auslesbar per USB, erweiterbar über zwei Bricklet Anschlüsse


.. _imu_brick_description:

Beschreibung
------------

Der IMU :ref:`Brick <primer_bricks>` ist mit je einem 3-Achsen
Beschleunigungssensor, Magnetfeldsensor (Kompass) und Gyroskop ausgestattet und
arbeitet als **USB** 
`Inertialsensor <http://de.wikipedia.org/wiki/Inertialsensor>`__.
Dieser kann 9 Freiheitsgrade messen und berechnet
`Quaternionen <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
sowie auch `Roll-, Nick- und Gier-Winkel
<http://de.wikipedia.org/wiki/Roll-Pitch-Yaw-Winkel>`__. Es ist ein vollständiges
`Attitude and Heading Reference System <http://de.wikipedia.org/wiki/Attitude_Heading_Reference_System>`__.

Die API, verfügbar für 
:ref:`viele Programmiersprachen <imu_brick_programming_interface>`, erlaubt den 
Zugriff auf die berechneten Daten sowie auf die Beschleunigung, Magnetfeld und 
Winkelgeschwindigkeiten für die drei Achsen. Wenn die Quaternionen-Darstellung 
benutzt wird, ist der IMU Brick 
`Gimbal Lock <http://de.wikipedia.org/wiki/Gimbal_Lock>`__ frei (im Gegensatz 
zur Euler-Winkel Darstellung).

Über zwei Anschlüsse können :ref:`Bricklets <primer_bricklets>` 
angeschlossen werden, die die Fähigkeiten des Bricks erweitern. Als Beispiel 
kann ein :ref:`GPS Bricklet <gps_bricklet>` angeschlossen werden um 
Positionsdaten zu ermitteln. Ein 
`Youtube Video <http://www.youtube.com/watch?v=TaqtzG7lyp0>`__ zeigt, wie der
Brick zusammen mit einem :ref:`Barometer Bricklet <barometer_bricklet>` genutzt
werden kann um die Höhe zu bestimmen.

Der IMU Brick kann aber auch mit anderen Bricks in einem 
:ref:`Stapel <primer_stack>` genutzt werden.
Zum Beispiel kann ein zusätzlicher :ref:`Master Brick <master_brick>` mit
:ref:`Master Extensions <primer_master_extensions>` genutzt werden,
um die USB Verbindung durch andere kabelgebundene Schnittstellen 
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
oder drahtlose Schnittstellen (:ref:`WLAN <wifi_extension>`) zu ersetzen.


Technische Spezifikation
------------------------

==============================================================  ============================================================
Eigenschaft                                                     Wert
==============================================================  ============================================================
Beschleunigungs-, Magnetfeld-, Winkelgeschwindigkeitsauflösung  12Bit, 16Bit, 16Bit
Auflösung der Roll-, Nick- (Pitch), Gier- (Yaw) Winkel          0,01° Schritte
Quaternionenauflösung                                           32Bit
Abtastrate                                                      500Hz
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse                                             2
Abmessungen (B x T x H)                                         40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                                                         12g
Stromverbrauch                                                  53mA
==============================================================  ============================================================


Ressourcen
----------

* LSM303 (3-Achsen Beschleunigungssensor/Kompass) Datenblatt (`Download <https://github.com/Tinkerforge/imu-brick/raw/master/datasheets/LSM303.pdf>`__)
* ITG-3200 (3-Achsen Gyroskop) Datenblatt (`Download <https://github.com/Tinkerforge/imu-brick/raw/master/datasheets/ITG3200.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/imu-brick/raw/master/hardware/imu-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/imu_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/imu-brick/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
IMU Bricks.

.. image:: /Images/Bricks/brick_imu_caption_600.jpg
   :scale: 100 %
   :alt: IMU Brick mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_imu_caption_800.jpg


.. _imu_brick_test:

Erster Test
-----------

|test_intro|

|test_tab|

.. image:: /Images/Bricks/imu_brickv.jpg
   :scale: 60 %
   :alt: IMU Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/imu_brickv.jpg

Alle verfügbaren Daten des IMU Bricks werden angezeigt. Wenn der IMU Brick
wie dargestellt gehalten und dann der "Save Orientation" Knopf geklickt wird sollten
die Bewegungen des IMU Bricks entsprechend im Brick Viewer widergespiegelt
werden. Bevor allerdings der "Save Orientation" Knopf geklickt sollte der
Brick 15 Sekunden ruhig gehalten werden, damit die Lageberechnung zur richtigen
Position konvergieren kann.

|test_pi_ref|


Kalibrierung
------------

Der IMU Brick wird fertig kalibriert ausgeliefert und sollte daher direkt nach
dem Auspacken funktionieren. Falls es nötig sein sollte ist eine Neukalibrierung
leicht zu bewerkstelligen.

Die Werkskalibrierung wurde in einem Raum ohne signifikante magnetische
Störfelder durchgeführt. Wenn der IMU Brick in der nähe eines magnetische Feldes
(z.B. das eines Motors) betrieben werden soll, dann sollte das Magnetometer in
der Position, in der der IMU Brick später verwendet werden soll, neu kalibriert
werden!

Um das Magnetometer neu zu kalibrieren muss das Kalibrierungsfenster über den
"Calibrate" Knopf auf dem "IMU Brick" Tab im Brick Viewer aufgerufen werden. Wähle dann
denn "Magnetometer" Tab aus und klicke "Start Calibration". Bewege nun den IMU
Brick bis sich die angezeigten Gain und Bias Werte nicht mehr ändern. Sobald dies
der Fall ist kann der "Ready" Knopf geklickt werden und die Kalibrierung des
Magnetometers ist abgeschlossen.

Beschleunigungssensor und Gyroskop werden ähnlich kalibriert, folge dazu den
Anweisungen im Kalibrierungsfenster. Wir empfehlen zuerst die bestehende
Kalibrierung zu exportieren, bevor der Beschleunigungssensor und das Gyroskop
neu kalibriert werden, sodass im Notfall die alten Kalibrierung wieder
eingespielt werden kann.

Wir empfehlen den Gyroskop Gain nicht neu zu kalibrieren, da dies ohne
geeignete externe Maschinen nicht möglich ist.

Die Werkskalibrierung für jeden IMU Brick kann hier abgerufen werden::

 http://download.tinkerforge.com/imu_calibration/YOUR_IMU_UID.txt

Dazu muss ``YOUR_IMU_UID`` durch die UID des IMU Bricks ersetzt werden.
Falls ein Sensor verkalibriert ist oder eine neue Firmwareversion geflasht
wurde, dann kann die Werkskalibrierung wieder importiert werden. Dazu muss
das Kalibrierungsfenster über den "Calibrate" Knopf auf dem "IMU Brick" Tab
im Brick Viewer aufgerufen und der "Im/Export" Tab ausgewählt werden. Zum
Abschluss muss der Inhalt der ``YOUR_IMU_UID.txt`` Datei in das Textfeld kopiert
und auf den "Import" Knopf geklickt werden.

Seit Brick Viewer Version 1.1.13 kann auch der "Restore Factory Calibration"
Knopf verwendet werden. Dadurch wird die entsprechende Werkskalibrierung
automatisch heruntergeladen und importiert.

Ein Video, das zeigt wie wir die IMU Bricks kalibieren gibt es auf
`Youtube <http://www.youtube.com/watch?v=JckgemCHvCA>`__.


Quaternionen vs Eulerwinkel
---------------------------

Wir empfehlen
`Quaternion <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
anstatt Eulerwinkel (`Roll-, Nick- und Gier-Winkel
<http://de.wikipedia.org/wiki/Roll-Pitch-Yaw-Winkel>`__) zu verwenden, da die
letzteren einen `Gimbal Lock <http://de.wikipedia.org/wiki/Gimbal_Lock>`__
erleiden können.

Eine Formel um eine Quaternion in eine Rotationsmatrix umzurechnen findet sich
in der API Dokumentation. Beachte, dass Eulerwinkel immer eine definierte
Reihenfolge haben in der sie angewendet werden müssen. Im Falle des IMU Bricks
gilt folgenden Reihenfolge: erst Roll-Winkel, dann Gier-Winkel, zuletzt
Nick-Winkel.


Berechnung unabhängiger Winkel
------------------------------

Es ist nicht möglich Winkel für alle 3 Achsen zu berechnen die vollständig
unabhängig sind. Zumindest an den Gimbal Lock Positionen werden Sprünge von
180° auftreten für gewisse Winkel. Dies ist grundsätzlich nicht anders möglich.

Wenn Rotationswinkel für die X, Y und Z Achse in Abhängigkeit zu einer
definierten Grundposition benötigt werden, dann muss das Quaternion zuerst im
Bezug auf diese Grundposition rotiert werden bevor die Winkel berechnet werden.

Das folgende Python Beispiel tut exakt dies und es sollte einfach zu verstehen
und auf andere Programmiersprachen übertragbar sein. Beachte, dass Gimbal Locks
bei +90° und -90° für jede der Achsen auftreten. Die Grundposition ist (0,0,0):

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from tinkerforge.ip_connection import IPConnection
    from tinkerforge.brick_imu import IMU

    import math
    import time

    class Q:
        HOST = "localhost"
        PORT = 4223
        UID = "9yEBJVEHaem" # Change to your UID

        def __init__(self):
            self.base_x = 0.0
            self.base_y = 0.0
            self.base_z = 0.0
            self.base_w = 0.0

            self.ipcon = IPConnection() # Create IPconnection
            self.imu = IMU(self.UID, self.ipcon) # Create device object
            self.ipcon.connect(self.HOST, self.PORT) # Connect to brickd

            # Wait for IMU to settle
            print 'Set IMU to base position and wait for 10 seconds'
            print 'Base position will be 0 for all angles'
            time.sleep(10)
            q = self.imu.get_quaternion()
            self.set_base_coordinates(q.x, q.y, q.z, q.w)

            # Set period for quaternion callback to 10ms
            self.imu.set_quaternion_period(10)

            # Register quaternion callback
            self.imu.register_callback(self.imu.CALLBACK_QUATERNION, self.quaternion_cb)

        def quaternion_cb(self, x, y, z, w):
            # Use conjugate of quaternion to rotate coordinates according to base system
            x, y, z, w = self.make_relative_coordinates(-x, -y, -z, w)

            x_angle = int(math.atan2( 2.0*(y*z - w*x), 1.0 - 2.0*(x*x + y*y))*180/math.pi)
            y_angle = int(math.atan2(-2.0*(x*z + w*y), 1.0 - 2.0*(x*x + y*y))*180/math.pi)
            z_angle = int(math.atan2(-2.0*(x*y + w*z), 1.0 - 2.0*(x*x + z*z))*180/math.pi)

            print 'x: {0}, y: {1}, z: {2}'.format(x_angle, y_angle, z_angle)

        def set_base_coordinates(self, x, y, z, w):
            self.base_x = x
            self.base_y = y
            self.base_z = z
            self.base_w = w

        def make_relative_coordinates(self, x, y, z, w):
            # Multiply base quaternion with current quaternion
            return (
                w * self.base_x + x * self.base_w + y * self.base_z - z * self.base_y,
                w * self.base_y - x * self.base_z + y * self.base_w + z * self.base_x,
                w * self.base_z + x * self.base_y - y * self.base_x + z * self.base_w,
                w * self.base_w - x * self.base_x - y * self.base_y - z * self.base_z
            )

    if __name__ == "__main__":
        q = Q()

        raw_input('Press key to exit\n') # Use input() in Python 3
        q.ipcon.disconnect()

Paul Balzer von MechLab Engineering hat zusätzlich 
`Code auf GitHub <https://github.com/MechLabEngineering/TinkerforgeAttitude>`__
bereit gestellt der die Quaternionen in das Fahrzeugkoordinatensystem nach
DIN70000 umwandelt. Insbesondere wird dort durchgängig ein
`rechtshändiges Koordinatensystem <http://de.wikipedia.org/wiki/Rechtssystem_(Mathematik)>`__
verwendet. Mehr Informationen dazu gibt es im 
`Blog von MachLab Engineering <http://mechlab-engineering.de/2014/03/tinkerforge-imu-zur-lageerkennung-von-fahrzeugen/>`__.

Funktionsweise
--------------

Auf Basis der Sensordaten die der IMU Brick sammelt (Winkelgeschwindigkeit,
Beschleunigung und Magnetfeld) ist es möglich Sensorfusion zu betreiben, um eine
absolute Orientierung im Raum zu ermitteln.

Häufig wird für diesen Berechnungsprozess ein
`Kalman Filter <http://de.wikipedia.org/wiki/Kalman-Filter>`__ verwendet.
Der IMU Brick verwendet allerdings einen Filter der auf
`diesem Paper <http://www.x-io.co.uk/res/doc/madgwick_internal_report.pdf>`__
von `S. O. Madgwick <http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/>`__
basiert. Unsere Tests haben gezeigt, dass dieser neuartige
Filter signifikant bessere Ergebnisse als ein Kalman Filter erzielt. Madgwick
beschreibt die Arbeitsweise seines Filter so:

 [...] the filter calculates the orientation by numerically integrating the
 estimated orientation rate. It is computed as the rate of change of
 orientation measured by the gyroscopes. The magnitude of the gyroscope
 measurement error is removed in the direction of the estimated error,
 which is computed from accelerometer and magnetometer measurements.

Das folgende Bild zeigt die verschiedenen Schritte des Filters:

.. image:: /Images/Bricks/imu_math_magic.png
   :scale: 100 %
   :alt: Blockdiagramm des Orientierungsfilters von S. O. Madgwick: "An efficient orientation filter for inertial and inertial/magnetic sensor arrays", University of Bristol, April 2010.
   :align: center
   :target: ../../_images/Bricks/imu_math_magic.png

Bild und Erklärung stammen aus S. O. Madgwick: "An efficient orientation filter
for inertial and inertial/magnetic sensor arrays", University of Bristol,
April 2010.


.. _imu_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: IMU_Brick_hlpi.table
