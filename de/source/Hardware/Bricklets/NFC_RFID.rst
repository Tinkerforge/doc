
:shoplink: ../../../shop/bricklets/nfc-rfid-bricklet.html

.. include:: NFC_RFID.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_rfid_bricklet:

NFC/RFID Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_nfc_rfid_tilted_[?|?].jpg           NFC/RFID Bricklet
	Bricklets/bricklet_nfc_rfid_w_master_[100|600].jpg     NFC/RFID Bricklet mit Master Brick
	Bricklets/bricklet_nfc_rfid_horizontal_[?|?].jpg       NFC/RFID Bricklet
	Bricklets/bricklet_nfc_rfid_w_keyfob_[100|600].jpg     NFC/RFID Bricklet mit Schlüsselanhänger
	Cases/bricklet_nfc_rfid_case_tilted_[?|?].jpg          NFC/RFID Bricklet im Gehäuse
	Bricklets/bricklet_nfc_rfid_brickv_[100|].jpg          NFC/RFID Bricklet im Brick Viewer
	Dimensions/nfc_rfid_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Kann Mifare Classic und NFC Forum Typ 1 und 2 RFID/NFC Tags lesen/schreiben
* Reichweite auf 10cm begrenzt (3,94")
* Arbeitsfrequenz 13,56 MHz


.. _nfc_rfid_bricklet_description:

Beschreibung
------------

Mit dem NFC/RFID :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` um die Fähigkeit erweitert werden
`NFC <https://de.wikipedia.org/wiki/Near_Field_Communication>`__/`RFID
<https://de.wikipedia.org/wiki/RFID>`__
Tags zu lesen und zu schreiben. Dazu muss der NFC oder RFID Tag in
der Nähe des Bricklets platziert werden (bis zu 10cm Entfernung).

Aktuell werden Mifare Classic und NFC Forum Typ 1 und 2 unterstützt.

Die Möglichkeit Tags zu emulieren als auch NFC P2P Kommunikation könnte in 
Zukunft über ein Firmware Update hinzugefügt werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            PN532
Stromverbrauch                    115mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Unterstütze Tags                  Mifare Classic, NFC Forum Typ 1, NFC Forum Typ 2
Arbeitsfrequenz                   13,56MHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (B x T x H)             50 x 85 x 5mm (1,97 x 3,35 x 0,2")
Gewicht                           15g
================================  ============================================================


Ressourcen
----------

* PN532 Datenblatt (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/datasheets/PN532.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/hardware/nfc-rfid-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/nfc_rfid_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/zipball/master>`__)


Kompatibilität
--------------

Das Bricklet sollte mit jedem Tag funktionieren des zu Mifare Classic, NFC Forum
Typ 1 und NFC Forum Typ 2 kompatibel ist. Die folgenden Tags wurden von uns 
getestet:

**Mifare Classic:**

* FM11RF08
* MF1S50

**NFC Forum Typ 1:**

* Jewel
* Topaz 512 (TPZ-505-016)

**NFC Forum Typ 2:**

* NTAG203(F)
* NTAG210
* NTAG213
* NTAG215
* NTAG216
* Mifare Ultralight (MF01CU1)

Jedes Smartphone das NFC beherrscht, kann NFC Forum Typ 1 und 2 Tags lesen.

Page Größen und andere Dinge die man wissen sollte
--------------------------------------------------

Mifare Classic und NFC Forum Typ 1 und 2 haben verschiedene Page Größen und 
verschiedene Speicher-Strukturen. Wichtig ist diese Struktur zu beachten und 
nicht versehentlich den Tag zu locken.

**Mifare Classic:**

* Page Größe 16 Byte (1 Page wird pro Aufruf von *RequestPage*/*WritePage* gelesen/geschrieben).
* 4 Pages bilden einen Sektor.
* Sektor 0 (Seiten 0-3) sollte nicht überschrieben werden.
* Die letzte Seite jedes Sektors steuert den Zugriff (Seite 7, 11, 15, ..). Diese Seite sollte nur überschrieben werden, wenn man weiß was man tut.

`Adafruit <https://www.adafruit.com>`__ hat eine recht gute Beschreibung der Speicherstruktur:
`Link <https://learn.adafruit.com/adafruit-pn532-rfid-nfc/mifare>`__

**NFC Forum Typ 1:**

* Page Größe 8 Byte (2 Pages werden mit einem Aufruf von *RequestPage*/*WritePage* gelesen/geschrieben).
* Pages 0-2 sind für die Zugriffskontrolle reserviert. Diese Pages sollten nicht überschrieben werden, wenn man nicht weiß was man tut.
* Page 15 ist reserviert und kann nicht geschrieben werden.

**NFC Forum Typ 2:**

* Page Größe 4 Byte (4 Pages werden mit einem Aufruf von *RequestPage*/*WritePage* gelesen/geschrieben).
* Page 0-1 ist nur lesbar und enthält die Tag ID.
* Page 3-4 und die letzten zwei Pages (Die Page-Nummern hängen von der Größe des Tags ab) enthalten die Lock-Bits. Diese sollten nur überschrieben werden, wenn man weiß was man tut.


Tags Erkennen, Lesen und Schreiben
----------------------------------

Um einen Tag zu erkennen und auszuwählen muss *RequestTagID* mit einem Tagtyp 
(Mifare Classic or NFC Forum Type 1/2) aufgerufen werden. Der Zustand (State)
des Bricklets wird sich zu *STATE_REQUEST_TAG_ID* ändern und anschließend zu 
*STATE_REQUEST_TAG_ID_READY* wenn ein Tag gefunden wurde. Die ID des Tags kann
anschließend durch Aufruf von *GetTagID* ausgelesen werden. Der Tag mit dieser
Tag ID ist nun ausgewählt und kann gelesen/geschrieben werden. Wenn der Zustand
sich zu *STATE_REQUEST_TAG_ID_ERROR* ändert wurde kein Tag mit dem angegebenen
Tag-Typ gefunden. In diesem Fall kann ein weiterer Aufruf von *RequestTagID* 
versucht werden.

Wenn die Tag ID bekannt ist und *GetTagID* eine andere ID zurück gibt bedeutet 
dies, dass ein anderer Tag in der Nähe des Bricklets ist. In diesem Fall kann 
*RequestTagID* erneut aufgerufen werden, das NFC/RFID Bricklet wechselt zwischen
den beiden Tags mit jedem Aufruf von *RequestTagID*. *RequestTagID* selektiert
also jeweils ein Tag.

Wenn ein Tag selektiert wurde (der Zustand ist *STATE_REQUEST_TAG_ID_READY*) 
kann das Tag Page für Page gelesen oder geschrieben werden:

.. image:: /Images/Misc/NFC_Type12.png
   :scale: 100 %
   :alt: NFC/RFID Bricklet read/write procedure for Type 1 and 2
   :align: center
   :target: ../../_images/Misc/NFC_Type12.png

Um eine Page zu lesen muss als erstes *RequestPage* aufgerufen werden. Der 
Zustand ändert sich zu *STATE_REQUEST_PAGE_READY*. Anschließend kann die Page
mittels eines Aufrufs von *GetPage* gelesen werden. Eine Seite kann geschrieben 
werden mittels des Aufrufs von *WritePage*. Der Schreibvorgang ist beendet wenn
der Zustand zu *STATE_WRITE_PAGE_READY* wechselt.

Nachdem ein Tag selektiert wurde kann diese ohne Aufrufe von *RequestTagID*
gelesen/geschrieben werden solange das Tag nicht aus der Nähe des NFC/RFID 
Bricklets entfernt wurde.

**Spezialfall für Mifare Classic**

Im Falle von Mifare Classic muss man sich zuerst für den Zugriff auf eine Page 
authentifizieren:

.. image:: /Images/Misc/NFC_Mifare_Classic.png
   :scale: 100 %
   :alt: NFC/RFID Bricklet authenticate/read/write procedure for Mifare Classic
   :align: center
   :target: ../../_images/Misc/NFC_Mifare_Classic.png

Das bedeutet das jedesmal bevor *RequestPage* oder *WritePage* aufgerufen werden
soll, *AuthenticatingMifareClassicPage* aufgerufen werden muss. Anschließend 
muss gewartet werden bis sich der Zustand zu 
*STATE_AUTHENTICATING_MIFARE_CLASSIC_PAGE_READY* ändert. Ansonsten ist die 
Benutzung von Mifare Classic Tags identisch zu den oben beschriebenen.

Der Standardschlüssel (key number A) eines Mifare Classic Tags ist 
[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF].


NFC NDEF Messages
-----------------

Das NFC Forum hat ein NFC Data Exchange Format (NDEF) spezifiziert um Daten
zwischen Tags und Smartphones auszutauschen. NDEF Messages bestehen aus
einem oder mehreren NDEF Records. Viele der definierten NDEF Records können
von jedem Smartphone interpretiert werden welches NFC-Kommunikation
unterstützt.

Wir haben ein Beispielprogramm implementiert welches *Text*, *URI* und
*Mime Media Type* Records auf NFC Forum Type 1 und 2 Tags schreiben kann.

Das Beispiel ist in Python implementiert, kann aber einfach als 
Startpunkt für eine Implementierung in einer anderen Programmiersprache
verwendet werden.

* `Beispiel auf GitHub <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/software/examples/python/example_write_ndef_message.py>`__.


.. _nfc_rfid_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.


.. image:: /Images/Bricklets/bricklet_nfc_rfid_w_master_600.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_w_master_1200.jpg

|test_tab|

Wenn alles wie erwartet funktioniert können nun Tags gescannt und Pages
gelesen/geschrieben werden.

.. image:: /Images/Bricklets/bricklet_nfc_rfid_brickv.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_brickv.jpg

|test_pi_ref|


.. _nfc_rfid_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das NFC/RFID Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-nfc-rfid-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_nfc_rfid_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_rfid_case_tilted_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Stecke lange schrauben durch Unterteil,
* stecke Bricklet auf Unterteil und schraube es mit Abstandshaltern fest,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Unterteil und
* schraube Oberteil mit kleinen Schrauben zum Unterteil. 

Im folgenden befindet sich eine Explosionszeichnung des NFC/RFID Bricklet-Gehäuse:

.. image:: /Images/Exploded/nfc_rfid_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Exploded/nfc_rfid_exploded.png

|bricklet_case_hint|

.. _nfc_rfid_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: NFC_RFID_hlpi.table
