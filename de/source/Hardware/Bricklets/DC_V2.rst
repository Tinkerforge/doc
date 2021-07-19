:shoplink: ../../../shop/bricklets/dc-v2-bricklet.html

.. include:: DC_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dc_v2_bricklet:

DC Bricklet 2.0
===============


.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dc_v2_tilted_[?|?].jpg           DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_w_connector_[?|?].jpg      DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_tilted2_[?|?].jpg          DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_horizontal_[?|?].jpg       DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_w_motor_[?|?].jpg          DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_brickv_[100|].jpg          DC Bricklet 2.0 im Brick Viewer
	Dimensions/dc_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Steuert einen Gleichstrommotor mit max. **28V** und **5A** (Peak) über USB
* API für viele Programmiersprachen verfügbar
* Richtung, Geschwindigkeit und Beschleunigung können gesteuert werden
* Übertemperatur- und Überstrom-Callbacks konfigurierbar


.. _dc_v2_bricklet_description:

Beschreibung
------------

Mit dem DC :ref:`Bricklet <primer_bricks>` 2.0 kann ein
`Gleichstrommotor <https://de.wikipedia.org/wiki/Gleichstrommaschine>`__
(max. **28V** und **5A** (Peak)) gesteuert werden. Eine API für
:ref:`viele Programmiersprachen <dc_v2_bricklet_programming_interface>` ermöglicht
das Steuern der Richtung, Geschwindigkeit und Beschleunigung des Motors.

Neben Methoden zum Steuern des angeschlossenen Motors bietet die API 
Möglichkeiten zur Messung des Stromverbrauchs und der Versorgungsspannung. Im 
Falle einer Überhitzung oder Überspannung können Callbacks ausgelöst werden, 
so dass auf diese im eigenen Programm reagiert werden kann.

Zusätzlich kann der Fahrmodus zwischen Fahren/Bremsen und
Fahren/Leerlauf umgeschaltet werden (siehe :ref:`Fahrmodus
<dc_v2_bricklet_drive_mode>`).


Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Stromverbrauch                      50mW (10mA bei 5V) ohne Motor
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximaler Motorstrom                | Kurzzeitig: 5A (Peak)
                                    | Dauerhaft: > 3A (Abhängig von der Kühlung)
Minimale/Maximale Eingangsspannung  6V/28V
PWM Frequenz                        Einstellbar, 1-20kHz, Standard 15kHz
Geschwindigkeit                     -32767 bis 32767, Rückwärts nach Vorwärts, 0=Stopp
Beschleunigung                      0 bis 65535, Geschwindigkeit/s, Inkrement für Geschwindigkeit/s
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             40 x 40 x 15mm (1,57 x 1,57 x 0,59")
Gewicht                             12g
==================================  ============================================================


Ressourcen
----------

* MC33926 Datenblatt (`Download <https://github.com/Tinkerforge/dc-v2-bricklet/raw/master/datasheets/MC33926.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/dc-v2-bricklet/raw/master/hardware/dc-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dc_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dc-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://a360.co/3gNZ8h1>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/dc_v2/dc-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/dc_v2/dc-v2.FCStd>`__)


.. _dc_v2_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
DC Bricklet 2.0.

.. image:: /Images/Bricklets/bricklet_dc_v2_caption_600.jpg
   :scale: 100 %
   :alt: DC Bricklet 2.0 mit Beschriftung
   :align: center
   :target: ../../_images/Bricklets/bricklet_dc_v2_caption_800.jpg


.. _dc_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Schließe einen DC Motor und eine passende Stromversorgung an das Bricklet an.

|test_tab|

.. image:: /Images/Bricklets/bricklet_dc_v2_brickv.jpg
   :scale: 100 %
   :alt: DC Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dc_v2_brickv.jpg

Als erstes muss das Häkchen für "Enable" gesetzt werden, um die Treiberstufe
zu aktivieren. Es stehen 4 Regler zur Kontrolle der Geschwindigkeit
(vorwärts und rückwärts), der Beschleunigung und der
`PWM <https://de.wikipedia.org/wiki/Pulsweitenmodulation>`__ Frequenz zur
Verfügung. Letztere wird von der Treiberstufe benutzt, um den angeschlossenen
Motor anzusteuern.

Auf der rechten Seite befinden sich Anzeigen für die Spannungen der zwei
möglichen Stromversorgung sowie den Stromverbrauch des Motors.
Darunter befindet sich eine Tachometer zur Darstellung der
Motorgeschwindigkeit.

Unterhalb der Regler befinden sich Knöpfe für "Full Break" und die verschiedenen
Fahrmodi (siehe :ref:`here <dc_v2_bricklet_drive_mode>` für weiterführende Information).

|test_pi_ref|


.. _dc_v2_bricklet_drive_mode:

Fahrmodi
--------

Es gibt zwei Arten den Motor anzusteuern:

* Fahren/Bremsen

  In diesem Modus wird der Motor durchgehend angesteuert, entweder wird er
  gefahren oder gebremst. Es ist kein Freilauf möglich. Dies führt zu einer
  besseren Korrelation zwischen PWM und Geschwindigkeit, als Vorteil diese
  Modus. Dadurch kann eine genauere Beschleunigung erzielt werden. Gewöhnliche
  Motoren können in diesem Modus mit geringeren Geschwindigkeit gefahren
  werden. Ein Nachteil diese Modus ist der höhere Stromverbrauch wodurch sich
  die Treiberstufe schneller aufheizt.

* Fahren/Leerlauf

  In diesem Modus wird der Motor nicht durchgehend angesteuert, entweder wird er
  gefahren oder ist im Leerlauf. Dies verringert den Stromverbrauch und die
  Treiberstufe heizt sich nicht so schnell auf.
  Die Kontrolle über Geschwindigkeit und Beschleunigung ist weniger genau und
  kann "hinterher hinken".


.. _dc_v2_bricklet_error_led:

Error LED
---------

Die rote Error-LED hat drei unterschiedliche Zustände:

* Aus: Es liegt kein Fehler vor.
* 1s Intervall-Blinken: Eingangsspannung zu klein (unter 6V).
* 250ms Intervall-Blinken: Übertemperatur oder Überstrom.

Wenn ein Übertemperatur- oder Überstrom-Event eintritt hört
der Motor auf zu laufen und der treiber wird deaktiviert.
Um den Treiber wieder zu starten muss dieser explizit mit
der Enable-Funktion wieder aktiviert werden.


.. _dc_v2_bricklet_case:

Gehäuse
-------

TBD

..
	Ein `laser-geschnittenes Gehäuse für das DC Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-dc-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_dc_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für DC Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_dc_v2_case_1000.jpg

	.. include:: DC_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/dc_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für DC Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/dc_v2_exploded.png

	|bricklet_case_hint|


.. _dc_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: DC_V2_hlpi.table
