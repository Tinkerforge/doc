
.. _tutorial_authentication:

Tutorial - Authentifizierung
============================

Standardmäßig wird auf der TCP/IP Schnittstelle des Brick Daemons und der
Ethernet/WIFI Extension keine Zugriffskontrolle durchgeführt. Jeder der eine
TCP/IP Verbindung herstellen kann, kann auch die Bricks und Bricklets
kontrollieren. In den meisten Fällen ist dies allerdings kein Problem, da sich
im lokalen Netzwerk nur vertrauenswürdige Teilnehmer aufhalten.

Für den Fall, dass Brick und Bricklets vor dem Zugriff nicht-vertrauenswürdiger
Teilnehmer geschützt werden sollen, kann Authentifizierung verwendet werden.
Wenn Authentifizierung aktiviert ist können Brick und Bricklets nur noch von
Teilnehmer kontrolliert werden, die das Authentifizierungsgeheimnis kennen.

Authentifizierung wird seit diesen Softwareversionen unterstützt:

* Brick Daemon: 2.1.0
* Brick Viewer: 2.1.0
* Go, JavaScript, MATLAB/Octave, MQTT und Rust API Bindings: 2.0.0
* Alle anderen API Bindings: 2.1.0
* Master Brick Firmware (Ethernet/WIFI Extension): 2.2.0


.. _tutorial_authentication_concept:

Konzept
-------

Wenn Authentifizierung aktiviert ist kann jeglicher Client (z.B. API Bindings
und Brick Viewer) zwar noch eine TCP/IP Verbindung zum Brick Daemon und der
Ethernet/WIFI Extension herstellen, aber die Verbindung befindet sich initial
im nicht-authentifizierten Zustand. In diesem Zustand werden alle eingehenden
Nachrichten zur Kontrolle der Bricks und Bricklets sowie ausgehende Callbacks
verworfen. Im nicht-authentifizierten Zustand findet keine normale
Kommunikation statt.

Um eine TCP/IP Verbindung vom nicht-authentifizierten in den authentifizierten
Zustand zu überführen muss der Client sich authentifizierten. Er muss dem Brick
Daemon oder der Ethernet/WIFI Extension beweisen, dass er das
Authentifizierungsgeheimnis kennt und daher berechtigt ist die Bricks und
Bricklets zu kontrollieren. Dieser Beweis wird über einen HMAC-SHA1
basierten :ref:`Handshake <llproto_tcpip_authentication>` erbracht, wobei das
Authentifizierungsgeheimnis aber niemals direkt übertragen wird.

Ist der Handshake erfolgreich dann wechselt die Verbindung vom
nicht-authentifizierten in den authentifizierten Zustand und die Kommunikation
kann normal weitergeführt werden. Schlägt der Handshake fehl wird die
Verbindung durch die Gegenseite geschlossen. Die Authentifizierung kann
fehlschlagen wenn das Authentifizierungsgeheimnis nicht übereinstimmt oder
Authentifizierung für den Brick Daemon oder die Ethernet/WIFI Extension nicht
aktiviert ist.


Konfiguration
-------------

Die Authentifizierung ist standardmäßig nicht aktiviert und muss erst
konfiguriert werden. Dazu muss ein Authentifizierungsgeheimnis festgelegt
werden, welches maximal 64 ASCII Zeichen lang sein kann. In diesem Tutorial
wird ``My Authentication Secret!`` als Geheimnis verwendet. Weitere
Informationen wie das Authentifizierungsgeheimnis beim Brick Daemon und der
Ethernet/WIFI Extension konfiguriert wird finden sich in den jeweiligen
Dokumentationsabschnitten:

* :ref:`Brick Daemon: Authentifizierung <brickd_authentication>`
* :ref:`Ethernet Extension: Authentifizierung <ethernet_extension_authentication>`
* :ref:`WIFI Extension: Authentifizierung <wifi_extension_authentication>`
* :ref:`WIFI Extension 2.0: Authentifizierung <wifi_v2_extension_authentication>`


Verwendung
----------

Wenn Authentifizierung aktiviert ist muss der :ref:`Authentifizierung-Handshake
<llproto_tcpip_authentication>` vom Client durchgeführt werden, um
die TCP/IP Verbindung vom nicht-authentifizierten in den authentifizierten
Zustand zu überführen.

Im Brick Viewer muss dazu nur das Häkchen für "Use Authentication" auf dem
Setup Tab gesetzt und das Authentifizierungsgeheimnis vor dem Klick auf den 
"Connect" Knopf eingegeben werden. Ab dann arbeitet Brick Viewer wie gewohnt.

Im eigenen Programm muss stattdessen die ``authenticate()`` Funktion aufgerufen
werden, die allen API Bindings hinzugefügt wurde. Diese Funktion bekommt als
Parameter das Geheimnis übergeben und führt den Handshake durch. Dies ist
entweder erfolgreich oder schlägt mit einem Fehlercode oder einer Exception 
fehl. In diesem Fall stimmt entweder das Geheimnis nicht überein, 
oder Authentifizierung für den Brick Daemon oder die Ethernet/WIFI Extension 
ist nicht aktiviert.

Es gibt zwei Arten ``authenticate()`` aufzurufen, ohne und mit Callbacks.


Ohne Callbacks
^^^^^^^^^^^^^^

Der Aufruf von ``authenticate()`` kann direkt nach dem Aufruf von ``connect()``
eingefügt werden. Ein solches Programm sieht wie folgt aus (Pseudocode)::

 func main() {
     ipcon.connect(HOST, PORT);
     ipcon.authenticate("My Authentication Secret!");

     // here comes the rest of your program
 }

Es reicht also aus eine einzelne Zeile Code dem Programm hinzuzufügen um
Authentifizierung zu nutzen. Allerdings funktioniert dies dann nicht mit
Auto-Reconnect zusammen.

Wie im Tutorial über den :ref:`Robusten Ansatz <tutorial_rugged_approach>`
erklärt sollte der Code einer gewissen grundlegenden Struktur folgen bei der
der Connected und Enumerate Callback zusammen mit Auto-Reconnect verwendet
wird um robuster gegenüber Ausfällen zu sein.


Mit Callbacks
^^^^^^^^^^^^^

Den ``authenticate()`` Aufruf nach dem ``connect()`` Aufruf einzufügen
funktioniert. Aber ``authenticate()`` muss auch nach jedem Auto-Reconnect
aufgerufen werden, da Auto-Reconnect eine neue Verbindung erstellt, die sich
dann wieder im nicht-authentifizierten Zustand befindet. Ein abgewandelte
Version des :ref:`robusten <tutorial_rugged_approach>` Beispiel sieht wie
folgt aus (Pseudocode)::

 func connected_callback(...) {
     ipcon.authenticate("My Authentication Secret!");
     ipcon.enumerate();
 }

 func main() {
     ipcon.connect(HOST, PORT);

     // here comes the rest of your program
 }

Jedes mal wenn eine TCP/IP Verbindung hergestellt wird wird der Connected
Callback aufgerufen, um das Programm darüber zu informieren. Dann ruft die
Connected Callback Funktion zuerst ``authenticate()`` auf um die Verbindung
in den authentifizierten Zustand zu bringen bevor ``enumerate()`` aufgerufen
wird. Auf diese Weise wird sichergestellt, dass die Verbindung sich immer
im authentifizierten Zustand befindet.

Für alle API Bindings gibt es ein neues Authentifizierungsbeispiel, das die
Verwendung dieses Ansatzes demonstriert:

.. include:: Tutorial_authenticate_examples.table
