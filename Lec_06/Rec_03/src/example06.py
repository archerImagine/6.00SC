##Dictionaries

staff = {
	'Mitchell' 	: 'mizhi@mit.edu',
	'Ryan'		: 'rwx@mit.edu',
	'Sarina'	: 'Sarina@mit.edu'
}

print "staff: ", staff, " len(staff): ", len(staff)

# Made a mistake, Fix Ryan's address
staff['Ryan'] = 'rwj@mid.edu'

#Add Heymian
staff['Heymian'] = 'heymian@mit.edu'

if 'Heymian' in staff:
	print "Heymian in Staff"

if 'Gartbee' not in staff:
		print 'Adding Gartbee to the staff list'
		staff['Gartbee'] = 'gartbee@mit.edu'

print 'rvj@mit.edu' in staff

print staff

# One way to order alphabetically
staff.keys().sort() #will not sort
print staff

#Oops we fired Sarina
del staff['Sarina']
print staff

# Go Through key,value pair

for TA,Email in staff.items(): # staff.items() returns a key,value pairs
	print "TA: ", TA, " his mailid ", Email


#sorted Dictionaries

keys = staff.keys()	

keys.sort()

for k in keys:
	print k, staff[k]