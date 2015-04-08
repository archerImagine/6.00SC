class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def dToB(n,numDigits):
    """
        requires : n is a natural number less than 2 ** numDigits 
        return : a binary string of length numDigits representing the
                decial number n 
    """
    assert type(n) == int and type(numDigits) == int and \
    n >= 0 and n < 2 ** numDigits
    bStr = ""
    while n > 0:
        bStr = (str(n%2)) + bStr
        n = n/2
    while numDigits - len(bStr) > 0:
        bStr = '0'+bStr
    return bStr

def getPset(Items):
    """ Generate a list of list representing the power set of Items """    
    numSubSet = 2 ** len(Items)
    templates = []
    for i in range(numSubSet):
        templates.append(dToB(i,len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

def chooseBet(pset,constarints,getVal,getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)    
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constarints and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet,bestVal)

def testBet():
    Items = buildItems()
    pset = getPset(Items)
    taken,val = chooseBet(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item


testBet()
