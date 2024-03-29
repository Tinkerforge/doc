
:shoplink: ../../../shop/bricklets/distance-ir-10-80cm-v2-bricklet.html

.. include:: Distance_IR_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_ir_v2_bricklet:

Distance IR Bricklet 2.0
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_ir_v2_tilted_[?|?].jpg           Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_tilted2_[?|?].jpg          Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_top_[?|?].jpg              Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_side_[?|?].jpg             Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_bottom_[?|?].jpg           Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_brickv_[100|].jpg          Distance IR Bricklet 2.0 im Brick Viewer
	Dimensions/distance_ir_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Entfernungen mit IR Licht
* Sensor kann ausgetauscht werden
* Unterstützte Messbereiche: 4-30cm, 10-80cm und 20-150cm


.. _distance_ir_v2_bricklet_description:

Beschreibung
------------

Mit dem Distance IR :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` Entfernungen messen.
Dieses Bricklet wird auf der Rückseite von analogen
`Sharp <https://www.sharpsma.com>`__ Infrarot Entfernungssensoren befestigt.
Nachdem der verbundene Sensor konfiguriert wurde, können die gemessenen
Entfernungen direkt in Millimeter ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf veränderte Distanzmessung zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Im Shop sind Infrarot Sensoren für verschiedene Messbereiche verfügbar:

* `Infrarot Sensor 4-30cm GP2Y0A41SK0F
  <https://www.tinkerforge.com/de/shop/bricklets/distance-ir-4-30cm-v2-bricklet.html>`__
* `Infrarot Sensor 10-80cm GP2Y0A21YK0F
  <https://www.tinkerforge.com/de/shop/bricklets/distance-ir-10-80cm-v2-bricklet.html>`__
* `Infrarot Sensor 20-150cm GP2Y0A02YK0F
  <https://www.tinkerforge.com/de/shop/bricklets/distance-ir-20-150cm-v2-bricklet.html>`__

Typischerweise werden diese Sensoren in der Robotik genutzt um Entfernungen
zu messen, zur Lokalisierung oder zur Kartenerstellung. Sie sind aber noch
für viele andere Anwendungen genutzt werden. Zum Beispiel können diese Sensoren
wie eine Lichtschranke benutzt werden um zum Beispiel den Zugang zu einem
Raum zu kontrollieren.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_distance_ir_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_distance_ir_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_distance_ir_v2_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  ===========================================================================
Eigenschaft                       Wert
================================  ===========================================================================
Sensor                            GP2Y0A41SK0F oder GP2Y0A21YK0F oder GP2Y0A02YK0F
Stromverbrauch                    110mW (22mA bei 5V)
--------------------------------  ---------------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------------
Entfernungen                      Abhängig vom angeschlossenen IR Sensor:

                                  * GP2Y0A41SK0F:  4cm -  30cm (1,57" - 11,81")
                                  * GP2Y0A21YK0F: 10cm -  80cm (3,94" - 31,50")
                                  * GP2Y0A02YK0F: 20cm - 150cm (7,87" - 59,06")
--------------------------------  ---------------------------------------------------------------------------
--------------------------------  ---------------------------------------------------------------------------
Abmessungen (B x T x H)           45 x 13 x 5mm (1,76 x 0,51 x 0,19")*, passt auf Rückseite des Sensors
Gewicht                           8g
================================  ===========================================================================

\* ohne Kabel und Sensor


Ressourcen
----------

* GP2Y0A41SK0F Datenblatt (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/datasheets/GP2Y0A41SK0F.pdf>`__)
* GP2Y0A21YK0F Datenblatt (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/datasheets/GP2Y0A21YK0F.pdf>`__)
* GP2Y0A02YK0F Datenblatt (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/datasheets/GP2Y0A02YK0F.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/hardware/distance-ir-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/distance_ir_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2LPlBes>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/distance_ir_v2/distance-ir-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/distance_ir_v2/distance-ir-v2.FCStd>`__)


.. _distance_ir_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Distanz des Sensors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Distanz wieder.

.. image:: /Images/Bricklets/bricklet_distance_ir_v2_brickv.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_v2_brickv.jpg

|test_pi_ref|


.. _distance_ir_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Distance IR Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-distance-ir-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_distance_ir_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Distance IR Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_distance_ir_case_1000.jpg

.. include:: Distance_IR_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/distance_ir_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Distance IR Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/distance_ir_v2_exploded.png

|bricklet_case_hint|


.. _distance_ir_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Distance_IR_V2_hlpi.table
