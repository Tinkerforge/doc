
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. note::
  Dieses Brick befindet sich noch in Entwicklung und ist noch nicht erhältlich

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_red_prototype_350.jpg",
	               "Bricks/brick_red_prototype_600.jpg",
	               "RED Brick Prototyp")
	}}
	{{ tfdocend() }}


Features
--------

* Steuert andere Bricks und Bricklets
* Führt direkt dein geschriebenes Programm aus
* Unterstützt nahezu alle Sprachen

.. _red_brick_description:

Beschreibung
------------

.. note::
  Dieses Brick befindet sich noch in Entwicklung und ist noch nicht erhältlich. Geplanter Verkaufsstart: Dez 2014. 

  Aktuelle Informationen lassen sich in unserem `Blog <http://www.tinkerforge.com/de/blog/>`__ finden. Bisherige Blogposts:

  * `Tinkerforge goes Stand-Alone aka RED Brick <http://www.tinkerforge.com/de/blog/2014/2/21/tinkerforge-goes-stand-alone-aka-red-brick>`__
  * `RED Brick Leiterplatten angekommen <http://www.tinkerforge.com/de/blog/2014/4/10/red-brick-leiterplatten-angekommen>`__
  * `Neuigkeiten zum RED Brick <http://www.tinkerforge.com/de/blog/2014/5/13/neuigkeiten-zum-red-brick>`__
  * `RED Brick: Tut es? Oder tut es nicht? <http://www.tinkerforge.com/de/blog/2014/5/21/red-brick:-tut-es-oder-tut-es-nicht>`__
  * `RED Brick Software-Infrastruktur <http://www.tinkerforge.com/de/blog/2014/6/20/red-brick-software-infrastruktur>`__
  * `RED Brick im EMV Labor <http://www.tinkerforge.com/de/blog/2014/8/28/red-brick-im-emv-labor>`__
  * `RED Brick Zustandsbericht <http://www.tinkerforge.com/de/blog/2014/10/15/neuigkeiten-zum-red-brick>`__
  * `RED Brick, der Countdown läuft <http://www.tinkerforge.com/de/blog/2014/11/12/red-brick-der-countdown-laeuft>`__



Das Rapid Embedded Development Brick (RED Brick) kann andere Bricks und 
Bricklets steuern. Die aktuell unterstützten Sprachen: C/C++, C#, 
Delphi/Lazerus, Java, JavaScript, MATLAB/Octave, Perl, PHP, Python, Ruby, Shell 
und Visual Basic .NET, können direkt auf dem Brick ausgeführt werden.

Ein Programm, das Bricks und Bricklets steuert, kann auf einem normalen 
PC/Mac geschrieben und getestet werden. Anschließend kann es per Knopfdruck auf 
das RED Brick übertragen und ohne Änderungen auf diesen ausgeführt werden. 
Es können mehrere Programme gleichzeitig ausgeführt werden und deren Ausführung 
konfiguriert (dauernd, alle X Minuten etc.) sowie überwacht werden.

Eingebettete Systeme können somit sehr schnell und einfach entwickelt werden. 
Unseres Wissens nach ist keine auch nur im Ansatz vergleichbare Lösung 
erhältlich. 

Für jede unterstützte Programmiersprache sind die Tinkerforge API und häufig 
genutzte Bibliotheken vorinstalliert. Weitere notwendige Bibliotheken können 
nachinstalliert werden.

Das Brick ist mit einem Micro-HDMI Anschluss ausgestattet, so dass auch 
Programme mit grafischer Benutzeroberfläche ausgeführt werden können. Eine USB 
2.0 Host Schnittstelle kann genutzt werden um Eingabe- und Zeigegeräte, wie 
Tastaturen, Mäuse oder Touchscreens, zu nutzen.

Mit der Ethernet Master Extension kann das RED Brick um eine 
Ethernetschnittstelle erweitert werden. Die RS485 Master Extension wird 
ebenfalls unterstützt, so dass auch entfernte Stapel von Bricks und Bricklets
vom RED Brick gesteuert werden können.

Fortgeschrittene Nutzer können das Brick mit vollem Zugriff auf dem 
zugrundeliegenden Debian System nutzen. Ein GPIO FPC Steckverbinder ermöglicht 
den Zugriff auf ausgewählte Prozessorsignale und kann genutzt werden um eigene
Entwicklungen anzubinden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           TBDg
Stromverbrauch                    TBDmA
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/red_brick_dimensions.png>`__)
* Linux Image und Platinenlayout (`Download <https://github.com/Tinkerforge/red-brick/zipball/master>`__)


.. _red_brick_hardware:

Hardwarebeschreibung
--------------------

Das RED Brick ist mit einem 1Ghz Cortex A8 mit 512MB DDR3 SDRAM ausgestattet.
Dazu kommen noch diverse Schnittstellen

Power Button
^^^^^^^^^^^^

LEDs
^^^^


Linux Images
------------

Im Hintergrund läuft ein von uns angepasstes Debian Image. Dieses ist in zwei 
Versionen verfügbar. Das Full Image TODO. Das TODO Image.

Full Image
^^^^^^^^^^

X Image
^^^^^^^

.. _red_brick_test:

Erster Test
-----------

.. _red_brick_usage:

Nutzung des RED Bricks
----------------------

Programme ausführen
^^^^^^^^^^^^^^^^^^^
TODO Link auf RED Brick Tutorial

Ethernet konfigurieren
^^^^^^^^^^^^^^^^^^^^^^




.. _red_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RED_Brick_hlpi.table
