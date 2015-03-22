#
# Makefile for NetBSD disk tools
#

BUILD = ../build

DIRS = dsklbl mkpboot wrpboot loader makefs

.PHONY:		all install clean

all:
		for i in $(DIRS) ; do \
		  $(MAKE) -C $$i all ; \
		done

install:
		mkdir -p $(BUILD)/run/fs-NetBSD
		rm -rf $(BUILD)/run/fs-NetBSD/*
		for i in $(DIRS) ; do \
		  $(MAKE) -C $$i install ; \
		done
		cp Makefile.run $(BUILD)/run/fs-NetBSD/Makefile
		cp add.spec $(BUILD)/run/fs-NetBSD/add.spec
		cp ../os-bin/* $(BUILD)/run/fs-NetBSD

clean:
		for i in $(DIRS) ; do \
		  $(MAKE) -C $$i clean ; \
		done
		rm -f *~
