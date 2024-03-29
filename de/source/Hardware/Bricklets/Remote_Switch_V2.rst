
:shoplink: ../../../shop/bricklets/remote-switch-v2-bricklet.html

.. include:: Remote_Switch_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _remote_switch_v2_bricklet:

Remote Switch Bricklet 2.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_remote_switch_v2_tilted_[?|?].jpg             Remote Switch Bricklet 2.0
	Bricklets/bricklet_remote_switch_v2_side_[?|?].jpg               Remote Switch Bricklet 2.0
	Bricklets/bricklet_remote_switch_v2_top_[?|?].jpg                Remote Switch Bricklet 2.0
	Bricklets/bricklet_remote_switch_v2_brickv_[100|].jpg            Remote Switch Bricklet 2.0 im Brick Viewer
	Dimensions/remote_switch_v2_bricklet_dimensions_[100|600].png    Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Drahtlose Hausautomatisierung
* Steuert Funksteckdosen (:ref:`Unterstützte Steckdosen <remote_switch_v2_supported_devices>`)
* Kann Funksteckdosen mit Dimm-Funktion steuern
* Kann Funksteckdosen-Fernbedienungen auslesen


.. _remote_switch_v2_bricklet_description:

Beschreibung
------------

Das Remote Switch :ref:`Bricklet <primer_bricklets>` 2.0 ist mit einem
433MHz Funkmodul ausgestattet (433MHz SMA Antenne liegt bei). Es kann genutzt
werden um über einen :ref:`Brick <primer_bricks>` alle Funksteckdosen zu steuern 
die auf dem PT2262 oder HX2262 IC basieren.

Housecode und Receivercode der zu schaltenden Steckdose können über die
API konfiguriert werden.

Das Bricklet kann auch als Empfänger der Fernbedienungen genutzt werden.

Technische Spezifikation
------------------------

================================  ===============================================================================================
Eigenschaft                       Wert
================================  ===============================================================================================
Funkmodul                         RFM69HW
Stromverbrauch                    113mW (inaktiv), 231mW (senden)
--------------------------------  -----------------------------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------------------------
Funkfrequenz                      433MHz
Unterstütze Funksteckdosen        Alle auf PT2262 und HX2262 basierenden (:ref:`komplette Liste <remote_switch_v2_supported_devices>`)
--------------------------------  -----------------------------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------------------------
Abmessungen (B x T x H)           25 x 40 x 5mm (0,98 x 1,58 x 0,2")*
Gewicht                           8g*
================================  ===============================================================================================

\* ohne Antenne

Ressourcen
----------

* RFM69HW Datenblatt (`Download <https://github.com/Tinkerforge/remote-switch-v2-bricklet/raw/master/datasheets/RFM69HW.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/remote-switch-v2-bricklet/raw/master/hardware/remote-switch-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/remote_switch_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/remote-switch-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2BK1DJ4>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/remote_switch_v2/remote-switch-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/remote_switch_v2/remote-switch-v2.FCStd>`__)


.. _remote_switch_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Als nächstes müssen der House und Receiver Code konfiguriert werden.
Wenn alles wie erwartet funktioniert können nun Funksteckdosen gesteuert
werden.

.. image:: /Images/Bricklets/bricklet_remote_switch_v2_brickv.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_v2_brickv.jpg

|test_pi_ref|


.. _remote_switch_v2_supported_devices:

Liste unterstützter Geräte
--------------------------

Die folgenden Geräte werden vom Remote Switch Bricklet 2.0 unterstützt. Wenn du
eine weitere kompatible Funksteckdosen findest, würden wir uns über eine
E-Mail freuen. Dann können wir die Liste erweitern und aktuell halten.

Das Remote Switch Bricklet 2.0 unterstützt im Moment drei verschiedene
:ref:`Adressierungsarten <remote_switch_v2_bricklet_addressing_types>`: A, B und C.

.. |nbsp| unicode:: 0xA0
   :trim:

=================== ==================================== ================================== =======
Hersteller          Modelle                              Funktion                           Typ
=================== ==================================== ================================== =======
BAT                 RC 3500-A                            Schalter                           A
|nbsp|              RC AAA1000-A                         Schalter                           A
|nbsp|              RC AAA3680-A                         Schalter                           A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Brennenstuhl        RCS 1000 N Comfort                   Schalter Set                       A
|nbsp|              RCS 1044 N Comfort                   Außenschalter Set                  A
|nbsp|              RCS 2044 N Comfort Indoor            Schalter Set                       A
|nbsp|              RCS 2044 N Comfort Outdoor           Außenschalter Set                  A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
DÜWI                FS1                                  Schalter Set                       C
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
ELRO                AB440D                               Dimmer                             A
|nbsp|              AB440ID                              Dimmer (unter Putz)                A
|nbsp|              AB440IS                              Schalter (unter Putz)              A
|nbsp|              AB440L                               Lampenfassung-Dimmer               A
|nbsp|              AB440R                               Fernbedienung                      A
|nbsp|              AB440S                               Schalter                           A
|nbsp|              AB440W                               Außenschalter                      A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
ELRO Home Easy      HE801S                               Schalter Set                       B
|nbsp|              HE801SA                              Schalter Set                       C
|nbsp|              HE801SF                              Schalter Set                       B
|nbsp|              HE802SA                              Dimmer Set                         B
|nbsp|              HE802SF                              Dimmer Set                         B
|nbsp|              HE803S                               Dimmer Set                         B
|nbsp|              HE805S                               Schalter Set (unter Putz)          B
|nbsp|              HE808S                               Schalter Set                       B
|nbsp|              HE815S                               Dimmer/Schalter Set                B
|nbsp|              HE820                                Gong                               B
|nbsp|              HE821S                               Gong mit Blinklicht                B
|nbsp|              HE831S                               Außenschalter Set                  B
|nbsp|              HE834S                               Außenschalter Set                  B
|nbsp|              HE844A                               Fernbedienung                      B
|nbsp|              HE866                                Einbauschalter für Außenbereich    B
|nbsp|              HE867                                Außenschalter                      B
|nbsp|              HE871                                Lampenfassung-Schalter             B
|nbsp|              HE872                                Lampenfassung-Dimmer               B
|nbsp|              HE874                                Schalter                           C
|nbsp|              HE875                                Mini-Schalter                      B
|nbsp|              HE877                                Schalter                           B
|nbsp|              HE877A                               Schalter mit Ein/Aus am Empfänger  B
|nbsp|              HE878                                Schalter                           B
|nbsp|              HE878A                               Dimmer                             B
|nbsp|              HE881                                Einbausteckdose                    B
|nbsp|              HE886                                Schalter (unter Putz)              B
|nbsp|              HE888                                Dimmer (unter Putz)                B
|nbsp|              HE889                                Jalousieschalter (unter Putz)      B
|nbsp|              HE876                                Mini-Dimmer                        B
|nbsp|              HE892S                               Steckdosenleiste                   B
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Intertechno         CMR-300                              Dimmer (unter Putz)                C
|nbsp|              CMR-500                              Jalousieschalter (unter Putz)      C
|nbsp|              CMR-1000                             Schalter (unter Putz)              C
|nbsp|              CMR-1001                             Impulseschalter (unter Putz)       C
|nbsp|              CMR-1224                             12/24V Schalter (unter Putz)       C
|nbsp|              HDR-105                              12V Dimmer                         C
|nbsp|              GR-300                               Außendimmer                        C
|nbsp|              GRR-300                              Außendimmer                        B
|nbsp|              GRR-3500                             Außenschalter                      B
|nbsp|              IT-1500                              Schalter Set                       B
|nbsp|              IT-2300                              4x Schalter                        B
|nbsp|              IT-3500L                             Schalter                           B
|nbsp|              ITDL-1000                            Schalter (unter Putz)              B
|nbsp|              ITDM-250                             LED Dimmer (unter Putz)            B
|nbsp|              ITE-300                              Dimmer (unter Putz)                C
|nbsp|              ITE-1000                             Schalter (unter Putz)              C
|nbsp|              ITK-200                              Fernbedienung                      C
|nbsp|              ITL-150                              Dimmer (unter Putz)                B
|nbsp|              ITL-210                              Dimmer (unter Putz)                B
|nbsp|              ITL-230                              Schalter (unter Putz)              B
|nbsp|              ITL-250                              LED Dimmer (unter Putz)            B
|nbsp|              ITL-300                              Dimmer (unter Putz)                B
|nbsp|              ITL-500                              Jalousieschalter (unter Putz)      B
|nbsp|              ITL-1000                             Zeitschalter (unter Putz)          B
|nbsp|              ITL-3500                             Schalter (unter Putz)              B
|nbsp|              ITLR-300                             Dimmer                             B
|nbsp|              ITLR-3500                            Schalter                           B
|nbsp|              ITR-300                              Dimmer                             C
|nbsp|              ITR-1500                             Schalter Set                       B
|nbsp|              ITR-3500                             Schalter                           C
|nbsp|              ITR-7000                             Gong                               B
|nbsp|              ITT-1500                             Fernbedienung                      B
|nbsp|              LBUR-100                             Lampenfassung-Schalter             B
|nbsp|              PA3-1000                             Schalter Set                       C
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Mumbi               m-FS300 (Jahr 2013 Model)            Schalter Set                       A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
ONE FOR ALL         HC-8000                              Schalter Set                       C
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Vivanco             FSS 31000W                           Schalter Set                       A
|nbsp|              FSS 33600W                           Schalter Set                       A
=================== ==================================== ================================== =======


230V Geräte schalten
^^^^^^^^^^^^^^^^^^^^

230V Geräte schalten ist eine typische Anwendung. Geräte dafür gibt es in
verschiedenen Varianten. Zum Beispiel als Zwischenstecker der in eine
gewöhnliche Steckdose gesteckt wird (z.B. Intertechno ITR-1500 und ELRO HE874)
oder dafür gemacht um unter Putz verbaut zu werden (z.B. Intertechno ITL-1000).
Zusätzliche Funktionen wie eine Abschaltautomatik, die nach einer einstellbaren
Zeit das Gerät wieder abschaltet sind ebenfalls erhältlich.

.. image:: /Images/Bricklets/bricklet_remote_it_homeeasy_350.jpg
   :scale: 100 %
   :alt: Intertechno ITR-1500 Schalter und ELRO HE874 Schalter
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_homeeasy_1000.jpg

.. image:: /Images/Bricklets/bricklet_remote_it_itl_1000_350.jpg
   :scale: 100 %
   :alt: Intertechno ITL-1000 Zeitschalter (unter Putz)
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_itl_1000_1000.jpg


12/24V Geräte schalten
^^^^^^^^^^^^^^^^^^^^^^

Niederspannungs und batteriebetriebene Geräte sind üblich im Bereich von
Autos, LKWs und Booten. Dafür gibt es spezielle Funkschalter die mit 12/24V
arbeiten (z.B. Intertechno CMR-1224).

.. image:: /Images/Bricklets/bricklet_remote_it_cmr_1224_350.jpg
   :scale: 100 %
   :alt: Intertechno CMR-1224 12/24V Schalter (unter Putz)
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_cmr_1224_1000.jpg


(Energiespar-) Lampen und LEDs dimmen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Neben einfachen An- und Ausschaltern gibt es auch Funkdimmer für gewöhnliche
Lampen (z.B. Intertechno ITLR-300), für Energiespar-Lampen (z.B. Intertechno
ITL-150) und für LED Lampen (z.B. Intertechno ITL-250).

.. image:: /Images/Bricklets/bricklet_remote_it_dimmer_350.jpg
   :scale: 100 %
   :alt: Intertechno ITLR-300 Dimmer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_dimmer_1000.jpg


Garagentore und Jalousien steuern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Für Garagentore und Jalousien sind einfache An- und Ausschalter nicht
ausreichend. Für diesen Anwendungsfall gibt es spezielle Funkschalter die
drei Zustande haben: hoch, runter und aus (z.B. Intertechno CMR-500).

.. image:: /Images/Bricklets/bricklet_remote_it_cmr_500_350.jpg
   :scale: 100 %
   :alt: Intertechno CMR-500 Jalousieschalter (unter Putz)
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_cmr_500_1000.jpg


Gongs auslösen
^^^^^^^^^^^^^^

Neben Schaltern in verschiedensten Variationen gibt es auch noch Gongs (z.B.
Intertechno ITR-7000) die mit Ton und/oder Lichtsignalen auf sich aufmerksam
machen und ebenfalls über Funk ausgelöst werden können.

.. image:: /Images/Bricklets/bricklet_remote_it_gong_350.jpg
   :scale: 100 %
   :alt: Intertechno ITR-7000 Gong
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_gong_1000.jpg


.. _remote_switch_v2_bricklet_addressing_types:

Adressierungsarten
------------------

Um Funksteckdosen oder -dimmer zu steuern, muss deren Adresse bekannt sein.
Das Remote Switch Bricklet 2.0 unterstützt verschiedene Adressierungsarten. Wie
man die Adresse eines Gerätes herausfinden bzw. festlegt wird im Folgenden
beschrieben. Die :ref:`Liste unterstützter Geräte
<remote_switch_v2_supported_devices>` gibt an welche Adressierungsart jeweils
verwendet wird.


.. _remote_switch_v2_bricklet_type_a_house_and_receiver_code:

Typ A: Housecode und Receivercode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der Housecode und Receivercode wird typischerweise über kleine DIP-Schalter
in der Steckdose oder dem Dimmer eingestellt. Es kann vorkommen, dass Geräte
nicht mit House- oder Receivercode beschriftet sind. Im nachfolgenden Foto ist
zum Beispiel die DIP-Schalter-Abdeckung mit "System Code" und "Unit Code"
beschriftet. Hierbei ist mit "System Code" der Housecode und mit "Unit Code"
der Receivercode gemeint.

Im Bild unten sind die DIP-Schalter 1 und 5 für den Housecode auf On gestellt,
dies entspricht 10001 binär (niederwertigstes Bit zuerst) bzw. 17 dezimal. Für
den Receivercode steht nur DIP-Schalter A auf On, dies entspricht 10000 binär
(niederwertigstes Bit zuerst) bzw. 1 dezimal.

.. image:: /Images/Bricklets/bricklet_remote_dip_switch_350.jpg
   :scale: 100 %
   :alt: DIP-Schalter in Funksteckdose um Housecode und Reiceivercode zu setzen
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_dip_switch_1000.jpg


.. _remote_switch_v2_bricklet_type_b_address_and_unit:

Typ B: Adresse und Unit
^^^^^^^^^^^^^^^^^^^^^^^

Geräte von Typ B haben keine Schalter um ihre Adresse und Unit einzustellen.
Stattdessen kann diesen Funksteckdosen und -dimmern ihre Adresse und Unit
angelernt werden. Abhängig vom jeweiligen Gerät befindet sich dieses
automatisch für einige Sekunden nach dem Einstecken im Lernmodus (Intertechno
Gerät, links im Bild) oder es hat einen Knopf um es in den Lernmodus zu
versetzen (ELRO Gerät, rechts im Bild). Während das Gerät im Lernmodus ist
muss ein Einschaltbefehl gesendet werden mit der Adresse und Unit die dem
Gerät zugewiesen werden soll. Gegebenenfalls muss der Einschaltbefehl mehrfach 
gesendet werden bis das Gerät den Lernmodus verlässt.


.. image:: /Images/Bricklets/bricklet_remote_it_homeeasy_350.jpg
   :scale: 100 %
   :alt: Anlernbare Funkschalter von Intertechno und ELRO
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_homeeasy_1000.jpg


.. _remote_switch_v2_bricklet_type_c_system_and_device_code:

Typ C: Systemcode und Devicecode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der System- und Devicecode werden üblicherweise mittels Kodierrädern auf der
Rückseite des Funkschalters oder -dimmers. Es kann vorkommen, dass der
Systemcode anders benannt ist. Zum Beispiel "Housecode", "Systembuchstabe"
oder "Familiencode".

Im folgenden Bild steht das linke Kodierrad (A-P) auf M für den Systemcode und
das rechte Kodierrad (1-16) auf 1 für den Devicecode.

.. image:: /Images/Bricklets/bricklet_remote_it_cmr_500_350.jpg
   :scale: 100 %
   :alt: Kodierrad an Jalousieschalter um Systemcode und Devicecode einzustellen
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_cmr_500_1000.jpg


.. _remote_switch_v2_usage_as_receiver:

Nutzung als Empfänger
---------------------

Funksteckdosen werden üblicherweise mit dazugehörigen Fernbedienungen geliefert.
Diese Fernbedienungen kann das Remote Switch Bricklet 2.0 auslesen.

Dazu muss das Bricklet für einen Empfang des jeweiligen Typs konfiguriert werden.
Anschließend können die empfangenen Signale ausgelesen werden.


.. _remote_switch_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Remote Switch Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-remote-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_remote_case_tilted_front_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Remote Switch Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_remote_case_tilted_front_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet,
* baue Seitenteile auf mit Bricklet uns Sensor in der Mitte (das Antennenteil
  ist leicht asymmetrisch, der breitere Rand gehört von außen gesehen nach unten),
* schraube Unterteil an untere Abstandshalter,
* schraube Oberteil auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Remote Switch Bricklet 2.0-Gehäuse:

.. image:: /Images/Exploded/remote_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Remote Switch Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/remote_exploded.png

|bricklet_case_hint|


.. _remote_switch_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Remote_Switch_V2_hlpi.table
