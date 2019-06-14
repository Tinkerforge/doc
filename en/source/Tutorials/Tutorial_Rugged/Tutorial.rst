
.. _tutorial_rugged_approach:

Tutorial - Rugged Approach
==========================

With the new Protocol 2.0, it is possible to write programs that are
resilient to outages, brief electricity cuts and similar things.

The general approach for such a program is shown below in pseudo code::

 func enumerate_callback(...) {
     configure_brick();
     configure_bricklet();
 }

 func connected_callback(...) {
     ipcon.enumerate();
 }

 func main() {
     ipcon.enumerate();

     while (true) {
         if (brick_is_configured) {
             do_something_with_brick();
         }

         if (bricklet_is_configured) {
             do_something_with_bricklet();
         }
     }
 }

Generally, you have to make sure that the configuration is done while
the Bricks and Bricklets are enumerated. This ensures that the configuration
(e.g. callback periods) is always there, even if a Brick or Bricklet
was restarted and lost its configuration.

To do this, you can put the configuration code in the enumeration callback.
You should also make sure, that a new enumeration is triggered if the
TCP/IP connection was lost and then reconnected. If the connection was lost,
a Brick or Bricklet might have been restarted in the meantime, so it
needs to be reconfigured.

In the following you can find C# and Python source code for a program that displays the
temperature on a LCD 20x4 Bricklet. This program should keep working if
you reconnect/restart the Master Brick or if a Wi-Fi connection is lost.
It is even possible to exchange the Temperature or LCD 20x4 Bricklet, since
the program uses the UID from the enumeration.

C#
--

`Download (ExampleRugged.cs) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_Rugged/ExampleRugged.cs>`__

.. literalinclude:: ExampleRugged.cs
 :language: csharp
 :linenos:
 :tab-width: 4

Python
------

`Download (example_rugged.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_Rugged/example_rugged.py>`__

.. literalinclude:: example_rugged.py
 :language: python
 :linenos:
 :tab-width: 4
