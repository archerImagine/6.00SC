name = "Mitch"
print "name: ", name
print "name[0]: ", name[0]

for i in name:
	print i

#name[0]	 = "A"

print "name: ", name
print "name[1:3]: ", name[1:3]		#print it
print "name[:2]: ", name[:2]		#print Mi
print "name[1:]: ", name[1:]		#print itch
print "name[:-1]: ", name[:-1]		#print Mitc

print "len(name): ", len(name)

print "name.upper(): ", name.upper()						#print MITCH
print "name.lower(): ", name.lower()						#print mitch
print "name.find('i'): ", name.find('i')					#print 1
print "name.replace('X', 'P'): ", name.replace('X', 'P')	#print Mitch
print "name.replace('M', 'P'): ", name.replace('M', 'P')	#print Pitch

print "dir(str): ", dir(str)
print "help(str): ", help(str)