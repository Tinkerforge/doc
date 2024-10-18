
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
	Bricklets/bricklet_nfc_w_keyfob_[?|?].jpg         NFC Bricklet with keyfob
	Cases/bricklet_nfc_case_built_up_[?|?].jpg        NFC Bricklet with keyfob
	Bricklets/bricklet_nfc_brickv_[100|].jpg          NFC Bricklet in Brick Viewer
	Dimensions/nfc_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Can read and write NFC Forum Type 1, 2, 3, 4, 5 and Mifare Classic tags.
* NDEF definitions can be directly read/written with API.
* Supports NFC P2P mode
* Supports card emulation mode
* Range is restricted to 10cm (3.94")


.. _nfc_bricklet_description:

Description
-----------

The `NFC <https://en.wikipedia.org/wiki/Near_field_communication>`__ :ref:`Bricklet <primer_bricklets>` 
can be used to extend :ref:`Bricks <primer_bricks>` by the possibility to read
and write NFC tags. To do this you only have to place a NFC
tag in the proximity (up to 10cm) of the Bricklet.

NFC Forum Type 1, 2, 3, 4 (ISO 14443), NFC Forum Type 5 (ISO 15693) and Mifare Classic tags are supported. Direct page
access is available and it is possible to directly read/write NDEF messages
through the API.

The Bricklet also supports Card Emulation as well as NFC P2P communication.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
NFC IC                            PN7150
Current Consumption (idle)        24mW (~5mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Supported tags                    Mifare Classic, NFC Forum Type 1, 2, 3, 4, 5
Supported modes                   Read/Write tag, P2P, Card Emulation
Operating Frequency               13.56 MHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            80 x 50 x 7mm (3.15 x 1.97 x 0.28")
Weight                            18g
================================  ============================================================


Resources
---------

* PN7150 datasheet (`Download <https://github.com/Tinkerforge/nfc-bricklet/raw/master/datasheets/PN7150.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/nfc-bricklet/raw/master/hardware/nfc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/nfc_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/nfc-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BKd1ED>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/nfc/nfc.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/nfc/nfc.FCStd>`__)


Compatibility
-------------

The Bricklet should work with every tag that is either compatible to 
Mifare Classic, NFC Forum Type 1, 2, 3, 4 or 5. We explicitly
tested the Bricklet with the following tags:

**Mifare Classic:**

* FM11RF08
* MF1S50

**NFC Forum Type 1:**

* Jewel
* Topaz 512 (TPZ-505-016)

**NFC Forum Type 2:**

* NTAG203(F)
* NTAG210
* NTAG213
* NTAG215
* NTAG216
* Mifare Ultralight (MF01CU1)

**NFC Forum Type 3:**

* Sony FeliCa Lite-S RC-S966

**NFC Forum Type 4:**

* Mifare DESFire
* Mifare DESFire EV1

**NFC Forum Typ 5:**

* NXP ICODE SLIX

Every smart phone that is capable of NFC can read NFC Forum Type 1 and 2 tags.
Most support Type 3 and 4.

Page Sizes and other things to know
-----------------------------------

Mifare Classic and NFC Forum Type x tags have different
page sizes and a different memory structure. If you use the low level page write
functions you have to keep track of this structure to not accidentally lock a tag.

**Mifare Classic:**

* Page size 16 byte.
* 4 pages build one sector.
* Sector 0 (pages 0-3) should not be overwritten.
* The last page in every sector controls the authentication keys for this sector
  (page 7, 11, 15, ..). Do not overwrite these pages if you don't know what you are doing.

`Adafruit <https://www.adafruit.com>`__ has a quite good description of the structure:
`Link <https://learn.adafruit.com/adafruit-pn532-rfid-nfc/mifare>`__

**NFC Forum Type 1:**

* Page size 8 byte.
* pages 0-2 are reserved for lock control. Do not overwrite these pages if you
  don't know what you are doing.
* page 15 is reserved and can not be written.

**NFC Forum Type 2:**

* Page size 4 byte.
* Page 0-1 are read only and contains the tag ID.
* Page 3-4 and the last two pages (page number depends on the size of the tag)
  contain lock bits. Do not overwrite these pages if you don't know what you are doing.

**NFC Forum Type 3:**

* Page 0 contains attribute information.
* The other pages may be read-only. You can look up if it can be written in the
  attribute information.

**NFC Forum Type 4:**

* Does not have pages, uses a file system instead.
* Currently we support access to the capability container and NDEF record.
* Select page 3 to access the capability container.
* Select page 4 to access the NDEF record.

Identifying, Reading and Writing tags
-------------------------------------

To read or write a tag you first have to change the mode to *MODE_READER*.

To identify and select a tag you have to call *ReaderRequestTagID* with a tag 
type (Mifare Classic or NFC Forum Type 1/2). The state
of the Bricklet will change to *READER_STATE_REQUEST_TAG_ID* and then change to
*READER_STATE_REQUEST_TAG_ID_READY* if a tag was found. You can then get the tag ID
by calling *GetTagID*. Now the tag with this tag ID is selected and it can
be read or written. If the state changes to *READER_STATE_REQUEST_TAG_ID_ERROR*
no tag with the given tag type was found. In this case you can try again
by calling *ReaderRequestTagID* again.

If you know the tag ID of your tag and *ReaderGetTagID* returns another tag ID it
means that another tag is also in the proximity of the reader. In this case
you can call *ReaderRequestTagID* again, the NFC Bricklet will cycle through up
to two tags if *ReaderRequestTagID* is called repeatedly. Therefore *ReaderRequestTagID* 
select Tags.

If a tag is selected (i.e. the state is *READER_STATE_REQUEST_TAG_ID_READY*) you can 
read or write the tag page by page:

.. image:: /Images/Misc/NFC_Type12.png
   :scale: 100 %
   :alt: NFC Bricklet read/write procedure for Type 1, 2, 3 and 4
   :align: center
   :target: ../../_images/Misc/NFC_Type12.png

To read a page you have to first call *ReaderRequestPage*. The state will change
to *READER_STATE_REQUEST_PAGE_READY* after which you can get the page by calling
*GetPage*. Writing can be done by calling *ReaderWritePage*, the writing is finished
after the state changes to *READER_STATE_WRITE_PAGE_READY*.

If a tag is selected you can read and write without calling *ReaderRequestTagID*
again as long as the tag isn't removed from the proximity of the 
NFC Bricklet.

Instead of *ReaderRequestPage* or *ReaderWritePage* you can also use 
*ReaderRequestNDEF* or *ReaderWriteNDEF* to directly write NDEF messages
to an appropriate space instead of low-level pages.

**Special Case for Mifare Classic**

In case of Mifare Classic you have to authenticate a page before you can
read or write it:

.. image:: /Images/Misc/NFC_Mifare_Classic.png
   :scale: 100 %
   :alt: NFC Bricklet authenticate/read/write procedure for Mifare Classic
   :align: center
   :target: ../../_images/Misc/NFC_Mifare_Classic.png

This means that every time before you call *ReaderRequestPage* or *ReaderWritePage*,
you have to call *ReaderAuthenticatingMifareClassicPage* and wait for the state
to change to *READER_STATE_AUTHENTICATING_MIFARE_CLASSIC_PAGE_READY*. Otherwise
Mifare Classic tags can be handled exactly as described above.

The default key (key number A) of a Mifare Classic tag is 
[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF].

Card Emulation
---------------

To use card emulation you first have to change the mode to *MODE_CARDEMU*.

Starting from *CARDEMU_STATE_IDLE* you can set the NDEF with *CardemuWriteNDEF*.
After that call *CardemuStartDiscovery*. If a phone is now brought near to
the NFC Bricklet the state will change to *CARDEMU_STATE_DISCOVER_READY*.

Call *CardemuStartTransfer* to transfer to previously set NDEF message to
the phone.

Peer-To-Peer Mode
-----------------

.. warning::
   P2P support was removed in firmware version 2.1.0

To use P2P you first have to change the mode to *MODE_P2P*.

Starting from *P2P_STATE_IDLE* you can set the NDEF with *P2PWriteNDEF*.
After that call *P2PStartDiscovery*. If a phone is now brought near to
the NFC Bricklet the state will change to *P2P_STATE_DISCOVER_READY*.

Call *P2PStartTransfer* with parameter 1 to transfer to previously set 
NDEF message to the phone or with parameter 2 to read an NDEF message
from the phone.

In the second case you can read the NDEF message with *P2PReadNDEF*.

NFC NDEF Messages
-----------------

The NFC Forum has specified the NFC Data Exchange Format (NDEF) to 
transfer messages from NFC tags to smart phones. NDEF Messages
consist of one or more NDEF Records. Many of the predefined
NDEF Records can be understood by any smart phone that is capable
of NFC communication.

..
  TODO: Add link to examples using NDEF message.


.. _nfc_bricklet_test:

Test your NFC Bricklet
----------------------

|test_intro|

|test_connect|.

|test_tab|

If everything went as expected you can now scan for tags and read/write
pages etc.

.. image:: /Images/Bricklets/bricklet_nfc_brickv.jpg
   :scale: 100 %
   :alt: NFC Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_brickv.jpg

|test_pi_ref|


.. _nfc_bricklet_case:

Case
----

A `laser-cut case for the NFC Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-nfc-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_nfc_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for NFC Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_case_built_up_1000.jpg

The assembly is easiest if you follow the following steps:

* Put long screws through bottom plate,
* put Bricklet on plate and fasten screws with spacers,
* build up side plates,
* plug side plates in bottom plate,
* add top plate onto side plates and
* add screws to top plate.

Below you can see an exploded assembly drawing of the NFC Bricklet case:

.. image:: /Images/Exploded/nfc_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for NFC Bricklet
   :align: center
   :target: ../../_images/Exploded/nfc_exploded.png

|bricklet_case_hint|


.. _nfc_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: NFC_hlpi.table
