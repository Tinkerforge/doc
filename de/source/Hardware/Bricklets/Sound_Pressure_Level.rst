
:shoplink: ../../../shop/bricklets/sound-pressure-level-bricklet.html

.. include:: Sound_Pressure_Level.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _sound_pressure_level_bricklet:

Sound Pressure Level Bricklet
=============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_sound_pressure_level_tilted_[?|?].jpg           Sound Pressure Level Bricklet
	Bricklets/bricklet_sound_pressure_level_bottom_[?|?].jpg           Sound Pressure Level Bricklet
	Bricklets/bricklet_sound_pressure_level_top_[?|?].jpg              Sound Pressure Level Bricklet
	Cases/bricklet_sound_pressure_level_case_[?|?].jpg                 Sound Pressure Level Bricklet im Gehäuse
	Cases/bricklet_sound_pressure_level_case_hand_[?|?].jpg            Sound Pressure Level Bricklet im Gehäuse
	Bricklets/bricklet_sound_pressure_level_brickv_[100|].jpg          Sound Pressure Level Bricklet im Brick Viewer
	Dimensions/sound_pressure_level_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst den Schalldruckpegel in dB(A/B/C/D/Z) und ITU-R 468
* Misst das Spektrogramm mit bis zu 512 Gruppen und bis zu 80 Samples pro Sekunde
* Frequenzbereich 40Hz bis 40960Hz
* Rauschpegel 30dB, Maximum 120dB


.. _sound_pressure_level_bricklet_description:

Beschreibung
------------

Mit dem Sound Pressure Level :ref:`Bricklet <primer_bricklets>` können :ref:`Bricks <primer_bricks>` den
`Schalldruckpegel <https://de.wikipedia.org/wiki/Schalldruckpegel>`__ und das Geräusch-
`Spektrum <https://de.wikipedia.org/wiki/Spektrogramm>`__ messen. Der gemessene Schalldruckpegel kann als
`bewerteter Schalldruckpegel <https://de.wikipedia.org/wiki/Bewerteter_Schalldruckpegel>`__ mittels
A, B, C, D, ITU-R 468 und flacher Gewichtung (Z) gewichtet werden.

Das Bricklet kann genutzt werden um die Lautstärke zum Beispiel von Musik, Baustellen, Straßengeräuschen
und von anderen Umgebungsgeräuschen in verschiedenen Gewichtungen zu messen. Zusätzlich ist es möglich die 
Frequenzzusammensetzung zu bestimmen (Spektrum).

Das Sound Pressure Level Bricklet hat einen 7 Pol Bricklet Stecker und wird mit einem ``7p-10p`` Bricklet 
Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    50mW (10mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
dB(X) Genauigkeit*                +-5dB, +-5% Maximaler Full-scale Error
Messbereich                       30dB - 120dB
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 6mm (0.98 x 0.98 x 0.24")
Weight                            2.6g
================================  ============================================================

\* Gültig für den Bereich von 100Hz bis 8kHz. Für Details siehe :ref:`unten <sound_pressure_level_bricklet_genauigkeit>`.

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/sound-pressure-level-bricklet/raw/master/hardware/sound-pressure-level-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/sound_pressure_level_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/sound-pressure-level-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2IdCjzd>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/sound_pressure_level/sound-pressure-level.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/sound_pressure_level/sound-pressure-level.FCStd>`__)

.. _sound_pressure_level_bricklet_genauigkeit:

Genauigkeit und Kalibrierung
----------------------------

Das Bricklet ist gegen ein Schallpegelmessgerät mit 1.5dB Genauigkeit kalibriert.
Das verwendete MEMS Mikrofon hat einen Frequenzgang mit bis zu 1.5dB Abweichung
im Bereich von 100Hz bis 8kHz.

Zu den 1.5dB haben wir weitere 2dB für kleine Abweichungen in der Befestigung 
und in der Mikrofon-Bohrung addiert um so auf +-5dB zu kommen.

Für Frequenzen von 8kHz bis 20kHz erhöht sich die Abweichung des Frequenzganges
deutlich. Diesen Bereich haben wir anhand der im
ICS43432 Datenblattes angegebenen Werte kompensiert. Wir können aber keine 
Garantien dazu geben. Ein Vergleich mit anderen professionellen Schallpegelmessgeräten
liefert keine Information dazu, da diese meist nur bis 8kHz messen.

Zusätzlich ist der Frequenzgang zwischen zwei Mikrofonen verschieden. Um dieses
zu kompensieren müsste jedes einzelne Bricklet in einer reflexionsfreien Schallkammer
vermessen werden. Dies ist für ein Bricklet nicht ökonomisch. Diese Abweichung wird von
uns mit einem zusätzlichen maximalen 5% Full-Scale Error berücksichtigt.

Unsere Tests ergaben ein Grundrauschen von ca 30dB und eine maximal messbare Lautstärke
von 120dB.

Das Bricklet wurde nicht in Bezug auf IEC 61252:1993 Class 1 oder 2 
oder IEC 61672 Teil 2 getestet und besitzt keine "Mustergenehmigung".

Als Daumenregel gilt: Das Bricklet erbringt Leistungen wie andere Schallpegelmessgeräte im 
200€ Preisbereich. Das Bricklet sollte nicht genutzt werden, wenn Gesundheits- oder 
Sicherheitsauswirkungen zu befürchten sind!

.. _sound_pressure_level_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte nun das Spektrum und der Dezibel-Wert angezeigt werden.

.. image:: /Images/Bricklets/bricklet_sound_pressure_level_brickv.jpg
   :scale: 100 %
   :alt: Sound Pressure Level Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_pressure_level_brickv.jpg

|test_pi_ref|


.. _sound_pressure_level_bricklet_beispiele:

Beispiele
---------

Gitarrenmusik:

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/sound_pressure_level_guitar.mp4" type="video/mp4">
	  <source src="../../_images/Videos/sound_pressure_level_guitar.ogg" type="video/ogg">
	  <source src="../../_images/Videos/sound_pressure_level_guitar.webm" type="video/webm">
	</video>


Sich ändernder Sinuston:

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/sound_pressure_level_moving_sine_wave.mp4" type="video/mp4">
	  <source src="../../_images/Videos/sound_pressure_level_moving_sine_wave.ogg" type="video/ogg">
	  <source src="../../_images/Videos/sound_pressure_level_moving_sine_wave.webm" type="video/webm">
	</video>



.. _sound_pressure_level_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Sound Pressure Level Bricklet 
<https://www.tinkerforge.com/de/shop/cases/case-sound-pressure-level-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_sound_pressure_level_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Sound Pressure Level Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_sound_pressure_level_case_1000.jpg

.. include:: Sound_Pressure_Level.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/sound_pressure_level_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Sound Pressure Level Bricklet
   :align: center
   :target: ../../_images/Exploded/sound_pressure_level_exploded.png

|bricklet_case_hint|


.. _sound_pressure_level_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Sound_Pressure_Level_hlpi.table
