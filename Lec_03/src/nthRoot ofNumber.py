#!/usr/bin/env python

# find the nth root of a number using bisection search

x = int(raw_input("Enter a Number to find the square root: "))
root = int(raw_input("Enter the nth root: "))
epsilon = 0.01
numOfGuesses = 0
low = 0
high = x
ans = (low + high)/2.0

while abs(ans**root - x) > epsilon and ans <= x:
	print "LOW: ", low, " HIGH: ", high, " ANS: ", ans
	numOfGuesses += 1
	if ans**root < x:
		low = ans
	else:
		high = ans
	ans = (low + high)/2.0

print 'numOfGuesses =', numOfGuesses	
print ans, 'is close to', root,  ' root of', x