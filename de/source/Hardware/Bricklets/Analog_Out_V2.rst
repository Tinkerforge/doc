
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Analog Out Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/analog-out-v2-bricklet.html

.. include:: Analog_Out_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_out_v2_bricklet:

Analog Out Bricklet 2.0
=======================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Erzeugt konfigurierbare elektrische Spannungen zwischen 0V und 12V*
* Angabe in 1mV Schritten (12Bit Auflösung)


.. _analog_out_v2_bricklet_description:

Beschreibung
------------

Das Analog Out :ref:`Bricklet <primer_bricklets>` 2.0 kann genutzt werden
um :ref:`Bricks <primer_bricks>` mit einem 12Bit `Digital-Analog-Wandler
<http://de.wikipedia.org/wiki/Digital-Analog-Umsetzer>`__ zu erweitern.
Es ist der Nachfolger des :ref:`analog_out_bricklet` mit größerem
Ausgangsspannungsbereich.
Mit diesem können elektrische Spannungen von 0V bis 12V* generiert werden.
Die Spannung kann direkt in `Volt <http://en.wikipedia.org/wiki/Volt>`__
angegeben werden.

Für Ausgangsspannungen über 5V muss eine zusätzliche externe Spannungsquelle
angeschlossen werden. Die maximal erreichbare Ausgangsspannung entspricht der
Versorgungsspannung. Soll z.b. 12V ausgegeben werden, so muss das Bricklet
auch mit mindestens 12V versorgt werden.
Für Ausgangsspannungen bis 5V können die :ref:`5V und VIN Anschlussklemmen
<analog_out_v2_bricklet_connectivity>` verbunden werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
D/A-Wandler                       MCP4725
Stromverbrauch                    < 5mW (< 1mA bei 5V, ohne Last)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Spannung                          0V - 12V* in 1mV Schritten, 12Bit Auflösung
Maximaler Ausgangsstrom           24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           35 x 30 x 14mm (1,38 x 1,18 x 0,55")
Gewicht                           8g
================================  ============================================================

\* Die maximale Spannung hängt von der Versorgungsspannung an VIN ab.


Ressourcen
----------

* MCP4725 Datenblatt (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/hardware/analog-out-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog_out_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/zipball/master>`__)


.. _analog_out_v2_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das Analog Out Bricklet 2.0 hat fünf Anschlussklemmen. Eine
Gleichspannungsquelle (maximal 15V) muss an die VIN und die dazugehörige GND
Anschlussklemme angeschlossen werden. Das Bricklet verwendet diese
Eingangsspannung um die einstellbare Ausgangsspannung an der VOUT
Anschlussklemme zu erzeugen. Die 5V Anschlussklemme stellt 5V bereit. Diese
können z.B. genutzt werden, um die VIN Anschlussklemme zu versorgen, so dass
Ausgangsspannung bis zu 5V an VOUT ausgegeben werden können, ohne zusätzliche
externe Spannungsquelle.

.. image:: /Images/Bricklets/bricklet_analog_out_v2_horizontal_350.jpg
    :scale: 100 %
    :alt: Analog Out Bricklet 2.0 Anschlussklemmen
    :align: center
    :target: ../../_images/Bricklets/bricklet_analog_out_v2_horizontal_1200.jpg


.. _analog_out_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Zusätzlich muss eine Gleichspannungsquelle an die VIN und GND Anschlussklemmen
des Bricklets angeschlossen werden. Als Test kann die 5V Anschlussklemme mit
der VIN Anschlussklemme verbunden werden. Die GND Anschlussklemmen sind intern
bereits verbunden.

|test_tab|
Auf diesem Tab kann die Ausgangsspannung an der VOUT Anschlussklemme
eingestellt werden. Die maximale VOUT Ausgangsspannung ist begrenzt durch die
Eingangsspannung an der VIN Anschlussklemme.

Zu Testzwecken kann die VOUT Ausgangsspannung mit einem Voltmeter gemessen
werden. Wenn alles wie erwartet funktioniert sollte die eingestellte Spannung
mit der Messung des Voltmeters übereinstimmen.

.. image:: /Images/Bricklets/bricklet_analog_out_v2_brickv.jpg
   :scale: 100 %
   :alt: Analog Out Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_out_v2_brickv.jpg

|test_pi_ref|


.. _analog_out_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Analog Out Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-analog-in-out-v2-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_analog_in_v2_case_build_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_v2_case_build_up_1000.jpg

.. include:: Analog_Out_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/analog_in_v2_exploded.png

|bricklet_case_hint|


.. _analog_out_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Analog_Out_V2_hlpi.table
