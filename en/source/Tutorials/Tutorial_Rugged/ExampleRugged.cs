using Tinkerforge;

// This class will use any LCD Bricklet and Temperature Bricklet that
// are connected to the PC and display the temperature on the LCD.
//
// The program should stay stable if Bricks are connected/disconnected,
// if the Brick Daemon is restarted or if a Wi-Fi/RS485 connection is lost.
// It will also keep working if you exchange the Master or one of the
// Bricklets by a new one of the same type.
//
// If a Brick or Bricklet loses its state (e.g. callback configuration)
// while the connection was lost, it will automatically be reconfigured
// accordingly.
class ExampleRugged
{
	private static string HOST = "localhost";
	private static int PORT = 4223;

	private static IPConnection ipcon = null;
	private static BrickletLCD20x4 lcd = null;
	private static BrickletTemperature temp = null;

	static void Main() 
	{
		// Create IP Connection
		ipcon = new IPConnection();

		// Register IP Connection callbacks
		ipcon.EnumerateCallback += EnumerateCB;
		ipcon.Connected += ConnectedCB;

		// Connect to brickd, will trigger cb_connected
		ipcon.Connect(HOST, PORT); 
		ipcon.Enumerate();

		System.Console.WriteLine("Press key to exit");
		System.Console.ReadKey();
		ipcon.Disconnect();
	}

	// Callback updates temperature displayed on lcd
	static void TemperatureCB(BrickletTemperature sender, short temperature)
	{
		if(lcd != null)
		{
			lcd.ClearDisplay();
			string s = "Temperature: " + temperature/100.0 + (char)0xdf + "C";
			lcd.WriteLine(0, 0, s);
		}
	}

	// Callback switches lcd backlight on/off based on lcd button 0
	static void ButtonPressedCB(BrickletLCD20x4 sender, byte button)
	{
		if(lcd != null)
		{
			if(button == 0)
			{
				if(lcd.IsBacklightOn())
				{
					lcd.BacklightOff();
				}
				else
				{
					lcd.BacklightOn();
				}
			}
		}
	}

	// Callback handles device connections and configures possibly lost
	// configuration of lcd and temperature callbacks, backlight etc.
	static void EnumerateCB(IPConnection sender, string UID, string connectedUID, 
	                        char position, short[] hardwareVersion, 
	                        short[] firmwareVersion, int deviceIdentifier, 
	                        short enumerationType)
	{
		if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
		   enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE)
		{
			// Enumeration is for LCD Bricklet
			if(deviceIdentifier == BrickletLCD20x4.DEVICE_IDENTIFIER)
			{
				// Create lcd device object
				lcd = new BrickletLCD20x4(UID, ipcon);
				lcd.ButtonPressed += ButtonPressedCB;

				lcd.ClearDisplay();
				lcd.BacklightOn();
			}
			// Enumeration is for Temperature Bricklet
			if(deviceIdentifier == BrickletTemperature.DEVICE_IDENTIFIER)
			{
				// Create temperature device object
				temp = new BrickletTemperature(UID, ipcon);
				temp.Temperature += TemperatureCB;

				temp.SetTemperatureCallbackPeriod(50);
			}
		}
	}

	// Callback handles reconnection of IP Connection
	static void ConnectedCB(IPConnection sender, short connectReason)
	{
		// Enumerate devices again. If we reconnected, the Bricks/Bricklets
		// may have been offline and the configuration may be lost.
		// In this case we don't care for the reason of the connection
		ipcon.Enumerate();
	}
}
