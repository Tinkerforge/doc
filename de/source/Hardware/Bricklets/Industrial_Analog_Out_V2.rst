
:DISABLED_shoplink: ../../../shop/bricklets/industrial-analog-out-v2-bricklet.html

.. include:: Industrial_Analog_Out_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_analog_out_v2_bricklet:

Industrial Analog Out Bricklet 2.0
==================================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_analog_out_v2_tilted_[?|?].jpg           Industrial Analog Out Bricklet 2.0
	Bricklets/bricklet_industrial_analog_out_v2_horizontal_[?|?].jpg       Industrial Analog Out Bricklet 2.0
	Bricklets/bricklet_industrial_analog_out_v2_master_[100|600].jpg       Industrial Analog Out Bricklet 2.0 mit Master Brick
	Cases/bricklet_industrial_analog_out_v2_case_[100|600].jpg             Industrial Analog Out Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_industrial_analog_out_v2_brickv_[100|].jpg          Industrial Analog Out Bricklet 2.0 im Brick Viewer
	Dimensions/industrial_analog_out_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Gleichzeitig programmierbarer Spannungs- und Stromausgang
* Gibt elektrischen Strom zwischen 0mA und 24mA aus (IEC 60381-1)
* Gibt elektrische Spannung zwischen 0V und 10V aus (IEC 60381-2)
* Keine externe Stromversorgung nötig


.. _industrial_analog_out_v2_bricklet_description:

Beschreibung
------------

Das Industrial Analog Out :ref:`Bricklet <primer_bricklets>` 2.0 kann genutzt werden
um :ref:`Bricks <primer_bricks>` mit einem 12Bit `Digital-Analog-Wandler
<https://de.wikipedia.org/wiki/Digital-Analog-Umsetzer>`__ zu erweitern.
Mit diesem können gekoppelte elektrische Spannungen und Ströme generiert werden.
Die Spannung kann in mV und der Strom in µA angegeben werden.

Das Industrial Analog Out Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
D/A-Wandler                       DAC7760
Stromverbrauch                    90mW (18mA bei 5V, ohne Last)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         bis zu 1,2mV / 4,8µA

Spannungsbereiche                 * 0V - 5V
                                  * 0V - 10V

Strombereiche                     * 4mA - 20mA
                                  * 0mA - 20mA
                                  * 0mA - 24mA

VOUT Ausgang                      bis zu 30mA
12V Spannungsversorgungs-Ausgang  bis zu 100mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* DAC7760 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-analog-out-v2-bricklet/raw/master/datasheets/dac7760.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-analog-out-v2-bricklet/raw/master/hardware/industrial-analog-out-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_analog_out_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-analog-out-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2NYVTln>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_analog_out_v2/industrial-analog-out-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_analog_out_v2/industrial-analog-out-v2.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Analog Out Bricklet besitzt 2.0 eine 8 Pol Anschlussklemme.
Das folgende Bild stellt die Anschlussmöglichkeiten dar:

..
  TODO: Neues Bild?

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_caption_1200.jpg


.. _industrial_analog_out_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Das Industrial Analog Out Bricklet besitzt eine 8 Pol Anschlussklemme.
Das folgende Bild stellt die Anschlussmöglichkeiten dar:

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_v2_brickv.jpg

|test_pi_ref|


.. _industrial_analog_out_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Analog Out Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Analog_Out_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_analog_out_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Analog_Out_V2_hlpi.table
