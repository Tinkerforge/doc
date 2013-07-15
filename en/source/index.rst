.. Tinkerforge documentation master file, created by
   sphinx-quickstart on Fri Apr 29 12:57:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#############
Documentation
#############


.. _index_product_overview:

****************
Product Overview
****************

Our :ref:`products <product_overview>` are divided into five different categories:

* :ref:`product_overview_bricks`
* :ref:`product_overview_bricklets`
* :ref:`product_overview_master_extensions`
* :ref:`product_overview_power_supplies`
* :ref:`product_overview_accessories`

This :ref:`Timeline <timeline>` presents an overview of future products and
developments.

.. toctree::
   :hidden:

   Product_Overview
   Timeline

.. _index_tutorials:

*****************
Tutorials and FAQ
*****************

These Tutorials are an introduction to the usage of Bricks and Bricklets
and their concepts:

* :ref:`First Steps <tutorial_first_steps>`
* :ref:`Rugged Approach <tutorial_rugged_approach>`

Answers to frequently asked questions can be found in the :ref:`FAQ <faq>`.

.. toctree::
   :hidden:

   Tutorials/Tutorial_Extending/Tutorial
   Tutorials/Tutorial_Rugged/Tutorial
   FAQ


.. _index_kits:

****
Kits
****

We offer kits for different subject areas so you can get started more easily
with Tinkerforge:

* :ref:`starter_kit_weather_station`

.. * :ref:`starter_kit_hardware_hacking`

.. toctree::
   :hidden:

   Kits/WeatherStation/WeatherStation
   Kits/HardwareHacking/HardwareHacking


.. _index_software:

********
Software
********

The software includes service and test programs, the API to interact with Bricks
and Bricklets as well as their firmwares and plugins:

* :ref:`brickd`
* :ref:`brickv`
* :ref:`api_bindings`
* :ref:`firmwares_and_plugins`

Those can be downloaded in the :ref:`downloads section <downloads>`. The
:ref:`source code and links for bug trackers <source_code>` can be found in
their own section.

The basics of the different programming interfaces are described
:ref:`here <pi>`.

In `January 2013 <http://www.tinkerforge.com/en/blog/2013/1/15/protocol-2-0-available>`__
we updated the communication protocol used for Bricks. For programs that were
developed before this time we provide a guide for the :ref:`transitioning from
Protocol 1.0 to Protocol 2.0 <transition_1to2>`.

.. toctree::
   :hidden:

   Software/Brickd
   Software/Brickv
   Software/API_Bindings
   Software/Firmwares_And_Plugins
   Downloads
   Source_Code
   Programming_Interfaces
   Transitioning_Guide_1To2

.. toctree::
   :glob:
   :hidden:

   Software/*
   Software/Bricks/*
   Software/Bricklets/*


.. _index_embedded_boards:

***************
Embedded Boards
***************

Bricks and Bricklets can easily be combined with different embedded boards:

.. toctree::
   :maxdepth: 1
   :glob:

   Embedded/*


.. _index_spec:

**************
Specifications
**************

This specifications include the :ref:`technical data <technical_data>`
for the connectors used on Bricks and Bricklets as well as the different low
level protocols:

* :ref:`llproto_tcpip`
* :ref:`llproto_modbus`

.. toctree::
   :hidden:

   Technical_Data
   Low_Level_Protocols/TCPIP
   Low_Level_Protocols/Modbus


.. _index_links:

*****
Links
*****

The following table summarizes the hardware and API documentation for quick
access:

.. include:: index_links.table

.. toctree::
   :glob:
   :hidden:

   Hardware/Bricks/*
   Hardware/Bricklets/*
   Hardware/Master_Extensions/*
   Hardware/Power_Supplies/*
   Hardware/Accessories/*

The documentation for Protocol 1.0 can be found
`here <http://www.tinkerforge.com/en/doc_v1/index.html>`__.
