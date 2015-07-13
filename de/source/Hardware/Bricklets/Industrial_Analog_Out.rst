
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Analog Out Bricklet
:FIXME_shoplink: ../../../shop/bricklets/industrial-analog-out-bricklet.html

.. include:: Industrial_Analog_Out.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_analog_out_bricklet:

Industrial Analog Out Bricklet
==============================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Gleichzeitig programmierbarer Spannungs- und Stromausgang
* Gibt elektrische Spannung zwischen 0V und 10V aus
* Gibt elektrischen Strom zwischen 0mA und 24mA aus
* Keine externe Stromversorgung nötig


.. _industrial_analog_out_bricklet_description:

Beschreibung
------------

Das Industrial Analog Out :ref:`Bricklet <primer_bricklets>` kann genutzt werden
um :ref:`Bricks <primer_bricks>` mit einem 12Bit `Digital-Analog-Wandler
<http://de.wikipedia.org/wiki/Digital-Analog-Umsetzer>`__ zu erweitern.
Mit diesem können gekoppelte elektrische Spannungen und Ströme generiert werden.
Die Spannung kann in mV und der Strom in µA angegeben werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
D/A-Wandler                       DAC7760
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         bis zu 1,2mV / 4,8µA

Spannungsbereiche                 * 0V - 5V
                                  * 0V - 10V

Strombereiche                     * 4mA - 20mA
                                  * 0mA - 20mA
                                  * 0mA - 24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* DAC7760 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/raw/master/datasheets/dac7760.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/raw/master/hardware/industrial-analog-out-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_analog_out_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Analog Out Bricklet besitzt eine 8 Pol Anschlussklemme.
Das folgende Bild stellt die Anschlussmöglichkeiten dar:

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_caption_1200.jpg


.. _industrial_analog_out_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Auf diesem Tab kann die Ausgangsspannung am VOUT Pin oder der Ausgangsstrom am
IOUT Pin eingestellt werden.

Zu Testzwecken kann die Ausgangsspannung mit einem Voltmeter gemessen
werden. Wenn alles wie erwartet funktioniert sollte die eingestellte Spannung
mit der Messung des Voltmeters übereinstimmen.

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_brickv.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_brickv.jpg

|test_pi_ref|


.. _industrial_analog_out_bricklet_case:

Gehäuse
-------


.. _industrial_analog_out_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Analog_Out_hlpi.table
