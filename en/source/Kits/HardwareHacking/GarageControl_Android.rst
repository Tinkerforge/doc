
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Garage Door Openers using Android

.. |name| replace:: Android
.. |ref_CALLBACK_ENUMERATE| replace:: :java:func:`EnumerateListener <IPConnection.EnumerateListener>`
.. |ref_connect| replace:: :java:func:`connect() <IPConnection::connect>`
.. |connect| replace:: ``connect()``
.. |set_monoflop| replace:: ``setMonoflop(1 << 0, 1 << 0, 1500)``
.. |ref_get_identity| replace:: :java:func:`getIdentity() <BrickletIndustrialQuadRelay::getIdentity>`
.. |async_helper| replace:: ``AsyncTask``

.. include:: GarageControl.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_garage_control_android:

Control Garage Door Openers using Android
=========================================

.. include:: AndroidCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: GarageControl.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: GarageControl.substitutions
   :start-after: >>>goals
   :end-before: <<<goals

The app will reuse some common parts of the
:ref:`starter_kit_hardware_hacking_smoke_detector_java` project.


Step 1: Creating the GUI
------------------------

After creating a new "Android Application Project" named "Garage Control" in
Eclipse we start with creating the GUI:

.. image:: /Images/Kits/hardware_hacking_garage_control_android_gui_350.jpg
   :scale: 100 %
   :alt: App GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_control_android_gui.jpg

The basis is a "Linear Layout (Vertical)". Three text fields allow to enter
the host, port and UID of the Industrial Quad Relay Bricklet. For the port a
"Number" text field is used, so Android will restrict the content of this
text field to numbers. The final two elements are one "Button" to connect and
disconnect and another one to trigger the remote control.

Now the GUI layout is finished. To access the GUI components in the Java code
we use the ``findViewById()`` method and store the references to member
variables of the ``MainActivity`` class:

.. code-block:: java

    public class MainActivity extends Activity {
        private EditText host;
        private EditText port;
        private EditText uid;
        private Button connect;
        private Button trigger;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            host = (EditText)findViewById(R.id.host);
            port = (EditText)findViewById(R.id.port);
            uid = (EditText)findViewById(R.id.uid);
            connect = (Button)findViewById(R.id.connect);
            trigger = (Button)findViewById(R.id.trigger);
        }
    }


Step 2: Discover Bricks and Bricklets
-------------------------------------

This step is similar to step 1 in the
:ref:`Read out Smoke Detectors using Java
<starter_kit_hardware_hacking_smoke_detector_java_step1>` project.
|step2_discover_by_uid|

|step2_async|

.. code-block:: java

    public class MainActivity extends Activity {
        // [...]

        private IPConnection ipcon;
        private BrickletIndustrialQuadRelay relay;

        class ConnectAsyncTask extends AsyncTask<Void, Void, Void> {
            private String currentHost;
            private String currentPort;
            private String currentUID;

            @Override
            protected void onPreExecute() {
                currentHost = host.getText().toString();
                currentPort = port.getText().toString();
                currentUID = uid.getText().toString();
            }

            protected Void doInBackground(Void... params) {
                ipcon = new IPConnection();
                relay = new BrickletIndustrialQuadRelay(currentUID, ipcon);

                ipcon.connect(currentHost, Integer.parseInt(currentPort));

                return null;
            }
        }
    }

The ``ConnectAsyncTask`` is implemented as an inner class. This allows for
direct access to the member variables of the ``MainActivity`` class.

The ``onPreExecute()`` method is called before ``doInBackground()`` and stores
the host, port and UID configuration from the GUI elements. This is necessary,
because the ``doInBackground()`` method needs this information, but is not
allowed to access the GUI elements. Now the ``doInBackground()`` method can
create an ``IPConnection`` and ``BrickletIndustrialQuadRelay`` object and call
the ``connect()`` method.

Finally, a ``ConnectAsyncTask`` should be created and executed when the connect
button is clicked. A ``OnClickListener`` added to the connect button does this:

.. code-block:: java

    public class MainActivity extends Activity {
        // [...]

        class ConnectClickListener implements OnClickListener {
            public void onClick(View v) {
                new ConnectAsyncTask().execute();
            }
        }

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            // [...]

            connect.setOnClickListener(new ConnectClickListener());
        }
    }

|step2_finish|


Step 3: Triggering Switches
---------------------------

|step3_intro|

An ``OnClickListener`` is added to the trigger button that creates and executes
an ``AsyncTask`` that in turn calls the ``setMonoflop()`` method of the
Industrial Quad Relay Bricklet to trigger the switch on the remote control:

.. code-block:: java

    public class MainActivity extends Activity {
        // [...]

        private BrickletIndustrialQuadRelay relay;

        class TriggerAsyncTask extends AsyncTask<Void, Void, Void> {
            protected Void doInBackground(Void... params) {
                relay.setMonoflop(1 << 0, 1 << 0, 1500);
                return null;
            }
        }

        class TriggerClickListener implements OnClickListener {
            public void onClick(View v) {
                new TriggerAsyncTask().execute();
            }
        }
    }

|step3_monoflop|

|step3_finish1|

|step3_finish2|


Step 4: More GUI logic
----------------------

|step4_intro|

.. code-block:: java

    class ConnectAsyncTask extends AsyncTask<Void, Void, Void> {
        // [...]

        @Override
        protected void onPostExecute(Void result) {
            connect.setText("Disconnect");
            connect.setOnClickListener(new DisconnectClickListener());
        }
    }

The ``onPostExecute()`` method is called after ``doInBackground()``. It changes
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

|step4_disabled_gui|

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

|step4_robust1|

|step4_robust2|


Step 5: Error Handling and Reporting
------------------------------------

We will use similar principals as in step 4 of the
:ref:`Read out Smoke Detectors using Java
<starter_kit_hardware_hacking_smoke_detector_java_step4>` project,
but with some changes to make it work in a GUI program.

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
then passed to the ``onPostExecute()`` method. We use this ``enum`` that
represents the three possible outcomes of a connection attempt:

.. code-block:: java

    enum ConnectResult {
        SUCCESS,
        NO_CONNECTION,
        NO_DEVICE
    }

* |step5_connect_result1|
* |step5_connect_result2|
* |step5_connect_result3|

|step5_check_identity|

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

|step5_success|

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

|step5_finish|


Step 6: Persistent Configuration and State
------------------------------------------

The app doesn't store its configuration yet. Android provides the
``SharedPreferences`` class to take care of this. In ``onCreate()`` the
configuration is restored:

.. code-block:: java

    protected void onCreate(Bundle savedInstanceState) {
        // [...]

        SharedPreferences settings = getPreferences(0);
        host.setText(settings.getString("host", host.getText().toString()));
        port.setText(settings.getString("port", port.getText().toString()));
        uid.setText(settings.getString("uid", uid.getText().toString()));
    }

In ``onStop()`` the configuration is then stored again:

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
of the connection is stored when ``onSaveInstanceState()`` is called:

.. code-block:: java

    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);

        outState.putBoolean("connected", ipcon != null &&
                                         ipcon.getConnectionState() == IPConnection.CONNECTION_STATE_CONNECTED);
    }

And is restored when ``onCreate()`` is called:

.. code-block:: java

    protected void onCreate(Bundle savedInstanceState) {
        // [...]

        if (savedInstanceState != null && savedInstanceState.getBoolean("connected", false)) {
            new ConnectAsyncTask().execute();
        }
    }

|step6_finish|


Step 7: Everything put together
-------------------------------

|step7_intro|

|step7_together| (`Download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/android/GarageControl/src/com/tinkerforge/garagecontrol/MainActivity.java>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/android/GarageControl/src/com/tinkerforge/garagecontrol/MainActivity.java
 :language: java
 :tab-width: 4
