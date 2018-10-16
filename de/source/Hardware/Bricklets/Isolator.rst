
:shoplink: ../../../shop/bricklets/isolator-bricklet.html

.. include:: Isolator.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _isolator_bricklet:

Isolator Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_isolator_tilted_[?|?].jpg           Isolator Bricklet
	Bricklets/bricklet_isolator_tilted2_[?|?].jpg          Isolator Bricklet
	Bricklets/bricklet_isolator_top_[?|?].jpg              Isolator Bricklet
	Cases/bricklet_isolator_case_left_[100|600].jpg        Isolator Bricklet im Gehäuse
	Cases/bricklet_isolator_case_right_[100|600].jpg       Isolator Bricklet im Gehäuse
	Bricklets/bricklet_isolator_brickv_[100|].jpg          Isolator Bricklet im Brick Viewer
	Dimensions/isolator_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Galvanische Trennung der Strom- und Datenleitungen
* Kann zwischen allen Bricks und allen Bricklets mit 7 Pol Bricklet Stecker verwendet werden


.. _isolator_bricklet_description:

Beschreibung
------------

Das Isolator :ref:`Bricklet <primer_bricklets>` kann die Strom- und Datenleitungen
zwischen einem Brick und einem Bricklet mit 7 Pol Bricklet Stecker
`galvanisch trennen <https://de.wikipedia.org/wiki/Galvanische_Trennung>`__.

Alle Bricklet mit analoger/digitaler Eingabe/Ausgabe können von Galvanische
Trennung profitieren, zum Beispiel:

* :ref:`Analog Out 3.0 <analog_out_v3_bricklet>`
* :ref:`CAN 2.0 <can_v2_bricklet>`
* :ref:`DMX <dmx_bricklet>`
* :ref:`Industrial Analog Out 2.0 <industrial_analog_out_v2_bricklet>`
* :ref:`Industrial Counter <industrial_counter_bricklet>`
* :ref:`Industrial Dual 0-20mA 2.0 <industrial_dual_0_20ma_v2_bricklet>`
* :ref:`Industrial Dual Analog In 2.0 <industrial_dual_analog_in_v2_bricklet>`
* :ref:`Industrial Dual Relay <industrial_dual_relay_bricklet>`
* :ref:`IO-16 2.0 <io16_v2_bricklet>`
* :ref:`IO-4 2.0 <io4_v2_bricklet>`
* :ref:`Load Cell 2.0 <load_cell_v2_bricklet>`
* :ref:`One Wire <one_wire_bricklet>`
* :ref:`PTC 2.0 <ptc_v2_bricklet>`
* :ref:`RS232 2.0 <rs232_v2_bricklet>`
* :ref:`RS485 <rs485_bricklet>`
* :ref:`Thermocouple 2.0 <thermocouple_v2_bricklet>`
* :ref:`Voltage/Current 2.0 <voltage_current_v2_bricklet>`

Das Isolator Bricklet hat zwei 7 Pol Bricklet Stecker. Es wird zum Brick mit
einem ``7p-10p`` Bricklet Kabel verbunden und zum galvanisch zu trennenden
Bricklet mit einem ``7p-7p`` Bricklet Kabel verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    280mW (56mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Stromleitungs-Isolation           3kV (1s), 60V (dauerhaft)*
Datenleitungs-Isolation           2,5kV (ESD), 600V (60s), 200V (dauerhaft)*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 40 x 15 (1,18 x 1,58 x 0,59")
Gewicht                           7,1g
================================  ============================================================

\* Siehe Datenblatt MAX14850 für Details der Datenleitungs-Isolation und Datenblatt CRE1S0505S3C für Details der Stromleitungs-Isolation.


Ressourcen
----------

* MAX14850 Datenblatt (`Download <https://github.com/Tinkerforge/isolator-bricklet/raw/master/datasheets/MAX14850.pdf>`__)
* CRE1S0505S3C Datenblatt (`Download <https://github.com/Tinkerforge/isolator-bricklet/raw/master/datasheets/CRE1S0505S3C.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/isolator-bricklet/raw/master/hardware/isolator-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/isolator_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/isolator-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2NYVE9E>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/isolator/isolator.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/isolator/isolator.FCStd>`__)


Beispiel
--------

Im foglenden Bild ist ein Isolator Bricklet zu sehen welches auf einer Seite mit
einem Master Brick und auf der anderen Seite mit einem Voltage/Current Bricklet 2.0
verbunden ist.

.. image:: /Images/Bricklets/bricklet_isolator_action_800.jpg
   :scale: 100 %
   :alt: Isolator Bricklet verbunden mit Master Brick und Voltage/Current Bricklet 2.0
   :align: center
   :target: ../../_images/Bricklets/bricklet_isolator_action_1200.jpg

Das Voltage/Current Bricklet 2.0 ist in diesem Beispiel vom Master Brick galvanisch
isoliert. Dadurch ist es auch von anderen Bricks/Bricklets die mit dem Master Brick
verbunden werden können sowie dem USB-Anschluss isoliert.

Es kann jetzt Spannung und Strom gemessen werden ohne das auf das Masse-Potential
geachtet werden muss. Zum Beispiel könnte das Voltage/Current Bricklet 2.0 mit
einer beliebigen Zelle einer Multizellen-Batterie verbunden werden, sogar wenn
die Batterie den Master Brick mit Strom versorgt!

.. _isolator_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| und das Bricklet das isoliert werden solle mit dem Isolator Bricklet.

|test_tab|
Wenn alles wie erwartet funktioniert dann taucht jetzt das Isolator Bricklet und
das isolierte Bricklet im Brick Viewer auf.

.. image:: /Images/Bricklets/bricklet_isolator_brickv.jpg
   :scale: 100 %
   :alt: Isolator Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_isolator_brickv.jpg

|test_pi_ref|


.. _isolator_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Isolator Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-isolator-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_isolator_case_left_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Isolator Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_isolator_case_left_1000.jpg

.. include:: Isolator.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/isolator_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Isolator Bricklet
   :align: center
   :target: ../../_images/Exploded/isolator_exploded.png

|bricklet_case_hint|


.. _isolator_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Isolator_hlpi.table
