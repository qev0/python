#!/usr/bin/python
#
#

import pexpect 
#Set backup script command
backupScript = "./backup.sh"

#Set netscaler password
nspass = '3Bl1ndM1ce'

#Set netscaler IP to backup
nsDMZ = 'ssh nsroot@192.168.64.220'



print "spawning an ssh process to 192.168.64.220"
print ""
#Spawn an ssh session 
process = pexpect.spawn(nsDMZ)

print "ssh'd to the dmz netscaler successfully"
print ""
print "trying the password" 
#look for the password prompt
process.expect('.*assword:*')

print ""
#send the password
process.sendline(nspass)

print "successfully logged in"
print ""
process.expect('.*>')

print "entering the netscaler shell"
process.sendline('shell')

print ""
print "expecting the root prompt"

process.expect('root@bknsprtl01#')

print ""
print "cd to /nsconfig"
process.sendline('cd /nsconfig')
print ""
print "expect the root prompt again"
process.expect('root@bknsprtl01#')
print ""
print "running the shell scritp to backup"
process.sendline('./backup.sh')
print ""
print "expect root prompt again"
process.expect('root@bknsprtl01#')
print ""
process.sendline('exit')
process.sendline('exit')


#print "allow interaction for debugging"
#process.interact()

