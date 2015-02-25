#!/usr/bin/env python

import itertools


def main():
        list = 'abcdefghijklmnopqrstuvwxyz'
        list1 = 'abcdefghijklmnopqrstuvwxyz1234567890'
        LIST = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        result = []
        number = 8     #input("What is the maximum passwords length? ")
        if type(number) != int:
                print "Please enter a number."
                main()
        else:
                for zz in range(number+1):
                        for zzz in itertools.product(list1,repeat=zz):
                                print(''.join(zzz))



if __name__ == '__main__':
	main()
