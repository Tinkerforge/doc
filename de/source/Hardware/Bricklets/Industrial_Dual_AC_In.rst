:shoplink: ../../../shop/bricklets/industrial-dual-ac-in-bricklet.html

.. include:: Industrial_Dual_AC_in.substitutions
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
	Bricklets/bricklet_industrial_dual_ac_in_brickv_[100|].jpg          Industrial Dual AC In Bricklet in Brick Viewer
	Dimensions/industrial_dual_ac_in_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Zwei Eingänge um 230VAC Netzspannung zu erkennen
* Zustands-LED pro Eingang


.. _industrial_dual_ac_in_bricklet_description:

Beschreibung
------------

Das Industrial Dual AC In :ref:`Bricklet <primer_bricklets>` kann dazu genutzt werden
um die Eigenschaften von :ref:`Bricks <primer_bricks>` um zwei Eingänge zur Erkennung
von 230VAC Netzspannung zu erweitern. Der Zustand jedes Eingangs wird mittels einer
LED visualisiert.

Das Bricklet kann genutzt werden um zu Erkennen ob ein Leiter 230VAC Netzspannung führt.

.. warning::
 Die Anschlüsse und Kontakte des Bricklets sind nicht isoliert. Daher sollte dieses Bricklet
 in ein Gehäuse verbaut werden um eine Berührung auszuschließen. Das Berühren der Kontakte
 ist bei Netzspannung potentiell lebensgefährlich!

Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Eingangswiderstand                  249k Ohm (Optokopplereingang mit 249k Serienwiderstand
Stromverbrauch                      50mW (10mA bei 5V)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                             29g
==================================  ============================================================


Ressourcen
----------

* HCPL2731 Optokoppler (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/raw/master/datasheets/HCPL2731.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/raw/master/hardware/industrial-dual-ac-in-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_ac_in_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-ac-in-bricklet/zipball/master>`__)
* 3D Model (`Online ansehen <https://a360.co/3nvkxgh>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_in/industrial-dual-ac-in.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_in/industrial-dual-ac-in.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das nachfolgende Foto stellt die Anschlussmöglichkeiten des Industrial Dual AC In Bricklets dar.
Es können zwei Phasen (L) angeschlossen und überwacht werden. Diese verfügen über einen gemeinsamen Neutral-Anschluss (N),
der über zwei Klemmen erreichbar ist.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_in_caption_front_and_top_800.jpg
   :scale: 100 %
   :alt: Industrial Dual AC In Bricklet Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_in_caption_front_and_top_1200.jpg


.. _industrial_dual_ac_in_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert, sollte das Bricklet im Brick Viewer angezeigt werden.

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

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte Beschreibung.

.. include:: Industrial_Dual_AC_in_hlpi.table
