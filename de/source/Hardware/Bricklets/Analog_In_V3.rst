
:shoplink: ../../../shop/bricklets/analog-in-v3-bricklet.html

.. include:: Analog_In_V3.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_v3_bricklet:

Analog In Bricklet 3.0
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_analog_in_v3_tilted_[?|?].jpg           Analog In Bricklet 3.0
	Bricklets/bricklet_analog_in_v3_terminals_[?|?].jpg        Analog In Bricklet 3.0
	Bricklets/bricklet_analog_in_v3_top_[?|?].jpg              Analog In Bricklet 3.0
	Bricklets/bricklet_analog_in_v3_brickv_[100|].jpg          Analog In Bricklet 3.0 im Brick Viewer
	Dimensions/analog_in_v3_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst elektrische Spannungen bis zu 42V (DC)
* Auflösung über den gesamten Messbereich von ~10mV


.. _analog_in_v3_bricklet_description:

Beschreibung
------------

Das Analog In :ref:`Bricklet <primer_bricklets>` 3.0 kann benutzt werden
um :ref:`Bricks <primer_bricks>` die Möglichkeit zu geben elektrische
Spannungen zu messen. Es ist der Nachfolger des :ref:`analog_in_v2_bricklet`.
Die gemessene Spannung kann direkt in `Volt
<https://de.wikipedia.org/wiki/Volt>`__ ausgelesen werden.

Mit konfigurierbaren Events ist es möglich auf Spannungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    70mW (14mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Elektrische Spannung              0V - 42V (DC) in 1mV Schritten, 12Bit Auflösung (~10mV)
Maximaler Ausgangsstrom           150mA (3,3V), 150mA (5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           35 x 30 x 14mm (1,38 x 1,18 x 0,55")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/analog-in-v3-bricklet/raw/master/hardware/analog-in-v3-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog_in_v3_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/analog-in-v3-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2Ew7gh0>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/analog_in_v3/analog-in-v3.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/analog_in_v3/analog-in-v3.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das Analog In Bricklet 3.0 hat fünf Anschlussklemmen. Über diese sind folgende
Ausgangssignale verfügbar: 5V, 3,3V sowie GND. Zwischen der VIN Anschlussklemme
und GND kann die zu messende Spannung angelegt werden.

.. image:: /Images/Bricklets/bricklet_analog_in_v3_top_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet 3.0 Anschlussklemmen
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v3_top_1200.jpg


.. _analog_in_v3_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss eine zu messende Gleichspannungsquelle mit dem Bricklet
verbunden werden. Als Test kann z.B. die 5V oder 3,3V Anschlussklemme mit der
VIN Anschlussklemme verbunden werden. Die beiden GND Anschlussklemmen sind
intern schon verbunden.

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_analog_in_v3_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet 3.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v3_brickv.jpg

|test_pi_ref|


.. _analog_in_v3_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Analog In Bricklet 3.0
<https://www.tinkerforge.com/de/shop/cases/case-analog-in-out-v2-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_analog_in_v2_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Analog In Bricklet 3.0
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_v2_case_built_up_1000.jpg

.. include:: Analog_In_V3.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Analog In Bricklet 3.0
   :align: center
   :target: ../../_images/Exploded/analog_in_v2_exploded.png

|bricklet_case_hint|


.. _analog_in_v3_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Analog_In_V3_hlpi.table
