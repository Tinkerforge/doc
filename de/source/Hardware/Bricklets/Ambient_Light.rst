.. _ambient_light_bricklet:

Ambient Light Bricklet
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_ambient_light_tilted_350.jpg",
	               "Bricklets/bricklet_ambient_light_tilted_600.jpg",
	               "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_vertical_100.jpg",
	             "Bricklets/bricklet_ambient_light_vertical_600.jpg",
	             "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_horizontal_100.jpg",
	             "Bricklets/bricklet_ambient_light_horizontal_600.jpg",
	             "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_master_100.jpg",
	             "Bricklets/bricklet_ambient_light_master_600.jpg",
	             "Ambient Light Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_brickv_100.jpg",
	             "Bricklets/bricklet_ambient_light_brickv.jpg",
	             "Ambient Light Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/ambient_light_bricklet_dimensions_100.png",
	             "Dimensions/ambient_light_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Umgebungslicht bis zu 900Lux
* Ausgabe in 0,1Lux Schritten (12Bit Auflösung)


Beschreibung
------------

Mit dem Ambient Light :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` die Umgebungshelligkeit messen.
Die gemessene Helligkeit kann in `Lux <http://de.wikipedia.org/wiki/Lux>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
Helligkeitsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Board kann genutzt werden um z.B. helligkeitsabhängig Beleuchtungen
oder Motoren zu steuern.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            TEMT6000
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beleuchtungsstärke                0Lux - 900Lux in 0,1Lux Schritten, 12Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* TEMT6000 Datenblatt (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/datasheets/TEMT6000.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/hardware/ambient-light-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ambient_light_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/zipball/master>`__)


.. _ambient_light_bricklet_test:

Teste dein Ambient Light Bricklet
---------------------------------

Um das Ambient Light Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Now you can connect the Ambient Light Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet.

.. image:: /Images/Bricklets/bricklet_ambient_light_master_600.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Ambient Light Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected you can now see the illuminance in lux,
a graphical representation of the illuminance and a graph that shows the
illuminance over time. A good test for the sensor is to darken the room and
slowly move a flashlight over the sensor, the graph should then look
approximately as in the screenshot shown below.

.. image:: /Images/Bricklets/bricklet_ambient_light_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_brickv.jpg

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <ambient_light_programming_interfaces>` über das
API des Ambient Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _ambient_light_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Ambient_Light_hlpi.table
