
:shoplink: ../../../shop/bricklets/e-paper-296x128-bricklet-bwr.html

.. include:: EPaper_296x128.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _e_paper_296x128_bricklet:

E-Paper 296x128 Bricklet
========================


.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_e_paper_296x128_tilted_red_[?|?].jpg       E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_tilted_gray_[?|?].jpg      E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_top_red_[?|?].jpg          E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_top_gray_[?|?].jpg         E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_tilted_bottom_[?|?].jpg    E-Paper 296x128 Bricklet
	Cases/bricklet_e_paper_296x128_case_front_[?|?].jpg           E-Paper 296x128 Bricklet im Gehäuse
	Bricklets/bricklet_e_paper_296x128_brickv_[100|].jpg          E-Paper 296x128 Bricklet im Brick Viewer
	Dimensions/e_paper_296x128_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 7,4cm (2,9") E-Paper Display mit einer Auflösung von 296x128 Pixel
* Zwei Dreifarb-Displays verfügbar: Schwarz/Weiß/Rot und Schwarz/Weiß/Grau
* Eingebetteter Font für einfache Textdarstellung


.. _e_paper_296x128_bricklet_description:

Beschreibung
------------

Das E-Paper 296x128 :ref:`Bricklet <primer_bricklets>` ist ein E-Paper Display mit
einer Auflösung von 296x128 Pixel.

Jedes Pixel kann individuell gesetzt werden, das Display kann also Grafiken anzeigen.
Der Inhalt des Displays bleibt bestehen wenn das Bricklet vom Strom getrennt wird.

Das E-Paper 296x128 Bricklet ist verfügbar mit zwei unterschiedlichen 
Dreifarb-Display-Optionen: Schwarz/Weiß/Rot und Schwarz/Weiß/Grau.

Eine Dreifarb-Aktualisierung des Bildschirminhalts dauert ungefähr 7,5 Sekunden. Mit
unterschiedlichen Aktualisierungs-Modi ist es möglich Aktualisierungsraten von bis zu
1Hz zu erreichen wenn nur Schwarz und Weiß genutzt wird.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/bricklet_e_paper_296x128_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_e_paper_296x128_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_e_paper_296x128_video.webm" type="video/webm">
	</video>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    | 45mW (9mA bei 5V) inaktiv
                                  | 95mW (19mA bei 5V) während dem Setzen eines Bildes
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Display-Auflösung                 296x128 Pixel
Display-Größe                     7,4cm (2,9")
Display-Farben                    Schwarz/Weiß/Rot oder Schwarz/Weiß/Grau
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           100 x 40 x 6mm (3,93 x 1,57 x 0,24")
Gewicht                           20g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/raw/master/hardware/e-paper-296x128-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/e_paper_296x128_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2VyGhgF>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/e_paper_296x128/e-paper-296x128.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/e_paper_296x128/e-paper-296x128.FCStd>`__)


.. _e_paper_296x128_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte das Tab im Brick Viewer wie folgt aussehen.

Es ist möglich per Maus auf dem Display zu zeichnen und Text zu schreiben.

Hinweis: Beim Starten des Bricklet kann der Inhalt des Displays nicht ausgelesen werden.
Daher zeigt der Brick Viewer nach dem starten erst schwarzes Display, auch wenn etwas
auf dem Display dargestellt wird. Nach dem ersten Schreiben auf dem Display kann der
Brick Viewer den Display-Inhalt auslesen bis das Bricklet wieder neugestartet wird.

.. image:: /Images/Bricklets/bricklet_e_paper_296x128_brickv.jpg
   :scale: 100 %
   :alt: E-Paper 296x128 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_e_paper_296x128_brickv.jpg

|test_pi_ref|


Benutzung
---------

Um auf das Display zu zeichnen empfehlen wir eine Image Library
zu nutzen die für eine spezifische Programmiersprache entwickelt wurde
(zum Beispiel PIL für Python). Dadurch können die Zeichen-Primitiven und 
Schriftarten der Library verwendet werden und das fertig gezeichnete
Bild kann dann zum Bricklet übertragen werden.

Wir haben Beispiele für:

* `C/C++ <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/c/example_load_image.c>`__
  (mit `libgd <https://libgd.github.io/>`__),
* `C# <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/csharp/ExampleLoadImage.cs>`__,
* `Go <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/go/example_load_image.go>`__,
* `Java <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/java/ExampleLoadImage.java>`__,
* `Perl <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/perl/example_load_image.pl>`__
  (mit `GD <http://search.cpan.org/~lds/GD-2.56/lib/GD.pm>`__),
* `PHP <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/php/ExampleLoadImage.php>`__
  (mit `GD <https://php.net/manual/en/book.image.php>`__),
* `Python <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/python/example_load_image.py>`__
  (mit `PIL <http://python-pillow.org/>`__),
* `Rust <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/rust/example_load_image.rs>`__,
  (mit `image <https://docs.rs/image/0.21.1/image/>`__)
* `Visual Basic .NET <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/vbnet/ExampleLoadImage.vb>`__.

In dem Beispiel laden wir das Bild `tf_red.png <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/tf_red.png>`__
und schreiben es auf das Display:

TODO: tf_red image


Update-Modus
------------

.. note::
 Der *Default* Update-Modus basiert auf den Standardeinstellungen des E-Paper-Display
 Herstellers. Alle anderen Modi sind experimentell und es tritt mehr Ghosting sowie
 mögliche Langzeiteffekte auf.

 Für einen Überblick über die Funktionsweise eines E-Paper-Displays können wir
 das exzellente Video von Ben Krasnow empfehlen:
 `https://www.youtube.com/watch?v=MsbiO8EAsGw <https://www.youtube.com/watch?v=MsbiO8EAsGw>`__.

 Falls es nicht klar ist was diese Optionen bedeuten, empfehlen wir den
 Update-Modus auf *Default* zu belassen.

Aktuell gibt es drei unterschiedliche Update-Modi:

* **Default**: Einstellungen wie vom Hersteller vorgegeben. Eine Bildschirmaktualisierung dauert
  ungefähr 7,5 Sekunden und während der Aktualisierung flackert der Bildschirm mehrfach.
* **Black/White**: In diesem Modus werden nur die schwarzen und weißen Pixel aktualisiert. Es
  werden die Herstellereinstellungen für schwarz/weiß genutzt, allerdings wird der
  rote oder graue Buffer ignoriert. Mit diesem Modus flackert das Display bei einer Aktualisierung
  einmal und es dauert in etwa 2,5 Sekunden. Verglichen zu der Standardeinstellung entsteht
  mehr Ghosting.
* **Delta**: In diesem Modus werden auch nur die schwarzen und weißen Pixel aktualisiert. Es wird
  eine aggressive Aktualisierungsmethode genutzt. Änderungen werden nicht auf dem kompletten
  Buffer angewendet, sondern nur auf dem Unterschied (Delta) zwischen dem letzten und dem nächsten
  Buffer. Mit diesem Modus flackert das Display nicht und eine Aktualisierung dauert 900-950ms.
  Verglichen zu den anderen beiden Modi gibt es mehr Ghosting. Dieser Modus ist gut geeignet um z.B.
  flackerfrei einen regelmäßig aktualisierten Text darzustellen.

Wenn der Black/White- oder Delta-Modus zusammen mit dem schwarz/weiß/rot-Bildschirm verwendet wird,
bekommt die weiße Farbe nach mehrmaligem Wechsel zwischen schwarz und weiß einen rötlichen Stich.

Wenn der Delta-Modus mit schnellen Aktualisierungen verwendet wird, empfehlen wir in regelmäßigen
Abständen zurück zum Default-Modus zu wechseln um dort vollflächig zwischen den drei Farben hin
und her zu wechseln. Dadurch wird das Ghosting welches durch die Verwendung des Delta-Modus
entsteht wieder entfernt. Danach kann dann wieder in den Delta-Modus gewechselt werden für
flackerfreie Aktualisierungen.


.. _e_paper_296x128_bricklet_font:

Zeichensatz
-----------

Das Bricklet beinhaltet folgenden Zeichensatz (Codepage 437, ASCII ist grün markiert), mit
dem schnell und einfach Text auf dem Display angezeigt werden kann:

.. image:: /Images/Bricklets/bricklet_e_paper_296x128_font.png
   :scale: 100 %
   :alt: E-Paper 296x128 Bricklet Zeichensatz
   :align: center
   :target: ../../_images/Bricklets/bricklet_e_paper_296x128_font.png


.. _e_paper_296x128_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das E-Paper 296x128 Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-e-paper-296x128-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_e_paper_296x128_case_front_350.jpg
   :scale: 100 %
   :alt: Gehäuse für E-Paper 296x128 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_e_paper_296x128_case_front_1000.jpg

.. include:: EPaper_296x128.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/e_paper_296x128_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für E-Paper 296x128 Bricklet
   :align: center
   :target: ../../_images/Exploded/e_paper_296x128_exploded.png

|bricklet_case_hint|


.. _e_paper_296x128_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: EPaper_296x128_hlpi.table
