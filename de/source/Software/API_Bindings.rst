.. _api_bindings:

API Bindings
============

Die API Bindings stellen eine TCP/IP Verbindung zum
:ref:`Brick Daemon <brickd>` here. Jeder Funktionsaufruf erzeugt ein TCP/IP Paket,
das über den Brick Daemon zum Brick geschickt wird. Beim Brick Daemon vom Brick
eingehende Pakete werden an den Aufrufer zurückgeroutet.

Unser :ref:`tutorial` beschreibt wie alles zusammengehört und funktioniert.

.. _api_bindings_ip_connection:

IP Connection
-------------

Die IP Connection erstellt eine TCP/IP Verbindung zwischen dem
:ref:`Brick Daemon <brickd>` und den entsprechenden API Bindings für die
verschiedenen Programmiersprachen.

Diese wird in den Bindings benutzt und ist für jede unterstütze
Programmiersprache implementiert. Die dazugehörige Dokumentation ist hier zu
finden:

.. include:: API_Bindings_bindings.table


Verwendung der Bindings
-----------------------

Die neusten Versionen der Bindings sind im :ref:`Downloadbereich
<downloads_bindings_examples>` zu finden.


.. _api_bindings_c:

C/C++
^^^^^

Die C/C++ Bindings bestehen aus den Bindings für alle Tinkerforge Bricks und
Bricklets (in ``bindings/``) und allen verfügbaren C/C++ Beispielen (in
``examples/``).

Um die C/C++ Bindings einfach zu halten haben sie nur externe Abhängigkeiten,
die möglichst überall verfügbar sind, wodurch sie leicht in jegliches Projekt
eingebunden werden können. Wir bieten keine vorkompilierte Bibliothek an, da
dies zu viel Aufwand wäre alle möglichen Kombinationen von Architekturen und
Betriebssystem zu versorgen. Die Bindings sollten aber auf den meisten
Architekturen (ARM, x86, etc.) und den meisten Betriebssystemen (Windows und
POSIX Systeme, wie Linux und Mac OS X, usw.) lauffähig sein.

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit GCC unter
Linux kompilieren. Dafür müssen die IP Connection und die Stepper Brick
Bindings (``ip_connection.h``, ``ip_connection.c``, ``brick_stepper.c`` und
``brick_stepper.h``) vom ``bindings/`` Ordner sowie
``example_configuration.c`` vom ``examples/brick/stepper/`` Ordner in ein
Projektordner kopiert werden::

 project_folder/
  -> ip_connection.c
  -> ip_connection.h
  -> brick_stepper.c
  -> brick_stepper.h
  -> example_configuration.c

GCC
"""

Die einzige Abhängigkeit auf Unix-artigen Systemen ist pthreads. Somit sieht der
Befehl um das Beispiel mit GCC unter Linux zu kompilieren wie folgt aus::

 gcc -pthread -o example_configuration brick_stepper.c ip_connection.c example_configuration.c

Unter Windows wird Win32 für Threads und WinSock2 (``ws2_32``) für die
Netzwerkverbindung verwendet. Mit MinGW lässt sich das Beispiel wie folgt
kompilieren (Linkerparameter müssen nach den Quelldateien angegeben werden)::

 gcc -o example_configuration.exe brick_stepper.c ip_connection.c example_configuration.c -lws2_32

Visual Studio
"""""""""""""

Mit Visual Studio kann der ``project_folder/`` wie folgt verwendet werden:

* File
* New
* Project From Existing Code
* Wähle als Type "Visual C++"
* Wähle ``project_folder/``
* Wähle einen Projektnamen
* Klicke Next
* Wähle "Console Application"
* Klicke Finish

Als nächstes muss das Projekt auf den C++ Compiler umgestellt werden. Unser C
Quelltext verwendet den C99 Standard, Visual Studio unterstützt aber nur C89.
Diese Problem kann durch die Verwendung des C++ Compilers umgangen werden:

* Project
* Properties
* C/C++
* Advanced, Option "Compile as"
* Wähle "Compile as C++ Code (/TP)"

Zusätzlich muss noch ``ws2_32.lib`` (WinSock2) dem Projekt hinzugefügt werden:

* Project
* Properties
* Linker
* Input, Option "Additional Dependencies"
* Füge ``ws2_32.lib;`` hinzu

Ältere Versionen von Visual Studio bringen kein ``stdint.h`` mit. Eine kompatible
Version gibt es `hier <http://msinttypes.googlecode.com/svn/trunk/stdint.h>`__.
Falls nötig diese herunterladen und im ``project_folder/`` speichern.

Das waren alle nötigen Änderungen, jetzt kann es los gehen!

Der Visual Studio Compiler kann auch von der Kommandozeile aus verwendet werden::

 cl.exe /TP /I. brick_stepper.c ip_connection.c example_configuration.c /link /out:example_configuration.exe ws2_32.lib


.. _api_bindings_c_ios:

C/C++ (iOS)
^^^^^^^^^^^

Objective-C ist kompatible zu C. Dies erlaubt es uns die :ref:`C/C++ Bindings
<api_bindings_c>` in einer iOS App zu verwenden.

Im Folgenden wird angenommen, dass die iOS Entwicklungsumgebung schon
installiert ist. Als Beispiel soll ein kleines Projekt zum Schalten eines
Dual Relay Bricklets erstellt werden. Es sollte leicht sein dieses Beispiel
für deine Zwecke weiterzuentwickeln.

Starte ein neues Xcode Projekt:

* File
* New
* Project...
* Wähle "iOS Application"
* Wähle "Single View Application"
* Klicke Next
* Wähle einen "Product Name" (e.g. Relay)
* Klicke Next
* Wähle einen "Folder" für das Projekt
* Klicke Create

Füge den Quelltext der C/C++ Bindings dem Projekt hinzu:

* Rechtsklick auf den Relay Ordner im Project Navigator
* New Group, wähle als Name "Tinkerforge"
* Rechtsklick auf die neue Tinkerforge Group
* Add Files to "Relay"...
* Wähle alle Dateien aus dem ``bindings`` Ordner der C/C++ Bindings

Es folgt ein kleines Beispielprogramm zum Schalten eines Relays per Knopfdruck.

Bearbeite ``AppDelegate.h`` so wie unten gezeigt: füge zwei neue Variablen
für die IPConnection und das DualRelay Objekt und die ``toggleRelays`` Interface
Builder Action hinzu.

.. code-block:: objc

 #import <UIKit/UIKit.h>
 #include "ip_connection.h"
 #include "bricklet_dual_relay.h"

 @interface AppDelegate : UIResponder <UIApplicationDelegate>
 {
     IPConnection ipcon;
     DualRelay dr;
 }

 @property (strong, nonatomic) UIWindow *window;

 - (IBAction)toggleRelays;

 @end


Bearbeite ``AppDelegate.m`` so wie unten gezeigt: erzeuge das IPConnection und
DualRelay Objekt nachdem die App gestartet ist. Der Einfachheit halber haben wir
im Beispiel auf Fehlerbehandlung verzichtet. In der ``toggleRelays`` Action wird
der Zustand beider Relais umgeschaltet.

.. code-block:: objc

 #import "AppDelegate.h"

 @implementation AppDelegate

 @synthesize window = _window;

 - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
 {
     // Change to the IP address of your host
     ipcon_create(&ipcon);
     dual_relay_create(&dr, "a27", &ipcon); // Change to your UID
     ipcon_connect(&ipcon, "192.168.178.46", 4223);
     dual_relay_set_state(&dr, true, true);

     return YES;
 }

 - (IBAction) toggleRelays
 {
     // Get state of both relays and toogle it
     bool state1, state2;
     dual_relay_get_state(&dr, &state1, &state2);
     dual_relay_set_state(&dr, !state1, !state2);
 }

 @end

Jetzt öffne das ``MainStoryboard.storyboard`` im Interface Builder und füge ein
Label und ein an/aus Switch Objekt hinzu wie es im Screenshot zu sehen ist. Der
letzte Schritt is das Verbinden des *Value Changed* Events des Switches mit der
*toggleRelays* Action:

* Rechtsklicke auf den Switch
* Klicke auf den Kreis rechts vom Value Changed Event
* Ziehe eine Linie zum First Responder
* Wähle "toogleRelays" vom Action Menu

.. image:: /Images/Screenshots/ios_xcode_small.jpg
   :scale: 100 %
   :alt: Xcode example for C/C++ bindings in iOS
   :align: center
   :target: ../_images/Screenshots/ios_xcode.jpg

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Screenshots/ios_xcode_event1_small.jpg
       :scale: 100 %
       :alt: Xcode Beispiel für C/C++ Bindings in iOS, Event verbinden (Schritt 1)
       :align: center
       :target: ../_images/Screenshots/ios_xcode_event1.jpg

    - .. image:: /Images/Screenshots/ios_xcode_event2_small.jpg
       :scale: 100 %
       :alt: Xcode Beispiel für C/C++ Bindings in iOS, Event verbinden (Schritt 2)
       :align: center
       :target: ../_images/Screenshots/ios_xcode_event2.jpg

Die App kann mittles des Run Knopfes im Simulator getestet werden. Dabei ist
darauf zu achten UID und IP Adresse entsprechend des verwendeten Dual Relay
Bricklets und PCs abzuändern.


.. _api_bindings_csharp:

C#
^^

Die C# Bindings bestehen aus einer Bibliothek (.dll) für alle Tinkerforge Bricks
und Bricklets (``Tinkerforge.dll``), dem Quelltext der DLL (in ``source/``) und
allen verfügbaren C# Beispielen (in ``examples/``).

Die Bibliothek wurde mit dem folgenden Befehl erzeugt::

 gmcs /optimize /target:library /out:Tinkerforge.dll source/Tinkerforge/*.cs

Die Bibliothek hat keine weiteren Abhängigkeiten. Als Beispiel wird im Folgenden
das Konfigurationsbeispiel des Stepper Bricks kompiliert.

Dafür müssen zuerst die ``Tinkerforge.dll`` und die
``examples/Brick/Stepper/ExampleConfiguration.cs`` Datei in einen Ordern kopiert
werden::

 example_folder/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

In diesem Ordner kann jetzt ein C# Compiler mit den folgenden Parametern
aufgerufen werden (1. Windows und 2. Linux/Mac OS X (Mono))::

 1.) csc.exe       /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs
 2.) /usr/bin/gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

Alternativ können die Beispiele auch in einer C# Entwicklungsumgebung deiner
Wahl verwendet werden (wie Visual Studio oder Mono Develop).


.. _api_bindings_csharp_windows_phone:

C# (Windows Phone)
^^^^^^^^^^^^^^^^^^

**Voraussetzungen**: Windows Phone SDK 7.1 oder neuer

Für Windows Phone können die normalen :ref:`C# Bindings <api_bindings_csharp>`
verwendet werden. Die asynchronen Sockets die Windows Phone benötigt werden von
Mono im Moment nicht unterstützt. Da die ``Tinkerforge.dll`` für Kompatibilität
mit C# 2.0 und Mono kompiliert wird ist sie nicht kompatible mit Windows Phone.
Um dieses Problem zu umgehen haben wir eine asynchronen Socket Implementierung
hinzugefügt, die nur verwendet wird wenn der Quelltext für Windows Phone
kompiliert wird (``#if WINDOWS_PHONE``). Dies bedeutet, dass der
``Tinkerforge`` Ordner (im ``source/`` Ordner der C# Bindings) als externe
Ressource eingebunden werden musst, damit die Bindings für Windows Phone mit kompiliert
werden. Die gesamten C# Bindings funktionieren mit Windows Phone SDK >= 7.1
(SDK 7.0 unterstützt keine Sockets und kann daher nicht verwendet werden um zum
Brick Daemon eine Netzwerkverbindung aufzubauen).

Im Folgenden wird angenommen, dass  Visual Studio für Windows Phone bereits
installiert ist. Als Beispiel soll ein kleines Projekt zum Schalten eines
Dual Relay Bricklets erstellt werden. Es sollte leicht sein dieses Beispiel
für deine Zwecke weiterzuentwickeln.

Starte ein neues Projekt in Visual Studio für Windows Phone:

* File
* New Project...
* Wähle "Visual C#"
* Wähle "Windows Phone Application"
* Wähle einen Namen (e.g. Relay)
* Klicke OK
* Wähle als Target "Windows Phone OS 7.1"
* Klicke OK

* Rechtsklick auf das Projekt im Solution Explorer
* Add
* New Folder, wähle "Tinkerforge" als Name
* Rechtsklick auf Tinkerforge
* Add
* Existing Item, wähle alle Dateien aus dem ``source/Tinkerforge/`` Ordner der
  C# Bindings (ausgenommen ``AssemblyInfo.cs``)

Bearbeite ``MainPage.xaml`` um einen Umschaltknopf hinzuzufügen:

.. code-block:: xml

 <phone:PhoneApplicationPage
     x:Class="Relay.MainPage"
     xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
     xmlns:phone="clr-namespace:Microsoft.Phone.Controls;assembly=Microsoft.Phone"
     xmlns:shell="clr-namespace:Microsoft.Phone.Shell;assembly=Microsoft.Phone"
     xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
     xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
     mc:Ignorable="d" d:DesignWidth="480" d:DesignHeight="768"
     FontFamily="{StaticResource PhoneFontFamilyNormal}"
     FontSize="{StaticResource PhoneFontSizeNormal}"
     Foreground="{StaticResource PhoneForegroundBrush}"
     SupportedOrientations="Portrait" Orientation="Portrait"
     shell:SystemTray.IsVisible="True">

     <Grid x:Name="LayoutRoot" Background="Transparent">
         <ToggleButton Name="RelaySwitch" Content="Change relay state"
             Checked="RelaySwitch_Checked" Unchecked="RelaySwitch_Unchecked" />
     </Grid>
 </phone:PhoneApplicationPage>

Doppelklick auf den Umschaltknopf um die ``MainPage.xaml.cs`` zu bearbeiten:

.. code-block:: csharp

 using System.Windows.Media;
 using System.Windows.Media.Animation;
 using System.Windows.Shapes;
 using Microsoft.Phone.Controls;

 using Tinkerforge;

 namespace Relay
 {
     public partial class MainPage : PhoneApplicationPage
     {
         // Change to the IP address of your host
         private static string HOST = "192.168.178.35";
         private static int PORT = 4223;
         private static string UID = "batti"; // Change to your UID
         private BrickletDualRelay relay;

         public MainPage()
         {
             IPConnection ipcon = new IPConnection();
             relay = new BrickletDualRelay(UID, ipcon);
             ipcon.Connect(HOST, PORT);

             InitializeComponent();
         }

         private void RelaySwitch_Checked(object sender, RoutedEventArgs e)
         {
             relay.SetState(true, false);
         }

         private void RelaySwitch_Unchecked(object sender, RoutedEventArgs e)
         {
             relay.SetState(false, false);
         }
     }
 }

Der Emulator kann über F5 gestartet werden. Das Relais sollte jetzt mit dem
Umschaltknopf auf dem Windows Phone Bildschirm umgeschaltet werden können.
Dabei ist darauf zu achten UID und IP Adresse entsprechend des verwendeten Dual
Relay Bricklets und PCs abzuändern.


.. _api_bindings_delphi:

Delphi
^^^^^^

**Voraussetzungen**: Delphi 2007 oder neuer, oder Lazarus (Free Pascal Compiler
2.4 oder neuer), andere Delphi oder Object Pascal Compiler sollten auch
funktionieren

Die Delphi Bindings bestehen aus den Bindings für alle Tinkerforge Bricks und
Bricklets (in ``bindings/``) und allen verfügbaren Delphi Beispielen (in
``examples/``).

Um die Delphi Bindings einfach zu halten haben sie nur externe Abhängigkeiten,
die möglichst überall verfügbar sind, wodurch sie leicht in jegliches Projekt
eingebunden werden können. Wir bieten keine vorkompilierte Bibliothek an, da
dies zu viel Aufwand wäre alle möglichen Kombinationen von Architekturen und
Betriebssystem zu versorgen. Die Bindings sollten aber auf den meisten
Architekturen (ARM, x86, etc.) und den meisten Betriebssystemen (Windows und
POSIX Systeme, wie Linux und Mac OS X, usw.) lauffähig sein.

Lazarus
"""""""

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit dem Free
Pascal Compiler (FPC) den Lazarus verwendet unter Linux kompilieren. Dafür
müssen die IP Connection (``Base58.pas``, ``BlockingQueue.pas``, ``Device.pas``,
``IPConnection.pas``, ``LEConverter.pas`` und ``TimedSemaphore.pas``) und die
Stepper Brick Bindings (``BrickStepper.pas``) vom ``bindings/`` Ordner sowie
``ExampleConfiguration.pas`` vom ``examples/Brick/Stepper/`` Ordner in ein
Projektordner kopiert werden::

 project_folder/
  -> Base58.pas
  -> BlockingQueue.pas
  -> Device.pas
  -> IPConnection.pas
  -> LEConverter.pas
  -> TimedSemaphore.pas
  -> BrickStepper.pas
  -> ExampleConfiguration.pas

FPC findet die verwendeten Units, dadurch sieht der Befehl für die Kompilierung
des Beispiels mit FPC wie folgt aus::

 fpc ExampleConfiguration.pas

Mit Lazarus kann der ``project_folder/`` so verwendet werden:

* Project
* New Project from file ...
* Wähle ``project_folder/ExampleConfiguration.pas``
* Klicke Open
* Wähle "Console Application"
* Klicke OK
* Wähle einen "Application Class Name" und "Title"
* Klicke OK

Delphi
""""""

Mit Delphi XE2 (ältere Delphiversion sollten ähnlich funktionieren) kann der
``project_folder/`` wie folgt verwendet werden. Zuerst muss
``ExampleConfiguration.pas`` in ``ExampleConfiguration.dpr`` umbenannt werden
dann bleiben noch diese Schritte:

* Project
* Add Existing Project...
* Choose ``project_folder/ExampleConfiguration.dpr``
* Klicke Open


.. _api_bindings_java:

Java
^^^^

**Voraussetzungen**: Java 1.5 oder neuer

Die Java Bindings bestehen aus einer Bibliothek (.jar) für alle Tinkerforge
Bricks und Bricklets (``Tinkerforge.jar``), dem Quelltext des JAR (in
``source/``) und allen verfügbaren Java Beispielen (in ``examples/``).

Die Bibliothek hat keine weiteren Abhängigkeiten. Als Beispiel wird im Folgenden
das Konfigurationsbeispiel des Stepper Bricks kompiliert.

Dafür müssen zuerst die ``Tinkerforge.jar`` und die
``examples/Brick/Stepper/ExampleConfiguration.java`` Datei in einen Ordern
kopiert werden::

 example_folder/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

In diesem Ordner kann jetzt der Java Compiler mit den folgenden Parametern
aufgerufen werden (1. Windows und 2. Linux/Mac OS X)::

 1.) javac -cp Tinkerforge.jar;. ExampleConfiguration.java
 2.) javac -cp Tinkerforge.jar:. ExampleConfiguration.java

Und ausgeführt wird es mit dem folgenden Befehl (1. Windows and 2. Linux/Mac OS X)::

 1.) java -cp Tinkerforge.jar;. ExampleConfiguration
 2.) java -cp Tinkerforge.jar:. ExampleConfiguration

.. note::
  Der Unterschied zwischen 1. und 2. ist Semikolon vs Doppelpunkt

Alternativ können die Beispiele auch in einer Java Entwicklungsumgebung deiner
Wahl verwendet werden (wie Eclipse oder NetBeans).


.. _api_bindings_java_android:

Java (Android)
^^^^^^^^^^^^^^

Für Android können die normalen :ref:`Java Bindings <api_bindings_java>`
verwendet werden.

Im Folgenden wird angenommen, dass die Android Entwicklungsumgebung schon
installiert ist. Für Androidanfänger empfehlen wir zuerst mit dem
`Hello World Tutorial
<http://developer.android.com/resources/tutorials/hello-world.html>`__ von
Google zu beginnen.

Als Beispiel soll ein kleines Projekt zum Schalten eines Dual Relay Bricklets
erstellt werden. Es sollte leicht sein dieses Beispiel für deine Zwecke
weiterzuentwickeln.

Starte eine neues Android Projekt:

* File
* New
* Project...
* Android Project
* Wähle "Name" (e.g. ``relay``)
* Wähle "Target"
* Wähle "Package Name" (e.g. ``org.example``)
* Klicke Finish

Als nächstes muss der gesamte ``com/tinkerforge/`` Ordner von ``source/`` in
den ``PROJECTFOLDER/src/`` Ordner kopiert werden.

Bearbeite den Quelltext wie unten dargestellt. Vergiss nicht die Host IP
Adresse zu der des PCs auf dem der Brick Daemon äuft zu ändern. Dies kann die
lokale oder die IP Adresse für die Verbindung zum Internet sein. Für letztere
musst auch noch sichergestellt werden, dass der Port des Brick Daemons von außen
erreichbar ist.

Es folgt der Quelltext eines Beispielprogramms, dass ein Dual Relay Bricklet
mit einem Umschaltknopf steuern kann.

.. code-block:: java

 package org.example;

 import android.app.Activity;
 import android.os.Bundle;
 import android.view.View;
 import android.view.View.OnClickListener;
 import android.widget.ToggleButton;

 import com.tinkerforge.BrickletDualRelay;
 import com.tinkerforge.IPConnection;

 public class RelayActivity extends Activity {
     // Change to the IP address of your host
     private static final String host = "192.168.178.35";
     private static final int port = 4223;
     private static final String UID = "Axb";
     private IPConnection ipcon;
     private BrickletDualRelay dr;
     private ToggleButton tb;

     @Override
     public void onCreate(Bundle savedInstanceState) {
         super.onCreate(savedInstanceState);

         try {
             ipcon = new IPConnection();
             dr = new BrickletDualRelay(UID, ipcon);
             ipcon.connect(host, port);
         } catch(Exception e) {
             // Here you might want to give the user a retry button.
             return;
         }

         tb = new ToggleButton(this);
         tb.setOnClickListener(new OnClickListener() {
             public void onClick(View v) {
                 if(tb.isChecked()) {
                     dr.setState(true, false);
                 } else {
                     dr.setState(false, false);
                 }
             }
         });

         setContentView(tb);
     }
 }

Deine App braucht noch Internet Permission (um sich mit dem Netzwerk verbinden
zu dürfen). Füge dazu folgende Zeile:

.. code-block:: xml

 <uses-permission android:name="android.permission.INTERNET" />

zum ``AndroidManifest.xml`` auf der Ebene wie der ``<application>`` Tag hinzu.

Deine app sollte jetzt wie in diesem Bild aussehen:

.. image:: /Images/Screenshots/android_eclipse_small.jpg
   :scale: 100 %
   :alt: Eclipse Konfiguration für Java Bindings in Android
   :align: center
   :target: ../_images/Screenshots/android_eclipse.jpg

Die App kann nun im Simulator getestet werden:

* Run
* Run
* Android Application

.. note::
  Diese Beispiel ruft potentiell blockierende Methoden auf dem UI Thread auf,
  zum Beispiel ``new IPConnection`` und ``setState``. Davon wird im Allgemeinen
  abgeraten, da es zum Hängen des UIs führen kann. Um dies zu vermeiden sollte
  die Kommunikation über die IPConnection in einen extra Thread ausgelagert
  werden, zum Beispiel mit Hilfe eines ``AsyncTask``.

  Seit Android 4.2 führt der Aufruf von ``new IPConnection`` auf dem UI Thread
  zu einer ``andriod.os.NetworkOnMainThreadException``. Siehe diese
  `StackOverflow Frage <http://stackoverflow.com/questions/6343166/android-os-networkonmainthreadexception>`__
  für weitere Informationen.


.. _api_bindings_php:

PHP
^^^

**Voraussetzungen**: PHP 5.3 oder neuer mit bcmath Erweiterung

Die PHP Bindings bestehen aus einem PEAR Paket mit den Bindings für alle
Tinkerforge Bricks und Bricklets (``Tinkerforge.tgz``), dem Quelltext des PEAR
Pakets (in ``source/``) und allen verfügbaren PHP Beispielen (in ``examples/``).

Das PEAR Paket kann mit Hilfe des pear Tools installiert werden::

 pear install Tinkerforge.tgz

Danach können alle Beispiel unverändert verwendet werden.

Wenn das PEAR Paket nicht verwendet werden soll oder kann, dann kann der
Quelltext auch direkt verwendet werden. Dafür muss der ``Tinkerforge`` Ordner vom
``source/`` Ordner und das Beispiel, das ausprobiert werden soll (z.B. das
Stepper Konfigurationsbeispiel
``examples/brick/stepper/ExampleConfiguration.php``), in einen Ordner kopiert
werden::

 example_folder/
  -> Tinkerforge/
  -> ExampleConfiguration.php

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopieren werden. Das Stepper Brick
Beispiel benötigt ``IPConnection.php`` und ``BrickStepper.php``::

 example_folder/
  -> IPConnection.php
  -> BrickStepper.php
  -> ExampleConfiguration.php

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``Tinkerforge``
Ordner aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: php

 <?php
 require_once('Tinkerforge/IPConnection.php');
 require_once('Tinkerforge/BrickStepper.php');
 ...
 ?>

muss dort nun dies stehen:

.. code-block:: php

 <?php
 require_once('IPConnection.php');
 require_once('BrickStepper.php');
 ...
 ?>

Jetzt kann das Beispiel wieder ausgeführt werden.


.. _api_bindings_python:

Python
^^^^^^

**Voraussetzungen**: Python 2.5 oder neuer, Python 3 wird auch unterstützt

Die Python Bindings bestehen aus einem Python egg mit den Bindings für alle
Tinkerforge Bricks und Bricklets (``tinkerforge.egg``), dem Quelltext des eggs
(in ``source/``) und allen verfügbaren Python Beispielen (in ``examples/``).

Das egg kann mit Hilfe von easy_install installiert werden::

 easy_install tinkerforge.egg

Danach können alle Beispiel unverändert verwendet werden.

Wenn das egg nicht verwenden werden soll oder kann, dann kann der Quelltext
auch direkt verwendet werden. Dafür muss der ``tinkerforge`` Ordner
vom ``source/`` Ordner und das Beispiel, das ausprobiert werden soll (z.B. das
Stepper Konfigurationsbeispiel
``examples/brick/stepper/example_configuration.py``), in einen Ordner kopiert
werden::

 example_folder/
  -> tinkerforge/
  -> example_configuration.py

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopiert werden. Das Stepper Brick
Beispiel benötigt ``ip_connection.py`` und ``brick_stepper.py``::

 example_folder/
  -> ip_connection.py
  -> brick_stepper.py
  -> example_configuration.py

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``tinkerforge``
Package aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: python

 from tinkerforge.ip_connection import IPConnection
 from tinkerforge.brick_stepper import Stepper

muss dort nun dies stehen:

.. code-block:: python

 from ip_connection import IPConnection
 from brick_stepper import Stepper

Jetzt kann das Beispiel wieder ausgeführt werden.

.. note::
 Windows Installationshinweis:

 * Installiere easy_install: http://pypi.python.org/pypi/setuptools#windows (setuptools)
 * Öffne eine Eingabeaufforderung
 * Führe ``C:\\YourPythonDir\\Scripts\\easy_install.exe C:\\PathToEgg\\tinkerforge.egg`` aus


.. _api_bindings_ruby:

Ruby
^^^^

**Voraussetzungen**: Ruby 1.9 oder neuer


Die Python Bindings bestehen aus einem Ruby GEM mit den Bindings für alle
Tinkerforge Bricks und Bricklets (``tinkerforge.gem``), dem Quelltext des GEMs
(in ``source/``) und allen verfügbaren Ruby Beispielen (in ``examples/``).

Der GEM kann mit Hilfe des gem Tools installiert werden::

 gem install tinkerforge.gem

Danach können alle Beispiel unverändert verwendet werden.

Wenn der GEM nicht verwendet werden soll oder kann, dann kann der Quelltext auch
direkt verwendet werden. Dafür muss der ``tinkerforge`` Ordner vom ``source/``
Ordner und das Beispiel, das ausprobiert werden soll (z.B. das Stepper
Konfigurationsbeispiel ``examples/brick/stepper/example_configuration.rb``),
in einen Ordner kopiert werden::

 example_folder/
  -> tinkerforge/
  -> example_configuration.rb

Damit Ruby das ``tinkerforge`` findet muss es per ``-I.`` Option angewiesen
werden im aktuelle Ordner danach zu schauen::

 ruby -I. example_configuration.rb

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopiert werden. Das Stepper Brick
Beispiel benötigt ``ip_connection.rb`` und ``brick_stepper.rb``::

 example_folder/
  -> ip_connection.rb
  -> brick_stepper.rb
  -> example_configuration.rb

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``tinkerforge``
Package aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: ruby

 require 'tinkerforge/ip_connection'
 require 'tinkerforge/brick_stepper'

muss dort nun dies stehen:

.. code-block:: ruby

 require 'ip_connection'
 require 'brick_stepper'

Jetzt kann das Beispiel wieder ausgeführt werden.
