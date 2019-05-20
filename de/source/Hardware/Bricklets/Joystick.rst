
:shoplink: ../../../shop/bricklets/joystick-bricklet.html

.. include:: Joystick.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _joystick_bricklet:

Joystick Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_joystick_tilted_[?|?].jpg           Joystick Bricklet
	Bricklets/bricklet_joystick_front_[?|?].jpg            Joystick Bricklet
	Bricklets/bricklet_joystick_horizontal_[?|?].jpg       Joystick Bricklet
	Bricklets/bricklet_joystick_master_[100|600].jpg       Joystick Bricklet mit Master Brick
	Cases/bricklet_joystick_case_[100|600].jpg             Joystick Bricklet im Gehäuse
	Bricklets/bricklet_joystick_brickv_[100|].jpg          Joystick Bricklet im Brick Viewer
	Dimensions/joystick_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Joystick Bricklet ist abgekündigt. Wir verkaufen noch unseren restlichen Lagerbestand.
 Als Ersatz wird das :ref:`Joystick Bricklet 2.0 <joystick_v2_bricklet>`
 empfohlen.


Features
--------

* 2-Achsen Joystick mit Taster


.. _joystick_bricklet_description:

Beschreibung
------------

Das Joystick :ref:`Bricklet <primer_bricklets>` kann an jeden
:ref:`Brick <primer_bricks>` angeschlossen werden.

Der Joystick ist 2-achsig und mit einem Taster ausgestattet.
Die Position des Joysticks (X/Y Koordinaten) und der Status des Tasters kann
ausgelesen werden. Zusätzlich können Events konfiguriert werden die ausgelöst
werden wenn der Stick eine bestimmte Position erreicht oder der Taster gedrückt
wird.

Der Joystick kann benutzt werden um z.B. Roboter oder Spiele zu steuern.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Joystick                          2-achsig mit Taster
Stromverbrauch                    2mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
X/Y Position                      -100/100, 0=Mittelposition
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 45 x 23mm (0,98 x 1,77 x 0,9")*
Gewicht                           12g*
================================  ============================================================

\* ohne Knopf


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/joystick-bricklet/raw/master/hardware/joystick-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/joystick_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/joystick-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2zgphAT>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/joystick/joystick.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/joystick/joystick.FCStd>`__)


.. _joystick_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_joystick_master_600.jpg
   :scale: 100 %
   :alt: Joystick Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_master_1200.jpg

|test_tab|

.. image:: /Images/Bricklets/bricklet_joystick_brickv.jpg
   :scale: 100 %
   :alt: Joystick Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_brickv.jpg

Auf dem Tab wird in einem Koordinatenkreuz die aktuelle Position des Sticks
angezeigt. Der Zustand des Tasters wird über die Füllung des Kreises angezeigt.
Wenn der Taster gedrückt ist dann wird der Kreis gefüllt dargestellt.
Der Graph darunter gibt den zeitlichen Verlauf der Position wieder.
Der Verlauf im abgebildeten Graph ist durch folgenden Bewegungsablauf des
Joysticks entstanden: hoch, runter, rechts, links.

Falls die Position nicht als (0,0) angezeigt wird obwohl sich der Stick in
Mittelstellung befindet, dann kann der "Calibrate (0,0)" Knopf geklickt werden
um die Null-Position zu kalibrieren.

|test_pi_ref|


.. _joystick_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Joystick Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-joystick-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_joystick_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Joystick Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_joystick_case_1000.jpg

.. include:: Joystick.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/joystick_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Joystick Bricklet
   :align: center
   :target: ../../_images/Exploded/joystick_exploded.png

|bricklet_case_hint|


.. _joystick_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Joystick_hlpi.table
