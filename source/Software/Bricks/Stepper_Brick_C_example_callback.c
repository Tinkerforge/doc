// tested with 
// gcc -lpthread -lrt -o example_callback brick_stepper.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>
#include <stdlib.h>

#include "ip_connection.h"
#include "brick_stepper.h"

#define HOST "localhost"
#define PORT 4223
#define UID "a4LCLTYxDK9" // Change to your UID

Stepper stepper;

// Use position reached callback to program random movement 
void cb_reached(int16_t velocity) {
	int32_t steps;
	if(rand() % 2) {
		steps = (rand() % 4000) + 1000; // steps (forward)
		printf("Driving forward: %d  steps\n", steps);
	} else {
		steps = -((rand() % 4000) + 1000); // steps (backward)
		printf("Driving backward: %d  steps\n", steps);
	}

	int16_t vel = (rand() % 1800) + 200; // steps/s
	uint16_t acc = (rand() % 900) + 100; // steps/s^2
	uint16_t dec = (rand() % 900) + 100; // steps/s^2
	printf("Configuration (vel, acc, dec): %d, %d %d\n", vel, acc, dec);

	stepper_set_speed_ramping(&stepper, acc, dec);
	stepper_set_max_velocity(&stepper, vel);
	stepper_set_steps(&stepper, steps);
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	stepper_create(&stepper, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &stepper) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection


	// Register "position reached callback" to cb_reached
	// cb_reached will be called every time a position set with
	// set_steps or set_target_position is reached
	stepper_register_callback(&stepper, 
	                          STEPPER_CALLBACK_POSITION_REACHED,
							  cb_reached);

	stepper_enable(&stepper);
	// Drive one step forward to get things going
	stepper_set_steps(&stepper, 1);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
