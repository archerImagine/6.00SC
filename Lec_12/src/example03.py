def g(): 
    print("A")
    yield 1
    print("B")
    yield 2

iterable = g()
print("Getting first value")
print(next(iterable))
print("Getting second value")
print(next(iterable))
print("Done")
next(iterable)