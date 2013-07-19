
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Analog In Bricklet
:shoplink: ../../../shop/bricklets/analog-in-bricklet.html

.. include:: Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_bricklet:

Analog In Bricklet
==================

.. raw:: html

    {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
    {{
        tfdocstart("Bricklets/bricklet_analog_in_tilted_350.jpg",
                   "Bricklets/bricklet_analog_in_tilted_600.jpg",
                   "Analog In Bricklet")
    }}
    {{
        tfdocimg("Bricklets/bricklet_analog_in_vertical_100.jpg",
                 "Bricklets/bricklet_analog_in_vertical_600.jpg",
                 "Analog In Bricklet")
    }}
    {{
        tfdocimg("Bricklets/bricklet_analog_in_horizontal_100.jpg",
                 "Bricklets/bricklet_analog_in_horizontal_600.jpg",
                 "Analog In Bricklet")
    }}
    {{
        tfdocimg("Bricklets/bricklet_analog_in_master_100.jpg",
                 "Bricklets/bricklet_analog_in_master_600.jpg",
                 "Analog In Bricklet mit Master Brick")
    }}
    {{
        tfdocimg("Bricklets/bricklet_analog_in_brickv_100.jpg",
                 "Bricklets/bricklet_analog_in_brickv.jpg",
                 "Analog In Bricklet im Brick Viewer")
    }}
    {{
        tfdocimg("Dimensions/analog_in_bricklet_dimensions_100.png",
                 "Dimensions/analog_in_bricklet_dimensions_600.png",
                 "Umriss und Bohrplan")
    }}
    {{ tfdocend() }}


Features
--------

* Misst elektrische Spannungen bis zu 45V
* Ausgabe in 1mV Schritten (12Bit Auflösung)
* Hohe Auflösung bis zu 1,48mV


Beschreibung
------------

Das Analog In :ref:`Bricklet <product_overview_bricklets>` kann benutzt werden
um :ref:`Bricks <product_overview_bricks>` die Möglichkeit zu geben elektrische
Spannungen zu messen.
Der Messbereich beträgt 0V bis 45V mit hoher Auflösung für kleine Spannungen.
Die gemessene Spannung kann direkt in `Volt
<http://de.wikipedia.org/wiki/Volt>`__ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Spannungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            Automatisch geschalteter Spannungsteiler
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Elektrische Spannung              0V - 45V in 1mV Schritten, 12Bit Auflösung
Messbereich                       Automatisch geschaltet

                                  * 0V - 6,05V, ~1,48mV Auflösung
                                  * 0V - 10,32V, ~2,52mV Auflösung
                                  * 0V - 36,30V, ~8,86mV Auflösung
                                  * 0V - 45,00V, ~11,25mV Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 14mm (1,18 x 0,98 x 0,55")
Gewicht                           6g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/analog-in-bricklet/raw/master/hardware/analog-in-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog_in_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/analog-in-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Analog In Bricklet hat vier Anschlussklemmen. Über diese sind folgende
Ausgangssignale verfügbar: 5V, 3,3V sowie GND. Zwischen der VIN Anschlussklemme
und GND kann die zu messende Spannung angelegt werden. Das folgende Bild
zeigt die vier Anschlussklemmen.

.. image:: /Images/Bricklets/bricklet_analog_in_vertical_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet Anschlussklemmen
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_vertical_1200.jpg


.. _analog_in_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss noch eine Spannungsquelle mit dem Bricklet verbunden werden.
Zum Beispiel kann der Pluspol einer Batterie mit der VIN Anschlussklemme und
der Minuspol mit der GND Anschlussklemme verbunden werden.

.. image:: /Images/Bricklets/bricklet_analog_in_master_600.jpg
   :scale: 100 %
   :alt: Analog In Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_brickv.jpg

|test_pi_ref|

.. _analog_in_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Analog In Bricklet <https://www.tinkerforge.com/de/shop/cases/case-analog-in-out-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_analog_in_case_build_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Analog In Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_case_build_up_1000.jpg

.. include:: Analog_In.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Analog In Bricklet
   :align: center
   :target: ../../_images/Exploded/analog_in_exploded.png

|bricklet_case_hint|


.. _analog_in_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Analog_In_hlpi.table
