
:shoplink: ../../../shop/bricklets/performance-dc-bricklet.html

.. include:: Performance_DC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _performance_dc_bricklet:

Performance DC Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_performance_dc_tilted1_[?|?].jpg          Performance DC Bricklet
	Bricklets/bricklet_performance_dc_top_[?|?].jpg              Performance DC Bricklet
	Bricklets/bricklet_performance_dc_tilted2_[?|?].jpg          Performance DC Bricklet
	Bricklets/bricklet_performance_dc_caption_[?|?].jpg          Performance DC Bricklet
	Bricklets/bricklet_performance_dc_brickv_[100|].jpg          Performance DC Bricklet im Brick Viewer
	Dimensions/performance_dc_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Steuert einen Gleichstrommotor mit max. **36V** und **10A** (kontinuierlich)
* Richtung, Geschwindigkeit und Beschleunigung können gesteuert werden
* Zwei konfigurierbare optisch isolierte GPIOs für Endstopps o.ä.
* Status-, Error- und Richtungs-LEDs
* Übertemperatur- und Überstrom-Callbacks konfigurierbar


.. _performance_dc_bricklet_description:

Beschreibung
------------

Mit dem DC :ref:`Brick <primer_bricks>` kann ein
`Gleichstrommotor <https://de.wikipedia.org/wiki/Gleichstrommaschine>`__
(max. **36V** und **10A** (kontinuierlich)) gesteuert werden. Eine API für
:ref:`viele Programmiersprachen <performance_dc_bricklet_programming_interface>` ermöglicht 
das Steuern der Richtung, Geschwindigkeit und Beschleunigung des Motors.
Zusätzlich kann der Fahrmodus zwischen Fahren/Bremsen und
Fahren/Leerlauf umgeschaltet werden (siehe :ref:`Fahrmodus
<performance_dc_bricklet_drive_mode>`).

Neben Methoden zum Steuern des angeschlossenen Motors bietet die API 
Möglichkeiten zur Messung des Stromverbrauchs und der Versorgungsspannung. Im 
Falle einer Überhitzung oder Überspannung können Callbacks ausgelöst werden, 
so dass auf diese im eigenen Programm reagiert werden kann.

Das Bricklet kommt mit zwei optisch isolierten Eingängen die als Endstopps 
konfiguriert werden können.

Sechs nutzerkonfigurierbare Status-KEDs zeigen den GPIO-Status, die Motorichtung,
Fehlerzustände und mehr.


Technische Spezifikation
------------------------

===================================  ===============================================================
Eigenschaft                          Wert
===================================  ===============================================================
Stromverbrauch                       60mW (12mA bei 5V) ohne Motor
-----------------------------------  ---------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------
Maximaler Motorstrom                 Kurzzeitig: 10A (kontinuierlich)
Minimale/Maximale Eingangsspannung   6V/36V
PWM Frequenz                         Einstellbar, 1-50kHz, Standard 20kHz
Geschwindigkeit                      -32767 bis 32767, Rückwärts nach Vorwärts, 0=Stopp
Beschleunigung                       0 bis 65535, Geschwindigkeit/s, Inkrement für Geschwindigkeit/s
-----------------------------------  ---------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------
Abmessungen (B x T x H)              80 x 80 x 22mm (3.15 x 3.15 x 0.87")
Gewicht                              50g
===================================  ===============================================================


Ressourcen
----------

* DRV8701 datasheet (`Download <https://github.com/Tinkerforge/performance-dc-bricklet/raw/master/datasheets/drv8701.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/performance-dc-bricklet/raw/master/hardware/performance-dc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/performance_dc_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/performance-dc-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _performance_dc_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
Performance DC Bricklets

.. image:: /Images/Bricklets/bricklet_performance_dc_caption_600.jpg
   :scale: 100 %
   :alt: Performance DC Bricklet mit Beschriftung
   :align: center
   :target: ../../_images/Bricklets/bricklet_performance_dc_caption_800.jpg


.. _performance_dc_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Schließe einen DC Motor und eine passende Stromversorgung an das Bricklet an.

|test_tab|

.. image:: /Images/Bricklets/bricklet_performance_dc_brickv.jpg
   :scale: 100 %
   :alt: Performance DC Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_performance_dc_brickv.jpg

Als erstes muss das Häkchen für "Enable" gesetzt werden um die Treiberstufe
zu aktivieren. Es stehen 4 Regler zur Kontrolle der Geschwindigkeit
(vorwärts und rückwärts), der Beschleunigung und der
`PWM <https://de.wikipedia.org/wiki/Pulsweitenmodulation>`__ Frequenz zur
Verfügung. Letztere wird von der Treiberstufe benutzt um den angeschlossenen
Motor anzusteuern.

Auf der rechten Seite befinden sich Anzeigen für die Spannungen der zwei
möglichen Stromversorgung sowie den Stromverbrauch des Motors.
Darunter befindet sich eine Tachometer zur Darstellung der
Motorgeschwindigkeit.

Unterhalb der Regler befinden sich Knöpfe für "Full Break" und die verschiedenen
Fahrmodi (siehe :ref:`here <performance_dc_bricklet_drive_mode>` für weiterführende Information).

|test_pi_ref|


.. _performance_dc_bricklet_drive_mode:

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


.. _performance_dc_bricklet_error_led:

Error LED
---------

Die rote Error-LED hat drei unterschiedliche Zustände:

* Aus: Es liegt kein Fehler vor.
* 1s Intervall-Blinken: Eingangsspannung zu klein (unter 6V).
* 250ms Intervall-Blinken: Übertemperatur oder Überstrom.

Wenn ein Überttemperatur- oder Überstrom-Event eintritt hört
der Motor auf zu laufen und der treiber wird deaktiviert.
Um den Treiber wieder zu starten muss dieser explizit mit
der Enable-Funktion wieder aktiviert werden.


.. _performance_dc_bricklet_case:

Gehäuse
-------

TBD

..
	Ein `laser-geschnittenes Gehäuse für das Performance DC Bricklet
	<https://www.tinkerforge.com/de/shop/cases/case-performance-dc-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_performance_dc_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Performance DC Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_performance_dc_case_1000.jpg

	.. include:: Performance_DC.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/performance_dc_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Performance DC Bricklet
	   :align: center
	   :target: ../../_images/Exploded/performance_dc_exploded.png

	|bricklet_case_hint|


.. _performance_dc_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Performance_DC_hlpi.table
