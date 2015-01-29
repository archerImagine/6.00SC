def makePerson(name,age,height,weight):
	person = {}
	person['name'] = name
	person['age'] = age
	person['height'] = height
	person['weight'] = weight
	return person

def getName(person):
	return person['name']

def setName(person,name):
		person['name'] = name

def getAge(person):
	return person['age']	

def setAge(person,age):
	person['age'] = age		

def getHeight(person):
	return person['height']	

def setHeight(person,height):
	person['height'] = height

def getWeight(person):
	return person['weight']	

def setWeight(person,weight):
		person['weight'] = weight	
def printPerson(person):
	print 'Name: ', getName(person)," Age: ", getAge(person)," height: ", getHeight(person), " weight: ", getWeight(person)

def equalPerson(person1,person2):
	return getName(person1) == getName(person2)

mitch = makePerson('Mitch',32,70,200)	
Sarina = makePerson('Sarina',25,65,130)	

printPerson(mitch)
printPerson(Sarina)

setAge(mitch,25)
printPerson(mitch)

#The below code will return <type 'dict'>
print "type(mitch): ", type(mitch)

# notAPerson = {'RandomJunk':'Junk','Junk' : 'RandomJunk'}
# printPerson(notAPerson)

print "equalPerson(mitch,Sarina): ", equalPerson(mitch,Sarina)