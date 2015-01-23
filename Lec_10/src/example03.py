def readVal(valType,requestMsg,errorMsg):
	numTries = 0
	print numTries
	while numTries < 4:
		val = raw_input(requestMsg)
		try:
			val = valType(val)
			return val
		except ValueError:
			print errorMsg
			numTries += 1		
	raise TypeError('Num tries excedded.')


print readVal(int,"Enter int: ","Not a Int")	

try:
	a = readVal(int,"Enter int: ","Not a Int")
	print "a: ", a
except TypeError, s:
	print "s: ", s