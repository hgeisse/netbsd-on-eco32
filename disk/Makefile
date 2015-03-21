#
# Makefile for NetBSD disk tools
#

BUILD = ../build

#DIRS = dsklbl mkpboot wrboot makefs loader
DIRS = dsklbl mkpboot

.PHONY:		all install clean

all:
		for i in $(DIRS) ; do \
		  $(MAKE) -C $$i all ; \
		done

install:
		for i in $(DIRS) ; do \
		  $(MAKE) -C $$i install ; \
		done
		mkdir -p $(BUILD)/run/fs-NetBSD
		cp Makefile.run $(BUILD)/run/fs-NetBSD/Makefile
		cp add.spec $(BUILD)/run/fs-NetBSD/add.spec

clean:
		for i in $(DIRS) ; do \
		  $(MAKE) -C $$i clean ; \
		done
		rm -f *~
