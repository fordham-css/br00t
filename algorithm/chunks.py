#!/usr/bin/python

import sys, itertools, time

if len(sys.argv) < 2:
	print "\nPlease specify a dictionary file to chunk."
	print "\n Example: %s /path/to/dictionary.txt % (sys.argv[0])"

dictionary = sys.argv[1]
list = open(dictionary, 'r')
c = 1

def main(i,c):
	if c >= 14344391:
		sys.exit(1)
	for line in itertools.islice(list,c,None):
		i.append(line.strip())
		if len(i) >= 100:		
			c += 100
			print i
			time.sleep(1)
			return c								



for i in list:
	i = []
	main(i,c)




