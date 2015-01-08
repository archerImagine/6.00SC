x = 0.0

numIter = 100000

for i in range(numIter):
	x += 0.1

print "x: "	, x
print "repr(x): ", repr(x)
print 10.0 * x == numIter
print "repr(10.0 * x): ", repr(10.0 * x)


# Do this to check equality of floating Point.
def close(x,y,epsilon=0.00001):
	return abs(x-y) < epsilon


if close(10.0 * x, numIter):
		print "Good Enough"	
