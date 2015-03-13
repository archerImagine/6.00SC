import random

def chooseDoor():
    return random.choice([1,2,3])

def playMontyHall(numTrails = 1000):
    stayWins = 0
    switchWins = 0
    for trails in range(numTrails):
        prizeDoor = chooseDoor()    
        playerDoor = chooseDoor()
        if prizeDoor == playerDoor:
            stayWins += 1
        elif prizeDoor != playerDoor:
            switchWins += 1
    print "Stay Wins: ", stayWins/float(numTrails)
    print "Switch Wins: ", switchWins/float(numTrails)

playMontyHall()    