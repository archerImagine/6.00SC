#!/usr/bin/env python

# find the square root of a number

x = int(raw_input("Enter a Number to Find its Square Root: "))
epsilon = 0.01
numOfGuesses = 0
ans = 0

while abs(ans**2 - x) > epsilon and ans <= x:
	ans += 0.00001
	numOfGuesses += 1
print "Number of Guess: ", numOfGuesses
if abs(ans ** 2 - x) >= epsilon:
	print "Failed to find Square Root"
else:
	print ans, " is close to square root of ", x
		
