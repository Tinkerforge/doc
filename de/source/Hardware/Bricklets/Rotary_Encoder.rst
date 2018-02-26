
:shoplink: ../../../shop/bricklets/rotary-encoder-bricklet.html

.. include:: Rotary_Encoder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _rotary_encoder_bricklet:

Rotary Encoder Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rotary_encoder_tilted_[?|?].jpg               Rotary Encoder Bricklet
	Bricklets/bricklet_rotary_encoder_horizontal_[?|?].jpg           Rotary Encoder Bricklet
	Bricklets/bricklet_rotary_encoder_w_knob_[100|600].jpg           Rotary Encoder Bricklet und Knopf
	Bricklets/bricklet_rotary_encoder_tilted_back_wo_knob_[?|?].jpg  Rotary Encoder Bricklet
	Bricklets/bricklet_rotary_encoder_tilted_wo_knob_[?|?].jpg       Rotary Encoder Bricklet
	Cases/bricklet_rotary_poti_case_shallow_[100|600].jpg            Rotary Encoder Bricklet im Gehäuse
	Bricklets/bricklet_rotary_encoder_brickv_[100|].jpg              Rotary Encoder Bricklet im Brick Viewer
	Dimensions/rotary_encoder_bricklet_dimensions_[100|600].png      Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Rotary Encoder Bricklet ist abgekündigt.
 Als Ersatz wird das :ref:`Rotary Encoder Bricklet 2.0 <rotary_encoder_v2_bricklet>`
 empfohlen.

Features
--------

* 360° Drehgeber / Drehencoder
* Zählt 24 Schritte pro Umdrehung (Schrittwinkel 15°)
* Integrierter Taster


.. _rotary_encoder_bricklet_description:

Beschreibung
------------

Das Rotary Encoder :ref:`Bricklet <primer_bricklets>` erweitert
:ref:`Bricks <primer_bricks>` um einen 360° Encoder. Der Encoder hat 
24 Schritte pro Umdrehung mit "Klick-Haptik" pro Schritt. Der Encoder hat einen 
integrierten Taster (auslösbar indem man auf den Knopf drückt) der genutzt 
werden kann um Menüpunkte o.ä. auszuwählen.

Der Unterschied zwischen dem :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`
und dem Rotary Encoder Bricklet ist, dass der Encoder ohne Begrenzungen gedreht
werden kann.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Anzahl Schritten pro Rotation     24 (Winkel pro Schritt: 15°)
Maximale erkennbare Schritte      bis zu 250 Schritte / Sekunde
Taster Betätigungskraft           200gf
Taster Bewegungsdistanz           0,5mm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 23mm (1,18 x 0,98 x 0,9")*
Gewicht                           5g*
================================  ============================================================

\* ohne Knopf

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/rotary-encoder-bricklet/raw/master/hardware/rotary-encoder-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rotary_encoder_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rotary-encoder-bricklet/zipball/master>`__)


.. _rotary_encoder_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun der aktuelle 
Encoderzählstand angezeigt.

.. image:: /Images/Bricklets/bricklet_rotary_encoder_brickv.jpg
   :scale: 100 %
   :alt: Rotary Encoder Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_encoder_brickv.jpg

|test_pi_ref|

.. _rotary_encoder_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Rotary Encoder Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-rotary-poti-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_rotary_poti_case_shallow_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Rotary Encoder Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_poti_case_shallow_1000.jpg

.. include:: Rotary_Encoder.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Rotary Encoder Bricklet
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|


.. _rotary_encoder_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Rotary_Encoder_hlpi.table
