import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,2,3,4])
pylab.figure(2)
pylab.plot([1,4,2,3], [5,6,7,8])
pylab.savefig('firstSaved')
pylab.figure(1)
pylab.plot([5,6,7,10])
pylab.savefig('secondSaved')

pylab.show()