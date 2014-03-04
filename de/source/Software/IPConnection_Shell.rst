
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - IP Connection

.. |ref_api_bindings| replace:: :ref:`Shell Bindings <api_bindings_shell>`

.. _ipcon_shell:

Shell - IP Connection
=====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_shell_examples:

Beispiele
---------

Der folgende Beispielcode ist `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/deed.de>`__.

Enumerate
^^^^^^^^^

`Download (example-enumerate.sh) <https://github.com/Tinkerforge/generators/raw/master/shell/example-enumerate.sh>`__

.. literalinclude:: IPConnection_Shell_example-enumerate.sh
 :language: bash
 :linenos:
 :tab-width: 4


.. _ipcon_shell_api:

API
---

Als erstes einige Information über die allgemeine Struktur der Befehle:

.. sh:function:: X Ntinkerforge A[<option>..] L<command> L[<argument>..]

 :param <command>: string

 Der Grundbefehl kennt mehrere Optionen:

 * ``--help`` zeigt allgemeine Hilfe an und endet dann
 * ``--version`` zeigt die Versionsnummer an und endet dann
 * ``--host <host>`` IP Adresse oder Hostname des Verbindungsziels, Standard: ``localhost``
 * ``--port <port>`` Port-Nummer des Verbindungsziels, Standard: ``4223``
 * ``--item-separator <item-separator>`` Trennzeichen für Array-Einträge,
   Standard: ``,`` (Komma)
 * ``--group-separator <group-separator>`` Trennzeichen für Ausgabegruppen,
   Standard: ``\n`` (neue Zeile)
 * ``--no-symbolic-input`` deaktiviert symbolische Eingabe von Werten
 * ``--no-symbolic-output`` deaktiviert symbolische Ausgabe von Werten

 Alle Befehle, außer die ``--help`` oder ``--version`` Option sind angegeben,
 erstellen eine TCP/IP Verbindung zum gegebenen ``host`` und ``port``. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Das Trennzeichen für Array-Einträge wird beim Parse und Formatieren von Arrays
 verwendet. Ein Array mit den drei Werten 1, 2 und 3 wird als ``1,2,3``
 formatiert.

 Das Trennzeichen für Ausgabegruppen wird beim Formatieren der Ausgabe von
 Callbacks verwendet. Das Trennzeichen wird vor jeder Callback-Ausgabe mit mehr
 als einer Zeile ausgegeben, außer der ersten, um die Ausgabe von mehreren
 Callback-Aufrufen zu trennen. Siehe den Abschnitt über
 :ref:`Ausgabeformatierung <ipcon_shell_output>` für mehr Details.

 Standardmäßig ist die symbolische Eingabe und Ausgabe aktiviert. Zum Beispiel
 kann die :sh:func:`set-i2c-mode <temperature-bricklet set-i2c-mode>` Funktion
 des Temperature Bricklets mit zwei verschiedenen Werten aufgerufen werden: 0
 und 1. Wenn symbolische Eingabe aktiviert ist, dann werden auch noch die beiden
 Symbole ``fast`` (0) und ``slow`` (1) als Eingabe für diese Werte akzeptiert.
 Das gleiche gilt für die :sh:func:`get-i2c-mode
 <temperature-bricklet get-i2c-mode>` Funktion: Die gleichen Symbole werden für
 symbolische Ausgabe verwendet, wenn diese aktiviert ist.

 Es gibt vier Unterbefehle: ``call``, ``dispatch``, ``enumerate`` und ``listen``


.. sh:function:: X Ptinkerforge Ncall A[<option>..] L<device> L<uid> L<function> L[<argument>..]

 :param <device>: string
 :param <uid>: string
 :param <function>: string

 Der ``call`` Befehl wird verwendet um eine Funktion eines Bricks oder Bricklets
 aufzurufen. Der Befehl kennt mehrere Optionen:

 * ``--help`` zeigt Hilfe für den spezifischen ``call`` Befehl an und endet dann
 * ``--list-devices`` zeigt eine Liste der bekannten Geräte an und enden dann
 * ``--timeout <timeout>`` maximale Zeit (msec) für die auf eine Antwort
    gewartet wird, Standard: ``2500``

 Wenn die ``--list-devices`` Option angegeben ist werden alle bekannten
 Gerätenamen für das ``<device>`` Argument aufgelistet. Zum Beispiel
 ``master-brick`` und ``ambient-light-bricklet``.

 Die ``--timeout`` Option erlaubt es die maximale Zeit in msec festzulegen für
 die auf einen Antwort auf einen Funktionsaufruf gewartet wird. Falls eine
 Antwort nicht rechtzeitig eintrifft, dann wird das Programm mit einem Fehler
 beendet.

 Das ``<uid>`` Argument nimmt eine UID entsprechend dem gewählten Gerätetypen.
 Dies erlaubt es ein spezifisches Gerät auszuwählen. Alle verbundenen Bricks
 und Bricklets können mittels des :sh:func:`enumerate <tinkerforge enumerate>`
 Befehls entdeckt werden.

 Das ``<function>`` Argument gibt an welche Funktion aufgerufen werden soll.
 Welche weiteren Argumente angegeben werden müssen hängt von der ausgewählten
 Funktion ab.


.. sh:function:: X Ptinkerforge Ndispatch A[<option>..] L<device> L<uid> L<callback>

 :param <device>: string
 :param <uid>: string
 :param <callback>: string

 Der ``dispatch`` Befehl wird verwendet um eingehende Callbacks eines Bricks
 oder Bricklets abzufertigen. Der Befehl kennt mehrere Optionen:

 * ``--help`` zeigt Hilfe für den spezifischen ``dispatch`` Befehl an und endet
   dann
 * ``--list-devices`` zeigt eine Liste der bekannten Geräte an und enden dann
 * ``--duration <duration>`` die Zeit (msec) für die eingehende Callbacks
   abgefertigt werden (0: Ende nach dem ersten Callback, -1: unbegrenzt),
   Standard: -1

 Wenn die ``--list-devices`` Option angegeben ist werden alle bekannten
 Gerätenamen für das ``<device>`` Argument aufgelistet. Zum Beispiel
 ``master-brick`` und ``ambient-light-bricklet``.

 Die ``--duration`` Option erlaubt es die Zeit in msec festzulegen für die
 eingehende Callbacks abgefertigt werden.

 Das ``<uid>`` Argument nimmt eine UID entsprechend dem gewählten Gerätetypen.
 Dies erlaubt es ein spezifisches Gerät auszuwählen. Alle verbundenen Bricks
 und Bricklets können mittels des :sh:func:`enumerate <tinkerforge enumerate>`
 Befehls entdeckt werden.

 Das ``<callback>`` Argument gibt an welcher Callback abgefertigt werden soll.


Grundfunktionen
^^^^^^^^^^^^^^^

.. sh:function:: X Ptinkerforge Nenumerate A[<option>..]

 :returns uid: string
 :returns connected-uid: string
 :returns position: char
 :returns hardware-version: int,int,int
 :returns firmware-version: int,int,int
 :returns device-identifier: int (hat Symbole)
 :returns enumeration-type: int (hat Symbole)

 Der ``enumerate`` Befehl wird verwendet um verbundenen Bricks und Bricklets zu
 entdecken. Der Befehl kennt mehrere Optionen:

 * ``--help`` zeigt Hilfe für den ``enumerate`` Befehl an und endet dann
 * ``--duration <duration>`` die Zeit (msec) für die eingehende Antworten
   abgefertigt werden (0: Ende nach der ersten Antwort, -1: unbegrenzt),
   Standard: 250
 * ``--types <types>`` Array von abzufertigenden Enumerierungsarten, Standard:
   ``available``
 * ``--execute <command>`` Shell-Befehl der für jede eingehende Antwort
   ausgeführt wird ()

 Die ``--duration`` Option ermöglicht es die Zeit (msec) festzulegen für die
 eingehende Antworten abgefertigt werden.

 Die ``--types`` Option ermöglicht es anzugeben welche Enumerierungsarten
 abgefertigt werden sollen. Standardmäßig werden nur Enumerate-Callback mit
 ``enumeration-type=available`` abgefertigt.

 Die ``--execute`` Option ermöglicht erweiterte Ausgabeformatierung. Siehe dazu
 den Abschnitt über :ref:`Ausgabeformatierung <ipcon_shell_output>` für Details.

 Der Befehl hat sieben Ausgabewerte:

 * ``uid`` ist die UID des Bricks/Bricklets.
 * ``connected-uid`` ist die UID des Bricks mit dem das Brick/Bricklet verbunden
   ist. Für ein Bricklet ist dies die UID des Bricks mit dem es verbunden ist.
   Für einen Brick ist es die UID des untersten Master Bricks in einem Stapel.
   Der unterste Master Brick hat die Connected-UID "0". Mit diesen Informationen
   sollte es möglich sein die komplette Netzwerktopologie zu rekonstruieren.
 * ``position`` ist die Position im Stapel (0 - 8) für Bricks oder die Position
   am Brick (a - d) für Bricklets.
 * ``hardware-version`` in Major, Minor und Release Format.
 * ``firmware-version`` in Major, Minor und Release Format.
 * ``device-identifier`` ist der Name des Bricks/Bricklets wie er auch von der
   ``--list-devices`` Option der ``call`` und ``dispatch`` Befehle ausgegeben
   wird. Wenn symbolische Ausgabe deaktiviert ist, dann ist es eine Zahl die
   das Brick/Bricklet repräsentiert.
 * ``enumeration-type`` Art der Enumerierung.

 Mögliche Enumerierungsarten sind:

 * ``available`` = 0, das Gerät ist verfügbar (Enumerierung vom Benutzer
   ausgelöst).
 * ``connected`` = 1, das Gerät wurde neu verbunden (Automatisch vom Brick
   gesendet nachdem die Kommunikation aufgebaut wurde). Dies kann bedeuten,
   dass das Gerät die vorher eingestellte Konfiguration verloren hat und neu
   konfiguriert werden muss.
 * ``disconnected`` = 2, das Gerät wurde getrennt (Nur bei USB-Verbindungen
   möglich). In diesem Fall haben nur ``uid`` und ``enumeration-type`` einen
   gültigen Wert.

 Die Device Identifier Werte sind :ref:`hier <device_identifier>` zu finden.

Fortgeschrittene Funktionen
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sh:function:: X Ptinkerforge Nlisten A[<option>..]

 Der ``listen`` Befehlt wird verwendet um einen TCP/IP Socket zu öffnen der
 ``call``, ``dispatch`` und ``enumerate`` Befehle entgegen nimmt. Dies erlaubt
 es die Shell Bindings als Text Protokoll Proxy für Clients wie ``netcat``,
 ``telnet`` oder die :ref:`NetIO Controller App <netio_setup>` zu verwenden.
 Der ``listen`` Befehl kennt mehrere Optionen:

 * ``--help`` zeigt Hilfe für den ``listen`` Befehl an und endet dann
 * ``--address <address>`` IP Adresse auf der gelauscht wird, Standard: ``0.0.0.0``
 * ``--port <port>`` Port-Nummer auf der gelauscht wird, Standard: ``4217``
 * ``--enable-host`` aktiviert die ``--host`` Option um IP Adresse oder Hostname des Verbindungsziels zu ändern
 * ``--enable-port`` aktiviert die ``--port`` Option um Port-Nummer des Verbindungsziels zu ändern
 * ``--enable-execute`` aktiviert die ``--execute`` Option für Getter und Callbacks

 Im Listen Modus sind einige Optionen für eingehende Befehle standardmäßig
 deaktiviert.

 Die ``--host`` und ``--port`` Optionen sind standardmäßig deaktiviert, so dass
 eingehende Befehle nur Verbindungen zu Hostname und Port-Nummer aufbauen
 können, welche beim ``listen`` Befehl angegeben wurden.
 Mittels ``--enable-host`` und ``--enable-port`` können diese Optionen für
 eingehende Befehle aktiviert werden.

 Die ``--execute`` Option ist standardmäßig deaktiviert, so dass eingehende
 Befehle keine anderen Kommandozeilenbefehle ausführen können. Mittels
 ``--enable-execute`` kann diese Option für eingehende Befehle aktiviert werden.

 Eingehende Befehle müssen mit ``\n`` terminiert werden. Die Ausgabe ist
 ebenfalls mit ``\n`` terminiert. Siehe den Abschnitt über
 :ref:`Ausgabeformatierung <ipcon_shell_output>` für weitere Details.

 .. versionadded:: 2.0.3

.. _ipcon_shell_output:

Ausgabeformatierung
^^^^^^^^^^^^^^^^^^^

Standardmäßig wird die Ausgabe von Getter-Funktionen und Callbacks in
``<key>=<value>``-Format ausgegeben. Zum Beispiel hier die Ausgabe eines
Enumerate-Callbacks:

.. code-block:: bash

    $ tinkerforge enumerate
    uid=68yjBL
    connected-uid=0
    position=0
    hardware-version=1,0,0
    firmware-version=2,0,6
    device-identifier=master-brick
    enumeration-type=available

    uid=eN3
    connected-uid=68yjBL
    position=a
    hardware-version=1,1,0
    firmware-version=2,0,0
    device-identifier=distance-ir-bricklet
    enumeration-type=available

Die ``--item-separator`` Option beeinflusst wie Arrays formatiert werden und die
``--group-separator`` Option beeinflusst wie die Ausgabe von Gruppen formatiert
wird. Das obigen Beispiel zeigt zwei Gruppen getrennt mit einer leeren Zeile.

Die Ausgabe im Listen Modus (siehe :sh:func:`tinkerforge listen`) unterscheidet
sich in zwei Aspekten und das Parsen auf der Client Seite zu vereinfachen:

* es wird kein Trennzeichen zwischen Ausgabegruppen verwendet und die
  ``--group-separator`` Option wird ignoriert
* einzelne Zeilen einer Ausgabegruppen werden mit ``\t`` statt ``\n`` getrennt

Dies bedeutet, dass die Ausgabe des ``enumerate`` Befehls im Liste Modus so aussieht::

 uid=68yjBL\tconnected-uid=0\tposition=0\thardware-version=1,0,0\tfirmware-version=2,0,6\tdevice-identifier=master-brick\tenumeration-type=available\n
 uid=eN3\tconnected-uid=68yjBL\tposition=a\thardware-version=1,1,0\tfirmware-version=2,0,0\tdevice-identifier=distance-ir-bricklet\tenumeration-type=available\n

Erweiterte Optionen
"""""""""""""""""""

Für erweitere Ausgabeformatierung unterstützen alle Getter-Funktionen und
Callbacks die ``--execute`` Option. Diese nimmt als Argument eine
Shell-Befehlszeile mit Platzhaltern der für jede eingehende Antwort ausgeführt
wird.

Ein einfaches Beispiel: Die aktuelle Distanz in mm eines Distance IR Bricklets
in ``<key>=<value>``-Format:

.. code-block:: bash

    $ tinkerforge call distance-ir-bricklet eN3 get-distance
    distance=473

Und jetzt mit ``--execute`` Option erweitere Ausgabeformatierung mit ``bc`` und
``printf``:

.. code-block:: bash

    $ tinkerforge call distance-ir-bricklet eN3 get-distance\
      --execute "echo 'scale=2; {distance} / 10' | bc | xargs printf 'current distance is %.1fcm\n'"
    current distance is 46.3cm

Bevor die Befehlszeile ausgeführt wird, werden die enthaltenen Platzhalter mit
den entsprechenden Werten ersetzt. Im obigen Beispiel gibt ein Aufruf von
``get-distance`` ohne ``--execute`` eine einzelne Zeile mit dem Key ``distance``
aus. Dieser Key wird auch als Platzhalter in geschweiften Klammern für die
`--execute`` Option verwendet: ``{distance}``.

Im Listen Modus (siehe :sh:func:`tinkerforge listen`) ist die ``--execute``
Option standardmäßig nicht verfügbar und muss über die ``--enable-execute``
Option des ``listen`` Befehls erst aktiviert werden.
