.. _api_bindings:

API Bindings
============

API bindings establish a TCP/IP connection to the
:ref:`Brick Daemon <brickd>`. Each function call creates a TCP/IP packet that
is send over the Brick Daemon to the Brick. Incoming TCP/IP packets
are routed back to the caller.

See also our :ref:`tutorial` for more information on how everything works
together.


IP Connection
-------------

The IP Connection creates a TCP/IP connection between the
:ref:`Brick Daemon <brickd>` and the corresponding programming language
API bindings.

It is used by the bindings and implemented for each programming language.
The corresponding documentation can be found here:

.. include:: API_Bindings_bindings.table


Using the Bindings
------------------

The latest versions of the bindings can be found on the
:ref:`download page <downloads_bindings_examples>`.

.. _api_bindings_c:

C/C++
^^^^^

The C/C++ bindings consist of the bindings for all Tinkerforge Bricks and
Bricklets (in bindings/) and all available C/C++ examples (in
examples/).

To keep the C/C++ bindings stupid and simple, they only have
dependencies that are available nearly everywhere, thus making it
possible to compile into any project hassle-free.
We do not offer a pre-compiled library, since it would be a
pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the
bindings should work on most architectures (ARM, x86, etc.) and on most
operating systems (Windows and POSIX systems, such as Linux and Mac OS, etc.).

As an example we will compile the Stepper Brick configuration example
with gcc on Windows and Linux.
For that we have to copy the IP connection and the Stepper Brick
bindings (ip_connection.h, ip_connection.c, brick_stepper.c and
brick_stepper.h) from the bindings/ folder as well as the
example_configuration.c from the examples/brick/stepper/ folder into our
project::

 project_folder/
  -> ip_connection.c
  -> ip_connection.h
  -> brick_stepper.c
  -> brick_stepper.h
  -> example_configuration.c

The only dependency on Unix-like systems is pthread, therefore a
compilation of the project with gcc on Linux looks like::

 gcc -pthread -o example_configuration brick_stepper.c ip_connection.c example_configuration.c

On Windows Winsock2 is used for threading. Under MinGW we can compile the example as
following (hint: the library linking must come after the source)::

 gcc -o example_configuration.exe brick_stepper.c ip_connection.c example_configuration.c -lws2_32

With Visual Studio we can use our project_folder/ as follows:

* File
* New
* Project From Existing Code
* Type: Visual C++
* Choose project_folder/
* Choose project name
* Next
* Choose Console Application
* Finish

Now we have to tell Visual Studio to use the C++ compiler, since we
would need C99 but Visual Studio can only compile C89... Also we have to
include ws2_32.lib by clicking on:

* Project
* Properties
* C/C++
* Advanced, option "Compile as"
* Choose "Compile as C++ Code (/TP)"

* Project
* Properties
* Linker
* Input, option "Additional Dependencies"
* Add "ws2_32.lib;"

Thats it, we are ready to go!

The Visual Studio compiler can also be used from the command line::

 cl /TP /I. brick_stepper.c ip_connection.c example_configuration.c /link /out:example_configuration.exe ws2_32.lib


.. _api_bindings_c_ios:

C/C++ (iOS)
^^^^^^^^^^^

Objective-C is compatible to C. This allows to use the C/C++ bindings
(see :ref:`above <api_bindings_c>`) in an iOS App.

In the following we assume that you already have the iOS development environment
installed.

As an example we will create a small project that can toggle a relay. It
should be easy to adjust this example for your needs.

Start a new Xcode project by clicking on:

* File
* New
* Project...
* Choose iOS Application
* Choose Single View Application
* Click Next
* Choose Product Name (e.g. Relay)
* Click Next
* Choose a Folder for the project
* Click Create

Add the C/C++ bindings code:

* Right click on the Relay folder in the Project navigator
* New Group, choose name Tinkerforge
* Right click on new Tinkerforge group
* Add Files to "Relay"...
* Choose all files from the bindings folder of the C/C++ bindings

Below is a small example program that turns a relay on and off with a toggle button.

Edit AppDelegate.h as shown below and add the two variables for the IPConnection
and DualRelay objects and the toggleRelays Interface Builder action.

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


Edit AppDelegate.m as shown below to create the IPConnection and DualRelay
objects after the App is launched. For simplicity no error handling is done here.
In the toggleRelays action the state of both relays is switched.

.. code-block:: objc

 #import "AppDelegate.h"

 @implementation AppDelegate

 @synthesize window = _window;

 - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
 {
     // Change to the IP address of your host
     ipcon_create(&ipcon, "192.168.178.46", 4223);
     dual_relay_create(&dr, "927");
     ipcon_add_device(&ipcon, &dr);
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

Now open MainStoryboard.storyboard in the Interface Builder and add a Label and
a on/off Switch object as shown in the screenshot. The last step is to connect the
Switch *Value Changed* event with the *toggleRelays* action:

* Right click on the Switch
* Click on the circle right of the Value Changed event
* Drag a line to the First Responder
* Choose toogleRelays from the action menu

.. image:: /Images/Screenshots/ios_xcode_small.jpg
   :scale: 100 %
   :alt: Xcode example for C/C++ bindings in iOS
   :align: center
   :target: ../_images/Screenshots/ios_xcode.jpg

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Screenshots/ios_xcode_event1_small.jpg
       :scale: 100 %
       :alt: Xcode example for C/C++ bindings in iOS, connect event, step 1
       :align: center
       :target: ../_images/Screenshots/ios_xcode_event1.jpg

    - .. image:: /Images/Screenshots/ios_xcode_event2_small.jpg
       :scale: 100 %
       :alt: Xcode example for C/C++ bindings in iOS, connect event, step 2
       :align: center
       :target: ../_images/Screenshots/ios_xcode_event2.jpg

Test the App in the simulator by clicking the Run button.


.. _api_bindings_csharp:

C#
^^

The C# bindings consist of a library for all Tinkerforge Bricks and Bricklets
(Tinkerforge.dll), the source of the DLL (in source/) and all available
C# examples (in examples/).

The library has been compiled with::

 gmcs /optimize /target:library /out:Tinkerforge.dll source/Tinkerforge/*.cs

The library can be used without any further extensions. As an example
lets compile the configuration example of the Stepper Brick.

For this we create a folder and copy the Tinkerforge.dll and the
examples/Brick/Stepper/ExampleConfiguration.cs into this folder::

 example_folder/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

In this folder we can now call the c# compiler with the following parameters
(1. Windows and 2. Linux/Mac OS (Mono))::

 1.) csc.exe       /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs
 2.) /usr/bin/gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

Or, alternatively add the DLL and the Example in an C# IDE of your choice
(such as Visual Studio or Mono Develop).

Documentation for the API can be found :ref:`here <index_bricks>`.

.. _api_bindings_csharp_windows_phone:


C# (Windows Phone)
^^^^^^^^^^^^^^^^^^

**Requirements**: Windows Phone SDK 7.1 or newer

For Windows Phone the normal C# bindings can be used
(see :ref:`above <api_bindings_csharp>`). The asynchronous sockets that
are needed for Windows Phone are currently not supported in Mono. Since
the DLL is build to be compatible with C# 2.0 and Mono, the DLL is not
compatible with Windows Phone. To overcome this we have added asynchronous
sockets for Windows Phone with *#if WINDOWS_PHONE* directives in the socket
code. This means you can add the Tinkerforge folder (from the source/ folder
in the C# bindings) as an external resource. The complete C# API bindings
work with Windows Phone SDK >= 7.1 (SDK 7.0 does not support sockets
and can thus not be used to interface with brickd).

In the following we assume that you already have Visual Studio for Windows
Phone installed. As an example we will create a small project that can toggle
a relay. It should be easy to adjust this example for your needs.

Start a new project by clicking on:

* File
* New Project...
* Choose Visual C#
* Choose Windows Phone Application
* Choose Name (e.g. Relay)
* Click OK
* Choose Target Windows Phone OS 7.1
* Click OK

* Right click on project in Solution Explorer
* Add
* New Folder, choose name Tinkerforge
* Right click on Tinkerforge
* Add
* Existing Item, choose all files from source/Tinkerforge/ folder of C# bindings (excluding AssemblyInfo.cs)

Edit the MainPage.xaml to add a toggle button:

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

Double click on the toggle button to edit the MainPage.xaml.cs:

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
             IPConnection ipcon = new IPConnection(HOST, PORT);
             relay = new BrickletDualRelay(UID);
             ipcon.AddDevice(relay);

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

Start the emulator with F5. You should be able to toggle a relay with
the toggle button on your Windows Phone. Don't forget to change the
UID and the host IP address to the correct values for your brickd host and
your Relay Bricklet.

.. _api_bindings_delphi:

Delphi
^^^^^^

**Requirements**: Delphi 2007 or newer, or Lazarus (Free Pascal Compiler 2.4
or newer), other Delphi or Object Pascal compilers might work as well

The Delphi bindings consist of the bindings for all Tinkerforge Bricks and
Bricklets (in bindings/) and all available Delphi examples (in
examples/).

To keep the Delphi bindings stupid and simple, they only have dependencies that
are available nearly everywhere, thus making it possible to compile into any
project hassle-free. We do not offer a pre-compiled library, since it would be
a pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the bindings should work on most architectures
(ARM, x86, etc.) and on most operating systems (Windows and POSIX systems such
as Linux and Mac OS, etc.).

As an example we will compile the Stepper Brick configuration example with
the Free Pascal Compiler (FPC) that comes with the Lazarus. For that we
have to copy the IP Connection (Base58.pas, BlockingQueue.pas, Device.pas,
IPConnection.pas, LEConverter.pas and TimedSemaphore.pas) and the Stepper
Brick bindings (BrickStepper.pas) from the bindings/ folder as well as the
ExampleConfiguration.pas from the examples/Brick/Stepper/ folder into our
project::

 project_folder/
  -> Base58.pas
  -> BlockingQueue.pas
  -> Device.pas
  -> IPConnection.pas
  -> LEConverter.pas
  -> TimedSemaphore.pas
  -> BrickStepper.pas
  -> ExampleConfiguration.pas

FPC automatically finds the used units, therefore a compilation of the project
with FPC like::

 fpc ExampleConfiguration.pas

With Lazarus we can use our project_folder/ by clicking:

* Project
* New Project from file ...
* Choose project_folder/ExampleConfiguration.pas
* Open
* Choose Console Application
* OK
* Choose Application class name and Title
* OK

With Delphi XE2 (older Delphi version should work similar) we can use our
project_folder/ as follows. First rename ExampleConfiguration.pas to
ExampleConfiguration.dpr then click:

* Project
* Add Existing Project...
* Choose project_folder/ExampleConfiguration.dpr
* Open


.. _api_bindings_java:

Java
^^^^

The Java bindings consist of a library (.jar) for all Tinkerforge Bricks and
Bricklets (Tinkerforge.jar), the source of the jar (in source/) and all
available Java examples (in examples/).

The library can be used without any further extensions. As an example lets
compile the configuration example of the Stepper Brick.

For this we create a folder and copy the Tinkerforge.jar and the
examples/Brick/Stepper/ExampleConfiguration.java into this folder::

 example_folder/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

In this folder we can now call the Java compiler with the following
parameters (1. Windows and 2. Linux/Mac OS)::

 1.) javac -cp Tinkerforge.jar;. ExampleConfiguration.java
 2.) javac -cp Tinkerforge.jar:. ExampleConfiguration.java

and run it with the following parameters (1. Windows and 2. Linux/Mac OS)::

 1.) java -cp Tinkerforge.jar;. ExampleConfiguration
 2.) java -cp Tinkerforge.jar:. ExampleConfiguration

(Note: The difference is colon vs semicolon)

Or, alternatively add the jar and the Example in an Java IDE of your choice
(such as Eclipse or NetBeans).

Documentation for the API can be found :ref:`here <index_bricks>`.

.. _api_bindings_java_android:

Java (Android)
^^^^^^^^^^^^^^

For Android the normal Java bindings can be used
(see :ref:`above <api_bindings_java>`).

In the following we assume that you already have the Android development
environment installed. If you are just starting with Android development,
you should first complete the
`hello world tutorial
<http://developer.android.com/resources/tutorials/hello-world.html>`__ from Google.

As an example we will create a small project that can toggle
a relay. It should be easy to adjust this example for your needs.

Start a new project by clicking on:

* File
* New
* Project...
* Android Project
* Choose name (e.g. relay)
* Choose target
* Choose package name (e.g. org.example)
* Finish

Copy complete com/tinkerforge/ folder from source/ into PROJECTFOLDER/src/

Edit the source. Don't forget to set the host IP to the IP address of the
PC running brickd. You can use your local IP or the IP you are connected
to the Internet with. If you use the latter, you also have to make sure that
the brickd port is opened to the outside.

Below is a small example program that turns a relay on and off with a
toggle button.

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
     private BrickletDualRelay dr;
     private ToggleButton tb;

     @Override
     public void onCreate(Bundle savedInstanceState) {
         super.onCreate(savedInstanceState);
         IPConnection ipcon;

         try {
             ipcon = new IPConnection(host, port);
             dr = new BrickletDualRelay(UID);
             ipcon.addDevice(dr);
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


After that you have to add the Internet permission (to be able
to use the network):

.. code-block:: xml

 <uses-permission android:name="android.permission.INTERNET" />

to AndroidManifest.xml on the same level as the ``<application>`` tag.

Your application should now look as depicted below:

.. image:: /Images/Screenshots/android_eclipse_small.jpg
   :scale: 100 %
   :alt: Eclipse configuration for Java bindings in Android
   :align: center
   :target: ../_images/Screenshots/android_eclipse.jpg


Test in simulator by clicking:

* Run
* Run
* Android Application

.. _api_bindings_php:

PHP
^^^

**Requirements**: PHP 5.3 or newer with bcmath extension

The PHP bindings consist of a PEAR package with the bindings for all
Tinkerforge Bricks and Bricklets (Tinkerforge.tgz), the source of the
PEAR package (in source/) and all available PHP examples (in examples/).

You can install the PEAR package with the pear tool::

 pear install Tinkerforge.tgz

After that you can use the examples as they are.

If you can't or don't want to use the PEAR package, you can also use the source
directly, just create a folder for your project and copy the Tinkerforge
folder from source/ and the example you want to try in there
(e.g. the Stepper configuration example from
examples/brick/stepper/ExampleConfiguration.php)::

 example_folder/
  -> Tinkerforge/
  -> ExampleConfiguration.php

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need IPConnection.php and
BrickStepper.php. After copying these in the project folder::

 example_folder/
  -> IPConnection.php
  -> BrickStepper.php
  -> ExampleConfiguration.php

we have to remove the Tinkerforge directory from the examples, i.e. instead of::

 require_once('Tinkerforge/IPConnection.php');
 require_once('Tinkerforge/BrickStepper.php');

we use::

 require_once('IPConnection.php');
 require_once('BrickStepper.php');

After that, the example can be executed again.



.. _api_bindings_python:

Python
^^^^^^

**Requirements**: Python 2.6 or newer, Python 3 is also supported

The Python bindings consist of a Python egg with the bindings for all
Tinkerforge Bricks and Bricklets (tinkerforge.egg), the source of the
egg (in source/) and all available Python examples (in examples/).

You can install the egg with easy_install::

 easy_install tinkerforge.egg

After that you can use the examples as they are.

If you can't or don't want to use the egg, you can also use the source
directly, just create a folder for your project and copy the tinkerforge
folder from source/ and the example you want to try in there
(e.g. the Stepper configuration example from
examples/brick/stepper/example_configuration.py)::

 example_folder/
  -> tinkerforge/
  -> example_configuration.py

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need ip_connection.py and
stepper_brick.py. After copying these in the project folder::

 example_folder/
  -> ip_connection.py
  -> brick_stepper.py
  -> example_configuration.py

we have to remove the tinkerforge package from the examples, i.e. instead of::

 from tinkerforge.ip_connection
 from tinkerforge.brick_stepper

we use::

 from ip_connection
 from brick_stepper

After that, the example can be executed again.

.. note:: Windows installation hint

 * Install easy_install: http://pypi.python.org/pypi/setuptools#windows (setuptools)
 * Open Windows command shell
 * C:\\YourPythonDir\\Scripts\\easy_install.exe C:\\PathToEgg\\tinkerforge.egg



.. _api_bindings_ruby:

Ruby
^^^^

**Requirements**: Ruby 1.9 or newer

The Ruby bindings consist of a Ruby GEM with the bindings for all
Tinkerforge Bricks and Bricklets (tinkerforge.gem), the source of the
GEM (in source/) and all available Ruby examples (in examples/).

You can install the GEM with the gem tool::

 gem install tinkerforge.gem

After that you can use the examples as they are.

If you can't or don't want to use the GEM, you can also use the source
directly, just create a folder for your project and copy the tinkerforge
folder from source/ and the example you want to try in there
(e.g. the Stepper configuration example from
examples/brick/stepper/example_configuration.rb)::

 example_folder/
  -> tinkerforge/
  -> example_configuration.rb

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need ip_connection.rb and
stepper_brick.rb. After copying these in the project folder::

 example_folder/
  -> ip_connection.rb
  -> brick_stepper.rb
  -> example_configuration.rb

we have to remove the tinkerforge package from the examples, i.e. instead of::

 require 'tinkerforge/ip_connection'
 require 'tinkerforge/brick_stepper'

we use::

 require 'ip_connection'
 require 'brick_stepper'

After that, the example can be executed again.
