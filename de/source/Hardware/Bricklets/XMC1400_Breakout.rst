
:shoplink: ../../../shop/bricklets/xmc1400-breakout-bricklet.html

.. include:: XMC1400_Breakout.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _xmc1400_breakout_bricklet:

XMC1400 Breakout Bricklet
=========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_xmc1400_breakout_tilted_[?|?].jpg           XMC1400 Breakout Bricklet
	Bricklets/bricklet_xmc1400_breakout_top_[?|?].jpg              XMC1400 Breakout Bricklet
	Bricklets/bricklet_xmc1400_breakout_brickv_[100|].jpg          XMC1400 Breakout Bricklet im Brick Viewer
	Dimensions/xmc1400_breakout_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Bricklet Entwicklungsboard
* Nutzbar um eigene Bricklets zu entwickeln


.. _xmc1400_breakout_bricklet_description:

Beschreibung
------------

Das XMC1400 Breakout :ref:`Bricklet <primer_bricklets>` ist ein Breakout-Board
für Infineons XMC1400 Mikrocontroller im Bricklet-Formfaktor.

Das Bricklet kann als Basis dienen um neue Bricklets zu entwickeln.

Ausgestattet ist das Bricklet mit dem Standard-Brickletstecker, einer Status-LED,
einem 16MHz Quarz und einem Bootpad. Der Bootloader und eine Beispielfirmware sind bereits auf dem Bricklet
vorhanden. Alle zur Verfügung stehenden Pins sind nach außen geführt und können
über Stiftleisten angeschlossen werden.

Wenn ein eigenes Bricklet entwickelt werden soll, kann das Board als Einstieg dienen,
da nicht direkt eigene Hardware entwickelt werden muss.

Das XMC1400 Breakout Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    55mW (11mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Anzahl verfügbarer I/Os           42
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           50 x 45 x 15mm (1,97 x 1,77 x 0,59")
Gewicht                           12g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/xmc1400-breakout-bricklet/raw/master/hardware/xmc1400-breakout-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/xmc1400_breakout_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/xmc1400-breakout-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2TzY9Dl>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/xmc1400_breakout/xmc1400-breakout.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/xmc1400_breakout/xmc1400-breakout.FCStd>`__)


.. _xmc1400_breakout_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird das Beispiel Brick Viewer Plugin angezeigt.

	.. image:: /Images/Bricklets/bricklet_xmc1400_breakout_brickv.jpg
	   :scale: 100 %
	   :alt: XMC1400 Breakout Bricklet im Brick Viewer
	   :align: center
	   :target: ../../_images/Bricklets/bricklet_xmc1400_breakout_brickv.jpg

|test_pi_ref|


.. _xmc1400_breakout_bricklet_tutorial:

Tutorial: Eine Getter Funktion hinzufügen
-----------------------------------------

.. note::

 Dieses Tutorial ist leider noch nicht vollständig. Bei Interesse schreibe
 bitte eine E-Mail an info@tinkerforge.com, so wissen wir, dass Interesse
 besteht.

Es ist geplant ein Tutorial hier zu präsentieren, indem der ganze Prozess,
wie API Funktionen hinzugefügt werden können, dargestellt wird:

* Getter-Funktion zum Generator hinzufügen
* Stubs generieren/kopieren
* Stub-Funktion in der Firmware implementieren
* Bindings-Generieren
* Programm für neue Bindings schreiben
* GUI-Element im Brick Viewer hinzufügen, welches den Getter nutzt



.. _xmc1400_breakout_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: XMC1400_Breakout_hlpi.table
