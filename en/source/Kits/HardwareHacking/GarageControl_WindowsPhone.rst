
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
clicked. To do this the ``Connect_Click`` method is bound to the click event of
the connect button:

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        // [...]

        private void Connect_Click(object sender, RoutedEventArgs e)
        {
            Connect();
        }
    }

Host, port and UID can now be configured and a click on the connect button
establishes the connection.


Step 3: Triggering Switches
---------------------------

The connection is established and the Industrial Quad Relay Bricklet is found
but there is no logic yet to trigger the switch on the remote control if the
trigger button is clicked.

To do this the ``Trigger_Click`` method is bound to the click event of the
trigger button. It starts another ``BackgroundWorker`` that in turn calls the
``SetMonoflop`` method of the Industrial Quad Relay Bricklet to trigger the
switch on the remote control:

.. code-block:: csharp

    public partial class MainPage : PhoneApplicationPage
    {
        // [...]

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

            connectWorker = new BackgroundWorker();
            connectWorker.DoWork += ConnectWorker_DoWork;
            connectWorker.RunWorkerCompleted += ConnectWorker_RunWorkerCompleted;

            // [...]
        }

        private void ConnectWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            connect.Content = "Disconnect";
        }
    }

The ``ConnectWorker_RunWorkerCompleted()`` method is called after ``ConnectWorker_DoWork()``. It changes
the text on the button and sets a new ``OnClickListener`` that will closes the
connection if the button is clicked:

.. code-block:: java

    class DisconnectClickListener implements OnClickListener {
        public void onClick(View v) {
            new DisconnectAsyncTask().execute();
        }
    }

We don't want to call the :java:func:`disconnect() <IPConnection::disconnect>`
method directly, because it might take a moment and block the GUI during that
period of time. Instead ``disconnect()`` will be called from an ``AsyncTask``,
so it will run in the background and the GUI stays responsive:

.. code-block:: java

    class DisconnectAsyncTask extends AsyncTask<Void, Void, Void> {
        protected Void doInBackground(Void... params) {
            ipcon.disconnect();
            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            connect.setText("Connect");
            connect.setOnClickListener(new ConnectClickListener());
        }
    }

Once the connection is closed a new ``OnClickListener`` is set that will
execute ``ConnectAsyncTask`` to establish the connection if the connect button
is clicked:

.. code-block:: java

    class ConnectClickListener implements OnClickListener {
        public void onClick(View v) {
            new ConnectAsyncTask().execute();
        }
    }

Finally, the user should not be able to change the content of the text fields
during the time the connection gets established and the trigger button should
not be clickable if there is no connection.

The ``ConnectAsyncTask`` and the ``DisconnectAsyncTask`` are extended to
disable and enable the GUI elements according to the current connection state:

.. code-block:: java

    class ConnectAsyncTask extends AsyncTask<Void, Void, Void> {
        // [...]

        @Override
        protected void onPreExecute() {
            // [...]

            host.setEnabled(false);
            port.setEnabled(false);
            uid.setEnabled(false);
            connect.setEnabled(false);
            trigger.setEnabled(false);
        }

        // [...]

        @Override
        protected void onPostExecute(Void result) {
            // [...]

            connect.setEnabled(true);
            trigger.setEnabled(true);
        }
    }

.. code-block:: java

    class DisconnectAsyncTask extends AsyncTask<Void, Void, Void> {
        // [...]

        @Override
        protected void onPreExecute() {
            connect.setEnabled(false);
            trigger.setEnabled(false);
        }

        // [...]

        @Override
        protected void onPostExecute(Void result) {
            host.setEnabled(true);
            port.setEnabled(true);
            uid.setEnabled(true);
            connect.setEnabled(true);

            // [...]
        }
    }

But the program is not yet robust enough. What happens if can't connect? What
happens if there is no Industrial Quad Relay Bricklet with the given UID?

What we need is error handling!


Step 5: Error handling and Reporting
------------------------------------

We will use similar principals as in step 4 of the :ref:`Read out Smoke
Detectors using Java <starter_kit_hardware_hacking_smoke_detector_java_step4>`
project, but with some changes to make it work in a GUI program.

We can't just use ``System.out.println()`` for error reporting because there
is no console window in an app. Instead dialog boxes are used.

The ``ConnectAsyncTask`` has to validate the user input before using it. An
``AlertDialog`` is used to report possible problems:

.. code-block:: java

    class ConnectAsyncTask extends AsyncTask<Void, Void, ConnectResult> {
        // [...]
        private ProgressDialog progressDialog;

        @Override
        protected void onPreExecute() {
            currentHost = host.getText().toString();
            currentPort = port.getText().toString();
            currentUID = uid.getText().toString();

            if (currentHost.length() == 0 || currentPort.length() == 0 || currentUID.length() == 0) {
                AlertDialog.Builder builder = new AlertDialog.Builder(context);
                builder.setMessage("Host/Port/UID cannot be empty");
                builder.create().show();
                cancel(true);
                return;
            }
        }

The ``ConnectAsyncTask`` also gains a ``ProgressDialog`` to show the connection
process:

.. code-block:: java

    class ConnectAsyncTask extends AsyncTask<Void, Void, ConnectResult> {
        // [...]
        private ProgressDialog progressDialog;

        @Override
        protected void onPreExecute() {
            // [...]

            progressDialog = new ProgressDialog(context);
            progressDialog.setMessage("Connecting to " + currentHost + ":" + currentPort);
            progressDialog.setCancelable(false);
            progressDialog.show();
        }

Then the ``doInBackground()`` method needs to be able to report its result. But
it is not allowed to interact with the GUI, but it can return a value that is
then passed to the ``onPostExecute()`` method. We use this enum that represents
the three possible outcomes of a connection attempt:

.. code-block:: java

    enum ConnectResult {
        SUCCESS,
        NO_CONNECTION,
        NO_DEVICE
    }

* SUCCESS: The connection got established and an Industrial Quad Relay Bricklet
  with the given UID was found.
* NO_CONNECTION: The connection could not be established.
* NO_DEVICE: The connection got established but there was no Industrial Quad
  Relay Bricklet with the given UID.

The :java:func:`getIdentity <BrickletIndustrialQuadRelay::getIdentity>` method
is used to check the device for the given UID really is an Industrial Quad
Relay Bricklet. If this is not the case then the connection gets closed:

.. code-block:: java

    protected ConnectResult doInBackground(Void... params) {
        ipcon = new IPConnection();
        relay = new BrickletIndustrialQuadRelay(currentUID, ipcon);

        try {
            ipcon.connect(currentHost, currentPort);
        } catch(java.net.UnknownHostException e) {
            return ConnectResult.NO_CONNECTION;
        } catch(java.io.IOException e) {
            return ConnectResult.NO_CONNECTION;
        } catch(com.tinkerforge.AlreadyConnectedException e) {
            return ConnectResult.NO_CONNECTION;
        }

        try {
            if (relay.getIdentity().deviceIdentifier != BrickletIndustrialQuadRelay.DEVICE_IDENTIFIER) {
                ipcon.disconnect();
                return ConnectResult.NO_DEVICE;
            }
        } catch (com.tinkerforge.TinkerforgeException e1) {
            try {
                ipcon.disconnect();
            } catch (com.tinkerforge.NotConnectedException e2) {
            }

            return ConnectResult.NO_DEVICE;
        }

        return ConnectResult.SUCCESS;
    }

Now the ``onPostExecute()`` method has to handle this three outcomes. First the
progress dialog is dismissed:

.. code-block:: java

    @Override
    protected void onPostExecute(ConnectResult result) {
        progressDialog.dismiss();

In case the connection attempt was successful the original logic stays the same:

.. code-block:: java

        if (result == ConnectResult.SUCCESS) {
            connect.setText("Disconnect");
            connect.setOnClickListener(new DisconnectClickListener());
            connect.setEnabled(true);
            trigger.setEnabled(true);
        }

In the error case we use an ``AlertDialog`` and set the error message according
to the connection result:

.. code-block:: java

        else {
            AlertDialog.Builder builder = new AlertDialog.Builder(context);

            if (result == ConnectResult.NO_CONNECTION) {
                builder.setMessage("Could not connect to " + currentHost + ":" + currentPort);
            } else { // ConnectResult.NO_DEVICE
                builder.setMessage("Could not find Industrial Quad Relay Bricklet [" + currentUID + "]");
            }

            builder.setCancelable(false);

Then retry and cancel buttons are added with the respective logic to either
retry to connect or to cancel the connection attempt:

.. code-block:: java

            builder.setPositiveButton("Retry", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    dialog.dismiss();
                    new ConnectAsyncTask().execute();
                }
            });
            builder.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    host.setEnabled(true);
                    port.setEnabled(true);
                    uid.setEnabled(true);
                    connect.setText("Connect");
                    connect.setOnClickListener(new ConnectClickListener());
                    connect.setEnabled(true);
                    dialog.dismiss();
                }
            });

Finally, the dialog gets created and shown:

.. code-block:: java

            builder.create().show();
        }
    }

Now the app can connect to an configurable host and port and trigger a button
on the remote control of your garage door opener using an Industrial Quad Relay
Bricklet.


Step 6: Persistent Configuration and State
------------------------------------------

The app doesn't store its configuration yet. Android provides the
``SharedPreferences`` class to take care of this. In ``onCreate`` the
configuration is restored:

.. code-block:: java

    protected void onCreate(Bundle savedInstanceState) {
        // [...]

        SharedPreferences settings = getPreferences(0);
        host.setText(settings.getString("host", host.getText().toString()));
        port.setText(settings.getString("port", port.getText().toString()));
        uid.setText(settings.getString("uid", uid.getText().toString()));
    }

In ``onStop`` the configuration is then stored again:

.. code-block:: java

    protected void onStop() {
        super.onStop();

        SharedPreferences settings = getPreferences(0);
        SharedPreferences.Editor editor = settings.edit();

        editor.putString("host", host.getText().toString());
        editor.putString("port", port.getText().toString());
        editor.putString("uid", uid.getText().toString());
        editor.commit();
    }

If the orientation is changed Android basically restarts the app for the
new orientation. This makes our app loss the connection. Therefore, the state
of the connection is stored when ``onSaveInstanceState`` is called:

.. code-block:: java

    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);

        outState.putBoolean("connected", ipcon != null &&
                                         ipcon.getConnectionState() == IPConnection.CONNECTION_STATE_CONNECTED);
    }

And is restored when ``onCreate`` is called:

.. code-block:: java

    protected void onCreate(Bundle savedInstanceState) {
        // [...]

        if (savedInstanceState != null && savedInstanceState.getBoolean("connected", false)) {
            new ConnectAsyncTask().execute();
        }
    }

Now the configuration and state is stored persistent across a restart of the app.


Step 7: Everything put together
-------------------------------

That's it! We are done with the app for our hacked garage door opener remote
control.

Now all of the above put together (`download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/android/GarageControl/src/com/tinkerforge/garagecontrol/MainActivity.java>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/android/GarageControl/src/com/tinkerforge/garagecontrol/MainActivity.java
 :language: java
 :tab-width: 4
