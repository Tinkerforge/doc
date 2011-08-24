// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_temperature_ir.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_temperature_ir.h"

#define HOST "localhost"
#define PORT 4223
#define UID "abcde" // Change to your UID

// Callback functions for object/ambient temperature callbacks
// (parameters have unit °C/10)
void cb_object(uint16_t temperature) {
	printf("Object Temperature: %f °C.\n", temperature/10.0);
}

void cb_ambient(uint16_t temperature) {
	printf("Ambient Temperature: %f °C.\n", temperature/10.0);
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

	// Set Period for temperature callbacks to 1s (1000ms)
	// Note: The callbacks are only called every second if the 
	//       value has changed since the last call!
	temperature_ir_set_object_temperature_callback_period(&tir, 1000);
	temperature_ir_set_ambient_temperature_callback_period(&tir, 1000);

	// Register object temperature callback to function cb_object
	temperature_ir_register_callback(&tir,
	                                 TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE, 
	                                 cb_object);

	// Register ambient temperature callback to function cb_ambient
	temperature_ir_register_callback(&tir,
	                                 TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE, 
	                                 cb_ambient);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
