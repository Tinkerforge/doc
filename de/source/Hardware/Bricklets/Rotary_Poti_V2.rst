
:DISABLED_shoplink: ../../../shop/bricklets/rotary-poti-v2-bricklet.html

.. include:: Rotary_Poti_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rotary_poti_v2_bricklet:

Rotary Poti Bricklet 2.0
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rotary_poti_v2_tilted_[?|?].jpg           Rotary Poti Bricklet 2.0
	Bricklets/bricklet_rotary_poti_v2_top_[?|?].jpg              Rotary Poti Bricklet 2.0
	Bricklets/bricklet_rotary_poti_v2_knob_[?|?].jpg             Rotary Poti Bricklet 2.0
	Bricklets/bricklet_rotary_poti_v2_side_[?|?].jpg             Rotary Poti Bricklet 2.0
	Bricklets/bricklet_rotary_poti_v2_brickv_[100|].jpg          Rotary Poti Bricklet 2.0 im Brick Viewer
	Dimensions/rotary_poti_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 300° Dreh-Potentiometer
* Ausgabe der Position von -150° bis 150° in 1° Schritten


.. _rotary_poti_v2_bricklet_description:

Beschreibung
------------

Das Rotary Poti :ref:`Bricklet <primer_bricklets>` ist mit einem
Dreh-`Potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`__ ausgestattet,
dessen Position über einen :ref:`Brick <primer_bricks>` ausgelesen werden kann. 
Zusätzlich können Events konfiguriert werden, die ausgelöst werden, wenn eine 
spezifizierte Position erreicht wird.

Dieses Bricklet kann für Steueraufgaben benutzt werden, wie z.B. das Steuern
einer Lautstärke.

Das Rotary Poti Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Dreh-Potentiometer                1 Umdrehung, 300°
Stromverbrauch                    40mW (8mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          -150° bis 150° (links nach rechts) in 1° Schritten
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 23mm (1,18 x 0,98 x 0,9")*
Gewicht                           7g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rotary-poti-v2-bricklet/raw/master/hardware/rotary-poti-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rotary_poti_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rotary-poti-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2MjfcsB>`__ | Download: `STEP <https://download.tinkerforge.com/3d/rotary_poti_v2/rotary_poti_v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/rotary_poti_v2/rotary_poti_v2.FCStd>`__)


.. _rotary_poti_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_rotary_poti_v2_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_v2_brickv.jpg

Der Graph ist durch Drehen des Knopfes von links nach rechts und zurück
entstanden.

|test_pi_ref|


.. _rotary_poti_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Rotary Poti Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-rotary-poti-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_rotary_poti_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Rotary Poti Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_poti_case_1000.jpg

.. include:: Rotary_Poti_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Rotary Poti Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|


.. _rotary_poti_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Rotary_Poti_V2_hlpi.table
