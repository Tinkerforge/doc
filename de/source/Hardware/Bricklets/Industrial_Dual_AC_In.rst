:shoplink: ../../../shop/bricklets/industrial-dual-ac-in-bricklet.html

.. include:: Industrial_Dual_AC_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_ac_in_bricklet:

Industrial Dual AC In Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_ac_in_tilted_[?|?].jpg           Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_w_connector_[?|?].jpg      Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_horizontal_[?|?].jpg       Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_caption_[?|?].jpg          Industrial Dual AC In Bricklet
	Bricklets/bricklet_industrial_dual_ac_in_brickv_[100|].jpg          Industrial Dual AC In Bricklet im Brick Viewer
	Dimensions/industrial_dual_ac_in_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Zwei Eingänge die 230VAC Netzspannung erkennen können
* Zustandsanzeige mit LED pro Eingang


.. _industrial_dual_ac_in_bricklet_description:

Beschreibung
------------

Mit dem Industrial Dual AC In :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` um zwei Eingänge zum erkennen von 230VAC Netzspannung
erweitert werden. Der Zustand wird jeweils durch eine LED angezeigt.

Dieses Bricklet kann benutzt werden um zu erkennen ob 230V AC auf einer Leitung
anliegen oder nicht.

.. warning::
 Anschlussklemmen und Kontakte sind nicht isoliert. Beim Schalten von hohen
 Spannungen sollte das Dual AC In Bricklet in ein Gehäuse verbaut werden.
 Das Berühren der Kontakte ist potentiell lebensgefährlich!

Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Optokoppler                         Fairchild HCPL2731
Stromverbrauch                      TBDmW (5mA bei 5V)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                             TBDg
==================================  ============================================================


Ressourcen
----------

* HCPL2731 Optokoppler (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/raw/master/datasheets/HCPL2731.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/raw/master/hardware/industrial-dual-ac-in-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_ac_in_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://a360.co/3nvkxgh>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_in/industrial-dual-ac-in.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_in/industrial-dual-ac-in.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeiten des Industrial Dual AC In Bricklet.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_in_caption_front_and_top_800.jpg
   :scale: 100 %
   :alt: Industrial Dual AC In Bricklet Anschlussmöglichkeiten
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_in_caption_front_and_top_1200.jpg


.. _industrial_dual_ac_in_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_in_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual AC In Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_in_brickv.jpg

|test_pi_ref|


.. _industrial_dual_ac_in_bricklet_case:

Gehäuse
-------

TBD


.. _industrial_dual_ac_in_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_AC_In_hlpi.table
