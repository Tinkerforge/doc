
:DISABLED_shoplink: ../../../shop/bricklets/io4-v2-bricklet.html

.. include:: IO4_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _io4_v2_bricklet:

IO-4 Bricklet 2.0
=================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_io4_v2_tilted_[?|?].jpg           IO-4 Bricklet 2.0
	Bricklets/bricklet_io4_v2_tilted2_[?|?].jpg          IO-4 Bricklet 2.0
	Bricklets/bricklet_io4_v2_top_[?|?].jpg              IO-4 Bricklet 2.0
	Cases/bricklet_io4_v2_case_[100|600].jpg             IO-4 Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_io4_v2_brickv_[100|].jpg          IO-4 Bricklet 2.0 im Brick Viewer
	Dimensions/io4_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 4 digitale Ein- und Ausgänge
* 3,3V Logikspannung
* Konfigurierbare Pull-Ups und Interrupts


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
In unserem Testaufbau ist eine LED über einen Vorwiderstand angeschlossen,
mit Anode an Pin 3 und Kathode an einen GND Pin.
Zusätzlich ist noch ein Schiebeschalter angeschlossen der Pin 0 mit GND
verbinden kann (siehe folgendes Bild).

TODO: Bild machen

.. image:: /Images/Bricklets/bricklet_io4_master_600.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_master_1200.jpg

|test_tab|

TODO: Screenshot machen

.. image:: /Images/Bricklets/bricklet_io4_v2_brickv.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_v2_brickv.jpg

|test_pi_ref|

Hier kann die "Debounce Period" eingestellt werden, dies ist die Entprellperiode
für die Interrupt Callbacks. Ein Beispiel: Wenn die Entprellperiode auf 100 gestellt
wird, werden Interrupts maximal alle 100ms ausgelöst. Dies ist notwendig wenn
etwas prellendes (z.B. ein Taster) an das IO-4 Bricklet angeschlossen wird.
Der optimale Wert kann im Brick Viewer ermittelt und dann später im eigenen
Programm verwendet werden.

Unter der Einstellung für die Entprellperiode können die einzelnen Pins
konfiguriert werden. Jeder Pin kann als Eingang oder Ausgang betrieben werden.
Für Eingangspins kann zusätzlich ein Pull-Up geschaltet werden. Die aktuelle
Konfiguration und der Zustand der Pins ist dann in der Tabelle weiter unten
aufgelistet.

Um die LED leuchten zu lassen muss Pin 3 als Ausgang konfiguriert und auf
logisch 1 (High) gestellt werden. Um den Schiebeschalter zu testen muss Pin 0
als Eingang mit Pull-Up konfiguriert werden. Der Pull-Up ist nötig um einen
stabilen Zustand zu erreichen wenn der Schiebeschalter Pin 0 nicht mit GND
verbindet. In der Tabelle sollte sich jetzt der Zustand des Pins ändern wenn
der Schiebeschalter umgeschaltet wird.

Wenn kein Schalter oder eine LED zu Hand ist kann auch ein Voltmeter verwendet
werden um Änderungen an Ausgangspins zu messen. Interrupts an Eingangspins können
auch mit Hilfe einer Büroklammer erzeugt werden.

.. _io4_v2_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das IO-4 Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-io4-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_io4_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für IO-4 Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_io4_v2_case_1000.jpg

	.. include:: IO4_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/io4_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für IO-4 Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/io4_v2_exploded.png

	|bricklet_case_hint|


.. _io4_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: IO4_V2_hlpi.table
