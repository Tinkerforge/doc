// tested with 
// gcc -lpthread -lrt -o example_configuration brick_dc.c 
//     ip_connection.c example_configuration.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "brick_dc.h"

#define HOST "localhost"
#define PORT 4223
#define UID "apaYPikNHEj" // Change to your UID

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	DC dc;
	dc_create(&dc, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &dc) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	dc_set_pwm_frequency(&dc, 10000); // Use PWM frequency of 10khz
	dc_set_drive_mode(&dc, 1); // use 1 = Drive/Coast instead of 0 = Drive/Brake

	dc_enable(&dc);
	dc_set_acceleration(&dc, 5000); // Slow acceleration
	dc_set_velocity(&dc, 32767); // Full speed

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
