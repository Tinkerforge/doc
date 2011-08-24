#include <stdio.h>
#include <stdbool.h>

#include "ip_connection.h"
#include "brick_dc.h"

//#include <unistd.h>

#define HOST "localhost"
#define PORT 4223
#define DC_UID "J"

int main() {
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	DC dc;
	dc_create(&dc, DC_UID);
	if(ipcon_add_device(&ipcon, &dc) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}

	dc_enable(&dc);

	dc_set_acceleration(&dc, 10000);

	dc_set_velocity(&dc, 30000);
	usleep(3000000);

	dc_set_velocity(&dc, 0);
	usleep(3000000);

	ipcon_destroy(&ipcon);
}
