L1 = [2]
L2 = [L1,L1]

print "L2: ", L2

L1[0] = 3

print "L2: ", L2

L2[0] = 'a'
print "L2: ", L2

L1 = [2]
print "L2: ", L2

del L1[0]
print "L2: --", L2, " L1: ", L1
print "-------------"


L1 = [2]
L2 = [L1, L1]
print 'L2 =', L2
L1[0] = 3
print 'L2 =', L2
L2[0] = 'a'
print 'L2 =', L2
print "-------------"

L1 = [2]
print 'L1 =', L1
print 'L2 =', L2
L2 = L1
L2[0] = 'a'
print 'L1 =', L1
print 'L2 =', L2

L1 = [2]
L2 = L1[:]
L2[0] = 'a'
print 'L1 =', L1
