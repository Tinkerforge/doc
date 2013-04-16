
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit Java auf das LCD 20x4 Bricklet schreiben

.. |ref_CALLBACK_ENUMERATE| replace:: :java:func:`EnumerateListener <IPConnection.EnumerateListener>`
.. |ref_CALLBACK_CONNECTED| replace:: :java:func:`ConnectedListener <IPConnection.ConnectedListener>`
.. |callback| replace:: Listener
.. |ref_enumerate| replace:: :java:func:`Enumerate <IPConnection.Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``illuminance``
.. |cb_humidity| replace:: ``humidity``
.. |cb_air_pressure| replace:: ``airPressure``

.. include:: JavaToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_java_to_lcd:

Mit Java auf das LCD 20x4 Bricklet schreiben
============================================

.. include:: JavaCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: JavaToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

|step1_start_off|

.. code-block:: java

    private static final String host = "localhost";
    private static final int port = 4223;

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: java

    public static void main(String args[]) {
        ipcon = new IPConnection();
        ipcon.connect(host, port);

        weatherListener = new WeatherListener(ipcon);
        ipcon.addEnumerateListener(weatherListener);
        ipcon.addConnectedListener(weatherListener);

        ipcon.enumerate();
    }

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: java

    class WeatherListener implements IPConnection.EnumerateListener,
                                     IPConnection.ConnectedListener {
        public void connected(short connectedReason) {
            if(connectedReason == IPConnection.CONNECT_REASON_AUTO_RECONNECT) {
                ipcon.enumerate();
            }
        }
    }

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: java

    class WeatherListener implements IPConnection.EnumerateListener,
                                     IPConnection.ConnectedListener {
        private IPConnection ipcon = null;

        public WeatherListener(IPConnection ipcon) {
            this.ipcon = ipcon;
        }

        public void connected(short connectedReason) {
            if(connectedReason == IPConnection.CONNECT_REASON_AUTO_RECONNECT) {
                ipcon.enumerate();
            }
        }
    }

    public class WeatherStation {
        private static final String host = "localhost";
        private static final int port = 4223;
        private static IPConnection ipcon = null;
        private static WeatherListener weatherListener = null;

        public static void main(String args[]) {
            ipcon = new IPConnection();
            ipcon.connect(host, port);

            weatherListener = new WeatherListener(ipcon);
            ipcon.addEnumerateListener(weatherListener);
            ipcon.addConnectedListener(weatherListener);

            ipcon.enumerate();
        }
    }


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: java

    public void enumerate(String uid, String connectedUid, char position,
                          short[] hardwareVersion, short[] firmwareVersion,
                          int deviceIdentifier, short enumerationType) {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE) {

|step2_lcd_config|

.. code-block:: java

    if(deviceIdentifier == BrickletLCD20x4.DEVICE_IDENTIFIER) {
        brickletLCD = new BrickletLCD20x4(uid, ipcon);
        brickletLCD.clearDisplay();
        brickletLCD.backlightOn();
    }

|step2_other_config1|

.. code-block:: java

      else if(deviceIdentifier == BrickletAmbientLight.DEVICE_IDENTIFIER) {
        brickletAmbientLight = new BrickletAmbientLight(uid, ipcon);
        brickletAmbientLight.setIlluminanceCallbackPeriod(1000);
        brickletAmbientLight.addIlluminanceListener(this);
    } else if(deviceIdentifier == BrickletHumidity.DEVICE_IDENTIFIER) {
        brickletHumidity = new BrickletHumidity(uid, ipcon);
        brickletHumidity.setHumidityCallbackPeriod(1000);
        brickletHumidity.addHumidityListener(this);
    } else if(deviceIdentifier == BrickletBarometer.DEVICE_IDENTIFIER) {
        brickletBarometer = new BrickletBarometer(uid, ipcon);
        brickletBarometer.setAirPressureCallbackPeriod(1000);
        brickletBarometer.addAirPressureListener(this);
    }

|step2_other_config2|

|step2_put_together|

.. code-block:: java

    public void enumerate(String uid, String connectedUid, char position,
                          short[] hardwareVersion, short[] firmwareVersion,
                          int deviceIdentifier, short enumerationType) {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE) {
            if(deviceIdentifier == BrickletLCD20x4.DEVICE_IDENTIFIER) {
                brickletLCD = new BrickletLCD20x4(uid, ipcon);
                brickletLCD.clearDisplay();
                brickletLCD.backlightOn();
            } else if(deviceIdentifier == BrickletAmbientLight.DEVICE_IDENTIFIER) {
                brickletAmbientLight = new BrickletAmbientLight(uid, ipcon);
                brickletAmbientLight.setIlluminanceCallbackPeriod(1000);
                brickletAmbientLight.addIlluminanceListener(this);
            } else if(deviceIdentifier == BrickletHumidity.DEVICE_IDENTIFIER) {
                brickletHumidity = new BrickletHumidity(uid, ipcon);
                brickletHumidity.setHumidityCallbackPeriod(1000);
                brickletHumidity.addHumidityListener(this);
            } else if(deviceIdentifier == BrickletBarometer.DEVICE_IDENTIFIER) {
                brickletBarometer = new BrickletBarometer(uid, ipcon);
                brickletBarometer.setAirPressureCallbackPeriod(1000);
                brickletBarometer.addAirPressureListener(this);
            }
        }
    }


Schritt 3: Messwerte auf dem Display anzeigen
---------------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: java

    String text = String.format("%6.2f", value);

|step3_printf|

.. code-block:: java

    public void illuminance(int illuminance) {
        String text = String.format("Illuminanc %6.2f lx", illuminance/10.0);
        brickletLCD.writeLine((short)0, (short)0, text);
    }

    public void humidity(int humidity) {
        String text = String.format("Humidity   %6.2f %%", humidity/10.0);
        brickletLCD.writeLine((short)1, (short)0, text);
    }

    public void airPressure(int airPressure) {
        String text = String.format("Air Press %7.2f mb", airPressure/1000.0);
        brickletLCD.writeLine((short)2, (short)0, text);
    }

|step3_temperature|

.. code-block:: java

    public void airPressure(int airPressure) {
        String text = String.format("Air Press %7.2f mb", airPressure/1000.0);
        brickletLCD.writeLine((short)2, (short)0, text);

        int temperature = brickletBarometer.getChipTemperature();
        text = String.format("Temperature %5.2f %cC", temperature/100.0, 0xDF);
        brickletLCD.writeLine((short)3, (short)0, text);
    }

|step3_put_together|

.. code-block:: java

    public void illuminance(int illuminance) {
        String text = String.format("Illuminanc %6.2f lx", illuminance/10.0);
        brickletLCD.writeLine((short)0, (short)0, text);
    }

    public void humidity(int humidity) {
        String text = String.format("Humidity   %6.2f %%", humidity/10.0);
        brickletLCD.writeLine((short)1, (short)0, text);
    }

    public void airPressure(int airPressure) {
        String text = String.format("Air Press %7.2f mb", airPressure/1000.0);
        brickletLCD.writeLine((short)2, (short)0, text);

        int temperature = brickletBarometer.getChipTemperature();
        // 0xDF == ° on LCD 20x4 charset
        text = String.format("Temperature %5.2f %cC", temperature/100.0, 0xDF);
        brickletLCD.writeLine((short)3, (short)0, text);
    }

|step3_complete|

|step3_suggestions1| |step3_suggestions2_common|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

|step4_intro1|

.. code-block:: java

    while(true) {
        try {
            ipcon.connect(host, port);
            break;
        } catch(java.net.UnknownHostException e) {
        } catch(java.io.IOException e) {
        } catch(com.tinkerforge.AlreadyConnectedException e) {
        }

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ei) {
        }
    }

|step4_intro2|

.. code-block:: java

    while(true) {
        try {
            ipcon.enumerate();
            break;
        } catch(com.tinkerforge.NotConnectedException e) {
        }

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ei) {
        }
    }

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: java

    public void illuminance(int illuminance) {
        if(brickletLCD != null) {
            String text = String.format("Illuminanc %6.2f lx", illuminance/10.0);
            try {
                brickletLCD.writeLine((short)0, (short)0, text);
            } catch(com.tinkerforge.TinkerforgeException e) {
            }

            System.out.println("Write to line 0: " + text);
        }
    }

|step4_lcd_initialized2|

.. code-block:: java

    if(deviceIdentifier == BrickletAmbientLight.DEVICE_IDENTIFIER) {
        try {
            brickletAmbientLight = new BrickletAmbientLight(uid, ipcon);
            brickletAmbientLight.setIlluminanceCallbackPeriod(1000);
            brickletAmbientLight.addIlluminanceListener(this);
            System.out.println("AmbientLight initialized");
        } catch(com.tinkerforge.TinkerforgeException e) {
            brickletAmbientLight = null;
            System.out.println("AmbientLight init failed: " + e);
        }
    }

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/java/WeatherStation.java>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/java/WeatherStation.java
 :language: java
 :tab-width: 4
