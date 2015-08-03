
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Dual Analog In Bricklet
:shoplink: ../../../shop/bricklets/industrial-dual-analog-in-bricklet.html

.. include:: Industrial_Dual_Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_analog_in_bricklet:

Industrial Dual Analog In Bricklet
==================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_dual_analog_in_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_dual_analog_in_tilted_600.jpg",
	               "Industrial Dual Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_analog_in_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_dual_analog_in_horizontal_600.jpg",
	             "Industrial Dual Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_analog_in_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_dual_analog_in_brickv.jpg",
	             "Industrial Dual Analog In Bricklet im Brick Viewer")
	}}
	{{ tfdocend() }}

..
	{{
	    tfdocimg("Dimensions/industrial_dual_analog_in_bricklet_dimensions_100.png",
	             "Dimensions/industrial_dual_analog_in_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Unabhängig Messung zweier Spanungen zwischen -35V und +35V (DC)
* 24Bit A/D-Wandler für hohe Auflösung
* Kalibriert
* Genauigkeit von 0,1% / ±4mV über den gesamten Messbereich
* Bis zu 976 Messwerte pro Sekunde


.. _industrial_dual_analog_in_bricklet_description:

Beschreibung
------------

Mit dem Industrial Dual Analog In :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Spannungen präzise messen. Beide Kanäle des
Brickles sind kalibriert, so dass die Spannungsmessung sehr verlässlich ist.

Mit konfigurierbaren Events ist es möglich auf Spannungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
A/D-Wandler                       MCP3911
Stromverbrauch                    15mW (3mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Kanäle                            2
Messbereich                       -35V bis +35V (DC)
Auflösung                         24Bit
Genauigkeit                       0,1% / ±4mV über den gesamten Messbereich
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* MCP3911 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/datasheets/MCP3911.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/hardware/industrial_dual_analog_in-schematic.pdf>`__)
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

Ein `laser-geschnittenes Gehäuse für das Industrial Dual Analog In Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual Analog In Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Dual_Analog_In.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Dual Analog In Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_dual_analog_in_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_Analog_In_hlpi.table
