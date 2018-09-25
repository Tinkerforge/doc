
.. include:: Thermocouple.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermocouple_bricklet:

Thermocouple Bricklet
=====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermocouple_tilted1_[?|?].jpg          Thermocouple Bricklet
	Bricklets/bricklet_thermocouple_tilted2_[?|?].jpg          Thermocouple Bricklet
	Bricklets/bricklet_thermocouple_horizontal_[?|?].jpg       Thermocouple Bricklet
	Bricklets/bricklet_thermocouple_w_sensor_[100|600].jpg     Thermocouple Bricklet mit Sensor
	Bricklets/bricklet_thermocouple_brickv_[100|].jpg          Thermocouple Bricklet im Brick Viewer
	Dimensions/thermocouple_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Thermocouple Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`Thermocouple Bricklet 2.0 <thermocouple_v2_bricklet>`
 empfohlen.


Features
--------

* Misst Temperatur mit Thermoelement
* Unterstützt B, E, J, K, N, R, S und T Typ


.. _thermocouple_bricklet_description:

Beschreibung
------------

Mit dem Thermocouple :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Temperaturen mittels eines `Thermoelements
<https://de.wikipedia.org/wiki/Thermoelement>`__ messen. Die gemessene
Temperatur kann in `°C
<https://de.wikipedia.org/wiki/Grad_Celsius>`__ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Temperaturänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Die Thermoelementtypen B, E, J, K, N, R, S und T werden unterstützt. Es können
auch benutzerdefiniert Faktoren eingestellt werden. Dadurch können noch andere
oder auch benutzerdefiniert Typen ausgelesen werden.

Fehler, wie fehlendes Thermoelement oder Über-/Unterspannung werden automatisch
erkannt und gemeldet.

Standardmäßig wird das Bricklet mit einem K-Typ Mini-Thermoelementanschluss
ausgeliefert. Dieser Anschluss verwendet Alumel für den negativen und Chromel
für den positiven Kontakt. Auf Wunsch können wir das Bricklet auch mit passendem
Anschluss für andere :ref:`Thermoelementtypen <thermocouple_bricklet_types>`
ausstatten. Es kann Typ J, T, E, U und N gewählt werden. Ist der gewünschte 
Anschluss nicht dabei, so kann das Bricklet auch mit zwei isolieren 20cm Drähten 
geliefert werden. Somit kann auch ein eigener Anschluss angeschlossen werden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MAX31856
Stromverbrauch                    10mW (2mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       -210°C bis +1800°C
Auflösung                         0,01°C
Genauigkeit                       ±0,15% (gesamter Messbereich), ±0,7°C (Cold Junction)
Unterstütze Typen                 B, E, J, K, N, R, S und T (benutzerdefiniert Typen möglich)
Anschluss                         Mini-Thermoelementbuchse
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             40 x 30 x 8mm (1,58 x 1,18 x 0,32")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* MAX31856 Datenblatt (`Download <https://github.com/Tinkerforge/thermocouple-bricklet/raw/master/datasheets/MAX31856.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/thermocouple-bricklet/raw/master/hardware/thermocouple-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/thermocouple_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/thermocouple-bricklet/zipball/master>`__)


.. _thermocouple_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie ein Thermoelement mit dem Thermocouple Bricklet.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_thermocouple_brickv.jpg
   :scale: 100 %
   :alt: Rhermocouple Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_thermocouple_brickv.jpg

|test_pi_ref|


.. _thermocouple_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Thermocouple Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-thermocouple-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_thermocouple_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Thermocouple Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_thermocouple_case_built_up_1000.jpg

.. include:: Thermocouple.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/thermocouple_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Thermocouple Bricklet
   :align: center
   :target: ../../_images/Exploded/thermocouple_exploded.png

|bricklet_case_hint|


.. _thermocouple_bricklet_types:

Thermoelementtypen
------------------

Die verschiedenen Thermoelementtypen unterscheiden sich durch die Metalle
aus denen sie gefertigt sind. Im optimalen Fall ist der Anschluss des
Thermoelements am Bricklet aus den gleichen Metallen gefertigt wie das
Thermoelement selbst.

Standardmäßig wird das Bricklet mit einem K-Typ Mini-Thermoelementanschluss
ausgeliefert (Alumel für den negativen und Chromel für den positiven Kontakt).
An diesen Anschluss kann jegliches Thermoelement angeschlossen werden,
allerdings mit einem leichten Genauigkeitsverlust. Soll aber ein nicht-K-Typ
Thermoelement mit der bestmöglichen Genauigkeit verwendet werden, dann können
wir auf Anfrage das Bricklet auch mit einem anderen Anschluss liefern:

====  ============================  ============================
Typ   Negativer Kontakt             Positiver Kontakt
====  ============================  ============================
B     Platin/Rhodium                Platin/Rhodium
E     Konstantan                    Chromel
J     Konstantan                    Eisen
K     Alumel                        Chromel
N     Nisil                         Nicrosil
R     Platin                        Platin/Rhodium
S     Platin                        Platin/Rhodium
T     Konstantan                    Kupfer
====  ============================  ============================

Bitte vor der Bestellung bei uns melden, wenn ein nicht-K-Typ Anschluss benötigt
wird. Neben K-Type haben wir noch T und J-Typ auf Lager. Andere Anschlusstypen
müssen erst bestellt werden.

.. _thermocouple_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Thermocouple_hlpi.table
