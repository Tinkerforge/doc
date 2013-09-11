
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / NetIO Controller App Setup

.. _netio_setup:

NetIO Controller App Setup
==========================

Die `NetIO Controller App <http://netio.davideickhoff.de/>`__ in Kombination
mit den :ref:`Shell Bindings <api_bindings_shell>` erlaubte es einem Smartphone
mit Bricks und Bricklets zu interagieren. Die NetIO App stellt ein flexibles und
online konfigurierbares GUI bereit welches u.a. Textbefehle senden und empfangen
kann. Die Shell Bindings agieren dann als Proxy zwischen den NetIO Textbefehlen
und dem binären :ref:`TCP/IP Protokoll <llproto_tcpip>`, das zur Kommunikation
mit den Bricks und Bricklets verwendet wird.

Die Tinkerforge Seite
---------------------

Als erste Schritt sollten die Shell Bindings aus dem :ref:`Downloadbereich
<downloads_bindings_examples>` heruntergeladen und getestet werden. Der
:ref:`Brick Daemon <brickd>` wird zusätzlich benötigt, wenn die Bricks über USB
angeschlossen sind.

Befehlsformat
^^^^^^^^^^^^^

Die Shell Bindings können Befehle über die Kommandozeile und über TCP/IP
Verbindungen entgegennehmen. Das Befehlsformat ist in beiden Fällen fast das
gleiche. Zum Beispiel, dieser Befehl:

.. code-block:: bash

 $ tinkerforge call ambient-light-bricklet gxe get-illuminance
 illuminance=721

muss über eine TCP/IP Verbindung so gesendet werden::

 call ambient-light-bricklet gxe get-illuminance\n

Also, ``tinkerforge`` am Anfang entfernen und ``\n`` als Terminator anhängen.
NetIO hat ein ``commandTermination`` Attribut mit ``\n`` als Standardwert,
daher kümmert sich NetIO schon von sich aus um das Anhängen von ``\n`` an die
Befehle.

Die Ausgabe der Befehle über eine TCP/IP Verbindung wird auch mit ``\n``
terminiert::

 illuminance=721\n

Falls die Ausgabe mehrere Werte beinhaltet, dann werden diese auf der
Kommandozeile jeweils als ein Wert pro Zeile ausgegeben:

.. code-block:: bash

 $ tinkerforge call dual-relay-bricklet fAa get-state
 relay1=true
 relay2=false

Wenn die Ausgabe über eine TCP/IP Verbindung gesendet wird dann wird ``\t`` als
Trennzeichen verwendet::

 relay1=true\trelay2=false\n

Listen Befehl
^^^^^^^^^^^^^

Der Text Protokoll Proxy wird über den :sh:func:`listen <tinkerforge listen>`
Befehl gestartet:

.. code-block:: bash

 $ tinkerforge listen

Standardmäßig wird eine Verbindung zum Brick Daemon auf ``localhost``
hergestellt. Falls der Brick Daemon auf einen anderen Computer läuft, oder
die Verbindung zu einer WIFI oder Ethernet Extension hergestellt werden soll,
dann können dazu die ``--host`` und ``--port`` Optionen verwendet werden:

.. code-block:: bash

 $ tinkerforge --host different-computer --port 5000 listen

Standardmäßig lauscht der ``listen`` Befehl auf Port-Nummer 4217. Mit der
``--port`` Option des ``listen`` Befehls kann dies geändert werden:

.. code-block:: bash

 $ tinkerforge --host different-computer --port 5000 listen --port 6000

Dieser Befehl stellt die Verbindung zu ``different-computer`` auf Port-Nummer
5000 her und lauscht auf Port-Nummer 6000 auf eingehende Verbindungen.

Die NetIO Seite
---------------

Als Einstiegspunkt können diese `Demo UI Config (iPhone)
<http://netio.davideickhoff.de/editor2?config=7179>`__ oder diese `Demo UI
Config (Nexus 7) <http://netio.davideickhoff.de/editor/?config=7223>`__
verwendet werden. Sie demonstrieren wie die Werte eines
:ref:`Temperature Bricklets <temperature_bricklet>` und eines
:ref:`Ambient Light Bricklets <ambient_light_bricklet>` ausgelesen werden
können und wie ein :ref:`Dual Relay Bricklet <dual_relay_bricklet>` geschaltet
werden kann. Siehe die :ref:`API Dokumentation <api_bindings_shell_links>` für
eine vollständige Referenz aller Befehle.

.. image:: /Images/Screenshots/netio_small.jpg
   :scale: 100 %
   :alt: NetIO Controller App Demo UI Config
   :align: center
   :target: ../_images/Screenshots/netio.jpg

Beide Demos verwenden erweiterte Ausgabeformatierung und setzen daher voraus,
dass der ``tinkerforge listen`` Befehl mit der ``--enable-execute`` Option
gestartet wurde. Mehr Details dazu im folgenden Abschnitt.

Bevor die Demo UI Configs verwendet werden können muss die Connection passend
eingestellt werden. Dazu muss mindestens das ``host`` Attribut passend zur IP
Adresse oder dem Hostnamen des Computers geändert werden auf dem der
``tinkerforge listen --enable-execute`` Befehl gestartet wurde.

Für die Shell Bindings wird eine Connection benötigt, deren ``format`` auf
``string`` und ``protocol`` auf ``socket`` eingestellt ist. Dies sind aber eh
die Standardeinstellungen.

Als weiteren Schritt müssen die UIDs der Bricks und Bricklets, mit denen
interagiert werden soll, ermittelt werden. Dazu kann der
:sh:func:`enumerate <tinkerforge enumerate>` Befehl der Shell Bindings
verwendet werden, oder alternative der :ref:`Brick Viewer <brickv>`.

Werte auslesen
^^^^^^^^^^^^^^

Um den Temperaturwert eines Temperature Bricklets mit UID ``dHd`` auszulesen
kann ein Label verwendet werden, dessen ``reads`` Attribut den folgenden Befehl
beinhaltet::

 call temperature-bricklet dHd get-temperature

Dies zeigt dann ``temperature=2168`` als Text im Label an. Das
``parseResponse`` Attribut kann verwendet werden, um den Zahlanteil der Antwort
zu extrahieren. Hier ein Beispiel, das dazu eine `Positive Lookbehind
Assertion <http://regexp-evaluator.de/tutorial/assertions/>`__ verwendet::

 (?<=temperature=)[^\n]+

Dieser reguläre Ausdruck erfasst alle Zeichen zwischen ``temperature=`` und dem
nächsten ``\n``.

Eine einfachere aber weniger robuste Lösung dafür ist es einfach ``\d+`` zu
verwenden, um eine Zahl an irgendeiner Stelle der Antwort zu erfassen.

Das ``formatResponse`` Attribut ermöglicht es an die Antwort eine Einheit
anzuhängen::

 {0} °C/100

Dies zeigt dann ``2168 °C/100`` als Text im Label an. Das liest sich etwas
umständlich, bedingt dadurch, dass das Temperature Bricklet seinen Wert in
°C/100 Einheiten ausgibt.

Die Shell Bindings können die Ausgabe der Befehle an einen beliebigen
Kommandozeilenbefehl übergeben, so dass sich dieser dann um die Formatierung
der Ausgabe kümmern kann. Die ``--execute`` Option ist dafür zuständig. Siehe
den Abschnitt über :ref:`Ausgabeformatierung <ipcon_shell_output>` für mehr
Details. Da die ``--execute`` Option verwendet werden kann um beliebige
Kommandozeilenbefehle auszuführen ist sie standardmäßig im Listen Modus
deaktiviert und muss erst über die ``--enable-execute`` Option aktiviert
werden::

 tinkerforge listen --enable-execute

Um die Temperatur in °C anstatt °C/100 ausgeben zu können muss der Wert durch
100 geteilt werden. Dazu kann der ``bc`` Befehl verwendet werden::

 echo "scale=2; 2168/100" | bc

Diese Kommandozeile gibt ``21.68`` aus benötigt aber eine geeignet Shell wie sie
typischerweise auf Linux und Mac OS X, aber nicht auf Windows, zu finden ist.
Um also solche Formatierung der Ausgabe durchzuführen ist es ratsam
``tinkerforge listen`` auf Linux oder Mac OS X zu starten. Es funktioniert
natürlich auf auf Windows erfordert es dann aber mit den Einschränkungen der
Windows Eingabeaufforderung umzugehen.

Wird das ``reads`` Attribut des Label wie folgt gesetzt::

 call temperature-bricklet dHd get-temperature --execute "echo scale=2\; {temperature}/100 | bc"

und das ``parseResponse`` Attribut auf ``.*`` und ``formatResponse`` auf
``{0} °C`` dann ergibt sich die gewünschte Ausgabe ``21.68 °C`` als Text im
Label.

Aktionen auslösen
^^^^^^^^^^^^^^^^^

Neben dem Auslesen von Sensorwerten können auch Aktionen wie das Umschalten
eines Dual Relay Bricklet (die UID für diese Beispiel ist ``fAa``) realisiert
werden.

Eine einfache Umsetzung dazu besteht aus zwei Buttons. Einer schaltet das Relais
ein und der andere schaltet es wieder aus. Das ``sends`` Attribut des On Buttons
ist wie folgt gesetzt::

 call dual-relay-bricklet fAa set-selected-state 1 true

und das ``sends`` Attribut des Off Buttons so::

 call dual-relay-bricklet fAa set-selected-state 1 false

Dies schaltet Relais 1 des Dual Relay Bricklets. Um Relais 2 zu schalten muss
``1`` durch ``2`` in beiden Befehlen ersetzt werden.

Eine andere Umsetzung dazu besteht aus einem Switch Element. Diese Element hat
zwei ``sends`` Attribute und ein ``reads`` Attribut um den aktuellen Status
des Relais zurückzulesen und darzustellen. Es gibt einige weitere Attribute die
passend eingestellt werden müssen, damit das Switch Element richtig funktioniert
(in ``<Attribut>: <Wert>`` Format)::

 onSend:         call dual-relay-bricklet fAa set-selected-state 1 true
 offSend:        call dual-relay-bricklet fAa set-selected-state 1 false
 reads:          call dual-relay-bricklet fAa get-state
 parseResponse:  (?<=relay1=)[^\t]+
 formatResponse: {0}
 onValue:        true
 interval:       2000

Die ``onSend`` und ``offSend`` Attribute verwenden die gleichen Befehle wie die
zwei Buttons im vorherigen Beispiel. Das ``reads`` Attribut liest den Zustand
des Relais aus. Die Ausgabe sieht wie folgt aus::

 relay1=true\trelay2=false\n

Die ``parseResponse`` und ``formatResponse`` Attribute werden verwendet um den
Zustand von Relais 1 aus der Antwort zu parsen, dieser ist entweder ``true``
oder ``false``. Letztlich vergleicht das Switch Element das Ergebnis mit dem
Wert des ``onValue`` Attributs, um zu entscheiden in welchen Zustand es
dargestellt werden soll. Dies wird mit einem ``interval`` von 2 Sekunden
wiederholt.

Damit dies für Relais 2 funktioniert muss ``1`` durch ``2`` in den ``onSend``
und ``offSend`` Befehlen ersetzt werden und das ``parseResponse`` Attribut muss
so geändert werden::

 (?<=relay2=)[^\n]+

Die beiden Demo UI Configs verwenden zwei Switch Elemente die wie beschrieben
funktionieren.
