// tested with 
// gcc -lpthread -lrt -o example_configuration brick_stepper.c 
//     ip_connection.c example_configuration.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "brick_stepper.h"

#define HOST "localhost"
#define PORT 4223
#define UID "a4LCLTYxDK9" // Change to your UID

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Stepper stepper;
	stepper_create(&stepper, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &stepper) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection


	stepper_set_motor_current(&stepper, 800); // 800mA
	stepper_set_step_mode(&stepper, 8); // 1/8 step mode
	stepper_set_decay(&stepper, 12000); // Mixed decay mode

	stepper_set_max_velocity(&stepper, 2000); // Velocity 2000 steps/s
	// Slow acceleration (500 steps/s^2), 
	// Fast deacceleration (5000 steps/s^2)
	stepper_set_speed_ramping(&stepper, 500, 5000);

	stepper_enable(&stepper);
	stepper_set_steps(&stepper, 60000); // Drive 60000 steps forward

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
