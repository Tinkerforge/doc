
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../Software.html">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C# (Windows Phone) - API Bindings

.. _api_bindings_csharp_windows_phone:

C# (Windows Phone) - API Bindings
=================================

**Requirements**: Windows Phone SDK 7.1 or newer

For Windows Phone the normal :ref:`C# bindings <api_bindings_csharp>` can be
used. The asynchronous sockets that are needed for Windows Phone are currently
not supported in Mono. Since the ``Tinkerforge.dll`` is build to be compatible
with C# 2.0 and Mono, the DLL is not
compatible with Windows Phone. To overcome this we have added asynchronous
sockets for Windows Phone with ``#if WINDOWS_PHONE`` directives in the socket
code. This means you can add the ``Tinkerforge`` folder (from the ``source/``
folder in the C# bindings) as an external resource. This makes Visual Studio
compile the bindings for Windows Phone. The complete C# bindings
work with Windows Phone SDK >= 7.1 (SDK 7.0 does not support sockets
and can thus not be used to interface with the Brick Daemon).

In the following we assume that you already have Visual Studio for Windows
Phone installed. As an example we will create a small project that can toggle
a Dual Relay Bricklet. It should be easy to adjust this example for your needs.

Start a new project by clicking on:

* File
* New Project...
* Choose "Visual C#"
* Choose "Windows Phone Application"
* Choose a name (e.g. Relay)
* Click OK
* Choose Target as "Windows Phone OS 7.1"
* Click OK

* Right click on the project in Solution Explorer
* Add
* New Folder, choose name "Tinkerforge"
* Right click on Tinkerforge
* Add
* Existing Item, choose all files from ``source/Tinkerforge/`` folder of C#
  bindings (excluding ``AssemblyInfo.cs``)

Edit the ``MainPage.xaml`` to add a toggle button:

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

Double click on the toggle button to edit the ``MainPage.xaml.cs``:

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

Start the emulator with F5. You should be able to toggle a relay with
the toggle button on your Windows Phone. Don't forget to change the
UID and the host IP address to the correct values for your brickd host and
your Dual Relay Bricklet.
