.. _api_bindings_python:

Python - API Bindings
=====================

**Voraussetzungen**: Python 2.5 oder neuer, Python 3 wird auch unterstützt

Die Python Bindings bestehen aus einem Python egg mit den Bindings für alle
Tinkerforge Bricks und Bricklets (``tinkerforge.egg``), dem Quelltext des eggs
(in ``source/``) und allen verfügbaren Python Beispielen (in ``examples/``).

Das egg kann mit Hilfe von easy_install installiert werden::

 easy_install tinkerforge.egg

Danach können alle Beispiel unverändert verwendet werden.

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

.. note::
 Windows Installationshinweis:

 * Installiere easy_install: http://pypi.python.org/pypi/setuptools#windows (setuptools)
 * Öffne eine Eingabeaufforderung
 * Führe ``C:\\YourPythonDir\\Scripts\\easy_install.exe C:\\PathToEgg\\tinkerforge.egg`` aus
