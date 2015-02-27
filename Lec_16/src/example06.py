import random

def integrate(a, b, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        pinSum += f(random.uniform(a, b))
    average = pinSum/numPins
    return average*(b - a)

def one(x):
    return 1.0

print integrate(0, 8, one, 100000)

import math
print integrate(0, 8, math.sin, 1000000)    