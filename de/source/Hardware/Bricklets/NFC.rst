
:DISABLED_shoplink: ../../../shop/bricklets/nfc-bricklet.html

.. include:: NFC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_bricklet:

NFC Bricklet
============

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_nfc_tilted_[?|?].jpg           NFC Bricklet
	Bricklets/bricklet_nfc_horizontal_[?|?].jpg       NFC Bricklet
	Bricklets/bricklet_nfc_master_[100|600].jpg       NFC Bricklet mit Master Brick
	Cases/bricklet_nfc_case_[100|600].jpg             NFC Bricklet im Gehäuse
	Bricklets/bricklet_nfc_brickv_[100|].jpg          NFC Bricklet im Brick Viewer
	Dimensions/nfc_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Liest und schreibt NFC Forum Type 1, 2, 3, 4 und Mifare Classic tags.
* Ndef Begriffe können direkt mit API gelesen und geschrieben werden.
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

Unterstützt werden NFC Forum Type 1, 2, 3, 4 und Mifare Classic tags. Ein direkter
Seitenzugriff ist verfügbar und es ist möglich Ndef Mitteilungen direkt über das
API zu lesen oder zu schreiben.

Das Bricklet unterstützt außerdem Kartenemulation sowie auch NFC P2P Kommunikation.

Das NFC Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
NFC IC                            PN7150
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Unterstützte Tags                 Mifare Classic, NFC Forum Type 1, 2, 3 und 4
Unterstützte Modi                 Lesen/Schreiben Tag, P2P, Kartenemulation
Arbeitsfrequenz                   13.56 MHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           TBD x TBD x TBDmm (TBD x TBD x TBD")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* PN7150 Datenblatt (`Download <https://github.com/Tinkerforge/nfc-bricklet/raw/master/datasheets/PN7150.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/nfc-bricklet/raw/master/hardware/nfc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/nfc_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/nfc-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


Kompatibilität
--------------

Das Bricklet sollte mit jedem Tag funktionieren des zu Mifare Classic, NFC
Forum Typ 1, 2, 3 oder 4 kompatibel ist. Die folgenden Tags wurden von uns getestet:

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

Jedes Smartphone das NFC beherrscht, kann NFC Forum Typ 1 und 2 Tags lesen.
Meist unterstützt wird Typ 3 und 4.

Page Größen und andere Dinge die man wissen sollte
--------------------------------------------------

Mifare Classic und NFC Forum Typ x Tags haben verschiedene Page Größen und
verschiedene Speicher-Strukturen. Wenn die Low Level Page Schreibfunktion
verwendet wird muss diese Struktur beachtet werden, um nicht versehentlich den Tag zu locken.

**Mifare Classic:**

* Page Größe 16 Byte.
* 4 Pages bilden einen Sektor.
* Sektor 0 (Seiten 0-3) sollte nicht überschrieben werden.
* Die letzte Seite jedes Sektors steuert den Zugriff (Seite 7, 11, 15, ..). Diese Seite sollte nur überschrieben werden, wenn man weiß was man tut.

`Adafruit <https://www.adafruit.com>`__ has a quite good description of the structure:
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
* Derzeit unterstützen wir den Zugriff zu dem __ und Ndef Record.
* Page 3 auswählen, um auf das Capability Container zu zugreifen.
* Page 4 auswählen, um auf das Ndef REcord zu zugreifen.

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

Anstelle von *ReaderREquestPage* oder *ReaderWritePage* kann auch *ReaderREquestNdef*
oder *ReaderWriteNdef* verwendet werden, um Ndef MASSAGES innerhalb eines angemessenen
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

Nach dem Start von *CARDEMU_STATE_IDEL* kann das Ndef mit *CardemuWriteNdef* eingestellt werden.
Danch muss *CardemuStartDiscovery* aufgefrufen werden. Sobald nun ein Telefon in die
Nähe des NFC Bricklet gebracht wird wechselt der Zustand auf *CARDEMU_STATE_DISCOVER_READY*.

Mit *CardemuStartTransfer* wird die zuvor festgelegte Ndef Massage auf das Telefon übertragen.

Peer-To-Peer Modus
------------------

Damit das P2P genutzt werden kann, muss auf den Modus *MODE_P2P* gewechselt werden.

Nach dem Start von *P2P_STATE_IDLE* kann das Ndef mit *P2PWriteNdef* eingestellt werden.
Danch muss *P2PStartDiscovery* aufgefrufen werden. Sobald nun ein Telefon in die
Nähe des NFC Bricklet gebracht wird wechselt der Zustand auf *P2P_STATE_DISCOVER_READY*.

Mit *CardemuStartTransfer* und dem Parameter 1 wird die zuvor festgelegte Ndef
Massage auf das Telefon übertragen. Mit dem Parameter 2 kann eine Ndef Massage auf
Telefon gelesen werden.

Die Ndef Massage kann auch über *P2PReadNdef* gelesen werden.

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

.. image:: /Images/Bricklets/bricklet_nfc_w_master_600.jpg
   :scale: 100 %
   :alt: NFC Bricklet with tag 
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_w_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert ... TBD.

.. image:: /Images/Bricklets/bricklet_nfc_brickv.jpg
   :scale: 100 %
   :alt: NFC Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_brickv.jpg

|test_pi_ref|


.. _nfc_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das NFC Bricklet
	<https://www.tinkerforge.com/de/shop/cases/case-nfc-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_nfc_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für NFC Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_nfc_case_1000.jpg

	.. include:: NFC.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

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
