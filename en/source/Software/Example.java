import com.tinkerforge.IPConnection;

public class Example {
	private static final String host = "localhost";
	private static final int port = 4223;

	// Note: To make the example code cleaner we do not handle exceptions. Exceptions you
	//       might normally want to catch are described in the comments below
	public static void main(String args[]) throws Exception {
		// Create connection to brickd
		IPConnection ipcon = new IPConnection(host, port); // Can throw IOException

		// Register enumerate listener and print incoming information
		ipcon.enumerate(new IPConnection.EnumerateListener() {
			public void enumerate(String uid, String name, short stackID, boolean isNew) {
				if(isNew) {
					System.out.println("New device:");
				} else {
					System.out.println("Removed device:");
				}

				System.out.println(" Name:     " + name);
				System.out.println(" UID:      " + uid);
				System.out.println(" Stack ID: " + stackID);
				System.out.println("");
			}
		});

		System.console().readLine("Press key to exit\n");
		ipcon.destroy();
	}
}
