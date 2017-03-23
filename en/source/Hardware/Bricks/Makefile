# Defines
CC=g++
CFLAGS=-c -Wall -I/usr/include/tinkerforge
LIBS=-ltinkerforge -lpthread
EXE=example
SOURCES=example.c
OBJECTS=$(SOURCES:.c=.o)

# Build Rules
all: $(SOURCES) $(EXE)

.c.o:
	$(CC) $(CFLAGS) $< -o $@

$(EXE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXE) $(LIBS)

clean:
	rm -f *.o $(EXE)
