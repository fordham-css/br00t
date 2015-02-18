#!/usr/bin/env python

import itertools

#a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#b = []
#for c in a:
#	b.append(c)
#for d in range(len(a)):
#	for e in range(len(a)):
#		b.append(a[d]+a[e])
#for f in range(len(a)):
#	for g in range(len(a)):
#		for h in range(len(a)): 
#			b.append(a[f]+a[g]+a[h])

#for k in b:
#	print k


def main():
	list = 'abcdefghijklmnopqrstuvwxyz'
	result = []				
	number = 8     #input("What is the maximum passwords length? ")
	if type(number) != int:
		print "Please enter a number."
		main()
	else:
		for i in range(number+1):
			for k in itertools.combinations_with_replacement(list,r=i):
#			z = (itertools.combinations('abcd',r=i))
				print(''.join(k))
#		for j in result:
#			print ' '.join(j)


if __name__ == '__main__':
	main()
