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
   Downloads

.. toctree::
   :maxdepth: 1

   Programming_Interfaces
   Technical_Data
   Source_Code


.. _index_bricks:

******
Bricks
******

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   Hardware/Bricks/*

.. container:: indextable

 .. csv-table::
  :delim: |

  * :ref:`DC <dc_brick>`           | :ref:`TCP/IP <dc_brick_tcpip>`,      :ref:`C/C++ <dc_brick_c>`,      :ref:`C# <dc_brick_csharp>`,      :ref:`Java <dc_brick_java>`,      :ref:`PHP <dc_brick_php>`,      :ref:`Python <dc_brick_python>`
  * :ref:`Debug <debug_brick>`     |
  * :ref:`IMU <imu_brick>`         | :ref:`TCP/IP <imu_brick_tcpip>`,     :ref:`C/C++ <imu_brick_c>`,     :ref:`C# <imu_brick_csharp>`,     :ref:`Java <imu_brick_java>`,     :ref:`PHP <imu_brick_php>`,     :ref:`Python <imu_brick_python>`
  * :ref:`Master <master_brick>`   | :ref:`TCP/IP <master_brick_tcpip>`,  :ref:`C/C++ <master_brick_c>`,  :ref:`C# <master_brick_csharp>`,  :ref:`Java <master_brick_java>`,  :ref:`PHP <master_brick_php>`,  :ref:`Python <master_brick_python>`
  * :ref:`Servo <servo_brick>`     | :ref:`TCP/IP <servo_brick_tcpip>`,   :ref:`C/C++ <servo_brick_c>`,   :ref:`C# <servo_brick_csharp>`,   :ref:`Java <servo_brick_java>`,   :ref:`PHP <servo_brick_php>`,   :ref:`Python <servo_brick_python>`
  * :ref:`Stepper <stepper_brick>` | :ref:`TCP/IP <stepper_brick_tcpip>`, :ref:`C/C++ <stepper_brick_c>`, :ref:`C# <stepper_brick_csharp>`, :ref:`Java <stepper_brick_java>`, :ref:`PHP <stepper_brick_php>`, :ref:`Python <stepper_brick_python>`


.. _index_bricklets:

*********
Bricklets
*********

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   Hardware/Bricklets/*

.. container:: indextable

 .. csv-table::
  :delim: |

  * :ref:`Ambient Light <ambient_light_bricklet>`   | :ref:`TCP/IP <ambient_light_bricklet_tcpip>`,  :ref:`C/C++ <ambient_light_bricklet_c>`,  :ref:`C# <ambient_light_bricklet_csharp>`,  :ref:`Java <ambient_light_bricklet_java>`,  :ref:`PHP <ambient_light_bricklet_php>`,  :ref:`Python <ambient_light_bricklet_python>`
  * :ref:`Analog In <analog_in_bricklet>`           | :ref:`TCP/IP <analog_in_bricklet_tcpip>`,      :ref:`C/C++ <analog_in_bricklet_c>`,      :ref:`C# <analog_in_bricklet_csharp>`,      :ref:`Java <analog_in_bricklet_java>`,      :ref:`PHP <analog_in_bricklet_php>`,      :ref:`Python <analog_in_bricklet_python>`
  * :ref:`Analog Out <analog_out_bricklet>`         | :ref:`TCP/IP <analog_out_bricklet_tcpip>`,     :ref:`C/C++ <analog_out_bricklet_c>`,     :ref:`C# <analog_out_bricklet_csharp>`,     :ref:`Java <analog_out_bricklet_java>`,     :ref:`PHP <analog_out_bricklet_php>`,     :ref:`Python <analog_out_bricklet_python>`
  * :ref:`Breakout <breakout_bricklet>`             |
  * :ref:`Current12 <current12_bricklet>`           | :ref:`TCP/IP <current12_bricklet_tcpip>`,      :ref:`C/C++ <current12_bricklet_c>`,      :ref:`C# <current12_bricklet_csharp>`,      :ref:`Java <current12_bricklet_java>`,      :ref:`PHP <current12_bricklet_php>`,      :ref:`Python <current12_bricklet_python>`
  * :ref:`Current25 <current25_bricklet>`           | :ref:`TCP/IP <current25_bricklet_tcpip>`,      :ref:`C/C++ <current25_bricklet_c>`,      :ref:`C# <current25_bricklet_csharp>`,      :ref:`Java <current25_bricklet_java>`,      :ref:`PHP <current25_bricklet_php>`,      :ref:`Python <current25_bricklet_python>`
  * :ref:`Distance IR <distance_ir_bricklet>`       | :ref:`TCP/IP <distance_ir_bricklet_tcpip>`,    :ref:`C/C++ <distance_ir_bricklet_c>`,    :ref:`C# <distance_ir_bricklet_csharp>`,    :ref:`Java <distance_ir_bricklet_java>`,    :ref:`PHP <distance_ir_bricklet_php>`,    :ref:`Python <distance_ir_bricklet_python>`
  * :ref:`Dual Relay <dual_relay_bricklet>`         | :ref:`TCP/IP <dual_relay_bricklet_tcpip>`,     :ref:`C/C++ <dual_relay_bricklet_c>`,     :ref:`C# <dual_relay_bricklet_csharp>`,     :ref:`Java <dual_relay_bricklet_java>`,     :ref:`PHP <dual_relay_bricklet_php>`,     :ref:`Python <dual_relay_bricklet_python>`
  * :ref:`Humidity <humidity_bricklet>`             | :ref:`TCP/IP <humidity_bricklet_tcpip>`,       :ref:`C/C++ <humidity_bricklet_c>`,       :ref:`C# <humidity_bricklet_csharp>`,       :ref:`Java <humidity_bricklet_java>`,       :ref:`PHP <humidity_bricklet_php>`,       :ref:`Python <humidity_bricklet_php>`
  * :ref:`IO4 <io4_bricklet>`                       | :ref:`TCP/IP <io4_bricklet_tcpip>`,            :ref:`C/C++ <io4_bricklet_c>`,            :ref:`C# <io4_bricklet_csharp>`,            :ref:`Java <io4_bricklet_java>`,            :ref:`PHP <io4_bricklet_php>`,            :ref:`Python <io4_bricklet_python>`
  * :ref:`IO16 <io16_bricklet>`                     | :ref:`TCP/IP <io16_bricklet_tcpip>`,           :ref:`C/C++ <io16_bricklet_c>`,           :ref:`C# <io16_bricklet_csharp>`,           :ref:`Java <io16_bricklet_java>`,           :ref:`PHP <io16_bricklet_php>`,           :ref:`Python <io16_bricklet_python>`
  * :ref:`Joystick <joystick_bricklet>`             | :ref:`TCP/IP <joystick_bricklet_tcpip>`,       :ref:`C/C++ <joystick_bricklet_c>`,       :ref:`C# <joystick_bricklet_csharp>`,       :ref:`Java <joystick_bricklet_java>`,       :ref:`PHP <joystick_bricklet_php>`,       :ref:`Python <joystick_bricklet_python>`
  * :ref:`LCD 16x2 <lcd_16x2_bricklet>`             | :ref:`TCP/IP <lcd_16x2_bricklet_tcpip>`,       :ref:`C/C++ <lcd_16x2_bricklet_c>`,       :ref:`C# <lcd_16x2_bricklet_csharp>`,       :ref:`Java <lcd_16x2_bricklet_java>`,       :ref:`PHP <lcd_16x2_bricklet_php>`,       :ref:`Python <lcd_16x2_bricklet_python>`
  * :ref:`LCD 20x4 <lcd_20x4_bricklet>`             | :ref:`TCP/IP <lcd_20x4_bricklet_tcpip>`,       :ref:`C/C++ <lcd_20x4_bricklet_c>`,       :ref:`C# <lcd_20x4_bricklet_csharp>`,       :ref:`Java <lcd_20x4_bricklet_java>`,       :ref:`PHP <lcd_20x4_bricklet_php>`,       :ref:`Python <lcd_20x4_bricklet_python>`
  * :ref:`Piezo Buzzer <piezo_buzzer_bricklet>`     | :ref:`TCP/IP <piezo_buzzer_bricklet_tcpip>`,   :ref:`C/C++ <piezo_buzzer_bricklet_c>`,   :ref:`C# <piezo_buzzer_bricklet_csharp>`,   :ref:`Java <piezo_buzzer_bricklet_java>`,   :ref:`PHP <piezo_buzzer_bricklet_php>`,   :ref:`Python <piezo_buzzer_bricklet_python>`
  * :ref:`Rotary Poti <rotary_poti_bricklet>`       | :ref:`TCP/IP <rotary_poti_bricklet_tcpip>`,    :ref:`C/C++ <rotary_poti_bricklet_c>`,    :ref:`C# <rotary_poti_bricklet_csharp>`,    :ref:`Java <rotary_poti_bricklet_java>`,    :ref:`PHP <rotary_poti_bricklet_php>`,    :ref:`Python <rotary_poti_bricklet_python>`
  * :ref:`Linear Poti <linear_poti_bricklet>`       | :ref:`TCP/IP <linear_poti_bricklet_tcpip>`,    :ref:`C/C++ <linear_poti_bricklet_c>`,    :ref:`C# <linear_poti_bricklet_csharp>`,    :ref:`Java <linear_poti_bricklet_java>`,    :ref:`PHP <linear_poti_bricklet_php>`,    :ref:`Python <linear_poti_bricklet_python>`
  * :ref:`Temperature <temperature_bricklet>`       | :ref:`TCP/IP <temperature_bricklet_tcpip>`,    :ref:`C/C++ <temperature_bricklet_c>`,    :ref:`C# <temperature_bricklet_csharp>`,    :ref:`Java <temperature_bricklet_java>`,    :ref:`PHP <temperature_bricklet_php>`,    :ref:`Python <temperature_bricklet_python>`
  * :ref:`Temperature IR <temperature_ir_bricklet>` | :ref:`TCP/IP <temperature_ir_bricklet_tcpip>`, :ref:`C/C++ <temperature_ir_bricklet_c>`, :ref:`C# <temperature_ir_bricklet_csharp>`, :ref:`Java <temperature_ir_bricklet_java>`, :ref:`PHP <temperature_ir_bricklet_php>`, :ref:`Python <temperature_ir_bricklet_python>`
  * :ref:`Voltage <voltage_bricklet>`               | :ref:`TCP/IP <voltage_bricklet_tcpip>`,        :ref:`C/C++ <voltage_bricklet_c>`,        :ref:`C# <voltage_bricklet_csharp>`,        :ref:`Java <voltage_bricklet_java>`,        :ref:`PHP <voltage_bricklet_php>`,        :ref:`Python <voltage_bricklet_python>`


*****************
Master Extensions
*****************

.. toctree::
   :maxdepth: 1
   :glob:

   Hardware/Master_Extensions/Chibi_Extension
   Hardware/Master_Extensions/RS485_Extension

**************
Power Supplies
**************

.. toctree::
   :maxdepth: 1
   :glob:

   Hardware/Power_Supplies/*

*****
Tools
*****

.. toctree::
   :maxdepth: 1
   :glob:

   Hardware/Tools/DC_Jack_Adapter


.. toctree::
   :glob:
   :hidden:

   Software/*
   Software/Bricks/*
   Software/Bricklets/*
