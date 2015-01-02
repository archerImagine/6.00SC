def keySearch(L,k):
	for elem in L:
		if elem[0] == k:
			return elem[1]
	return None

myList = [
			[1,"One"],
			[2,"Two"],
		]
for e in myList:
	print "e = ", e

print "keySearch(myList,1): ", keySearch(myList,1)		