
:shoplink: ../../../shop/bricklets/dmx-bricklet.html

.. include:: DMX.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dmx_bricklet:

DMX Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dmx_tilted1_[?|?].jpg          DMX Bricklet
	Bricklets/bricklet_dmx_tilted2_[?|?].jpg          DMX Bricklet
	Bricklets/bricklet_dmx_front_[?|?].jpg            DMX Bricklet
	Bricklets/bricklet_dmx_back_[?|?].jpg             DMX Bricklet
	Bricklets/bricklet_dmx_top_[?|?].jpg              DMX Bricklet
	Bricklets/bricklet_dmx_brickv_[100|].jpg          DMX Bricklet im Brick Viewer
	Dimensions/dmx_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Unterstützt DMX Slave und Master
* Verfügt über XLR Buchse und Stecker
* Alle 512 DMX Kanäle verfügbar
* Kann genutzt werden um bestehende DMX Netzwerke zu überwachen
* Schaltbare 120 Ohm Termination


.. _dmx_bricklet_description:

Beschreibung
------------

Mit dem DMX :ref:`Bricklet <primer_bricklets>` können :ref:`Bricks <primer_bricks>` 
als DMX Slave oder Master eingesetzt werden.

Im Master Modus kann das Bricklet bis zu 512 Kanäle mit der maximal möglichen
DMX Geschwindigkeit gesteuert werden. Frames können mit einer festen Frame-Rate
gesendet werden um gleichmäßige Animationen zu erzeugen. Die Frames sind
double-buffered um die Performance zu erhöhen.

Im Slave Modus kann das Bricklet alle 512 Kanäle empfangen. Es kann auf jeden 
dieser Kanäle reagiert werden. Es ist auch möglich ein existierendes DMX Netzwerk
ohne Beeinflussung zu überwachen.

Das Bricklet ist mit einer XLR Buchse und Stecker ausgestattet und verfügt über eine
schaltbare 120 Ohm Terminierung.

Das Bricklet verfügt über keine galvanische Trennung zum Tinkerforge System. 
Das heißt es gibt eine direkte elektrische Verbindung zwischen den 
Anschlussklemmen des Bricklets und dem restlichen System. Sollte dies in der 
jeweiligen Anwendung zu ungewollten Verbindungen, Masseschleifen oder 
Kurzschlüssen führen, so ist der Einsatz zusammen mit einem :ref:`Isolator Bricklet <isolator>` ratsam.

Das DMX Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    180mW (36mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Modis                             Master / Slave
Kanäle                            512
Frame Rate                        Bis zu 44Hz bei 512 Kanälen (höher bei weniger Kanälen)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Größe (B x T x H)                 60 x 50 x 30mm (2.36 x 1.97 x 1.18")
Gewicht                            30g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/dmx-bricklet/raw/master/hardware/dmx-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dmx_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dmx-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2C4Vatz>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/dmx/dmx.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/dmx/dmx.FCStd>`__)


.. _dmx_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Nun kann zwischen Master/Slave Modus umgeschaltet werden und Daten können je nach Modus
gesendet oder empfangen werden.

.. image:: /Images/Bricklets/bricklet_dmx_brickv.jpg
   :scale: 100 %
   :alt: DMX Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dmx_brickv.jpg

|test_pi_ref|


.. _dmx_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das DMX Bricklet 
<https://www.tinkerforge.com/de/shop/cases/case-dmx-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_dmx_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für DMX Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_dmx_case_built_up1_800.jpg


Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Unterteil,
* schraube 12mm Schrauben mit Mutter an Unterteil
* Schraube Abstandshalter an das Bricklet und,
* schraube Oberteil auf obere Abstandshalter.

Im Folgenden befindet sich eine Explosionszeichnung des DMX Bricklet Gehäuses:

.. image:: /Images/Exploded/dmx_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für DMX Bricklet
   :align: center
   :target: ../../_images/Exploded/dmx_exploded.png

|bricklet_case_hint|


.. _dmx_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: DMX_hlpi.table
