def fibonacci(x):
	"""assumes x an int >= 0
        Returns Fibonacci of x"""
	assert type(x) == int and x >=  0
	if x == 0 or x == 1:
		return 1
	else:
		return fibonacci(x-1) + fibonacci(x-2)



def testFib(n):
	for i in range(n+1):
		print ('fib of', i, '=', fibonacci(i))

testFib(5)