.. Tinkerforge documentation master file, created by
   sphinx-quickstart on Fri Apr 29 12:57:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#############
Documentation
#############

.. toctree::
   :maxdepth: 2

   Product_Overview
   Tutorials/Tutorial
   Software
   Low_Level_Protocols
   Downloads

.. toctree::
   :maxdepth: 1

   Timeline
   Programming_Interfaces
   Technical_Data
   Source_Code
   Protocol_20


.. _index_embedded_boards:

**************************
Usage with Embedded Boards
**************************

.. toctree::
   :maxdepth: 1
   :glob:

   Embedded/*

.. _index_ip_connection:

*************
IP Connection
*************

.. container:: indextable

 .. csv-table::
  :delim: |

  * :ref:`IP Connection <api_bindings_ip_connection>` | :ref:`Modbus <llproto_modbus_api>`, :ref:`TCP/IP <llproto_tcpip_api>`, :ref:`C/C++ <ipcon_c>`, :ref:`C# <ipcon_csharp>`, :ref:`Delphi <ipcon_delphi>`, :ref:`Java <ipcon_java>`, :ref:`PHP <ipcon_php>`, :ref:`Python <ipcon_python>`, :ref:`Ruby <ipcon_ruby>`

.. _index_bricks:

******
Bricks
******

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   Hardware/Bricks/*

.. include:: index_bricks.table


.. _index_bricklets:

*********
Bricklets
*********

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   Hardware/Bricklets/*

.. include:: index_bricklets.table


*****************
Master Extensions
*****************

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   Hardware/Master_Extensions/*

.. include:: index_extensions.table


**************
Power Supplies
**************

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   Hardware/Power_Supplies/*

.. include:: index_power_supplies.table


***********
Accessories
***********

.. toctree::
   :maxdepth: 1
   :glob:

   Hardware/Accessories/DC_Jack_Adapter


.. toctree::
   :glob:
   :hidden:

   Software/*
   Software/Bricks/*
   Software/Bricklets/*
