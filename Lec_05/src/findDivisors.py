x = 100
divisors = ()

for i in range(1,x):
	if x % i == 0:
		divisors = divisors + (i,)

print "divisors: ", divisors

print "divisors[1:3]: ", divisors[1:3]