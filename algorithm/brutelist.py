a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = []
for i in range(len(a)):
	for j in range(len(a)):
		b.append(a[i]+a[j])
for k in b:
	print k
				
