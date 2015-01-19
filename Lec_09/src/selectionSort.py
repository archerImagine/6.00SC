def selectionSort(L):
	"""
		Assumes that L is a list of elements which can be compared using >
		Sorts L in asscending order
	"""
	print "len(L): ", len(L)
	for i in range(len(L) - 1):
		print "::::::::::::::::i: ", i
		#Invariant: the list L[:i] is sorted.
		minIndex = i
		minValue = L[i]
		j = i + 1
		while j < len(L):
			print "j: ", j
			if minValue > L[j]:
				minIndex = j
				minValue = L[j]
			j += 1
			temp = L[i]
			L[i] = L[minIndex]
			L[minIndex] = temp 
			print "L: ", L



L = [35, 4, 5, 29, 17, 58, 0]		
print L
selectionSort(L)	
print L