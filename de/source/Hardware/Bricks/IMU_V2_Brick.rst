
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / IMU Brick 2.0
:shoplink: ../../../shop/bricks/imu-v2-brick.html

.. include:: IMU_V2_Brick.substitutions


.. _imu_v2_brick:

IMU Brick 2.0
=============

.. raw:: html

    {% tfgallery %}

	Bricks/brick_imu_v2_tilted1_[?|?].jpg          IMU Brick 2.0
	Bricks/brick_imu_v2_tilted2_[?|?].jpg          IMU Brick 2.0
	Bricks/brick_imu_v2_front_[?|?].jpg            IMU Brick 2.0
	Bricks/brick_imu_v2_caption_[?|?].jpg          IMU Brick 2.0 mit Beschriftung
	Bricks/brick_imu_v2_top_[?|?].jpg              IMU Brick 2.0 Oberseite
	Bricks/brick_imu_v2_bottom_[?|?].jpg           IMU Brick 2.0 Unterseite
	Dimensions/imu_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Voll ausgestattete IMU/AHRS mit 9 Freiheitsgraden (je 3-Achsen
  Beschleunigungssensor, Kompass, Gyroskop)
* Keine akkumulierenden Fehler, kein Gimbal Lock!
* Werkskalibriert, automatische durchgehende Selbstkalibrierung während des
  Betriebs
* Berechnet Quaternionen, lienare Beschleunigung, Schwerkraftvektor sowie
  unabhängige Gier- (Heading), Roll- und Nick- (Pitch) Winkel
* Direkt auslesbar per USB, erweiterbar über zwei Bricklet Anschlüsse


.. _imu_v2_brick_description:

Beschreibung
------------

Der IMU Brick 2.0 ist der Nachfolger des :ref:`imu_brick` mit höher auflösenden
Sensoren, einfacherer Kalibrierung, zusätzlicher kontinuierlicher
Selbst-Kalibrierung und einer um **zwei Größenordnungen besseren Genauigkeit**.

Der IMU :ref:`Brick <primer_bricks>` 2.0 ist mit je einem 3-Achsen
Beschleunigungssensor, Magnetfeldsensor (Kompass) und Gyroskop ausgestattet und
arbeitet als **USB**
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
benutzt wird, ist der IMU Brick
`Gimbal Lock <https://de.wikipedia.org/wiki/Gimbal_Lock>`__ frei (im Gegensatz
zur Euler-Winkel Darstellung).

Über zwei Anschlüsse können :ref:`Bricklets <primer_bricklets>`
angeschlossen werden, die die Fähigkeiten des Bricks erweitern. Als Beispiel
kann ein :ref:`gps_bricklet` angeschlossen werden um Positionsdaten zu ermitteln.

Der IMU Brick 2.0 kann aber auch mit anderen Bricks in einem
:ref:`Stapel <primer_stack>` genutzt werden.
Zum Beispiel kann ein zusätzlicher :ref:`Master Brick <master_brick>` mit
:ref:`Master Extensions <primer_master_extensions>` genutzt werden,
um die USB Verbindung durch andere kabelgebundene Schnittstellen
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`)
oder drahtlose Schnittstellen (:ref:`WLAN <wifi_extension>`) zu ersetzen.

Ein Vergleichsvideo zwischen IMU Brick 1.0 und IMU Brick 2.0 ist auf Youtube verfügbar:

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/Aq3SqVen5AQ" frameborder="0" allowfullscreen></iframe>

Technische Spezifikation
------------------------

==============================================================  ============================================================
Eigenschaft                                                     Wert
==============================================================  ============================================================
Beschleunigungs-, Magnetfeld-, Winkelgeschwindigkeitsauflösung  14Bit, 16Bit, 16Bit
Auflösung der Gier- (Heading), Roll-, Nick- (Pitch) Winkel      0,0625° Schritte
Quaternionenauflösung                                           16Bit
Abtastrate                                                      100Hz
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse                                             2
Abmessungen (B x T x H)                                         40 x 40 x 19mm (1,57 x 1,57 x 0,75")
Gewicht                                                         12g
Stromverbrauch                                                  415mW (83mA bei 5V)
==============================================================  ============================================================


Ressourcen
----------

* BNO055 Datenblatt (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/datasheets/BNO055.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/hardware/imu-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/imu_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/imu-v2-brick/zipball/master>`__)
* 3D Modell (Download: `STEP <http://download.tinkerforge.com/3d/bricks/imu_v2/imu.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricks/imu_v2/imu.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
IMU Bricks 2.0.

.. image:: /Images/Bricks/brick_imu_v2_caption_600.jpg
   :scale: 100 %
   :alt: IMU Brick 2.0 mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_imu_v2_caption_800.jpg


.. _imu_v2_brick_test:

Erster Test
-----------

|test_intro|

|test_tab|

.. image:: /Images/Bricks/imu_v2_brickv.jpg
   :scale: 100 %
   :alt: IMU Brick 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/imu_v2_brickv.jpg

Alle verfügbaren Daten des IMU Bricks 2.0 werden angezeigt. Wenn der IMU Brick
2.0 wie dargestellt gehalten und dann der "Save Orientation" Knopf geklickt
wird sollten die Bewegungen des IMU Bricks entsprechend im Brick Viewer
widergespiegelt werden.

|test_pi_ref|


Kalibrierung
------------

Der IMU Brick 2.0 führt durchgehend eine Selbst-Kalibrierung durch.
Es ist nicht notwendig eine gesonderte Kalibrierung von Hand durchzuführen. Die
IMU kann die Kalibrierungsdaten speichern, um die Selbst-Kalibrierung nach
einem Neustart zu beschleunigen. Diese Kalibrierungsdaten werden bei der
Produktion bereits gesetzt.

.. image:: /Images/Screenshots/imu_v2_brick_calibration.jpg
   :scale: 100 %
   :alt: IMU Brick 2.0 Kalibrierung im Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/imu_v2_brick_calibration.jpg

Klicke den "Calibration" Knopf im Brick Viewer, um den aktuellen Zustand der
durchgehenden Selbst-Kalibrierung einzusehen. Auf diesem Dialog können auch die
gespeicherten Kalibrierungsdaten aktualisiert werden.


.. _imu_v2_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: IMU_V2_Brick_hlpi.table
