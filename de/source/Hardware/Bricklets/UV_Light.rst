
.. include:: UV_Light.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _uv_light_bricklet:

UV Light Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_uv_light_tilted_[?|?].jpg           UV Ligh Bricklet
	Bricklets/bricklet_uv_light_horizontal_[?|?].jpg       UV Ligh Bricklet
	Bricklets/bricklet_uv_light_brickv_[100|].jpg          UV Ligh Bricklet im Brick Viewer
	Dimensions/uv_light_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das UV Light Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`UV Light Bricklet 2.0 <uv_light_v2_bricklet>`
 empfohlen.

Features
--------

* Misst UV Lichtintensität in µW/cm² und UV Index


.. _uv_light_bricklet_description:

Beschreibung
------------

Mit dem UV Light :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die `UV Lichtintensität
<https://en.wikipedia.org/wiki/Ultraviolet>`__ messen. Die gemessene
Intensität kann in µW/cm² ausgelesen werden. 1 µW/cm² entspricht dabei
0,004 UV Index.
Mit konfigurierbaren Events ist es möglich auf Intensitätsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Dieses Bricklet kann z.B. als UV Warner und zur Umweltdatenmessung
genutzt werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            VEML6070
Stromverbrauch                    < 5mW (< 1mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0mW/cm² bis 328mW/cm²
Auflösung                         1µW/cm² (0,004 UV Index)
Spektralbereich                   320nm bis 410nm (UVA)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* VEML6070 Datenblatt (`Download <https://github.com/Tinkerforge/uv-light-bricklet/raw/master/datasheets/veml6070.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/uv-light-bricklet/raw/master/hardware/uv-light-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/uv_light_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/uv-light-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2BfEWjJ>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/uv_light/uv-light.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/uv_light/uv-light.FCStd>`__)


.. _uv_light_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die UV Lichtintensität in µW/cm² und
UV Index. Der Graph gibt den zeitlichen Verlauf der UV Lichtintensität wieder.

.. image:: /Images/Bricklets/bricklet_uv_light_brickv.jpg
   :scale: 100 %
   :alt: UV Light Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_uv_light_brickv.jpg

|test_pi_ref|


.. _uv_light_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das UV Light Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für UV Light Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: UV_Light.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für UV Light Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _uv_light_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: UV_Light_hlpi.table
