
:shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions

.. |c| unicode:: 0x2713
    :trim:

.. _red_brick_installed_versions:

RED Brick - Installierte Bibliotheken und deren Versionen
=========================================================

Eine Vielzahl von verschiedenen Software-Bibliotheken sind bereits auf den
RED Brick Image vorinstalliert. Auf dieser Seite sind deren Namen und
die jeweils installierte Version für die aktuelle Version des Images zu
finden. Diese Liste kann auch im :ref:`Versions Tab des Brick Viewers
<red_brick_brickv_versions_tab>` eingesehen werden und bezieht sich dort
auf den jeweiligen RED Brick.

Die Liste der Versionen wird automatisch generiert und ist leider
nicht vollständig. Bibliotheken werden aus vielen verschiedenen Quellen
installiert (Debian Pakete, pip Pakete, Tarballs etc.). Leider sind nicht alle
Quellen einfach parsebar, so dass manche nicht auftauchen.

Andere Bibliotheken installieren
--------------------------------

Es können ganz einfach andere Bibliotheken auf dem RED Brick installiert
werden.

Sprachen, die einen Paketmanager besitzen (JavaScript, Perl, PHP, Python, Ruby)
können die vorinstallierten Paketmanager (``npm``, ``cpanm``, ``pear``,
``pip``, ``gem``) über das :ref:`Console Tab des Brick Viewers
<red_brick_brickv_console>` nutzen. Für jeden
Paketmanager gibt es im Netz gute Beschreibungen, wie diese zu benutzen sind.
Selbst wenn diese bisher nicht benutzt wurden, hat man innerhalb von ein paar
Minuten die gewünschte Bibliothek installiert!

Bei C# und Visual Basic .NET kann einfach die gewünschte .NET DLL zusammen
mit dem eigenen Programm hochgeladen werden und als Referenz hinzugefügt
werden. Gleiches gilt für Java, wo fehlende JARs mithochgeladen werden können.
Diese werden automatisch zum Class Path hinzugefügt.

Die meisten C Bibliotheken sind über das normale Debian Repository verfügbar.
Nutze ``apt-get`` um diese über das Console Tab zu installieren.

Die Tinkerforge Bindings sind natürlich für alle Sprachen vorinstalliert
und können direkt verwendet werden.

Wenn eine Bibliothek fehlt, die vorinstalliert sein sollte, schreib uns eine
E-Mail (info@tinkerforge.com). In dieser sollte der Ort stehen an dem wir
die Bibliothek finden und eine Beschreibung wie man diese installiert. Am
einfachsten wäre es, wenn diese direkt im Debian wheezy Repository verfügbar
wäre.

Mono aktualisieren
^^^^^^^^^^^^^^^^^^

Ab Image Version 1.7 kann Mono auf Version 4 aktualisiert werden,
standardmäßig ist Version 3 installiert. Für das Update benötigt der RED Brick
eine Internet-Verbindung. Es müssen folgende Befehle über den :ref:`Console
Tab <red_brick_brickv_console>` im Brick Viewer oder eine SSH Verbindung auf
dem RED Brick ausgeführt werden::

  sudo apt-get update
  sudo apt-get install mono-devel mono-complete ca-certificates-mono

Im Moment bringt Mono 4 den Visual Basic .NET Compiler ``vbnc`` nicht mit.
Wenn auf dem RED Brick Visual Basic .NET Quelltext kompiliert werden soll, dann
sollte im Moment nicht auf Mono 4 aktualisiert werden.

Installierte Bibliotheken
-------------------------

.. include:: RED_Brick_c_features.table

.. include:: RED_Brick_java_features.table

.. include:: RED_Brick_mono_features.table

.. include:: RED_Brick_perl_features.table

.. include:: RED_Brick_php_features.table

.. include:: RED_Brick_python_features.table

.. include:: RED_Brick_ruby_features.table
