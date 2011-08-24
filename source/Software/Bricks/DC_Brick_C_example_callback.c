// tested with 
// gcc -lpthread -lrt -o example_callback brick_dc.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "brick_dc.h"

#define HOST "localhost"
#define PORT 4223
#define UID "apaYPikNHEj" // Change to your UID

DC dc;

// Use velocity reached callback to swing back and forth
void cb_reached(int16_t velocity) {
	if(velocity == 32767) {
		printf("Velocity: Full Speed forward, turning backward\n");
		dc_set_velocity(&dc, -32767);
	} else if(velocity == -32767) {
		printf("Velocity: Full Speed backward, turning forward\n");
		dc_set_velocity(&dc, 32767);
	} else {
		printf("Error\n"); // Can only happen if another program sets velocity
	}
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	dc_create(&dc, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &dc) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection


	// Register "velocity reached callback" to cb_reached
	// cb_reached will be called every time a velocity set with
	// set_velocity is reached
	dc_register_callback(&dc, DC_CALLBACK_VELOCITY_REACHED, cb_reached);

	dc_enable(&dc);
	// The acceleration has to be smaller or equal to the maximum acceleration
	// of the dc motor, otherwise cb_reached will be called too early
	dc_set_acceleration(&dc, 5000); // Slow acceleration
	dc_set_velocity(&dc, 32767); //Full speed forward

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
