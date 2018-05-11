
:shoplink: ../../../shop/bricklets/motion-detector-v2-bricklet.html

.. include:: Motion_Detector_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _motion_detector_v2_bricklet:

Motion Detector Bricklet 2.0
============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_motion_detector_v2_tilted_[?|?].jpg             Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_side_[?|?].jpg               Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_bottom_[?|?].jpg             Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_top_[?|?].jpg                Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_tilted_black_lense_[?|?].jpg Motion Detector Bricklet 2.0 (schwarze Linse)
	Cases/bricklet_motion_detector_v2_case_built_up_[?|?].jpg          Motion Detector Bricklet 2.0 im Gehäuse
	Cases/bricklet_motion_detector_v2_case_be_built_up_[100|].jpg      Motion Detector Bricklet 2.0 im Gehäuse (schwarz)
	Bricklets/bricklet_motion_detector_v2_brickv_[100|].jpg            Motion Detector Bricklet 2.0 im Brick Viewer
	Dimensions/motion_detector_v2_bricklet_dimensions_[100|600].png    Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Passiver Infrarot Bewegungssensor
* Erkennt Bewegungen in einer Distanz von bis zu 12m (konfigurierbar)
* Hoher Erfassungswinkel (120°)
* Fresnellinse hat konfigurierbare Hintergrundbeleuchtung


.. _motion_detector_v2_bricklet_description:

Beschreibung
------------

Das Motion Detector :ref:`Bricklet <primer_bricklets>` erweitert 
:ref:`Bricks <primer>` um einen Passiv-Infrarot (PIR) Sensor. Es kann benutzt
werden um Bewegungen von Personen und Tieren zu erkennen. Es hat eine 
konfigurierbare Reichweite von bis zu 12m mit einem Erfassungswinkel von 120°.

Es ist auch möglich Events zu nutzen. Dadurch ist es möglich auf eine
Bewegungserkennung zu reagieren ohne zu pollen.

Die Fresnel Linse kann über blaue LEDs beleuchtet werden. Die Helligkeit ist per API 
einstellbar und kann dazu genutzt werden um eine erkannte Bewegung anzuzeigen.

Das Motion Detector Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Hintergrundbeleuchting im Einsatz: 

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_motion_detector_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_motion_detector_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_motion_detector_v2_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch (LEDs aus)         37mW
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Erkennungsreichweite              bis zu 12m (konfigurierbar)
Erfassungswinkel                  120°
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 45 x 30mm (0,98 x 1,78 x 1,18")
Gewicht                           6g
================================  ============================================================


Ressourcen
----------

* PIR Sensor AS612 (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/raw/master/datasheets/AS612.pdf>`__)
* Fresnel Lens S8002-2W (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/raw/master/datasheets/S8002-2w.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/raw/master/hardware/motion-detector-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/motion_detector_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2sBeApm>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/motion_detector_v2/motion-detector-v2.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/motion_detector_v2/motion-detector-v2.FCStd>`__)


.. _motion_detector_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun eine erkannte Bewegung
angezeigt.

.. image:: /Images/Bricklets/bricklet_motion_detector_v2_brickv.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_v2_brickv.jpg

|test_pi_ref|



.. _motion_detector_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Motion Detector Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-motion-detector-v2-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_motion_detector_v2_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Motion Detector Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_v2_case_built_up_1000.jpg

.. include:: Motion_Detector_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/motion_detector_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Motion Detector Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/motion_detector_v2_exploded.png

|bricklet_case_hint|


.. _motion_detector_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Motion_Detector_V2_hlpi.table
