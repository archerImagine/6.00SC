# Factorial computation.
def f(n):
	assert n >= 0
	answer = 1
	while n > 1:
		answer *= n
		n -= 1
	return answer

print "f(5)", f(5)	