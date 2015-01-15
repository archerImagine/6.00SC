def factorial(n):
	assert n >= 0
	if n <= 1:
		return n
	else:
		return n * factorial(n - 1)

print factorial(5)

