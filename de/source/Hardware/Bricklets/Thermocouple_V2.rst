
:shoplink: ../../../shop/bricklets/thermocouple-v2-bricklet.html

.. include:: Thermocouple_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermocouple_v2_bricklet:

Thermocouple Bricklet 2.0
=========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermocouple_v2_tilted_[?|?].jpg           Thermocouple Bricklet 2.0
	Bricklets/bricklet_thermocouple_v2_tilted2_[?|?].jpg          Thermocouple Bricklet 2.0
	Bricklets/bricklet_thermocouple_v2_side_[?|?].jpg             Thermocouple Bricklet 2.0
	Bricklets/bricklet_thermocouple_v2_top_[?|?].jpg              Thermocouple Bricklet 2.0
	Cases/bricklet_thermocouple_v2_case_[?|?].jpg                 Thermocouple Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_thermocouple_v2_brickv_[100|].jpg          Thermocouple Bricklet 2.0 im Brick Viewer
	Dimensions/thermocouple_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Temperatur mit Thermoelement
* Unterstützt B, E, J, K, N, R, S und T Typ


.. _thermocouple_v2_bricklet_description:

Beschreibung
------------

Mit dem Thermocouple :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` Temperaturen mittels eines `Thermoelements
<https://de.wikipedia.org/wiki/Thermoelement>`__ messen. Die gemessene
Temperatur kann in `°C
<https://de.wikipedia.org/wiki/Grad_Celsius>`__ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Temperaturänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Die Thermoelementtypen B, E, J, K, N, R, S und T werden unterstützt. Es können
auch benutzerdefiniert Faktoren eingestellt werden. Dadurch können noch andere
oder auch benutzerdefiniert Typen ausgelesen werden.

Fehler, wie ein fehlendes Thermoelement oder Über-/Unterspannung werden automatisch
erkannt und gemeldet.

Standardmäßig wird das Bricklet mit einem K-Typ Mini-Thermoelementanschluss
ausgeliefert. Dieser Anschluss verwendet Alumel für den negativen und Chromel
für den positiven Kontakt. Auf Wunsch können wir das Bricklet auch mit passendem
Anschluss für andere :ref:`Thermoelementtypen <thermocouple_v2_bricklet_types>`
ausstatten. Es kann Typ J, T, E, U und N gewählt werden. Ist der gewünschte 
Anschluss nicht dabei, so kann das Bricklet auch mit zwei isolierten 20cm Drähten 
geliefert werden. Somit kann auch ein eigener Anschluss angeschlossen werden.

Das Bricklet verfügt über keine galvanische Trennung zum Tinkerforge System. 
Das heißt es gibt eine direkte elektrische Verbindung zwischen den 
Anschlussklemmen des Bricklets und dem restlichen System. Sollte dies in der 
jeweiligen Anwendung zu ungewollten Verbindungen, Masseschleifen oder 
Kurzschlüssen führen, so ist der Einsatz zusammen mit einem :ref:`Isolator Bricklet <isolator_bricklet>` ratsam.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MAX31856
Stromverbrauch                    45mW (9mA bei 5V)
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
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* MAX31856 Datenblatt (`Download <https://github.com/Tinkerforge/thermocouple-bricklet/raw/master/datasheets/MAX31856.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/thermocouple-v2-bricklet/raw/master/hardware/thermocouple-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/thermocouple_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/thermocouple-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rAevPA>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/thermocouple_v2/thermocouple-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/thermocouple_v2/thermocouple-v2.FCStd>`__)


.. _thermocouple_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie ein Thermoelement mit dem Thermocouple Bricklet.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_thermocouple_v2_brickv.jpg
   :scale: 100 %
   :alt: Thermocouple Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_thermocouple_v2_brickv.jpg

|test_pi_ref|


.. _thermocouple_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Thermocouple Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-thermocouple-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_thermocouple_v2_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Thermocouple Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_thermocouple_v2_case_1000.jpg

.. include:: Thermocouple_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/thermocouple_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Thermocouple Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/thermocouple_exploded.png

|bricklet_case_hint|



.. _thermocouple_v2_bricklet_types:

Thermoelement Typen
-------------------

Je nach Thermoelement-Art werden verschiedene Metalle für die Drähte verwendet. Optimalerweise
nutzt der Stecker des Bricklets die gleichen Metalle.

Normalerweise ist das Bricklet mit einer Mini K-Typ Thermoelement-Buchse ausgestattet 
(Alumel für den negative und Chromel für den positiven Anschluss). Es können auch andere 
Thermoelemente an die Buchse angeschlossen werden, allerdings führt dieses zu einem kleinen 
Messfehler. Aus diesem Grund bieten wir für andere Thermoelemente andere Buchsen an:

====  ============================  ============================
Typ   Negativer Kontakt             Positiver Kontakt
====  ============================  ============================
B     Platin/Rhodium                Platin/Rhodium
E     Konstantan                    Chromel
J     Konstantan                    Eisel
K     Alumel                        Chromel
N     Nisil                         Nicrosil
R     Platin                        Platin/Rhodium
S     Platin                        Platin/Rhodium
T     Konstantan                    Kupfer
====  ============================  ============================

Wenn eine andere Buchse, wie der K-Typ verwendet werden soll, so kann im Shop
direkt der passende Typ gewählt werden. Ist dieser nicht dabei, können wir auf 
Anfrage das Bricklet mit der korrekten Buchse ausstatten.


.. _thermocouple_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Thermocouple_V2_hlpi.table
