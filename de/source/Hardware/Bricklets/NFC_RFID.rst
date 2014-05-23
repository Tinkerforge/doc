
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / NFC/RFID Bricklet
:shoplink: ../../../shop/bricklets/nfc-rfid-bricklet.html

.. include:: NFC_RFID.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_rfid_bricklet:

NFC/RFID Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_nfc_rfid_tilted_350.jpg",
	               "Bricklets/bricklet_nfc_rfid_tilted_600.jpg",
	               "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_horizontal_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_horizontal_600.jpg",
	             "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_vertical_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_vertical_600.jpg",
	             "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_setup_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_setup_600.jpg",
	             "NFC/RFID Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_nfc_rfid_case_100.jpg",
	             "Cases/bricklet_nfc_rfid_case_600.jpg",
	             "NFC/RFID Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_brickv_100.png",
	             "Bricklets/bricklet_nfc_rfid_brickv.png",
	             "NFC/RFID Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/nfc_rfid_bricklet_dimensions_100.png",
	             "Dimensions/nfc_rfid_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* TODO: FIXME
* Misst Leistung, Spannung und Strom bis zu 720W/36V/20A
* Auflösung 1mW, 1mV, 1mA über kompletten Messbereich
* Bidirektionale Strommessung (z.B. Laden/Entladen)
* Konfigurierbare Mittelwertbildung und ADC-Wandlungszeit


Beschreibung
------------

TODO: FIXME

Mit dem NFC/RFID :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` um die Fähigkeit Leistung/Spannung/Strom
zu messen erweitert werden. Das Bricklet wird einfach
zwischen Spannungsversorgung (z.B. Batterie) und Last (z.B. Motor) eingebaut.

In akkubetriebenen Systemen können über die bidirektionale Strommessung
Aussagen über den Ladezustand des Akkus getroffen werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            PN532
Stromverbrauch                    TODOmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
TODO                              TODO
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (B x T x H)             TODO: 30 x 30 x 18mm (1,18 x 1,18 x 0,67")
Gewicht                           TODOg
================================  ============================================================


Ressourcen
----------

* INA226 Datenblatt (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/datasheets/PN532.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/hardware/nfc-rfid-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/nfc_rfid_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/zipball/master>`__)


.. _nfc_rfid_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.


.. image:: /Images/Bricklets/bricklet_nfc_rfid_setup_600.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_setup_1200.jpg

|test_tab|

Wenn alles wie erwartet funktioniert wird TBD

.. image:: /Images/Bricklets/bricklet_nfc_rfid_brickv.png
   :scale: 70 %
   :alt: NFC/RFID Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_brickv.png

|test_pi_ref|

.. _nfc_rfid_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das NFC/RFID Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-nfc-rfid-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_nfc_rfid_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_rfid_case_1000.jpg

.. include:: NFC_RFID.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/nfc_rfid_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Exploded/nfc_rfid_exploded.png

|bricklet_case_hint|


.. _nfc_rfid_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: NFC_RFID_hlpi.table
