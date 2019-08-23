
:shoplink: ../../../shop/bricklets/piezo-speaker-v2-bricklet.html

.. include:: Piezo_Speaker_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _piezo_speaker_v2_bricklet:

Piezo Speaker Bricklet 2.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_piezo_speaker_v2_tilted_[?|?].jpg           Piezo Speaker Bricklet 2.0
	Bricklets/bricklet_piezo_speaker_v2_top_[?|?].jpg              Piezo Speaker Bricklet 2.0
	Bricklets/bricklet_piezo_speaker_v2_side_[?|?].jpg             Piezo Speaker Bricklet 2.0
	Cases/bricklet_piezo_speaker_v2_case_front_[?|?].jpg           Piezo Speaker Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_piezo_speaker_v2_brickv_[100|].jpg          Piezo Speaker Bricklet 2.0 im Brick Viewer
	Dimensions/piezo_speaker_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Kann einen konfigurierbaren Piepton zwischen 50Hz und 15000Hz erzeugen
* Kann einen einstellbaren Alarm/Sirenen-Ton ausgeben
* Lautstärke ist zwischen 85dB(A) und 110dB(A) konfigurierbar


.. _piezo_speaker_v2_bricklet_description:

Beschreibung
------------

Das Piezo Speaker :ref:`Bricklet <primer_bricklets>` 2.0 kann genutzt werden um mit
:ref:`Bricks <primer_bricks>` Töne mit unterschiedlichen Frequenzen und Lautstäken zu 
erzeugen.

Der verfügbare Frequenzbereich ist 50Hz bis 15000Hz. Die Lautstärke kann zwischen
85dB(A) und 110dB(A) eingestellt werden.

Zusätzlich hat das Bricklet Unterstützung für Alarm und Sirenen-Töne. In diesem Modus
wird ein *sweep* erzeugt der einen Frequenzbereich mit konfigurierbarer
Schrittgröße und Länge abläuft.

Das Piezo Speaker Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Die folgende Audiodatei besteht aus Beispielen von Piep und Alarm-Tönen die mit
einem Piezo Speaker Bricklet 2.0 erzeugt wurden:

.. raw:: html
 
	<audio controls>
	  <source src="../../_images/Videos/bricklet_piezo_speaker_v2_audio.ogg" type="audio/ogg">
	  <source src="../../_images/Videos/bricklet_piezo_speaker_v2_audio.mp3" type="audio/mp3">
	</audio>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Buzzer                            PT-4532PLQ
Stromverbrauch                    55mW (11mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Frequenzbereich                   50Hz - 15000Hz (konfigurierbar)
Lautstärke                        85dB(A) - 110dB(A) @50cm/1kHz (konfigurierbar)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           55 x 45 x 20mm (2.2 x 1.8 x 0.8")
Gewicht                           20g
================================  ============================================================


Ressourcen
----------

* PT-4532PLQ Datenblatt (`Download <https://github.com/Tinkerforge/piezo-speaker-v2-bricklet/raw/master/datasheets/PT-4532PLQ.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/piezo-speaker-v2-bricklet/raw/master/hardware/piezo-speaker-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/piezo_speaker_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/piezo-speaker-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/30jdwD4>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/piezo_speaker_v2/piezo-speaker-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/piezo_speaker_v2/piezo-speaker-v2.FCStd>`__)


.. _piezo_speaker_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun Töne erzeugt werden.

.. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_brickv.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_v2_brickv.jpg

|test_pi_ref|


Lautstärke und Schalldruckpegel
-------------------------------

Das Bricklet hat 11 unterschiedliche Lautstärkenstufen (0 bis 10).

Wir haben den Schalldruckpegel mit dem unten beschriebenen Testaufbau
gemessen. Dazu haben wir den Durchschnitt von drei unterschiedlichen
Schallpegelmessgeräten bei einer Distanz von 50cm bestimmt. Die
eingestellte Frequenz des Piezo Speaker Bricklet 2.0 war 1kHz.

.. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_spl1_800.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_v2_spl1_1200.jpg

Das Resultat ist ein Bereich von 85dB(A) bis 110dB(A):

.. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_spl_bargraph.png
   :scale: 100 %
   :alt: Piezo Speaker Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_v2_spl_bargraph.png

Der Lautstärkenbereich 0-4 kann für Benachrichtigungstöne genutzt werden und
die Lautstärke im Bereich 5-10 ist gut geeignet für laute und nervige Alarm-Töne.

.. warning::
	Hinweis: Bei 110 dB(A) beträgt die empfohlene zulässige Expositionszeit (laut
	`NIOSH und CDC <https://www.cdc.gov/niosh/topics/noise/chart-lookatnoise.html>`__) 
	nur ungefähr 1,5 Minuten!


.. _piezo_speaker_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Piezo Speaker Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-piezo-speaker-v2-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_piezo_speaker_v2_case_front_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Piezo Speaker Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_piezo_speaker_v2_case_front_1000.jpg

.. include:: Piezo_Speaker_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/piezo_speaker_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Piezo Speaker Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/piezo_speaker_v2_exploded.png

|bricklet_case_hint|


.. _piezo_speaker_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Piezo_Speaker_V2_hlpi.table
