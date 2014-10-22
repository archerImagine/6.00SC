#!/usr/bin/env python

x = int(raw_input('Enter an integer: '))
for ans in range(0, abs(x)+1):
	if ans == 3:
		break
	else:
		print ans

for ans in range(1,10):
		for x in xrange(1,10):
			print "ans: ", ans, " x " , x
			if x == 3:
				break
		print "Iteration : ", ans, " Completed"
		print "ans: ", ans