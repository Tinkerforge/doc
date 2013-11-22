
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Piezo Speaker Bricklet
:FIXME_shoplink: ../../../shop/bricklets/piezo-speaker-bricklet.html

.. include:: Piezo_Speaker.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _piezo_speaker_bricklet:

Piezo Speaker Bricklet
========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_piezo_speaker_tilted_350.jpg",
	               "Bricklets/bricklet_piezo_speaker_tilted_600.jpg",
	               "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_vertical_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_vertical_600.jpg",
	             "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_horizontal_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_horizontal_600.jpg",
	             "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_brickv_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_brickv.jpg",
	             "Piezo Speaker Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/piezo_speaker_bricklet_dimensions_100.png",
	             "Dimensions/piezo_speaker_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Erzeugt Piepton mit konfigurierbarer Frequenz von 585Hz bis 7100Hz
* Konfigurierbare Piepdauer
* Morsecode Ausgabe unterstützt

Beschreibung
------------

Das Piezo Speaker :ref:`Bricklet <product_overview_bricklets>` kann genutzt
werden um Töne mit unterschiedlichen Frequenzen zu erzeugen. Der verfügbare
Frequenzbereich ist 585Hz bis 7100Hz. Ein Ton hat eine konfigurierbare Länge
und es ist möglich `Moresezeichen <http://de.wikipedia.org/wiki/Morsezeichen>`__
als String zu übergeben.

Eine typische Anwendung dieses Bricklets ist das signalisieren von 
Zustandsänderungen wie "E-Mail empfangen".

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Buzzer                            PS1420P02CT
Frequenzbereich                   585 - 7100Hz (konfigurierbar)
Schalldruck                       60 - 82dB/10cm (abhängig von Frequenz)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 30 x 13mm (0,98 x 1,18 x 0,51")
Gewicht                           5g
================================  ============================================================


Ressourcen
----------

* PS1420P02CT Datenblatt (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/raw/master/datasheets/ef532_ps.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/raw/master/hardware/piezo-speaker-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/piezo_speaker_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/zipball/master>`__)


.. _piezo_speaker_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird können nun Töne erzeugt werden. 

.. image:: /Images/Bricklets/bricklet_piezo_speaker_brickv.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_brickv.jpg

|test_pi_ref|

.. _piezo_speaker_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Piezo Speaker Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-piezo-speaker-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_piezo_speaker_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Piezo Speaker Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_piezo_speaker_case_built_up_1000.jpg

.. include:: Piezo_Speaker.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/piezo_speaker_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Piezo Speaker Bricklet
   :align: center
   :target: ../../_images/Exploded/piezo_speaker_exploded.png

|bricklet_case_hint|


.. _piezo_speaker_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Piezo_Speaker_hlpi.table
