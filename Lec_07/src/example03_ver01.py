def isPal(x):
	""" requires x to be a list,
		return True if the list is a palindrome, False otherwise """
	assert type(x) == list
	temp = x
	temp.reverse
	if temp == x:
		return True
	else:
		return False

def silly(n):
	""" requires: n is an int > 0
		Gets n input from user
		Prints Yes, if the input is a palindrome; No otherwise"""
	assert type(n) == int and n > 0
	for i in range(n):
		result = []
		elem = raw_input("Enter Something: ")
		print "result: ", result
		result.append(elem)
	if isPal(result):
		print 'Is a palindrome'
	else:
		print "Is not a palindrome"


silly(2)		
		