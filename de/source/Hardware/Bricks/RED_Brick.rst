
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. note::
  Dieses Brick befindet sich noch in Entwicklung und ist noch nicht erhältlich. Geplanter Verkaufsstart: Dez 2014. Aktuelle Informationen lassen sich in unserem `Blog <http://www.tinkerforge.com/de/blog/>`__ finden.

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
  Dieses Brick befindet sich noch in Entwicklung und ist noch nicht erhältlich. Geplanter Verkaufsstart: Dez 2014. Aktuelle Informationen lassen sich in unserem `Blog <http://www.tinkerforge.com/de/blog/>`__ finden.

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


.. _red_brick_connectivity:

Anschlussmöglichkeit
--------------------


.. _red_brick_test:

Erster Test
-----------


.. _red_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RED_Brick_hlpi.table
