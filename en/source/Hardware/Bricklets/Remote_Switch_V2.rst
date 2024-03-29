
:shoplink: ../../../shop/bricklets/remote-switch-v2-bricklet.html

.. include:: Remote_Switch_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _remote_switch_v2_bricklet:

Remote Switch Bricklet 2.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_remote_switch_v2_tilted_[?|?].jpg             Remote Switch Bricklet 2.0
	Bricklets/bricklet_remote_switch_v2_side_[?|?].jpg               Remote Switch Bricklet 2.0
	Bricklets/bricklet_remote_switch_v2_top_[?|?].jpg                Remote Switch Bricklet 2.0
	Bricklets/bricklet_remote_switch_v2_brickv_[100|].jpg            Remote Switch Bricklet 2.0 in Brick Viewer
	Dimensions/remote_switch_v2_bricklet_dimensions_[100|600].png    Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Wireless house automation
* Controls remote mains switches (:ref:`supported devices <remote_switch_v2_supported_devices>`)
* Can control remote mains switches with dimming function
* Can read out the remotes of remote mains switches


.. _remote_switch_v2_bricklet_description:

Description
-----------

The Remote Switch :ref:`Bricklet <primer_bricklets>` is equipped with
a 433MHz radio module (433MHz SMA antenna is included). It can be used to
extend :ref:`Bricks <primer_bricks>` by the possibility to
control remote mains switches that are based on the PT2262 and HX2262 ICs.

House code as well as receiver code can be configured with the API.

The Bricklet can also be used as a receiver for the remotes.

Technical Specifications
------------------------

================================  ========================================================================================
Property                          Value
================================  ========================================================================================
Radio Module                      RFM69HW
Current Consumption               113mW (idle), 231mW (sending)
--------------------------------  ----------------------------------------------------------------------------------------
--------------------------------  ----------------------------------------------------------------------------------------
Radio Frequency                   433MHz
Supported Remote Mains Switches   All based on PT2262 and HX2262, (:ref:`complete list <remote_switch_v2_supported_devices>`)
--------------------------------  ----------------------------------------------------------------------------------------
--------------------------------  ----------------------------------------------------------------------------------------
Dimensions (W x D x H)            25 x 40 x 5mm (0.98 x 1.58 x 0.2")*
Weight                            8g*
================================  ========================================================================================

\* without antenna

Resources
---------

* RFM69HW datasheet (`Download <https://github.com/Tinkerforge/remote-switch-v2-bricklet/raw/master/datasheets/RFM69HW.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/remote-switch-v2-bricklet/raw/master/hardware/remote-switch-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/remote_switch_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/remote-switch-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BK1DJ4>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/remote_switch_v2/remote-switch-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/remote_switch_v2/remote-switch-v2.FCStd>`__)


.. _remote_switch_v2_bricklet_test:

Test your Remote Switch Bricklet 2.0
------------------------------------

|test_intro|

|test_connect|.

|test_tab|
After that configure the house and receiver code.
If everything went as expected you can now control remote mains switches.

.. image:: /Images/Bricklets/bricklet_remote_switch_v2_brickv.jpg
   :scale: 100 %
   :alt: Remote Switch Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_switch_v2_brickv.jpg

|test_pi_ref|


.. _remote_switch_v2_supported_devices:

List of Supported Devices
-------------------------

The following devices are known to be controllable with the
Remote Switch Bricklet 2.0. If you found another remote mains switch
that is compatible please write us an email, we would like to add it.

The Remote Switch Bricklet 2.0 currently supports three different
:ref:`addressing types <remote_switch_v2_bricklet_addressing_types>`: A, B and C.

.. |nbsp| unicode:: 0xA0
   :trim:

=================== ==================================== ================================== =======
Manufacturer        Models                               Function                           Type
=================== ==================================== ================================== =======
BAT                 RC 3500-A                            Switch                             A
|nbsp|              RC AAA1000-A                         Switch                             A
|nbsp|              RC AAA3680-A                         Switch                             A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Brennenstuhl        RCS 1000 N Comfort                   Switch Set                         A
|nbsp|              RCS 1044 N Comfort                   Outdoor Switch Set                 A
|nbsp|              RCS 2044 N Comfort Indoor            Switch Set                         A
|nbsp|              RCS 2044 N Comfort Outdoor           Outdoor Switch Set                 A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
DÜWI                FS1                                  Switch Set                         C
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
ELRO                AB440D                               Dimmer                             A
|nbsp|              AB440ID                              Dimmer (flush-mounted)             A
|nbsp|              AB440IS                              Switch (flush-mounted)             A
|nbsp|              AB440L                               Bulb Holder Dimmer                 A
|nbsp|              AB440R                               Remote                             A
|nbsp|              AB440S                               Switch                             A
|nbsp|              AB440W                               Outdoor Switch                     A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
ELRO Home Easy      HE801S                               Switch Set                         B
|nbsp|              HE801SA                              Switch Set                         C
|nbsp|              HE801SF                              Switch Set                         B
|nbsp|              HE802SA                              Dimmer Set                         B
|nbsp|              HE802SF                              Dimmer Set                         B
|nbsp|              HE803S                               Dimmer Set                         B
|nbsp|              HE805S                               Switch Set (flush-mounted)         B
|nbsp|              HE808S                               Switch Set                         B
|nbsp|              HE815S                               Dimmer/Switch Set                  B
|nbsp|              HE820                                Gong                               B
|nbsp|              HE821S                               Gong with light                    B
|nbsp|              HE831S                               Outdoor Switch Set                 B
|nbsp|              HE834S                               Outdoor Switch Set                 B
|nbsp|              HE844A                               Remote                             B
|nbsp|              HE866                                Outdoor build-in Switch            B
|nbsp|              HE867                                Outdoor Switch                     B
|nbsp|              HE871                                Bulb Holder Switch                 B
|nbsp|              HE872                                Bulb Holder Switch Dimmer          B
|nbsp|              HE874                                Switch                             C
|nbsp|              HE875                                Mini-Switch                        B
|nbsp|              HE877                                Switch                             B
|nbsp|              HE877A                               Switch with On/Off at Receiver     B
|nbsp|              HE878                                Switch                             B
|nbsp|              HE878A                               Dimmer                             B
|nbsp|              HE881                                Build-in Switch                    B
|nbsp|              HE886                                Switch (flush-mounted)             B
|nbsp|              HE888                                Dimmer (flush-mounted)             B
|nbsp|              HE889                                Blind Switch (flush-mounted)       B
|nbsp|              HE876                                Mini-Dimmer                        B
|nbsp|              HE892S                               Outlet Strip                       B
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Intertechno         CMR-300                              Dimmer (flush-mounted)             C
|nbsp|              CMR-500                              Blind Switch (flush-mounted)       C
|nbsp|              CMR-1000                             Switch (flush-mounted)             C
|nbsp|              CMR-1001                             Impulse Switch (flush-mounted)     C
|nbsp|              CMR-1224                             12/24V Switch (flush-mounted)      C
|nbsp|              HDR-105                              12V Dimmer                         C
|nbsp|              GR-300                               Outdoor Dimmer                     C
|nbsp|              GRR-300                              Outdoor Dimmer                     B
|nbsp|              GRR-3500                             Outdoor Switch                     B
|nbsp|              IT-1500                              Switch Set                         B
|nbsp|              IT-2300                              4x Switch                          B
|nbsp|              IT-3500L                             Switch                             B
|nbsp|              ITDL-1000                            Switch (flush-mounted)             B
|nbsp|              ITDM-250                             LED Dimmer (flush-mounted)         B
|nbsp|              ITE-300                              Dimmer (flush-mounted)             C
|nbsp|              ITE-1000                             Switch (flush-mounted)             C
|nbsp|              ITK-200                              Remote                             C
|nbsp|              ITL-150                              Dimmer (flush-mounted)             B
|nbsp|              ITL-210                              Dimmer (flush-mounted)             B
|nbsp|              ITL-230                              Switch (flush-mounted)             B
|nbsp|              ITL-250                              LED Dimmer (flush-mounted)         B
|nbsp|              ITL-300                              Dimmer (flush-mounted)             B
|nbsp|              ITL-500                              Blind Switch (flush-mounted)       B
|nbsp|              ITL-1000                             Timer Switch (flush-mounted)       B
|nbsp|              ITL-3500                             Switch (flush-mounted)             B
|nbsp|              ITLR-300                             Dimmer                             B
|nbsp|              ITLR-3500                            Switch                             B
|nbsp|              ITR-300                              Dimmer                             C
|nbsp|              ITR-1500                             Switch Set                         B
|nbsp|              ITR-3500                             Switch                             C
|nbsp|              ITR-7000                             Gong                               B
|nbsp|              ITT-1500                             Remote                             B
|nbsp|              LBUR-100                             Bulb Holder Switch                 B
|nbsp|              PA3-1000                             Switch Set                         C
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Mumbi               m-FS300 (year 2013 model)            Switch Set                         A
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
ONE FOR ALL         HC-8000                              Switch Set                         C
------------------- ------------------------------------ ---------------------------------- -------
------------------- ------------------------------------ ---------------------------------- -------
Vivanco             FSS 31000W                           Switch Set                         A
|nbsp|              FSS 33600W                           Switch Set                         A
=================== ==================================== ================================== =======


Switch 230V devices
^^^^^^^^^^^^^^^^^^^

Switching 230V devices is a typical application. Devices for this come in
several forms. For example, as intermediate adapter that goes into your
standard socket (e.g. Intertechno ITR-1500 and ELRO HE874) or designed for
flush-mounting (e.g. Intertechno ITL-1000). Additional features such as
timers to turn off the connected device after a given amount of time are
also available.

.. image:: /Images/Bricklets/bricklet_remote_it_homeeasy_350.jpg
   :scale: 100 %
   :alt: Intertechno ITR-1500 Switch and ELRO HE874 Switch
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_homeeasy_1000.jpg

.. image:: /Images/Bricklets/bricklet_remote_it_itl_1000_350.jpg
   :scale: 100 %
   :alt: Intertechno ITL-1000 Timer Switch (flush-mounted)
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_itl_1000_1000.jpg


Switch 12/24V devices
^^^^^^^^^^^^^^^^^^^^^

Low-voltage or battery powered systems are common in cars, trucks and boats.
There are specialized remote switches that operate on 12/24V (e.g. Intertechno
CMR-1224).

.. image:: /Images/Bricklets/bricklet_remote_it_cmr_1224_350.jpg
   :scale: 100 %
   :alt: Intertechno CMR-1224 12/24V Switch (flush-mounted)
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_cmr_1224_1000.jpg


Dim (energy-saving) light bulbs and LEDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to simple on/off switches there are also dimmers for normal lamps
(e.g. Intertechno ITLR-300), for energy-saving lamps (e.g. Intertechno
ITL-150) and for LED lamps (e.g. Intertechno ITL-250).

.. image:: /Images/Bricklets/bricklet_remote_it_dimmer_350.jpg
   :scale: 100 %
   :alt: Intertechno ITLR-300 Dimmer
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_dimmer_1000.jpg


Control Garage Doors and Blinds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For garage doors and blinds simple on/off switches are not enough. For this
applications there are specialized remote switches that can handle three state
up, down and off (e.g. Intertechno CMR-500).

.. image:: /Images/Bricklets/bricklet_remote_it_cmr_500_350.jpg
   :scale: 100 %
   :alt: Intertechno CMR-500 Blind Switch (flush-mounted)
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_cmr_500_1000.jpg


Trigger Gongs
^^^^^^^^^^^^^

Beside switches in different variations there are also gongs (e.g. Intertechno
ITR-7000) that can draw attention with sound and/or light signals and are
trigger remotely.

.. image:: /Images/Bricklets/bricklet_remote_it_gong_350.jpg
   :scale: 100 %
   :alt: Intertechno ITR-7000 Gong
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_gong_1000.jpg


.. _remote_switch_v2_bricklet_addressing_types:

Addressing Types
----------------

To control remote switches or dimmers their address must be known.
The Remote Switch Bricklet 2.0 supports different addressing types. How to figure
out or set the address of your device is described below. See the :ref:`list
of supported devices <remote_switch_v2_supported_devices>` for the specific
addressing type of your device.


.. _remote_switch_v2_bricklet_type_a_house_and_receiver_code:

Type A: House Code and Receiver Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The house and receiver codes are typically configurable with small DIP-switches
inside the remote switch or dimmer. Please note that house and receiver code
is sometimes labeled differently. In the following example image the removed
cover of the DIP switch is labeled with "System Code" and "Unit Code".
"System Code" means house code and with "Unit Code" the receiver code is meant.

In the image below DIP-switches 1 and 5 are on for the house code, this equals
10001 in binary (least-significant bit first) or 17 in decimal. For the receiver
code only DIP-switch A is on, this equals 10000 in binary (least-significant bit
first) or 1 in decimal.

.. image:: /Images/Bricklets/bricklet_remote_dip_switch_350.jpg
   :scale: 100 %
   :alt: DIP switch in remote switch to set type A house and receiver code
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_dip_switch_1000.jpg


.. _remote_switch_v2_bricklet_type_b_address_and_unit:

Type B: Address and Unit
^^^^^^^^^^^^^^^^^^^^^^^^

Devices of type B do not have switches to configure their address and unit.
Instead the remote switch or dimmer has to learn its address and unit.
Depending on the specific device at hand it is in learning mode for some
seconds after it has been plugged in (left one from Intertechno in the image
below) or it has a button that has to be pushed to enter learning mode (right
one from ELRO in the image below). While in learning mode you have to send a
switch-on command to the device with the address and unit that should be
assigned to the device. Maybe it is necessary to send this command several 
times until the device leaves the learning mode.

.. image:: /Images/Bricklets/bricklet_remote_it_homeeasy_350.jpg
   :scale: 100 %
   :alt: Learing remote switches from Intertechno and ELRO
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_homeeasy_1000.jpg


.. _remote_switch_v2_bricklet_type_c_system_and_device_code:

Type C: System Code and Device Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The system and device code are typically configurable with code wheels on the
back of the remote switch or dimmer. Please note that the system code is
sometimes called differently. For example, "House Code", "System Character"
or "Family Code".

In the image below the left code wheel (A-P) is set to M for the system code
and the right code wheel (1-16) is set to 1 for the device code.

.. image:: /Images/Bricklets/bricklet_remote_it_cmr_500_350.jpg
   :scale: 100 %
   :alt: Code wheels on blind switch to set system code and device code
   :align: center
   :target: ../../_images/Bricklets/bricklet_remote_it_cmr_500_1000.jpg


.. _remote_switch_v2_usage_as_receiver:

Usage as Receiver
-----------------

Typically remote mains switches come with a remote. The signals of these remotes 
can be read out with the Remote Switch Bricklet 2.0.

For that the Bricklet has to be configured to receive the signals of the corresponding
addressing type. After that the received data can be read out.

.. _remote_switch_v2_bricklet_case:

Case
----

A `laser-cut case for the Remote Switch Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-remote-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_remote_case_tilted_front_350.jpg
   :scale: 100 %
   :alt: Case for Remote Switch Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_remote_case_tilted_front_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet (the antenna plate is slightly
  asymmetric, the wider margin goes to the bottom side, when viewed from the outside),
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Temperature IR Bricklet case:

.. image:: /Images/Exploded/remote_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Remote Switch Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/remote_exploded.png

|bricklet_case_hint|


.. _remote_switch_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Remote_Switch_V2_hlpi.table
