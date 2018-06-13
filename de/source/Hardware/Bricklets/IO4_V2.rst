
:shoplink: ../../../shop/bricklets/io4-v2-bricklet.html

.. include:: IO4_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _io4_v2_bricklet:

IO-4 Bricklet 2.0
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_io4_v2_tilted_[?|?].jpg           IO-4 Bricklet 2.0
	Bricklets/bricklet_io4_v2_tilted2_[?|?].jpg          IO-4 Bricklet 2.0
	Bricklets/bricklet_io4_v2_top_[?|?].jpg              IO-4 Bricklet 2.0
	Bricklets/bricklet_io4_v2_brickv_[100|].jpg          IO-4 Bricklet 2.0 im Brick Viewer
	Dimensions/io4_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 4 digitale Ein- und Ausgänge
* 3,3V Logikspannung
* Konfigurierbare Pull-Ups und Interrupts
* PWM-Ausgabe mit einer Frequenz bis zu 32MHz


.. _io4_v2_bricklet_description:

Beschreibung
------------

Mit dem IO-4 :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` um externe digitale Ein- und Ausgänge
(I/Os) erweitert werden.

Das Bricklet besitzt 4 I/O Pins die unabhängig voneinander als Ein- oder Ausgänge
konfiguriert werden können. Jeder Eingang kann zusätzlich mit einem Pull-Up oder als
Interrupt-Quelle konfiguriert werden. Die I/O Pins sind über Schraubklemmen nach außen
geführt. Zwei zusätzliche Schraubklemmen führen 3,3V und GND nach außen.

In typischen Anwendungen können Schalter, Taster und LEDs angeschlossen werden

Das IO-4 Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  =================================================================
Eigenschaft                       Wert
================================  =================================================================
I/O Pins                          4
Stromverbrauch                    30mW (6mA bei 5V)
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
I/O Spannung                      3,3V
Maximaler Ausgangsstrom           50mA** (pro Ausgang), 100mA (fester 3,3V Ausgang)
Maximale API Aufrufe*             ``set-value`` (1kHz), ``get-value`` (0,5kHz), Callbacks (1kHz)
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
Abmessungen (B x T x H)           35 x 35 x 14mm (1,38 x 1,38 x 0,55")
Gewicht                           15g
================================  =================================================================

\* abhängig vom jeweiligen System (Betriebssystem, CPU etc.)

\** 50mA pro Ausgang, allerdings maximal 130mA über alle Ausgänge

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/io4-v2-bricklet/raw/master/hardware/io4-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/io4_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/io4-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rzQHe1>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/io4_v2/io4-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/io4_v2/io4-v2.FCStd>`__)


.. _io4_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|

TODO: Screenshot machen

.. image:: /Images/Bricklets/bricklet_io4_v2_brickv.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_v2_brickv.jpg

|test_pi_ref|

Jeder Channel kann als Eingang oder Ausgang betrieben werden.
Für Eingangspins kann zusätzlich ein Pull-Up geschaltet werden. Die aktuelle
Konfiguration und der Zustand der Channel wird in der Tabelle aufgelistet.


.. _io4_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das IO-4 Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-io-4-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_io4_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für IO-4 Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_io4_case_1000.jpg

.. include:: IO4_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/io4_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für IO-4 Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/io4_exploded.png

|bricklet_case_hint|


.. _io4_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: IO4_V2_hlpi.table
