using Tinkerforge;

class Example
{
	private static string host = "localhost";
	private static int port = 4223;

	static void EnumerateCB(string uid, string name, byte stackID, bool isNew)
	{
		if(isNew)
		{
			System.Console.WriteLine("New Device:");
		}
		else
		{
			System.Console.WriteLine("Device Removed:");
		}

		System.Console.WriteLine(" Name:     " + name);
		System.Console.WriteLine(" UID:      " + uid);
		System.Console.WriteLine(" Stack ID: " + stackID);
	}

	static void Main() 
	{
		IPConnection ipcon = new IPConnection(host, port);
		ipcon.Enumerate(new IPConnection.EnumerateCallback(EnumerateCB));

		System.Console.WriteLine("Press key to exit");
		System.Console.ReadKey();
		ipcon.Destroy();
    }
}
