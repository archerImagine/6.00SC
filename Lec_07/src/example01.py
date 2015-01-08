x = 0.0

numIter = 100000

for i in range(numIter):
	x += 0.1

print "x: "	, x
print "repr(x): ", repr(x)
print 10.0 * x == numIter
print "repr(10.0 * x): ", repr(10.0 * x)
		