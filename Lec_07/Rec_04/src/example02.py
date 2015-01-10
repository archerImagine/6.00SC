# Iteratative Fibonacci series.

def iteratativeFibonacci(n):
	""" An Iteratative function to find the nth Fibonacci number,
		n is an int and >= 0
	"""
	if n == 0 and n == 1 :
		return n
	else:
		# Hold the currect and the previous Fibonacci number
		previousFib = 0
		currentFib = 1
		for iteration in xrange(1,n):
			# The next Fib number will be sum of currentFib and previousFib
			nextFib = previousFib + currentFib
			# print "nextFib: ", nextFib
			# Save these value
			previousFib = currentFib
			currentFib = nextFib
	return currentFib


def testFib(n):
	for i in range(n+1):
		print ('fib of', i, '=', iteratativeFibonacci(i))

testFib(5)