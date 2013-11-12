
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#specifications">Specifications</a> / Wireshark Dissector

.. _wireshark_dissector:

Wireshark Dissector
===================

`Wireshark <http://www.wireshark.org>`__ is a free and open-source packet 
analyzer. It is used for network troubleshooting, analysis, software and 
communications protocol development, and education.

A Wireshark dissector is a plugin for a specific protocol. With the
TFP (Tinkerforge Protocol) dissector it is possible to analyze the
protocol that is used between :ref:`Bindings <api_bindings>` and 
:ref:`Brick Daemon <brickd>` (TCP/IP) as well as the protocol that is used 
between Brick Daemon and :ref:`Bricks <product_overview_bricks>` (USB).

The dissector can assist in debugging bugs in the bindings and brickd. It
is also very helpful while creating new Bindings.

.. image:: /Images/Screenshots/wireshark_dissector.jpg
   :scale: 100 %
   :alt: Wireshark Dissector
   :align: center
   :target: ../_images/Screenshots/wireshark_dissector.jpg

Installation
------------

The TFP dissector is in the Wireshark SVN trunk since
`November 2013 <https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9324>`__. 
It is not yet available in the latest stable release. The following steps 
are necessary to build Wireshark trunk from source::

 svn co http://anonsvn.wireshark.org/wireshark/trunk/ wireshark
 cd wireshark/
 ./autogen.sh
 ./configure
 make

You can now start Wireshark directly with::

 ./wireshark

Or you can install it with::

 make install

Wireshark has lots of dependencies, the configure script will tell you which
ones are missing. On Debian based system you can install all necessary
dependencies via::

 apt-get build-dep wireshark

The dissector itself is also 
`available on GitHub <https://github.com/Tinkerforge/tf-wireshark-dissector>`__.

Display Filter
--------------

Display filter for all of the fields in the TFP packet are available.

Useful examples:

Only show TFP packets::

 tfp

Only show packets that are from or to UID "XYZ"::

 tfp.uid == "XYZ"

Only show packets with an error::

 tfp.e != 0

Only show specific function calls (in this case function ID 4)::

 tfp.fid == 4
