# Test if a number is prime.

def isPrime(n):
	"""
		Tests if a positive integer n is prime,
		returns true if n is prime, else False.
	"""
	# if n is less than equal to 3, it is prime.
	if n <= 3:
		if n == 2 or n == 3:
			return True
		else:
			return False
	#otherwise
	else:
		# check divisor between 2 and sqrt(n)
		for divisior in range(2,int(n ** 0.5) + 1):
			# If the divisor is even, 
			if (n % divisior) == 0 :
				return False
		return True


print "isPrime(121) : ", isPrime(121)