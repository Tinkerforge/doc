using Tinkerforge;

class Example
{
	private static string HOST = "localhost";
	private static int PORT = 4223;

	// Print incoming enumeration
	static void EnumerateCB(object sender, string UID, string connectedUID, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)
	{
		System.Console.WriteLine("Sender:           " + sender);
		System.Console.WriteLine("UID:              " + UID);
		System.Console.WriteLine("enumerationType:  " + enumerationType);
		if(enumerationType == IPConnection.ENUMERATION_TYPE_DISCONNECTED)
		{
			return;
		}

		System.Console.WriteLine("connectedUID:     " + connectedUID);
		System.Console.WriteLine("position:         " + position);
		System.Console.WriteLine("hardwareVersion:  " + hardwareVersion[0] + "." + hardwareVersion[1] + "." + hardwareVersion[2]);
		System.Console.WriteLine("firmwareVersion:  " + firmwareVersion[0] + "." + firmwareVersion[1] + "." + firmwareVersion[2]);
		System.Console.WriteLine("deviceIdentifier: " + deviceIdentifier);
	}

	static void Main() 
	{
		// Create connection and connect to brickd
		IPConnection ipcon = new IPConnection();
		ipcon.Connect(HOST, PORT);

		// Register Enumerate Callback
		ipcon.EnumerateCallback += EnumerateCB;

		System.Console.WriteLine("Press key to exit");
		System.Console.ReadKey();
	}
}
