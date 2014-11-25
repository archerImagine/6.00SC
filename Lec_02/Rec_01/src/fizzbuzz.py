for i in range(1,101):
	s = str(i)
	if i % 3 == 0 or i % 5 ==0 :
		s = ""
		if i % 3 == 0:
			s = s + 'Fizz'
		if i % 5 == 0:
			s = s + 'Buzz'
	print s