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
   :target: ../_images/Screenshots/bricklet_auto_update.jpg

Falls das automatische aktualisieren nicht funktioniert, können die
Bricklets natürlich auch noch auf die 
:ref:`herkömmliche Art und Weise <brickv_flash_plugin>` aktualisiert werden.

Am Ende sollte jede Versionsnummer mit einer "2" beginnen.

Allgemein
---------

Die IPConnection hat mehrere neue Funktionen die für alle Programmiersprachen
implementiert sind, unter anderem:

* connect
* disconnect
* register_callback (for enumeration)
* get_connection_state
* set_auto_reconnect
* get_auto_reconnect
* set_timeout
* get_timeout
* wait (replacement for join)
* unwait

Zusätzlich hat der Enumeration Callback jetzt eine andere Signatur. Mit
der neuen Signatur werden genug Informationen zurück gegeben um es zu
ermöglichen die komplette Topologie des Netzwerks aus Bricks und Bricklets
aufzustellen.

Dokumentation für diese Funktionen kann in der IPConnection Dokumentation
für jede Programmiersprache gefunden werden, siehe 
:ref:`hier <api_bindings_ip_connection>`.

Jedes Brick und Bricklet hat folgende neue Funktionen:

* get_response_expected
* set_response_expected
* set_response_expected_all

Dokumentation für diese Funktionen kann in der normalen Programmiersprachen
Dokumentation der Bricks und Bricklets gefunden werden.

Im folgenden werden wir relevante Codeschnippsel vom alten Protokoll mit
äquivalten aus Protokoll 2..0 vergleichen. Dabei sollte beachtet werden,
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

    // 2.0
    IPConnection ipcon;
    ipcon_create(&ipcon);

    AmbientLight al;
    ambient_light_create(&al, UID, &ipcon); 

    if(ipcon_connect(&ipcon, HOST, PORT) < 0) {
        fprintf(stderr, "Could not connect\n");
        exit(1);
    }

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

Neue Enumeration-Signatur:

.. code-block:: c

    // 1.0
    void cb_enumerate(char *uid, 
                      char *name, 
                      uint8_t stack_id, 
                      bool is_new)

    // 2.0
    void cb_enumerate(const char *uid,
                      const char *connected_uid,
                      char position,
                      uint8_t hardware_version[3],
                      uint8_t firmware_version[3],
                      uint16_t device_identifier,
                      uint8_t enumeration_type,
                      void *user_data)

C#
--

General:

There are no unsigned data types used anymore. This was necessary to make
the C# bindings CLS complient (i.e. they can be easily used from other 
.net languages). All unsigned data types have been replaced by the next
higher signed data type.

=============  =============
Data type 1.0  Data type 2.0
=============  =============
uint8          int16
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

    // 2.0
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.Connect(HOST, PORT);


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

Neue Enumeration-Signatur:

.. code-block:: csharp

    // 1.0
    static void EnumerateCB(string uid, 
                            string name, 
                            byte stackID, 
                            bool isNew)

    // 2.0
    static void EnumerateCB(IPConnection sender,
                            string uid, 
                            string connectedUid, 
                            char position,
                            short[] hardwareVersion, 
                            short[] firmwareVersion,
                            int deviceIdentifier, 
                            short enumerationType)

Delphi
------

Initialisierung:

.. code-block:: delphi

  { 1.0 }
  ipcon := TIPConnection.Create(HOST, PORT);
  al := TBrickletAmbientLight.Create(UID);
  ipcon.AddDevice(al);

  { 2.0 }
  ipcon := TIPConnection.Create;
  al := TBrickletAmbientLight.Create(UID, ipcon);
  ipcon.Connect(HOST, PORT);


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

Neue Enumeration-Signatur:

.. code-block:: delphi

    { 1.0 }
    procedure TExample.EnumerateCB(const uid: string; 
                                   const name: string; 
                                   const stackID: byte; 
                                   const isNew: boolean);

    { 2.0 }
    procedure TExample.EnumerateCB(sender: TIPConnection;
                                   const uid: string; 
                                   const connectedUid: string; 
                                   const position: char;
                                   const hardwareVersion: TVersionNumber;
                                   const firmwareVersion: TVersionNumber;
                                   const deviceIdentifier: word; 
                                   const enumerationType: byte);


Java
----

Initialisierung:

.. code-block:: java

    // 1.0
    IPConnection ipcon = new IPConnection(host, port);
    BrickletAmbientLight al = new BrickletAmbientLight(UID);
    ipcon.addDevice(al);

    // 2.0
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.connect(host, port);

Neue Enumeration-Signatur:

.. code-block:: java

    // 1.0
    new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String name, 
                              short stackID, 
                              boolean isNew);
    }

    // 2.0
    new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String connectedUid, 
                              char position,
                              short[] hardwareVersion, 
                              short[] firmwareVersion,
                              int deviceIdentifier, 
                              short enumerationType);
    }

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

    // 2.0
    $ipcon = new IPConnection();
    $al = new BrickletAmbientLight($uid, $ipcon);
    $ipcon->connect($host, $port);

Neue Enumeration-Signatur:

.. code-block:: php

    // 1.0
    function enumerateCB($uid, 
                         $name, 
                         $stackID, 
                         $isNew)

    // 2.0
    function enumerateCB($uid, 
                         $connectedUid, 
                         $position,
                         $hardwareVersion,
                         $firmwareVersion,
                         $deviceIdentifier,
                         $enumerationType,
                         $userData)

Python
------

Initialisierung:

.. code-block:: python

    # 1.0
    ipcon = IPConnection(HOST, PORT)
    al = AmbientLight(UID)
    ipcon.add_device(al)

    # 2.0
    ipcon = IPConnection()
    al = AmbientLight(UID, ipcon)
    ipcon.connect(HOST, PORT)

Neue Enumeration-Signatur:

.. code-block:: python

    # 1.0
    def cb_enumerate(uid, 
                     name, 
                     stack_id, 
                     is_new)

    # 2.0
    def cb_enumerate(uid, 
                     connected_uid, 
                     position, 
                     hardware_version, 
                     firmware_version,
                     device_identifier, 
                     enumeration_type)

Ruby
----

Initialisierung:

.. code-block:: ruby

    # 1.0
    ipcon = IPConnection.new HOST, PORT
    al = BrickletAmbientLight.new UID
    ipcon.add_device al

    # 2.0
    ipcon = IPConnection.new
    al = BrickletAmbientLight.new UID, ipcon
    ipcon.connect HOST, PORT

Neue Enumeration-Signatur:

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
