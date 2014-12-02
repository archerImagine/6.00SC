tupleOfNumber = (3.14,2,1,-100,240)
tupleOfString = ("What", "is","my","name?")

print "tupleOfNumber: ", tupleOfNumber
print "tupleOfString: ", tupleOfString

print "tupleOfNumber[0]: ", tupleOfNumber[0]
print "tupleOfString[0]: ", tupleOfString[0]
print "tupleOfString[-1]: ", tupleOfString[-1]
#print "tupleOfString[4]: ", tupleOfString[4]

print "len(tupleOfString): ", len(tupleOfString)

tupleOfMixed = (3.14, 'is', 'an imperfect', 'representation')
print "tupleOfMixed: ", tupleOfMixed

tupleOfTuple = (("astuff", "just"), 'got', 'real')
print "tupleOfTuple: ", tupleOfTuple
print "tupleOfTuple[0]: ", tupleOfTuple[0]
print "len(tupleOfTuple): ", len(tupleOfTuple)

#tupleOfNumber[1] = 3

print "tupleOfNumber: ", tupleOfNumber
print "tupleOfNumber[1:3]: ", tupleOfNumber[1:3]
print "tupleOfNumber[:2]: ", tupleOfNumber[:2]
print "tupleOfNumber[1:]: ", tupleOfNumber[1:]
print "tupleOfNumber[:-1]: ", tupleOfNumber[:-1]

for i in tupleOfNumber:
	print i

print "Before Modification: ", tupleOfNumber
tupleOfNumber = tupleOfNumber + (100,24)
print "After Modification: ", tupleOfNumber

oopsie = (50)
print "oopsie: ", oopsie

onsie = (50,)
print "onsie: ", onsie