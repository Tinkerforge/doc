// tested with 
// gcc -lpthread -lrt -o example_threshold bricklet_distance_ir.c 
//     ip_connection.c example_threshold.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_distance_ir.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback for distance smaller than 20cm
void cb_reached(uint16_t distance) {
	printf("Distance is smaller than 20cm: %f cm\n", distance/10.0);
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	DistanceIR dist;
	distance_ir_create(&dist, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &dist) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection


    // Get threshold callbacks with a debounce time of 1 second (1000ms)
    distance_ir_set_debounce_period(&dist, 1000);

    // Register threshold reached callback to function cb_reached
    distance_ir_register_callback(&dist,
	                              DISTANCE_IR_CALLBACK_DISTANCE_REACHED,
	                              cb_reached);
	
    // Configure threshold for "smaller than 20cm" (unit is mm)
    distance_ir_set_distance_callback_threshold(&dist, '<', 200, 0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
