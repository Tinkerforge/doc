
:shoplink: ../../../shop/bricklets/industrial-digital-in-4-v2-bricklet.html

.. include:: Industrial_Digital_In_4_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_in_4_v2_bricklet:

Industrial Digital In 4 Bricklet 2.0
====================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_digital_in_4_v2_tilted_[?|?].jpg           Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_tilted2_[?|?].jpg          Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_side_[?|?].jpg             Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_top_[?|?].jpg              Industrial Digital In 4 Bricklet 2.0
	Cases/bricklet_industrial_digital_in_4_v2_case_[?|?].jpg                 Industrial Digital In 4 Bricklet 2.0 im Gehäuse
	Cases/bricklet_industrial_digital_in_4_v2_case2_[?|?].jpg                Industrial Digital In 4 Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_industrial_digital_in_4_v2_brickv_[100|].jpg          Industrial Digital In 4 Bricklet 2.0 im Brick Viewer
	Dimensions/industrial_digital_in_4_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 4 digitale Eingänge 
* Eingangsspannung bis zu 36V (DC)
* Galvanisch getrennt


.. _industrial_digital_in_4_v2_bricklet_description:

Beschreibung
------------

Das Industrial Digital In 4 :ref:`Bricklet <primer_bricklets>` 2.0 kann benutzt werden
um :ref:`Bricks <primer_bricks>` mit vier digitalen Eingängen zu erweitern.
Die Eingangsspannung kann bis zu 36 `Volt <https://de.wikipedia.org/wiki/Volt>`__ (DC) betragen.
Die galvanische Trennung der Eingänge erlaubt eine Benutzung ohne direkte elektrische
Verbindung, so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit
gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüber hinaus ist eine Nutzung in Bereichen,
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_industrial_digital_in_4_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_industrial_digital_in_4_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_industrial_digital_in_4_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  =============================================================
Eigenschaft                       Wert
================================  =============================================================
Stromverbrauch                    28mW (5.6mA bei 5V)
--------------------------------  -------------------------------------------------------------
--------------------------------  -------------------------------------------------------------
Eingangstyp                       Vier opto-gekoppelte Eingänge (4,7kΩ Vorwiderstand enthalten)
Eingangsstrom                     Abhängig von der Eingangsspannung: ca. 1mA/5V, ca. 5mA/24V
Maximale Eingangsspannung         36V (DC)
Low Level Spannung                0-2V
High Level Spannung               3-36V
Isolation                         5000Vrms (Optokoppler Datenblattangabe)
--------------------------------  -------------------------------------------------------------
--------------------------------  -------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8.6g
================================  =============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-v2-bricklet/raw/master/hardware/industrial-digital-in-4-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_digital_in_4_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rG0jVB>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_digital_in_4_v2/industrial-digital-in-4-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_digital_in_4_v2/industrial-digital-in-4-v2.FCStd>`__)


.. _industrial_digital_in_4_v2_bricklet_connectivity:

Anschlussmöglichkeiten
----------------------

Das Industrial Digital In 4 Bricklet 2.0 besitzt eine 8 Pol Anschlussklemme. 
Diese führt die vier Eingänge nach außen. Jeder Eingang ist mit einer LED
innerhalb des Optokopplers verbunden. Um einen Eingang zu nutzen ist 
dieser wie folgt zu beschalten:

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_v2_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet 2.0 Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_v2_caption_1200.jpg


.. _industrial_digital_in_4_v2_bricklet_leds:

Kanal Status LEDs
-------------------

Das Bricklet verfügt über eine standard Status-LED und vier weitere LEDs
(jeweils eine für jeden Eingang).

Standardmäßig zeigen die Status-LEDs den jeweiligen Zustand des Eingangs an.
Die Funktion der LEDs kann auch per API geändert werden.

.. _industrial_digital_in_4_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der aktuelle Zustand der Eingänge angezeigt 
werden. Ist nichts mit dem Bricklet verbunden, so sollten alle Eingänge logisch "low" sein.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_v2_brickv.jpg

|test_pi_ref|


.. _industrial_digital_in_4_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Digital In 4 Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_digital_in_4_v2_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Digital In 4 Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_digital_in_4_v2_case_1000.jpg

.. include:: Industrial_Digital_In_4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Digital In 4 Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_digital_in_4_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Digital_In_4_V2_hlpi.table
