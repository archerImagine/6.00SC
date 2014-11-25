#!/usr/bin/env python

# find the square root of a number using bisection search

x = float(raw_input("Enter a Number to find the square root: "))
epsilon = 0.01
numOfGuesses = 0
low = 0
high = x
ans = (low + high)/2.0

while abs(ans**2 - x) > epsilon and ans <= x:
	print "LOW: ", low, " HIGH: ", high, " ANS: ", ans
	numOfGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (low + high)/2.0

print 'numOfGuesses =', numOfGuesses	
print ans, 'is close to square root of', x
	