
:shoplink: ../../../shop/bricklets/industrial-counter-bricklet.html

.. include:: Industrial_Counter.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_counter_bricklet:

Industrial Counter Bricklet
===========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_counter_tilted_[?|?].jpg           Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_tilted2_[?|?].jpg          Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_side_[?|?].jpg             Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_top_[?|?].jpg              Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_brickv_[100|].jpg          Industrial Counter Bricklet im Brick Viewer
	Dimensions/industrial_counter_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Frequenzzähler mit 4 galvanisch isolierten Kanälen
* Konfigurierbarer Flankenzähler pro Kanal
* Misst Tastverhältnis, Frequenz und Zustand pro Kanal
* Frequenzmessung im Bereich von 0,03Hz bis 4MHz
* Zeitauflösung bis zu 10,4ns und Frequenzauflösung bis zu 0,03Hz


.. _industrial_counter_bricklet_description:

Beschreibung
------------

Das Industrial Counter :ref:`Bricklet <primer_bricklets>` kann genutzt
werden um :ref:`Bricks <primer_bricks>` um vier unabhängige Frequenzzähler zu erweitern.

Das Bricklet verfügt über einen integrierten Flankenzähler, der Tastverhältnis, 
Periode und die Frequenz getrennt pro Kanal messen kann. Frequenzen bis zu
4MHz können vom Bricklet verarbeitet werden.

Der Frequenzzähler kann steigende, fallende und beide Flankenwechsel zählen. Die 
Richtung des Zählers (hoch oder runter) ist einstellbar. Es ist auch möglich einen
Kanal als Richtungseingang für einen anderen Zähler zu nutzen 
(z.B. high = zählt hoch, low = zählt runter).

Alle 4 Kanäle sind galavanisch voneinander getrennt.

Beispielanwendungen für das Bricklet ist das Auslesen eines PWM-Signals
oder das Auslesen von Sensoren, die über einen Flankenzähler- oder einen 
Frequenzausgang verfügen.

Das Industrial Counter Bricklet hat einen 7 Pol Bricklet Stecker und wird mit einem
``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_industrial_counter_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_industrial_counter_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_industrial_counter_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

================================  ==============================================================
Eigenschaft                       Wert
================================  ==============================================================
Stromverbrauch                    100mW (20mA bei 5V)
--------------------------------  --------------------------------------------------------------
--------------------------------  --------------------------------------------------------------
Eingangstyp                       Vier Optokoppler-Eingänge (mit 2,7kΩ Serienwiderstand)
Eingangsstrom                     Abhängig von der Eingangsspannung, ca. 3,85mA/12V, 8,3mA/24V
Maximale Eingangsspannung         26V (DC)
Low Level Spannung                0-2V
High Level Spannung               10-26V
Isolation                         3750Vrms (Optokoppler-Wert)
--------------------------------  --------------------------------------------------------------
--------------------------------  --------------------------------------------------------------
Minimale Eingangsfrequenz         0,03MHz
Maximale Eingangsfrequenz         4MHz
Zeit-Auflösung                    bis zu 10.4ns (Duty Cycle Prescaler auf 1 gesetzt)
Frequenz-Auflösung                bis zu 0.03Hz (Frequenz-Integrationsszeit auf 32768ms gesetzt)
--------------------------------  --------------------------------------------------------------
--------------------------------  --------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8.4g
================================  ==============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-counter-bricklet/raw/master/hardware/industrial-counter-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_counter_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-counter-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rzxZ72>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_counter/industrial-counter.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_counter/industrial-counter.FCStd>`__)


.. _industrial_counter_bricklet_quadrature_encoder:

Quadraturencoder / Inkrementalgeber
-----------------------------------

Das Industrial Counter Bricklet kann genutzt werden um bis zu zwei Quadraturencoder
bzw Inkrementalgeber mit Quadratursignal auszulesen.

Ein A/B-Paar des Encoders kann mit den Kanälen 0/2 und das andere Paar mit den
Kanälen 1/3 verbunden werden.
        
.. image:: /Images/Bricklets/bricklet_industrial_counter_w_encoder_600.jpg
   :scale: 100 %
   :alt: Industrial Counter Bricklet, Silent Stepper Brick und LPD3806-600BM Encoder
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_w_encoder_1200.jpg

Um ein Beispiel bereitzustellen haben wir den LPD3806-600BM Encoder genutzt. Dieser
Encoder hat eine einfache Schnittstelle die aus den Signalen A, B, VCC und GND/SHD
besteht. Der Encoder kann per 24V-Stromversorgung versorgt werden.

Um den Encoder mit dem Industrial Counter Bricklet zu nutzen haben wir A und B
mit einem 1k-Ohm Pull-Up zu VCC ausgestattet und A mit CH0- sowie B mit CH2- und
VCC mit CH0+ und CH2+ verbunden:

.. image:: /Images/Bricklets/bricklet_industrial_counter_encoder.png
   :scale: 100 %
   :alt: Diagram of Industrial Counter Bricklet with LPD3806-600BM encoder
   :align: center

In Software konfigurieren wir einfach Kanal 0 steigende Flanken zu zählen wenn
Kanal 2 *low* ist (siehe :ref:`Extern Count Direction <industrial_counter_bricklet_external_count_direction>`
für mehr Informationen zu dieser Konfiguration).

Der folgende Beispielcode (Python) führt die notwendigen Konfigurationen aus und
startet eine volle Drehung mit dem Silent Stepper Brick. Danach liest er den
Zählerstand von Kanal 0 des Industrial Counter Bricklets aus und gibt diesen
auf der Console aus. Der LPD3806-600BM Encoder hat 600 Schritte pro Umdrehung,
wir erwarten also einen Zählerstand von 600.

.. code-block:: python

    HOST = "localhost"
    PORT = 4223
    UID_COUNTER = "GfX" 
    UID_SILENT_STEPPER = "63noND"

    from tinkerforge.ip_connection import IPConnection
    from tinkerforge.bricklet_industrial_counter import BrickletIndustrialCounter
    from tinkerforge.brick_silent_stepper import BrickSilentStepper
    import time

    if __name__ == "__main__":
        ipcon = IPConnection() # Create IP connection
        counter = BrickletIndustrialCounter(UID_COUNTER, ipcon) # Create device object
        ss = BrickSilentStepper(UID_SILENT_STEPPER, ipcon) # Create device object

        ipcon.connect(HOST, PORT) # Connect to brickd
        # Don't use device before ipcon is connected


        # Configure channel 0 to count up if channel 2 is low
        counter.set_counter_configuration(counter.CHANNEL_0, 
                                          counter.COUNT_EDGE_RISING,
                                          counter.COUNT_DIRECTION_EXTERNAL_DOWN,
                                          counter.DUTY_CYCLE_PRESCALER_1,
                                          counter.FREQUENCY_INTEGRATION_TIME_1024_MS)
        counter.set_all_counter_active([True, False, False, False])
        counter.set_counter(0, 0)

        # Configure stepper motor with 800mA, 10000steps/s² acceleration,
        # 1/16 step resolution, velocity 3200 steps/s and enable motor.
        ss.set_motor_current(800)
        ss.set_speed_ramping(10000, 10000)
        ss.set_step_configuration(ss.STEP_RESOLUTION_16, True)
        ss.set_max_velocity(3200)
        ss.enable() # Enable motor power

        # Move 3200 steps (at 1/16 step resolution and 200 steps per revolution
        # this is exactly 1 full revolution)
        ss.set_steps(3200)

        # Wait for 3200 steps to finish
        time.sleep(2)

        # Get counter value. 
        # We expect this to return a value of 600 for the LPD3806-600BM encoder
        encoder_count = counter.get_counter(0)
        print('Encoder Count: {0}'.format(encoder_count))

        ipcon.disconnect()


In unserem Test war die Ausgabe des Testprogramms exakt wie erwartet::
    
    tf@pc:~/tests$ python count.py 
    > Encoder Count: 600


.. _industrial_counter_bricklet_channel_status_led:

Kanal Status LEDs
-----------------

Das Bricklet verfügt über die standard Status-LED sowie vier weitere LEDs (eine pro Kanal).

Standardmäßig leuchten die LEDs, wenn der dazugehörige Kanal high ist und umgekehrt.
Die LEDs können aber auch per API ein/-ausgeschaltet werden um andere Statusinformationen
anzuzeigen.


.. _industrial_counter_bricklet_duty_cycle_prescaler_and_frequency_integration_time:

Duty Cycle Prescaler und Frequency Integration Time
---------------------------------------------------

Das Bricklet verfügt über zwei Konfigurationen pro Kanal:


**Duty Cycle Prescaler**: Prescaler für die interne Clock.

Intern nutzt das Bricklet eine 96Mhz Clock. Der Prescaler ist ein Teiler für diese Clock. Wenn
die Eingangsfrequenz kleiner ist wie 1465Hz, kann der interne Zähler überlaufen (Overflow)
und die Frequenzmessung wird verzerrt. In diesem Fall muss der Prescaler erhöht werden.

Ist die Frequenz über 1465Hz, kann der Prescaler immer auf 1 gesetzt werden.
Ist die Eingangsfrequenz unter 1465Hz, kann die untere Tabelle genutzt werden um einen Prescaler zu wählen, 
der die höchste Auflösung ermöglicht.

* 1: Minimale Frequenz 1465Hz, Auflösung 10.4ns
* 2: Minimale Frequenz 733Hz, Auflösung 20.8ns
* 4: Minimale Frequenz 367Hz, Auflösung 41.6ns
* 8: Minimale Frequenz 184Hz, Auflösung 83.3ns
* 16: Minimale Frequenz 92Hz, Auflösung 166.6ns
* 32: Minimale Frequenz 46Hz, Auflösung 333.3ns
* 64: Minimale Frequenz 23Hz, Auflösung 0.66us
* 12: Minimale Frequenz 12Hz, Auflösung 1.33us
* 256: Minimale Frequenz 6Hz, Auflösung 2.66us
* 512: Minimale Frequenz 3Hz, Auflösung 5.33us
* 1024: Minimale Frequenz 2Hz, Auflösung 10.66us
* 2048: Minimale Frequenz 0.7Hz, Auflösung 21.33us
* 4096: Minimale Frequenz 0.36Hz, Auflösung 42.66us
* 8192: Minimale Frequenz 0.18Hz, Auflösung 85.33us
* 16384: Minimale Frequenz 0.09Hz, Auflösung 170.66us
* 32768: Minimale Frequenz 0.045Hz, Auflösung 341.33us


**Frequency Integration Time**: Zeit die genutzt wird um die Frequenz zu berechnen.

Die Frequenz wird berechnet indem die Anzahl der Flanken in der gewählten Integrationszeit
ermittelt wird. Beispiel: Die Frequency Integration Time ist auf 2048ms gesetzt und das Bricklet
sieht 40960 Flankenwechsel in dieser Zeit. Die ermittelte Frequenz beträgt dann 20kHz 
(40960 Flanken geteilt durch 2,048 Sekunden).

Damit die Frequenzermittlung korrekt funktioniert muss die Frequency Integration Time größer sein
wie die Periode der gemessenen Frequenz.

Die Aktualisierungsrate der Frequenz ist abhängig von der Frequency Integration Time.
Eine kleine Integration Time führt zu einer häufigeren Aktualisierung. Wird die Zeit zum Beispiel
auf 4096ms gesetzt, so wird die Frequenz nur alle ~4 Sekunden aktualisiert.

Die Auflösung der gemessenen Frequenz erhöht sich mit steigender Integrationszeit:

* 128ms: 7.81Hz
* 256ms: 3.90Hz
* 512ms: 1.95Hz
* 1024ms: 0.98Hz
* 2048ms: 0.49Hz
* 4096ms: 0.24Hz
* 8192ms: 0.12Hz
* 16384ms: 0.06Hz
* 32768ms: 0.03Hz


.. _industrial_counter_bricklet_count_duty_period_frequency:

Count, Duty Cycle, Period, Frequency, Value
-------------------------------------------

Das Industrial Counter Bricklet misst fünf verschiedene Dinge:


**Count**: Dieser Wert ist gleich der Anzahl der gemessenen Flankenwechsel. Das Bricklet kann steigende, 
fallende oder beide Flankenwechsel zählen. Die Richtung des Zählens (hoch oder runter) kann 
eingestellt werden. Für Kanal 0 und 3 ist es möglich einen anderen Kanal als Steuerungseingang für die 
Zählrichtung zu nutzen.

**Duty Cycle**: Ist der prozentuale Anteil des Signals pro Periode der *high* ist.

**Period**: Ist die Dauer eine Periode.

**Frequency**: Ist die Frequenz des Signals, gemessen über eine längere Zeit.

**Value**: Ist der aktuelle Zustand des Kanals (entweder high oder low).

Duty Cycle und Periode werden jeweils für den letzten Zyklus ausgegeben. Die Frequenz wird
über die konfigurierte Frequency Integration Time berechnet. Wenn die Zyklen einen Jitter
besitzen, so zeigen nur Period und Duty Cycle diesen Jitter. Frequency bleibt stabil.

Wenn die Auflösung der Periode hoch genug und die Frequenz stabil ist, so ist
die berechnete Frequenz gleich 1/Period.

Die nachfolgenden Screenshots zeigen verschiedene Messungen eines 12kHz Signals 
mit 60% Tastverhältnis mit einem Oszilloskop

.. image:: /Images/Bricklets/bricklet_industrial_counter_duty_period_freq.jpg
   :scale: 100 %
   :alt: Count, Duty Cycle, Period and Frequency shown on oscilloscope
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_duty_period_freq.jpg

sowie das selbe Signal mit dem Industiral Counter Bricklet über den Brick Viewer. 

.. image:: /Images/Bricklets/bricklet_industrial_counter_duty_period_freq_brickv.jpg
   :scale: 100 %
   :alt: Count, Duty Cycle, Period and Frequency shown on Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_duty_period_freq_brickv.jpg


.. _industrial_counter_bricklet_external_count_direction:

External Count Direction
------------------------

Die Zählrichtung (hoch oder runter) kann konfiguriert und jederzeit geändert werden. Kanal 0
erlaubt es zusätzlich Kanal 2 als Richtungssteuerungseingang zu verwenden. In diesem Fall
wird der Zähler von Kanal 0 inkrementiert (hoch zählen), wenn Kanal 2 *high* ist und dekrementiert
(runter zählen) wenn Kanal 2 *low* ist.

Für Kanal 3 kann Kanal 1 in gleicher Weise als Richtungseingang verwendet werden.


.. _industrial_counter_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun die Kanäle konfiguriert werden und
es sollten die dazugehörigen Zähler angezeigt werden.

.. image:: /Images/Bricklets/bricklet_industrial_counter_brickv.jpg
   :scale: 100 %
   :alt: Industrial Counter Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_brickv.jpg

|test_pi_ref|


.. _industrial_counter_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Counter Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Counter Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Counter.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Counter Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_counter_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Counter_hlpi.table
