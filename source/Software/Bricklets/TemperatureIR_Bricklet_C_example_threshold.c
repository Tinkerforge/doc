// tested with 
// gcc -lpthread -lrt -o example_threshold bricklet_temperature_ir.c 
//     ip_connection.c example_threshold.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_temperature_ir.h"

#define HOST "localhost"
#define PORT 4223
#define UID "abcde" // Change to your UID

// Callback for object temperature greater than 100 °C
// (parameter has unit °C/10)
void cb_reached(uint16_t temperature) {
	printf("The surface has a temperature of %f °C\n", temperature/10.0);
	printf("Far too hot, start the fan!\n");
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	TemperatureIR tir;
	temperature_ir_create(&tir, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &tir) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

    // Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    temperature_ir_set_debounce_period(&tir, 10000);

    // Register threshold reached callback to function cb_reached
    temperature_ir_register_callback(&tir,
	                                 TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE_REACHED,
	                                 cb_reached);
	
	// Configure threshold for "greater than 100 °C" (unit is °C/10)
    temperature_ir_set_object_temperature_callback_threshold(&tir, 
	                                                         '>', 
															 100*10, 
															 0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
