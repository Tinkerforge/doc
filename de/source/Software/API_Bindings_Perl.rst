
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

**Voraussetzungen**: Perl 5.014 or newer

Die Perl Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus einem CPAN Paket mit den Bindings für alle Tinkerforge Bricks und Bricklets
(``Tinkerforge.tar.gz``), dem Quelltext des CPAN Pakets (in ``source/``) und
allen verfügbaren Perl Beispielen (in ``examples/``).

Das CPAN Paket kann mit Hilfe des cpan Tools installiert werden::

 cpan install Tinkerforge.tar.gz

Das CPAN Paket auch auf `www.cpan.org <http://www.cpan.org/gems/tinkerforge>`__
gehostet und kann alternativ auch von dort installiert werden::

 gem install tinkerforge

Das egg kann mit Hilfe von easy_install installiert werden::

Das CPAN Paket ::

 sudo cpan install Tinkerforge

 easy_install tinkerforge.egg


Auf Windows ist easy_install möglicherweise noch nicht installiert:

* Installiere easy_install: https://pypi.python.org/pypi/setuptools#windows (setuptools)
* Öffne eine Eingabeaufforderung
* Führe ``C:\YourPythonDir\Scripts\easy_install.exe C:\PathToEgg\tinkerforge.egg`` aus

Danach können alle Beispiel unverändert verwendet werden.


Test eines Beispiels
--------------------

Wenn das egg nicht verwenden werden soll oder kann, dann kann der Quelltext
auch direkt verwendet werden. Dafür muss der ``tinkerforge`` Ordner
vom ``source/`` Ordner und das Beispiel, das ausprobiert werden soll (z.B. das
Stepper Konfigurationsbeispiel
``examples/brick/stepper/example_configuration.py``), in einen Ordner kopiert
werden::

 example_folder/
  -> tinkerforge/
  -> example_configuration.py

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopiert werden. Das Stepper Brick
Beispiel benötigt ``ip_connection.py`` und ``brick_stepper.py``::

 example_folder/
  -> ip_connection.py
  -> brick_stepper.py
  -> example_configuration.py

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``tinkerforge``
Package aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: python

 from tinkerforge.ip_connection import IPConnection
 from tinkerforge.brick_stepper import Stepper

muss dort nun dies stehen:

.. code-block:: python

 from ip_connection import IPConnection
 from brick_stepper import Stepper

Jetzt kann das Beispiel wieder ausgeführt werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_Perl_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
