
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Garage Door Openers using Windows Phone

.. |name| replace:: Windows Phone
.. |ref_CALLBACK_ENUMERATE| replace:: :csharp:func:`EnumerateCallback <IPConnection::EnumerateCallback>`
.. |ref_connect| replace:: :csharp:func:`Connect() <IPConnection::Connect>`
.. |connect| replace:: ``Connect()``
.. |set_monoflop| replace:: ``SetMonoflop(1 << 0, 15, 1500)``
.. |ref_get_identity| replace:: :csharp:func:`GetIdentity() <BrickletIndustrialQuadRelay::GetIdentity>`
.. |async_helper| replace:: a ``BackgroundWorker``

.. include:: GarageControl.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_garage_control_windows_phone:

Control Garage Door Openers using Windows Phone
===============================================

.. include:: WindowsPhoneCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: GarageControl.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

The complete Visual Studio project can be downloaded `here
<https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/windows_phone>`__.
A demo app based on this project is available in the
`Windows Phone Store <http://www.windowsphone.com/s?appid=4c9a8f61-d9ed-4fd2-b4e6-a332b617c596>`__.


Goals
-----

.. include:: GarageControl.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Creating the GUI
------------------------

After creating a new "Windows Phone App" named "Garage Control" in Visual Studio
we start with creating the GUI:

.. image:: /Images/Kits/hardware_hacking_garage_control_windows_phone_gui_350.jpg
   :scale: 100 %
   :alt: App GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_control_windows_phone_gui.jpg

We extend the precreated layout by appending a "StackPanel" to the "LayoutRoot"
grid, that will contain the other GUI elements. Three "TextBoxes" allow
to enter the host, port and UID of the Industrial Quad Relay Bricklet. For the
port a text box with ``InputScope="Number"`` is used, so Windows Phone will
restrict the content of this text box to numbers. Below the text boxes goes a
"ProgressBar" that will be used to indicate that a connection attempt is in
progress. The final two elements are one "Button" to connect and
disconnect and another one to trigger the remote control. Here is a snippet of
the ``MainPage.xaml`` file:

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

Now the GUI layout is finished. The initial GUI configuration is done in the
constructor of the ``MainPage`` class. The progress bar is initially hidden and
indeterminate mode is enabled, because the duration of a connection attempt is
unknown:

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


Step 2: Discover Bricks and Bricklets
-------------------------------------

This step is similar to step 1 in the
:ref:`Read out Smoke Detectors using C#
<starter_kit_hardware_hacking_smoke_detector_csharp_step1>` project.
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

The ``BackgroundWorker`` has an ``DoWork`` event that will be triggered from
another thread after ``RunWorkerAsync()`` was called. The host, port and UID
configuration is passed to the ``DoWork`` event. This is necessary, because the
``ConnectWorker_DoWork()`` method needs this information, but is not
allowed to access the GUI elements. Now the ``ConnectWorker_DoWork()`` method
can create an ``IPConnection`` and ``BrickletIndustrialQuadRelay`` object and
call the ``Connect()`` method.

Finally, the ``BackgroundWorker`` should be started when the connect button is
clicked. To do this the ``Connect_Click()`` method is bound to the ``Click``
event of the connect button:

.. code-block:: csharp

    private void Connect_Click(object sender, RoutedEventArgs e)
    {
        Connect();
    }

|step2_finish|


Step 3: Triggering Switches
---------------------------

|step3_intro|

To do this the ``Trigger_Click()`` method is bound to the ``Click`` event of the
trigger button. It starts another ``BackgroundWorker`` that in turn calls the
``SetMonoflop()`` method of the Industrial Quad Relay Bricklet to trigger the
switch on the remote control:

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
            relay.SetMonoflop(1 << 0, 15, 1500);
        }

        private void Trigger_Click(object sender, RoutedEventArgs e)
        {
            triggerWorker.RunWorkerAsync();
        }
    }

|step3_monoflop|

|step3_finish1|

|step3_finish2|


Step 4: More GUI logic
----------------------

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

The ``ConnectWorker_RunWorkerCompleted()`` method is called after
``ConnectWorker_DoWork()``. It changes the text on the button to "Disconnect".
The ``Connect_Click()`` method now decides dynamically what to do. If there is
no connection it calls ``Connect()``, if there is a connection is runs the
disconnect background worker:

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

The disconnect background worker calls the :csharp:func:`Disconnect()
<IPConnection::Disconnect>` method in the background, because it might take a
moment and block the GUI during that period of time:

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

The ``connectWorker`` and the ``disconnectWorker`` are extended to
disable and enable the GUI elements according to the current connection state:

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


Step 5: Error Handling and Reporting
------------------------------------

We will use similar principals as in step 4 of the
:ref:`Read out Smoke Detectors using C#
<starter_kit_hardware_hacking_smoke_detector_csharp_step4>` project,
but with some changes to make it work in a GUI program.

We can't just use ``System.Console.WriteLine()`` for error reporting because
there is no console window in an app. Instead message boxes are used.

The ``Connect()`` method has to validate the user input before using it. An
``MessageBox`` is used to report possible problems. Also the progress bar is
made visible to indicate that a connection attempt is in progress:

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

Then the ``ConnectWorker_DoWork()`` method needs to be able to report its result.
But it is not allowed to interact with the GUI, but it can assign a value to the
``Result`` member of the ``DoWorkEventArgs`` parameter that is then passed to
the ``ConnectWorker_RunWorkerCompleted()`` method. We use this ``enum`` that
represents the three possible outcomes of a connection attempt:

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

Now the ``ConnectWorker_RunWorkerCompleted()`` method has to handle this three
outcomes. First the progress bar is dismissed:

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

In the error case we use a ``MessageBox`` and set the error message according
to the connection result:

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

Retry to connect or cancel the connection attempt, according to the result of
the message box:

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


Step 6: Persistent Configuration and State
------------------------------------------

The app doesn't store its configuration yet. Windows Phone provides the
``IsolatedStorageSettings`` class to take care of this. In ``OnNavigatedTo()``
the configuration is restored and the connection is reestablished if it was
active before:

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

In ``OnNavigatedFrom()`` the configuration is then stored again:

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


Step 7: Everything put together
-------------------------------

|step7_intro|

|step7_together| (`Download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/windows_phone/GarageControl/MainPage.xaml.cs>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/windows_phone/GarageControl/MainPage.xaml.cs
 :language: csharp
 :tab-width: 4
