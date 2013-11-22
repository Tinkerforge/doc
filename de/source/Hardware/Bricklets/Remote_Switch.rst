
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Remote Switch Bricklet
:FIXME_shoplink: ../../../shop/bricklets/remote-switch-bricklet.html

.. include:: Remote_Switch.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _remote_switch_bricklet:

Remote Switch Bricklet
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_remote_tilted_350.jpg",
	               "Bricklets/bricklet_remote_tilted_600.jpg",
	               "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_vertical_100.jpg",
	             "Bricklets/bricklet_remote_vertical_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_horizontal_100.jpg",
	             "Bricklets/bricklet_remote_horizontal_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_tilted_wo_antenna_100.jpg",
	             "Bricklets/bricklet_remote_tilted_wo_antenna_600.jpg",
	             "Remote Switch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_w_antenna_100.jpg",
	             "Bricklets/bricklet_remote_w_antenna_600.jpg",
	             "Remote Switch Bricklet und Antenne")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_remote_switch_brickv_100.jpg",
	             "Bricklets/bricklet_remote_switch_brickv.jpg",
	             "Remote Switch Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/remote_bricklet_dimensions_100.png",
	             "Dimensions/remote_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Drahtlose Hausautomatisation
* Steuert Funksteckdosen (:ref:`Unterstützte Steckdosen <remote_switch_supported_devices>`)
* Kann Funksteckdosen mit Dimm-Funktion steuern

Beschreibung
------------

Das Remote Switch :ref:`Bricklet <product_overview_bricklets>` ist mit einem
433MHz Transceiver ausgestattet (433MHz SMA Antenne liegt bei). Es kann genutzt
werden um alle Funksteckdosen zu steuern die auf dem PT2262 oder HX2262 IC
basieren.

Housecode und Receivercode der zu schaltenden Steckdose können über die 
API konfiguriert werden.

Technische Spezifikation
------------------------

================================  ===============================================================================================
Eigenschaft                       Wert
================================  ===============================================================================================
Funkmodul                         RFM69HW
--------------------------------  -----------------------------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------------------------
Funkfrequenz                      433MHz
Unterstütze Funksteckdosen        Alle auf PT2262 und HX2262 basierenden (:ref:`komplette Liste <remote_switch_supported_devices>`)
--------------------------------  -----------------------------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------------------------
Abmessungen (B x T x H)           25 x 40 x 5mm (0,98 x 1,58 x 0,2")*
Gewicht                           7g*
================================  ===============================================================================================

\* ohne Antenne

Ressourcen
----------

* RFM69HW Datenblatt (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/raw/master/datasheets/RFM69HW.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/raw/master/hardware/remote-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/remote_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/remote-switch-bricklet/zipball/master>`__)


.. _remote_switch_supported_devices:

Liste unterstützter Geräte
--------------------------

Die folgenden Geräte werden vom Remote Switch Bricklet unterstützt. Wenn du
eine weitere kompatible Funksteckdosen findest, würden wir uns über eine
E-Mail freuen. Dann können wir die Liste erweitern und aktuell halten.

=============== ====================================
Hersteller      Modelle
=============== ====================================
BAT             * RC 3500-A
                * RC AAA1000-A
                * RC AAA3680-A
--------------- ------------------------------------
--------------- ------------------------------------
Brennstuhl      * RC 2044 Indoor
                * RC 2044 Outdoor
                * RC 3600
                * RCS 1000 N Comfort
                * RCS 1044 N Comfort
                * RCS 2044 N Comfort Indoor
                * RCS 2044 N Comfort Outdoor
--------------- ------------------------------------
--------------- ------------------------------------
ELRO            * AB440D
                * AB440ID
                * AB440IS
                * AB440L
                * AB440S
                * AB440W
--------------- ------------------------------------
--------------- ------------------------------------
Intertechno     * CMR-300
                * CMR-500
                * CMR-1000
                * CMR-1224
                * GRR-300
                * GRR-3500
                * IT-1500
                * IT-2300
                * ITL-150
                * ITL-210
                * ITL-230
                * ITL-250
                * ITL-300
                * ITL-500
                * ITL-1000
                * ITL-3500
                * ITR-300
                * ITR-1500
                * ITR-3500
                * ITR-7000
                * ITDL-1000
                * ITDR-3500
                * ITDR-3500T
                * LBUR-100
                * PA3-1000
--------------- ------------------------------------
--------------- ------------------------------------
Mumbi           * m-FS300
--------------- ------------------------------------
--------------- ------------------------------------
Vivanco         * FSS 31000W
                * FSS 33600W
=============== ====================================


.. _remote_switch_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_remote_switch_master_600.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert können nun Funksteckdosen gesteuert 
werden.

.. image:: /Images/Bricklets/bricklet_remote_switch_brickv.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_brickv.jpg

|test_pi_ref|


Housecode und Receivercode
----------------------------

Um Funksteckdosen oder -dimmer zu steuern muss der Housecode und der 
eingestellte Receivercode bekannt sein. Diese Codes werden typischerweise über
kleine DIP-Schalter in der Steckdose oder dem Dimmer eingestellt.

TODO Image


.. _remote_switch_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Remote Switch Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-remote-switch-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_remote_switch_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Remote Switch Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_remote_switch_case_built_up_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet,
* baue Seitenteile auf mit Bricklet uns Sensor in der Mitte,
* schraube Unterteil an untere Abstandshalter,
* schraube Oberteil auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Remote Switch Bricklet-Gehäuse:

.. image:: /Images/Exploded/remote_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Remote Switch Bricklet
   :align: center
   :target: ../../_images/Exploded/remote_exploded.png

|bricklet_case_hint|


.. _remote_switch_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Remote_Switch_hlpi.table
