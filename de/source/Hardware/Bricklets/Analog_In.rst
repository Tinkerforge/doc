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
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog-in_bricklet_dimensions.png>`__)
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

Teste dein Analog In Bricklet
-----------------------------

To test the Analog In Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Analog In Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable.
Additionally connect a voltage source to the Bricklet.
For testing purposes we have connected a battery.

.. image:: /Images/Bricklets/bricklet_analog_in_master_600.jpg
   :scale: 100 %
   :alt: Analog In Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_master_1200.jpg


If you connect the Brick to the PC over USB,
you should see a tab named "Analog In Bricklet" in the Brick Viewer after you
pressed "connect". Select this tab.
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_brickv.jpg

After this you can go on with writing your own application.
See the :ref:`Programming Interface <analog_in_programming_interfaces>` section
for the API of the Analog In Bricklet and examples in different
programming languages.


.. _analog_in_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Analog_In_hlpi.table
