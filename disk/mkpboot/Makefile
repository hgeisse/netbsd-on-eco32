#
# Makefile to build the partition boot block (with an empty disklabel)
#

BUILD = ../../build

.PHONY:		all install clean

all:		pbootblk

install:	pbootblk
		mkdir -p $(BUILD)/run/fs-NetBSD
		cp pbootblk $(BUILD)/run/fs-NetBSD

pbootblk:	stage1/pbr.bin stage2/pboot.bin
		dd if=/dev/zero of=./zeroes bs=512 count=1
		cat stage1/pbr.bin zeroes stage2/pboot.bin >pbootblk

stage1/pbr.bin:
		$(MAKE) -C stage1

stage2/pboot.bin:
		$(MAKE) -C stage2

clean:
		$(MAKE) -C stage1 clean
		$(MAKE) -C stage2 clean
		rm -f *~ zeroes pbootblk
