
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Garagentor mit Windows Phone fernsteuern

.. |name| replace:: Windows Phone
.. |ref_CALLBACK_ENUMERATE| replace:: :csharp:func:`EnumerateCallback <IPConnection::EnumerateCallback>`
.. |ref_connect| replace:: :csharp:func:`Connect() <IPConnection::Connect>`
.. |connect| replace:: ``Connect()``
.. |set_monoflop| replace:: ``SetMonoflop(1 << 0, 1 << 0, 1500)``
.. |ref_get_identity| replace:: :csharp:func:`GetIdentity() <BrickletIndustrialQuadRelay::GetIdentity>`
.. |async_helper| replace:: ``BackgroundWorker``

.. include:: GarageControl.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_garage_control_windows_phone:

Garagentor mit Windows Phone fernsteuern
========================================

.. include:: WindowsPhoneCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: GarageControl.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Das vollständige Visual Studio Projekt kann `hier
<https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/windows_phone>`__
heruntergeladen werden. Eine Demo-App basierend auf diesem Projekt steht im
`Windows Phone Store <http://www.windowsphone.com/s?appid=4c9a8f61-d9ed-4fd2-b4e6-a332b617c596>`__
zur Verfügung.


Ziele
-----

.. include:: GarageControl.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Die GUI erstellen
----------------------------

Nach dem Erstellen eines neuen "Windows Phone App" namens "Garage Control" in
Visual Studio beginnen wir mit der Erstellung der GUI:

.. image:: /Images/Kits/hardware_hacking_garage_control_windows_phone_gui_350.jpg
   :scale: 100 %
   :alt: App GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_control_windows_phone_gui.jpg

An das bereits bestehende "LayoutRoot" Element wird ein "StackPanel" angehängt,
das dann alle weiteren GUI Elemente aufnehmen wird. Drei "TextBoxes" ermöglichen
die Eingabe von Host, Port und UID des Industrial Quad Relay Bricklets. Für die
Port Textbox wird das Attribut ``InputScope="Number"`` gesetzt, dadurch wird
Windows Phone den Inhalt dieser Textbox auf Zahlen beschränken. Unterhalb der
Textboxen folgt eine "ProgressBar" die einen laufenden Verbindungsversuch
anzeigen wird. Die letzten beiden Elemente sind die "Button" für den Aufbau und
das Trennen der Verbindung sowie das Auslösen eines Tastendrucks auf der
gehackten Fernbedienung. Hier ein Auszug aus der ``MainPage.xaml`` Datei:

.. code-block:: xml

    <phone:PhoneApplicationPage>
        <Grid x:Name="LayoutRoot" Background="Transparent">
            <!-- [...] -->

            <StackPanel x:Name="ContentPanel" Grid.Row="1" Margin="12,0,12,0">
                <TextBlock TextWrapping="Wrap" Text="Host" VerticalAlignment="Top"/>
                <TextBox x:Name="host" Height="72" TextWrapping="Wrap" Text="192.168.178.46" VerticalAlignment="Top"/>
                <TextBlock TextWrapping="Wrap" Text="Port" VerticalAlignment="Top"/>
                <TextBox x:Name="port" Height="72" TextWrapping="Wrap" Text="4223" VerticalAlignment="Top"
                         InputScope="Number"/>
                <TextBlock TextWrapping="Wrap" Text="UID (Industrial Quad Relay Bricklet)" VerticalAlignment="Top"/>
                <TextBox x:Name="uid" Height="72" TextWrapping="Wrap" Text="ctG" VerticalAlignment="Top"/>
                <ProgressBar x:Name="progress" Height="10" VerticalAlignment="Top"/>
                <Button x:Name="connect" Content="Connect" VerticalAlignment="Top" Click="Connect_Click"/>
                <Button x:Name="trigger" Content="Trigger" VerticalAlignment="Top" Height="144" Click="Trigger_Click"/>
            </StackPanel>
        </Grid>
    </phone:PhoneApplicationPage>

Damit ist das Layout des GUIs fertig. Die initiale Konfiguration des GUIs wird
im Konstruktor der ``MainPage`` Klasse vorgenommen. Die "ProgressBar" ist am
Anfang nicht sichtbar und Indeterminate Mode wird aktiviert, da die Dauer eines
Verbindungsversuchs unbekannt ist:

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        public MainPage()
        {
            InitializeComponent();

            progress.Visibility = Visibility.Collapsed;
            progress.IsIndeterminate = true;
        }
    }


Schritt 2: Bricks und Bricklets erkennen
----------------------------------------

Dieser Schritt ist ähnlich zu Schritt 1 des
:ref:`Rauchmelder mit C# auslesen
<starter_kit_hardware_hacking_smoke_detector_csharp_step1>` Projekts.
|step2_discover_by_uid|

|step2_async|

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        private IPConnection ipcon = null;
        private BrickletIndustrialQuadRelay relay = null;
        private BackgroundWorker connectWorker = null;

        public MainPage()
        {
            // [...]

            connectWorker = new BackgroundWorker();
            connectWorker.DoWork += ConnectWorker_DoWork;
        }

        private void ConnectWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            string[] argument = e.Argument as string[];

            ipcon = new IPConnection();
            relay = new BrickletIndustrialQuadRelay(argument[2], ipcon);

            ipcon.Connect(argument[0], Convert.ToInt32(argument[1]));
        }

        private void Connect()
        {
            string[] argument = new string[3];

            argument[0] = host.Text;
            argument[1] = port.Text;
            argument[2] = uid.Text;

            connectWorker.RunWorkerAsync(argument);
        }
    }

Der ``BackgroundWorker`` hat eine ``DoWork``-Event das von einem anderen Thread
ausgelöst wird sobald ``RunWorkerAsync()`` aufgerufen wurde. Die Host, Port und
UID Konfiguration wird dann an das ``DoWork``-Event übergeben. Dies ist
notwendig, da die ``ConnectWorker_DoWork()`` Methode diese Informationen
benötigt, selbst aber nicht auf die GUI Elemente zugreifen darf. Jetzt kann die
``ConnectWorker_DoWork()`` Methode die ``IPConnection`` und
``BrickletIndustrialQuadRelay`` Objekte erzeugen und ``Connect()`` aufrufen.

Schlussendlich soll der ``BackgroundWorker`` gestartet werden, wenn der
Connect-Knopf geklickt wird. Dafür wird die ``Connect_Click()`` Methode an das
``Click``-Event des Connect-Knopfes gebunden:

.. code-block:: csharp

    private void Connect_Click(object sender, RoutedEventArgs e)
    {
        Connect();
    }

|step2_finish|


Schritt 3: Taster auslösen
--------------------------

|step3_intro|

Dafür wird die ``Trigger_Click()`` Methode an das ``Click``-Event des
Trigger-Knopfes gebunden. Diese startet einen anderen ``BackgroundWorker`` der
dann wiederum die ``SetMonoflop()`` Methode des Industrial Quad Relay Bricklet
aufruft um einen Taster auf der gehackten Fernbedienung zu drücken:

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        // [...]

        private BackgroundWorker triggerWorker = null;

        public MainPage()
        {
            // [...]

            triggerWorker = new BackgroundWorker();
            triggerWorker.DoWork += TriggerWorker_DoWork;
        }

        private void TriggerWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            relay.SetMonoflop(1 << 0, 1 << 0, 1500);
        }

        private void Trigger_Click(object sender, RoutedEventArgs e)
        {
            triggerWorker.RunWorkerAsync();
        }
    }

|step3_monoflop|

|step3_finish1|

|step3_finish2|


Schritt 4: Weitere GUI-Logik
----------------------------

|step4_intro|

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        // [...]

        public MainPage()
        {
            // [...]

            connectWorker.RunWorkerCompleted += ConnectWorker_RunWorkerCompleted;
        }

        private void ConnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            connect.Content = "Disconnect";
        }
    }

Die ``ConnectWorker_RunWorkerCompleted()`` Methode wird nach
``ConnectWorker_DoWork()`` aufgerufen. sie ändert den Text des Knopfes zu
"Disconnect". Die ``Connect_Click()`` Methode entscheidet nun dynamisch was zu
tun ist. Falls keine Verbindung besteht wird ``Connect()`` aufgerufen,
andernfalls wird der ``BackgroundWorker`` für das Trennen der Verbindung
gestartet:

.. code-block:: csharp

    private void Connect_Click(object sender, RoutedEventArgs e)
    {
        if (ipcon == null || ipcon.GetConnectionState() == IPConnection.CONNECTION_STATE_DISCONNECTED)
        {
            Connect();
        }
        else
        {
            disconnectWorker.RunWorkerAsync();
        }
    }

Der ``BackgroundWorker`` für das Trennen der Verbindung ruft die
:csharp:func:`Disconnect() <IPConnection::Disconnect>` Methode im Hintergrund
auf, da dies einen Moment dauern kann und während dieser Zeit die GUI blockiert
wäre:

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        // [...]

        private BackgroundWorker disconnectWorker = null;

        public MainPage()
        {
            // [...]

            disconnectWorker = new BackgroundWorker();
            disconnectWorker.DoWork += DisconnectWorker_DoWork;
            disconnectWorker.RunWorkerCompleted += DisconnectWorker_RunWorkerCompleted;
        }

        private void DisconnectWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            ipcon.Disconnect();
        }

        private void DisconnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            connect.Content = "Connect";
        }
    }

|step4_disabled_gui|

Der ``connectWorker`` und der ``disconnectWorker`` werden so erweitert,
dass sie die GUI Elemente abhängig von dem aktuellen Zustand der Verbindung
aktivieren oder deaktivieren:

.. code-block:: csharp

    private void ConnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
    {
        // [...]

        connect.IsEnabled = true;
        trigger.IsEnabled = true;
    }

.. code-block:: csharp

    private void DisconnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
    {
        // [...]

        host.IsEnabled = true;
        port.IsEnabled = true;
        uid.IsEnabled = true;
        connect.IsEnabled = true;
    }

.. code-block:: csharp

    private void Connect()
    {
        host.IsEnabled = false;
        port.IsEnabled = false;
        uid.IsEnabled = false;
        connect.IsEnabled = false;
        trigger.IsEnabled = false;

        // [...]
    }

|step4_robust1|

|step4_robust2|


Schritt 5: Fehlerbehandlung und Reporting
-----------------------------------------

Es werden die gleichen Konzepte wie in Schritt 4 des
:ref:`Rauchmelder mit C# auslesen
<starter_kit_hardware_hacking_smoke_detector_csharp_step4>` Projekts angewandt,
allerdings mit Abwandlungen damit sie in einem GUI Programm funktionieren.

Wir können nicht einfach ``System.Console.WriteLine()`` für Fehlermeldungen
verwenden, da dies ein GUI Programm ist und kein Konsolenfenster hat.
Stattdessen werden Messageboxen verwendet.

Die ``Connect()`` Methode muss die Benutzereingaben validieren bevor sie
verwendet werden. Mittels ``MessageBox`` werden mögliche Probleme gemeldet.
Die "ProgressBar" wird eingeblendet um auf den laufenden Verbindungsversuch
hinzuweisen:

.. code-block:: csharp

    private void Connect()
    {
        if (host.Text.Length == 0 || port.Text.Length == 0 || uid.Text.Length == 0)
        {
            MessageBox.Show("Host/Port/UID cannot be empty", "Error", MessageBoxButton.OK);
            return;
        }

        progress.Visibility = Visibility.Visible;

        // [...]
    }

    private void ConnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
    {
        progress.Visibility = Visibility.Collapsed;

        // [...]
    }

Dann benötigt die ``ConnectWorker_DoWork()`` Methode noch eine Möglichkeit das
Ergebnis des Verbindungsversuchs mitzuteilen. Sie darf zwar nicht direkt mit
dem GUI interagieren, kann aber einen Wert an den ``Result`` Member des
``DoWorkEventArgs`` Parameters zuweisen, der dann an den Aufruf der
``ConnectWorker_RunWorkerCompleted()`` Methode übergeben wird. Wir verwenden
hier ein ``enum``, das die drei möglichen Ausgänge eines Verbindungsversuchs
repräsentiert:

.. code-block:: csharp

    enum ConnectResult
    {
        SUCCESS,
        NO_CONNECTION,
        NO_DEVICE
    }

* |step5_connect_result1|
* |step5_connect_result2|
* |step5_connect_result3|

|step5_check_identity|

.. code-block:: csharp

    private void ConnectWorker_DoWork(object sender, DoWorkEventArgs e)
    {
        string[] argument = e.Argument as string[];

        ipcon = new IPConnection();

        try
        {
            relay = new BrickletIndustrialQuadRelay(argument[2], ipcon);
        }
        catch (ArgumentOutOfRangeException)
        {
            e.Result = ConnectResult.NO_DEVICE;
            return;
        }

        try
        {
            ipcon.Connect(argument[0], Convert.ToInt32(argument[1]));
        }
        catch (System.IO.IOException)
        {
            e.Result = ConnectResult.NO_CONNECTION;
            return;
        }
        catch (ArgumentOutOfRangeException)
        {
            e.Result = ConnectResult.NO_CONNECTION;
            return;
        }

        try
        {
            string uid;
            string connectedUid;
            char position;
            byte[] hardwareVersion;
            byte[] firmwareVersion;
            int deviceIdentifier;

            relay.GetIdentity(out uid, out connectedUid, out position,
                              out hardwareVersion, out firmwareVersion, out deviceIdentifier);

            if (deviceIdentifier != BrickletIndustrialQuadRelay.DEVICE_IDENTIFIER)
            {
                ipcon.Disconnect();
                e.Result = ConnectResult.NO_DEVICE;
                return;
            }
        }
        catch (TinkerforgeException)
        {
            try
            {
                ipcon.Disconnect();
            }
            catch (NotConnectedException)
            {
            }

            e.Result = ConnectResult.NO_DEVICE;
            return;
        }

        e.Result = ConnectResult.SUCCESS;
    }

Die ``ConnectWorker_RunWorkerCompleted()`` Methode muss jetzt entsprechend
reagieren. Als erstes wird immer die "ProgressBar`` ausgeblendet:

.. code-block:: csharp

    private void ConnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
    {
        ConnectResult result = (ConnectResult)e.Result;

        progress.Visibility = Visibility.Collapsed;

|step5_success|

.. code-block:: csharp

        if (result == ConnectResult.SUCCESS)
        {
            connect.Content = "Disconnect";
            connect.IsEnabled = true;
            trigger.IsEnabled = true;
        }

Im Fehlerfall wird eine ``MessageBox`` mit einer entsprechenden Meldung
angezeigt:

.. code-block:: csharp

        else
        {
            string message;
            MessageBoxResult retry;

            if (result == ConnectResult.NO_CONNECTION) {
                message = "Could not connect to " + host.Text + ":" + port.Text + ". Retry?";
            } else { // ConnectResult.NO_DEVICE
                message = "Could not find Industrial Quad Relay Bricklet [" + uid.Text + "]. Retry?";
            }

            retry = MessageBox.Show(message, "Error", MessageBoxButton.OKCancel);

Abhängig vom Ergebnis der ``MessageBox`` wird dann der Verbindungsversuch
abgebrochen oder wiederholt:

.. code-block:: csharp

            if (retry == MessageBoxResult.OK) {
                Connect();
            } else {
                host.IsEnabled = true;
                port.IsEnabled = true;
                uid.IsEnabled = true;
                connect.Content = "Connect";
                connect.IsEnabled = true;
            }
        }
    }

|step5_finish|


Schritt 6: Konfiguration und Zustand speichern
----------------------------------------------

Die App speichert die Konfiguration noch nicht. Windows Phone bietet hierfür die
``IsolatedStorageSettings`` Klasse. In ``OnNavigatedTo()`` wird die gespeicherte
Konfiguration wieder geladen und die Verbindung wiederhergestellt wenn sie zuvor
bestanden hat:

.. code-block:: csharp

    protected override void OnNavigatedTo(NavigationEventArgs e)
    {
        bool connected = false;

        try
        {
            host.Text = settings["host"] as string;
            port.Text = settings["port"] as string;
            uid.Text = settings["uid"] as string;
            connected = settings["connected"].Equals(true);
        }
        catch (KeyNotFoundException)
        {
            settings["host"] = host.Text;
            settings["port"] = port.Text;
            settings["uid"] = uid.Text;
            settings["connected"] = connected;
            settings.Save();
        }

        if (connected &&
            (ipcon == null ||
             ipcon.GetConnectionState() == IPConnection.CONNECTION_STATE_DISCONNECTED))
        {
            Connect();
        }
    }

In ``OnNavigatedFrom()`` wird die Konfiguration dann wieder gespeichert:

.. code-block:: csharp

    protected override void OnNavigatedFrom(NavigationEventArgs e)
    {
        settings["host"] = host.Text;
        settings["port"] = port.Text;
        settings["uid"] = uid.Text;

        if (ipcon != null && ipcon.GetConnectionState() == IPConnection.CONNECTION_STATE_CONNECTED)
        {
            settings["connected"] = true;
        }
        else
        {
            settings["connected"] = false;
        }

        settings.Save();
    }

|step6_finish|


Schritt 7: Alles zusammen
-------------------------

|step7_intro|

|step7_together| (`Download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/windows_phone/GarageControl/MainPage.xaml.cs>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/windows_phone/GarageControl/MainPage.xaml.cs
 :language: csharp
 :tab-width: 4
