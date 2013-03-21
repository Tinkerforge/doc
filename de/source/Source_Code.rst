
:breadcrumbs: <a href="index.html">Startseite</a> / Quelltexte und Bug Tracking

.. _source_code:

Quelltexte und Bug Tracking
===========================

Jedes von Tinkerforge veröffentlichte Produkt ist Open Source. Die Quelltexte
der Firmwares sowie die Platinenlayouts aller Bricks und Bricklets sind frei
verfügbar. Zusätzlich sind auch die Quelltexte aller Tools, wie des Brick
Daemon, des Brick Viewer und der Generatoren für API Bindings, verfügbar.

Das bedeute, dass alles an Tinkerforge Hardware und Software als
Ausgangspunkt für eigene Projekte verwenden werden kann, diese können
erweitert und modifiziert werden. Darüber hinaus kann unsere Entwicklungsarbeit
unterstützt und Probleme leichter gemeldet werden.

Um es der Community einfach zu machen Patches einzusenden und Probleme zu melden,
sind alle `Tinkerforge Projekte <https://github.com/Tinkerforge>`__ auf Github
gehostet.

Weiterführenden Informationen über git sind `hier <http://git-scm.com/>`__ zu
finden. Unsere Projekte können wie folgt geclonet werden::

 git clone git://github.com/Tinkerforge/PROJECT.git

Im Folgenden ist eine Liste aller Tinkerforge Projekt Repositories und
dazugehörigen Bug Trackern.

.. include:: Source_Code_gits.table


Wo und wie kann ich Problem melden?
-----------------------------------

Wenn du deinen Bug in einem der Tinkerforge Projekte findest, würden wir uns
freuen wenn du uns das Problem meldest. Als erstes musst du dazu das passende
Repository ermitteln:

Probleme die sich auf ein speziellen Brick oder Bricklet beziehen (z.B. ein
Parameter einer Funktion eines Bricks oder Bricklets funktioniert nicht wie
dokumentiert, oder ein Hardwareproblem) oder Probleme im Brick Daemon oder
Brick Viewer können in den offensichtlich dazugehörigen Repositories gemeldet
werden.

Falls das Problem aber alle Bricks gleichermaßen betrifft (z.B. die
Stapelkommunikation oder die USB Kommunikation ist fehlerhaft) dann solltest du
dies im Brick Library Repository melden. Falls das Problem bei jedem Bricklet
auftritt (z.B. das Timing wiederkehrender Callbacks passt nicht) dann solltest
du dies im Bricklet Library Repository melden. Probleme in der API oder deren
Dokumentation (z.B. Tippfehler oder falsche Aussagen) sollten im API
Generator Repository gemeldet werden.

Es ist wichtig, dass wir das Problem reproduzieren können. Daher ist es notwendig,
dass du beschreibst wie du das Problem erzeugt hast. Das kann z.B. ein kleines
Beispielprogramm sein, das das Problem erzeugt, oder eine Beschreibung deines
Hardwareaufbaus mit dem das Problem auftritt.
