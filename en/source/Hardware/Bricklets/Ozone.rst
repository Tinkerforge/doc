
:DISABLED_shoplink: ../../../shop/bricklets/ozone-bricklet.html

.. include:: Ozone.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ozone_bricklet:

Ozone Bricklet
==============

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ozone_tilted_[?|?].jpg           Ozone Bricklet
	Bricklets/bricklet_ozone_horizontal_[?|?].jpg       Ozone Bricklet
	Bricklets/bricklet_ozone_master_[100|600].jpg       Ozone Bricklet with Master Brick
	Cases/bricklet_ozone_case_[100|600].jpg             Ozone Bricklet with case
	Bricklets/bricklet_ozone_brickv_[100|].jpg          Ozone Bricklet in Brick Viewer
	Dimensions/ozone_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures ozone concentration from 0 to 250 ppb (parts per billion)

.. _ozone_bricklet_description:

Description
-----------

The Ozone :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure
`ozone concentration <https://en.wikipedia.org/wiki/Ozone>`__ in the air. The
measured ozone concentration can be read out in
`ppb <https://en.wikipedia.org/wiki/Parts-per_notation>`__.
With configurable events it is possible to react on changing ozone
concentration without polling.

Typical applications are TBD.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            A051020-SP-61
Current Consumption               TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 0ppb - 250ppb
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            TBD x TBD x TBDmm (TBD x TBD x TBD")
Weight                            TBDg
================================  ============================================================


Resources
---------

* A051020-SP-61 datasheet (`Download <https://github.com/Tinkerforge/ozone-bricklet/raw/master/datasheets/A051020-SP-61.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ozone-bricklet/raw/master/hardware/ozone-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ozone_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ozone-bricklet/zipball/master>`__)

.. _ozone_bricklet_test:

Test your Ozone Bricklet
------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_ozone_brickv.jpg
   :scale: 100 %
   :alt: Ozone Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ozone_brickv.jpg

|test_pi_ref|


.. _ozone_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Ozone_hlpi.table
