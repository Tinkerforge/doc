
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C/C++ (iOS) - API Bindings

.. _api_bindings_c_ios:

C/C++ (iOS) - API Bindings
==========================

Objective-C is compatible to C. This allows to use the :ref:`C/C++ bindings
<api_bindings_c>` in an iOS App.

In the following we assume that you already have the iOS development environment
installed.


Testing an Example
------------------

As an example we will create a small project that can toggle a Dual Relay
Bricklet. It should be easy to adjust this example for your needs.

Start a new Xcode project by clicking on:

* File
* New
* Project...
* Choose "iOS Application"
* Choose "Single View Application"
* Click Next
* Choose a "Product Name" (e.g. Relay)
* Click Next
* Choose a "Folder" for the project
* Click Create

Add the C/C++ bindings code:

* Right click on the Relay folder in the Project navigator
* New Group, choose name "Tinkerforge"
* Right click on new Tinkerforge group
* Add Files to "Relay"...
* Choose all files from the ``bindings`` folder of the C/C++ bindings

Below is a small example program that turns a relay on and off with a toggle button.

Edit ``AppDelegate.h`` as shown below and add the two variables for the IPConnection
and DualRelay objects and the ``toggleRelays`` Interface Builder action.

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

Edit ``AppDelegate.m`` as shown below to create the IPConnection and DualRelay
objects after the App is launched. For simplicity no error handling is done here.
In the ``toggleRelays`` action the state of both relays is switched.

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

Now open ``MainStoryboard.storyboard`` in the Interface Builder and add a Label and
a on/off Switch object as shown in the screenshot. The last step is to connect the
Switch *Value Changed* event with the *toggleRelays* action:

* Right click on the Switch
* Click on the circle right of the Value Changed event
* Drag a line to the First Responder
* Choose *toogleRelays* from the action menu

.. image:: /Images/Screenshots/ios_xcode_small.jpg
   :scale: 100 %
   :alt: Xcode example for C/C++ bindings in iOS
   :align: center
   :target: ../_images/Screenshots/ios_xcode.jpg

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Screenshots/ios_xcode_event1_small.jpg
       :scale: 100 %
       :alt: Xcode example for C/C++ bindings in iOS, connect event (step 1)
       :align: center
       :target: ../_images/Screenshots/ios_xcode_event1.jpg

    - .. image:: /Images/Screenshots/ios_xcode_event2_small.jpg
       :scale: 100 %
       :alt: Xcode example for C/C++ bindings in iOS, connect event (step 2)
       :align: center
       :target: ../_images/Screenshots/ios_xcode_event2.jpg

Test the App in the simulator by clicking the Run button. Don't forget to change
the UID and the host IP address to the correct values for your brickd host and
your Dual Relay Bricklet.


More Examples and Projects
--------------------------

All the small examples contained in the ZIP file of the bindings can also be
found in the API documentation of the :ref:`Bricks <product_overview_bricks>` and
:ref:`Bricklets <product_overview_bricklets>`.

Further project descriptions can be found in the :ref:`kits <index_kits>` section.

.. FIXME: add a list with direct links here
