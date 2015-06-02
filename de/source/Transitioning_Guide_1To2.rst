
:breadcrumbs: <a href="index.html">Startseite</a> / <a href="index.html#einstieg">Einstieg</a> / <a href="faq.html">FAQ</a> / Übergang von Protokoll 1.0 auf Protokoll 2.0

.. _transition_1to2:

Übergang von Protokoll 1.0 auf Protokoll 2.0
============================================

Tools und Firmwares aktualisieren
---------------------------------

Aktualisieren auf Protokoll 2.0 ist sehr einfach. Zuerst muss die
:ref:`neueste Version <downloads_tools>` vom Brick Daemon und vom Brick Viewer 
installiert werden.

Danach sollten die Bricks aktualisiert werden, der Aktualisierungsprozess
ist :ref:`hier <brickv_flash_firmware>` beschrieben.

Das Aktualisieren der Bricklets kann automatisiert passieren. Dazu kann
ein Brick mit nicht-aktualisierten Bricklets bestückt werden. Im Brick Viewer
im "Updates" Fenster gibt es im ersten Tab die Möglichkeit alle Bricklets
auf einmal zu aktualisieren. Dazu muss der "Auto-Update All Bricklets"
Knopf angeklickt werden.

.. image:: /Images/Screenshots/bricklet_auto_update.jpg
   :scale: 100 %
   :alt: Bricklet auto update feature of the Brick Viewer
   :align: center
   :target: _images/Screenshots/bricklet_auto_update.jpg

Falls das automatische aktualisieren nicht funktioniert, können die
Bricklets natürlich auch noch auf die 
:ref:`herkömmliche Art und Weise <brickv_flash_plugin>` aktualisiert werden.

Am Ende sollte jede Versionsnummer mit einer "2" beginnen.

Es sollte der Lieferung ein Beipackzettel beigelegen haben. Dieser beschreibt
auch wie Bricks und Bricklets aktualisiert werden können. Wenn keiner oder eine
veraltete Version dabei war, kann die neueste Version des Beipackzettels
`hier <http://download.tinkerforge.com/_stuff/beipackzettel.pdf>`__ 
heruntergeladen werden.

Allgemein
---------

Die IP Connection hat mehrere neue Funktionen die für alle Programmiersprachen
implementiert sind, unter anderem:

* connect
* disconnect
* register_callback (für Enumeration)
* get_connection_state
* set_auto_reconnect
* get_auto_reconnect
* set_timeout
* get_timeout
* wait (Ersatz für join_thread)
* unwait

Zusätzlich hat der Enumeration Callback jetzt eine andere Signatur. Mit
der neuen Signatur werden genug Informationen zurück gegeben um es zu
ermöglichen die komplette Topologie des Netzwerks aus Bricks und Bricklets
aufzustellen.

Die Registrierung und das Auslösen des Enumeration Callbacks ist jetzt in zwei
Schritte unterteilt.

Dokumentation für diese Funktionen kann in der IP Connection Dokumentation
für jede Programmiersprache gefunden werden, siehe 
:ref:`hier <api_bindings>`.

Jedes Brick und Bricklet hat folgende neue Funktionen:

* get_response_expected
* set_response_expected
* set_response_expected_all

Dokumentation für diese Funktionen kann in der normalen Programmiersprachen
Dokumentation der Bricks und Bricklets gefunden werden.

Im folgenden werden wir relevante Codeschnippsel vom alten Protokoll mit
Äquivalenten aus Protokoll 2.0 vergleichen. Dabei sollte beachtet werden,
dass die :ref:`neueste Version der Bindings <downloads_bindings_examples>`
benötigt wird um die neuen Funktionen nutzen zu können.

C/C++
-----

Initialisierung:

.. code-block:: c

    // 1.0
    IPConnection ipcon;
    if(ipcon_create(&ipcon, HOST, PORT) < 0) {
        fprintf(stderr, "Could not create connection\n");
        exit(1);
    }

    AmbientLight al;
    ambient_light_create(&al, UID); 

    if(ipcon_add_device(&ipcon, &al) < 0) {
        fprintf(stderr, "Could not connect to Bricklet\n");
        exit(1);
    }

    ...

    ipcon_destroy(&ipcon);

    // 2.0
    IPConnection ipcon;
    ipcon_create(&ipcon);

    AmbientLight al;
    ambient_light_create(&al, UID, &ipcon); 

    if(ipcon_connect(&ipcon, HOST, PORT) < 0) {
        fprintf(stderr, "Could not connect\n");
        exit(1);
    }

    ...

    ipcon_destroy(&ipcon); // Calls ipcon_disconnect internally

Callbacks:

.. code-block:: c

    // 1.0
    void cb_illuminance(uint16_t illuminance) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE, 
                                    (void *)cb_illuminance);

    // 2.0 (now with user data)
    void cb_illuminance(uint16_t illuminance, void *user_data) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE,
                                    (void *)cb_illuminance,
                                    NULL);

Neue Enumeration-Signatur und Registrierung:

.. code-block:: c

    // 1.0
    void cb_enumerate(char *uid, 
                      char *name, 
                      uint8_t stack_id, 
                      bool is_new);

    ipcon_enumerate(&ipcon, cb_enumerate);

    // 2.0
    void cb_enumerate(const char *uid,
                      const char *connected_uid,
                      char position,
                      uint8_t hardware_version[3],
                      uint8_t firmware_version[3],
                      uint16_t device_identifier,
                      uint8_t enumeration_type,
                      void *user_data);

    ipcon_register_callback(&ipcon,
                            IPCON_CALLBACK_ENUMERATE,
                            (void *)cb_enumerate,
                            NULL);

    ipcon_enumerate(&ipcon);

C#
--

Allgemein:

Es werden keine vorzeichenlosen Datentypen mehr verwendet. Dies war notwendig,
um die C# Bindings :ref:`CLS konform <api_bindings_csharp_cls_complience>` zu
machen, wodurch sie direkt in allen .NET kompatiblen Sprachen verwendet werden
können. Alle vorzeichenlosen Datentypen wurden durch den nächst größeren
vorzeichenbehafteten Datentypen ersetzt.

=============  =============
Datentyp 1.0   Datentyp 2.0
=============  =============
uint16         int32
uint32         int64
uint64         int64
=============  =============

Initialisierung:

.. code-block:: csharp

    // 1.0
    IPConnection ipcon = new IPConnection(HOST, PORT);    
    BrickletAmbientLight al = new BrickletAmbientLight(UID);    
    ipcon.AddDevice(al);
    ...
    ipcon.Destroy();

    // 2.0
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.Connect(HOST, PORT);
    ...
    ipcon.Disconnect();

Callbacks:

.. code-block:: csharp

    // 1.0
    static void IlluminanceCB(ushort illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.RegisterCallback(new BrickletAmbientLight.Illuminance(IlluminanceCB));

    // 2.0: Now with sender object in callback and "+=" syntax to add callback
    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.Illuminance += IlluminanceCB;

Neue Enumeration-Signatur und Registrierung:

.. code-block:: csharp

    // 1.0
    static void EnumerateCB(string uid, 
                            string name, 
                            byte stackID, 
                            bool isNew);

    ipcon.Enumerate(new IPConnection.EnumerateCallback(EnumerateCB));

    // 2.0
    static void EnumerateCB(IPConnection sender,
                            string uid, 
                            string connectedUid, 
                            char position,
                            short[] hardwareVersion, 
                            short[] firmwareVersion,
                            int deviceIdentifier, 
                            short enumerationType);

    ipcon.EnumerateCallback += EnumerateCB;

    ipcon.Enumerate();


Delphi
------

Initialisierung:

.. code-block:: delphi

  { 1.0 }
  ipcon := TIPConnection.Create(HOST, PORT);
  al := TBrickletAmbientLight.Create(UID);
  ipcon.AddDevice(al);
  ...
  ipcon.Destroy;

  { 2.0 }
  ipcon := TIPConnection.Create;
  al := TBrickletAmbientLight.Create(UID, ipcon);
  ipcon.Connect(HOST, PORT);
  ...
  ipcon.Destroy; { Calls ipcon.Disconnect internally }

Callback:

.. code-block:: delphi

  { 1.0 }
  procedure TExample.IlluminanceCB(const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;

  { 2.0: Now with sender object in callback }
  procedure TExample.IlluminanceCB(sender: TBrickletAmbientLight; const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;

Neue Enumeration-Signatur und Registrierung:

.. code-block:: delphi

    { 1.0 }
    procedure TExample.EnumerateCB(const uid: string; 
                                   const name: string; 
                                   const stackID: byte; 
                                   const isNew: boolean);

    ipcon.Enumerate({$ifdef FPC}@{$endif}EnumerateCB);

    { 2.0 }
    procedure TExample.EnumerateCB(sender: TIPConnection;
                                   const uid: string; 
                                   const connectedUid: string; 
                                   const position: char;
                                   const hardwareVersion: TVersionNumber;
                                   const firmwareVersion: TVersionNumber;
                                   const deviceIdentifier: word; 
                                   const enumerationType: byte);

    ipcon.OnEnumerate := {$ifdef FPC}@{$endif}EnumerateCB;

    ipcon.Enumerate();


Java
----

Initialisierung:

.. code-block:: java

    // 1.0
    IPConnection ipcon = new IPConnection(host, port);
    BrickletAmbientLight al = new BrickletAmbientLight(UID);
    ipcon.addDevice(al);
    ...
    ipcon.destroy();

    // 2.0
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.connect(host, port);
    ...
    ipcon.disconnect();

Neue Enumeration-Signatur und Registrierung:

.. code-block:: java

    // 1.0
    ipcon.enumerate(new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String name, 
                              short stackID, 
                              boolean isNew);
    });

    // 2.0
    ipcon.addListener(new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String connectedUid, 
                              char position,
                              short[] hardwareVersion, 
                              short[] firmwareVersion,
                              int deviceIdentifier, 
                              short enumerationType);
    });

    ipcon.enumerate();

Die TimeoutException wurde von
``com.tinkerforge.IPConnection.TimeoutException`` nach
``com.tinkerforge.TimeoutException`` verschoben.

Neuer Ansatz für Listener:

.. code-block:: java

    // 1.0
    brickletTemperature.addListener(new BrickletTemperature.TemperatureListener() {
        public void temperature(short temperature) {
            System.out.println("Temperature: " + temperature/100.0 + " °C");
        }
    });
    // Kein removeListener in 1.0

    // 2.0
    brickletTemperature.addTemperatureListener(new BrickletTemperature.TemperatureListener() {
        public void temperature(short temperature) {
            System.out.println("Temperature: " + temperature/100.0 + " °C");
        }
    });

    // Entfernen von Listener in 2.0 möglich
    brickletTemperature.removeTemperatureListener(temperatureListener);


PHP
---

Initialisierung:

.. code-block:: php

    // 1.0
    $ipcon = new IPConnection($host, $port);
    $al = new BrickletAmbientLight($uid);
    $ipcon->addDevice($al);
    ...
    $ipcon->destroy();

    // 2.0
    $ipcon = new IPConnection();
    $al = new BrickletAmbientLight($uid, $ipcon);
    $ipcon->connect($host, $port);
    ...
    $ipcon->disconnect();

Neue Enumeration-Signatur und Registrierung:

.. code-block:: php

    // 1.0
    function enumerateCB($uid, 
                         $name, 
                         $stackID, 
                         $isNew);

    $ipcon->enumerate('enumerateCB');

    // 2.0
    function enumerateCB($uid, 
                         $connectedUid, 
                         $position,
                         $hardwareVersion,
                         $firmwareVersion,
                         $deviceIdentifier,
                         $enumerationType,
                         $userData);

    $ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE, 'enumerateCB');

    $ipcon->enumerate();


Python
------

Initialisierung:

.. code-block:: python

    # 1.0
    ipcon = IPConnection(HOST, PORT)
    al = AmbientLight(UID)
    ipcon.add_device(al)
    ...
    ipcon.destroy()

    # 2.0
    ipcon = IPConnection()
    al = AmbientLight(UID, ipcon)
    ipcon.connect(HOST, PORT)
    ...
    ipcon.disconnect()

Neue Enumeration-Signatur und Registrierung:

.. code-block:: python

    # 1.0
    def cb_enumerate(uid, 
                     name, 
                     stack_id, 
                     is_new)

    ipcon.enumerate(cb_enumerate)

    # 2.0
    def cb_enumerate(uid, 
                     connected_uid, 
                     position, 
                     hardware_version, 
                     firmware_version,
                     device_identifier, 
                     enumeration_type)

    ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, cb_enumerate)

    ipcon.enumerate()


Ruby
----

Initialisierung:

.. code-block:: ruby

    # 1.0
    ipcon = IPConnection.new HOST, PORT
    al = BrickletAmbientLight.new UID
    ipcon.add_device al
    ...
    ipcon.destroy

    # 2.0
    ipcon = IPConnection.new
    al = BrickletAmbientLight.new UID, ipcon
    ipcon.connect HOST, PORT
    ...
    ipcon.disconnect

Neue Enumeration-Signatur und Registrierung:

.. code-block:: ruby

    # 1.0
    ipcon.enumerate do |uid, 
                        name, 
                        stack_id, 
                        is_new|

    # 2.0
    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, 
                                                                  connected_uid,
                                                                  position,
                                                                  hardware_version, 
                                                                  firmware_version,
                                                                  device_identifier, 
                                                                  enumeration_type|

    ipcon.enumerate
