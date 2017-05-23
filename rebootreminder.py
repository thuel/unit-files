#!/usr/bin/env python

# script to notify admins with an e-mail that the system has rebooted
#    and they should take an special action

import os, subprocess as sp

# list of admins' e-mail adresses:
admins = ["lukas@steffen-steffen.ch"]

# get hostname and define subject and message of notification:
hostname = sp.Popen("cat /etc/hostname", shell=True, stdout=sp.PIPE).communicate()[0].strip()
subject = "The system %s has been rebooted." % hostname
message = "Please log in to start essential services."

# set up the command to be processed:
cmds = []
for admin in admins:
    cmds.append('echo "%s" | mail -s "%s" %s' % (message, subject, admin))
    
for cmd in cmds:
    sp.Popen(cmd, shell=True, stdout=sp.PIPE)


