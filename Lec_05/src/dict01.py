D = {1:'one','deux':'two','pi':3.14}

D1 =D

print D1

D[1] = 'uno'
print D1

for k in D1.keys():
	print k, '=', D1[k]