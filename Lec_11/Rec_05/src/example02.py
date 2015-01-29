class Person(object):
	def __init__(self, name,age,height,weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	# This type of method is called accessor (or getter)
	def getName(self):
		return self.name

	# This type of method is called mutator (or setter)	
	def setName(self,name):
		self.name = name

	# This type of method is called accessor (or getter)
	def getAge(self):
		return self.age

	# This type of method is called mutator (or setter)	
	def setAge(self,age):
		self.age = age

	# This type of method is called accessor (or getter)
	def getHeight(self):
		return self.height

	# This type of method is called mutator (or setter)	
	def setHeight(self,height):
		self.height = height

	# This type of method is called accessor (or getter)
	def getWeight(self):
		return self.weight

	# This type of method is called mutator (or setter)	
	def setWeight(self,weight):
		self.weight = weight		


	# UnderBar methods have special significance in python
	def __str__(self):
		return 'Name: ' +self.name +' Age: ' + str(self.age) +' height: '+str(self.height)+' weight: '+str(self.weight)

	def __eq__(self,other):
		return self.name == other.name


mitch = Person("Mitch",32,70,300)		
sarina = Person("sarina",25,65,130)

print mitch
print sarina

mitch.setAge(25)
print mitch

print "type(mitch): ", type(mitch)

print "mitch == sarina: ", mitch == sarina

print "mitch.getAge(): ", mitch.getAge()
print "Person.getAge(mitch): ", Person.getAge(mitch) # Here mitch becomes the self parameter of Person