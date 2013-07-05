
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Garage Door Openers using Windows Phone

.. _starter_kit_hardware_hacking_garage_control_windows_phone:

Control Garage Door Openers using Windows Phone
===============================================

For this project we are assuming, that you have the `Windows Phone SDK
<https://dev.windowsphone.com/en-us/downloadsdk>`__ set up and that you have a
rudimentary understanding of the C# language.

If you are totally new to C# itself you should start
`here <http://csharp.net-tutorials.com/>`__.
If you are new to the Tinkerforge API, you should start
:ref:`here <api_bindings_csharp_windows_phone>`.

We are also assuming that you have a remote control connected to
an :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>` as
described :ref:`here <starter_kit_hardware_hacking_garage_control>`.


Goals
-----

In this project we will create a simple Windows Phone app that resembles the
functionality of the actual remote control.

The program will reuse some common parts of the :ref:`Read out Smoke Detectors
using C# <starter_kit_hardware_hacking_smoke_detector_csharp>` project.


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

This step is similar to step 1 in the :ref:`Read out Smoke Detectors using C#
<starter_kit_hardware_hacking_smoke_detector_csharp_step1>` project. We apply
some changes to make it work in a GUI program and instead of using the
:csharp:func:`EnumerateCallback <IPConnection::EnumerateCallback>` to discover
the Industrial Quad Relay Bricklet its UID has to be specified. This approach
allows to pick the correct Industrial Quad Relay Bricklet even if multiple are
connected to the same host at once.

We don't want to call the :csharp:func:`Connect() <IPConnection::Connect>`
method directly, because it might take a moment and block the GUI during that
period of time. Instead ``Connect()`` will be called by a ``BackgroundWorker``,
so it will run in the background and the GUI stays responsive:

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
another thread after ``RunWorkerAsync`` was called. The host, port and UID
configuration is passed to the ``DoWork`` event. This is necessary, because the
``ConnectWorker_DoWork()`` method needs this information, but is not
allowed to access the GUI elements. Now the ``ConnectWorker_DoWork()`` method
can create an ``IPConnection`` and ``BrickletIndustrialQuadRelay`` object and
call the ``Connect()`` method.

Finally, the ``BackgroundWorker`` should be started when the connect button is
clicked. To do this the ``Connect_Click()`` method is bound to the click event of
the connect button:

.. code-block:: csharp

    private void Connect_Click(object sender, RoutedEventArgs e)
    {
        Connect();
    }

Host, port and UID can now be configured and a click on the connect button
establishes the connection.


Step 3: Triggering Switches
---------------------------

The connection is established and the Industrial Quad Relay Bricklet is found
but there is no logic yet to trigger the switch on the remote control if the
trigger button is clicked.

To do this the ``Trigger_Click()`` method is bound to the click event of the
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
            relay.SetMonoflop(1 << 0, 1 << 0, 1500);
        }

        private void Trigger_Click(object sender, RoutedEventArgs e)
        {
            triggerWorker.RunWorkerAsync();
        }
    }

The call to ``SetMonoflop(1 << 0, 1 << 0, 1500)`` closes the first relay for
1.5s then opens it again.

That's it. If we would copy these three steps together in one file, we would
have a working app that allows a smart phone to control a garage door opener
using its hacked remote control!

We don't have a disconnect button yet and the trigger button can be clicked
before the connection is established. We need some more GUI logic!


Step 4: More GUI logic
----------------------

There is no button to close the connection again after it got established. The
connect button could do this. When the connection is established it should
allow to disconnect it again:

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

Finally, the user should not be able to change the content of the text fields
during the time the connection gets established and the trigger button should
not be clickable if there is no connection.

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

But the program is not yet robust enough. What happens if can't connect? What
happens if there is no Industrial Quad Relay Bricklet with the given UID?

What we need is error handling!


Step 5: Error Handling and Reporting
------------------------------------

We will use similar principals as in step 4 of the :ref:`Read out Smoke
Detectors using C# <starter_kit_hardware_hacking_smoke_detector_csharp_step4>`
project, but with some changes to make it work in a GUI program.

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
the ``ConnectWorker_RunWorkerCompleted()`` method. We use this enum that
represents the three possible outcomes of a connection attempt:

.. code-block:: csharp

    enum ConnectResult
    {
        SUCCESS,
        NO_CONNECTION,
        NO_DEVICE
    }

* SUCCESS: The connection got established and an Industrial Quad Relay Bricklet
  with the given UID was found.
* NO_CONNECTION: The connection could not be established.
* NO_DEVICE: The connection got established but there was no Industrial Quad
  Relay Bricklet with the given UID.

The :csharp:func:`GetIdentity() <BrickletIndustrialQuadRelay::GetIdentity>` method
is used to check that the device for the given UID really is an Industrial Quad
Relay Bricklet. If this is not the case then the connection gets closed:

.. code-block:: csharp

    private void ConnectWorker_DoWork(object sender, DoWorkEventArgs e)
    {
        string[] argument = e.Argument as string[];

        ipcon = new IPConnection();
        relay = new BrickletIndustrialQuadRelay(argument[2], ipcon);

        try
        {
            ipcon.Connect(argument[0], Convert.ToInt32(argument[1]));
        }
        catch (System.IO.IOException)
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
outcomes. First the progress dialog is dismissed:

.. code-block:: csharp

    private void ConnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
    {
        ConnectResult result = (ConnectResult)e.Result;

        progress.Visibility = Visibility.Collapsed;

In case the connection attempt was successful the original logic stays the same:

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

Now the app can connect to an configurable host and port and trigger a button
on the remote control of your garage door opener using an Industrial Quad Relay
Bricklet.


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

Now the configuration and state is stored persistent across a restart of the app.


Step 7: Everything put together
-------------------------------

That's it! We are done with the app for our hacked garage door opener remote
control.

Now all of the above put together (`download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/windows_phone/GarageControl/MainPage.xaml.cs>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/windows_phone/GarageControl/MainPage.xaml.cs
 :language: csharp
 :tab-width: 4
