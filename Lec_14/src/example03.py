import random

def rollDie():
	"""returns a random int between 1 and 6"""
	return random.choice([1,2,3,4,5,6])

# def testRoll(n = 10):
# 	result = ''	
# 	for x in range(n):
# 		result = result + str(rollDie())
# 	print(result)

def checkPascal(numTrials = 1000):
	yes = 0.0
	for i in range(numTrials):
		for j in range(24):
			d1 = rollDie()
			d2 = rollDie()
			if d1 == 6 and d2 == 6:
				yes += 1
				break
	print 'Probability of losing = ' + str(1.0 - yes/numTrials)

checkPascal()	