.. _current25_bricklet:

Current25 Bricklet
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_current_tilted_350.jpg",
	               "Bricklets/bricklet_current_tilted_600.jpg",
	               "Current25 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_current_horizontal_100.jpg",
	             "Bricklets/bricklet_current_horizontal_600.jpg",
	             "Current25 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_current_vertical_100.jpg",
	             "Bricklets/bricklet_current_vertical_600.jpg",
	             "Current25 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_current_master_100.jpg",
	             "Bricklets/bricklet_current_master_600.jpg",
	             "Current25 Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_current25_brickv_100.jpg",
	             "Bricklets/bricklet_current25_brickv.jpg",
	             "Current25 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/current25_bricklet_dimensions_100.png",
	             "Dimensions/current25_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst elektrische Ströme bis zu **25A**
* Misst die Stromrichtung
* Ausgabe in 1mA Schritten (12Bit Auflösung)


Beschreibung
------------

Mit dem Current25 :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` bidirektional Ströme bis zu **25A**
messen. Der gemessene Strom kann direkt in `Ampere
<http://de.wikipedia.org/wiki/Ampere>`__ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Stromänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Mittels einer bidirektionale Strommessungen kann z.B. zwischen Laden und
Entladen eines Akkus unterschieden werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            ACS711 (25A Version)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Strom                             -25A bis 25A in 1mA Schritten, 12Bit Auflösung
Maximale Eingangsspannung         100VAC/100VDC (Spitzenbelastung)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 14mm (0,98 x 0,98 x 0,55")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* ACS711 Datenblatt (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/datasheets/ACS711.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/hardware/current-25-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/current25_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/current25-bricklet/zipball/master>`__)


.. _current25_bricklet_test:

Teste dein Current25 Bricklet
-----------------------------

Um das Current25 Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Now you can connect the Current25 Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet. Connect a Motor
and a Battery to the Bricklet as displayed in the following image
(or anything else connected in series to the Current25 Bricklet that
produces a current).

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Current25 Bricklet mit Batterie und Motor verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Current25 Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected you can now see the current used by the
motor and a graph that shows the current over time.

.. image:: /Images/Bricklets/bricklet_current25_brickv.jpg
   :scale: 100 %
   :alt: Current25 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current25_brickv.jpg

In the screenshot you can see a high current peak. This is caused by the
starting of the motor when the battery is connected.

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <current25_programming_interfaces>` über das
API des Current25 Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _current25_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Current25_hlpi.table
