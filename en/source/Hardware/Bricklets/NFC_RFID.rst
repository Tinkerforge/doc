
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / NFC/RFID Bricklet
:shoplink: ../../../shop/bricklets/nfc-rfid-bricklet.html

.. include:: NFC_RFID.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _nfc_rfid_bricklet:

NFC/RFID Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_nfc_rfid_tilted_350.jpg",
	               "Bricklets/bricklet_nfc_rfid_tilted_600.jpg",
	               "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_horizontal_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_horizontal_600.jpg",
	             "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_vertical_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_vertical_600.jpg",
	             "NFC/RFID Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_setup_100.jpg",
	             "Bricklets/bricklet_nfc_rfid_setup_600.jpg",
	             "NFC/RFID Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_nfc_rfid_case_100.jpg",
	             "Cases/bricklet_nfc_rfid_case_600.jpg",
	             "NFC/RFID Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_nfc_rfid_brickv_100.png",
	             "Bricklets/bricklet_nfc_rfid_brickv.png",
	             "NFC/RFID Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/nfc_rfid_bricklet_dimensions_100.png",
	             "Dimensions/nfc_rfid_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Can read and write Mifare Classic and NFC Forum Type 1 and 2 tags
* Operating frequency is 13.56 MHz

Description
-----------

The NFC/RFID :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend :ref:`Bricks <product_overview_bricks>` by the possibility to read
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
Sensor                            PN532
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Supported tags                    Mifare Classic, NFC Forum Type 1, NFC Forum Type 2
Operating Frequency               13.56 MHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            TODO: 30 x 30 x 18mm (1.18 x 1.18 x 0.67")
Weight                            TODOg
================================  ============================================================


Resources
---------

* INA226 Datasheet (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/datasheets/PN532.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/raw/master/hardware/nfc-rfid-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/nfc_rfid_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/nfc-rfid-bricklet/zipball/master>`__)


Compatability
-------------

The Bricklet should work with every tag that is either compatible to 
Mifare Classic, NFC Forum Type 1 or NFC Forum Type 2. We explicitly
tested the Bricklet with the following tags.

Mifare Classic:

* FM11RF08
* MF1S50

NFC Forum Type 1:

* Jewel
* Topaz 512 (TPZ-505-016)

NFC Forum Type 2:

* NTAG203(F)
* NTAG210
* NTAG213
* NTAG215
* NTAG216
* Mifare Ultralight (MF01CU1)

Every smart phone that is capable of NFC can read NFC Form Type 1 and 2 tags.

Page Sizes and other things to know
-----------------------------------

Mifare Classic and NFC Forum Type 1 as well as NFC Forum Type 2 have different
page sizes and a different memory structure. You have to keep track of this
structure to not accidentially lock a tag.

Mifare Classic:

* Page size 16 byte (1 page is read/written per call of *RequestPage*/*WritePage*).
* Sector 0 (pages 0-3) should not be overwritten.
* The last page in every sector controls the authentication keys for this sector (page 7, 11, 15, ..). Do not overwrite these pages if you don't know what you are doing.

NFC Forum Type 1:

* Page size 8 byte (2 pages are read/written per call of *RequestPage*/*WritePage*).
* pages 0-2 are reserved for lock control. Do not overwrite these pages if you don't know what you are doing.
* page 15 is reserved and can not be written.

NFC Forum Type 2:

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
to two tags if *RequestTagID* is called repeatedly.

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


NFC NDEF messages
-----------------

TODO: Example


.. _nfc_rfid_bricklet_test:

First Test
----------

|test_intro|

|test_connect|.

.. image:: /Images/Bricklets/bricklet_nfc_rfid_setup_600.jpg
   :scale: 100 %
   :alt: NFC/RFID Bricklet with Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_setup_1200.jpg

|test_tab|

If everything went as expected you can now see TBD 

.. image:: /Images/Bricklets/bricklet_nfc_rfid_brickv.png
   :scale: 70 %
   :alt: NFC/RFID Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_nfc_rfid_brickv.png

|test_pi_ref|

.. _nfc_rfid_bricklet_case:

Case
----

A `laser-cut case for the NFC/RFID Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-nfc-rfid-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_nfc_rfid_case_350.jpg
   :scale: 100 %
   :alt: Case for NFC/RFID Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_nfc_rfid_case_1000.jpg

.. include:: NFC_RFID.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

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
