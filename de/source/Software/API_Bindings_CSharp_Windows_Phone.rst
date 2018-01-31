
.. _api_bindings_csharp_windows_phone:

C# (Windows Phone) - API Bindings
=================================

**Voraussetzungen**: Windows Phone SDK 7.1 oder neuer

Für Windows Phone können die normalen :ref:`C# Bindings <api_bindings_csharp>`
verwendet werden. Allgemeine Informationen sind in der Beschreibung der C#
Bindings zu finden, diese Seite befasst sich nur mit Windows Phone spezifischen
Dingen.

Die asynchronen Sockets die Windows Phone benötigt werden von
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


Test eines Beispiels
--------------------

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
