
.. _tutorial_bricklet_cables:

Tutorial - Bricklet Kabel (7-Pol vs 10-Pol) 
===========================================

Anfang 2017 haben wir angefangen alle existierenden Bricklets durch neue
Versionen zu ersetzen. Diese neuen Versionen haben einen 
:ref:`Co-Prozessor anstelle eines EEPROMs <tutorial_eeprom_vs_co_processor>`
sowie einen anderen Stecker.

Der alte Stecker hatte 10 Pole und wurde nur durch Reibung in der Buchse
gehalten. Leider war es möglich diesen Stecker in einem Winkel einzustecken,
sodass sich Pinne in der Buchse verbogen. Dies war mit Abstand die
häufigste Reklamation die wir von Kunden bekommen haben. Daher trafen
wir die Entscheidung den Stecker durch einen neuen auszutauschen während
der Umstellung von EEPROMs auf Co-Prozessoren.

Der neue Stecker hat 7 Pole, er hat einen Sicherungshaken und kann nicht
schief eingesteckt werden.

Auf Grund dieser Änderungen bieten wir aktuell drei unterschiedliche
Kabeltypen an:

* 10-Pol - 10-Pol (10p-10p),
* 7-Pol - 10-Pol (7p-10p) und
* 7-Pol - 7-Pol (7p-7p).

Altes Bricklet mit 10p Stecker und neues Bricklet mit 7p Stecker:

.. image:: /Images/Misc/cable_10p10p_and_7p10p_connect_800.jpg
   :scale: 100 %
   :alt: Bricklet mit 10p/7p Stecker
   :align: center
   :target: ../../_images/Misc/cable_10p10p_and_7p10p_connect_1200.jpg

Im weiteren beschreiben wir wie die einzelnen Kabeltypen benutzt werden
können.


Bricklet Kabel 10-Pol - 10-Pol (10p-10p)
----------------------------------------

.. image:: /Images/Misc/cable_10p10p_front_350.jpg
   :scale: 100 %
   :alt: Front- und Rückseite eines 10p-10p Kabels
   :align: center
   :target: ../../_images/Misc/cable_10p10p_front_1000.jpg

Das 10p-10p Kabel kann genutzt werden um Bricks mit

* alten Bricklets mit 10-Pol Stecker

zu verbinden.

Diese Brickelts werden durch neue Bricklets mit 7-Pol Stecker ersetzt,
daher werden diese Kabel in der Zukunft nicht mehr gebraucht werden.

Verfügbare Kabel:

* `Bricklet Kabel 6cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-6cm.html>`__
* `Bricklet Kabel 15cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-15cm.html>`__
* `Bricklet Kabel 50cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-50cm.html>`__
* `Bricklet Kabel 100cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-100cm.html>`__
* `Bricklet Kabel 200cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-200cm.html>`__

* `Bricklet Kabel Shielded 50cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-50cm.html>`__
* `Bricklet Kabel Shielded 100cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-100cm.html>`__
* `Bricklet Kabel Shielded 200cm (10p-10p) <https://www.tinkerforge.com/de/shop/accessories/bricklet-cable-black-200cm.html>`__


Bricklet Kabel 7-Pol - 10-Pol (7p-10p)
--------------------------------------

.. image:: /Images/Misc/cable_7p10p_connector_backfront_600.jpg
   :scale: 100 %
   :alt: Front- und Rückseite eines 7p-10p Kabels
   :align: center
   :target: ../../_images/Misc/cable_7p10p_connector_backfront_1000.jpg

Die 7p-10p Kabel können genutzt werden um Bricks mit

* neuen Bricklets mit 7-Pol Stecker

zu verbinden. Verfügbare Kabel:

* `Bricklet Kabel 6cm (7p-10p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-black-6cm-7p-10p.html>`__
* `Bricklet Kabel 15cm (7p-10p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-black-15cm-7p-10p.html>`__
* `Bricklet Kabel 50cm (7p-10p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-black-50cm-7p-10p.html>`__
* `Bricklet Kabel 100cm (7p-10p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-black-100cm-7p-10p.html>`__
* `Bricklet Kabel 200cm (7p-10p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-black-200cm-7p-10p.html>`__

Bricklet Kabel 7-Pol - 7-Pol (7p-7p)
------------------------------------

.. image:: /Images/Misc/cable_7p7p_connector_350.jpg
   :scale: 100 %
   :alt: Front- und Rückseite eines 7p-7p Kabel
   :align: center
   :target: ../../_images/Misc/cable_7p7p_connector_1000.jpg

Die 7p-7p Kabel können genutz werden um die neuem Bricklets mit 7-Pol
Stecker mit

* :ref:`Isolator Bricklet <isolator_bricklet>`,
* Bricklet HAT (noch nicht veröffentlicht) und
* Bricklet HAT Zero (noch nicht veröffentlicht)

zu verbinden. Es ist nicht möglich alte 10-Pol Bricklets mit dem Isolator oder
einem HAT zu verbinden.

Auf dem Bild unten ist ein Isolator Bricklet abgebildet welches auf der einen Seite
mit einem Master Brick und auf der anderen Seite mit einem Voltage/Current Bricklet
verbunden ist. In dieser Konfiguration wird links ein 7p-10p Kabel und rechts
ein 7p-7p Kabel benötigt.

.. image:: /Images/Bricklets/bricklet_isolator_cables_800.jpg
   :scale: 100 %
   :alt: Isolator Bricklet mit 7p-10p und 7p-7p Kabel
   :align: center
   :target: ../../_images/Bricklets/bricklet_isolator_cables_1200.jpg


Verfügbare Kabel:

* `Bricklet Kabel 6cm (7p-7p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-6cm-7p-7p.html>`__
* `Bricklet Kabel 15cm (7p-7p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-15cm-7p-7p.html>`__
* `Bricklet Kabel 50cm (7p-7p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-50cm-7p-7p.html>`__
* `Bricklet Kabel 100cm (7p-7p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-100cm-7p-7p.html>`__
* `Bricklet Kabel 200cm (7p-7p) <https://www.tinkerforge.com/en/shop/accessories/bricklet-cable-200cm-7p-7p.html>`__


Zukunftsaussichten
------------------

In der Zukunft werden alle Buchsen auf den neuen 7-Pol Stecker umgestellt
(inklusive Bricks). Daher werden die 7p-7p Kabel auf Dauer als einzige
Kategorie übrig bleiben.

Keine Sorge falls du alte Bricklets mit 10-Pol Stecker verwendest, wir
werden kompatible Bricks wieterhin im Shop behalten.
