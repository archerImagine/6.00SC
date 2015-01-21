def mergeSort(left,right,lt):
	"""
		Assumes left and right are sorted list.
		lt defines the ordering on the elements of the list.
		Returns a new sorted(by lt) list containing the same elements as 
		left + right would contain.
	"""
	result = []
	i,j = 0,0
	while i < len(left) and j < len(right):
		if lt(left[i],right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result

def sort(L,lt = lambda x,y: x < y):
		"""
			Returns a new sorted list containing the same elements as L
		"""	
		if len(L) < 2:
			return L[:]
		else:
			middle = int(len(L)/2)
			
			left = sort(L[:middle],lt)
			right = sort(L[middle:],lt)
			print "left: ", left, "right: ", right
			return mergeSort(left,right,lt)

L = [35, 4, 5, 29, 17, 58, 0]
newL = sort(L)
print 'Sorted list =', newL			