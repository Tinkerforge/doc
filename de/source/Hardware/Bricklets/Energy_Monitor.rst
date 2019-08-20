
:DISABLED_shoplink: ../../../shop/bricklets/energy-monitor-bricklet.html

.. include:: Energy_Monitor.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _energy_monitor_bricklet:

Energy Monitor Bricklet
=======================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_energy_monitor_tilted_[?|?].jpg                          Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_top_[?|?].jpg                             Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_w_transformer_[?|?].jpg                   Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_heater_brickv_[100|].jpg                  Energy Monitor Bricklet im Brick Viewer
	Bricklets/bricklet_energy_monitor_led_lamp_brickv_[100|].jpg                Energy Monitor Bricklet im Brick Viewer
	Bricklets/bricklet_energy_monitor_fan_brickv_[100|].jpg                     Energy Monitor Bricklet im Brick Viewer
	Bricklets/bricklet_energy_monitor_energy_saving_lightbulb_brickv_[100|].jpg Energy Monitor Bricklet im Brick Viewer
	Dimensions/energy_monitor_bricklet_dimensions_[100|600].png                 Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Ermöglicht die Messung der Netzspannung (120V/230V AC)
* Misst Spannung (V), Strom (A) und Energie (Wh)
* Misst Wirkleistung, Scheinleistung und Blindleistung (W/VA/VAR)
* Misst Leistungsfaktor und Frequenz (Hz)
* Liefert Spannungs- und Stromwellenform


.. _energy_monitor_bricklet_description:

Beschreibung
------------

Das Energy Monitor :ref:`Bricklet <primer_bricklets>` ist mit einer
3,5mm Hohlsteckerbuchse für einen Stromwandler und einer 3,5mm (1,35mm Innendurchmesser) 
Buchse für einen Spannungswandler (Transformator) ausgestattet. Über beide Wandler
werden Spannung, Strom, Energie, Wirkleistung/Scheinleistung und Blindleistung, sowie der
Leistungsfaktor und die Frequenz einer Phase der Netzspannung berechnet. 
Zusätzlich liefert das Bricklet die Wellenformen von Strom und Spannung.

Das Energy Monitor Bricklet kann alle diese Messungen vornehmen, ohne dass
Kabel aufgetrennt werden müssen!

Um das Bricklet zu nutzen, muss ein Stromwandler um den Leiter einer Phase gelegt werden.
Zusätzlich muss über einen Spannungswandler (z.B. Transformator) die Spannung der gleichen
Phase gemessen werden. Das Energy Monitor Bricklet nutzt die niedrigen Ausgangsspannungen
der Wandler, um die Messungen durchzuführen. Damit wird sichergestellt, dass die potentiell
gefährliche Netzspannung nicht direkt am Bricklet anliegt.

Separat erhältlich sind der `230V Spannungstransformator <https://www.tinkerforge.com/de/shop/ac-ac-voltage-transformer.html>`__
und der `5A Stromwandler <https://www.tinkerforge.com/de/shop/5a-1v-current-transformer-clamp.html>`__ bzw. der
`30A Stromwandler <https://www.tinkerforge.com/en/shop/30a-1v-current-transformer-clamp.html>`__.
Das Bricklet liefern wir kalibriert für diese Wandler aus.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    50mW (10mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Eingangsspannung                  Max 12V AC vom Spannungswandler
Eingangsstrom                     Max 1V AC vom Stromwandler
Anschluss Spannungsmessung        3,5mm Buchse (Kopfhörerbuchse)
Anschluss Strommessung            3,5mm Buchse (Außendurchmesser),  1,35mm Innendurchmesser 
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 5mm (1,57 x 1,57 x 0,2")
Gewicht                           7g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/energy-monitor-bricklet/raw/master/hardware/energy-monitor-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/energy_monitor_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/energy-monitor-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/31FfjlR>`__ | Download: `STEP <https://download.tinkerforge.com/3d/energy_monitor/energy_monitor.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/energy_monitor/energy_monitor.FCStd>`__)

.. _energy_monitor_bricklet_beispiel_heizluefter:

Beispiel: Leistungsmessung eines Heizlüfters
--------------------------------------------

.. warning::
 Es sollte niemals an stromführenden Teilen gearbeitet werden! 
 Diese sind vorher sicher vom Stromnetz zu trennen!

Als Beispiel werden wir die Leistung eines Heizlüfter messen.

Um dies zu bewerkstelligen müssen wir den Spannungswandler 
(AC/AC Transformator) und den Stromwandler an die Leitung
anschließen über die der Heizlüfter betrieben wird.

Ein typisches europäisches Netzkabel besitzt drei Leiter:

* Neutralleiter (N)
* Erde (PE)
* Phase (L)

Bei Dreiphasen Anschlüssen (Drehstrom), gibt es zwei weitere Leiter so
dass es die Phasen L1, L2 und L3 gibt. Möchte man die Leistung hier messen,
so müssten drei Bricklets, für jede Phase eins, jeweils mit einem Strom- und
Spannungswandler, genutzt werden.

In unserem einphasen Beispiel, wird der Stromwandler an L angeschlossen.
Dazu muss nur der Leiter durch den Wandler geführt werden. Einfach geht dies,
wenn man den Wandler dazu aufklappt. Es ist absolut notwendig, dass nur L
durch den Stromwandler geführt wird. Wird als Beispiel zusätzlich zu L auch
noch N durchgeführt, so funktioniert die Strommessung nicht.

.. image:: /Images/Bricklets/bricklet_energy_monitor_tutorial_2_600.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet Heizlüfter Beispiel
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_tutorial_2_1200.jpg

Auf der Brickletseite muss der Stromwandler mit dem *AC Current* Eingang
verbunden werden.

Unser AC/AC Transformator (Spannungswandler) kann einfach wie ein Steckernetzteil
mit einer Mehrfachsteckdose neben dem Heizlüfter eingesteckt werden.

.. image:: /Images/Bricklets/bricklet_energy_monitor_tutorial_3_600.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet Heizlüfter Beispiel Foto 2
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_tutorial_3_1200.jpg

Auf der Brickletseite muss nun der Spannungswandler in den *AC Voltage* 
Eingang eingesteckt werden.

Das Resultat sollte in etwa so aussehen:

.. image:: /Images/Bricklets/bricklet_energy_monitor_tutorial_1_w_caption_800.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet Heizlüfter Beispiel Foto 3
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_tutorial_1_w_caption_1200.jpg

Im Brick Viewer sieht der Aufbau wie folgt aus:

.. image:: /Images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet im Brick Viewer (Heizlüfter)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg


Wandler-Verhältnis
------------------

Beide Wandler (Strom- und Spannungswandler), die mit dem Energy
Monitor Bricklet verbunden werden, wandeln den gemessenen Strom/Spannung
mit einem festen Verhältnis um (Ratio).

Die Stromwandler, die von uns vertrieben werden, haben ein Verhältnis von
5A:1V und 30A:1V. Der Spannungswandler (Trafo) wird beim Anschluss an das 
Bricklet nicht belastet (es fließt kein großer Strom). Daher liefert der 
Wandler eine etwas höhere Ausgangsspannung von ca. 12V bei 230V Eingang.
Exakt gemessen beträgt das Verhältnis 19.23V:1V. Die Verhältnisse können
im Brick Viewer angepasst werden:


.. image:: /Images/Bricklets/bricklet_energy_monitor_brickv_ratios.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet Ratio Konfiguration
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_brickv_ratios.jpg

Wird der 5A:1V Stromwandler genutzt. so muss das Wandlerverhältnis (Ratio)
auf 5 gesetzt werden.

Werden eigene Strom- oder Spannungswandler genutzt, so müssen die Verhältnisse
dementsprechend angepasst werden.

Die Auflösung der Strommessung erhöhen
--------------------------------------

Die Stromwandler messen den Strom über das magnetische Feld, welches der 
umschlossene Leiter erzeugt (siehe 
`Wikipedia Stromwandler <https://de.wikipedia.org/wiki/Stromwandler>`__).
Über einen einfachen Trick, kann die Auflösung der Strommessung erhöht werden. 
Dazu muss einfach der Leiter mehrfach durch den Stromwandler geführt werden.

TODO Foto Stromwandler mit mehrfach durchgeführten Leiter

Dadurch ändert sich das Verhältnis der Strommessung:

* 2-fach durchgeführt: 2-faches Verhältnis
* 3-fach durchgeführt: 3-faches Verhältnis
* usw.

Sollte der reale Strom zu groß sein, so wird die Messung abgeschnitten.
Das Bricklet kann dadurch nicht beschädigt werden. Die Messung ist
dann aber natürlich nicht mehr korrekt. Das gleiche Problem tritt 
auch bei der Wahl eines zu kleinen Stromwandlers auf.

Das mehrfache Durchführen eines Leiters erhöht aber auch das Rauschen,
so dass prinzipiell immer ein möglichst passender Wandler gewählt werden
sollte.

.. _energy_monitor_bricklet_wellenformen:

Waveforms
---------

Das Energy Monitor Bricklet kann doe Wellenform von Strom und Spannung 
liefern. Normalerweise sollte die Spannungswellenform immer sinusförmig
aussehen, wohingegen die Stromwellenform je nach Last sehr verschieden 
aussehen kann. Nachfolgend ein paar Beispiel-Wellenformen für vier
verschiedene Lasten.

Wellenform 1: 1.7kW Heizlüfter.

.. image:: /Images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (Heizlüfter)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg

Wellenform 2: 125W Ventilator.

.. image:: /Images/Bricklets/bricklet_energy_monitor_fan_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (Ventilator)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_fan_brickv.jpg

Wellenform 3: 10W LED Lampe. Der Leiter wurde dreimal durch den Stromwandler geführt um
die Auflösung zu erhöhen. Viele AC/DC Stromversorgungen sehen ähnlich aus.

.. image:: /Images/Bricklets/bricklet_energy_monitor_led_lamp_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (LED lampe)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_led_lamp_brickv.jpg

Wellenform 4: 12W Energiesparbirne. Der Leiter wurde achtmal durch den Stromwandler geführt
um die Auflösung zu erhöhen. Wie man sehen kann nutzt die Energiesparbirne nur 1/4 der
Wellenform.

.. image:: /Images/Bricklets/bricklet_energy_monitor_energy_saving_lightbulb_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (Energiesparbirne)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_energy_saving_lightbulb_brickv.jpg



.. _energy_monitor_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Verbinde den Spannungs- und Stromwandler wie zuvor beschrieben.

Nun können die Wellenform von Strom und Spannung sowie die Spannung, Strom, 
Leistungsfaktor, Frequenz, Energie und Schein-, Wirk- und Blindleistung abgelesen werden.

.. image:: /Images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg

Die Wellenform des Stroms hängt dabei massiv on der Last ab (siehe :ref:`energy_monitor_bricklet_wellenformen`).


|test_pi_ref|


.. _energy_monitor_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Energy Monitor Bricklet
	<https://www.tinkerforge.com/de/shop/cases/case-energy-monitor-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_energy_monitor_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Energy Monitor Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_energy_monitor_case_1000.jpg

	.. include:: Energy_Monitor.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/energy_monitor_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Energy Monitor Bricklet
	   :align: center
	   :target: ../../_images/Exploded/energy_monitor_exploded.png

	|bricklet_case_hint|


.. _energy_monitor_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Energy_Monitor_hlpi.table
