def recursiveExponentiation(b,e):
	if e == 0:
		return 1
	else:
		return b * recursiveExponentiation(b,e-1)


print "recursiveExponentiation(3,0): ", recursiveExponentiation(3,0)		
print "recursiveExponentiation(3,2): ", recursiveExponentiation(3,2)		


def recursiveMultiplication(m,n):
	#Base Case
	if n == 0:
		return 0
	elif n >= 1 :
		return m + recursiveMultiplication(m,n-1)
	elif n <= -1 :
		return -m + recursiveMultiplication(m,n+1)



print "recursiveMultiplication(3,3): ", recursiveMultiplication(3,3)		
print "recursiveMultiplication(3,2): ", recursiveMultiplication(3,2)		
