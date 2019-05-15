
:DISABLED_shoplink: ../../../shop/bricklets/hall-effect-v2-bricklet.html

.. include:: Hall_Effect_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _hall_effect_v2_bricklet:

Hall Effect Bricklet 2.0
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_hall_effect_v2_tilted_[?|?].jpg           Hall Effect Bricklet 2.0
	Bricklets/bricklet_hall_effect_v2_horizontal_[?|?].jpg       Hall Effect Bricklet 2.0
	Bricklets/bricklet_hall_effect_v2_master_[100|600].jpg       Hall Effect Bricklet 2.0 mit Master Brick
	Cases/bricklet_hall_effect_v2_case_[100|600].jpg             Hall Effect Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_hall_effect_v2_brickv_[100|].jpg          Hall Effect Bricklet 2.0 im Brick Viewer
	Dimensions/hall_effect_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst magnetische Flussdichte zwischen -7mT und 7mT
* Zähler mit konfigurierbaren Grenzbereich, bipolar und unipolar
* Kann mit Frequenzen bis zu 10kHz zählen


.. _hall_effect_v2_bricklet_description:

Beschreibung
------------

Das Hall Effect :ref:`Bricklet <primer_bricklets>` 2.0 kann die 
`magnetische Flussdichte <https://de.wikipedia.org/wiki/Magnetische_Flussdichte>`__
zwischen -7mT und 7mT (`Milli-Tesla <https://de.wikipedia.org/wiki/Tesla_(Einheit)>`__) bestimmen.
Es zählt das Auftreten und Verschwinden eines
Magnetfelds und kann von :ref:`Bricks <primer_bricks>` genutzt werden, um z.B. 
die Geschwindigkeit eines Rades, an dem ein Magnet befestigt ist, mit bis zu 
10kHz zu messen.

Für den Zähler kann ein unterer und oberer Grenzbereich sowie eine Enprellzeit
eingestellt und auf die jeweilige Anwendung angepasst werden.

Beispielanwendungen sind:

* Erkennen ob eine Tür offen/geschlossen ist
* Auslesen eines Wasser-/Stromzählers
* Umdrehungszahl eines Motors messen

Das Hall Effect Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            DRV5053
Stromverbrauch                    59mW (11.8mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Funktionsweise                    Omnipolar (Nord- und Südpol werden detektiert)
Messbereich                       -7mT to 7mT
Zähler-Triggerpunkt               Konfigurierbar (unipolar und bipolar)
Zähler-Abtastfrequenz             10kHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* DRV5053 Datenblatt (`Download <https://github.com/Tinkerforge/hall-effect-v2-bricklet/raw/master/datasheets/DRV5053.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/hall-effect-v2-bricklet/raw/master/hardware/hall-effect-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hall_effect_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hall-effect-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2VBKu39>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/hall-effect-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/hall-effect-v2.FCStd>`__)


.. _hall_effect_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert kann jetzt die magnetische
Flussdichte abgelese werden. Zum Testen kann ein Magnet in die
nähe des Bricklets geführt werden.

.. image:: /Images/Bricklets/bricklet_hall_effect_v2_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_v2_brickv.jpg

|test_pi_ref|



.. _hall_effect_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Hall_Effect_V2_hlpi.table
