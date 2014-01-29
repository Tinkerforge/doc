
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starterkit: Blinkenlights
:shoplink: ../../../shop/kits/starter-kit-blinkenlights.html


.. _starter_kit_blinkenlights:

Starterkit: Blinkenlights
==========================

.. note::
 This Starter Kit is currently in the prototype state and the software/hardware
 as well as the documentation is incomplete and may not represent the final
 version.

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/kit_blinkenlights_fire_350.jpg",
	               "Kits/kit_blinkenlights_fire_600.jpg",
	               "Blinkenlights: Feuer Simulation")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_fire_daylight_100.jpg",
	             "Kits/kit_blinkenlights_fire_daylight_600.jpg",
	             "Blinkenlights: Feuer Simulation bei Tageslicht")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_on_wall_100.jpg",
	             "Kits/kit_blinkenlights_on_wall_600.jpg",
	             "Blinkenlights: An der Wand")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_pong_100.jpg",
	             "Kits/kit_blinkenlights_pong_600.jpg",
	             "Blinkenlights: Pong")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_pong_daylight_100.jpg",
	             "Kits/kit_blinkenlights_pong_daylight_600.jpg",
	             "Blinkenlights: Pong bei Tageslicht")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_tetris_100.jpg",
	             "Kits/kit_blinkenlights_tetris_600.jpg",
	             "Blinkenlights: Tetris")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_text_daylight_100.jpg",
	             "Kits/kit_blinkenlights_text_daylight_600.jpg",
	             "Blinkenlights: Text-Anzeige")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_rainbow_near_far_dark_100.jpg",
	             "Kits/kit_blinkenlights_rainbow_near_far_dark_600.jpg",
	             "Blinkenlights: Regenbogen mit verschiedenen Frontpaneln")
	}}
	{{ tfdocend() }}

Features
--------

* Riesiges 40x80cm 200 Pixel RGB Display mit Aktualisierungsraten bis zu 100Hz
* Entwickel Party Spiele, Messe-Auftritte und kundenspezifische Anzeigen
  jeglicher Art
* Frei programmierbar, konfigurierbar und erweiterbar
* Pixel: 12mm Durchmesser, wasserdicht (IP65), voll-farb RGB mit 1600mcd pro p
  Pixel


Beschreibung
------------

Das *Starterkit: Blinkenlights* ist ein großes, freiprogrammierbares Display.
Es besteht aus 200 individuell steuerbare vollfarb RGB LED Pixel, deren Farbe
bis zu 100 mal pro Sekunde geändert werden kann. Es gibt vielfältige 
Anwendungen, dazu zählen das Schreiben von eigenen (Party-) Spielen, 
Messeauftritte, schicke Moodlights oder individuelle Anzeigen aller Art.

Das Basiskit besteht aus einem :ref:`Master Brick <master_brick>`, einem 
:ref:`LED Strip Bricklet <led_strip_bricklet>`, vier 50 LED Pixel Sets, einer 
LED power supply, vier Wandbefestigungs-Platten, einer gelochten Rückplatte,
einer Frontplatte sowie alle notwendigen Kabel und Befestigungsmaterialien.
Das Kasiskit kann per USB von jedem(Embedded-) PC (z.B. 
:ref:`Raspberry Pi <embedded_raspberry_pi>`), Laptop, Server oder Tablet
gesteuert werden.

Über andere Tinkerforge Produkte kann das Kit erweitert werden.
Bei Spiele-Anwendungen kann das 
:ref:`Multi Touch Bricklet <multi_touch_bricklet>` nützlich sein wenn
individuelle Spielsteuerungen realisiert werden sollen. Mit den 
:ref:`Master Brick Extensions <product_overview_master_extensions>` kann die
USB Schnittstelle durch :ref:`Wi-Fi <wifi_extension>` oder
:ref:`Ethernet <ethernet_extension>` ausgetauscht werden, so dass Smartphone 
oder Tablet gesteuerte Anwendungen möglich sind. Ein größeres Display kann durch
das Hinzufügen weiterer Pixel realisiert werden.

Eine :ref:`Demo-Anwendung <starter_kit_blinkenlights_demo_examples>` 
implementiert Clone von `Tetris <http://en.wikipedia.org/wiki/Tetris>`__ und
`Pong <http://en.wikipedia.org/wiki/Pong>`__ und beinhaltet verschiedene
andere Anwendungen. Zum Beispiel können individuelle scrollende Texte in 
diversen Farben, Regenbogen oder individuelle Bildsätze mit konfigurierbarer
Dauer angezeigt werden. Ein virtuelles Feuer erwärmt das Herz auch in den 
kältesten Wintermonaten. Die Spiele können über eine PC Tastatur gesteuert 
werden aber auch per Multi Touch oder Dual Button Bricklet.

Der Kitname "Blinkenlights" wird im 
`Hackerjargon <http://de.wikipedia.org/wiki/Blinkenlights_%28Jargon%29>`__ 
benutzt um blinkende Lampen von Netzwerkequipment zu beschreiben. Er ist auch 
über das
`Blinkenlights Projekt <http://de.wikipedia.org/wiki/Projekt_Blinkenlights>`__
bekannt.

Technische Spezifikation
------------------------

=========================================  ============================================================
Eigenschaft                                Wert
=========================================  ============================================================
Maximale Update Rate (LED Strip Bricklet)  100Hz (pro Pixel)
RGB Auflösung (LED Strip Bricklet)         3 x 8bit
Helligkeit                                 1600mcd pro Pixel
-----------------------------------------  ------------------------------------------------------------
-----------------------------------------  ------------------------------------------------------------
Anzahl der RGB Pixel                       10 x 20
Abmessungen (B x T x H)                    | 40 x 80 x 7cm (ohne Frontpanel)
                                           | 50 x 90 x > 7cm* (mit Frontpanel)
Gewicht                                    TODO
=========================================  ============================================================

\* hängt von dem eingestellten Abstand zwischen Fron- und Rückseite ab

.. _starter_kit_blinkenlights_resources:

Ressourcen
----------

* Beispiel Source Code für :ref:`Tetris <starter_kit_blinkenlights_tetris>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__, `C# <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__)
* Beispiel Source Code für :ref:`Pong <starter_kit_blinkenlights_Pong>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__, `C# <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__)
* Beispiel Source Code für :ref:`Fire <starter_kit_blinkenlights_fire>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/python>`__, `Delphi <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/delphi>`__)
* Beispiel Source Code für :ref:`Scrolling Text <starter_kit_blinkenlights_scrolling_text>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/text/python>`__, `PHP <https://github.com/Tinkerforge/blinkenlights/tree/master/text/php>`__)
* Beispiel Source Code für :ref:`Display Images <starter_kit_blinkenlights_images>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/images/python>`__, `Java <https://github.com/Tinkerforge/blinkenlights/tree/master/images/java>`__)
* :ref:`Demo Anwendung <starter_kit_blinkenlights_demo_examples>` (Download: Windows, Linux, Mac OS X, `Source Code <https://github.com/Tinkerforge/blinkenlights/tree/master/demo>`__)


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe das LED Strip Bricklet an den Master Brick an und verbinde es per USB 
mit dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_plugin>`):

.. image:: /Images/Kits/kit_blinkenlights_update_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Update im Brick Viewer
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_update.jpg

   
Im nächsten Schritt sollte das LED Strip Bricklet und die Pixel wie
:ref:`hier <led_strip_bricklet_test>` beschrieben getestet werden. Anschließend
kann damit begonnen werden das Kit zusammenzubauen.


Konstruktion
------------

.. image:: /Images/Kits/kit_blinkenlights_build_step9_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Konstruktionsschritt mit 40cm Kabel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step9_1200.jpg

Die Aufbauanleitung ist 
:ref:`hier <starter_kit_blinkenlights_construction>` im Detail beschrieben.

.. toctree::
   :hidden:

   Construction


.. _starter_kit_blinkenlights_demo_examples:

Beispielanwendung und Beispielprojekte
--------------------------------------

.. image:: /Images/Kits/blinkenlights_demo_setup_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Setup
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_setup.jpg

Die Demoanwendungen demonstriert verschiedene Anwendungen des Kits. Es besteht
aus 6 Teilanwendungen die als individuelle Projekte zur Verfügung stehen (siehe 
unten). Jedes Projekt wird durch ein eigenes Tab dargestellt. Zwei Dual Button 
Bricklets und ein Multi Touch Bricklet können zusätzlich zur Steuerung der
Spiele genutzt werden. Ist ein Piezo Speaker Bricklet oder ein Segment Display
4x7 Bricklet angeschlossen, so werden diese von den Spielen genutzt um ein 
akustisches Feedback zu geben und den Spielstand anzuzeigen.

Vor Beginn müssen Host und Port konfiguriert werden. Falls das normale Kit 
benutzt wird und dieses direkt per USB an einem PC angeschlossen ist, sind
"localhost" und "4223" die korrekten Einstellungen. Falls das Kit mit
:ref:`Extensions <product_overview_master_extensions>` erweitert wurden oder
es von einem anderen PC gesteuert werden soll muss die IP Adresse oder der 
Hostname des Rechners oder der Extension eingestellt werden zu dem das Kit 
verbunden wurde. Die Tabelle unter der Host/Port Konfiguration gibt einen
überblick über die angeschlossenen Bricks und Bricklets.


.. _starter_kit_blinkenlights_tetris:

Tetris
^^^^^^
Die Demoanwendung implementiert ein typisches 
`Tetris <http://de.wikipedia.org/wiki/Tetris>`__ mit allen Besonderheiten.
Es kann mit:

.. image:: /Images/Kits/kit_blinkenlights_tetris_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris
   :align: center

oder ohne Frontpanel:

.. image:: /Images/Kits/kit_blinkenlights_tetris_wo_frontpanel_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris
   :align: center

gespielt werden.

Dieser Tetris-Clone kann über drei verschiedene Arten gesteuert werden. Als 
erstes können die Buttons im Tab genutzt werden um das Spiel zu steuern.
Alternativ funktioniert dies auch über die PC Tastatur ("a" ist zum Beispiel 
links). Als letzte Möglichkeit kann ein Mutli Touch Bricklet angeschlossen 
werden (Elektrode 0 ist zum Beispiel links).

.. image:: /Images/Kits/blinkenlights_demo_tetris_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demo Anwendung: Tetris
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_tetris.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__
heruntergeladen werden. Dieses beinhaltet auch das 
:ref:`Pong <starter_kit_blinkenlights_pong>` Project und beseht hauptsächlich 
aus zwei Dateien: ``tetris.py`` implementiert das Spiel und ``config.py`` 
definiert Konfigurationen (Host, Port, UIDs, LED Matrixlayout und Keymap).

Die ``config.py`` muss entprechend angepasst werden und die Anwendung mittels:

.. code-block:: python

   python tetris.py

ausgeführt werden.

Zusätzlich ist dieses Projekt in :ref:`C# <api_bindings_csharp>` implementiert
worden. Diese kann von `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__
heruntergeladen werden.


.. _starter_kit_blinkenlights_pong:

Pong
^^^^

Wie :ref:`Tetris <starter_kit_blinkenlights_tetris>` kann
`Pong <http://en.wikipedia.org/wiki/Pong>`__ mit oder ohne Frontpanel genutzt 
werden.

Die folgenden Bilder zeigen Pong bei Dunkelheit und Tageslicht.

.. image:: /Images/Kits/kit_blinkenlights_pong_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Pong
   :align: center


.. image:: /Images/Kits/kit_blinkenlights_pong_daylight_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Pong bei Tageslicht
   :align: center

Das Spiel kann über Buttons, Tastatur oder Multi Touch Bricklet gesteuert
werden. Zusätzlich ist eine Steuerung über Dual Button Bricklets möglich.

.. image:: /Images/Kits/blinkenlights_demo_pong_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Pong
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_pong.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__.
heruntergeladen werden. Dieses beinhaltet das
:ref:`Tetris <starter_kit_blinkenlights_tetris>` Projekt und besteht 
hauptsächlich aus zwei Dateien: ``pong.py`` implementiert das Spiel und
``config.py`` definiert Konfigurationen (Host, Port, UIDs, LED Matrixlayout 
und Keymaps).


Die ``config.py`` muss entprechend angepasst werden und die Anwendung mittels:

.. code-block:: python

   python pong.py

gestartet werden. Zusätzlich ist dieses Projekt in 
:ref:`C# <api_bindings_csharp>` implementiert worden und kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__
herunter geladen werden.


.. _starter_kit_blinkenlights_fire:

Feuer Simulation
^^^^^^^^^^^^^^^^

Wenn das Fire Tab gewählt wird erscheint eine Feuersimulation. Diese sieht
besonders gut aus, wenn das Frontpanel in einem Abstand von 
42mm (2x9mm und 2x12mm Abstandsbolzen) zur Rückseite angebracht wird.

Die folgenden Bilder zeigen die Feuersimulation bei Dunkelheit und bei 
Tageslicht.

.. image:: /Images/Kits/kit_blinkenlights_fire_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Feuer Simulation
   :align: center


.. image:: /Images/Kits/kit_blinkenlights_fire_daylight_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Feuer Simulation bei Tageslicht
   :align: center

Die Simulation bastiert auf einem Partikelsystem und kann über vier 
Schieberegler beeinflusst werden:

* **Frame Rate**:
  Definiert die Bildrate in Hz. Die Simulation wird jedes neue Bild (frame)
  aktualisiert. Wenn die Bildrate erhöht wird, dann brennt das Feuer schneller.

* **Hue**:
  Definiert die Farbe des Feuers.

* **Start**:
  Definiert die Startposition der Feuerpartikel.

* **End**:
  Definiert die Position bei dem die Feuerpartikel ausgehen.

Spiele mit den Schiebereglern und erstelle dein persönliches Feuer. Mit dem
"Default" Button können die Regler wieder auf die Ausgangswerte zurückgesetzt
werden.

.. image:: /Images/Kits/blinkenlights_demo_fire_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Fire
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_fire_1200.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/python>`__
heruntergeladen werden. Es besteht hauptsächlich aus zwei Dateien:
``fire.py`` implementiert die Feuersimulation und ``config.py`` konfiguriert
Host, Port, UID, LED Matrixlayout und Simulationsparameter.

Nach dem Anpassen der ``config.py`` kann die Anwendung mittels:

.. code-block:: python

   python fire.py

ausgeführt werden. Das Projekt ist auch in :ref:`Delphi <api_bindings_delphi>` 
implementiert worden und kann von `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/fire/delphi>`__
heruntergeladen werden.


.. _starter_kit_blinkenlights_scrolling_text:

Scrolling Text
^^^^^^^^^^^^^^

Die "Text" Demo scrollt den eingegebenen Text in der angegebenen 
Geschwindigkeit.

.. image:: /Images/Kits/kit_blinkenlights_text_daylight_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Text Demo
   :align: center

Der Text bewegt sich eine Spalte pro Frame. Eine höhere Framerate führt also zu
einem schneller bewegenden Text. Dauerhafte Farbwechsel können über klicken auf
"Rainbow" aktiviert werden. Alternativ kann auch eine Farbe direkt gewählt 
werden.

.. image:: /Images/Kits/blinkenlights_demo_text_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Text
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_text.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von Github
heruntergeladen werden
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/text/python>`__.
Es besteht ebenfalls hauptsächlich aus zwei Dateien: ``text.py`` implementiert
die Logik und ``config.py`` definiert Host, Port, UID, LED Matrixlayout und
Farbparameter.

Nach Anpassen der ``config.py`` kann die Anwendung wie folgt gestartet werden:

.. code-block:: python

   python text.py Starter Kit: Blinkenlights

Das Demo ist auch in :ref:`PHP <api_bindings_php>` implementiert worden und kann
von `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/text/php>`__ 
heruntergeladen werden.


.. _starter_kit_blinkenlights_images:

Bilder anzeigen
^^^^^^^^^^^^^^^

Das "Images" Demo kann genutzt werden um spezifische Bilder und ganze 
Animationen angezeigt werden.

Das folgende Bild

.. image:: /Images/Kits/kit_blinkenlights_heart_input.png
   :scale: 100 %
   :alt: Blinkenlights Herz Eingabe
   :align: center

generiert folgende Ausgabe

.. image:: /Images/Kits/kit_blinkenlights_heart_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Herz
   :align: center

Wähle die Bilder, die angezeigt werden sollen, durch Klicken auf 
"Choose images...". Die Demo zeigt das erste Bild an und wechselt in der 
angegebenen Framerate zum nächsten Bild in der Reihe. Auf diese Art können
Animationen erstellt werden. Jedes Bild wird auf eine Größe von 20x10 Pixel
(Größe des Displays) verkleinert und verzerrt falls das Bildformat nicht passt.
Ein Bildverarbeitungstool kann benutzt werden wenn die Ergebnisse nicht 
zufriedenstellend sind.

.. image:: /Images/Kits/blinkenlights_demo_images_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Images
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_images.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/images/python>`__
heruntergeladen werden. Es besteht hauptsächlich aus zwei Dateien:
``images.py`` implementiert die Logik und ``config.py`` definiert wie bei den
anderen Beispielprojekten auch Host, Port, UID und das LED Matrixlayout.

Nach Anpassen der ``config.py`` kann das Demo mit den anzuzeigenden Bildern wie 
folgt gestartet werden:

.. code-block:: python

   python text.py image1.jpg image2.jpg

Zusätzlich wurde das Projekt in :ref:`Java <api_bindings_java>` implementiert
und kann bei `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/text/java>`__ 
heruntergeladen werden.


.. _starter_kit_blinkenlights_scrolling_rainbow:

Moving Rainbow
^^^^^^^^^^^^^^

The "Rainbow" demo will display a moving rainbow with the given frame rate
and speed. The results depend on the distance to the front panel. 

The following image shows the rainbow demo with 12mm distance in daylight, 
42mm distance in daylight and with 42mm distance during darkness.

.. image:: /Images/Kits/kit_blinkenlights_rainbow_near_far_dark_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Rainbow Demo
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_rainbow_near_far_dark_1200.jpg

A higher frame rate and speed results in faster moving rainbow.

.. image:: /Images/Kits/blinkenlights_demo_rainbow_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Rainbow
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_rainbow.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/rainbow/python>`__.
It consists of mainly two files: ``rainbow.py`` implements the logic and
``config.py`` defines the configuration (host, port, UID, LED matrix layout and
speed parameter).

Modify the ``config.py`` according to your needs and run the application:

.. code-block:: python

   python rainbow.py

There is also a :ref:`C <api_bindings_c>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/rainbow/c>`__.


Further Enhancements
--------------------

If you modded, extended or improved your Blinkenlights installation in any way and you
have published your results on our `Wiki <http://www.tinkerunity.org/wiki/>`__,
on your blog or similar: Please give us a notice. We would love to add a link
to your project here!
