.. Tinkerforge documentation master file, created by
   sphinx-quickstart on Fri Apr 29 12:57:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#########################
Tinkerforge Documentation
#########################

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
			
  * :ref:`DC_Brick`      | :ref:`C/C++ <dc_brick_c>`,      :ref:`C# <dc_brick_csharp>`,      :ref:`Java <dc_brick_java>`,      :ref:`Python <dc_brick_python>`
  * :ref:`IMU_Brick`     | :ref:`C/C++ <imu_brick_c>`,     :ref:`C# <imu_brick_csharp>`,     :ref:`Java <imu_brick_java>`,     :ref:`Python <imu_brick_python>`
  * :ref:`Master_Brick`  | :ref:`C/C++ <master_brick_c>`,  :ref:`C# <master_brick_csharp>`,  :ref:`Java <master_brick_java>`,  :ref:`Python <master_brick_python>`
  * :ref:`Servo_Brick`   | :ref:`C/C++ <servo_brick_c>`,   :ref:`C# <servo_brick_csharp>`,   :ref:`Java <servo_brick_java>`,   :ref:`Python <servo_brick_python>`
  * :ref:`Stepper_Brick` | :ref:`C/C++ <stepper_brick_c>`, :ref:`C# <stepper_brick_csharp>`, :ref:`Java <stepper_brick_java>`, :ref:`Python <stepper_brick_python>`

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

  * :ref:`ambient_light_bricklet`  | :ref:`C/C++ <ambient_light_bricklet_c>`,  :ref:`C# <ambient_light_bricklet_csharp>`,  :ref:`Java <ambient_light_bricklet_java>`,  :ref:`Python <ambient_light_bricklet_python>`
  * :ref:`current12_bricklet`      | :ref:`C/C++ <current12_bricklet_c>`,      :ref:`C# <current12_bricklet_csharp>`,      :ref:`Java <current12_bricklet_java>`,      :ref:`Python <current12_bricklet_python>`
  * :ref:`current25_bricklet`      | :ref:`C/C++ <current25_bricklet_c>`,      :ref:`C# <current25_bricklet_csharp>`,      :ref:`Java <current25_bricklet_java>`,      :ref:`Python <current25_bricklet_python>`
  * :ref:`distance_ir_bricklet`    | :ref:`C/C++ <distance_ir_bricklet_c>`,    :ref:`C# <distance_ir_bricklet_csharp>`,    :ref:`Java <distance_ir_bricklet_java>`,    :ref:`Python <distance_ir_bricklet_python>`
  * :ref:`dual_relay_bricklet`     | :ref:`C/C++ <dual_relay_bricklet_c>`,     :ref:`C# <dual_relay_bricklet_csharp>`,     :ref:`Java <dual_relay_bricklet_java>`,     :ref:`Python <dual_relay_bricklet_python>`
  * :ref:`humidity_bricklet`       | :ref:`C/C++ <humidity_bricklet_c>`,       :ref:`C# <humidity_bricklet_csharp>`,       :ref:`Java <humidity_bricklet_java>`,       :ref:`Python <humidity_bricklet_python>`
  * :ref:`io16_bricklet`           | :ref:`C/C++ <io16_bricklet_c>`,           :ref:`C# <io16_bricklet_csharp>`,           :ref:`Java <io16_bricklet_java>`,           :ref:`Python <io16_bricklet_python>`
  * :ref:`io4_bricklet`            | :ref:`C/C++ <io4_bricklet_c>`,            :ref:`C# <io4_bricklet_csharp>`,            :ref:`Java <io4_bricklet_java>`,            :ref:`Python <io4_bricklet_python>`
  * :ref:`joystick_bricklet`       | :ref:`C/C++ <joystick_bricklet_c>`,       :ref:`C# <joystick_bricklet_csharp>`,       :ref:`Java <joystick_bricklet_java>`,       :ref:`Python <joystick_bricklet_python>`
  * :ref:`lcd_16x2_bricklet`       | :ref:`C/C++ <lcd_16x2_bricklet_c>`,       :ref:`C# <lcd_16x2_bricklet_csharp>`,       :ref:`Java <lcd_16x2_bricklet_java>`,       :ref:`Python <lcd_16x2_bricklet_python>`
  * :ref:`lcd_20x4_bricklet`       | :ref:`C/C++ <lcd_20x4_bricklet_c>`,       :ref:`C# <lcd_20x4_bricklet_csharp>`,       :ref:`Java <lcd_20x4_bricklet_java>`,       :ref:`Python <lcd_20x4_bricklet_python>`
  * :ref:`linear_poti_bricklet`    | :ref:`C/C++ <linear_poti_bricklet_c>`,    :ref:`C# <linear_poti_bricklet_csharp>`,    :ref:`Java <linear_poti_bricklet_java>`,    :ref:`Python <linear_poti_bricklet_python>`
  * :ref:`piezo_buzzer_bricklet`   | :ref:`C/C++ <piezo_buzzer_bricklet_c>`,   :ref:`C# <piezo_buzzer_bricklet_csharp>`,   :ref:`Java <piezo_buzzer_bricklet_java>`,   :ref:`Python <piezo_buzzer_bricklet_python>`
  * :ref:`rotary_poti_bricklet`    | :ref:`C/C++ <rotary_poti_bricklet_c>`,    :ref:`C# <rotary_poti_bricklet_csharp>`,    :ref:`Java <rotary_poti_bricklet_java>`,    :ref:`Python <rotary_poti_bricklet_python>`
  * :ref:`temperature_bricklet`    | :ref:`C/C++ <temperature_bricklet_c>`,    :ref:`C# <temperature_bricklet_csharp>`,    :ref:`Java <temperature_bricklet_java>`,    :ref:`Python <temperature_bricklet_python>`
  * :ref:`temperature_ir_bricklet` | :ref:`C/C++ <temperature_ir_bricklet_c>`, :ref:`C# <temperature_ir_bricklet_csharp>`, :ref:`Java <temperature_ir_bricklet_java>`, :ref:`Python <temperature_ir_bricklet_python>`
  * :ref:`voltage_bricklet`        | :ref:`C/C++ <voltage_bricklet_c>`,        :ref:`C# <voltage_bricklet_csharp>`,        :ref:`Java <voltage_bricklet_java>`,        :ref:`Python <voltage_bricklet_python>`

*****************
Master Extensions
*****************

.. toctree::
   :maxdepth: 1
   :glob:

   Hardware/Master_Extensions/*

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

   Hardware/Tools/*


.. toctree::
   :glob:
   :hidden:

   Software/*
   Software/Bricks/*
   Software/Bricklets/*

******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
