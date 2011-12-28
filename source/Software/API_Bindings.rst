.. _api_bindings:

API Bindings
============

API bindings establish a TCP connection to the 
:ref:`Brick Daemon <brickd>`. Each method call creates a TCP package that
is send over the Brick Daemon to the Brick. Incoming TCP packages
are routed back to the calling method.

See also our :ref:`tutorial` for more information on how everything works 
together.


IP Connection
-------------

The IPConnection creates a connection between the
:ref:`Brick Daemon <brickd>` and the corresponding programming language 
:ref:`API bindings<api_bindings>`. 

It is used by the bindings and implemented for each programming language.
The corresponding documentation can be found here:

* :ref:`Python <ipcon_brick_python>`
* :ref:`C/C++ <ipcon_brick_c>`
* :ref:`C# <ipcon_brick_csharp>`
* :ref:`Java <ipcon_brick_java>`

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
We do not offer a pre compiled lib, since it would be a
pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the
bindings should work on most architectures (arm, x86, etc.) and on most
operating systems (Windows and posix systems such as linux and Mac
OS, etc.).

As an example we will compile the Stepper Brick configuration example 
with gcc on Windows and linux.
For that we have to copy the IP Connection and the Stepper Brick
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
compilation of the project with gcc on linux looks like::

 gcc -lpthread -o example_configuration brick_stepper.c ip_connection.c example_configuration.c

On Windows Winsock2 is used for threading. Under MinGW we can compile the example as 
following (hint: the library linking must come after the source)::

 gcc -o example_configuration.exe brick_stepper.c ip_connection.c example_configuration.c -lws2_32

With Visual Studio we can use our project_folder/ as follows::

 File -> New -> Project From Existing Code -> Type: Visual C++ -> choose test_project, choose project name -> Next ->  choose Console Application -> Finish

Now we have to tell Visual Studio to use the C++ compiler, since we
would need C99 but Visual Studio can only compile C89... Also we have to
include ws2_32.lib::

 Project -> properties -> C/C++ -> Advanced and option "Compile as" -> choose "Compile as C++ Code (/TP)"
 Project -> properties -> Linker -> Additional Dependencies -> add "ws2_32.lib;"

Thats it, we are ready to go!


.. _api_bindings_csharp:

C#
^^

The C# bindings consist of a library for all Tinkerforge Bricks and Bricklets 
(Tinkerforge.dll), the source of the dll (in source/) and all available 
C# examples (in examples/).

The library has been compiled with::

 gmcs /optimize /target:library /out:Tinkerforge.dll source/Tinkerforge/*.cs

The library can be used without any further extensions. As an example 
lets compile the configuration example of the stepper brick.

For this we create a folder and copy the Tinkerforge.dll and the 
examples/Brick/Stepper/ExampleConfiguration.cs into this folder::

 example_folder/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

In this folder we can now call the c# compiler with the following parameters 
(1. Windows and 2. linux/Mac OS (mono))::

 1.) csc.exe       /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs
 2.) /usr/bin/gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs 

Or, alternatively add the dll and the Example in an C# IDE of your choice 
(such as Visual Studio or Mono Develop).

Documentation for the API can be found :ref:`here <index_bricks>`.

.. _api_bindings_csharp_windows_phone:

C# (Windows Phone)
^^^^^^^^^^^^^^^^^^

For Windows Phone the normal C# bindings can be used 
(see :ref:`above <api_bindings_csharp>`). The asynchronous sockets that 
are needed for Windows Phone are currently not supported in mono. Since
the DLL is build to be compatible with C# 2.0 and mono, the DLL is not
compatible with Windows Phone. To overcome this we have added asynchronous
sockets for Windows Phone with *#if WINDOWS_PHONE* directives in the socket 
code. This means you can add the Tinkerforge folder (from the source/ folder 
in the csharp bindings) as an external resource. The complete C# api bindings
work with Windows Phone SDK >= 7.1 (SDK 7.0 does not support sockets
and can thus not be used to interface with brickd).

In the following we assume that you already have visual studio for Windows
Phone installed. As an example we will create a small project that can toggle 
a relay. It should be easy to adjust this example for your needs.

Start a new project by clicking on:

* File
* New Project...
* Choose Visual C#
* Choose Windows Phone Application 
* Choose Name (e.g. Relay) 
* Press OK
* Choose Target Windows Phone OS 7.1 
* Press OK

* Right click on project in Solution Explorer 
* Add 
* New Folder, choose name Tinkerforge
* Right click on Tinkerforge 
* Add
* Existing Item, choose all files from source/Tinkerforge/ folder of csharp bindings

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
        <ToggleButton Name="RelaySwitch" Content="Change relay state" Checked="RelaySwitch_Checked" Unchecked="RelaySwitch_Unchecked"/>
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
        // Change host ip address to ip from brickd
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
the toggle button on your windows phone. Don't forget to change the
UID and the host IP address to the correct values for your brickd host and
your Relay Bricklet.

.. _api_bindings_java:

Java
^^^^

The java bindings consist of a library (.jar) for all Tinkerforge Bricks and 
Bricklets (Tinkerforge.jar), the source of the jar (in source/) and all 
available Java examples (in examples/).

The library can be used without any further extensions. As an example lets 
compile the configuration example of the stepper brick. 

For this we create a folder and copy the Tinkerforge.jar and the 
examples/Brick/Stepper/ExampleConfiguration.java into this folder::

 example_folder/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

In this folder we can now call the Java compiler with the following
parameters (1. Windows and 2. linux/Mac OS)::

 1.) javac -cp Tinkerforge.jar;. ExampleConfiguration.java 
 2.) javac -cp Tinkerforge.jar:. ExampleConfiguration.java

and run it with the following parameters (1. Windows and 2. linux/Mac OS)::

 1.) java -cp Tinkerforge.jar;. ExampleConfiguration (windows)
 2.) java -cp Tinkerforge.jar:. ExampleConfiguration (linux)

(Note: The difference is colon vs semicolon)

Or, alternatively add the jar and the Example in an Java IDE of your choice 
(such as Eclipse or NetBeans).

Documentation for the API can be found :ref:`here <index_bricks>`.

.. _api_bindings_java_android:

Java (Android)
^^^^^^^^^^^^^^
For Android the normal Java bindings can be used 
(see :ref:`above <api_bindings_java>`).

In the following we assume that you already have the android development
environment installed. If you are just starting with android development,
you should first complete the 
`hello world tutorial <http://developer.android.com/resources/tutorials/hello-world.html>`__ from google.

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
to the internet with. If you use the latter, you also have to make sure that
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
	private static final String host = new String("192.168.178.35");
	private static final int port = 4223;
	private static final String UID = new String("Axb");
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


After that you have to add the internet permssion (to be able
to use the network)::

 <uses-permission android:name="android.permission.INTERNET" /> 
 
to AndroidManifest.xml on the same level as the <application> tag.

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

.. _api_bindings_python:

Python
^^^^^^

The Python bindings consist of a Python egg with the bindings for all 
Tinkerforge Bricks and Bricklets (tinkerforge.egg), the source of the 
egg (in source/) and all available Python examples (in examples/).

You can install the egg with easy_install::

 easy_install tinkerforge.egg

After that you can use the examples as they are.

If you can't or don't want to use the egg, you can also use the source 
directly, just create a folder for your project and copy the tinkerforge 
folder from source/ and the example you want to try in there 
(e.g. the stepper configuration example from 
examples/brick/stepper/example_configuration.py)::

 example_folder/
  -> tinkerforge/
  -> example_configuration.py

If you just want to use a few Bricks or Bricklets and you don't want to 
have this many files in you project, you can also copy the files as they are
needed. For the stepper examples we need ip_connection.py and 
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
 * Open windows command shell
 * C:\\YourPythonDir\\Scripts\\easy_install.exe C:\\PathToEgg\\tinkerforge.egg
