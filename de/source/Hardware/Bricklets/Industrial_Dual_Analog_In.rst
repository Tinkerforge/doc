
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Dual Analog In Bricklet
:FIXME_shoplink: ../../../shop/bricklets/industrial-dual-analog-in-bricklet.html

.. include:: Industrial_Dual_Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_analog_in_bricklet:

Industrial Dual Analog In Bricklet
==================================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Unabhängig Messung zweier Spanungen zwischen -45V und +45V (DC)
* 24Bit A/D-Wandler für hohe Auflösung
* Kalibriert
* Genaugikeit von 0,1% / ±4mV über den gesamten Messbereich
* Bis zu 976 Messwerte pro Sekunde


.. _industrial_dual_analog_in_bricklet_description:

Beschreibung
------------


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
A/D-Wandler                       MCP3911
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Kanäle                            2
Messbereich                       -45V bis +45V (DC)
Auflösung                         24Bit
Genauigkeit                       0,1% / ±4mV über den gesamten Messbereich
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* MCP3911 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/datasheets/MCP3911.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/hardware/industrial-dual-analog-in-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_analog_in_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Dual Analog In Bricklet besitzt eine 8 Pol Anschlussklemme.
Das folgende Bild stellt die Anschlussmöglichkeiten dar:

.. image:: /Images/Bricklets/bricklet_industrial_dual_analog_in_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Dual Analog In Bricklet Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_analog_in_caption_1200.jpg


.. _industrial_dual_analog_in_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss eine zu messende Gleichspannungsquelle mit dem Bricklet
verbunden werden. Als Test kann der 3,3V Ausgang mit dem IN0- Eingang und der
GND Pin mit dem IN0+ Eingang verbunden werden.

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_industrial_dual_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual Analog In Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_analog_in_brickv.jpg

|test_pi_ref|


.. _industrial_dual_analog_in_bricklet_case:

Gehäuse
-------


.. _industrial_dual_analog_in_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_Analog_In_hlpi.table
