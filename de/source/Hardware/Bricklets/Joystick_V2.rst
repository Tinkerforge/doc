
:DISABLED_shoplink: ../../../shop/bricklets/joystick-v2-bricklet.html

.. include:: Joystick_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _joystick_v2_bricklet:

Joystick Bricklet 2.0
=====================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_joystick_v2_tilted_[?|?].jpg           Joystick Bricklet 2.0
	Bricklets/bricklet_joystick_v2_horizontal_[?|?].jpg       Joystick Bricklet 2.0
	Bricklets/bricklet_joystick_v2_master_[100|600].jpg       Joystick Bricklet 2.0 mit Master Brick
	Cases/bricklet_joystick_v2_case_[100|600].jpg             Joystick Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_joystick_v2_brickv_[100|].jpg          Joystick Bricklet 2.0 im Brick Viewer
	Dimensions/joystick_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 2-Achsen Joystick mit Taster


.. _joystick_v2_bricklet_description:

Beschreibung
------------

Das Joystick :ref:`Bricklet <primer_bricklets>` 2.0 kann an jeden
:ref:`Brick <primer_bricks>` angeschlossen werden.

Der Joystick ist 2-achsig und mit einem Taster ausgestattet.
Die Position des Joysticks (X/Y Koordinaten) und der Status des Tasters kann
ausgelesen werden. Zusätzlich können Events konfiguriert werden die ausgelöst
werden wenn der Stick eine bestimmte Position erreicht oder der Taster gedrückt
wird.

Der Joystick kann benutzt werden um z.B. Roboter oder Spiele zu steuern.

Das Joystick Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Joystick                          2-achsig mit Taster
Stromverbrauch                    45mW (9mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
X/Y Position                      -100/100, 0=Mittelposition
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 45 x 23mm (0,98 x 1,77 x 0,9")*
Gewicht                           15g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/joystick-v2-bricklet/raw/master/hardware/joystick-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/joystick_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/joystick-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _joystick_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte folgendes Tab im Brick Viewer erscheinen.

.. image:: /Images/Bricklets/bricklet_joystick_v2_brickv.jpg
   :scale: 100 %
   :alt: Joystick Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_v2_brickv.jpg

Auf dem Tab wird in einem Koordinatenkreuz die aktuelle Position des Sticks
angezeigt. Der Zustand des Tasters wird über die Füllung des Kreises angezeigt.
Wenn der Taster gedrückt ist dann wird der Kreis gefüllt dargestellt.
Der Graph darunter gibt den zeitlichen Verlauf der Position wieder.
Der Verlauf im abgebildeten Graph ist durch folgenden Bewegungsablauf des
Joysticks entstanden: hoch, runter, rechts, links.

Falls die Position nicht als (0,0) angezeigt wird obwohl sich der Stick in
Mittelstellung befindet, dann kann der "Calibrate Zero" Knopf geklickt werden
um die Null-Position zu kalibrieren.

|test_pi_ref|


.. _joystick_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Joystick Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-joystick-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_joystick_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Joystick Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_joystick_case_1000.jpg

.. include:: Joystick.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/joystick_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Joystick Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/joystick_exploded.png

|bricklet_case_hint|


.. _joystick_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Joystick_V2_hlpi.table
