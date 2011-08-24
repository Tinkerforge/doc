// tested with 
// gcc -lpthread -lrt -o example_callback brick_servo.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "brick_servo.h"

#define HOST "localhost"
#define PORT 4223
#define UID "aySDPqVAkmw" // Change to your UID

Servo servo;

// Use position reached callback to swing back and forth
void cb_reached(uint8_t servo_num, int16_t position) {
	if(position == 9000) {
		printf("Position: 90°, going to -90°\n");
		servo_set_position(&servo, servo_num, -9000);
	} else if(position == -9000) {
		printf("Position: -90°, going to 90°\n");
		servo_set_position(&servo, servo_num, 9000);
	} else {
		printf("Error\n"); // Can only happen if another program sets position
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
	servo_create(&servo, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &servo) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection


	// Register "position reached callback" to cb_reached
	// cb_reached will be called every time a position set with
	// set_position is reached
	servo_register_callback(&servo, 
	                        SERVO_CALLBACK_POSITION_REACHED, 
							cb_reached);

	// Set velocity to 100°/s. This has to be smaller or equal to 
	// maximum velocity of the servo, otherwise cb_reached will be
	// called to early.
	servo_set_velocity(&servo, 0, 10000); 
	servo_set_position(&servo, 0, 9000);
	servo_enable(&servo, 0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
