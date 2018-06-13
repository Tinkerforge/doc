
.. include:: NFC_RFID.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_rfid_bricklet:

NFC/RFID Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_nfc_rfid_tilted_[?|?].jpg           NFC/RFID Bricklet
	Bricklets/bricklet_nfc_rfid_w_master_[100|600].jpg     NFC/RFID Bricklet with Master Brick
	Bricklets/bricklet_nfc_rfid_horizontal_[?|?].jpg       NFC/RFID Bricklet
	Bricklets/bricklet_nfc_rfid_w_keyfob_[100|600].jpg     NFC/RFID Bricklet with keyfob
	Cases/bricklet_nfc_rfid_case_tilted_[?|?].jpg          NFC/RFID Bricklet with case
	Bricklets/bricklet_nfc_rfid_brickv_[100|].jpg          NFC/RFID Bricklet in Brick Viewer
	Dimensions/nfc_rfid_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The NFC/RFID Bricklet is discontinued and is no longer sold. The
 :ref:`NFC Bricklet <nfc_bricklet>` is the recommended
 replacement.


Features
--------

* Can read and write Mifare Classic and NFC Forum Type 1 and 2 RFID/NFC tags
* Range is restricted to 10cm (3.94")
* Operating frequency is 13.56 MHz


.. _nfc_rfid_bricklet_description:

Description
-----------

The `NFC <https://en.wikipedia.org/wiki/Near_field_communication>`__/
`RFID <https://en.wikipedia.org/wiki/Rfid>`__
:ref:`Bricklet <primer_bricklets>` can be used to 
extend :ref:`Bricks <primer_bricks>` by the possibility to read
and write NFC/RFID tags. To do this you only have to place a NFC or RFID 
tag in the proximity (up to 10cm) of the Bricklet.

Currently we support Mifare Classic as well as NFC Forum Type 1 and 2 tags.

Capability for tag emulation as well as NFC P2P communication may be added
in the future firmware updates.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
NFC IC                            PN532
Current Consumption               115mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Supported tags                    Mifare Classic, NFC Forum Type 1, NFC Forum Type 2
Operating Frequency               13.56 MHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            50 x 85 x 5mm (1.97 x 3.35 x 0.2")
Weight                            15g
================================  ============================================================


Resources
---------

* PN532 datasheet (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/datasheets/PN532.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/hardware/nfc-rfid-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/nfc_rfid_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/zipball/master>`__)


Compatibility
-------------

The Bricklet should work with every tag that is either compatible to 
Mifare Classic, NFC Forum Type 1 or NFC Forum Type 2. We explicitly
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

Every smart phone that is capable of NFC can read NFC Forum Type 1 and 2 tags.

Page Sizes and other things to know
-----------------------------------

Mifare Classic and NFC Forum Type 1 as well as NFC Forum Type 2 have different
page sizes and a different memory structure. You have to keep track of this
structure to not accidentally lock a tag.

**Mifare Classic:**

* Page size 16 byte (1 page is read/written per call of *RequestPage*/*WritePage*).
* 4 pages build one sector.
* Sector 0 (pages 0-3) should not be overwritten.
* The last page in every sector controls the authentication keys for this sector (page 7, 11, 15, ..). Do not overwrite these pages if you don't know what you are doing.

`Adafruit <https://www.adafruit.com>`__ has a quite good description of the structure:
`Link <https://learn.adafruit.com/adafruit-pn532-rfid-nfc/mifare>`__

**NFC Forum Type 1:**

* Page size 8 byte (2 pages are read/written per call of *RequestPage*/*WritePage*).
* pages 0-2 are reserved for lock control. Do not overwrite these pages if you don't know what you are doing.
* page 15 is reserved and can not be written.

**NFC Forum Type 2:**

* Page size 4 byte (4 pages are read/written per call of *RequestPage*/*WritePage*).
* Page 0-1 are read only and contains the tag ID
* Page 3-4 and the last two pages (page number depends on the size of the tag) contain lock bits. Do not overwrite these pages if you don't know what you are doing.

Identifying, Reading and Writing tags
-------------------------------------

To identify and select a tag you have to call *RequestTagID* with a tag 
type (Mifare Classic or NFC Forum Type 1/2). The state
of the Bricklet will change to *STATE_REQUEST_TAG_ID* and then change to
*STATE_REQUEST_TAG_ID_READY* if a tag was found. You can then get the tag ID
by calling *GetTagID*. Now the tag with this tag ID is selected and it can
be read or written. If the state changes to *STATE_REQUEST_TAG_ID_ERROR*
no tag with the given tag type was found. In this case you can try again
by calling *RequestTagID* again.

If you know the tag ID of your tag and *GetTagID* returns another tag ID it
means that another tag is also in the proximity of the reader. In this case
you can call *RequestTagID* again, the NFC/RFID Bricklet will cycle through up
to two tags if *RequestTagID* is called repeatedly. Therefore *RequestTagID* 
select Tags.

If a tag is selected (i.e. the state is *STATE_REQUEST_TAG_ID_READY*) you can 
read or write the tag page by page:

.. image:: /Images/Misc/NFC_Type12.png
   :scale: 100 %
   :alt: NFC/RFID Bricklet read/write procedure for Type 1 and 2
   :align: center
   :target: ../../_images/Misc/NFC_Type12.png

To read a page you have to first call *RequestPage*. The state will change
to *STATE_REQUEST_PAGE_READY* after which you can get the page by calling
*GetPage*. Writing can be done by calling *WritePage*, the writing is finished
after the state changes to *STATE_WRITE_PAGE_READY*.

If a tag is selected you can read and write without calling *RequestTagID*
again as long as the tag isn't removed from the proximity of the 
NFC/RFID Bricklet.

**Special Case for Mifare Classic**

In case of Mifare Classic you have to authenticate a page before you can
read or write it:

.. image:: /Images/Misc/NFC_Mifare_Classic.png
   :scale: 100 %
   :alt: NFC/RFID Bricklet authenticate/read/write procedure for Mifare Classic
   :align: center
   :target: ../../_images/Misc/NFC_Mifare_Classic.png

This means that every time before you call *RequestPage* or *WritePage*,
you have to call *AuthenticatingMifareClassicPage* and wait for the state
to change to *STATE_AUTHENTICATING_MIFARE_CLASSIC_PAGE_READY*. Otherwise
Mifare Classic tags can be handled exactly as described above.

The default key (key number A) of a Mifare Classic tag is 
[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF].


NFC NDEF Messages
-----------------

The NFC Forum has specified the NFC Data Exchange Format (NDEF) to 
transfer messages from NFC tags to smart phones. NDEF Messages
consist of one or more NDEF Records. Many of the predefined
NDEF Records can be understood by any smart phone that is capable
of NFC communication.

We implemented an example program that can write *Text*, *URI* and 
*Mime Media Type* Records to NFC Forum Type 1 and 2 tags.

The example is implemented in Python, but it can easily be used as a
starting point if you want to write NDEF Messages with any programming
language.

* `Example on github <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/software/examples/python/example_write_ndef_message.py>`__.


.. _nfc_rfid_bricklet_test:

First Test
----------

|test_intro|

|test_connect|.

.. image:: /Images/Bricklets/bricklet_nfc_rfid_w_master_600.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet with tag 
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_w_master_1200.jpg

|test_tab|

If everything went as expected you can now scan for tags and read/write
pages.

.. image:: /Images/Bricklets/bricklet_nfc_rfid_brickv.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_brickv.jpg

|test_pi_ref|


.. _nfc_rfid_bricklet_case:

Case
----

A laser-cut case for the NFC/RFID Bricklet was available, but is not sold
any longer.

.. image:: /Images/Cases/bricklet_nfc_rfid_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_rfid_case_tilted_1000.jpg

The assembly is easiest if you follow the following steps:

* Put long screws through bottom plate,
* put Bricklet on plate and fasten screws with spacers,
* build up side plates,
* plug side plates in bottom plate,
* add top plate onto side plates and
* add screws to top plate.

Below you can see an exploded assembly drawing of the NFC/RFID Bricklet case:

.. image:: /Images/Exploded/nfc_rfid_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Exploded/nfc_rfid_exploded.png

|bricklet_case_hint|


.. _nfc_rfid_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: NFC_RFID_hlpi.table
