
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / IMU Brick 2.0
:FIXME_shoplink: ../../../shop/bricks/imu-v2-brick.html

.. include:: IMU_V2_Brick.substitutions


.. _imu_v2_brick:

IMU Brick 2.0
=============

.. note::
  Dieser Brick ist noch in Entwicklung!


Features
--------

* Voll ausgestattete IMU/AHRS mit 9 Freiheitsgraden (je 3-Achsen
  Beschleunigungssensor, Kompass, Gyroskop)
* Keine akkumulierenden Fehler, kein Gimbal Lock!
* Werkskalibriert, automatische durchgehende Selbstkalibrierung während des
  Betriebs
* Berechnet Quaternionen, lienare Beschleunigung, Schwerkraftvektor sowie
  Gier- (Heading), Roll- und Nick- (Pitch) Winkel
* Direkt auslesbar per USB, erweiterbar über zwei Bricklet Anschlüsse


.. _imu_v2_brick_description:

Beschreibung
------------


Technische Spezifikation
------------------------

==============================================================  ============================================================
Eigenschaft                                                     Wert
==============================================================  ============================================================
Beschleunigungs-, Magnetfeld-, Winkelgeschwindigkeitsauflösung  14Bit, 16Bit, 16Bit
Auflösung der Gier- (Heading), Roll-, Nick- (Pitch) Winkel      0,01° Schritte
Quaternionenauflösung                                           16Bit
Abtastrate                                                      100Hz
--------------------------------------------------------------  ------------------------------------------------------------
--------------------------------------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse                                             2
Abmessungen (B x T x H)                                         40 x 40 x 19mm (1,57 x 1,57 x 0,75")
Gewicht                                                         TBDg
Stromverbrauch                                                  TBDmA
==============================================================  ============================================================


Ressourcen
----------

* BNO055 Datenblatt (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/datasheets/BNO055.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/hardware/imu-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/imu_v2_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/imu-v2-brick/zipball/master>`__)


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


.. _imu_v2_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: IMU_V2_Brick_hlpi.table
