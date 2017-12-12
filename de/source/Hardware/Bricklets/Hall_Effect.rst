
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Hall Effect Bricklet
:shoplink: ../../../shop/bricklets/hall-effect-bricklet.html

.. include:: Hall_Effect.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _hall_effect_bricklet:

Hall Effect Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_hall_effect_tilted_[?|?].jpg           Hall Effect Bricklet
	Bricklets/bricklet_hall_effect_vertical_[?|?].jpg         Hall Effect Bricklet
	Bricklets/bricklet_hall_effect_horizontal_[?|?].jpg       Hall Effect Bricklet
	Bricklets/bricklet_hall_effect_tilted_back_[?|?].jpg      Hall Effect Bricklet
	Bricklets/bricklet_hall_effect_brickv_[100|].jpg          Hall Effect Bricklet im Brick Viewer
	Dimensions/hall_effect_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Detektiert Magnetfelder
* Zählt das Auftreten und Verschwinden eines Magnetfelds
* Kann genutzt werden um einen Wasser-/Stromzähler auszulesen


.. _hall_effect_bricklet_description:

Beschreibung
------------

Das Hall Effect :ref:`Bricklet <primer_bricklets>` kann die Präsenz
eines Magnetfelds detektieren. Es zählt das Auftreten und Verschwinden eines
Magnetfelds und kann von :ref:`Bricks <primer_bricks>` genutzt werden, um z.B. 
die Geschwindigkeit eines Rades, an dem ein Magnet befestigt ist, mit bis zu 
13Hz zu messen.

Beispielanwendungen:

* Erkennung ob eine Tür geöffnet oder geschlossen ist
* Auslesen eines Wasser-/Stromzählers

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            AH180N
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Funktionsweise                    Omnipolar (Nord- und Südpol werden detektiert)
Auslösepunkt                      -35/35 Gauss
Freigabepunkt                     -25/25 Gauss
Abtastrate                        8Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* AH180N Datenblatt (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/datasheets/AH180N.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/hardware/hall-effect-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hall_effect_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BEB8sU>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/hall_effecthall_effect.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/hall_effect/hall_effect.FCStd>`__)


.. _hall_effect_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird ein Magnetfeld erkannt. Zum Testen
kann zum Beispiel ein Magnet verwendet werden, der an dem Bricklet vorbei geführt wird.

.. image:: /Images/Bricklets/bricklet_hall_effect_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_brickv.jpg

|test_pi_ref|


.. _hall_effect_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Hall_Effect_hlpi.table
