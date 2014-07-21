
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-python">Software</a> / Python - API Bindings

.. _api_bindings_python:

Python - API Bindings
=====================

**Voraussetzungen**: Python 2.5 oder neuer, Python 3 wird auch unterstützt

Die Python Bindings (:ref:`download <downloads_bindings_examples>`) bestehen
aus dem Python Quelltext der Bindings für alle Tinkerforge Bricks und Bricklets
(in ``source/``) und allen verfügbaren Python Beispielen (in ``examples/``).

Die Bindings können mit Hilfe der `setuptools
<https://pypi.python.org/pypi/setuptools>`__ installiert werden, dazu folgenden
Befehl im ``source/`` Ordner ausführen::

 python setup.py install

Die Bindings stehen auch im Python Package Index `PyPI
<https://pypi.python.org>`__ bereit. Von dort können sie mit dem Python Package
Installer `pip <https://pip.pypa.io>`__ und folgendem Befehl installiert werden::

 pip install tinkerforge

Danach können alle Beispiel unverändert verwendet werden.


.. _api_bindings_python_install:

Installation
------------

TODO


Test eines Beispiels
--------------------

Wenn die Bindings nicht installiert werden sollen oder können, dann kann der
Quelltext auch direkt verwendet werden. Dafür muss der ``tinkerforge/`` Ordner
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
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Python_links.table
