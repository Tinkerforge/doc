// tested with 
// gcc -lpthread -lrt -o example_threshold bricklet_ambient_light.c 
//     ip_connection.c example_threshold.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_ambient_light.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback for illuminance greater than 200 Lux
void cb_reached(uint16_t illuminance) {
	printf("We have %f Lux.\n", illuminance/10.0);
	printf("Too bright, close the curtains!\n");
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


    // Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    ambient_light_set_debounce_period(&al, 10000);

    // Register threshold reached callback to function cb_reached
    ambient_light_register_callback(&al,
	                                AMBIENT_LIGHT_CALLBACK_ILLUMINANCE_REACHED,
	                                cb_reached);
	
    // Configure threshold for "greater than 200 Lux" (unit is Lux/10)
    ambient_light_set_illuminance_callback_threshold(&al, '>', 200*10, 0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
