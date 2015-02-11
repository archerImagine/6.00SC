import random

def flipCoin(numFlips):
	heads = 0
	for i in range(numFlips):
		if random.random() < 0.5:
			heads += 1
	return heads/float(numFlips)

print "Flip 100 times"
for i in range(10):
	print "CoinFlip i = ", i," flipCoin(100): ",flipCoin(100)	

print "Flip 1000000 times"
for i in range(10):
	print "CoinFlip i = ", i," flipCoin(1000000): ",flipCoin(1000000)		