
:shoplink: ../../../shop/bricklets/nfc-bricklet.html

.. include:: NFC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_bricklet:

NFC Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_nfc_tilted_[?|?].jpg           NFC Bricklet
	Bricklets/bricklet_nfc_front_[?|?].jpg            NFC Bricklet
	Bricklets/bricklet_nfc_top_[?|?].jpg              NFC Bricklet
	Bricklets/bricklet_nfc_w_keyfob_[?|?].jpg         NFC Bricklet mit NFC-Tag
	Cases/bricklet_nfc_case_built_up_[?|?].jpg        NFC Bricklet im Gehäuse
	Bricklets/bricklet_nfc_brickv_[100|].jpg          NFC Bricklet im Brick Viewer
	Dimensions/nfc_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Liest und schreibt NFC Forum Type 1, 2, 3, 4 und Mifare Classic Tags.
* NDEF Datensätze können direkt mit API gelesen und geschrieben werden.
* Unterstützt NFC P2P Betriebsmodi
* Unterstützt Kartenemulations Betriebsmodi
* Reichweite ist auf 10cm begrenzt (3.94")


.. _nfc_bricklet_description:

Beschreibung
------------

Das `NFC <https://en.wikipedia.org/wiki/Near_field_communication>`__ :ref:`Bricklet <primer_bricklets>`
erweitert die Funktionalität der :ref:`Bricks <primer_bricks>` indem es die Möglichkeit
bietet NFC tags zu lesen und zu schreiben. Dafür muss lediglich ein NFC tag
in der Nähe (bis zu 10cm) des Bricklets platziert werden.

Unterstützt werden NFC Forum Type 1, 2, 3, 4 (ISO 14443), NFC Forum Type 5 (ISO 15693) und Mifare Classic Tags. Ein direkter
Page-Zugriff ist verfügbar und es ist möglich NDEF Mitteilungen direkt über das
API zu lesen oder zu schreiben.

Das Bricklet unterstützt außerdem Kartenemulation sowie auch NFC P2P Kommunikation.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
NFC IC                            PN7150
Stromverbrauch (idle)             24mW (~5mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Unterstützte Tags                 Mifare Classic, NFC Forum Type 1, 2, 3, 4, 5
Unterstützte Modi                 Lesen/Schreiben Tag, P2P, Kartenemulation
Arbeitsfrequenz                   13.56 MHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           80 x 50 x 7mm (3,15 x 1,97 x 0,28")
Gewicht                           18g
================================  ============================================================


Ressourcen
----------

* PN7150 Datenblatt (`Download <https://github.com/Tinkerforge/nfc-bricklet/raw/master/datasheets/PN7150.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/nfc-bricklet/raw/master/hardware/nfc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/nfc_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/nfc-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2BKd1ED>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/nfc/nfc.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/nfc/nfc.FCStd>`__)


Kompatibilität
--------------

Das Bricklet sollte mit jedem Tag funktionieren das zu Mifare Classic, NFC
Forum Typ 1, 2, 3, 4 oder 5 kompatibel ist. Die folgenden Tags wurden von uns getestet:

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

**NFC Forum Typ 3:**

* Sony FeliCa Lite-5 RC-S966

**NFC Forum Typ 4:**

* Mifare DESFire
* MIfare DESFire EV1

**NFC Forum Typ 5:**

* NXP ICODE SLIX


Page Größen und andere Dinge die man wissen sollte
--------------------------------------------------

Mifare Classic und NFC Forum Typ x Tags haben verschiedene Page-Größen und
verschiedene Speicher-Strukturen. Wenn die Low Level Page Schreibfunktion
verwendet wird muss diese Struktur beachtet werden, um nicht versehentlich den Tag zu locken.

**Mifare Classic:**

* Page Größe 16 Byte.
* 4 Pages bilden einen Sektor.
* Sektor 0 (Seiten 0-3) sollte nicht überschrieben werden.
* Die letzte Seite jedes Sektors steuert den Zugriff (Seite 7, 11, 15, ..). Diese Seite sollte nur überschrieben werden, wenn man weiß was man tut.

`Adafruit <https://www.adafruit.com>`__ hat eine gute Beschreibung der Struktur:
`Link <https://learn.adafruit.com/adafruit-pn532-rfid-nfc/mifare>`__

**NFC Forum Typ 1:**

* Page Größe 8 Byte
* Pages 0-2 sind für die Zugriffskontrolle reserviert. Diese Pages sollten 
  nicht überschrieben werden, wenn man nicht weiß was man tut.
* Page 15 ist reserviert und kann nicht geschrieben werden.

**NFC Forum Typ 2:**

* Page Größe 4 Byte
* Page 0-1 ist nur lesbar und enthält die Tag ID.
* Page 3-4 und die letzten zwei Pages (Die Page-Nummern hängen von der 
  Größe des Tags ab) enthalten die Lock-Bits. Diese sollten nur überschrieben
  werden, wenn man weiß was man tut.

**NFC Forum Typ 3:**

* Page 0 enthält Attributinformationen.
* Die anderen Pages sind nur zum lesen. Man kann es betrachten wenn es in den Attributinformationen gewährt wird.

**NFC Forum Typ 4:**

* Hat keine Pages, nutzt stattdessen ein Dateisystem.
* Derzeit unterstützen wir den Zugriff zu dem __ und NDEF Record.
* Page 3 auswählen, um auf das Capability Container zu zugreifen.
* Page 4 auswählen, um auf das NDEF Record zu zugreifen.

Tags Erkennen, Lesen und Schreiben
----------------------------------

Damit ein Tag gelesen oder geschrieben werden kann muss zunächst der Modus auf
*MODE_READER* gewechselt werden.

Um einen Tag zu erkennen und auszuwählen muss *ReaderRequestTagID* mit einem Tagtyp
(Mifare Classic or NFC Forum Type 1/2) aufgerufen werden. Der Zustand (State)
des Bricklets wird sich zu *READER_STATE_REQUEST_TAG_ID* ändern und anschließend zu
*READER_STATE_REQUEST_TAG_ID_READY* wenn ein Tag gefunden wurde. Die ID des Tags kann
anschließend durch Aufruf von *GetTagID* ausgelesen werden. Der Tag mit dieser
Tag ID ist nun ausgewählt und kann gelesen/geschrieben werden. Wenn der Zustand
sich zu *READER_STATE_REQUEST_TAG_ID_ERROR* ändert wurde kein Tag mit dem angegebenen Tag-Typ
gefunden. In diesem Fall kann ein weiterer Aufruf von *ReaderRequestTagID* versucht werden.

Wenn die Tag ID bekannt ist und *ReaderGetTagID* eine andere ID zurück gibt bedeutet
dies, dass ein anderer Tag in der Nähe des Bricklets ist. In diesem Fall kann
*ReaderRequestTagID* erneut aufgerufen werden, das NFC/RFID Bricklet wechselt zwischen
den beiden Tags mit jedem Aufruf von *ReaderRequestTagID*. *ReaderRequestTagID*
selektiert also jeweils ein Tag.

Wenn ein Tag selektiert wurde (der Zustand ist *READER_STATE_REQUEST_TAG_ID_READY*)
kann das Tag Page für Page gelesen oder geschrieben werden:

.. image:: /Images/Misc/NFC_Type12.png
   :scale: 100 %
   :alt: NFC Bricklet read/write procedure for Type 1, 2, 3 and 4
   :align: center
   :target: ../../_images/Misc/NFC_Type12.png

Um eine Page zu lesen muss als erstes *ReaderRequestPage* aufgerufen werden. Der
Zustand ändert sich zu *READER_STATE_REQUEST_PAGE_READY*. Anschließend kann die Page
mittels eines Aufrufs von *GetPage* gelesen werden. Eine Seite kann geschrieben
werden mittels des Aufrufs von *ReaderWritePage*. Der Schreibvorgang ist beendet wenn
der Zustand zu *READER_STATE_WRITE_PAGE_READY* wechselt.

Nachdem ein Tag selektiert wurde kann diese ohne Aufrufe von *ReaderRequestTagID*
gelesen/geschrieben werden solange das Tag nicht aus der Nähe des NFC/RFID
Bricklets entfernt wurde.

Anstelle von *ReaderRequestPage* oder *ReaderWritePage* kann auch *ReaderRequestNDEF*
oder *ReaderWriteNDEF* verwendet werden, um NDEF MASSAGES innerhalb eines angemessenen
Platzes direkt zu schreiben anstatt auf Low-Level Pages.

**Spezialfall für Mifare Classic**

Im Falle von Mifare Classic muss man sich zuerst für den Zugriff auf eine
Page authentifizieren:

.. image:: /Images/Misc/NFC_Mifare_Classic.png
   :scale: 100 %
   :alt: NFC Bricklet authenticate/read/write procedure for Mifare Classic
   :align: center
   :target: ../../_images/Misc/NFC_Mifare_Classic.png

Das bedeutet das jedesmal bevor *ReaderRequestPage* oder *ReaderWritePage*
aufgerufen werden soll, *ReaderAuthenticatingMifareClassicPage* aufgerufen
werden muss. Anschließend muss gewartet werden bis sich der Zustand zu
*READER_STATE_AUTHENTICATING_MIFARE_CLASSIC_PAGE_READY* ändert. Ansonsten ist die
Benutzung von Mifare Classic Tags identisch zu den oben beschriebenen.

Der Standardschlüssel (key number A) eines Mifare Classic Tags ist
[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF].

Kartenemulation
---------------

Um die Kartenemulation zu nutzen muss zunächst auf den Modus *MODE_CARDEMU* gewechselt werden.

Nach dem Start von *CARDEMU_STATE_IDEL* kann das NDEF mit *CardemuWriteNDEF* eingestellt werden.
Danach muss *CardemuStartDiscovery* aufgerufen werden. Sobald nun ein Telefon in die
Nähe des NFC Bricklet gebracht wird wechselt der Zustand auf *CARDEMU_STATE_DISCOVER_READY*.

Mit *CardemuStartTransfer* wird die zuvor festgelegte NDEF Massage auf das Telefon übertragen.

Peer-To-Peer Modus
------------------

.. warning::
   P2P-Support wurde in Firmware-Version 2.1.0 entfernt.

Damit das P2P genutzt werden kann, muss auf den Modus *MODE_P2P* gewechselt werden.

Nach dem Start von *P2P_STATE_IDLE* kann das NDEF mit *P2PWriteNDEF* eingestellt werden.
Danach muss *P2PStartDiscovery* aufgerufen werden. Sobald nun ein Telefon in die
Nähe des NFC Bricklet gebracht wird wechselt der Zustand auf *P2P_STATE_DISCOVER_READY*.

Mit *CardemuStartTransfer* und dem Parameter 1 wird die zuvor festgelegte NDEF
Massage auf das Telefon übertragen. Mit dem Parameter 2 kann eine NDEF Massage auf
Telefon gelesen werden.

Die NDEF Massage kann auch über *P2PReadNDEF* gelesen werden.

NFC NDEF Messages
-----------------

Das NFC Forum hat ein NFC Data Exchange Format (NDEF) spezifiziert um Daten
zwischen Tags und Smartphones auszutauschen. NDEF Messages bestehen aus einem
oder mehreren NDEF Records. Viele der definierten NDEF Records können von jedem
Smartphone interpretiert werden welches NFC-Kommunikation unterstützt.


.. _nfc_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert kann nun nach Tags gescannt werden und Seiten
gelesen/geschrieben werden.

.. image:: /Images/Bricklets/bricklet_nfc_brickv.jpg
   :scale: 100 %
   :alt: NFC Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_brickv.jpg

|test_pi_ref|


.. _nfc_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das NFC Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-nfc-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_nfc_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für NFC Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_case_built_up_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Stecke lange schrauben durch Unterteil,
* stecke Bricklet auf Unterteil und schraube es mit Abstandshaltern fest,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Unterteil und
* schraube Oberteil mit kleinen Schrauben zum Unterteil. 

Im folgenden befindet sich eine Explosionszeichnung des NFC Bricklet-Gehäuse:

.. image:: /Images/Exploded/nfc_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für NFC Bricklet
   :align: center
   :target: ../../_images/Exploded/nfc_exploded.png

|bricklet_case_hint|


.. _nfc_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: NFC_hlpi.table
