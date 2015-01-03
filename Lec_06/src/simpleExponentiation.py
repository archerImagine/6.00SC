def simpleExponentiation(b,n):
	if n == 0 :
		return 1
	else:
		return b * simpleExponentiation(b,n-1)


print "simpleExponentiation(5,3): ", simpleExponentiation(5,3)