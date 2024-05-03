
.. _api_bindings_python:

Python - API Bindings
=====================

Die Python Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Python Skripten
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``source/`` den Quelltext der Bindings (inklusive ``setup.py``
  Installations Skript)
* in ``examples/`` die Beispiele für alle Bricks und Bricklets


Voraussetzungen
---------------

* Python 2.6 oder neuer, Python 3 wird auch unterstützt

.. _api_bindings_python_install:

Installation
------------

Die Python Bindings können auf drei Weisen installiert werden:
von unserem :ref:`APT Repository <api_bindings_python_install_apt>` für Debian
basierte Linux Distributionen oder von
:ref:`PyPI <api_bindings_python_install_pypi>` oder vom
:ref:`Quelltext <api_bindings_python_install_source>`. Die Bindings können aber auch
:ref:`ohne Installation <api_bindings_python_install_without>` genutzt werden.

.. _api_bindings_python_install_apt:

Vom APT Repository
^^^^^^^^^^^^^^^^^^

Die Bindings stehen in unserem APT Repository für Debian basierte Linux
Distributionen bereit (dazu wird die ZIP Datei der Bindings nicht benötigt).
Zuerst das :ref:`APT Repository einrichten <apt_repository_setup>` dann
die Bindings installieren:

* Für Python 3::

   sudo apt install python3-tinkerforge

* Für Python 2::

   sudo apt install python-tinkerforge

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das Debian
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.


.. _api_bindings_python_install_pypi:

Von PyPI
^^^^^^^^

Die Bindings stehen im Python Package Index `PyPI
<https://pypi.python.org/pypi/tinkerforge>`__ bereit. Von dort können sie mit
dem Python Package Installer `pip <https://pip.pypa.io>`__ und folgendem Befehl
installiert werden (dazu wird die ZIP Datei der Bindings nicht benötigt).
Abhängig von der Art der Python Installation muss dies möglicherweise mit
``sudo`` bzw. als Administrator ausgeführt werden::

 pip install tinkerforge

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das PyPI
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.


.. _api_bindings_python_install_source:

Vom Quelltext
^^^^^^^^^^^^^

Der ``source/`` Ordner beinhaltet ein ``setup.py`` Installations Skript,
welches die `setuptools <https://pypi.python.org/pypi/setuptools>`__ für Python
benötigt. Um die Bindings zu installieren muss nur dieses Skript im
``source/`` Ordner ausgeführt werden. Abhängig von der Art der Python
Installation muss dies möglicherweise mit ``sudo`` bzw. als Administrator
ausgeführt werden::

 python setup.py install

Aktuell funktioniert diese Installationsmethode noch. Sie ist allerdings als
deprecated markiert. Stattdessen kann auch `pip <https://pip.pypa.io>`__
verwendet werden::

 pip install .

Dann ist auch schon alles bereit, um Beispiele testen zu können.


.. _api_bindings_python_install_without:

Ohne Installation
^^^^^^^^^^^^^^^^^

Die Python Bindings müssen nicht unbedingt installiert werden. Stattdessen
kann auch einfach der ``tinkerforge/`` Ordner vom ``source/`` Ordner in den
gleichen Ordner wie dein Python Skript kopiert werden und Python wird die
Bindings automatisch finden. Der Abschnitt über den Test eines Beispiels
vermittelt mehr Details darüber.


Test eines Beispiels
--------------------

Um ein Python Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``example_configuration.py`` Datei aus dem
``examples/brick/stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> example_configuration.py

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: python

  HOST = "localhost"
  PORT = 4223
  UID = "XXYYZZ" # Change XXYYZZ to the UID of your Stepper Brick

Wenn die Bindings installiert wurden, dann kann das Beispiel jetzt direkt
ausgeführt werden::

 python example_configuration.py

Wenn die Bindings **nicht** installiert wurden, dann kann der Quelltext der
Bindings auch direkt verwendet werden. Dafür muss der ``tinkerforge/`` Ordner
vom ``source/`` Ordner in den ``example_project/`` Ordner kopiert werden und
Python wird die Bindings automatisch finden::

 example_project/
  -> tinkerforge/
  -> example_configuration.py

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können::

 python example_configuration.py


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Python_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Python>
   Bricks <Bricks_Python>
   Bricks (Abgekündigt) <Bricks_Python_Discontinued>
   Bricklets <Bricklets_Python>
   Bricklets (Abgekündigt) <Bricklets_Python_Discontinued>
