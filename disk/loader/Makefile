#
# Makefile to build the NetBSD system loader
#

BUILD = ../../build

.PHONY:		all install clean

all:		loader.bin

install:	loader.bin
		mkdir -p $(BUILD)/run/fs-NetBSD
		cp loader.bin $(BUILD)/run/fs-NetBSD

loader.bin:	loader
		$(BUILD)/bin/load -p loader loader.bin

loader:		c0.o loader.o auxlib.o biolib.o
		$(BUILD)/bin/ld -s stage2.lnk -o loader \
		  c0.o loader.o auxlib.o biolib.o

c0.o:		c0.s
		$(BUILD)/bin/as -o c0.o c0.s

loader.o:	loader.c
		$(BUILD)/bin/lcc -A -c -o loader.o loader.c

auxlib.o:	auxlib.c
		$(BUILD)/bin/lcc -A -c -o auxlib.o auxlib.c

biolib.o:	biolib.s
		$(BUILD)/bin/as -o biolib.o biolib.s

clean:
		rm -f *~ c0.o loader.o auxlib.o biolib.o
		rm -f loader loader.bin
