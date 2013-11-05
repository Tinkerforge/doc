
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Garagentor mit Android fernsteuern

.. |name| replace:: Android
.. |ref_CALLBACK_ENUMERATE| replace:: :java:func:`EnumerateListener <IPConnection.EnumerateListener>`
.. |ref_connect| replace:: :java:func:`connect() <IPConnection::connect>`
.. |connect| replace:: ``connect()``
.. |set_monoflop| replace:: ``setMonoflop(1 << 0, 15, 1500)``
.. |ref_get_identity| replace:: :java:func:`getIdentity() <BrickletIndustrialQuadRelay::getIdentity>`
.. |async_helper| replace:: einem ``AsyncTask``

.. include:: GarageControl.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_garage_control_android:

Garagentor mit Android fernsteuern
==================================

.. include:: AndroidCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: GarageControl.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Das vollständige Eclipse Projekt kann `hier
<https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/android>`__
heruntergeladen werden. Eine Demo-App basierend auf diesem Projekt steht im
`Google Play Store <https://play.google.com/store/apps/details?id=com.tinkerforge.garagecontrol>`__
zur Verfügung.


Ziele
-----

.. include:: GarageControl.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Die GUI erstellen
----------------------------

Nach dem Erstellen eines neuen "Android Application Project" namens
"Garage Control" in Eclipse beginnen wir mit der Erstellung der GUI:

.. image:: /Images/Kits/hardware_hacking_garage_control_android_gui_350.jpg
   :scale: 100 %
   :alt: App GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_control_android_gui.jpg

Die Grundlage ist ein "Linear Layout (Vertical)". Drei Textfelder ermöglichen
die Eingabe von Host, Port und UID des Industrial Quad Relay Bricklets. Für den
Port wird ein "Number" Textfeld verwendet, so dass Android die möglichen
Eingaben in diesem Textfeld auf Zahlen beschränken wird. Die letzten beiden
Elemente sind Knöpfe für den Aufbau und das Trennen der Verbindung sowie das
Auslösen eines Tastendrucks auf der gehackten Fernbedienung.

Damit ist das Layout des GUIs fertig. Um auf die GUI Elemente von Java aus
zugreifen zu können bietet Android die ``findViewById()`` Methode. Über diese
erhält man Referenzen auf die GUI Elemente, welche dann in Member-Variablen
der ``MainActivity`` Klasse zugewiesen werden:

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


Schritt 2: Bricks und Bricklets erkennen
----------------------------------------

Dieser Schritt ist ähnlich zu Schritt 1 des
:ref:`Rauchmelder mit Java auslesen
<starter_kit_hardware_hacking_smoke_detector_java_step1>` Projekts.
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

Der ``ConnectAsyncTask`` ist als Inner Class implementiert. Dadurch kann diese
direkt auf Member-Variablen der äußeren ``MainActivity`` Klasse zugreifen.

Die ``onPreExecute()`` Methode wird vor ``doInBackground()`` aufgerufen und
speichert die Host, Port und UID Konfiguration von den GUI Elementen zwischen.
Dies ist notwendig, da die ``doInBackground()`` Methode diese Information
benötigt, aber selbst nicht auf die GUI Elemente zugreifen darf. Jetzt kann
die ``doInBackground()`` Methode die ``IPConnection`` und
``BrickletIndustrialQuadRelay`` Objekte erzeugen und ``connect()`` aufrufen.

Schlussendlich soll ein ``ConnectAsyncTask`` erzeugt und gestartet werden, wenn
der Connect-Knopf geklickt wird. Ein ``OnClickListener`` wird für diesen Zweck
dem Connect-Knopf hinzugefügt:

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


Schritt 3: Taster auslösen
--------------------------

|step3_intro|

Ein ``OnClickListener`` wird dem Trigger-Knopf hinzugefügt. Dieser erzeugt und
startet einen ``AsyncTask`` der wiederum die ``setMonoflop()`` Methode des
Industrial Quad Relay Bricklet aufruft, um einen Taster auf der Fernbedienung
zu drücken:

.. code-block:: java

    public class MainActivity extends Activity {
        // [...]

        private BrickletIndustrialQuadRelay relay;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            // [...]

            trigger.setOnClickListener(new TriggerClickListener());
        }

        class TriggerAsyncTask extends AsyncTask<Void, Void, Void> {
            protected Void doInBackground(Void... params) {
                relay.setMonoflop(1 << 0, 15, 1500);
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


Schritt 4: Weitere GUI-Logik
----------------------------

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

Die ``onPostExecute()`` Methode wird nach ``doInBackground()`` aufgerufen. Sie
ändert den Text des Knopfes und setzt einen neuen ``OnClickListener``, der die
Verbindung trennen wird wenn der Knopf geklickt wird:

.. code-block:: java

    class DisconnectClickListener implements OnClickListener {
        public void onClick(View v) {
            new DisconnectAsyncTask().execute();
        }
    }

Die :java:func:`disconnect() <IPConnection::disconnect>` Methode soll nicht
direkt aufgerufen werden, da diese einen Moment dauern kann und in dieser Zeit
die GUI blockiert ist. Stattdessen wird ``disconnect()`` in einem ``AsyncTask``
aufgerufen, wodurch es im Hintergrund ausgeführt und die GUI nicht blockiert
wird:

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

Sobald die Verbindung getrennt ist wird ein neuer ``OnClickListener`` gesetzt
der einen ``ConnectAsyncTask`` erzeugt und startet, um die Verbindung neu
aufzubauen wenn der Connect-Knopf geklickt wird:

.. code-block:: java

    class ConnectClickListener implements OnClickListener {
        public void onClick(View v) {
            new ConnectAsyncTask().execute();
        }
    }

|step4_disabled_gui|

Der ``ConnectAsyncTask`` und der ``DisconnectAsyncTask`` werden so erweitert,
dass sie die GUI Elemente abhängig von dem aktuellen Zustand der Verbindung
aktivieren oder deaktivieren:

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


Schritt 5: Fehlerbehandlung und Reporting
-----------------------------------------

Es werden die gleichen Konzepte wie in Schritt 4 des
:ref:`Rauchmelder mit Java auslesen
<starter_kit_hardware_hacking_smoke_detector_java_step4>` Projekts angewandt,
allerdings mit Abwandlungen damit sie in einem GUI Programm funktionieren.

Wir können nicht einfach ``System.out.println()`` für Fehlermeldungen
verwenden, da dies ein GUI Programm ist und kein Konsolenfenster hat.
Stattdessen werden Dialogboxen verwendet.

Der ``ConnectAsyncTask`` muss die Benutzereingaben validieren bevor sie
verwendet werden. Mittels ``AlertDialog`` werden mögliche Probleme gemeldet:

.. code-block:: java

    class ConnectAsyncTask extends AsyncTask<Void, Void, ConnectResult> {
        // [...]

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

        // [...]
    }

Der ``ConnectAsyncTask`` bekommt auch einen ``ProgressDialog`` um auf den
laufenden Verbindungsversuch hinzuweisen:

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

        // [...]
    }

Dann benötigt die ``doInBackground()`` Methode noch eine Möglichkeit das
Ergebnis des Verbindungsversuchs mitzuteilen. Sie darf zwar nicht direkt mit
dem GUI interagieren, kann aber einen Wert zurückgeben, der dann an den Aufruf
der ``onPostExecute()`` Methode übergeben wird. Wir verwenden hier ein ``enum``,
das die drei möglichen Ausgänge eines Verbindungsversuchs repräsentiert:

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

        try {
            relay = new BrickletIndustrialQuadRelay(currentUID, ipcon);
        } catch(IllegalArgumentException e) {
            return ConnectResult.NO_DEVICE;
        }

        try {
            ipcon.connect(currentHost, currentPort);
        } catch(java.net.UnknownHostException e) {
            return ConnectResult.NO_CONNECTION;
        } catch(IllegalArgumentException e) {
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

Die ``onPostExecute()`` Methode muss jetzt entsprechend reagieren. Als erstes
wird immer der ``ProgressDialog`` ausgeblendet:

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

Im Falle eines Fehler wird ein ``AlertDialog`` mit der entsprechenden
Fehlermeldung angezeigt:

.. code-block:: java

        else {
            AlertDialog.Builder builder = new AlertDialog.Builder(context);

            if (result == ConnectResult.NO_CONNECTION) {
                builder.setMessage("Could not connect to " + currentHost + ":" + currentPort);
            } else { // ConnectResult.NO_DEVICE
                builder.setMessage("Could not find Industrial Quad Relay Bricklet [" + currentUID + "]");
            }

            builder.setCancelable(false);

Die Knöpfe für "Wiederholen" und "Abbrechen" und werden abhängig vom Ausgang
des Verbindungsversuchs zum Dialog hinzugefügt:

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

Schlussendlich wird der Dialog erzeugt und angezeigt:

.. code-block:: java

            builder.create().show();
        }
    }

|step5_finish|


Schritt 6: Konfiguration und Zustand speichern
----------------------------------------------

Die App speichert die Konfiguration noch nicht. Android bietet dafür die
``SharedPreferences`` Klasse an. In ``onCreate()`` wird die Konfiguration
geladen:

.. code-block:: java

    protected void onCreate(Bundle savedInstanceState) {
        // [...]

        SharedPreferences settings = getPreferences(0);
        host.setText(settings.getString("host", host.getText().toString()));
        port.setText(settings.getString("port", port.getText().toString()));
        uid.setText(settings.getString("uid", uid.getText().toString()));
    }

In ``onStop()`` wird die Konfiguration gespeichert:

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

Wenn die Orientierung wechselt dann wird die App beendet und mit der neuen
Orientierung neu gestartet. Dadurch verliert die App die aufgebaute Verbindung.
Daher wird der Verbindungszustand in ``onSaveInstanceState()`` gespeichert:

.. code-block:: java

    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);

        outState.putBoolean("connected", ipcon != null &&
                                         ipcon.getConnectionState() == IPConnection.CONNECTION_STATE_CONNECTED);
    }

Und in ``onCreate()`` wiederhergestellt:

.. code-block:: java

    protected void onCreate(Bundle savedInstanceState) {
        // [...]

        if (savedInstanceState != null && savedInstanceState.getBoolean("connected", false)) {
            new ConnectAsyncTask().execute();
        }
    }

|step6_finish|


Schritt 7: Alles zusammen
-------------------------

|step7_intro|

|step7_together| (`Download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/android/GarageControl/src/com/tinkerforge/garagecontrol/MainActivity.java>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/android/GarageControl/src/com/tinkerforge/garagecontrol/MainActivity.java
 :language: java
 :tab-width: 4
