
:shoplink: ../../../shop/bricklets/industrial-dual-analog-in-v2-bricklet.html

.. include:: Industrial_Dual_Analog_In_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_analog_in_v2_bricklet:

Industrial Dual Analog In Bricklet 2.0
======================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_analog_in_v2_tilted_[?|?].jpg           Industrial Dual Analog In Bricklet 2.0
	Bricklets/bricklet_industrial_dual_analog_in_v2_tilted2_[?|?].jpg          Industrial Dual Analog In Bricklet 2.0
	Bricklets/bricklet_industrial_dual_analog_in_v2_top_[?|?].jpg              Industrial Dual Analog In Bricklet 2.0
	Bricklets/bricklet_industrial_dual_analog_in_v2_w_connector_[?|?].jpg      Industrial Dual Analog In Bricklet 2.0
	Bricklets/bricklet_industrial_dual_analog_in_v2_brickv_[100|].jpg          Industrial Dual Analog In Bricklet 2.0 im Brick Viewer
	Dimensions/industrial_dual_analog_in_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Unabhängig Messung zweier Spannungen zwischen -35V und +35V (DC)
* 24Bit A/D-Wandler für hohe Auflösung
* Individuell kalibriert
* Genauigkeit von 0,1% / ±4mV über den gesamten Messbereich
* Bis zu 976 Messwerte pro Sekunde


.. _industrial_dual_analog_in_v2_bricklet_description:

Beschreibung
------------

Mit dem Industrial Dual Analog In :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` Spannungen präzise messen. Beide Kanäle des
Bricklets sind kalibriert, so dass die Spannungsmessung sehr verlässlich ist.

Mit konfigurierbaren Events ist es möglich auf Spannungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Das Bricklet verfügt über keine galvanische Trennung zum Tinkerforge System. 
Das heißt es gibt eine direkte elektrische Verbindung zwischen den 
Anschlussklemmen des Bricklets und dem restlichen System. Sollte dies in der 
jeweiligen Anwendung zu ungewollten Verbindungen, Masseschleifen oder 
Kurzschlüssen führen, so ist der Einsatz zusammen mit einem :ref:`Isolator Bricklet <isolator_bricklet>` ratsam.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
A/D-Wandler                       MCP3911
Stromverbrauch                    50mW (10mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Kanäle                            2
Messbereich                       -35V bis +35V (DC)
Auflösung                         24Bit
Genauigkeit                       0,1% / ±4mV über den gesamten Messbereich
Maximaler Ausgangsstrom           150mA (3,3V), 150mA (5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* MCP3911 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-v2-bricklet/raw/master/datasheets/MCP3911.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-v2-bricklet/raw/master/hardware/industrial-dual-analog-in-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_analog_in_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2M5t3iv>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_analog_in_v2/industrial-dual-analog-in-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_analog_in_v2/industrial-dual-analog-in-v2.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Dual Analog In Bricklet 2.0 besitzt eine 8 Pol Anschlussklemme.
Das folgende Bild stellt die Anschlussmöglichkeiten dar:

.. image:: /Images/Bricklets/bricklet_industrial_dual_analog_in_v2_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Dual Analog In Bricklet Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_analog_in_v2_caption_1200.jpg
.. _industrial_dual_analog_in_v2_bricklet_test:


Erster Test
-----------

|test_intro|

|test_connect|.
Anschließend muss eine zu messende Gleichspannungsquelle mit dem Bricklet
verbunden werden. Als Test kann der 3,3V Ausgang mit dem IN0- Eingang und der
GND Pin mit dem IN0+ Eingang verbunden werden.

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_industrial_dual_analog_in_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual Analog In Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_analog_in_v2_brickv.jpg

|test_pi_ref|


.. _industrial_dual_analog_in_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Dual Analog In Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual Analog In Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Dual_Analog_In_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Dual Analog In Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_dual_analog_in_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_Analog_In_V2_hlpi.table
