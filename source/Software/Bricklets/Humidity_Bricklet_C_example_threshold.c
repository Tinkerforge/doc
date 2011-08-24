// tested with 
// gcc -lpthread -lrt -o example_threshold bricklet_humidity.c 
//     ip_connection.c example_threshold.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_humidity.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback for humidity outside of 30 to 60 %RH
void cb_reached(uint16_t humidity) {
	if(humidity < 30) {
		printf("Humidity too low: %f %%RH\n", humidity/10.0);
	}
	if(humidity > 60) {
		printf("Humidity too high: %f %%RH\n", humidity/10.0);
	}

	printf("Recommended humiditiy for human comfort is 30 to 60 %%RH.\n");
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Humidity h;
	humidity_create(&h, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &h) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

    // Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    humidity_set_debounce_period(&h, 10000);

    // Register threshold reached callback to function cb_reached
    humidity_register_callback(&h,
	                           HUMIDITY_CALLBACK_HUMIDITY_REACHED,
	                           cb_reached);
	
	// Configure threshold for "outside of 30 to 60 %RH" (unit is %RH/10)
    humidity_set_humidity_callback_threshold(&h, 'o', 30*10, 60*10);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
