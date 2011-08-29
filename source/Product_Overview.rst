Product Overview
----------------

There exist four types of hardware components:
 * :ref:`Bricks <product_overview_bricks>`: 
   Stackable microcontroller boards for sensing and controlling purposes.
 * :ref:`Master-Extensions <product_overview_master_extensions>`:
   Boards which extend the communication interfaces of a
   :ref:`Master-Brick <master_brick>`.
 * :ref:`Bricklets <product_overview_bricklets>`:
   Non-stackable sensor/actor boards which extend the features of a 
   :ref:`Brick <product_overview_bricks>`.
 * :ref:`Power-Supplys <product_overview_powersupplies>`:
   Boards to power a Stack of 
   :ref:`Bricks <product_overview_bricks>` plugged below the Stack.


.. _product_overview_bricks:

Bricks
^^^^^^

.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 40 %
   :alt: Servo Brick

Bricks are 4 x 4cm (1.57" x 1.57") boards equipped with a 32bit
microcontroller, an USB port, two status LEDs, connectors for 
stacking and up to four connectors for :ref:`Bricklets <product_overview_bricklets>`. 
There are Bricks which perform complex 
sensor tasks (e.g. :ref:`IMU-Brick <imu_brick>`), 
communicate (e.g. :ref:`Master-Brick <master_brick>`) 
and driving motors (e.g. :ref:`DC-Brick <dc_brick>`).

Bricks can be plugged together to a Stack.
A :ref:`Master-Brick <master_brick>`
at the bottom of this Stack can control all boards within the Stack. 
This master routes the messages between the boards in the Stack and the PC 
(:ref:`High Level Programming Interface <concepts_hlpi>`).
For the user it behaves as all Bricks are connected seperately over USB with
the PC. The interface between PC and the Master-Brick can be the USB 
connection of the master. This connection can be changed by the usage of 
:ref:`Master-Extensions <product_overview_master_extensions>`. There are
Master-Extensions for cable-based or wireless interfaces.
The boards of a Stack can be powered by the master of the Stack but this is
limited. Large Stacks might draw to much power. Therefore special
:ref:`Power-Supplys <product_overview_powersupplies>` exist. These boards
will connected below the Stack and power it.
See TODO Tutorial Stacking for more information
about Stacks.

Besides the :ref:`High Level Programming Interface <concepts_hlpi>` it is also
possible to use Bricks with our 
:ref:`Low Level Programming Interface <concepts_llpi>`
or :ref:`On Device Programming Interface <concepts_hlpi>` concept.


.. raw:: html

	<table cellspacing="0" cellpadding="0" border="0">
        <tbody>
                <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Datasheet</th>
                        <th colspan="5" scope="col" align="center">API</th>
                </tr>
                <tr>
                        <th scope="col"></th>
                        <th scope="col"></th>
                        <th scope="col"></th>
                        <th scope="col"><img src="doc/build/html/_images/icon_python.png"></th>
                        <th scope="col">C++</th>
                        <th scope="col">C#</th>
                        <th scope="col">Java</th>
                        <th scope="col">Python</th>
                </tr>
                <tr>
                        <th scope="row">DC Brick</th>
                        <td>3A DC Motor Driver</td>
                        <td><a href="doc/Hardware/Bricks/DC_Brick.html">Datasheet</a></td>
                        <td>C</td>
                        <td>C++</td>
                        <td>C#</td>
                        <td>Java</td>
                        <td>Python</td>
                </tr>
                <tr>
                        <th scope="row">IMU Brick</th>
                        <td>IMU with 3D Accelerometer and Gyroscope</td>
                        <td>Datasheet</td>
                        <td>C</td>
                        <td>C++</td>
                        <td>C#</td>
                        <td>Java</td>
                        <td>Python</td>
                </tr>
                <tr>
                        <th scope="row">Master Brick</th>
                        <td>Allow building of Stacks, 4 Bricklet Ports</td>
                        <td>Datasheet</td>
                        <td>C</td>
                        <td>C++</td>
                        <td>C#</td>
                        <td>Java</td>
                        <td>Python</td>
                </tr>
                <tr>
                        <th scope="row">Servo Brick</th>
                        <td>Control up to 7 RC Servos</td>
                        <td>Datasheet</td>
                        <td>C</td>
                        <td>C++</td>
                        <td>C#</td>
                        <td>Java</td>
                        <td>Python</td>
		</tr>
	</tbody>
	</table>


.. _product_overview_master_extensions:

Master-Extensions
^^^^^^^^^^^^^^^^^

.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Chibi-Extension

When using our :ref:`High Level Programming Interface <concepts_hlpi>` concept
:ref:`Master-Bricks <master_brick>` can route messages between 
:ref:`Bricks <product_overview_bricks>` and the PC. To establish a connection 
between an PC and the Master-Brick typically the USB port is used.
Master-Extensions can be utilized to change the interface of a Master-Brick.
There are cable based or wireless Master-Extensions available. The usage of the
different interfaces is transparent for the user. 
It behaves such as every board of the 
Stack is directly connected to the 
PC with its USB connection. This means:

The user can develop his application with all
boards independently connected to the PC over USB. Later he can plug these 
boards together to Stacks, add Master-Bricks and cable based or wireless
Extensions and can run his previous written code without any changes.


.. _product_overview_bricklets:

Bricklets
^^^^^^^^^
.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Chibi-Extension

Bricklets can be used to extend the features of a 
:ref:`Brick <product_overview_bricks>`. There are Bricklets to measure rotation,
voltage, current, ambient light and other physical values. 
Also there are Bricklets for control purposes like
switching relays, digital Input and Output and drawing on LCDs. 

Unlike :ref:`Bricks <product_overview_bricks>`
Bricklets have no fixed size. Each Bricklet has the size it needs.
Each :ref:`Brick <product_overview_bricks>` has up to four connectors for Bricklets.
You can easily connect the Bricklet with the supplied cable. The Brick than
detects the new features and new software methods are available. See 
:ref:`High Level Programming Interface <concepts_hlpi>` for more information.

.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Brick and Bricklet

Boards
""""""
:ref:`Ambient Light <ambient_light_bricklet>`, 
:ref:`Breakout <breakout_bricklet>`, 
:ref:`Current-12 <current-12_bricklet>`, 
:ref:`Current-25 <current-25_bricklet>`, 
:ref:`Distance-IR <distance-ir_bricklet>`, 
:ref:`Dual-Relay <dual-relay_bricklet>`, 
:ref:`Humidity <humidity_bricklet>`, 
:ref:`Incremental-Encoder <incremental-encoder_bricklet>`, 
:ref:`IO-4 <io-4_bricklet>`, 
:ref:`IO-16 <io-16_bricklet>`, 
:ref:`Joystick <joystick_bricklet>`, 
:ref:`LCD-16x2 <lcd16x2_bricklet>`, 
:ref:`LCD-20x4 <lcd20x4_bricklet>`, 
:ref:`Line-Sensor <line_bricklet>`, 
:ref:`Piezo-Buzzer <piezo-buzzer_bricklet>`, 
:ref:`Rotary-Poti <rotary-Poti_bricklet>`, 
:ref:`Linear-Poti <linear-poti_bricklet>`, 
:ref:`Temperature <temperature_bricklet>`, 
:ref:`Temperature-IR <temperature-ir_bricklet>`,
:ref:`Voltage <voltage_bricklet>`


.. _product_overview_powersupplies:

Power-Supply
^^^^^^^^^^^^
.. image:: /Images/Bricks/Servo_Brick/servo_brick2.jpg
   :scale: 100 %
   :alt: Step-Down Powersupply

A stack can be powered by the
master of the stack over its USB connection (if connected). 
This option is of course limited by the USB specification (500mA). 
A large stack may need more than these 500mA.

To provide greater currents Power-Supply boards are available.
These boards power the stack and can additionally be used to supply the power
for driver bricks (e.g. :ref:`DC-Brick <dc_brick>`). These Power-Supply
boards have the same size as :ref:`Bricks <product_overview_bricks>` and are
mounted at the bottom of the stack.

