
:shoplink: ../../../shop/bricklets/industrial-quad-relay-v2-bricklet.html

.. include:: Industrial_Quad_Relay_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_quad_relay_v2_bricklet:

Industrial Quad Relay Bricklet 2.1
==================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_quad_relay_v2_tilted_[?|?].jpg           Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_tilted2_[?|?].jpg          Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_side_[?|?].jpg             Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_top_[?|?].jpg              Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_brickv_[100|].jpg          Industrial Quad Relay Bricklet 2.0 im Brick Viewer
	Dimensions/industrial_quad_relay_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 4 Solid State Relais
* Schaltet bis zu 30V mit 0,6A
* Galvanisch getrennt


.. _industrial_quad_relay_v2_bricklet_description:

Beschreibung
------------

Das Industrial Quad Relay :ref:`Bricklet <primer_bricklets>` 2.1 kann benutzt werden
um :ref:`Bricks <primer_bricks>` mit vier galvanisch getrennten Solid State Relais
zu erweitern. Jedes Relais kann bis zu 0,6 `Ampere <https://en.wikipedia.org/wiki/Ampere>`__
mit 30 `Volt <https://en.wikipedia.org/wiki/Volt>`__ schalten.
Die Isolierung des Ausgangs erlaubt eine Nutzung ohne eine direkte elektrische Verbindung,
so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüber hinaus ist eine Nutzung in Bereichen,
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    | 31mW (6.2mA bei 5V)
                                  | + 3mW (0.6mA bei 5V) pro aktiviertem Relais
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Ausgangstyp                       Vier galvanisch getrennte Solid State Relais
Maximaler Schaltstrom             0,6A
Maximale Schaltspannung           30V
Isolation                         1500Vrms (Datenblattangabe)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* CPC1002N Datenblatt (`Download <https://github.com/Tinkerforge/industrial-quad-relay-v2-bricklet/raw/master/datasheets/CPC1002N.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-quad-relay-v2-bricklet/raw/master/hardware/industrial-quad-relay-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_quad_relay_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-quad-relay-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2JSDnZI>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_quad_relay_v2/industrial-quad-relay-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_quad_relay_v2/industrial-quad-relay-v2.FCStd>`__)


Anschlussmöglichkeiten
----------------------

Das Industrial Quad Relay Bricklet besitzt eine 8 Pol Anschlussklemme.
Das nachfolgende Bild erklärt die Pinbelegung:

.. note::
   Ab Version 2.1 muss die Polarität der Last beachtet werden.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_v2_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay 4 2.0 Anschlussmöglichkeiten
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_v2_caption_1200.jpg


Kanal Status LEDs
-------------------

Das Bricklet verfügt über die Standard LED sowie vier weitere LEDs (jeweils eine pro
Relais).

Standardmäßig stellen die vier LEDs den Status der jeweiligen Relais dar. Über die API
können die LEDs aber auch manuell gesteuert werden und zum Beispiel andere Statusinformationen
anzeigen.

.. _industrial_quad_relay_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Für einen einfachen Test schließen wir eine Batterie und eine LED an (siehe nachfolgendes Bild).

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet Setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_setup_1200.jpg

|test_tab|
Anschließend sollte die LED über den Brick Viewer geschaltet werden können.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_v2_brickv.jpg

|test_pi_ref|


.. _industrial_quad_relay_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Quad Relay Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Quad_Relay.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


Änderungen zwischen Version 2.0 und 2.1
---------------------------------------

Version 2.0 war mit vier CPC1020N Solid State Relais ausgestattet,
die über eine maximale Spannung von 30V und einen maximalen Strom von 1.2A
verfügten. Diese Relais waren bidirektional, das heißt eine Polarität musste 
nicht beachtet werden. AC Spannungen konnten diese Relais aber nicht schalten.

Das Industrial Quad Relay Bricklet wurde oft eingesetzt um 24V Ventile o.ä. zu 
schalten. Hierbei handelt es sich um induktive Lasten, die beim Schalten eine 
hohe Spannung erzeugen. Die Maximalspannung von 30V konnte daher überschritten 
werden, ohne das die auf dem Bricklet verbauten Varistoren dies verhindern konnten.

Daher haben wir auf Version 2.1 den Relaistyp geändert. Es kommen nun unipolare 60V
Relais mit einem maximalen Schaltstrom von 0.6A zum Einsatz. Der kleinere Maximalstrom
ist in der Praxis meist nicht relevant, da damit dennoch die meisten Lasten geschaltet 
werden können. Die verdoppelte Maximalspannung macht aber den Unterschied, dass die 
verbauten Varistoren die Spannung wirkungsvoll begrenzen können und somit Ausfälle verhindert
werden.


.. _industrial_quad_relay_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Quad_Relay_V2_hlpi.table
