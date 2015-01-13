def h(x):
	assert type(x) == int and x >= 0
	answer = 0
	s = str(x)
	for c in s:
		answer += int(c)
	return answer


print h(556)			