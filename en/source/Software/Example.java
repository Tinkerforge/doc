import com.tinkerforge.IPConnection;

public class Example {
	private static final String host = "localhost";
	private static final int port = 4223;

    // Note: To make the example code cleaner we do not handle exceptions. Exceptions you
    //       might normally want to catch are described in the documentation
    public static void main(String args[]) throws Exception {
        // Create connection and connect to brickd
        IPConnection ipcon = new IPConnection();
		ipcon.connect(host, port);

        // Register enumerate listener and print incoming information
        ipcon.addListener(new IPConnection.EnumerateListener() {
            public void enumerate(String UID, String connectedUID, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType) {
                System.out.println("UID:               " + UID);
                System.out.println("enumeration type:  " + enumerationType);
				
				if(enumerationType == IPConnection.ENUMERATION_TYPE_DISCONNECTED) {
					return;
				}

				System.out.println("connected UID:     " + connectedUID);
				System.out.println("position:          " + position);
				System.out.println("hardware version:  " + hardwareVersion[0] + "." + hardwareVersion[1] + "." + hardwareVersion[2]);
				System.out.println("firmware version:  " + firmwareVersion[0] + "." + firmwareVersion[1] + "." + firmwareVersion[2]);
				System.out.println("device identifier: " + deviceIdentifier);
            }
        });

		ipcon.enumerate();
        System.console().readLine("Press key to exit\n");
    }
}
