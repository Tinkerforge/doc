
:shoplink: ../../../shop/bricklets/imu-v3-bricklet.html

.. include:: IMU_V3.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _imu_v3_bricklet:

IMU Bricklet 3.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_imu_v3_tilted_[?|?].jpg           IMU Bricklet 3.0
	Bricklets/bricklet_imu_v3_tilted2_[?|?].jpg          IMU Bricklet 3.0
	Bricklets/bricklet_imu_v3_horizontal_[?|?].jpg       IMU Bricklet 3.0
	Bricklets/bricklet_imu_v3_brickv_[100|].jpg          IMU Bricklet 3.0 im Brick Viewer
	Dimensions/imu_v3_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Voll ausgestattete IMU/AHRS mit 9 Freiheitsgraden (je 3-Achsen
  Beschleunigungssensor, Kompass, Gyroskop)
* Keine akkumulierenden Fehler, kein Gimbal Lock!
* Werkskalibriert, automatische durchgehende Selbstkalibrierung während des
  Betriebs
* Berechnet Quaternionen, lineare Beschleunigung, Schwerkraftvektor sowie
  unabhängige Gier- (Heading), Roll- und Nick- (Pitch) Winkel


.. _imu_v3_bricklet_description:

Beschreibung
------------

Das IMU Bricklet 3.0 bietet die gleiche Funktionalität wie das
:ref:`IMU Brick 2.0 <imu_v2_brick>`, allerdings im Formfaktor eines Bricklets.

Das IMU :ref:`Bricklet <primer_bricklets>` 3.0 ist mit je einem 3-Achsen
Beschleunigungssensor, Magnetfeldsensor (Kompass) und Gyroskop ausgestattet und
arbeitet als
`Inertialsensor <https://de.wikipedia.org/wiki/Inertialsensor>`__.
Dieser kann 9 Freiheitsgrade messen und berechnet
`Quaternionen <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
sowie auch unabhängige `Gier-, Roll- und Nick-Winkel
<https://de.wikipedia.org/wiki/Roll-Pitch-Yaw-Winkel>`__. Es ist ein vollständiges
`Attitude and Heading Reference System
<https://de.wikipedia.org/wiki/Attitude_Heading_Reference_System>`__.

Die API, verfügbar für
:ref:`viele Programmiersprachen <imu_brick_programming_interface>`, erlaubt den
Zugriff auf die berechneten Daten sowie auf die Beschleunigung, Magnetfeld und
Winkelgeschwindigkeiten für die drei Achsen. Wenn die Quaternionen-Darstellung
benutzt wird, ist das IMU Bricklet 3.0
`Gimbal Lock <https://de.wikipedia.org/wiki/Gimbal_Lock>`__ frei (im Gegensatz
zur Euler-Winkel Darstellung).

Das IMU Bricklet 3.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_imu_v3_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_imu_v3_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_imu_v3_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

==============================================================  ============================================================
Eigenschaft                                                     Wert
==============================================================  ============================================================
Sensor                                                          BNO055
Stromverbrauch                                                  95mW (19mA bei 5V)
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Beschleunigungs-, Magnetfeld-, Winkelgeschwindigkeitsauflösung  14Bit, 16Bit, 16Bit
Auflösung der Gier- (Heading), Roll-, Nick- (Pitch) Winkel      0,0625° Schritte
Quaternionenauflösung                                           16Bit
Abtastrate                                                      100Hz
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                                         25 x 25 x 5mm (0,98 x 0,98 x 0,19")
Gewicht                                                         3g
==============================================================  ============================================================


Ressourcen
----------

* BNO055 Datenblatt (`Download <https://github.com/Tinkerforge/imu-v3-bricklet/raw/master/datasheets/bno055.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/imu-v3-bricklet/raw/master/hardware/imu-v3-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/imu_v3_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/imu-v3-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/imu_v3/imu-v3.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/imu_v3/imu-v3.FCStd>`__)


.. _imu_v3_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
	
.. image:: /Images/Bricklets/bricklet_imu_v3_brickv.jpg
   :scale: 100 %
   :alt: IMU Bricklet 3.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_imu_v3_brickv.jpg

Alle verfügbaren Daten des IMU Bricklets 3.0 werden angezeigt. Wenn das IMU Bricklet
3.0 wie dargestellt gehalten und dann der "Save Orientation" Knopf geklickt
wird sollten die Bewegungen des IMU Bricks entsprechend im Brick Viewer
widergespiegelt werden.

|test_pi_ref|


Kalibrierung
------------

Das IMU Bricklet 3.0 führt durchgehend eine Selbst-Kalibrierung durch.
Es ist nicht notwendig eine gesonderte Kalibrierung von Hand durchzuführen. Die
IMU kann die Kalibrierungsdaten speichern, um die Selbst-Kalibrierung nach
einem Neustart zu beschleunigen. Diese Kalibrierungsdaten werden bei der
Produktion bereits gesetzt.

.. image:: /Images/Screenshots/imu_v3_bricklet_calibration.jpg
   :scale: 100 %
   :alt: IMU Bricklet 3.0 Kalibrierung im Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/imu_v3_bricklet_calibration.jpg

Klicke den "Calibration" Knopf im Brick Viewer, um den aktuellen Zustand der
durchgehenden Selbst-Kalibrierung einzusehen. Auf diesem Dialog können auch die
gespeicherten Kalibrierungsdaten aktualisiert werden.


.. _imu_v3_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das IMU Bricklet 3.0
<https://www.tinkerforge.com/de/shop/cases/case-real-time-clock-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_real_time_clock_v2_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für IMU Bricklet 3.0
   :align: center
   :target: ../../_images/Cases/bricklet_real_time_clock_v2_case_1000.jpg

.. include:: IMU_V3.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/real_time_clock_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für IMU Bricklet 3.0
   :align: center
   :target: ../../_images/Exploded/real_time_clock_exploded.png

|bricklet_case_hint|


.. _imu_v3_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: IMU_V3_hlpi.table
