#!/bin/bash

###
# Script purpose: mount external drives in combination with systemd unit file
# Version: 0.1
# Usage: called by systemd unit file
###

#UUIDs of the devices to be mounted
UUID1=UUID
# Eventually more...

if [ $1 = "mount" ]; then
#Eventually a for loop and arrays could be used
  mount UUID=$UUID1 /media/backup/
elif [ $1 = "unmount" ]; then
  umount UUID=$UUID1
else
  exit 1
fi

exit 0
