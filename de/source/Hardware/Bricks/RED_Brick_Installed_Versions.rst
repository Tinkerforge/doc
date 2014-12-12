
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / <a href="RED_Brick.html">RED Brick</a> / Installierte Versionen
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions

.. |c| unicode:: 0x2713
    :trim:

.. _red_brick_installed_versions:

RED Brick - Installierte Bibliotheken und deren Versionen
=========================================================

Beschreibung
------------

Eine Vielzahl von verschiedenen Software-Bibliotheken sind bereits auf den
RED Brick Images vorinstalliert. Auf dieser Seite sind deren Namen und
die jeweils installierte Version für die aktuelle Version des
``Full`` und des ``Fast`` Images zu finden.

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
Email (info@tinkerforge.com). In dieser sollte der Ort stehen an dem wir
die Bibliothek finden und eine Beschreibung wie man diese installiert. Am
einfachsten wäre es, wenn diese direkt im Debian wheezy Repository verfügbar
wäre.

Installierte Bibliotheken
-------------------------

.. include:: RED_Brick_c_features.table

.. include:: RED_Brick_java_features.table

.. include:: RED_Brick_mono_features.table

.. include:: RED_Brick_perl_features.table

.. include:: RED_Brick_php_features.table

.. include:: RED_Brick_python_features.table

.. include:: RED_Brick_ruby_features.table
