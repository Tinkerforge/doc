
:shoplink: ../../../shop/bricklets/industrial-digital-out-4-bricklet.html

.. include:: Industrial_Digital_Out_4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_out_4_bricklet:

Industrial Digital Out 4 Bricklet
=================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_digital_out_4_tilted_[?|?].jpg           Industrial Digital Out 4 Bricklet
	Bricklets/bricklet_industrial_digital_out_4_vertical_[?|?].jpg         Industrial Digital Out 4 Bricklet
	Bricklets/bricklet_industrial_digital_out_4_horizontal_[?|?].jpg       Industrial Digital Out 4 Bricklet
	Bricklets/bricklet_industrial_digital_out_4_setup_[?|?].jpg            Industrial Digital Out 4 Bricklet Setup
	Cases/bricklet_industrial_case_[100|600].jpg                           Industrial Digital Out 4 in Case
	Bricklets/bricklet_industrial_digital_out_4_brickv_[100|].jpg          Industrial Digital Out 4 Bricklet in Brick Viewer
	Dimensions/industrial_digital_out_4_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 digitale Ausgänge
* Ausgangsspannung bis zu 36V
* Galvanisch getrennt
* Gruppierbar


.. _industrial_digital_out_4_bricklet_description:

Beschreibung
------------

Das Industrial Digital Out 4 :ref:`Bricklet <primer_bricklets>` kann benutzt werden
um :ref:`Bricks <primer_bricks>` mit vier digitalen Ausgänge zu erweitern.
Die Ausgangsspannung kann bis zu 36 `Volt <https://de.wikipedia.org/wiki/Volt>`__ betragen.
Die galvanische Trennung der Ausgänge erlaubt eine Benutzung ohne direkte elektrische
Verbindung, so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit
gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüber hinaus ist eine Nutzung in Bereichen,
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.

Wenn mehr als vier Ausgänge benötigt werden kann ein weiteres Industrial Digital Out 4
Bricklet mit angeschlossen und gruppiert werden. Anschließend ist es möglich
8 Ausgänge simultan zu schreiben anstatt zwei mal 4 Ausgänge hintereinander zu schreiben.
Die Gruppierung kann nur pro Brick erfolgen, so dass an einem Master Brick
maximal 4, an anderen Bricks 2 Industrial Bricklets gruppiert werden können.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    2mA (pro aktivem Ausgang)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Externe Spannungsversorgung       Bis zu 36V
Ausgangstyp                       Vier Operationsverstärker-Ausgänge
Maximaler Ausgangsstrom           25mA (pro Ausgang)
Isolation                         5000Vrms (Optokoppler Datenblattangabe)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 14mm (1,57 x 1,57 x 0,55")
Gewicht                           10g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-bricklet/raw/master/hardware/industrial-digital-out-4-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_digital_out_4_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BcCVER>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_digital_out_4/industrial-digital-out-4.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_digital_out_4/industrial-digital-out-4.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Digital Out 4 Bricklet besitzt eine 8 Pol Anschlussklemme.
Das folgende Bild stellt die Anschlussmöglichkeiten dar:

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_caption_1200.jpg


.. _industrial_digital_out_4_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Verbinde zusätzlich eine Spannungsquelle mit dem Bricklet um es zu Versorgen
und eine Last. Für diesen Test schließen wir eine Batterie und eine LED an
(siehe nachfolgendes Bild).

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet Setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_setup_1200.jpg

|test_tab|

Anschließend sollte die LED über den Brick Viewer geschaltet werden können.

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_brickv.jpg

|test_pi_ref|

.. _industrial_digital_out_4_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Digital Out 4 Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Digital Out 4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Digital_Out_4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Digital Out 4 Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_digital_out_4_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Digital_Out_4_hlpi.table
