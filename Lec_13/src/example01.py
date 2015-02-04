import random

class Location(object):
	def __init__(self, x,y):
		"""x and y are float"""
		self.x = x
		self.y = y
	def move(self,deltaX,deltaY):
		"""deltaX and deltaY are float"""
		return Location(self.x + deltaX, self.y + deltaY)
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def distFrom(self,other):
		ox = other.x
		oy = other.y
		xDist = self.x - ox
		yDist = self.y - oy
		return (xDist**2 + yDist**2) ** 0.5
	def __str__(self):
		return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
		def __init__(self):
			self.drunks = {}
		def addDrunk(self,drunk,loc):
			if drunk in self.drunks:
				raise ValueError('Duplicate Drunk')
			else:
				self.drunks[drunk] = loc
		def moveDrunk(self,drunk):
			if not drunk in self.drunks:
				raise ValueError('Drunk not in field')
			xDist,yDist = drunk.takeStep()
			self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
		def getLoc(self, drunk):
			if not drunk in self.drunks:
				raise ValueError('Drunk not in field')
			return self.drunks[drunk]

class Drunk(object):
	def __init__(self, name):
		self.name = name
	def takeStep(self):
		stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
		return random.choice(stepChoices)
	def __str__(self):
		return 'This drunk is named ' + self.name

def walk(f, d, numSteps):
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return(start.distFrom(f.getLoc(d)))

# def simWalks(numSteps, numTrials):
# 	homer = Drunk('Homer')
# 	origin = Location(0, 0)
# 	distances = []
# 	for t in range(numTrials):
# 		f = Field()
# 		f.addDrunk(homer, origin)
# 		distances.append(walk(f, homer, numTrials)) #this argument is wrong
# 	return distances

def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances


def drunkTest(numTrials):
	for numSteps in [10, 100, 1000, 10000, 100000]:
	# for numSteps in [0,1]:
		distances = simWalks(numSteps, numTrials)
		print 'Random walk of ' + str(numSteps) + ' steps'
		print '  Mean =', sum(distances)/len(distances)
		print '  Max =', max(distances), 'Min =', min(distances)
				
homer = Drunk("homer")
origin = Location(0,0)
field = Field()
field.addDrunk(homer,origin)
print "walk(field,homer,10): ", walk(field,homer,10)

drunkTest(10)