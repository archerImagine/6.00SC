#Implementing Multiplication using a Iterative approach

def IterativeMultiplication(m,n):
	if n == 0 or m == 0:
		return 0

	# Initialize variable to hold result
	result = 0
	if n >= 1:
		while n > 0:
			#Add m to the result n times
			result += m
			n -= 1
	elif n <= -1 :
		# n is negative, we we would increment n
		while n < 0:
			# Add -m to the result n times.
			result += -m
			n += 1

	return result


print "IterativeMultiplication(3,3): ", IterativeMultiplication(3,3)		
print "IterativeMultiplication(-3,2): ", IterativeMultiplication(-3,2)	
