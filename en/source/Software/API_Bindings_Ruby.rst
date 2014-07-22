
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-ruby">Software</a> / Ruby - API Bindings

.. _api_bindings_ruby:

Ruby - API Bindings
===================

**Requirements**: Ruby 1.9 or newer

The Ruby bindings (:ref:`download <downloads_bindings_examples>`) consist of
a Ruby GEM with the bindings for all
Tinkerforge Bricks and Bricklets (``tinkerforge.gem``), the source of the
GEM (in ``source/``) and all available Ruby examples (in ``examples/``).

You can install the GEM with the gem tool::

 gem install tinkerforge.gem

The GEM is also hosted on `rubygems.org <https://rubygems.org/gems/tinkerforge>`__.
So you can alternatively install it from there::

 gem install tinkerforge

After that you can use the examples as they are.


.. _api_bindings_ruby_install:

Installation
------------

TODO


Testing an Example
------------------

To test a Ruby example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.




If you can't or don't want to use the GEM, you can also use the source
directly, just create a folder for your project and copy the ``tinkerforge``
folder from ``source/`` and the example you want to try in there
(e.g. the Stepper configuration example from
``examples/brick/stepper/example_configuration.rb``)::

 example_project/
  -> tinkerforge/
  -> example_configuration.rb

You need to tell Ruby to look in the current folder for required modules::

 ruby -I. example_configuration.rb

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need ``ip_connection.rb`` and
``stepper_brick.rb``. After copying these in the project folder::

 example_project/
  -> ip_connection.rb
  -> brick_stepper.rb
  -> example_configuration.rb

we have to remove the ``tinkerforge`` package from the examples, i.e. instead of:

.. code-block:: ruby

 require 'tinkerforge/ip_connection'
 require 'tinkerforge/brick_stepper'

we use:

.. code-block:: ruby

 require 'ip_connection'
 require 'brick_stepper'

After that, the example can be executed again.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Ruby_links.table
