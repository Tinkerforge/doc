
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#starterkits">Starterkits</a> / Starterkit: Blinkenlights
:shoplink: ../../../shop/kits/starter-kit-blinkenlights.html


.. _starter_kit_blinkenlights:

Starterkit: Blinkenlights
==========================

.. raw:: html

	{% tfgallery %}

	Kits/kit_blinkenlights_fire_[100|600].jpg                   Blinkenlights: Feuer Simulation
	Kits/kit_blinkenlights_fire_daylight_[100|600].jpg          Blinkenlights: Feuer Simulation bei Tageslicht
	Kits/kit_blinkenlights_on_wall_[100|600].jpg                Blinkenlights: An der Wand
	Kits/kit_blinkenlights_pong_[100|600].jpg                   Blinkenlights: Pong
	Kits/kit_blinkenlights_pong_daylight_[100|600].jpg          Blinkenlights: Pong bei Tageslicht
	Kits/kit_blinkenlights_tetris_[100|600].jpg                 Blinkenlights: Tetris
	Kits/kit_blinkenlights_text_daylight_[100|600].jpg          Blinkenlights: Text-Anzeige
	Kits/kit_blinkenlights_rainbow_near_far_dark_[100|600].jpg  Blinkenlights: Regenbogen mit verschiedenen Frontplatten

	{% tfgalleryend %}

Features
--------

* Riesiges 90x50cm 200 Pixel RGB Display mit Aktualisierungsraten bis zu 100Hz
* Entwickle Party Spiele, Messeauftritte und kundenspezifische Anzeigen
  jeglicher Art
* Frei programmierbar, konfigurierbar und erweiterbar
* Pixel: 12mm Durchmesser, wasserdicht (IP65), vollfarb RGB mit 1600mcd pro
  Pixel


Beschreibung
------------

Das *Starterkit: Blinkenlights* ist ein großes, frei programmierbares Display.
Es besteht aus 200 individuell steuerbaren vollfarb RGB LED Pixel, deren Farbe
bis zu 100 mal pro Sekunde geändert werden kann. Es gibt vielfältige 
Anwendungen, dazu zählen eigene (Party-) Spiele,
Messeauftritte, schicke Moodlights oder individuelle Anzeigen aller Art.

Das Basiskit besteht aus einem :ref:`Master Brick <master_brick>`, einem 
:ref:`LED Strip Bricklet <led_strip_bricklet>`, vier 50 LED Pixel Sets, einer 
LED Stromversorgung, vier Wandbefestigungsplatten, einer gelochten Rückplatte,
einer Frontplatte sowie alle notwendigen Kabel und Befestigungsmaterialien.
Das Basiskit kann per USB von jedem (Embedded-) PC (z.B.
:ref:`Raspberry Pi <embedded_raspberry_pi>`), Laptop, Server oder Tablet
gesteuert werden.

Über andere Tinkerforge Produkte kann das Kit erweitert werden.
Bei Spiele-Anwendungen kann das 
:ref:`Giant Game Pad <multi_touch_bricklet_giant_game_pad>` zur
Steuerung verwendet werden. Des weiteren kann das 
:ref:`Piezo Speaker Bricklet <piezo_speaker_bricklet>` zur musikalischen
Untermalung sowie das :ref:`Segment Display 4x7 <segment_display_4x7_bricklet>`
zur Punktedarstellung verwendet werden. Pong lässt sich mit zwei
:ref:`Dual Button Bricklets <dual_button_bricklet>` spielen.
Mit der :ref:`Ethernet Extension <ethernet_extension>` kann die
USB Schnittstelle durch Ethernet ausgetauscht werden, so dass Smartphone 
oder Tablet gesteuerte Anwendungen möglich sind. Ein größeres Display kann durch
das Hinzufügen weiterer Pixel realisiert werden.

Eine :ref:`Demo-Anwendung <starter_kit_blinkenlights_demo_examples>` 
implementiert Klone von `Tetris <https://de.wikipedia.org/wiki/Tetris>`__ und
`Pong <https://de.wikipedia.org/wiki/Pong>`__ und beinhaltet verschiedene
andere Anwendungen. Zum Beispiel können individuelle scrollende Texte in 
diversen Farben, Regenbogen oder individuelle Bildsätze mit konfigurierbarer
Dauer angezeigt werden. Ein virtuelles Feuer erwärmt das Herz auch in den 
kältesten Wintermonaten. Die Spiele können über eine PC Tastatur gesteuert 
werden aber auch per Multi Touch (Giant Game Pad) oder Dual Button Bricklet.

Der Name des Kits "Blinkenlights" wird im
`Hackerjargon <https://de.wikipedia.org/wiki/Blinkenlights_%28Jargon%29>`__
benutzt um blinkende Lampen von Netzwerk-Equipment zu beschreiben. Er ist auch
über das
`Blinkenlights Projekt <https://de.wikipedia.org/wiki/Projekt_Blinkenlights>`__
bekannt.

Das nachfolgende Video zeigt die Beispiele und den Zusammenbau im Zeitraffer:

.. raw:: html

 <center><iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/mmNRa-lLaXM" frameborder="0" allowfullscreen></iframe></center>


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
Abmessungen (B x T x H)                    | 40 x 80 x 7cm (ohne Frontplatte)
                                           | 50 x 90 x > 7cm* (mit Frontplatte)
Gewicht                                    4kg (zusammengebautes Kit)
=========================================  ============================================================

\* hängt von dem eingestellten Abstand zwischen Front- und Rückplatte ab

.. _starter_kit_blinkenlights_resources:

Ressourcen
----------

* Beispiel Quelltext für :ref:`Tetris <starter_kit_blinkenlights_tetris>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__, `C# <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__)
* Beispiel Quelltext für :ref:`Pong <starter_kit_blinkenlights_Pong>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__, `C# <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__)
* Beispiel Quelltext für :ref:`Fire <starter_kit_blinkenlights_fire>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/python>`__, `Delphi <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/delphi>`__)
* Beispiel Quelltext für :ref:`Scrolling Text <starter_kit_blinkenlights_scrolling_text>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/text/python>`__, `PHP <https://github.com/Tinkerforge/blinkenlights/tree/master/text/php>`__)
* Beispiel Quelltext für :ref:`Display Images <starter_kit_blinkenlights_images>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/images/python>`__, `Java <https://github.com/Tinkerforge/blinkenlights/tree/master/images/java>`__)
* :ref:`Demo-Anwendung <starter_kit_blinkenlights_demo_examples>` (Download: `Windows <http://download.tinkerforge.com/kits/blinkenlights/windows/starter_kit_blinkenlights_demo_windows_latest.exe>`__, `Linux <http://download.tinkerforge.com/kits/blinkenlights/linux/starter-kit-blinkenlights-demo-linux_latest.deb>`__, `Mac OS X <http://download.tinkerforge.com/kits/blinkenlights/macos/starter_kit_blinkenlights_demo_macos_latest.dmg>`__, `Quelltext <https://github.com/Tinkerforge/blinkenlights/tree/master/demo>`__)


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe das LED Strip Bricklet an den Master Brick an und verbinde es per USB 
mit dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_brick_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_bricklet_plugin>`):

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

   Details <Construction>


.. _starter_kit_blinkenlights_demo_examples:

Beispielanwendung und Beispielprojekte
--------------------------------------

.. image:: /Images/Kits/blinkenlights_demo_setup_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demoanwendung: Setup
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_setup.jpg

Die Demoanwendung demonstriert verschiedene Anwendungen des Kits. Es besteht
aus 6 Teilanwendungen die als individuelle Projekte zur Verfügung stehen (siehe 
unten). Jedes Projekt wird durch ein eigenes Tab dargestellt. Zwei Dual Button 
Bricklets und ein Multi Touch Bricklet können zusätzlich zur Steuerung der
Spiele genutzt werden. Ist ein Piezo Speaker Bricklet oder ein Segment Display
4x7 Bricklet angeschlossen, so werden diese von den Spielen genutzt um ein 
akustisches Feedback zu geben und den Spielstand anzuzeigen.

Vor Beginn müssen Host und Port konfiguriert werden. Falls das normale Kit 
benutzt wird und dieses direkt per USB an einem PC angeschlossen ist, sind
"localhost" und "4223" die korrekten Einstellungen. Falls das Kit mit
:ref:`Extensions <primer_master_extensions>` erweitert wurde oder
es von einem anderen PC gesteuert werden soll muss die IP Adresse oder der 
Hostname des Rechners oder der Extension eingestellt werden zu dem das Kit 
verbunden wurde. Die Tabelle unter der Host/Port Konfiguration gibt einen
überblick über die angeschlossenen Bricks und Bricklets.


.. _starter_kit_blinkenlights_tetris:

Tetris
^^^^^^

Die Demoanwendung implementiert ein typisches 
`Tetris <https://de.wikipedia.org/wiki/Tetris>`__ mit allen Besonderheiten.
Es kann mit:

.. image:: /Images/Kits/kit_blinkenlights_tetris_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris
   :align: center

oder ohne Frontplatte:

.. image:: /Images/Kits/kit_blinkenlights_tetris_wo_frontpanel_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris
   :align: center

gespielt werden.

Dieser Tetris-Klon kann über drei verschiedene Arten gesteuert werden. Als
erstes können die Buttons im Tab genutzt werden um das Spiel zu steuern.
Alternativ funktioniert dies auch über die PC Tastatur. 
Als letzte Möglichkeit kann ein Mutli Touch Bricklet mit
einem Giant Game Pad oder selbstgebauten Elektroden angeschlossen
werden.

.. image:: /Images/Kits/blinkenlights_demo_tetris_350.jpg
   :scale: 100 %
   :alt: Screenshot Blinkenlights Demo Anwendung: Tetris
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_tetris.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__
heruntergeladen werden. Dieses beinhaltet auch das 
:ref:`Pong <starter_kit_blinkenlights_pong>` Projekt und beseht hauptsächlich
aus zwei Dateien: ``tetris.py`` implementiert das Spiel und ``config.py`` 
definiert Konfigurationen (Host, Port, UIDs, LED Matrixlayout und Keymap).

Die ``config.py`` muss entsprechend angepasst werden und die Anwendung mittels:

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
`Pong <https://de.wikipedia.org/wiki/Pong>`__ mit oder ohne Frontplatte genutzt
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
werden. Zusätzlich ist eine Steuerung über zwei Dual Button Bricklets möglich.

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


Die ``config.py`` muss entsprechend angepasst werden und die Anwendung mittels:

.. code-block:: python

   python pong.py

gestartet werden. Zusätzlich ist dieses Projekt in 
:ref:`C# <api_bindings_csharp>` implementiert worden und kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__
herunter geladen werden.


.. _starter_kit_blinkenlights_fire:

Feuersimulation
^^^^^^^^^^^^^^^

Wenn der Fire Tab gewählt wird erscheint eine Feuersimulation. Diese sieht
besonders gut aus, wenn das Frontplatte in einem Abstand von 
42mm (2x9mm und 2x12mm Abstandsbolzen) zur Rückplatte angebracht wird.

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

Die Simulation basiert auf einem Partikelsystem und kann über vier
Schieberegler beeinflusst werden:

* **Frame Rate**:
  Definiert die Bildrate in Hz. Die Simulation wird jedes neue Bild (Frame)
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

Scrollender Text
^^^^^^^^^^^^^^^^

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

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/text/python>`__
heruntergeladen werden.
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

Die "Images" Demo kann genutzt werden um spezifische Bilder und ganze 
Animationen anzuzeigen.

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
"Choose Images...". Die Demo zeigt das erste Bild an und wechselt in der
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
<https://github.com/Tinkerforge/blinkenlights/tree/master/images/java>`__
heruntergeladen werden.


.. _starter_kit_blinkenlights_scrolling_rainbow:

Bewegender Regenbogen
^^^^^^^^^^^^^^^^^^^^^

Die "Rainbow" Demo zeigt einen mit der eingestellten Framerate und 
Geschwindigkeit sich bewegenden Regenbogen auf dem Display an.
Die Ergebnisse hängen von dem Abstand des Frontplatte zur Rückplatte ab.
Das folgende Bild zeigt das Demo mit 12mm Abstand in Tageslicht, 42mm Abstand in
Tageslicht und 42mm Abstand in Dunkelheit an.

.. image:: /Images/Kits/kit_blinkenlights_rainbow_near_far_dark_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Rainbow Demo
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_rainbow_near_far_dark_1200.jpg

Eine höhere Framerate und Geschwindigkeit führen zu einem sich schneller 
bewegenden Regenbogen.

.. image:: /Images/Kits/blinkenlights_demo_rainbow_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Rainbow
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_rainbow.jpg

Das einzelne :ref:`Python <api_bindings_python>` Projekt kann von 
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/rainbow/python>`__
heruntergeladen werden. Dieses besteht hauptsächlich aus zwei Dateien:
``rainbow.py`` implementiert die Logik, wohingegen ``config.py`` die 
Konfiguration speichert.

Nach Anpassen der ``config.py`` kann die Demo wie folgt gestartet werden:

.. code-block:: python

   python rainbow.py

In :ref:`C <api_bindings_c>` ist diese Demo ebenfalls Implementiert worden. Sie 
kann von `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/rainbow/c>`__ 
heruntergeladen werden.


Zusätzliche Erweiterungen
-------------------------

Mods, Erweiterungen und Verbesserungen des Blinkenlight Kits veröffentlicht in
unserem `Wiki <http://www.tinkerunity.org/wiki/>`__,
in einem Blog oder ähnlich würden hier gerne vorstellen. Bitte kontaktiert uns und 
wir verlinken es hier!
