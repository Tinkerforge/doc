.. _product_overview:

Product Overview
----------------

There are four different types of hardware components:

* :ref:`Bricks <product_overview_bricks>`: 
  Stackable microcontroller boards for sensing and controlling.
* :ref:`Master Extensions <product_overview_master_extensions>`:
  Boards which extend the communication interfaces of a
  :ref:`Master Brick <master_brick>`.
* :ref:`Bricklets <product_overview_bricklets>`:
  Non-stackable sensor/actor boards which extend the features of a 
  :ref:`Brick <product_overview_bricks>`.
* :ref:`Power Supplies <product_overview_powersupplies>`:
  Boards to power a Stack of 
  :ref:`Bricks <product_overview_bricks>`, plugged below the Stack.


See the :ref:`tutorial <tutorial>` for an explanation of how everything works
together.


.. _product_overview_bricks:

Bricks
^^^^^^

.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 40 %
   :alt: Servo Brick

Bricks are 4 x 4cm (1.57" x 1.57") boards equipped with a 32bit
microcontroller, an USB port, two status LEDs, connectors for 
stacking and up to four connectors for 
:ref:`Bricklets <product_overview_bricklets>`. 
There are Bricks which perform complex 
sensor tasks (e.g. :ref:`IMU Brick <imu_brick>`), 
communicate (e.g. :ref:`Master Brick <master_brick>`) 
and drive motors (e.g. :ref:`DC Brick <dc_brick>`).

Bricks can be plugged together to a Stack.
A :ref:`Master Brick <master_brick>`
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
   :header: "Name", "Description", "Datasheet", "C/C++", "Python"
   :widths: 15, 40, 5, 5, 5

   "DC Brick", "3A DC Motor Driver", ":ref:`Datasheet <dc_brick>`", ":ref:`C/C++ <dc_brick_c>`", ":ref:`Python <dc_brick_python>`"
   "IMU Brick", "IMU with 9 degrees of freedom", ":ref:`Datasheet <imu_brick>`", ":ref:`C/C++ <imu_brick_c>`", ":ref:`Python <imu_brick_python>`"
   "Master Brick", "Allow building of Stacks, 4 Bricklet Ports", ":ref:`Datasheet <master_brick>`", ":ref:`C/C++ <master_brick_c>`", ":ref:`Python <master_brick_python>`"
   "Servo Brick", "Control up to 7 Servos", ":ref:`Datasheet <servo_brick>`", ":ref:`C/C++ <servo_brick_c>`", ":ref:`Python <servo_brick_python>`"
   "Stepper Brick", "2.5A Stepper Motor Driver", ":ref:`Datasheet <stepper_brick>`", ":ref:`C/C++ <stepper_brick_c>`", ":ref:`Python <stepper_brick_python>`"


.. _product_overview_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Chibi Extension

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
   :header: "Name", "Description", "Datasheet", "C/C++", "Python"
   :widths: 20, 70, 5, 5, 5

   "Chibi Extension", "Wireless Chibi Master Extension", ":ref:`Datasheet <chibi_extension>`", "", ""
   "LCD Extension", "Graphic LCD for ontop Stack usage", ":ref:`Datasheet <lcd_extension>`", "", ""
   "RS485 Extension", "Cable based RS485 Master Extension", ":ref:`Datasheet <rs485_extension>`", "", ""


.. _product_overview_bricklets:

Bricklets
^^^^^^^^^
.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Chibi Extension

Bricklets can be used to extend the features of a 
:ref:`Brick <product_overview_bricks>`. There are Bricklets to measure
physical values such as rotation, voltage, current, ambient light.
Also there are Bricklets for control purposes such as
switching relays, digital input/output and drawing on LCDs. 

Unlike :ref:`Bricks <product_overview_bricks>`,
Bricklets have no fixed size. Each Bricklet has the minimum size it needs.
Each :ref:`Brick <product_overview_bricks>` has up to four connectors for 
Bricklets.
You can easily connect the Bricklet with the supplied cable. The Brick than
detects the new features and new software methods are available. See 
:ref:`High Level Programming Interface <pi_hlpi>` for more information.

.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Brick and Bricklet


.. csv-table::
   :header: "Name", "Description", "Datasheet", "C/C++", "Python"
   :widths: 20, 70, 5, 5, 5

   "Ambient Light", "Ambient Light Sensor", ":ref:`Datasheet <ambient_light_bricklet>`", ":ref:`C/C++ <ambient_light_bricklet_c>`", ":ref:`Python <ambient_light_bricklet_python>`"
   "Current12", "Bidirectional Current Sensor max. 12.5 A", ":ref:`Datasheet <current12_bricklet>`", ":ref:`C/C++ <current12_bricklet_c>`", ":ref:`Python <current12_bricklet_python>`"
   "Current25", "Bidirectional Current Sensor max. 25 A", ":ref:`Datasheet <current25_bricklet>`", ":ref:`C/C++ <current25_bricklet_c>`", ":ref:`Python <current25_bricklet_python>`"
   "Distance IR", "Measure Distances with IR Light", ":ref:`Datasheet <distance_ir_bricklet>`", ":ref:`C/C++ <distance_ir_bricklet_c>`", ":ref:`Python <distance_ir_bricklet_python>`"
   "Dual Relay", "Equipped with two relays", ":ref:`Datasheet <dual_relay_bricklet>`", ":ref:`C/C++ <dual_relay_bricklet_c>`", ":ref:`Python <dual_relay_bricklet_python>`"
   "Humidity", "Humidity Sensor", ":ref:`Datasheet <humidity_bricklet>`", ":ref:`C/C++ <humidity_bricklet_c>`", ":ref:`Python <humidity_bricklet_python>`"
   "IO4", "Input/Output 4-Channel", ":ref:`Datasheet <io4_bricklet>`", ":ref:`C/C++ <io4_bricklet_c>`", ":ref:`Python <io4_bricklet_python>`"
   "IO16", "Input/Output 16-Channel", ":ref:`Datasheet <io16_bricklet>`", ":ref:`C/C++ <io16_bricklet_c>`", ":ref:`Python <io16_bricklet_python>`"
   "Joystick", "Two directional Joystick with Button", ":ref:`Datasheet <joystick_bricklet>`", ":ref:`C/C++ <joystick_bricklet_c>`", ":ref:`Python <joystick_bricklet_python>`"
   "LCD 16x2", "16x2 alphanummeric chars display with backlight", ":ref:`Datasheet <lcd_16x2_bricklet>`", ":ref:`C/C++ <lcd_16x2_bricklet_c>`", ":ref:`Python <lcd_16x2_bricklet_python>`"
   "LCD 20x4", "20x4 alphanummeric chars display with backlight", ":ref:`Datasheet <lcd_20x4_bricklet>`", ":ref:`C/C++ <lcd_20x4_bricklet_c>`", ":ref:`Python <lcd_20x4_bricklet_python>`"
   "Piezo Buzzer", "Buzzer for signaling", ":ref:`Datasheet <piezo_buzzer_bricklet>`", ":ref:`C/C++ <piezo_buzzer_bricklet_c>`", ":ref:`Python <piezo_buzzer_bricklet_python>`"
   "Rotary Poti", "Rotary Potentiometer", ":ref:`Datasheet <rotary_poti_bricklet>`", ":ref:`C/C++ <rotary_poti_bricklet_c>`", ":ref:`Python <rotary_poti_bricklet_python>`"
   "Linear Poti", "Linear Potentiometer", ":ref:`Datasheet <linear_poti_bricklet>`", ":ref:`C/C++ <linear_poti_bricklet_c>`", ":ref:`Python <linear_poti_bricklet_python>`"
   "Temperature", "High Precision Thermometer", ":ref:`Datasheet <temperature_bricklet>`", ":ref:`C/C++ <temperature_bricklet_c>`", ":ref:`Python <temperature_bricklet_python>`"
   "Temperature IR", "Infrared Thermometer", ":ref:`Datasheet <temperature_ir_bricklet>`", ":ref:`C/C++ <temperature_ir_bricklet_c>`", ":ref:`Python <temperature_ir_bricklet_python>`"
   "Voltage", "Sensor to measure voltages", ":ref:`Datasheet <voltage_bricklet>`", ":ref:`C/C++ <voltage_bricklet_c>`", ":ref:`Python <voltage_bricklet_python>`"
   

.. _product_overview_powersupplies:

Power Supplies
^^^^^^^^^^^^^^
.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Step Down Power Supply

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
   :header: "Name", "Description", "Datasheet", "C/C++", "Python"
   :widths: 20, 70, 5, 5, 5

   "Step-Down", "Powers a Stack with 6-27V input", ":ref:`Datasheet <step-down>`", "", ""

