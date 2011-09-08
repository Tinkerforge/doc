Tutorial
========

Simply use your Brick
---------------------



Add Bricklets to extend features
--------------------------------

If you like to replace a Bricklet by another, do the following:

1. Remove old Bricklet
2. Press "reset" at Brick:

   *After this the Brick's Bricklet port is configured default as input.*
3. Connect new Bricklet
4. Press "reset" at Brick again:

   *After this the Bricklet code is loaded and Brick's Bricklet port is 
   configured according to new connected Bricklet.*

.. warning::

   A wrong handling of Bricklets can destroy your hardware!

   If you replace a Bricklet without removing power of the Brick or bringing 
   the Brick's Bricklet port in an input state 
   (e.g. by removing the old Bricklet and afterwards resetting the Brick)
   you can connect two hardware modules both active driving a signal.
   This can lead to a shortcut and destroyed hardware.

Building Stacks
---------------

* 2x Bricks -> Master + 2x Bricks (Stack)

Cross-Link Stacks
-----------------

* 2x Stacks (USB) -> Chibi

