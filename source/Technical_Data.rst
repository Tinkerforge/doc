Technical Data
==============

In the following you can find a brief description of all connectors.
If you need more information you can take a look in the schematics or in the 
kicad development files of each product.




Stack Connectors
----------------

Each :ref:`Brick <product_overview_bricks>` has two connector types:

 * **Stack Data Connector:** Used for data exchange between Bricks.
 * **Stack Power Connector:** Powers the Bricks and attached Bricklets, motors, servos etc.

.. _connector_stack_data:

Stack Data Connector
^^^^^^^^^^^^^^^^^^^^

.. csv-table:: 
   :header: "Comment", "Signal", "Pin", "Pin", "Signal", "Comment"
   :widths: 200, 150, 25, 25, 150, 200

   "Stack SPI: MasterIn SlaveOut", 			"SPI-MISO",		"**01**", 	"**02**", "I2C-SDA/TDI",	"Stack I2C: Serial Data/ JTAG-TDI"
   "Stack SPI: MasterOut SlaveIn", 			"SPI-MOSI",		"**03**",	"**04**", "I2C-SCL/TDO", 	"Stack I2C: Serial Clock/ JTAG-TDO"
   "Stack SPI: Clock", 					"SPI-SCLK",		"**05**",	"**06**", "SEL-0",		"Stack Select 0"
   "Reset Signal", 					"RESET",		"**07**",	"**08**", "SEL-1",		"Stack Select 1"
   "Stack Detect/ JTAG-TMS", 				"DETECT/TMS",		"**09**",	"**10**", "SEL-2",		"Stack Select 2"
   "Stack Synchronization/ JTAG-TCK", 			"SYNC/GP/TCK",		"**11**",	"**12**", "SEL-3", 		"Stack Select 3"
   "Extension SPI: MasterIn SlaveOut", 			"EX-SPI-MISO",		"**13**",	"**14**", "SEL-4",		"Stack Select 4"
   "Extension SPI: MasterOut SlaveIn", 			"EX-SPI-MOSI",		"**15**",	"**16**", "SEL-5",		"Stack Select 5"
   "Extension SPI: Clock", 				"EX-SPI-SCLK",		"**17**",	"**18**", "SEL-6",		"Stack Select 6"
   "Extension 0: General Purpose 0/ Interrupt 0", 	"EX-0-GP-0/nINT0",	"**19**",	"**20**", "SEL-7",		"Stack Select 7"
   "Extension 0: General Purpose 1/ Interrupt 1", 	"EX-0-GP-1/nINT1",	"**21**",	"**22**", "EX-SEL-0",		"Extension Select 0"
   "Extension 0: General Purpose 2/ Interrupt 2", 	"EX-0-GP-2/nINT2",	"**23**",	"**24**", "EX-SEL-1",		"Extension Select 1"
   "Extension 1: General Purpose 0", 			"EX-1-GP-0",		"**25**",	"**26**", "EX-SER-RXD",	"Extension Serial Interface: RXD"
   "Extension 1: General Purpose 1", 			"EX-1-GP-1",		"**27**",	"**28**", "EX-SER-TXD",	"Extension Serial Interface: TXD"
   "Extension 1: General Purpose 2", 			"EX-1-GP-2",		"**29**",	"**30**", "EX-SER-RTS", 	"Extension Serial Interface: RTS"

All signals are 3.3V based.

Description
"""""""""""

 * **Stack SPI** (HLPI/LLPI): SPI Bus for 
   :ref:`Brick <product_overview_bricks>` <-> 
   Master communication (:ref:`HLPI <pi_hlpi>`) 
   or interfacing Bricks via SPI (:ref:`LLPI <pi_llpi>`).
 * **JTAG**: Debug Interface, shared with other signals. JTAG must
   not be used when a Brick is stacked together with others.
 * **Reset**: Signal to reset a Brick, routed through a
   Stack such that all Bricks are reseted at the same time.
 * **Stack Detect** (HLPI): Signal to detect the presence of a 
   :ref:`Master Brick <master_brick>`.
   All Bricks except the Master Brick have the signals on top and bottom 
   internally connected and check for a high signal (input pull down) to detect
   Stack operation. Master Bricks have two independent
   signals for top and bottom side. Each Master Brick sets the top signal 
   output high and the bottom to input pull down. If a low signal is detected on
   the bottom, the Master Brick will act as a master for the Stack. If a high
   signal is detected, another Master Brick is below and will work as the
   master of the Stack.
 * **Stack Synchronization** (HLPI): This signal is used by a Master Brick to
   synchronize the actions of other Bricks in a Stack.
 * **Extension SPI** (HLPI) The SPI bus for Master <-> Master-Extensions 
   communication.
 * **Extension General Purpose 0,1** (HLPI): Three general purpose signals can
   be used by a Master Brick to control a Master-Extension. The usage depends on 
   the connected Master-Extension.
 * **Interrupt 0,1,2** (LLPI): Interrupt outputs, usage depends on 
   configuration.
 * **Stack-I2C** (HLPI/LLPI): I2C bus used by a Master to communicate with 
   Extensions (HLPI) or to interface Bricks over I2C (LLPI).
 * **Select 0-7** (HLPI): Up to eight select lines can be used by a master of a
   stack to select up to eight Bricks in the Stack. A Brick is only permitted 
   to answer messages if it is selected (Select=low). Every Brick takes the 
   first select signal of the bottom connector as its select. The other select 
   lines are shifted, such that the second select signal of the bottom is the 
   first select signal at the top, and so on. This method guarantees that the 
   next eight Bricks on the top of a master have their own select lines. If 
   more than eight Bricks would be connected to the master, only the lower 
   eight Bricks can be selected and are able to communicate with the master.
 * **Extension Select 0,1** (HLPI): Used by a master to select up to two
   Master-Extensions. These lines are shifted by Master-Extensions
   (working like select lines of Bricks). Hence the two lowermost
   Master-Extensions stacked on top of a master can be used.
 * **Extension Serial Interface** (HLPI/LLPI): Used by a master to communicate
   with Master-Extensions via a serial interface (HLPI). Since every Brick
   connects the RXD and TXD signals, a Brick can be controlled via this serial
   interface when using LLPI.


.. _connector_stack_power:

Stack Power Connector
^^^^^^^^^^^^^^^^^^^^^

.. tabularcolumns: |C|C|C|C|

.. csv-table:: 
   :header: "Func", "Pin", "Pin", "Func"
   :widths: 60, 25, 25, 60

   "PGND",		"01",		"02", "PVCC"
   "PGND",		"03",		"04", "PVCC"
   "PGND",		"05",		"06", "PVCC"
   "PGND",		"07",		"08", "PVCC"
   "PGND",		"09",		"10", "PVCC"
   "PGND",		"11",		"12", "PVCC"
   "PGND",		"13",		"14", "PVCC"
   "PGND",		"15",		"16", "PVCC"
   "PGND",		"17",		"18", "PVCC"
   "PGND",		"19",		"20", "PVCC"
   "GND",		"21",		"22", "5V"
   "GND",		"23",		"24", "5V"
   "GND",		"25",		"26", "5V"
   "GND",		"27",		"28", "3V3"
   "CURRENT",	"29",		"28", "VOLTAGE"


Description
"""""""""""

 * **PGND**: Stack power ground signal.
 * **PVCC**: Stack power signal (max. 27V), powered by 
   :ref:`Power Supply <product_overview_powersupplies>` boards.
 * **GND**: Common ground signal.
 * **5V**: 5V power supply, powered by every Brick (per USB) or Power Supply 
   Boards. Since the USB voltage depends on your PC/USB hub, the 5V
   on this rail can not be guaranteed.
 * **3V3**: Powered by every Brick. Created with on board DC/DC power supplies 
   (5V -> 3V3).
 * **Current**: Signal to measure the current flow created by Power Supply
   Boards (max. 3.3V). Can be measured by Master Bricks.
 * **Voltage**: Signal to measure the voltage of the power supply connected to
   Power Supply Boards (max. 3.3V). Can be measured by Master Bricks.


.. _connector_bricklet:

Bricklet Connector
------------------

.. csv-table:: 
   :header: "Pin", "Func", "Description"
   :widths: 25, 100, 200

   "01", "5V",			"5V signal, same as 5V in Stack"
   "02", "GND",			"Ground"
   "03", "3V3",			"3.3V generated by Brick"
   "04", "SCL",			"I2C serial clock"
   "05", "SDA",			"I2C serial data"
   "06", "ADDR",		"Address line (low/high) used to select Bricklets"
   "07", "IO_1/AD",		"Input/Output 1 with analog to digital capability"
   "08", "IO_2/DA",		"Input/Output 2 with digital to analog capability (some
   boards)"
   "09", "IO_3/PWM",	"Input/Output 3 with pulse with modulation capability"
   "10", "IO_4",		"Input/Output 4"

When not otherwise stated, all signals are 3.3V based.
