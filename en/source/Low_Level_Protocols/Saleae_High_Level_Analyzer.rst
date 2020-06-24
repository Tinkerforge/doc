
.. _saleae_high_level_analyzer:

Saleae Logic High Level Analyzer
================================

The Tinkerforge Saleae Logic High Level Analyzer is an extension
for `Saleae Logic 2 <https://www.saleae.com/downloads/>`__.
It makes analysis of the communication with Co-MCU Bricklets using one
of the Saleae Logic Analyzers a lot easier.

The analyzer can decode captured SPI communication into SPITFP and
TFP packets. It contains a database of all functions of Bricks and Bricklets.

The analyzer can assist in debugging bugs when developing new Bricklets
using the :ref:`XMC1400 Breakout Bricklet <xmc1400_breakout_bricklet>`.

..
 or when building new hardware abstraction layers for the low level C bindings.

.. image:: /Images/Screenshots/saleae_hla.png
   :scale: 100 %
   :alt: Saleae High Level Analyzer
   :align: center
   :target: ../_images/Screenshots/saleae_hla.png

Hardware
--------

To be able to capture the SPI communication, you need to build yourself an
adapter to tap into the electric signals. You can, for example, use two
:ref:`Breakout Bricklets <breakout_bricklet>` and a pin header to connect them.

If you are using the :ref:`XMC1400 Breakout Bricklet <xmc1400_breakout_bricklet>`
you can capture the SPI communication from the pins marked with CS, CLK, MOSI and MISO.

Installation
------------

The analyzer requires an up-to-date version of the Saleae Logic 2 alpha, at least 2.3.0.

In Logic 2 you can add the analyzer as an extension from the marketplace.
It should then be possible to add the SPITFP analyzer.

Configuration
-------------

The following options can be configured for the analyzer:

* Input Analyzer: This is the underlying protocol. This should always be SPI.
* Output Format: Packets with large payloads can create a lot of graph overlay text. If necessary, you can limit the output to only the headers or the (TFP) payload here.
* Direction: Selects the SPI signal to analyze. Use MOSI to analyze messages sent to the Bricklet, or MISO to analyze messages created by the Bricklet.
* Device: You can select the attached device. This is required to allow the analyzer to parse the function IDs and payload.

It is possible to add multiple instances of the analyzer.
This allows parsing both directions of communication (i.e. from/to the Bricklet)
at the same time. This can also be used to get a multi-line output when analyzing large
packages: Add one instance with Headers output format and one with the Payload output format
to see the parsed packets as shown in the screenshot above.
