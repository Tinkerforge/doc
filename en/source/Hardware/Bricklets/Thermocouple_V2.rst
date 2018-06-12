
:shoplink: ../../../shop/bricklets/thermocouple-v2-bricklet.html

.. include:: Thermocouple_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermocouple_v2_bricklet:

Thermocouple Bricklet 2.0
=========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermocouple_v2_tilted_[?|?].jpg           Thermocouple Bricklet 2.0
	Bricklets/bricklet_thermocouple_v2_tilted2_[?|?].jpg          Thermocouple Bricklet 2.0
	Bricklets/bricklet_thermocouple_v2_side_[?|?].jpg             Thermocouple Bricklet 2.0
	Bricklets/bricklet_thermocouple_v2_top_[?|?].jpg              Thermocouple Bricklet 2.0
	Cases/bricklet_thermocouple_v2_case_[?|?].jpg                 Thermocouple Bricklet 2.0 in case
	Bricklets/bricklet_thermocouple_v2_brickv_[100|].jpg          Thermocouple Bricklet 2.0 in Brick Viewer
	Dimensions/thermocouple_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures temperature with a thermocouple
* Supports B, E, J, K, N, R, S and T type


.. _thermocouple_v2_bricklet_description:

Description
-----------

The Thermocouple :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure temperature with a
`thermocouple <https://en.wikipedia.org/wiki/Thermocouple>`__. The
measured temperature can be read out in
`°C <https://en.wikipedia.org/wiki/Celsius>`__.
With configurable events it is possible to react on changing 
values without polling.

The supported thermocouple types are B, E, J, K, N, R, S and T. It
is also possible to configure custom gains, with which you can
read out other thermocouple types or even custom thermocouple types.

Faults such as missing thermocouple and over/under-voltage are
automatically detected and reported.

By default the Bricklet comes with a K-type mini thermocouple 
connector. The connector uses Alumel for the negative
Chromel for the positive contact. We can also fit the
Bricklet with a matching connector for other :ref:`thermocouple types
<thermocouple_bricklet_types>`. You can choose type J,T,E,U and N. 
Another option is to choose the wire option. Then you will get the Bricklet 
without any connector but with two 20cm isolated wires. This way you can 
connect your own connector to it.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MAX31856
Current Consumption               45mW (9mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 -210°C to +1800°C
Resolution                        0.01°C
Accuracy                          ±0.15% (full-scale), ±0.7°C (cold-junction)
Supported Types                   B, E, J, K, N, R, S and T (custom types possible)
Connector                         mini thermocouple jack
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 30 x 8mm (1.58 x 1.18 x 0.32")
Weight                            9g
================================  ============================================================


Resources
---------

* MAX31856 datasheet (`Download <https://github.com/Tinkerforge/thermocouple-bricklet/raw/master/datasheets/MAX31856.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/thermocouple-v2-bricklet/raw/master/hardware/thermocouple-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/thermocouple_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/thermocouple-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2rAevPA>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/thermocouple_v2/thermocouple-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/thermocouple_v2/thermocouple-v2.FCStd>`__)


.. _thermocouple_v2_bricklet_test:

Test your Thermocouple Bricklet 2.0
-----------------------------------

|test_intro|

|test_connect| as well as a thermocouple to the Thermocouple Bricklet.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_thermocouple_v2_brickv.jpg
   :scale: 100 %
   :alt: Thermocouple Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_thermocouple_v2_brickv.jpg

|test_pi_ref|


.. _thermocouple_v2_bricklet_case:

Case
----

A `laser-cut case for the Thermocouple Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-thermocouple-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_thermocouple_v2_case_350.jpg
   :scale: 100 %
   :alt: Case for Thermocouple Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_thermocouple_v2_case_1000.jpg

.. include:: Thermocouple_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/thermocouple_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Thermocouple Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/thermocouple_exploded.png

|bricklet_case_hint|


.. _thermocouple_bricklet_types:

Thermocouple types
------------------

Different thermocouple types use different types of metals for their
wires. Optimally, the connector on the Bricklet uses the same types of metals.

By default the Bricklet comes with a K-type mini thermocouple 
connector (Alumel for the negative and Chromel for the positive 
contact). You can connect any type of thermocouple to the
Bricklet too, but with a slight increase in error. If you want to use
a non-K-type thermocouple and you need the best possible performance
we can fit the Bricklet with different connectors for you:

====  ============================  ============================
Type  Negative Contact              Positive Contact
====  ============================  ============================
B     Platinum/Rhodium              Platinum/Rhodium
E     Constantan                    Chromel
J     Constantan                    Iron
K     Alumel                        Chromel
N     Nisil                         Nicrosil
R     Platinum                      Platinum/Rhodium
S     Platinum                      Platinum/Rhodium
T     Constantan                    Copper
====  ============================  ============================

In our shop different connectors can be choosen. If the necessary connector
can't be selected, please contact us before your order.


.. _thermocouple_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Thermocouple_V2_hlpi.table
