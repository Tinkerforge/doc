
:DISABLED_shoplink: ../../../shop/bricklets/voltage-current-v2-bricklet.html

.. include:: Voltage_Current_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _voltage_current_v2_bricklet:

Voltage/Current Bricklet 2.0
============================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_voltage_current_v2_tilted_[?|?].jpg           Voltage/Current Bricklet 2.0
	Bricklets/bricklet_voltage_current_v2_horizontal_[?|?].jpg       Voltage/Current Bricklet 2.0
	Bricklets/bricklet_voltage_current_v2_master_[100|600].jpg       Voltage/Current Bricklet 2.0 mit Master Brick
	Cases/bricklet_voltage_current_v2_case_[100|600].jpg             Voltage/Current Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_voltage_current_v2_brickv_[100|].jpg          Voltage/Current Bricklet 2.0 im Brick Viewer
	Dimensions/voltage_current_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Leistung, Spannung und Strom bis zu 720W/36V/20A
* Auflösung 1mW, 1mV, 1mA über kompletten Messbereich
* Bidirektionale Strommessung (z.B. Laden/Entladen)
* Konfigurierbare Mittelwertbildung und ADC-Wandlungszeit


.. _voltage_current_v2_bricklet_description:

Beschreibung
------------

Mit dem Voltage/Current :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` um die Fähigkeit Leistung/Spannung/Strom
zu messen erweitert werden. Das Bricklet wird einfach
zwischen Spannungsversorgung (z.B. Batterie) und Last (z.B. Motor) eingebaut.

In akkubetriebenen Systemen können über die bidirektionale Strommessung
Aussagen über den Ladezustand des Akkus getroffen werden.

Das Voltage/Current Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            INA226 mit 4mΩ Shunt Widerstand
Stromverbrauch                    30mW (6mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximaler Strom                   ±20A
Maximale Spannung                 36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (B x T x H)             30 x 30 x 18mm (1,18 x 1,18 x 0,67")
Gewicht                           10g

================================  ============================================================


Ressourcen
----------

* INA226 Datenblatt (`Download <https://github.com/Tinkerforge/voltage-current-v2-bricklet/raw/master/datasheets/ina226.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/voltage-current-v2-bricklet/raw/master/hardware/voltage-current-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/voltage_current_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/voltage-current-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


Anschlussmöglichkeiten
----------------------

Das Voltage/Current Bricklet 2.0 wird einfach zwischen Stromversorgung und der 
Last eingebaut. Schließe an die Klemme beschriftet mit "IN" die 
Stromversorgung an. An die Klemme "OUT" die Last. Die Polung ist mit "+" 
und "-" vor der Klemme gekennzeichnet.

.. warning::

 Die Polung beim Anschließen unbedingt beachten! Das Bricklet ist nicht
 verpolungssicher!

Das Bricklet misst die zwischen "+" und "-" der "IN" Klemme anliegende Spannung,
sowie den Stromfluss vom "+" der "IN" Klemme zum "+" der "OUT" Klemme.

.. _voltage_current_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

Als nächstes muss noch eine Last und eine Stromquelle mit dem Bricklet 
verbunden werden.  
Zum Beispiel einen Motor und eine Batterie wie im folgenden Bild.

TODO: Bild aktualisieren

.. image:: /Images/Bricklets/bricklet_voltage_current_setup_600.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_setup_1200.jpg

|test_tab|

Wenn alles wie erwartet funktioniert wird die Stromaufnahme des Motors 
angezeigt.
Der Graph gibt den zeitlichen Verlauf der Stromaufnahme wieder.

.. image:: /Images/Bricklets/bricklet_voltage_current_v2_brickv.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_v2_brickv.jpg

|test_pi_ref|


Kalibrierung
------------

Die Strommessung des Voltage/Current Bricklet ist bei Raumtemperatur
werkskalibriert worden. Die Messwerte können sich um wenige mA
verschieben falls in einer sehr kalten oder sehr warmen Umgebung
gemessen wird. Mit einem präzisen Multimeter kann dies allerdings
leicht behoben werden:

.. image:: /Images/Bricklets/bricklet_voltage_current_v2_brickv_calibration.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet 2.0 Kalibrierung im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_v2_brickv_calibration.jpg

Starte Brick Viewer und klicke auf den "Calibration..."-Button und folge den Schritten
die in der GUI beschrieben sind. 

Die Spannung kann auch kalibriert werden, nach unsere
Erfahrung erreicht die Spannungsmessung allerdings auch komplett ohne Kalibrierung
bereits eine Genauigkeit von 0,5%.

Wenn die Werkskalibrierung der Strommessung entfernt wird, muss die Strommessung
neu kalibriert werden (auf Grund der Toleranz des Shunt-Winderstandes).

.. _voltage_current_v2_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Voltage/Current Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-voltage-current-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_voltage_current_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Voltage/Current Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_voltage_current_v2_case_1000.jpg

	.. include:: Voltage_Current_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/voltage_current_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Voltage/Current Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/voltage_current_v2_exploded.png

	|bricklet_case_hint|


.. _voltage_current_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Voltage_Current_V2_hlpi.table
