
:shoplink: ../../../shop/bricklets/dual-button-v2-bricklet.html

.. include:: Dual_Button_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dual_button_v2_bricklet:

Dual Button Bricklet 2.0
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dual_button_v2_tilted_[?|?].jpg           Dual Button Bricklet 2.0
	Bricklets/bricklet_dual_button_v2_tilted2_[?|?].jpg          Dual Button Bricklet 2.0
	Bricklets/bricklet_dual_button_v2_top_[?|?].jpg              Dual Button Bricklet 2.0
	Cases/bricklet_dual_button_v2_case_[100|600].jpg             Dual Button Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_dual_button_v2_brickv_[100|].jpg          Dual Button Bricklet 2.0 im Brick Viewer
	Dimensions/dual_button_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Zwei Taster mit eingebauten blauen LEDs
* Auto-Toggle der LEDs möglich


.. _dual_button_v2_bricklet_description:

Beschreibung
------------

Das Dual Button :ref:`Bricklet <primer_bricklets>` 2.0 ist mit zwei
Drucktastern ausgestattet und kann :ref:`Bricks <primer_bricks>` um diese 
erweitern. Beide Taster haben eine eingebaute blaue LED. Der
aktuelle Zustand der Taster (gedrückt/nicht gedrückt) und der LEDs (an/aus) kann
jederzeit ausgelesen werden. Es ist möglich die LEDs selbst an/aus zu schalten
sowie Auto-Toggle zu aktivieren. Im Auto-Toggle Modus werden die LEDs
automatisch bei jedem Tastendruck umgeschaltet.

Es ist auch möglich Events zu nutzen. Dadurch kann auf einen
Tastendruck reagiert werden ohne zu pollen.

Das Dual Button Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_dual_button_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_dual_button_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_dual_button_v2_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    27mW (5.4mA bei 5V) + 3mW pro aktiver LED
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Taster Typ                        Drucktaster mit LED
Taster Betätigungskraft           150gf
Taster Bewegungsdistanz           2,5mm
LED Farbe                         Blau
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 20 x 10mm (1,77 x 0,79 x 0,39")
Gewicht                           5,5g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/dual-button-v2-bricklet/raw/master/hardware/dual-button-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_button_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-button-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2LOtykd>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/dual_button_v2/dual-button-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/dual_button_v2/dual-button-v2.FCStd>`__)


.. _dual_button_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun Tastendrücke beobachtet 
werden sowie die Zustände der LEDs verändert werden.

.. image:: /Images/Bricklets/bricklet_dual_button_v2_brickv.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_v2_brickv.jpg

|test_pi_ref|


.. _dual_button_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Dual Button Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-dual-button-v2-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_dual_button_v2_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Dual Button Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_dual_button_v2_case_1000.jpg

.. include:: Dual_Button_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/dual_button_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Dual Button Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/dual_button_v2_exploded.png

|bricklet_case_hint|


.. _dual_button_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Dual_Button_V2_hlpi.table
