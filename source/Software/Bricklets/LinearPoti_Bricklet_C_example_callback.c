// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_linear_poti.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_linear_poti.h"

#define HOST "localhost"
#define PORT 4223
#define UID "abc" // Change to your UID

// Callback function for position callback (parameter has range 0-100)
void cb_position(uint16_t position) {
	printf("Position: %d\n", position);
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	LinearPoti poti;
	linear_poti_create(&poti, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &poti) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Set Period for position callback to 0.05s (50ms)
	// Note: The position callback is only called every 50ms if the 
	//       position has changed since the last call!
	linear_poti_set_position_callback_period(&poti, 50);

	// Register position callback to function cb_position
	linear_poti_register_callback(&poti,
	                              LINEAR_POTI_CALLBACK_POSITION, 
	                              cb_position);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
