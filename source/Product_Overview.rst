.. _product_overview:

Product Overview
----------------

There are four different types of hardware components:

* :ref:`Bricks <product_overview_bricks>`: 
  Stackable microcontroller boards for sensing and controlling.
* :ref:`Master Extensions <product_overview_master_extensions>`:
  Boards that extend the communication interfaces of a
  :ref:`Master Brick <master_brick>`.
* :ref:`Bricklets <product_overview_bricklets>`:
  Non-stackable sensor/actor boards that extend the features of a Brick.
* :ref:`Power Supplies <product_overview_powersupplies>`:
  Boards to power a Stack of Bricks, plugged below the Stack.


See the :ref:`tutorial <tutorial>` for an explanation of how everything works
together.


.. _product_overview_bricks:

Bricks
^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricks/brick_master_tilted_front_100.jpg
       :scale: 100 %
       :alt: Master Brick
       :align: center
       :target: _images/Bricks/brick_master_tilted_front_800.jpg
	   
    - .. image:: /Images/Bricks/brick_dc_tilted_front_100.jpg
       :scale: 100 %
       :alt: DC Brick
       :align: center
       :target: _images/Bricks/brick_dc_tilted_front_800.jpg
	   
    - .. image:: /Images/Bricks/brick_stepper_tilted_front_100.jpg
       :scale: 100 %
       :alt: Stepper Brick
       :align: center
       :target: _images/Bricks/brick_stepper_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_servo_tilted_front_100.jpg
       :scale: 100 %
       :alt: Servo Brick
       :align: center
       :target: _images/Bricks/brick_servo_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_imu_tilted_front_100.jpg
       :scale: 100 %
       :alt: IMU Brick
       :align: center
       :target: _images/Bricks/brick_imu_tilted_front_800.jpg


Bricks are 4 x 4cm (1.57" x 1.57") boards equipped with a 32bit
microcontroller, an USB port, two status LEDs, connectors for 
stacking and up to four connectors for 
:ref:`Bricklets <product_overview_bricklets>`. 
There are Bricks that perform complex 
sensor tasks (e.g. :ref:`IMU Brick <imu_brick>`), 
communicate (e.g. :ref:`Master Brick <master_brick>`) 
and drive motors (e.g. :ref:`DC Brick <dc_brick>`).

Bricks can be plugged together to a Stack. A Master Brick
at the bottom of this Stack can control all boards within the Stack. 
This master routes the messages between the boards in the Stack and the PC 
(:ref:`High Level Programming Interface <pi_hlpi>`).
For the user, the stack behaves as if all Bricks are connected separately 
over USB with the PC. 
See :ref:`Tutorial Stacking <tutorial_build_stacks>` for more information
about Stacks.

Besides the :ref:`High Level Programming Interface <pi_hlpi>` it is also
possible to use Bricks with the
:ref:`Low Level Programming Interface <pi_llpi>`
or the :ref:`On Device Programming Interface <pi_hlpi>`.

.. csv-table::
   :header: "Name", "Description", "C/C++", "C#", "Java", "Python"
   :widths: 15, 40, 5, 5, 5, 5

   ":ref:`dc_brick`", "3A DC Motor Driver", ":ref:`C/C++ <dc_brick_c>`", ":ref:`C# <dc_brick_csharp>`", ":ref:`Java <dc_brick_java>`", ":ref:`Python <dc_brick_python>`"
   ":ref:`imu_brick`", "IMU with 9 degrees of freedom", ":ref:`C/C++ <imu_brick_c>`", ":ref:`C# <imu_brick_csharp>`", ":ref:`Java <imu_brick_java>`", ":ref:`Python <imu_brick_python>`"
   ":ref:`master_brick`", "Allow building of Stacks, 4 Bricklet Ports", ":ref:`C/C++ <master_brick_c>`", ":ref:`C# <master_brick_csharp>`", ":ref:`Java <master_brick_java>`", ":ref:`Python <master_brick_python>`"
   ":ref:`servo_brick`", "Control up to 7 Servos", ":ref:`C/C++ <servo_brick_c>`", ":ref:`C# <servo_brick_csharp>`", ":ref:`Java <servo_brick_java>`", ":ref:`Python <servo_brick_python>`"
   ":ref:`stepper_brick`", "2.5A Stepper Motor Driver", ":ref:`C/C++ <stepper_brick_c>`", ":ref:`C# <stepper_brick_csharp>`", ":ref:`Java <stepper_brick_java>`", ":ref:`Python <stepper_brick_python>`"


.. _product_overview_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Extensions/extension_chibi_tilted_100.jpg
       :scale: 100 %
       :alt: Chibi Extension
       :align: center
       :target: _images/Extensions/extension_chibi_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_rs485_tilted_100.jpg
       :scale: 100 %
       :alt: RS485 Extension
       :align: center
       :target: _images/Extensions/extension_rs485_tilted_800.jpg

When using the :ref:`High Level Programming Interface <pi_hlpi>` concept,
:ref:`Master Bricks <master_brick>` can route messages between 
:ref:`Bricks <product_overview_bricks>` and the PC. To establish a connection 
between a PC and the Master Brick, typically the USB port is used.
Master Extensions can be utilized to change the interface of a Master Brick.
There are cable based and wireless Master Extensions available. The usage 
of the different interfaces is transparent. 
It behaves as if every board of the Stack is directly connected to the 
PC with its USB connection. This means:

You can develop an application with all
boards independently connected to the PC over USB. Later you can plug these 
boards together to Stacks, add Master Bricks and cable based or wireless
Extensions and can run the previously written code without any changes.

.. csv-table::
   :header: "Name", "Description"
   :widths: 20, 70 

   ":ref:`chibi_extension`", "Wireless Chibi Master Extension"
   ":ref:`rs485_extension`", "Cable based RS485 Master Extension"


.. _product_overview_bricklets:

Bricklets
^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricklets/bricklet_dual_relay_tilted_100.jpg
       :scale: 100 %
       :alt: Dual Relay Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_dual_relay_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_joystick_tilted_100.jpg
       :scale: 100 %
       :alt: Joystick Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_joystick_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_lcd_20x4_tilted_100.jpg
       :scale: 100 %
       :alt: LCD 20x4 Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_lcd_20x4_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_temperature_ir_tilted_100.jpg
       :scale: 100 %
       :alt: Temperature IR Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_temperature_ir_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_linear_poti_tilted_100.jpg
       :scale: 100 %
       :alt: Linear Poti Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_linear_poti_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_distance_ir_tilted_100.jpg
       :scale: 100 %
       :alt: Distance IR Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_distance_ir_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_voltage_tilted_100.jpg
       :scale: 100 %
       :alt: Voltage Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_voltage_tilted_800.jpg

Bricklets can be used to extend the features of a 
:ref:`Brick <product_overview_bricks>`. There are Bricklets to measure
physical values such as rotation, voltage, current, ambient light.
Also there are Bricklets for control purposes such as
switching relays, digital input/output and drawing on LCDs. 

Unlike Bricks, Bricklets have no fixed size. Each Bricklet has the minimum 
size it needs. Each Brick has up to four connectors for Bricklets.
You can easily connect the Bricklet with the supplied cable. The Brick than
detects the new features and new software methods are available. See 
:ref:`High Level Programming Interface <pi_hlpi>` for more information.

.. csv-table::
   :header: "Name", "Description", "C/C++", "C#", "Java", "Python"
   :widths: 20, 70, 5, 5, 5, 5

   ":ref:`ambient_light_bricklet`", "Ambient Light Sensor", ":ref:`C/C++ <ambient_light_bricklet_c>`", ":ref:`C# <ambient_light_bricklet_csharp>`", ":ref:`Java <ambient_light_bricklet_java>`", ":ref:`Python <ambient_light_bricklet_python>`"
   ":ref:`current12_bricklet`", "Bidirectional Current Sensor max. 12.5 A", ":ref:`C/C++ <current12_bricklet_c>`", ":ref:`C# <current12_bricklet_csharp>`", ":ref:`Java <current12_bricklet_java>`", ":ref:`Python <current12_bricklet_python>`"
   ":ref:`current25_bricklet`", "Bidirectional Current Sensor max. 25 A", ":ref:`C/C++ <current25_bricklet_c>`", ":ref:`C# <current25_bricklet_csharp>`", ":ref:`Java <current25_bricklet_java>`", ":ref:`Python <current25_bricklet_python>`"
   ":ref:`distance_ir_bricklet`", "Measure Distances with IR Light", ":ref:`C/C++ <distance_ir_bricklet_c>`", ":ref:`C# <distance_ir_bricklet_csharp>`", ":ref:`Java <distance_ir_bricklet_java>`", ":ref:`Python <distance_ir_bricklet_python>`"
   ":ref:`dual_relay_bricklet`", "Equipped with two relays", ":ref:`C/C++ <dual_relay_bricklet_c>`", ":ref:`C# <dual_relay_bricklet_csharp>`", ":ref:`Java <dual_relay_bricklet_java>`", ":ref:`Python <dual_relay_bricklet_python>`"
   ":ref:`humidity_bricklet`", "Humidity Sensor", ":ref:`C/C++ <humidity_bricklet_c>`", ":ref:`C# <humidity_bricklet_csharp>`", ":ref:`Java <humidity_bricklet_java>`", ":ref:`Python <humidity_bricklet_python>`"
   ":ref:`io4_bricklet`", "Input/Output 4-Channel", ":ref:`C/C++ <io4_bricklet_c>`", ":ref:`C# <io4_bricklet_csharp>`", ":ref:`Java <io4_bricklet_java>`", ":ref:`Python <io4_bricklet_python>`"
   ":ref:`io16_bricklet`", "Input/Output 16-Channel", ":ref:`C/C++ <io16_bricklet_c>`", ":ref:`C# <io16_bricklet_csharp>`", ":ref:`Java <io16_bricklet_java>`", ":ref:`Python <io16_bricklet_python>`"
   ":ref:`joystick_bricklet`", "Two directional Joystick with Button", ":ref:`C/C++ <joystick_bricklet_c>`", ":ref:`C# <joystick_bricklet_csharp>`", ":ref:`Java <joystick_bricklet_java>`", ":ref:`Python <joystick_bricklet_python>`"
   ":ref:`lcd_16x2_bricklet`", "16x2 alphanummeric chars display with backlight", ":ref:`C/C++ <lcd_16x2_bricklet_c>`", ":ref:`C# <lcd_16x2_bricklet_csharp>`", ":ref:`Java <lcd_16x2_bricklet_java>`", ":ref:`Python <lcd_16x2_bricklet_python>`"
   ":ref:`lcd_20x4_bricklet`", "20x4 alphanummeric chars display with backlight", ":ref:`C/C++ <lcd_20x4_bricklet_c>`", ":ref:`C# <lcd_20x4_bricklet_csharp>`", ":ref:`Java <lcd_20x4_bricklet_java>`", ":ref:`Python <lcd_20x4_bricklet_python>`"
   ":ref:`piezo_buzzer_bricklet`", "Buzzer for signaling", ":ref:`C/C++ <piezo_buzzer_bricklet_c>`", ":ref:`C# <piezo_buzzer_bricklet_csharp>`", ":ref:`Java <piezo_buzzer_bricklet_java>`", ":ref:`Python <piezo_buzzer_bricklet_python>`"
   ":ref:`rotary_poti_bricklet`", "Rotary Potentiometer", ":ref:`C/C++ <rotary_poti_bricklet_c>`", ":ref:`C# <rotary_poti_bricklet_csharp>`", ":ref:`Java <rotary_poti_bricklet_java>`", ":ref:`Python <rotary_poti_bricklet_python>`"
   ":ref:`linear_poti_bricklet`", "Linear Potentiometer", ":ref:`C/C++ <linear_poti_bricklet_c>`", ":ref:`C# <linear_poti_bricklet_csharp>`", ":ref:`Java <linear_poti_bricklet_java>`", ":ref:`Python <linear_poti_bricklet_python>`"
   ":ref:`temperature_bricklet`", "High Precision Thermometer", ":ref:`C/C++ <temperature_bricklet_c>`", ":ref:`C# <temperature_bricklet_csharp>`", ":ref:`Java <temperature_bricklet_java>`", ":ref:`Python <temperature_bricklet_python>`"
   ":ref:`temperature_ir_bricklet`", "Infrared Thermometer", ":ref:`C/C++ <temperature_ir_bricklet_c>`", ":ref:`C# <temperature_ir_bricklet_csharp>`", ":ref:`Java <temperature_ir_bricklet_java>`", ":ref:`Python <temperature_ir_bricklet_python>`"
   ":ref:`voltage_bricklet`", "Sensor to measure voltages", ":ref:`C/C++ <voltage_bricklet_c>`", ":ref:`C# <voltage_bricklet_csharp>`", ":ref:`Java <voltage_bricklet_java>`", ":ref:`Python <voltage_bricklet_python>`"
   

.. _product_overview_powersupplies:

Power Supplies
^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply_tilted_front_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply_tilted_front_800.jpg

A stack can be powered by the
master of the stack over its USB connection. 
This option is limited by the USB specification (500mA). 
A large stack may need more than these 500mA.

To provide greater currents Power Supply Boards are available.
These boards power the stack and can additionally be used to supply the power
for driver bricks (e.g. :ref:`DC Brick <dc_brick>`). Power Supply
Boards have the same size as :ref:`Bricks <product_overview_bricks>` and are
plugged in at the bottom of the stack.

.. csv-table::
   :header: "Name", "Description"
   :widths: 30, 60

   ":ref:`step-down`", "Powers a Stack with 6-27V input"

