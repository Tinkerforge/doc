
.. _api_bindings_mathematica:

Mathematica - API Bindings
==========================

Die Mathematica Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Mathematica Notebooks
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``Tinkerforge.dll``, eine vorkompilierte .NET Bibliothek
* in ``source/`` den Quelltext für ``Tinkerforge.dll``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Mathematica Bindings basieren auf den :ref:`C# Bindings <api_bindings_csharp>`.
Seit Version 2.0.0 sind die C# Bindings `CLS
<https://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `.NET kompatiblen Sprachen
<https://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. Mathematicas `.NET/Link Unterstützung
<https://reference.wolfram.com/language/NETLink/tutorial/CallingNETFromTheWolframLanguage.html>`__.
Diese benötigt das `.NET Framework <https://www.microsoft.com/net>`__ unter
Windows und das `Mono Framework <https://www.mono-project.com/>`__ unter
Linux und macOS.


Voraussetzungen
---------------

* Mathematica 5.0 oder neuer auf Windows, Linux und macOS mit .NET/Link
  Unterstützung


.. _api_bindings_mathematica_install:

Installation
------------

Die Installation der Mathematica Bindings ist optional. Sie können als
Mathematica :ref:`AddOn <api_bindings_mathematica_install_addon>` oder als
Mathematica :ref:`SystemFile <api_bindings_mathematica_install_systemfile>`
installiert werden, sie können aber auch :ref:`ohne Installation
<api_bindings_mathematica_install_without>` genutzt werden.


.. _api_bindings_mathematica_install_addon:

Als AddOn
^^^^^^^^^

Zur Installation als AddOn einfach in Mathematicas AddOn-Applications Ordner
ein neue Ordner für Tinkerforge anlegen und die ``Tinkerforge.dll`` Datei hinein
kopieren. Unter Windows ist der AddOn-Applications Ordner für Mathematica 9 hier
zu finden (für Mathematica 10 die ``9.0`` durch ``10.0`` ersetzen)::

 C:\Programme\Wolfram Research\Mathematica\9.0\AddOns\Applications\

Unter Linux ist er hier (für Mathematica 10 die ``9.0`` durch ``10.0`` ersetzen)
zu finden::

 /usr/local/Wolfram/Mathematica/9.0/AddOns/Applications/

Und unter macOS ist er hier zu finden::

 /Applications/Mathematica.app/AddOns/Applications/

In diesem Ordner dann einen ``Tinkerforge/`` Ordner anlegen, in diesem einen
``assembly/`` Ordner anlegen und in diesen dann die ``Tinkerforge.dll`` Datei
kopieren. Es sollte dann unter Windows so aussehen::

 C:\Programme\Wolfram Research\Mathematica\9.0\AddOns\Applications\Tinkerforge\assembly\Tinkerforge.dll

So unter Linux::

 /usr/local/Wolfram/Mathematica/9.0/AddOns/Applications/Tinkerforge/assembly/Tinkerforge.dll

Und so unter macOS::

 /Applications/Mathematica.app/AddOns/Applications/Tinkerforge/assembly/Tinkerforge.dll

Wenn die Bindings so installiert wurden dann muss noch der ``LoadNETAssembly[]``
Aufruf in den Beispielen zu

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge","Tinkerforge`"]

abgeändert werden. Der Abschnitt über den Test eines Beispiels vermittelt mehr
Details darüber.


.. _api_bindings_mathematica_install_systemfile:

Als SystemFile
^^^^^^^^^^^^^^

Zur Installation als SystemFile einfach die ``Tinkerforge.dll`` in Mathematicas
SystemFiles Ordner für .NET/Link kopieren. Unter Windows ist der SystemFiles
Ordner für .NET/Link für Mathematica 9 hier zu finden (für Mathematica 10 die
``9.0`` durch ``10.0`` ersetzen)::

 C:\Programme\Wolfram Research\Mathematica\9.0\SystemFiles\Links\NETLink\

Unter Linux ist er hier (für Mathematica 10 die ``9.0`` durch ``10.0`` ersetzen)::

 /usr/local/Wolfram/Mathematica/9.0/SystemFiles/Links/NETLink/

Und unter macOS ist er hier::

 /Applications/Mathematica.app/SystemFiles/Links/NETLink/

Wenn die Bindings so installiert wurden dann muss noch der ``LoadNETAssembly[]``
Aufruf in den Beispielen zu

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge"]

abgeändert werden. Der Abschnitt über den Test eines Beispiels vermittelt mehr
Details darüber.


.. _api_bindings_mathematica_install_without:

Ohne Installation
^^^^^^^^^^^^^^^^^

Die Mathematica Bindings müssen nicht unbedingt installiert werden. Stattdessen
kann auch einfach der Ordner in dem die ``Tinkerforge.dll`` liegt beim
``LoadNETAssembly[]`` Aufruf mit angegeben werden. In den Beispielen ist
der ``LoadNETAssembly[]`` schon so, dass er passend auf die ``Tinkerforge.dll``
Datei verweist, wenn die Bindings und die Beispiele aus deren ZIP Datei entpackt
wurden. Der Abschnitt über den Test eines Beispiels vermittelt mehr Details
darüber.


Test eines Beispiels
--------------------

Um ein Mathematica Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Stepper Brick
^^^^^^^^^^^^^

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel ausführen.
Dazu das ``ExampleConfiguration.nb`` Notebook aus dem
``examples/Brick/Stepper/`` Ordner in Mathematica öffnen.

Bindings laden
""""""""""""""

Abhängig davon ob und wie die Mathematica Bindings installiert wurden muss
die ``LoadNETAssembly[]`` Zeile angepasst werden, damit Mathematica die
``Tinkerforge.dll`` Datei finden kann. Weitere Details über das Laden von
.NET Bibliotheken finden sich in der `Mathematica Dokumentation
<https://reference.wolfram.com/language/NETLink/ref/LoadNETAssembly.html>`__.

Wurden die Bindings als :ref:`AddOn <api_bindings_mathematica_install_addon>`
installiert dann muss der ``LoadNETAssembly[]`` Aufruf so aussehen:

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge","Tinkerforge`"]

Wurden die Bindings als :ref:`SystemFile
<api_bindings_mathematica_install_systemfile>` installiert dann muss der
``LoadNETAssembly[]`` Aufruf so aussehen:

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge"]

Wurden die Bindings :ref:`nicht installiert
<api_bindings_mathematica_install_without>` dann kann der ``LoadNETAssembly[]``
Aufruf unverändert bleiben, wenn die Beispiele direkt aus der entpackten
ZIP Datei der Bindings ausgeführt werden. Die Beispiele sind so konstruiert,
dass der ``LoadNETAssembly[]`` Aufruf sich auf die ``Tinkerforge.dll`` Datei aus
der entpackten ZIP Datei bezieht.

Ansonsten kann ``LoadNETAssembly[]`` auch mit dem absoluten Pfad zur
``Tinkerforge.dll`` Datei aufgerufen werden. Zum Beispiel so unter Windows:

.. code-block:: mathematica

  LoadNETAssembly["C:\\Absoluter\\Pfad\\zur\\Tinkerforge.dll"]

Und zum Beispiel so unter Linux und macOS:

.. code-block:: mathematica

  LoadNETAssembly["/Absoluter/Pfad/zur/Tinkerforge.dll"]

Netzwerkadresse und UID einstellen
""""""""""""""""""""""""""""""""""

Am Anfang des Beispiels ist mit ``host`` und ``port`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``uid`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: mathematica

  host="localhost"
  port=4223
  uid="XXYYZZ"(* Change XXYYZZ to the UID of your Stepper Brick *)

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können. Dazu
alle Zellen des Notebooks von oben nach unten auswerten.

Temperature Bricklet
^^^^^^^^^^^^^^^^^^^^

Hier ein weiteres :ref:`Beispiel <temperature_bricklet_mathematica_examples>`,
das einen dynamischen Plot der Temperaturwerte eines Temperature Bricklets
zeigt. Der Einbruch bei Sample 82 wurde mittels eines Kältesprays erzeugt.

.. image:: /Images/Screenshots/mathematica_example.jpg
   :scale: 100 %
   :alt: Temprature Bricklet mit dynamischem Plot der Messwerte
   :align: center


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Mathematica_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Mathematica>
   Bricks <Bricks_Mathematica>
   Bricks (Abgekündigt) <Bricks_Mathematica_Discontinued>
   Bricklets <Bricklets_Mathematica>
   Bricklets (Abgekündigt) <Bricklets_Mathematica_Discontinued>
