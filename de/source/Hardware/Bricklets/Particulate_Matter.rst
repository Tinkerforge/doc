
:DISABLED_shoplink: ../../../shop/bricklets/particulate-matter-bricklet.html

.. include:: Particulate_Matter.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _particulate_matter_bricklet:

Particulate Matter Bricklet
===========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_particulate_matter_tilted_[?|?].jpg           Particulate Matter Bricklet
	Bricklets/bricklet_particulate_matter_top_[?|?].jpg              Particulate Matter Bricklet
	Bricklets/bricklet_particulate_matter_front_[?|?].jpg            Particulate Matter Bricklet
	Bricklets/bricklet_particulate_matter_tilted2_[?|?].jpg          Particulate Matter Bricklet
	Cases/bricklet_particulate_matter_case_[?|?].jpg                 Particulate Matter Bricklet im Gehäuse
	Cases/bricklet_particulate_matter_case_side_[?|?].jpg            Particulate Matter Bricklet im Gehäuse
	Dimensions/particulate_matter_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst die Feinstaubkonzentration
* Messungen in µg/m³ für verschiedene Partikelgrößen
* Unterscheidbare Partikelgrößen: PM1.0, PM2.5 and PM10
* Integrierter Lüfter zur Erzeugung eines Luftstroms


.. _particulate_matter_bricklet_description:

Beschreibung
------------

Das Particulate Matter :ref:`Bricklet <primer_bricklets>` kann genutzt werden um die 
Eigenschaften eines :ref:`Bricks <primer_bricks>` um die Möglichkeit Feinstaub zu messen 
zu erweitern.

Das Bricklet unterstützt die Größenklassen PM1.0, PM2.5 und PM10. Zusätzlich ist es möglich
die Anzahl der Partikel in 100ml Luft in den Größen 0,3µm, 0,5µm, 1,0µm, 2,5µm, 5,0µm und 10,0µm.

Das Particulate Matter Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            PMS7003
Stromverbrauch                    388mW (77.6mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Feinstaubkonzentration            PM1.0, PM2.5, PM10
Partikelzählung                   0,3µm, 0,5µm, 1,0µm, 2,5µm, 5,0µm, 10,0µm (in 100ml Luft)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           70 x 40 x 15mm (2,76 x 1,57 x 0,59")
Gewicht                           36,3g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/particulate-matter-bricklet/raw/master/hardware/particulate-matter-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/particulate_matter_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/particulate-matter-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rFjjDp>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/particulate_matter/particulate-matter.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/particulate_matter/particulate-matter.FCStd>`__)


.. _particulate_matter_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun die Feinstaubkonzentration angezeigt.

.. image:: /Images/Bricklets/bricklet_particulate_matter_brickv.jpg
   :scale: 100 %
   :alt: Particulate Matter Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_particulate_matter_brickv.jpg

|test_pi_ref|


.. _particulate_matter_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Particulate Matter Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-particulate-matter-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_particulate_matter_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Particulate Matter Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_particulate_matter_case_1000.jpg

.. include:: Particulate_Matter.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/particulate_matter_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Particulate Matter Bricklet
   :align: center
   :target: ../../_images/Exploded/particulate_matter_exploded.png

|bricklet_case_hint|


.. _particulate_matter_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Particulate_Matter_hlpi.table
