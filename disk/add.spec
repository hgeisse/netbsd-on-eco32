#
# add.spec -- additional specifications for NetBSD file system
#

.		type dir
dev		type dir
console		type char mode 666 uid 0 gid 0 device 0
dsk0a		type block mode 666 uid 0 gid 0 device netbsd,0,0
dsk0b		type block mode 666 uid 0 gid 0 device netbsd,0,1
dsk0c		type block mode 666 uid 0 gid 0 device netbsd,0,2
dsk0d		type block mode 666 uid 0 gid 0 device netbsd,0,3
