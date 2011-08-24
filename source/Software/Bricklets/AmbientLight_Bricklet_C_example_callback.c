// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_ambient_light.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_ambient_light.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback function for illuminance callback (parameter has unit Lux/10)
void cb_illuminance(uint16_t illuminance) {
	printf("Illuminance: %f Lux.\n", illuminance/10.0);
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	AmbientLight al;
	ambient_light_create(&al, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &al) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Set Period for illuminance callback to 1s (1000ms)
	// Note: The illuminance callback is only called every second if the 
	//       illuminance has changed since the last call!
	ambient_light_set_illuminance_callback_period(&al, 1000);

	// Register illuminance callback to function cb_illuminance
	ambient_light_register_callback(&al,
	                                AMBIENT_LIGHT_CALLBACK_ILLUMINANCE, 
	                                cb_illuminance);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
