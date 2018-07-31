
:DISABLED_shoplink: ../../../shop/bricklets/uv-light-v2-bricklet.html

.. include:: UV_Light_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _uv_light_v2_bricklet:

UV Light Bricklet 2.0
=====================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_uv_light_v2_tilted_[?|?].jpg           UV Light Bricklet 2.0
	Bricklets/bricklet_uv_light_v2_horizontal_[?|?].jpg       UV Light Bricklet 2.0
	Bricklets/bricklet_uv_light_v2_master_[100|600].jpg       UV Light Bricklet 2.0 mit Master Brick
	Cases/bricklet_uv_light_v2_case_[100|600].jpg             UV Light Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_uv_light_v2_brickv_[100|].jpg          UV Light Bricklet 2.0 im Brick Viewer
	Dimensions/uv_light_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst UV-A, UV-B UV Index


.. _uv_light_v2_bricklet_description:

Beschreibung
------------

Das UV Light :ref:`Bricklet <primer_bricklets>` 2.0 misst UV-A sowie UV-B
und berechnet aus diesen Messungen den `UV-Index <https://de.wikipedia.org/wiki/UV-Index>`__.

Mit konfigurierbaren Events ist es möglich auf Intensitätsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Dieses Bricklet kann z.B. als UV Warner und zur Umweltdatenmessung
genutzt werden.

Das UV Light Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            VEML6076
Stromverbrauch                    35mW (7mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
UV-A Auflösung                    0,93 µW/cm²
UV-B Auflösung                    2,1 µW/cm²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Gewicht                           2.1g
================================  ============================================================


Ressourcen
----------

* VEML6075 Datenblatt (`Download <https://github.com/Tinkerforge/uv-light-v2-bricklet/raw/master/datasheets/veml6075.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/uv-light-v2-bricklet/raw/master/hardware/uv-light-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/uv_light_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/uv-light-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2KcOI6s>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/uv_light_v2/uv-light-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/uv_light_v2/uv-light-v2.FCStd>`__)


.. _uv_light_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird der UV-A und UV-B Messwert sowie der
UV-Index angezeigt. Der Graph gibt den zeitlichen Verlauf wieder.

TODO: Neuer Screenshot mit UV-Index!

.. image:: /Images/Bricklets/bricklet_uv_light_v2_brickv.jpg
   :scale: 100 %
   :alt: UV Light Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_uv_light_v2_brickv.jpg

|test_pi_ref|


.. _uv_light_v2_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das UV Light Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-uv-light-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_uv_light_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für UV Light Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_uv_light_v2_case_1000.jpg

	.. include:: UV_Light_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/uv_light_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für UV Light Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/uv_light_v2_exploded.png

	|bricklet_case_hint|


.. _uv_light_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: UV_Light_V2_hlpi.table
