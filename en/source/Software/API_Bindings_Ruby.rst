
.. _api_bindings_ruby:

Ruby - API Bindings
===================

The Ruby bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Ruby programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``tinkerforge.gem``, a Ruby GEM (installable with `gem
  <https://rubygems.org/pages/download>`__ tool)
* in ``source/`` the source code of ``tinkerforge.gem``
* in ``examples/`` the examples for every Brick and Bricklet


Requirements
------------

* Ruby 1.9 or newer


.. _api_bindings_ruby_install:

Installation
------------

There are two ways to install the Ruby bindings:
from our :ref:`APT repository <api_bindings_ruby_install_apt>` for Debian
based Linux distributions or
from :ref:`GEM <api_bindings_ruby_install_gem>`.
But the bindings can also be used
:ref:`without installing <api_bindings_ruby_install_without>` them first.

.. _api_bindings_ruby_install_apt:

From APT Repository
^^^^^^^^^^^^^^^^^^^

The bindings are available in our APT repository for Debian based Linux
distributions (in this case you don't even need the ZIP file for the bindings).
Follow the :ref:`setup guide <apt_repository_setup>` then install the bindings::

 sudo apt install ruby-tinkerforge

Now you're ready to test an example. The Debian package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

.. _api_bindings_ruby_install_gem:

From GEM
^^^^^^^^

The bindings are available as a GEM on `rubygems.org
<https://rubygems.org/gems/tinkerforge>`__. You can install them with the
`gem <https://rubygems.org/pages/download>`__ tool using the following
command (in this case you don't even need the ZIP file for the bindings).
Depending on your Ruby installation you might have to execute this with
``sudo`` or as administrator::

 gem install tinkerforge

Alternatively, the GEM is also part of the ZIP file of the bindings. It
can be installed from there as well with the following command which might has
to execute with ``sudo`` or as administrator::

 gem install tinkerforge.gem

Now you're ready to test an example. The GEM does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

.. _api_bindings_ruby_install_without:

Without Installation
^^^^^^^^^^^^^^^^^^^^

You can use the bindings without having to install them. Just copy the
``tinkerforge/`` folder from the ``source/`` folder in the same folder as your
Ruby program. The section about testing an example has more details about this.


Testing an Example
------------------

To test a Ruby example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``example_configuration.rb`` file from the
``examples/brick/stepper/`` folder into a new folder::

 example_project/
  -> example_configuration.rb

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: ruby

  HOST = 'localhost'
  PORT = 4223
  UID = 'XXYYZZ' # Change XXYYZZ to the UID of your Stepper Brick

If you did install the bindings then you're now ready to test this example::

 ruby example_configuration.rb

If you did **not** install the bindings then you can also use the source of the
bindings directly. Just copy the ``tinkerforge/`` folder from the ``source/``
folder to your ``example_project/`` folder::

 example_project/
  -> tinkerforge/
  -> example_configuration.rb

Now you're ready to test this example. You need to tell Ruby to look in the
current folder for required modules using the ``-I.`` option::

 ruby -I. example_configuration.rb


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_Ruby_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Ruby>
   Bricks <Bricks_Ruby>
   Bricks (Discontinued) <Bricks_Ruby_Discontinued>
   Bricklets <Bricklets_Ruby>
   Bricklets (Discontinued) <Bricklets_Ruby_Discontinued>
