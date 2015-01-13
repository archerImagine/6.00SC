def search(L,e):
	for elem in L:
		if elem == e:
			return True
		if elem > e:
			return False
	return False


L = range(100)	
print search(L, 0)
print search(L, 50)
print search(L, 100)