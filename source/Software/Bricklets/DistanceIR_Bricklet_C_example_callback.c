// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_distance_ir.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_distance_ir.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback function for distance callback (parameter has unit mm)
void cb_distance(uint16_t distance) {
	printf("Distance: %f cm\n", distance/10.0);
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

	// Set Period for distance callback to 0.2s (200ms)
	// Note: The callback is only called every 200ms if the 
	//       distance has changed since the last call!
	distance_ir_set_distance_callback_period(&dist, 200);

	// Register distance callback to function cb_distance
	distance_ir_register_callback(&dist,
	                              DISTANCE_IR_CALLBACK_DISTANCE, 
	                              cb_distance);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
