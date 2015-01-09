def isPal(x):
	""" requires x to be a list,
		return True if the list is a palindrome, False otherwise """
	assert type(x) == list
	temp = x
	print "Before Reverse temp: ", temp
	print "Before Reverse x: ", x
	temp.reverse()
	print "After Reverse temp: ", temp
	print "After Reverse x: ", x
	if temp == x:
		return True
	else:
		return False

def isPalTest():
	L = ['a','b']
	result = isPal(L)

	print "Should print False, ", result

	L = ['a','b','a']
	result = isPal(L)
	print "Should print True, ", result


isPalTest()	
