
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../Software.html">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C/C++ - API Bindings

.. _api_bindings_c_ios:

C/C++ (iOS) - API Bindings
==========================

Objective-C ist kompatible zu C. Dies erlaubt es uns die :ref:`C/C++ Bindings
<api_bindings_c>` in einer iOS App zu verwenden.

Im Folgenden wird angenommen, dass die iOS Entwicklungsumgebung schon
installiert ist.


Test eines Beispiels
--------------------

Als Beispiel soll ein kleines Projekt zum Schalten eines
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

Die App kann mittels des Run Knopfes im Simulator getestet werden. Dabei ist
darauf zu achten UID und IP Adresse entsprechend des verwendeten Dual Relay
Bricklets und PCs abzuändern.
