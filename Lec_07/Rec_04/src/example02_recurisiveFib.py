# Fibonacci Series for recursion.


def recursiveFibonacci(n):
	"""
		A recursive fibonacci to find the nth fibonacci were
		n is a int > 0
	"""

	# Base Case: 0th fibonacci number is either 0 or 1
	if n == 0 or n == 1:
		return 1
	else:
		return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)
		

def testFib(n):
	for i in range(n+1):
		print ('fib of', i, '=', recursiveFibonacci(i))

testFib(5)