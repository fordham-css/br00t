#!/usr/bin/env python

import itertools

#a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#b = []
#z = range(len(a))

#########################################################################

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
                        for zzz in itertools.product(list,repeat=zz):
                                print(''.join(zzz))

#########################################################################

#for c in a:
#	b.append(c)
#for d in z:
#	for e in z:
#		b.append(a[d]+a[e])
#for f in z:
#	for g in z:
#		for h in z: 
#			b.append(a[f]+a[g]+a[h])
#for i in z:
#	for j in z:
#		for k in z:
#			for l in z:
#				b.append(a[i]+a[j]+a[k]+a[l])
#for m in z:
#	for n in z:
#		for o in z:
#			for p in z:
#				for q in z:
#					b.append(a[m]+a[n]+a[o]+a[p]+a[q])
#for r in z:
#	for s in z:
#		for t in z:
#			for u in z:
#				for v in z:
#					for w in z:
#						b.append(a[r]+a[s]+a[t]+a[u]+a[v]+a[w])
#for x in z:
#	for y in z:
#		for aa in z:
#			for ab in z:
#				for ac in z:
#					for ad in z:
#						for ae in z:
#							b.append(a[x]+a[y]+a[aa]+a[ab]+a[ac]+a[ad]+a[ae])
#for af in z:
#	for ag in z:
#		for ah in z:
#			for ai in z:
#				for aj in z:
#					for ak in z:
#						for al in z:
#							for am in z:
#								b.append(a[af]+a[ag]+a[ah]+a[ai]+a[aj]+a[ak]+a[al]+a[am])
									
#for each in b:
#	print each

#########################################################################

if __name__ == '__main__':
	main()
