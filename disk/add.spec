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
dsk0e		type block mode 666 uid 0 gid 0 device netbsd,0,4

rdsk0a		type char mode 666 uid 0 gid 0 device netbsd,4,0
rdsk0b		type char mode 666 uid 0 gid 0 device netbsd,4,1
rdsk0c		type char mode 666 uid 0 gid 0 device netbsd,4,2
rdsk0d		type char mode 666 uid 0 gid 0 device netbsd,4,3
rdsk0e		type char mode 666 uid 0 gid 0 device netbsd,4,4
