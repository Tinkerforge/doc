:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Motorized Linear Poti Bricklet
:FIXME_shoplink: ../../../shop/bricklets/motorized-linear-poti-bricklet.html

.. include:: Motorized_Linear_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _motorized_linear_poti_bricklet:

Motorized Linear Poti Bricklet
==============================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_motorized_linear_poti_tilted_[?|?].jpg           Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_horizontal_[?|?].jpg       Motorized Linear Poti Bricklet
	Bricklets/bricklet_motorized_linear_poti_master_[100|600].jpg       Motorized Linear Poti Bricklet mit Master Brick
	Cases/bricklet_motorized_linear_poti_case_[100|600].jpg             Motorized Linear Poti Bricklet im Gehäuse
	Bricklets/bricklet_motorized_linear_poti_brickv_[100|].jpg          Motorized Linear Poti Bricklet im Brick Viewer
	Dimensions/motorized_linear_poti_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Schiebepotentiometer mit 100mm Weg
* Knopfposition kann vom Nutzer und vom integrierten Motor gesteuert werden
* Keine zusätzliche Stromversorgung notwendig
* Automatische Kalibrierung


.. _motorized_linear_poti_bricklet_description:

Beschreibung
------------

Das Motorized Linear Poti :ref:`Bricklet <primer_bricklets>` ist mit einem 100mm
`Schiebepotentiometer <https://de.wikipedia.org/wiki/Potentiometer>`__ ausgestattet das
von dem integrierten Motor gesteuert werden kann. Das Bricklet kann mit 
:ref:`Bricks <primer_bricks>` verbunden werden.

Die Position des Potentiometers reicht von 0 (Schiebeknopf unten) bis zu 100
(Schiebeknopf oben). Der Nutzer kann die Position vom Knopf ändern, die Position
kann aber auch vom integrierten Motor geändert werden.

Das Potentiometer kann konfiguriert werden, die Position zu halten. In diesem Fall
fährt das Potentiometer selbstständig wieder zu der Ausgangsposition zurück, wenn der
Nutzer die Position ändert. Wenn das Potentiometer nicht dazu konfiguriert wurde die Position
zu halten, lässt sich der Schiebeknopf nach dem Anfahren der Position bewegen und verändert
seine Position von selbst nicht.


Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Stromverbrauch                        TBDmA
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Schiebeweg                            100mm

Befestigungsgewinde am Potentiometer  M3
Abstand zwischen den Gewinden         120mm
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               145 x 20 x 28mm (5.70 x 0.79 x 1.10")
Gewicht                               67g
====================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/motorized-linear-poti-bricklet/raw/master/hardware/motorized-linear-poti-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/motorized_linear_poti_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/motorized-linear-poti-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2ztZjZo>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/motorized_linear_poti/motorized-poti.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/motorized_linear_poti/motorized-poti.FCStd>`__)


.. _motorized_linear_poti_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert kann nun die Position des Potentiometers
geändert werden.

.. image:: /Images/Bricklets/bricklet_motorized_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Motorized Linear Poti Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motorized_linear_poti_brickv.jpg

|test_pi_ref|


.. _motorized_linear_poti_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Motorized Linear Poti Bricklet 
	<https://www.tinkerforge.com/de/shop/cases/case-motorized-linear-poti-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_motorized_linear_poti_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Motorized Linear Poti Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_motorized_linear_poti_case_1000.jpg

	.. include:: Motorized_Linear_Poti.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/motorized_linear_poti_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Motorized Linear Poti Bricklet
	   :align: center
	   :target: ../../_images/Exploded/motorized_linear_poti_exploded.png

	|bricklet_case_hint|


.. _motorized_linear_poti_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Motorized_Linear_Poti_hlpi.table
