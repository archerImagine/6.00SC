# How to make Factorial?

def Factorial(n):
	#if base case is true, what is the base case.
	if n == 0:
		return 1
	else:
		return n * Factorial(n-1)


#Test

print "Factorial(0): ", Factorial(0)		
print "Factorial(5): ", Factorial(5)		

#Can you write it using for loop

def loopFactorial(n):
	result = 1
	for x in range(2, n+1):
		result *= x
	return result


print "loopFactorial(5): ", loopFactorial(5)		
print "loopFactorial(0): ", loopFactorial(0)
print "loopFactorial(1): ", loopFactorial(1)
print "loopFactorial(2): ", loopFactorial(2)

print "loopFactorial(100): ", loopFactorial(100)