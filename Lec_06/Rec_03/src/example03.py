LA = [6.00,'MIT',600,600]
print "LA: ", LA

LA.append('Harvard')
print "LA: LA.append('Harvard'): ", LA

LA.append(['Yale','Standford'])
print "LA: LA.append(['Yale','Standford']): ", LA

LA.pop()
print "LA: LA.pop(): ", LA

LA.pop(0)
print "LA: LA.pop(0)", LA

LA.extend(['Yale','Standford'])
print "LA: LA.extend(['Yale','Standford']): ", LA

LA.remove(600)
print "LA: LA.remove(600): ", LA

LA.remove(600)
print "LA: LA.remove(600): ", LA

#LA.remove(500) #error: ValueError: list.remove(x): x not in list

if 500 in LA:
	LA.remove(500)


LA.sort()	
print "LA: LA.sort(): ", LA