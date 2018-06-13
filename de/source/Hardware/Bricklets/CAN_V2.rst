
:shoplink: ../../../shop/bricklets/can-v2-bricklet.html

.. include:: CAN_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _can_v2_bricklet:

CAN Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_can_v2_tilted_[?|?].jpg           CAN Bricklet 2.0
	Bricklets/bricklet_can_v2_tilted2_[?|?].jpg          CAN Bricklet 2.0
	Bricklets/bricklet_can_v2_top_[?|?].jpg              CAN Bricklet 2.0
	Bricklets/bricklet_can_v2_brickv_[100|].jpg          CAN Bricklet 2.0 im Brick Viewer
	Dimensions/can_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Sendet und empfängt Daten über einen CAN-Bus
* Konfigurierbare Baudrate, Modi und Filter


.. _can_v2_bricklet_description:

Beschreibung
------------

Mit dem CAN :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` Daten auf einem CAN-Bus
senden und empfangen.

Die Baudrate kann zwischen 10kbit/s und 1Mbit/s konfiguriert werden. Es
ist möglich Filter anzuwenden um nur Frames mit einem spezifischen
Identifier zu empfangen.

Das CAN Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    72mW (14.4mA bei 5V, Idle)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Baudrate                          10kbit/s - 1Mbit/s
Maximaler Durchsatz               1000 Frames pro Sekunden*
Filter                            Disabled / Accept All / Match / Match Data / Match Extended
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 35 x 14mm (1,77 x 1,38 x 0,55")
Gewicht                           8.6g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/can-v2-bricklet/raw/master/hardware/can-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/can_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/can-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2KeTiSi>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/can_v2/can-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/can_v2/can-v2.FCStd>`__)


.. _can_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Verbinde ein CAN Gerät an die CAN-L, CAN-H und GND Anschlussklemme.

|test_tab|
Wenn alles wie erwartet funktioniert, können die Daten ausgelesen werden die
über den verbundeteten CAN-Bus geschickt werden.

.. image:: /Images/Bricklets/bricklet_can_v2_brickv.jpg
   :scale: 100 %
   :alt: CAN Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_can_v2_brickv.jpg

|test_pi_ref|


.. _can_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das CAN Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-can-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_can_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für CAN Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_can_built_up1_case_1000.jpg

.. include:: CAN_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/can_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für CAN Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/can_exploded.png

|bricklet_case_hint|


.. _can_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: CAN_V2_hlpi.table
