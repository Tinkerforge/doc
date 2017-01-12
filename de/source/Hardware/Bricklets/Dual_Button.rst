
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Dual Button Bricklet
:shoplink: ../../../shop/bricklets/dual-button-bricklet.html

.. include:: Dual_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _dual_button_bricklet:

Dual Button Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dual_button_tilted_[?|?].jpg           Dual Button Bricklet
	Bricklets/bricklet_dual_button_vertical_[?|?].jpg         Dual Button Bricklet
	Bricklets/bricklet_dual_button_horizontal_[?|?].jpg       Dual Button Bricklet
	Bricklets/bricklet_dual_button_tilted_back_[?|?].jpg      Dual Button Bricklet
	Bricklets/bricklet_dual_button_brickv_[100|].jpg          Dual Button Bricklet im Brick Viewer
	Dimensions/dual_button_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Zwei Taster mit eingebauten blauen LEDs
* Auto-Toggle der LEDs möglich


.. _dual_button_bricklet_description:

Beschreibung
------------

Das Dual Button :ref:`Bricklet <primer_bricklets>` ist mit zwei
Drucktastern ausgestattet und kann :ref:`Bricks <primer_bricks>` um diese 
erweitern. Beide Taster haben eine eingebaute blaue LED. Der
aktuelle Zustand der Taster (gedrückt/nicht gedrückt) und der LEDs (an/aus) kann
jederzeit ausgelesen werden. Es ist möglich die LEDs selbst an/aus zu schalten
sowie Auto-Toggle zu aktivieren. Im Auto-Toggle Modus werden die LEDs
automatisch bei jedem Tastendruck umgeschaltet.

Es ist auch möglich Events zu nutzen. Dadurch kann auf einen
Tastendruck reagiert werden ohne zu pollen.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    1mA pro leuchtender LED
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Taster Typ                        Drucktaster mit LED
Taster Betätigungskraft           150gf
Taster Bewegungsdistanz           2,5mm
LED Farbe                         Blau
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 20 x 10mm (1,77 x 0,79 x 0,39")
Gewicht                           6g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/dual-button-bricklet/raw/master/hardware/dual-button-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_button_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-button-bricklet/zipball/master>`__)


.. _dual_button_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun Tastendrücke beobachtet 
werden sowie die Zustände der LEDs verändert werden.

.. image:: /Images/Bricklets/bricklet_dual_button_brickv.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_brickv.jpg

|test_pi_ref|


.. _dual_button_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Dual_Button_hlpi.table
