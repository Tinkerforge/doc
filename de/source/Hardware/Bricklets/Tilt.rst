
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Tilt Bricklet
:shoplink: ../../../shop/bricklets/tilt-bricklet.html

.. include:: Tilt.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _tilt_bricklet:

Tilt Bricklet
=============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_tilt_tilted_[?|?].jpg           Tilt Bricklet
	Bricklets/bricklet_tilt_vertical_[?|?].jpg         Tilt Bricklet
	Bricklets/bricklet_tilt_horizontal_[?|?].jpg       Tilt Bricklet
	Bricklets/bricklet_tilt_tilted_back_[?|?].jpg      Tilt Bricklet
	Cases/bricklet_tilt_case_tilted_front_[?|?].jpg    Tilt Bricklet im Gehäuse
	Bricklets/bricklet_tilt_brickv_[100|].jpg          Tilt Bricklet im Brick Viewer
	Dimensions/tilt_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Erkennt Neigung des Bricklets (Neigungsschalter offen/geschlossen)
* Erkennt ob Bricklet vibriert


.. _tilt_bricklet_description:

Beschreibung
------------

Das Tilt :ref:`Bricklet <primer_bricklets>` ist mit einem
Neigungsschalter ausgestattet. :ref:`Bricks <primer_bricks>` können somit 
erkennen ob das Bricklet aktuell geneigt ist oder ob es vibriert.

Es ist möglich Events zu konfigurieren die automatisch ausgelöst werden 
wenn sich der Status des Tilt Bricklets ändert.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 15mm (0,98 x 0,59 x 0,59")
Gewicht                           3g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/tilt-bricklet/raw/master/hardware/tilt-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/tilt_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/tilt-bricklet/zipball/master>`__)


.. _tilt_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun der aktuelle Status
des Tilt Bricklet angezeigt.

.. image:: /Images/Bricklets/bricklet_tilt_brickv.jpg
   :scale: 100 %
   :alt: Tilt Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_tilt_brickv.jpg

|test_pi_ref|

.. _tilt_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Tilt Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-tilt-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_tilt_case_tilted_front_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Tilt Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_tilt_case_tilted_front_1000.jpg

.. include:: Tilt.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/tilt_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Tilt Bricklet
   :align: center
   :target: ../../_images/Exploded/tilt_exploded.png

|bricklet_case_hint|


.. _tilt_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Tilt_hlpi.table
