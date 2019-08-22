
:shoplink: ../../../shop/bricklets/multi-touch-bricklet.html

.. include:: Multi_Touch.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _multi_touch_bricklet:

Multi Touch Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_multi_touch_tilted_[?|?].jpg           Multi Touch Bricklet
	Bricklets/bricklet_multi_touch_vertical_[?|?].jpg         Multi Touch Bricklet
	Bricklets/bricklet_multi_touch_horizontal_[?|?].jpg       Multi Touch Bricklet
	Bricklets/bricklet_multi_touch_tilted_back_[?|?].jpg      Multi Touch Bricklet
	Cases/bricklet_multi_touch_case_tilted_[?|?].jpg          Multi Touch Bricklet im Gehäuse
	Bricklets/button_pad_w_multi_touch_tilted_[?|?].jpg       Multi Touch Bricklet mit Button Pads
	Bricklets/cursor_pad_w_cable_[100|600].jpg                Cursor Pad mit Kabel
	Bricklets/key_pad_w_multi_touch_[100|600].jpg             Multi Touch Bricklet mit Key Pad
	Bricklets/slider_pad_w_multi_touch_[100|600].jpg          Multi Touch Bricklet mit Slider Pad
	Bricklets/bricklet_multi_touch_brickv_[100|].jpg          Multi Touch Bricklet im Brick Viewer
	Dimensions/multi_touch_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Multi Touch Bricklet ist abgekündigt. Wir verkaufen noch unseren restlichen Lagerbestand.
 Als Ersatz wird das :ref:`Multi Touch Bricklet 2.0 <multi_touch_v2_bricklet>`
 empfohlen.


Features
--------

* Kapazitiver Touch Sensor
* Unterstützt bis zu 12 Elektroden nutzbar als Touchflächen 
* Berührung kann durch eine dünne Schicht Glas/Plastik/Papier erkannt werden
* Größe und Positionierung der Berührungsfläche wird vom Nutzer festgelegt
* Kann genutzt werden um ein maßgeschneidertes Touchpanel zu bauen


.. _multi_touch_bricklet_description:

Beschreibung
------------

Das Multi Touch :ref:`Bricklet <primer_bricklets>` ist mit dem MPR121
Capacitive Touch Sensor ausgestattet und erweitert 
:ref:`Bricks <primer_bricks>`. Es kann genutzt werden um Berührungen an 12 
unterschiedlichen Stellen zu erkennen.

Das zu berührende Teil wird "Elektrode" genannt. Die Elektrode kann
ein Kabel, elektrisch leitendes Klebeband oder die Kupferlage einer 
Leiterplatte sein. Elektroden können eine Berührung durch eine dünne
Schicht Glas, Plastik, Papier o.ä. erkennen.

Mit dem Multi Touch Bricklet ist es möglich eine individuelles Touchpanel
zu bauen, in dem man eine dünne Abdeckung auf die Elektroden klebt.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MPR121
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Anzahl Elektroden                 12 + simulierte 13te Elektrode für Naherkennung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 7mm (1,18 x 0,98 x 0,28")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* MPR121 Datenblatt (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/raw/master/datasheets/MPR121.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/raw/master/hardware/multi-touch-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/multi_touch_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/zipball/master>`__)


.. _multi_touch_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Bei Berührung von einzelnen Pins des Multi Touch Bricklets sollte sich der 
angezeigte Zustand im Brick Viewer verändern:

.. image:: /Images/Bricklets/bricklet_multi_touch_brickv.jpg
   :scale: 100 %
   :alt: Multi Touch Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_brickv.jpg

|test_pi_ref|


Eigene Touchpads / Empfindlichkeit einstellen
---------------------------------------------

Einfache Touchpads können mittels abisolierter Drähte erzeugt werden. Dazu
wird der Draht mit `Aluminium Klebeband
<https://www.tinkerforge.com/de/shop/accessories/sensors/aluminum-tape-1m.html>`__
auf einer Oberfläche festgeklebt. Die Aluminium Fläche dient dann als Touch Pad.
Da es sich um eine kapazitive Technologie
handelt können die erzeugten Flächen mit dünnen nicht-leitenden Materialien
bedeckt werden. Ist die Empfindlichkeit dieser Pads zu hoch kann einfach ein 
Teil des Klebebands entfernt werden oder die Sensitivität per Software
reduziert werden.

Das nachfolgende Bild zeigt den grundsätzlichen Aufbau eines Touchpads:

.. image:: /Images/Bricklets/bricklet_multi_touch_custom_pad2_350.jpg
   :scale: 100 %
   :alt: Touch Pad für das Multi Touch Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_custom_pad2_1200.jpg

Abhängig vom Aufbau der Touchpads kann es notwendig sein die Empfindlichkeit
einzustellen. Die Brick Viewer Software kann genutzt werden um verschiedene 
Empfindlichkeiten auszuprobieren. Dazu muss nur der Electrode Sensitivity Wert
geändert und mittels "Recalibrate" übertragen werden.

.. _multi_touch_bricklet_circuit_board_pads:

Leiterplatten Pads
------------------

.. image:: /Images/Bricklets/cursor_pad_w_cable_350.jpg
   :scale: 100 %
   :alt: Cursor Pad mit Kabel
   :align: center
   :target: ../../_images/Bricklets/cursor_pad_w_cable_1200.jpg

Verschiedene Leiterplatten-Pads werden im Shop angeboten, die als Touchpads
für das Multi Touch Bricklet genutzt werden können ohne das eigene Pads
hergestellt werden müssen.

 * `Cursor Pad <https://www.tinkerforge.com/de/shop/cursor-pad.html>`__
 * `Key Pad 3x4 <https://www.tinkerforge.com/de/shop/key-pad-3x4.html>`__
 * `Slider Pad <https://www.tinkerforge.com/de/shop/slider-pad.html>`__
 * `Button Pad <https://www.tinkerforge.com/de/shop/button-pad.html>`__

Für Spiele-Anwendungen gibt es ein spezielles Pad-Kit:

 * `Giant Game Pad (siehe unten) <https://www.tinkerforge.com/de/shop/giant-game-pad.html>`__

.. _multi_touch_bricklet_giant_game_pad:

Benutzung des Giant Game Pads
-----------------------------

.. image:: /Images/Kits/ggp_table_top_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad auf einem Tisch
   :align: center
   :target: ../../_images/Kits/ggp_table_top_1200.jpg

Das Giant Game Pad Kit besteht aus verschiedenen Pads, hergestellt aus 3mm PMMA.
Neben den Pads sind 10m Litze, zwei Streifen Aluminiumklebeband und eine 12pol
Pfostenbuchse im Kit enthalten.

.. image:: /Images/Kits/ggp_content_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad Kit Inhalt
   :align: center
   :target: ../../_images/Kits/ggp_content_1200.jpg

Um aus diesen Teilen Touchpads herzustellen müssen die 10m Litze in 12 
Abschnitte geteilt werden. Anschließend müssen einseitig jeweils 5cm abisoliert 
werden. Jedes Pad wird von der Unterseite mit Aluminiumklebeband beklebt.
Die Abisolierten Drahtenden werden dabei mit dem Klebeband eingeklebt. Zu Anfang
sollte nicht die volle Fläche beklebt werden.

.. image:: /Images/Kits/ggp_pad_bottom_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad Ansicht von Unten
   :align: center
   :target: ../../_images/Kits/ggp_pad_bottom_1200.jpg

Anschließend werden die Litzen in die Pfostenbuchse gesteckt und diese
zusammengedrückt. Dazu kann ein kleiner Schraubstock o.ä. hilfreich sein.

.. image:: /Images/Kits/ggp_connector_crimp_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad Pfostenbuchse
   :align: center
   :target: ../../_images/Kits/ggp_connector_crimp_1200.jpg


Nach diesem Schritt ist das Giant Game Pad fertiggestellt. Falls gewünscht
können die mitgelieferten Gummifüße unter die Pads geklebt werden um ein
Rutschen der Pads zu vermeiden.

.. image:: /Images/Kits/ggp_table_front_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad auf einem Tisch
   :align: center
   :target: ../../_images/Kits/ggp_table_front_1200.jpg

Abhängig von der Kabellänge muss die Sensitivität für die Pads angepasst werden.
Dies kann allgemein per Software geschehen und für jedes Pad einzeln über die
Aluminiumfläche.

.. _multi_touch_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Multi Touch Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-multi-touch-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_multi_touch_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Multi Touch Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_multi_touch_case_tilted_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet,
* baue Seitenteile auf mit Bricklet uns Sensor in der Mitte,
* schraube Unterteil an untere Abstandshalter,
* schraube Oberteil auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Multi Touch Bricklet-Gehäuse:

.. image:: /Images/Exploded/multi_touch_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Multi Touch Bricklet
   :align: center
   :target: ../../_images/Exploded/multi_touch_exploded.png

|bricklet_case_hint|


.. _multi_touch_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Multi_Touch_hlpi.table
