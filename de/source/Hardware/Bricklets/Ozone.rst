
:DISABLED_shoplink: ../../../shop/bricklets/ozone-bricklet.html

.. include:: Ozone.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ozone_bricklet:

Ozone Bricklet
==============

.. note::
  Diese Bricklet ist noch in Entwicklung!


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
Abmessung (W x D x H)             TBD x TBD x TBDmm (TBD x TBD x TBD")
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


.. _ozone_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Ozone_hlpi.table
