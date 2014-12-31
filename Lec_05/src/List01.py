Techs = ['MIT','Cal Tech']
Ivys = ['Harvard','Yale','Brown']

Univs = []
Univs.append(Techs)				#Modifes the original List

print "Univs: ", Univs
print "len(Univs): ", len(Univs)

Univs.append(Ivys) 				#Modifes the original List
print "Univs: ", Univs
print "len(Univs): ", len(Univs)
for e in Univs:
	print "e: ", e


Flat = Techs + Ivys
print "Flat: ", Flat
print "len(Flat): ", len(Flat)

artSchools = ['RISD', 'Harvard']

for u2 in artSchools:
	if u2 in Flat:
		Flat.remove(u2)

print "Flat: ", Flat

Flat.sort()		
print "SORTED Flat: ", Flat

Flat[1] = 'UMass'
print "Flat: ", Flat