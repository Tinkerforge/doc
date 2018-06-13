
:DISABLED_shoplink: ../../../shop/bricklets/ozone-bricklet.html

.. include:: Ozone.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ozone_bricklet:

Ozone Bricklet
==============

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ozone_tilted_[?|?].jpg           Ozone Bricklet
	Bricklets/bricklet_ozone_horizontal_[?|?].jpg       Ozone Bricklet
	Bricklets/bricklet_ozone_master_[100|600].jpg       Ozone Bricklet mit Master Brick
	Cases/bricklet_ozone_case_[100|600].jpg             Ozone Bricklet im Gehäuse
	Bricklets/bricklet_ozone_brickv_[100|].jpg          Ozone Bricklet im Brick Viewer
	Dimensions/ozone_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Ozon Konzentration von 0 bis 250 ppb (Teile pro Milliarde)


.. _ozone_bricklet_description:

Beschreibung
------------

Mit dem Ozone :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die `Ozon Konzentration
<https://de.wikipedia.org/wiki/Ozon>`__ der Luft messen.
Die gemessene Ozon Konzentration kann in `ppb
<https://de.wikipedia.org/wiki/Parts_per_billion>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
Ozon Konzentrationsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Bricklet kann genutzt werden TBD.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            A051020-SP-61
Stromverbrauch                    TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0ppb - 250ppb
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           TBD x TBD x TBDmm (TBD x TBD x TBD")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* A051020-SP-61 Datenblatt (`Download <https://github.com/Tinkerforge/ozone-bricklet/raw/master/datasheets/A051020-SP-61.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ozone-bricklet/raw/master/hardware/ozone-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ozone_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ozone-bricklet/zipball/master>`__)


.. _ozone_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_ozone_brickv.jpg
   :scale: 100 %
   :alt: Ozone Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ozone_brickv.jpg

|test_pi_ref|


.. _ozone_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Ozone Bricklet
	<https://www.tinkerforge.com/de/shop/cases/case-ozone-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_ozone_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Ozone Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_ozone_case_1000.jpg

	.. include:: Ozone.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/ozone_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Ozone Bricklet
	   :align: center
	   :target: ../../_images/Exploded/ozone_exploded.png

	|bricklet_case_hint|


.. _ozone_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Ozone_hlpi.table
