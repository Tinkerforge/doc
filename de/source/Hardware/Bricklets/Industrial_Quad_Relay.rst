
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Quad Relay Bricklet
:shoplink: ../../../shop/bricklets/industrial-quad-relay-bricklet.html

.. include:: Industrial_Quad_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_quad_relay_bricklet:

Industrial Quad Relay Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_quad_relay_tilted_[?|?].jpg           Industrial Quad Relay Bricklet
	Bricklets/bricklet_industrial_quad_relay_vertical_[?|?].jpg         Industrial Quad Relay Bricklet
	Bricklets/bricklet_industrial_quad_relay_horizontal_[?|?].jpg       Industrial Quad Relay Bricklet
	Bricklets/bricklet_industrial_quad_relay_setup_[?|?].jpg            Industrial Quad Relay Bricklet Setup
	Cases/bricklet_industrial_case_[100|600].jpg                        Industrial Quad Relay Bricklet im Gehäuse
	Bricklets/bricklet_industrial_quad_relay_brickv_[100|].jpg          Industrial Quad Relay Bricklet im Brick Viewer
	Dimensions/industrial_quad_relay_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 4 Solid State Relais
* Schaltet bis zu 30V mit 1,2A
* Galvanisch getrennt
* Gruppierbar


.. _industrial_quad_relay_bricklet_description:

Beschreibung
------------

Das Industrial Quad Relay :ref:`Bricklet <primer_bricklets>` kann benutzt werden
um :ref:`Bricks <primer_bricks>` mit vier galvanisch getrennten Solid State Relais
zu erweitern. Jedes Relais kann bis zu 1,2 `Ampere <https://en.wikipedia.org/wiki/Ampere>`__
mit 30 `Volt <https://en.wikipedia.org/wiki/Volt>`__ schalten.
Die Isolierung des Ausgangs erlaubt eine Nutzung ohne eine direkte elektrische Verbindung,
so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüber hinaus ist eine Nutzung in Bereichen,
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.

Wenn mehr als vier Relais benötigt werden kann ein weiteres Industrial Quad Relay
Bricklet mit angeschlossen und gruppiert werden. Anschließend ist es möglich
8 Relais simultan zu setzen anstatt zwei mal 4 Relais hintereinander zu setzen.
Die Gruppierung kann nur pro Brick erfolgen, so dass an einem Master Brick
maximal 4, an anderen Bricks 2 Industrial Bricklets gruppiert werden können.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Solid State Relais                CPC1020N
Stromverbrauch                    2mA (pro Relais)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Ausgangstyp                       Vier galvanisch getrennte Solid State Relais
Maximaler Schaltstrom             1,2A
Maximale Schaltspannung           30V
Isolation                         1500Vrms (Datenblattangabe)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* CPC1020N Datenblatt (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/raw/master/datasheets/CPC1020N.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/raw/master/hardware/industrial-quad-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_quad_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BEE1de>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_quad_relay/industrial-quad-relay.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_quad_relay/industrial-quad-relay.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Quad Relay Bricklet besitzt eine 8 Pol Anschlussklemme.
Das nachfolgende Bild erklärt die Pinbelegung:

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay 4 Pinbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_caption_1200.jpg


.. _industrial_quad_relay_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Für einen einfachen Test werden wir eine Batterie und eine LED anschließen (siehe nachfolgendes Bild).


.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet Setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_setup_1200.jpg

|test_tab|

Anschließend sollte die LED über den Brick Viewer geschaltet werden können.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg

|test_pi_ref|

.. _industrial_quad_relay_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Quad Relay Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__
ist verfügbar.

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


.. _industrial_quad_relay_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Quad_Relay_hlpi.table
