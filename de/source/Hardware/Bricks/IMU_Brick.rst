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

* Voll ausgestattetes AHRS mit 9 Freiheitsgraden
* Keine akkumulierenden Fehler, kein Gimbal Lock!
* Vorkalibriert, einfach Anwendungsspezifisch zu kalibrieren
* Berechnet Quaternionen sowie Roll-, Nick- (Pitch) und Gier- (Yaw) Winkel
* Ein USB und zwei Bricklet Anschlüsse


Beschreibung
------------

Der IMU :ref:`Brick <product_overview_bricks>` ist mit einem 32-Bit ARM
Mikrocontroller und einem `Inertialsensor
<http://de.wikipedia.org/wiki/Inertialsensor>`__ ausgestattet.
Dieser kann 9 Freiheitsgrade messen und besteht aus einem 3-Achsen
Beschleunigungssensor, Kompass und Gyroskop. Die Platine berechnet
`Quaternionen <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
sowie auch `Roll-, Nick- und Gier-Winkel
<http://de.wikipedia.org/wiki/Roll-Pitch-Yaw-Winkel>`__.
Die API erlaubt den Zugriff auf die berechneten Daten sowie
Beschleunigung, Magnetfeld und Winkelgeschwindigkeiten für die
drei Achsen. Wenn die Quaternionen-Darstellung benutzt wird, ist der IMU Brick
`Gimbal Lock <http://de.wikipedia.org/wiki/Gimbal_Lock>`__ frei.

Der Brick ist kompatibel zu anderen Tinkerforge
:ref:`Bricks <product_overview_bricks>`
und kann in einem Stapel benutzt werden.
Über zwei Anschlüsse können :ref:`Bricklet <product_overview_bricklets>`
angeschlossen werden.

Über eine **USB** Verbindung kann der Brick von einem PC gesteuert werden.
Über einen zusätzlichen Master Brick mit Master Extension ist es möglich diese
USB Verbindung durch kabelgebundene Schnittstellen (**RS485**, **Ethernet**)
oder drahtlose Schnittstellen (**WLAN**) zu ersetzen
(:ref:`High Level Konzept <pi_hlpi>`).

Da die Firmware Open Source ist, ist es natürlich auch möglich den Brick direkt
zu programmieren (:ref:`On Device Programmierung <pi_odpi>`).
Momentan bieten wir keine On Device API an.


Technische Spezifikation
------------------------

==============================================================  ============================================================
Eigenschaft                                                     Wert
==============================================================  ============================================================
Mikrocontroller                                                 ATSAM3S2B (128kB Flash, 32kB RAM)
Stromverbrauch                                                  53mA
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Beschleunigungs-, Magnetfeld-, Winkelgeschwindigkeitsauflösung  16Bit
Auflösung der Roll-, Nick- (Pitch), Gier- (Yaw) Winkel          16Bit, in 0,01° Schritten
Quaternionenauflösung                                           32Bit
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse                                             2
Abmessungen (B x T x H)                                         40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                                                         12g
==============================================================  ============================================================


Ressourcen
----------

* 3-Achsen Beschleunigungssensor/Kompass LSM303 Datenblatt (`Download <http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00260288.pdf>`__)
* 3-Achsen Gyroskop ITG-3200 Datenblatt (`Download <http://invensense.com/mems/gyro/documents/PS-ITG-3200A.pdf>`__)
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

Teste deinen IMU Brick
----------------------

Um den IMU Brick testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connector your IMU Brick to the PC over USB, you should see a tab named
"IMU Brick" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricks/imu_brickv.jpg
   :scale: 60 %
   :alt: IMU Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/imu_brickv.jpg

You can see all of the available data form the IMU Brick. If you hold the
IMU Brick in the orientation as shown in the image and press
"Save Orientation", the movements that you make with the IMU Brick should be
mirrored in the Brick Viewer. Before you press "Save Orientation" you should
hold the IMU Brick still for about 15 seconds, so it can converge to the
correct position.

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <imu_brick_programming_interfaces>` über das
API des IMU Bricks und Beispiele in verschiedenen Programmiersprachen.


IMU Calibration
---------------

The IMU Brick comes factory calibrated and should work out of the box. It is
however easy to recalibrate, if necessary.

The factory calibration has taken place in a room without any significant
magnetic fields. If you want to operate the IMU Brick near something that
has a magnetic field (e.g. near a motor), you will have to recalibrate
the magnetometer in the exact position where it will be used later on!

To calibrate the magnetometer press on "Calibrate" in the Brick Viewer and
choose "Magnetometer" in the tab of the new window. Press "Start Calibration"
and now change the orientation of the IMU Brick until the bias and gain values
shown in the GUI do not change anymore. Press "Ready" when this is the case
and you are done.

Accelerometer and gyroscope can be calibrated similarly, follow the
instructions as given by the calibration tool. We recommend that you
export the calibration before you start recalibrating the accelerometer
and the gyroscope, so you are able to go back to the old calibration.

We recommend that you don't try to recalibrate the gyroscope gain, it is not
possible without suitable external machinery.

The factory calibration for your IMU Brick can be found at:
http://download.tinkerforge.com/imu_calibration/YOUR_IMU_UID.txt
(replace YOUR_IMU_UID by the UID of your IMU Brick).
If you accidentially miscalibrated a sensor or you
flashed a new firmware version, you can reimport the factory calibration.


Quaternions vs Euler Angles
---------------------------

We highly recommend that you use
`quaternions <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
in your project rather than euler angles (`roll, pitch and yaw
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`__), since the latter
exhibits a `gimbal lock <http://en.wikipedia.org/wiki/Gimbal_lock>`__.

A formula to transform quaternions to rotation matrices can be found in the
API documentation. Note that Euler Angles always have an order in which they
are applied. The order is: roll, yaw, pitch.


How to get angles that are independent?
---------------------------------------
It is not possible to get angles for all 3 axis that are completely independent.
At least at the gimbal lock positions there will be jumps of 180 degree for
some of the angles. This is simply not possible otherwise.

If you want rotation angles for the x, y and z axis for a given base
position, you have to rotate the quaternion according to your base
position and calculate the angles after that. The followin Python example should
do exactly that and it should be easy to understand and translate in other
languages. Note that there are gimbal locks at +90 and -90 degree from each of the
angles. The base position will be 0, 0, 0::

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

			self.imu = IMU(self.UID) # Create device object
			self.ipcon = IPConnection(self.HOST, self.PORT) # Create IPconnection to brickd
			self.ipcon.add_device(self.imu) # Add device to IP connection
			# Don't use device before it is added to a connection

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

			x_angle = int(math.atan2(2.0*(y*z - w*x), 1.0 - 2.0*(x*x + y*y))*180/math.pi)
			y_angle = int(math.atan2(2.0*(x*z + w*y), 1.0 - 2.0*(x*x + y*y))*180/math.pi)
			z_angle = int(math.atan2(2.0*(x*y + w*z), 1.0 - 2.0*(x*x + z*z))*180/math.pi)

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
		q.ipcon.destroy()


What is this sourcery, how does it work?
----------------------------------------
With the sensor data gathered by the IMU Brick (angular velocity, acceleration,
magnetic field), it is possible to apply sensor fusion to accquire an absolute
orientation.

For this process often a
`Kalman Filter <http://en.wikipedia.org/wiki/Kalman_filter>`__ is used.
The filter that is used in the IMU Brick is based on
`this paper <http://imumargalgorithm30042010sohm.googlecode.com/files/An%20efficient%20orientation%20filter%20for%20inertial%20and%20inertialmagnetic%20sensor%20arrays.pdf>`__
by S. O. Madgwick. In our tests this new state of the art filter
could achieve significantly better results than a Kalman Filter.

Madgwick's filter calculates the orientation by numerically integrating the
estimated orientation rate. It is computed as the rate of change of
orientation measured by the gyroscopes. The magnitude of the gyroscope
measurement error is removed in the direction of the estimated error,
which is computed from accelerometer and magnetometer measurements.

.. image:: /Images/Bricks/imu_math_magic.png
   :scale: 100 %
   :alt: Block diagram of orientation filter from S. O. Madgwick: "An efficient orientation filter for inertial and inertial/magnetic sensor arrays", University of Bristol, April 2010.
   :align: center
   :target: ../../_images/Bricks/imu_math_magic.png

Image and explanation from S. O. Madgwick: "An efficient orientation filter
for inertial and inertial/magnetic sensor arrays", University of Bristol,
April 2010.


.. _imu_brick_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: IMU_Brick_hlpi.table


On Device Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
 In Kürze!

 Eine API und Dokumentation um direkt auf dem Mikrocontroller zu programmieren
 (vergleichbar mit Arduino) ist geplant.
 Bis es soweit ist kann unsere Firmware als Grundlage für eigene Modifikationen
 verwendet werden (C Kenntnisse vorausgesetzt).

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"
