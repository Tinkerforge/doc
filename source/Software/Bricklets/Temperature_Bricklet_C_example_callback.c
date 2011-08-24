// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_temperature.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_temperature.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback function for temperature callback (parameter has unit °C/100)
void cb_temperature(int16_t temperature) {
	printf("Temperature: %f °C.\n", temperature/100.0);
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Temperature t;
	temperature_create(&t, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &t) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Set Period for temperature callback to 1s (1000ms)
	// Note: The callback is only called every second if the 
	//       temperature has changed since the last call!
	temperature_set_temperature_callback_period(&t, 1000);

	// Register temperature callback to function cb_temperature
	temperature_register_callback(&t,
	                              TEMPERATURE_CALLBACK_TEMPERATURE, 
	                              cb_temperature);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
